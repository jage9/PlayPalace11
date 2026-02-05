import asyncio
import json
import ssl
import types

import pytest

import network_manager as nm_mod
from certificate_prompt import CertificateInfo
from network_manager import NetworkManager


class DummyWebsocket:
    def __init__(self):
        self.closed = False

    async def close(self):
        self.closed = True


class DummyConfigManager:
    def __init__(self):
        self.set_calls = []
        self.trusted_entry = None

    def set_trusted_certificate(self, server_id, data):
        self.set_calls.append((server_id, data))
        self.trusted_entry = data

    def get_trusted_certificate(self, server_id):
        return self.trusted_entry


class DummyMainWindow:
    def __init__(self):
        self.server_id = "server-123"
        self.config_manager = DummyConfigManager()


PACKET_TO_HANDLER = {
    "authorize_success": "on_authorize_success",
    "speak": "on_server_speak",
    "play_sound": "on_server_play_sound",
    "play_music": "on_server_play_music",
    "play_ambience": "on_server_play_ambience",
    "stop_ambience": "on_server_stop_ambience",
    "add_playlist": "on_server_add_playlist",
    "start_playlist": "on_server_start_playlist",
    "remove_playlist": "on_server_remove_playlist",
    "get_playlist_duration": "on_server_get_playlist_duration",
    "menu": "on_server_menu",
    "request_input": "on_server_request_input",
    "clear_ui": "on_server_clear_ui",
    "game_list": "on_server_game_list",
    "disconnect": "on_server_disconnect",
    "update_options_lists": "on_update_options_lists",
    "open_client_options": "on_open_client_options",
    "open_server_options": "on_open_server_options",
    "table_create": "on_table_create",
    "pong": "on_server_pong",
    "chat": "on_receive_chat",
}


class RecordingMainWindow(DummyMainWindow):
    def __init__(self):
        super().__init__()
        self.calls = []
        self.connection_lost = 0
        for method in PACKET_TO_HANDLER.values():
            setattr(self, method, self._build_handler(method))

    def _build_handler(self, method_name):
        def handler(packet):
            self.calls.append((method_name, packet.get("type")))

        return handler

    def on_connection_lost(self):
        self.connection_lost += 1

    def add_history(self, *args, **kwargs):
        pass


@pytest.fixture(autouse=True)
def callafter_immediate(monkeypatch):
    monkeypatch.setattr(nm_mod.wx, "CallAfter", lambda func, *a, **k: func(*a, **k))


def make_certificate_info(**overrides):
    defaults = dict(
        host="example.com",
        common_name="Example",
        sans=("example.com",),
        issuer="CA",
        valid_from="2025",
        valid_to="2026",
        fingerprint="AA:BB",
        fingerprint_hex="AABB",
        pem="---",
        matches_host=True,
    )
    defaults.update(overrides)
    return CertificateInfo(**defaults)


def test_verify_pinned_certificate_accepts_matching():
    nm = NetworkManager(main_window=DummyMainWindow())
    nm._extract_peer_certificate = lambda ws: ("AABB", {}, "pem")  # type: ignore[attr-defined]
    nm._get_trusted_certificate_entry = lambda: {"fingerprint": "aabb"}  # type: ignore[attr-defined]
    ws = DummyWebsocket()
    asyncio.run(nm._verify_pinned_certificate(ws, "wss://example.com"))
    assert ws.closed is False


def test_verify_pinned_certificate_rejects_mismatch():
    nm = NetworkManager(main_window=DummyMainWindow())
    nm._extract_peer_certificate = lambda ws: ("FFFF", {}, "pem")  # type: ignore[attr-defined]
    nm._get_trusted_certificate_entry = lambda: {"fingerprint": "1111"}  # type: ignore[attr-defined]
    ws = DummyWebsocket()
    with pytest.raises(ssl.SSLError):
        asyncio.run(nm._verify_pinned_certificate(ws, "wss://example.com"))
    assert ws.closed is True


def test_store_and_get_trusted_certificate_round_trip():
    window = DummyMainWindow()
    nm = NetworkManager(main_window=window)
    info = make_certificate_info()

    nm._store_trusted_certificate(info)
    stored_server, stored_payload = window.config_manager.set_calls[0]
    assert stored_server == "server-123"
    assert stored_payload["fingerprint"] == "AABB"

    entry = nm._get_trusted_certificate_entry()
    assert entry["host"] == "example.com"


def test_store_trusted_certificate_noop_without_manager():
    class NoConfigWindow:
        server_id = None
        config_manager = None

    nm = NetworkManager(main_window=NoConfigWindow())
    nm._store_trusted_certificate(make_certificate_info())
    assert nm._get_trusted_certificate_entry() is None


def test_build_certificate_info_matches_host():
    nm = NetworkManager(main_window=DummyMainWindow())
    cert_dict = {
        "subject": ((("commonName", "example.com"),),),
        "issuer": ((("organizationName", "Example CA"),),),
        "subjectAltName": (("DNS", "example.com"), ("DNS", "alt.example.com")),
        "notBefore": "2025",
        "notAfter": "2026",
    }
    info = nm._build_certificate_info(cert_dict, "AABBCCDDEE1122", pem="", host="example.com")
    assert info.matches_host is True
    assert info.fingerprint == "AA:BB:CC:DD:EE:11:22"


