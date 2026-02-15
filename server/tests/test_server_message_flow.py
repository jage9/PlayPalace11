"""Additional coverage for core.server message and auth flows."""

from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from collections import deque
from types import SimpleNamespace

import pytest

from server.core.server import Server
from server.core.state import ModeSnapshot, ServerMode
from server.core.users.base import TrustLevel
from server.auth.auth import AuthResult


class DummyClient:
    def __init__(self, address="9.9.9.9:1234"):
        self.address = address
        self.username = None
        self.authenticated = False
        self.sent: list[dict] = []
        self.closed = False

    async def send(self, payload):
        self.sent.append(payload)

    async def close(self):
        self.closed = True


class FakeAuth:
    def __init__(self):
        self.users: dict[str, SimpleNamespace] = {}
        self.sessions: dict[str, str] = {}
        self.refresh_payloads: dict[str, tuple] = {}

    def authenticate(self, username, password):
        # Treat any known user/password as success for tests
        if username in self.users and password == "secret":
            return AuthResult.SUCCESS
        return AuthResult.NOT_FOUND

    def register(self, username, password, locale="en"):
        self.users[username] = SimpleNamespace(
            uuid=f"uuid-{username}",
            locale=locale,
            trust_level=TrustLevel.USER,
            approved=False,
            preferences_json="{}",
        )
        return True

    def get_user(self, username):
        return self.users.get(username)

    def validate_session(self, token):
        return self.sessions.get(token)

    def create_session(self, username, ttl_seconds):
        return "access", 111

    def create_refresh_token(self, username, ttl_seconds):
        return "refresh", 222

    def refresh_session(self, token, access_ttl, refresh_ttl):
        return self.refresh_payloads.get(token)


class FakeDB:
    def __init__(self):
        self.user_count = 1

    def get_user_count(self):
        return self.user_count

    def initialize_trust_levels(self):
        return None

    def load_all_tables(self):
        return []

    def delete_all_tables(self):
        return None


@pytest.fixture
def make_server(monkeypatch, tmp_path):
    def _factory():
        srv = Server(host="127.0.0.1", port=0, db_path=tmp_path / "db.sqlite", preload_locales=True)
        srv._db = FakeDB()
        srv._auth = FakeAuth()
        # Relax credential length checks for tests
        srv._username_min_length = 1
        srv._password_min_length = 1

        async def no_game_list(_client):
            return None

        monkeypatch.setattr(srv, "_send_game_list", no_game_list)
        monkeypatch.setattr(srv, "_show_main_menu", lambda user: None)
        monkeypatch.setattr(srv, "_broadcast_login_presence", lambda user: None)
        # make packet validation a no-op for routing tests
        class FakeAdapter:
            def validate_python(self, pkt):
                return SimpleNamespace(model_dump=lambda **kwargs: pkt)

        monkeypatch.setattr("server.core.server.CLIENT_TO_SERVER_PACKET_ADAPTER", FakeAdapter())
        return srv

    return _factory


@pytest.mark.asyncio
async def test_authorize_banned_user_disconnects(make_server):
    srv = make_server()
    client = DummyClient()
    srv._auth.users["evil"] = SimpleNamespace(
        uuid="uuid-evil",
        locale="en",
        trust_level=TrustLevel.BANNED,
        approved=True,
        preferences_json="{}",
    )
    packet = {"type": "authorize", "username": "evil", "password": "secret"}

    await srv._handle_authorize(client, packet)

    disconnects = [p for p in client.sent if p.get("type") == "disconnect"]
    assert disconnects and disconnects[0]["reconnect"] is False


@pytest.mark.asyncio
async def test_authorize_unapproved_routes_to_menu(make_server):
    called = {}
    srv = make_server()
    client = DummyClient()
    srv._auth.users["new"] = SimpleNamespace(
        uuid="uuid-new",
        locale="en",
        trust_level=TrustLevel.USER,
        approved=False,
        preferences_json="{}",
    )

    def record_menu(user):
        called["user"] = user.username

    srv._show_main_menu = record_menu
    packet = {"type": "authorize", "username": "new", "password": "secret"}

    await srv._handle_authorize(client, packet)

    assert called.get("user") == "new"


