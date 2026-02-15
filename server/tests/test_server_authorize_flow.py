"""Targeted tests for Server._handle_authorize logic using fakes."""

from __future__ import annotations

import asyncio
from types import SimpleNamespace

import pytest

from server.core.server import Server
from server.core.users.base import TrustLevel
from server.auth.auth import AuthResult


class DummyClient(SimpleNamespace):
    def __init__(self, address="1.2.3.4:9999"):
        super().__init__(address=address, username=None, authenticated=False, sent=[])

    async def send(self, payload):
        self.sent.append(payload)


class FakeAuth:
    def __init__(self):
        self.users = {"alice": SimpleNamespace(uuid="uuid-a", locale="en", trust_level=TrustLevel.USER, approved=True, preferences_json="{}")}
        self.sessions: dict[str, str] = {}
        self.authenticate_calls: list[tuple[str, str]] = []

    def authenticate(self, username, password):
        self.authenticate_calls.append((username, password))
        if username == "alice" and password == "secret":
            return AuthResult.SUCCESS
        if username == "alice":
            return AuthResult.WRONG_PASSWORD
        return AuthResult.NOT_FOUND

    def register(self, username, password, locale="en"):
        self.users[username] = SimpleNamespace(uuid="new", locale=locale, trust_level=TrustLevel.USER, approved=False, preferences_json="{}")
        return True

    def get_user(self, username):
        return self.users.get(username)

    def validate_session(self, token):
        return self.sessions.get(token)

    def create_session(self, username, ttl_seconds):
        self.sessions["generated"] = username
        return "access-token", 123

    def create_refresh_token(self, username, ttl_seconds):
        return "refresh-token", 456


class FakeDB:
    def __init__(self):
        self.user_count = 0

    def get_user_count(self):
        return self.user_count

    def initialize_trust_levels(self):
        return None

    def load_all_tables(self):
        return []

    def delete_all_tables(self):
        return None


@pytest.fixture
def server(tmp_path, monkeypatch):
    srv = Server(host="127.0.0.1", port=0, db_path=tmp_path / "db.sqlite", preload_locales=True)
    srv._db = FakeDB()
    srv._auth = FakeAuth()
    async def _send_game_list(_client):
        return None

    monkeypatch.setattr(srv, "_send_game_list", _send_game_list)
    monkeypatch.setattr(srv, "_show_main_menu", lambda user: None)
    # bypass actual presence broadcast side effects
    monkeypatch.setattr(srv, "_broadcast_login_presence", lambda user: None)
    return srv


@pytest.mark.asyncio
async def test_authorize_with_session_token_valid(server):
    client = DummyClient()
    server._auth.sessions["token"] = "alice"
    packet = {"type": "authorize", "session_token": "token", "username": "alice"}

    await server._handle_authorize(client, packet)

    assert client.authenticated is True
    assert client.username == "alice"
    assert any(p.get("type") == "authorize_success" for p in client.sent)


@pytest.mark.asyncio
async def test_authorize_rejects_mismatched_session_username(server):
    client = DummyClient()
    server._auth.sessions["token"] = "alice"
    packet = {"type": "authorize", "session_token": "token", "username": "bob"}

    await server._handle_authorize(client, packet)

    assert any(p.get("type") == "disconnect" for p in client.sent)


@pytest.mark.asyncio
async def test_authorize_wrong_password_records_failure(monkeypatch, server):
    client = DummyClient()
    packet = {"type": "authorize", "username": "alice", "password": "wrongpass"}

    # track throttling state mutations
    server._login_attempts_user.clear()

    await server._handle_authorize(client, packet)

    assert "alice" in server._login_attempts_user
    # should send disconnect with message
    assert any(p.get("type") == "disconnect" for p in client.sent)


def test_sanitize_credentials_handles_none():
    username, password = Server._sanitize_credentials(None, None)
    assert username == ""
    assert password == ""
