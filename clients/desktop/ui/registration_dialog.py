"""Registration dialog for Play Palace v9 client."""

import wx
import json
import asyncio
import logging
import threading
import websockets
import ssl
import sys
import hashlib
import os
import tempfile
from urllib.parse import urlparse
from pathlib import Path
from websockets.asyncio.client import connect

sys.path.insert(0, str(Path(__file__).parent.parent))
from constants import USERNAME_LENGTH_HINT, PASSWORD_LENGTH_HINT
from certificate_prompt import CertificatePromptDialog, CertificateInfo

LOG = logging.getLogger(__name__)

class RegistrationDialog(wx.Dialog):
    """Registration dialog for creating new accounts."""

    def __init__(self, parent, server_url, server_id=None):
        """Initialize the registration dialog."""
        super().__init__(parent, title="Create Play Palace Account", size=(500, 450))

        self.server_url = server_url
        self.server_id = server_id
        self._create_ui()
        self.CenterOnScreen()

    def _create_ui(self):
        """Create the UI components."""
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Title
        title = wx.StaticText(panel, label="Create New Account")
        title_font = title.GetFont()
        title_font.PointSize += 4
        title_font = title_font.Bold()
        title.SetFont(title_font)
        sizer.Add(title, 0, wx.ALL | wx.CENTER, 10)

        # Info text
        info_text = wx.StaticText(
            panel,
            label="Your account will require admin approval before you can log in.",
        )
        sizer.Add(info_text, 0, wx.ALL | wx.CENTER, 5)

        # Username
        username_label = wx.StaticText(panel, label="&Username:")
        sizer.Add(username_label, 0, wx.LEFT | wx.TOP, 10)

        self.username_input = wx.TextCtrl(panel)
        sizer.Add(self.username_input, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        username_help = wx.StaticText(
            panel,
            label="Letters, numbers, underscores, and dashes only. "
            + USERNAME_LENGTH_HINT,
        )
        username_help.SetForegroundColour(wx.Colour(100, 100, 100))
        sizer.Add(username_help, 0, wx.LEFT | wx.RIGHT, 10)

        # Email
        email_label = wx.StaticText(panel, label="&Email:")
        sizer.Add(email_label, 0, wx.LEFT | wx.TOP, 10)

        self.email_input = wx.TextCtrl(panel)
        sizer.Add(self.email_input, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Password
        password_label = wx.StaticText(panel, label="&Password:")
        sizer.Add(password_label, 0, wx.LEFT | wx.TOP, 10)

        self.password_input = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        sizer.Add(self.password_input, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        password_help = wx.StaticText(panel, label=PASSWORD_LENGTH_HINT)
        password_help.SetForegroundColour(wx.Colour(100, 100, 100))
        sizer.Add(password_help, 0, wx.LEFT | wx.RIGHT, 10)

        # Confirm Password
        confirm_label = wx.StaticText(panel, label="&Confirm Password:")
        sizer.Add(confirm_label, 0, wx.LEFT | wx.TOP, 10)

        self.confirm_input = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        sizer.Add(self.confirm_input, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Bio
        bio_label = wx.StaticText(panel, label="&Bio:")
        sizer.Add(bio_label, 0, wx.LEFT | wx.TOP, 10)

        self.bio_input = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(0, 80))
        sizer.Add(self.bio_input, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        bio_help = wx.StaticText(panel, label="Tell us a bit about yourself")
        bio_help.SetForegroundColour(wx.Colour(100, 100, 100))
        sizer.Add(bio_help, 0, wx.LEFT | wx.RIGHT, 10)

        # Buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.register_btn = wx.Button(panel, label="&Register")
        self.register_btn.SetDefault()
        button_sizer.Add(self.register_btn, 0, wx.RIGHT, 5)

        cancel_btn = wx.Button(panel, wx.ID_CANCEL, "&Cancel")
        button_sizer.Add(cancel_btn, 0)

        sizer.Add(button_sizer, 0, wx.ALL | wx.CENTER, 10)

        # Set sizer
        panel.SetSizer(sizer)

        # Bind events
        self.register_btn.Bind(wx.EVT_BUTTON, self.on_register)
        cancel_btn.Bind(wx.EVT_BUTTON, self.on_cancel)

        # Set focus
        self.username_input.SetFocus()

    def on_register(self, event):
        """Handle register button click."""
        username = self.username_input.GetValue().strip()
        email = self.email_input.GetValue().strip()
        password = self.password_input.GetValue()
        confirm = self.confirm_input.GetValue()
        bio = self.bio_input.GetValue().strip()

        # Validate fields
        if not username:
            wx.MessageBox("Please enter a username", "Error", wx.OK | wx.ICON_ERROR)
            self.username_input.SetFocus()
            return

        if not email:
            wx.MessageBox(
                "Please enter an email address", "Error", wx.OK | wx.ICON_ERROR
            )
            self.email_input.SetFocus()
            return

        if not password:
            wx.MessageBox("Please enter a password", "Error", wx.OK | wx.ICON_ERROR)
            self.password_input.SetFocus()
            return

        if password != confirm:
            wx.MessageBox("Passwords do not match", "Error", wx.OK | wx.ICON_ERROR)
            self.confirm_input.SetFocus()
            return

        if not bio:
            wx.MessageBox("Please enter a bio", "Error", wx.OK | wx.ICON_ERROR)
            self.bio_input.SetFocus()
            return

        # Disable button during registration
        self.register_btn.Enable(False)

        # Send registration to server
        self._send_registration(username, email, password, bio)

    def _send_registration(self, username, email, password, bio):
        """Send registration packet to server."""
        # Run in a thread to avoid blocking UI
        thread = threading.Thread(
            target=self._register_thread,
            args=(username, email, password, bio),
            daemon=True,
        )
        thread.start()

    def _register_thread(self, username, email, password, bio):
        """Thread to handle registration."""
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(
                self._send_register_packet(username, email, password, bio)
            )
            loop.close()

            # Show result on main thread
            wx.CallAfter(self._show_registration_result, result)
        except Exception as e:
            wx.CallAfter(self._show_registration_result, f"Connection error: {str(e)}")

    async def _send_register_packet(self, username, email, password, bio):
        """Send registration packet and wait for response."""
        try:
            ws = await self._open_connection(self.server_url)
            if not ws:
                return "TLS certificate was not trusted; connection aborted."

            try:
                # Send registration packet
                await ws.send(
                    json.dumps(
                        {
                            "type": "register",
                            "username": username,
                            "email": email,
                            "password": password,
                            "bio": bio,
                        }
                    )
                )

                # Wait for response (server will send a "speak" message)
                message = await asyncio.wait_for(ws.recv(), timeout=5.0)
                data = json.loads(message)

                if data.get("type") == "speak":
                    return data.get("text", "Registration successful")
                else:
                    return "Unexpected response from server"
            finally:
                try:
                    await ws.close()
                except (OSError, RuntimeError, websockets.exceptions.ConnectionClosed) as exc:
                    LOG.debug("Failed to close registration websocket: %s", exc)

        except asyncio.TimeoutError:
            return "Server did not respond in time"
        except Exception as e:
            return f"Error: {str(e)}"

    def _build_default_ssl_context(self) -> ssl.SSLContext:
        context = ssl.create_default_context()
        context.check_hostname = True
        context.verify_mode = ssl.CERT_REQUIRED
        return context

    async def _open_connection(self, server_url: str):
        if not server_url.startswith("wss://"):
            return await connect(server_url)

        try:
            websocket = await connect(server_url, ssl=self._build_default_ssl_context())
            await self._verify_pinned_certificate(websocket)
            return websocket
        except ssl.SSLCertVerificationError:
            websocket = await self._handle_tls_failure(server_url)
            if websocket:
                return websocket
            return None

    async def _handle_tls_failure(self, server_url: str):
        trust_entry = self._get_trusted_certificate_entry()
        if trust_entry:
            return await self._connect_with_trusted_certificate(server_url, trust_entry)

        cert_info = await self._fetch_certificate_info(server_url)
        if not cert_info:
            return None

        if not self._prompt_trust_decision(cert_info):
            return None

        self._store_trusted_certificate(cert_info)
        trust_entry = self._get_trusted_certificate_entry()
        if not trust_entry:
            return None
        return await self._connect_with_trusted_certificate(server_url, trust_entry)

    async def _connect_with_trusted_certificate(self, server_url: str, trust_entry: dict):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        websocket = await connect(server_url, ssl=context)
        await self._verify_pinned_certificate(websocket, trust_entry)
        return websocket

    async def _verify_pinned_certificate(self, websocket, trust_entry: dict | None = None):
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
                except (OSError, RuntimeError, websockets.exceptions.ConnectionClosed) as exc:
                    LOG.debug("Failed to close TLS probe websocket: %s", exc)

    def _prompt_trust_decision(self, cert_info: CertificateInfo) -> bool:
        decision = {"trust": False}
        done = threading.Event()

        def _show_dialog():
            dlg = CertificatePromptDialog(self, cert_info)
            result = dlg.ShowModal()
            dlg.Destroy()
            decision["trust"] = result == wx.ID_OK
            done.set()

        wx.CallAfter(_show_dialog)
        done.wait()
        return decision["trust"]

    def _store_trusted_certificate(self, cert_info: CertificateInfo) -> None:
        manager = getattr(self.GetParent(), "config_manager", None)
        server_id = self.server_id or getattr(self.GetParent(), "server_id", None)
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
        manager = getattr(self.GetParent(), "config_manager", None)
        server_id = self.server_id or getattr(self.GetParent(), "server_id", None)
        if not manager or not server_id:
            return None
        return manager.get_trusted_certificate(server_id)

    def _extract_peer_certificate(self, websocket):
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
        cert_dict = self._merge_certificate_dict(cert_dict, pem)
        common_name = self._extract_common_name(cert_dict.get("subject", []))
        issuer_text = self._format_issuer(cert_dict.get("issuer", []))
        sans = self._extract_sans(cert_dict)
        matches = self._host_matches(common_name, sans, host)
        display_fp = self._format_fingerprint(fingerprint_hex)
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

    def _merge_certificate_dict(self, cert_dict, pem: str) -> dict:
        cert_dict = cert_dict or {}
        if not pem or (cert_dict and "notBefore" in cert_dict and "notAfter" in cert_dict):
            return cert_dict
        decoded = self._decode_certificate_dict(pem)
        if not decoded:
            return cert_dict
        merged = dict(decoded)
        for key, value in cert_dict.items():
            if value:
                merged[key] = value
        return merged

    def _extract_common_name(self, subject) -> str:
        for entry in subject:
            for key, value in entry:
                if key == "commonName":
                    return value
        return ""

    def _format_issuer(self, issuer_entries) -> str:
        issuer = [
            "=".join(entry_part[1] for entry_part in entry)
            for entry in issuer_entries
        ]
        return ", ".join(issuer) if issuer else "(unknown)"

    def _extract_sans(self, cert_dict) -> list[str]:
        return [
            value
            for kind, value in cert_dict.get("subjectAltName", [])
            if kind == "DNS"
        ]

    def _host_matches(self, common_name: str, sans: list[str], host: str) -> bool:
        host_lower = (host or "").lower()
        if not host_lower:
            return False
        if common_name.lower() == host_lower:
            return True
        return any(san.lower() == host_lower for san in sans)

    def _format_fingerprint(self, fingerprint_hex: str) -> str:
        return ":".join(
            fingerprint_hex[i : i + 2] for i in range(0, len(fingerprint_hex), 2)
        )

    def _get_server_host(self, server_url: str) -> str:
        try:
            return urlparse(server_url).hostname or ""
        except Exception:
            return ""

    def _show_registration_result(self, message):
        """Show registration result to user."""
        self.register_btn.Enable(True)

        # Check if it was successful
        if "successfully" in message.lower() or "approval" in message.lower():
            wx.MessageBox(
                message, "Registration Successful", wx.OK | wx.ICON_INFORMATION
            )
            self.EndModal(wx.ID_OK)
        else:
            wx.MessageBox(message, "Registration Failed", wx.OK | wx.ICON_ERROR)

    def on_cancel(self, event):
        """Handle cancel button click."""
        self.EndModal(wx.ID_CANCEL)