@pytest.mark.asyncio
async def test_disconnect_clients_for_status_sends_and_closes(make_server):
    srv = make_server()

    class FakeWSS:
        def __init__(self, clients):
            self.clients = clients

    c1 = DummyClient()
    c2 = DummyClient()
    srv._ws_server = FakeWSS({"a": c1, "b": c2})

    snapshot = ModeSnapshot(ServerMode.MAINTENANCE, "maint", datetime(2025, 1, 1, tzinfo=timezone.utc))
    await srv._disconnect_clients_for_status(snapshot)

    for client in (c1, c2):
        assert any(msg["type"] == "server_status" for msg in client.sent)
        assert any(msg["type"] == "disconnect" for msg in client.sent)
        assert client.closed is True


def test_registration_and_refresh_limits_block(make_server, monkeypatch):
    srv = make_server()
    srv._registration_ip_limit = 1
    srv._registration_ip_window = 10
    srv._registration_attempts_ip = {"ip": deque([0.0])}
    monkeypatch.setattr("server.core.server.time", SimpleNamespace(monotonic=lambda: 0.0))

    msg = srv._check_registration_rate_limit("ip")
    assert "registration" in msg

    srv._refresh_ip_limit = 1
    srv._refresh_ip_window = 10
    srv._refresh_attempts_ip = {"ip": deque([0.0])}
    msg2 = srv._check_refresh_rate_limit("ip")
    assert "refresh" in msg2


@pytest.mark.asyncio
async def test_on_client_message_drops_unauthenticated_non_auth(make_server):
    srv = make_server()
    client = DummyClient()
    called = {"ping": 0}
    srv._handle_ping = lambda c: called.__setitem__("ping", called["ping"] + 1)  # type: ignore

    await srv._on_client_message(client, {"type": "ping"})

    assert called["ping"] == 0  # unauthenticated so ignored


@pytest.mark.asyncio
async def test_on_client_message_allows_ping_when_auth(make_server):
    srv = make_server()
    client = DummyClient()
    client.authenticated = True
    called = {"ping": 0}

    async def ping(_c):
        called["ping"] += 1

    srv._handle_ping = ping  # type: ignore

    await srv._on_client_message(client, {"type": "ping"})

    assert called["ping"] == 1


@pytest.mark.asyncio
async def test_on_client_message_drops_unapproved_other_packets(make_server):
    srv = make_server()
    client = DummyClient()
    client.authenticated = True
    client.username = "u1"
    srv._users["u1"] = SimpleNamespace(approved=False)
    called = {"chat": 0}

    async def chat(_c, _p):
        called["chat"] += 1

    srv._handle_chat = chat  # type: ignore

    await srv._on_client_message(client, {"type": "chat", "text": "hi"})

    assert called["chat"] == 0


@pytest.mark.asyncio
async def test_on_client_message_routes_chat_when_approved(make_server):
    srv = make_server()
    client = DummyClient()
    client.authenticated = True
    client.username = "u1"
    srv._users["u1"] = SimpleNamespace(approved=True)
    called = {"chat": 0}

    async def chat(_c, _p):
        called["chat"] += 1

    srv._handle_chat = chat  # type: ignore

    await srv._on_client_message(client, {"type": "chat", "text": "hi"})

    assert called["chat"] == 1


@pytest.mark.asyncio
async def test_handle_refresh_session_failure_sends_disconnect(make_server):
    srv = make_server()
    client = DummyClient()
    packet = {"type": "refresh_session", "refresh_token": "bad"}

    await srv._handle_refresh_session(client, packet)

    types = [p.get("type") for p in client.sent]
    assert "refresh_session_failure" in types
    assert "disconnect" in types


@pytest.mark.asyncio
async def test_handle_refresh_session_username_mismatch(make_server):
    srv = make_server()
    client = DummyClient()
    srv._auth.refresh_payloads["tok"] = ("alice", "access2", 1, "refresh2", 2)
    packet = {"type": "refresh_session", "refresh_token": "tok", "username": "bob"}

    await srv._handle_refresh_session(client, packet)

    failures = [p for p in client.sent if p.get("type") == "refresh_session_failure"]
    assert failures and "does not match" in failures[0]["message"]


@pytest.mark.asyncio
async def test_handle_refresh_session_success_calls_finalize(make_server, monkeypatch):
    srv = make_server()
    client = DummyClient()
    srv._auth.refresh_payloads["tok"] = ("alice", "access2", 1, "refresh2", 2)
    called = {}

    async def fake_finalize(client_arg, username, **kwargs):
        called["username"] = username
        called["kwargs"] = kwargs

    monkeypatch.setattr(srv, "_finalize_login", fake_finalize)

    await srv._handle_refresh_session(client, {"type": "refresh_session", "refresh_token": "tok"})

    assert called["username"] == "alice"
    assert called["kwargs"]["success_type"] == "refresh_session_success"