def test_build_certificate_info_detects_hostname_mismatch():
    nm = NetworkManager(main_window=DummyMainWindow())
    cert_dict = {
        "subject": ((("commonName", "other.example.com"),),),
        "subjectAltName": (("DNS", "alt.example.com"),),
        "issuer": (),
        "notBefore": "",
        "notAfter": "",
    }
    info = nm._build_certificate_info(cert_dict, "ABCD", pem="", host="example.com")
    assert info.matches_host is False
    assert info.common_name == "other.example.com"


def test_get_server_host_parses_url():
    nm = NetworkManager(main_window=DummyMainWindow())
    assert nm._get_server_host("wss://playpalace.example:8443") == "playpalace.example"
    assert nm._get_server_host("not a url") == ""


def test_handle_packet_dispatches_to_main_window():
    window = RecordingMainWindow()
    nm = NetworkManager(main_window=window)
    for packet_type in PACKET_TO_HANDLER:
        nm._handle_packet({"type": packet_type})
    assert len(window.calls) == len(PACKET_TO_HANDLER)
    assert {name for name, _ in window.calls} == set(PACKET_TO_HANDLER.values())


def test_send_packet_requires_connection():
    nm = NetworkManager(main_window=RecordingMainWindow())
    assert nm.send_packet({"type": "ping"}) is False


def test_send_packet_submits_to_loop(monkeypatch):
    window = RecordingMainWindow()
    manager = NetworkManager(main_window=window)
    loop = asyncio.new_event_loop()
    manager.loop = loop
    manager.connected = True

    class DummyWebsocket:
        def __init__(self):
            self.messages = []

        def send(self, message):
            self.messages.append(message)

            async def _done():
                return None

            return _done()

    ws = DummyWebsocket()
    manager.ws = ws

    def fake_run_coroutine_threadsafe(coro, used_loop):
        assert used_loop is loop
        used_loop.run_until_complete(coro)

        class DummyFuture:
            def result(self, timeout=None):
                return None

        return DummyFuture()

    monkeypatch.setattr(asyncio, "run_coroutine_threadsafe", fake_run_coroutine_threadsafe)
    try:
        assert manager.send_packet({"type": "ping", "data": 1}) is True
    finally:
        loop.close()

    assert len(ws.messages) == 1
    payload = json.loads(ws.messages[0])
    assert payload["type"] == "ping"
    assert payload["data"] == 1


def test_send_packet_failure_notifies_window(monkeypatch):
    window = RecordingMainWindow()
    manager = NetworkManager(main_window=window)
    manager.connected = True
    manager.loop = asyncio.new_event_loop()
    manager.ws = object()

    def fail_run_coroutine_threadsafe(*_):
        raise RuntimeError("boom")

    monkeypatch.setattr(asyncio, "run_coroutine_threadsafe", fail_run_coroutine_threadsafe)
    try:
        assert manager.send_packet({"type": "ping"}) is False
    finally:
        manager.loop.close()

    assert manager.connected is False
    assert window.connection_lost == 1


def test_disconnect_waits_for_thread(monkeypatch):
    window = RecordingMainWindow()
    manager = NetworkManager(main_window=window)
    loop = asyncio.new_event_loop()
    manager.loop = loop
    manager.ws = DummyWebsocket()
    manager.connected = True

    class DummyThread:
        def __init__(self):
            self.join_called = False
            self.alive = True

        def is_alive(self):
            return self.alive

        def join(self, timeout=None):
            self.join_called = True
            self.alive = False

    dummy_thread = DummyThread()
    manager.thread = dummy_thread

    run_calls = []

    def fake_run_coroutine_threadsafe(coro, used_loop):
        used_loop.run_until_complete(coro)
        run_calls.append((coro, used_loop))

        class DummyFuture:
            def result(self, timeout=None):
                return None

        return DummyFuture()

    monkeypatch.setattr(asyncio, "run_coroutine_threadsafe", fake_run_coroutine_threadsafe)
    try:
        manager.disconnect(wait=True)
    finally:
        loop.close()

    assert manager.should_stop is True
    assert dummy_thread.join_called is True
    assert run_calls, "Websocket close coroutine should be scheduled"


def test_disconnect_without_thread(monkeypatch):
    manager = NetworkManager(main_window=RecordingMainWindow())
    manager.loop = asyncio.new_event_loop()
    manager.ws = DummyWebsocket()

    def fake_threadsafe(coro, used_loop):
        used_loop.run_until_complete(coro)

        class DummyFuture:
            def result(self, timeout=None):
                return None

        return DummyFuture()

    monkeypatch.setattr(asyncio, "run_coroutine_threadsafe", fake_threadsafe)
    try:
        manager.disconnect(wait=False)
    finally:
        manager.loop.close()

    assert manager.thread is None
