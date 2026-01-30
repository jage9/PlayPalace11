"""Network manager for WebSocket communication with server."""

import asyncio
import json
import threading
import hashlib
import os
import tempfile
from urllib.parse import urlparse

import wx
import websockets
import ssl
from websockets.asyncio.client import connect

from certificate_prompt import CertificatePromptDialog, CertificateInfo


class TLSUserDeclinedError(Exception):
    """Raised when the user declines to trust a presented TLS certificate."""

    pass


class NetworkManager:
    """Manages WebSocket connection to Play Palace server."""

    def __init__(self, main_window):
        """
        Initialize network manager.

        Args:
            main_window: Reference to MainWindow for callbacks
        """
        self.main_window = main_window
        self.ws = None
        self.connected = False
        self.username = None
        self.thread = None
        self.loop = None
        self.should_stop = False
        self.server_url = None
        self.server_id = None

    def connect(self, server_url, username, password):
        """
        Connect to server.

        Args:
            server_url: WebSocket URL (e.g., "ws://localhost:8000")
            username: Username for authorization
            password: Password for authorization
        """
        try:
            # Wait for old thread to finish if it exists
            if self.thread and self.thread.is_alive():
                self.should_stop = True
                # Wait up to 2 seconds for thread to finish
                self.thread.join(timeout=2.0)

            self.username = username
            self.should_stop = False
            self.server_url = server_url
            self.server_id = getattr(self.main_window, "server_id", None)

            # Start async thread
            self.thread = threading.Thread(
                target=self._run_async_loop,
                args=(server_url, username, password),
                daemon=True,
            )
            self.thread.start()

            return True
        except Exception:
            import traceback

            traceback.print_exc()
            return False

    def _run_async_loop(self, server_url, username, password):
        """Run the async event loop in a thread."""
        try:
            # Create new event loop for this thread
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)

            # Run the connection coroutine
            self.loop.run_until_complete(
                self._connect_and_listen(server_url, username, password)
            )
        except Exception:
            import traceback

            traceback.print_exc()
        finally:
            self.loop.close()

    async def _connect_and_listen(self, server_url, username, password):
        """Connect to server and listen for messages."""
        websocket = None
        try:
            websocket = await self._open_connection(server_url)
            self.ws = websocket
            self.connected = True

            await self._send_authorize(websocket, username, password)

            while not self.should_stop:
                try:
                    message = await asyncio.wait_for(websocket.recv(), timeout=1.0)
                    packet = json.loads(message)
                    wx.CallAfter(self._handle_packet, packet)
                except asyncio.TimeoutError:
                    continue
                except websockets.exceptions.ConnectionClosed:
                    break
        except TLSUserDeclinedError:
            wx.CallAfter(
                self.main_window.add_history,
                "TLS certificate was not trusted; connection aborted.",
                "activity",
            )
        except Exception:
            import traceback

            traceback.print_exc()
        finally:
            self.connected = False
            self.ws = None
            if websocket:
                try:
                    await websocket.close()
                except Exception:
                    pass
            if not self.should_stop:
                wx.CallAfter(self.main_window.on_connection_lost)

    async def _send_authorize(self, websocket, username, password):
        """Send the authorize packet after connecting."""
        await websocket.send(
            json.dumps(
                {
                    "type": "authorize",
                    "username": username,
                    "password": password,
                    "major": 11,
                    "minor": 0,
                    "patch": 0,
                }
            )
        )

    async def _open_connection(self, server_url: str):
        """Open a websocket connection, handling TLS verification."""
        if not server_url.startswith("wss://"):
            return await connect(server_url)

        try:
            websocket = await connect(server_url, ssl=self._build_default_ssl_context())
            await self._verify_pinned_certificate(websocket, server_url)
            return websocket
        except ssl.SSLCertVerificationError:
            websocket = await self._handle_tls_failure(server_url)
            if websocket:
                return websocket
            raise

    def _build_default_ssl_context(self) -> ssl.SSLContext:
        context = ssl.create_default_context()
        context.check_hostname = True
        context.verify_mode = ssl.CERT_REQUIRED
        return context

    async def _handle_tls_failure(self, server_url: str):
        """Recover from TLS verification failure (self-signed certs)."""
        trust_entry = self._get_trusted_certificate_entry()
        if trust_entry:
            return await self._connect_with_trusted_certificate(server_url, trust_entry)

        cert_info = await self._fetch_certificate_info(server_url)
        if not cert_info:
            return None

        if not self._prompt_trust_decision(cert_info):
            raise TLSUserDeclinedError("User declined to trust the certificate.")

        self._store_trusted_certificate(cert_info)
        trust_entry = self._get_trusted_certificate_entry()
        if not trust_entry:
            raise TLSUserDeclinedError("Unable to store trusted certificate.")
        return await self._connect_with_trusted_certificate(server_url, trust_entry)

    async def _connect_with_trusted_certificate(
        self, server_url: str, trust_entry: dict
    ):
        """Connect using a stored certificate fingerprint (TOFU)."""
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        websocket = await connect(server_url, ssl=context)
        await self._verify_pinned_certificate(websocket, server_url, trust_entry)
        return websocket

    async def _verify_pinned_certificate(
        self,
        websocket: websockets.WebSocketClientProtocol,
        server_url: str,
        trust_entry: dict | None = None,
    ):
        """Compare presented certificate fingerprint with stored metadata."""
        entry = trust_entry or self._get_trusted_certificate_entry()
        if not entry:
            return

        fingerprint_hex, _, _ = self._extract_peer_certificate(websocket)
        if not fingerprint_hex:
            raise ssl.SSLError("Unable to read peer certificate.")

        expected = entry.get("fingerprint", "").upper()
        if expected != fingerprint_hex.upper():
            await websocket.close()
            raise ssl.SSLError("Trusted certificate fingerprint mismatch.")

    async def _fetch_certificate_info(self, server_url: str) -> CertificateInfo | None:
        """Retrieve certificate information without enforcing trust."""
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        websocket = None
        try:
            websocket = await connect(server_url, ssl=context)
            fingerprint_hex, cert_dict, pem = self._extract_peer_certificate(websocket)
            if not fingerprint_hex or not pem:
                return None
            host = self._get_server_host(server_url)
            return self._build_certificate_info(cert_dict or {}, fingerprint_hex, pem, host)
        except Exception:
            return None
        finally:
            if websocket:
                try:
                    await websocket.close()
                except Exception:
                    pass

    def _prompt_trust_decision(self, cert_info: CertificateInfo) -> bool:
        """Show the trust dialog on the main thread."""
        decision = {"trust": False}
        done = threading.Event()

        def _show_dialog():
            dlg = CertificatePromptDialog(self.main_window, cert_info)
            result = dlg.ShowModal()
            dlg.Destroy()
            decision["trust"] = result == wx.ID_OK
            done.set()

        wx.CallAfter(_show_dialog)
        done.wait()
        return decision["trust"]

    def _store_trusted_certificate(self, cert_info: CertificateInfo) -> None:
        """Persist the trusted certificate metadata via ConfigManager."""
        manager = getattr(self.main_window, "config_manager", None)
        server_id = getattr(self.main_window, "server_id", None)
        if not manager or not server_id:
            return
        manager.set_trusted_certificate(
            server_id,
            {
                "fingerprint": cert_info.fingerprint_hex,
                "pem": cert_info.pem,
                "host": cert_info.host,
                "common_name": cert_info.common_name,
            },
        )

    def _get_trusted_certificate_entry(self) -> dict | None:
        manager = getattr(self.main_window, "config_manager", None)
        server_id = getattr(self.main_window, "server_id", None)
        if not manager or not server_id:
            return None
        return manager.get_trusted_certificate(server_id)

    def _extract_peer_certificate(self, websocket):
        """Return (hex fingerprint, decoded cert dict, PEM)."""
        if not websocket or not websocket.transport:
            return None, None, None
        ssl_obj = websocket.transport.get_extra_info("ssl_object")
        if not ssl_obj:
            return None, None, None
        der_bytes = ssl_obj.getpeercert(binary_form=True)
        cert_dict = ssl_obj.getpeercert()
        pem = None
        if der_bytes:
            pem = ssl.DER_cert_to_PEM_cert(der_bytes)

        if cert_dict is None and pem:
            cert_dict = self._decode_certificate_dict(pem)

        if not der_bytes or cert_dict is None:
            return None, cert_dict, None
        fingerprint_hex = hashlib.sha256(der_bytes).hexdigest().upper()
        return fingerprint_hex, cert_dict, pem

    def _decode_certificate_dict(self, pem: str) -> dict | None:
        """Decode certificate metadata from PEM when ssl.getpeercert() returns None."""
        tmp_path = None
        try:
            tmp = tempfile.NamedTemporaryFile("w", delete=False)
            tmp.write(pem)
            tmp.flush()
            tmp_path = tmp.name
            tmp.close()
            return ssl._ssl._test_decode_cert(tmp_path)
        except Exception:
            return None
        finally:
            if tmp_path:
                try:
                    os.unlink(tmp_path)
                except OSError:
                    pass

    def _build_certificate_info(
        self, cert_dict, fingerprint_hex: str, pem: str, host: str
    ) -> CertificateInfo:
        """Convert Python's SSL cert dict into CertificateInfo."""
        cert_dict = cert_dict or {}
        # Enrich metadata with fields parsed from PEM if they were missing
        if pem and (not cert_dict or "notBefore" not in cert_dict or "notAfter" not in cert_dict):
            decoded = self._decode_certificate_dict(pem)
            if decoded:
                merged = dict(decoded)
                # Preserve any values we already have, such as SAN entries that _test_decode_cert lacks
                for key, value in cert_dict.items():
                    if value:
                        merged[key] = value
                cert_dict = merged

        subject = cert_dict.get("subject", [])
        common_name = ""
        for entry in subject:
            for key, value in entry:
                if key == "commonName":
                    common_name = value
        issuer = []
        for entry in cert_dict.get("issuer", []):
            issuer.append("=".join(entry_part[1] for entry_part in entry))
        issuer_text = ", ".join(issuer) if issuer else "(unknown)"
        sans = [
            value for kind, value in cert_dict.get("subjectAltName", []) if kind == "DNS"
        ]
        matches = False
        host_lower = (host or "").lower()
        if host_lower:
            if common_name.lower() == host_lower:
                matches = True
            elif any(san.lower() == host_lower for san in sans):
                matches = True
        display_fp = ":".join(
            fingerprint_hex[i : i + 2] for i in range(0, len(fingerprint_hex), 2)
        )
        return CertificateInfo(
            host=host,
            common_name=common_name,
            sans=sans,
            issuer=issuer_text,
            valid_from=cert_dict.get("notBefore", ""),
            valid_to=cert_dict.get("notAfter", ""),
            fingerprint=display_fp,
            fingerprint_hex=fingerprint_hex,
            pem=pem,
            matches_host=matches,
        )

    def _get_server_host(self, server_url: str) -> str:
        try:
            return urlparse(server_url).hostname or ""
        except Exception:
            return ""

    def disconnect(self, wait=False, timeout=3.0):
        """
        Disconnect from server.

        Args:
            wait: If True, wait for the thread to fully stop
            timeout: Maximum time to wait for thread to stop (seconds)
        """
        self.should_stop = True
        self.connected = False

        # Close websocket if it exists
        if self.ws and self.loop:
            try:
                # Schedule close in the async loop
                asyncio.run_coroutine_threadsafe(self.ws.close(), self.loop)
            except Exception:
                pass  # Ignore errors during cleanup

        # Wait for thread to fully stop if requested
        if wait and self.thread and self.thread.is_alive():
            self.thread.join(timeout=timeout)

    def send_packet(self, packet):
        """
        Send packet to server.

        Args:
            packet: Dictionary to send as JSON
        """
        if not self.connected or not self.ws or not self.loop:
            return False

        try:
            message = json.dumps(packet)

            # Schedule send in the async loop
            asyncio.run_coroutine_threadsafe(self.ws.send(message), self.loop)
            return True
        except Exception:
            import traceback

            traceback.print_exc()
            self.connected = False
            wx.CallAfter(self.main_window.on_connection_lost)
            return False

    def _handle_packet(self, packet):
        """
        Handle incoming packet from server (called in main thread).

        Args:
            packet: Dictionary received from server
        """
        packet_type = packet.get("type")

        if packet_type == "authorize_success":
            self.main_window.on_authorize_success(packet)
        elif packet_type == "speak":
            self.main_window.on_server_speak(packet)
        elif packet_type == "play_sound":
            self.main_window.on_server_play_sound(packet)
        elif packet_type == "play_music":
            self.main_window.on_server_play_music(packet)
        elif packet_type == "play_ambience":
            self.main_window.on_server_play_ambience(packet)
        elif packet_type == "stop_ambience":
            self.main_window.on_server_stop_ambience(packet)
        elif packet_type == "add_playlist":
            self.main_window.on_server_add_playlist(packet)
        elif packet_type == "start_playlist":
            self.main_window.on_server_start_playlist(packet)
        elif packet_type == "remove_playlist":
            self.main_window.on_server_remove_playlist(packet)
        elif packet_type == "get_playlist_duration":
            self.main_window.on_server_get_playlist_duration(packet)
        elif packet_type == "menu":
            self.main_window.on_server_menu(packet)
        elif packet_type == "request_input":
            self.main_window.on_server_request_input(packet)
        elif packet_type == "clear_ui":
            self.main_window.on_server_clear_ui(packet)
        elif packet_type == "game_list":
            self.main_window.on_server_game_list(packet)
        elif packet_type == "disconnect":
            self.main_window.on_server_disconnect(packet)
        elif packet_type == "update_options_lists":
            self.main_window.on_update_options_lists(packet)
        elif packet_type == "open_client_options":
            self.main_window.on_open_client_options(packet)
        elif packet_type == "open_server_options":
            self.main_window.on_open_server_options(packet)
        elif packet_type == "table_create":
            self.main_window.on_table_create(packet)
        elif packet_type == "pong":
            self.main_window.on_server_pong(packet)
        elif packet_type == "chat":
            self.main_window.on_receive_chat(packet)
