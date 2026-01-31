"""Tests for Server._handle_authorize covering key flows."""

import asyncio
import json
from types import SimpleNamespace

import pytest


from server.core.server import Server, DEFAULT_WS_MAX_MESSAGE_BYTES
from server.auth.auth import AuthResult
from server.users.base import TrustLevel


class DummyClient:
    def __init__(self, address="127.0.0.1:12345"):
        self.username = None
        self.authenticated = False
        self.sent = []
        self.address = address

    async def send(self, payload):
        self.sent.append(payload)


class DummyAuth:
    def __init__(self, *, authenticate_result=AuthResult.SUCCESS, register_result=True, user_record=None):
        self.authenticate_result = authenticate_result
        self.register_result = register_result
        self.calls = {"authenticate": [], "register": []}
        self.user_record = user_record

    def authenticate(self, username, password):
        self.calls["authenticate"].append((username, password))
        return self.authenticate_result

    def register(self, username, password):
        self.calls["register"].append((username, password))
        return self.register_result

    def get_user(self, username):
        return self.user_record


@pytest.fixture
def server(tmp_path):
    db_path = tmp_path / "auth.db"
    srv = Server(db_path=str(db_path), locales_dir="locales")
    return srv


@pytest.mark.asyncio
@pytest.mark.slow
async def test_authorize_registers_and_waits_for_approval(monkeypatch, server):
    server._db = SimpleNamespace(get_user_count=lambda: 5)
    record = SimpleNamespace(
        username="newbie",
        locale="en",
        uuid="uuid-1",
        trust_level=TrustLevel.USER,
        approved=False,
        preferences_json=json.dumps(
            {"play_turn_sound": False, "dice_keeping_style": "playpalace"}
        ),
    )
    auth = DummyAuth(authenticate_result=AuthResult.USER_NOT_FOUND, register_result=True, user_record=record)
    server._auth = auth
    server._tables = SimpleNamespace(find_user_table=lambda username: None)

    notifications = []
    server._notify_admins = lambda message_id, sound: notifications.append((message_id, sound))

    sent_game_list = []

    async def fake_send_game_list(client):
        sent_game_list.append(client.username)

    server._send_game_list = fake_send_game_list

    main_menu_calls = []

    def fake_show_main_menu(user):
        main_menu_calls.append(user.username)

    server._show_main_menu = fake_show_main_menu

    client = DummyClient()
    packet = {"username": "newbie", "password": "pw"}

    await server._handle_authorize(client, packet)

    assert auth.calls["authenticate"] == [("newbie", "pw")]
    assert auth.calls["register"] == [("newbie", "pw")]
    assert notifications == [("account-request", "accountrequest.ogg")]
    assert client.authenticated and client.username == "newbie"
    assert sent_game_list == ["newbie"]
    assert main_menu_calls == ["newbie"]
    assert "newbie" in server._users


@pytest.mark.asyncio
@pytest.mark.slow
async def test_authorize_existing_admin_announces(monkeypatch, server):
    server._db = SimpleNamespace(
        get_user_count=lambda: 0,
        get_pending_users=lambda exclude_banned=True: [],
    )
    record = SimpleNamespace(
        username="admin",
        locale="es",
        uuid="uuid-2",
        trust_level=TrustLevel.ADMIN,
        approved=True,
        preferences_json="{}",
    )
    auth = DummyAuth(authenticate_result=AuthResult.SUCCESS, user_record=record)
    server._auth = auth
    server._tables = SimpleNamespace(find_user_table=lambda username: None)

    broadcasts = []
    server._broadcast_presence_l = lambda msg, player, sound: broadcasts.append((msg, player, sound))
    server._broadcast_admin_announcement = lambda player: broadcasts.append(("admin", player))
    server._broadcast_server_owner_announcement = lambda player: broadcasts.append(("owner", player))
    main_menu_calls = []
    server._show_main_menu = lambda user: main_menu_calls.append(user.username)
    server._notify_admins = lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("should not notify"))

    async def fake_send_game_list(client):
        fake_send_game_list.calls.append(client.username)

    fake_send_game_list.calls = []

    server._send_game_list = fake_send_game_list

    client = DummyClient()
    packet = {"username": "admin", "password": "pw"}

    await server._handle_authorize(client, packet)

    assert auth.calls["register"] == []
    assert broadcasts[0] == ("user-online", "admin", "onlineadmin.ogg")
    assert ("admin", "admin") in [(b[1], b[1]) for b in broadcasts if b[0] == "admin"]
    assert main_menu_calls == ["admin"]
    assert fake_send_game_list.calls == ["admin"]
    assert "admin" in server._users


@pytest.mark.asyncio
@pytest.mark.slow
async def test_register_requires_username_and_password(server):
    client = DummyClient()

    await server._handle_register(client, {"username": "", "password": ""})

    expected = (
        f"Username must be between {server._username_min_length} and {server._username_max_length} characters."
    )
    assert client.sent == [
        {"type": "speak", "text": expected}
    ]


@pytest.mark.asyncio
@pytest.mark.slow
async def test_register_success_notifies_admins(server):
    server._db = SimpleNamespace(get_user_count=lambda: 3)
    auth = DummyAuth(register_result=True)
    server._auth = auth
    notifications = []
    server._notify_admins = lambda msg, sound: notifications.append((msg, sound))

    client = DummyClient()
    await server._handle_register(client, {"username": "fresh", "password": "pw"})

    assert client.sent[-1] == {
        "type": "speak",
        "text": "Registration successful! You can now log in with your credentials.",
    }
    assert auth.calls["register"] == [("fresh", "pw")]
    assert notifications == [("account-request", "accountrequest.ogg")]


@pytest.mark.asyncio
@pytest.mark.slow
async def test_register_rejects_duplicate_username(server):
    server._db = SimpleNamespace(get_user_count=lambda: 0)
    auth = DummyAuth(register_result=False)
    server._auth = auth

    client = DummyClient()
    await server._handle_register(client, {"username": "taken", "password": "pw"})

    assert client.sent[-1] == {
        "type": "speak",
        "text": "Username already taken. Please choose a different username.",
    }
    assert auth.calls["register"] == [("taken", "pw")]


@pytest.mark.asyncio
async def test_authorize_rejects_invalid_username_length(server):
    server._auth = DummyAuth()
    client = DummyClient()
    packet = {"username": "aa", "password": "validpass"}

    await server._handle_authorize(client, packet)

    assert server._auth.calls["authenticate"] == []
    assert len(client.sent) == 3
    assert client.sent[1]["text"].startswith("Username must be between")


@pytest.mark.asyncio
async def test_authorize_rejects_invalid_password_length(server):
    server._auth = DummyAuth()
    client = DummyClient()
    packet = {"username": "validuser", "password": "short"}

    await server._handle_authorize(client, packet)

    assert server._auth.calls["authenticate"] == []
    assert len(client.sent) == 3
    assert client.sent[1]["text"].startswith("Password must be between")


@pytest.mark.asyncio
async def test_register_rejects_invalid_lengths(server):
    server._auth = DummyAuth()
    client = DummyClient()

    await server._handle_register(client, {"username": "aa", "password": "pw"})

    assert server._auth.calls["register"] == []
    assert client.sent[-1]["text"].startswith("Username must be between")


@pytest.mark.asyncio
@pytest.mark.slow
async def test_login_rate_limit_by_ip(server):
    server._auth = DummyAuth(authenticate_result=AuthResult.USER_NOT_FOUND, register_result=False)
    server._login_ip_limit = 1
    server._db = SimpleNamespace(get_user_count=lambda: 0)
    client = DummyClient()
    packet = {"username": "foo", "password": "validpass"}

    await server._handle_authorize(client, packet)
    client.sent.clear()
    await server._handle_authorize(client, packet)

    assert server._auth.calls["authenticate"] == [("foo", "validpass")]
    assert "Too many login attempts" in client.sent[1]["text"]


@pytest.mark.asyncio
@pytest.mark.slow
async def test_login_rate_limit_by_username(server):
    server._auth = DummyAuth(authenticate_result=AuthResult.WRONG_PASSWORD)
    server._login_user_limit = 1
    server._db = SimpleNamespace(get_user_count=lambda: 1)
    client = DummyClient()
    packet = {"username": "repeat", "password": "validpass"}

    await server._handle_authorize(client, packet)
    client.sent.clear()
    await server._handle_authorize(client, packet)

    assert "Too many failed login attempts" in client.sent[1]["text"]


@pytest.mark.asyncio
@pytest.mark.slow
async def test_registration_rate_limit_by_ip(server):
    server._db = SimpleNamespace(get_user_count=lambda: 0)
    server._auth = DummyAuth(register_result=True)
    server._registration_ip_limit = 1
    client = DummyClient()

    await server._handle_register(client, {"username": "first", "password": "validpass"})
    client.sent.clear()
    await server._handle_register(client, {"username": "second", "password": "validpass"})

    assert "Too many registration attempts" in client.sent[-1]["text"]


def test_auth_limits_loaded_from_config(tmp_path):
    config_path = tmp_path / "config.toml"
    config_path.write_text(
        """
[auth]
username_min_length = 5
username_max_length = 12
password_min_length = 10
password_max_length = 42
[network]
max_message_bytes = 2048
"""
    )
    srv = Server(db_path=str(tmp_path / "auth.db"), locales_dir="locales", config_path=config_path)

    assert srv._username_min_length == 5
    assert srv._username_max_length == 12
    assert srv._password_min_length == 10
    assert srv._password_max_length == 42
    assert srv._ws_max_message_size == 2048


def test_network_max_size_defaults(tmp_path):
    srv = Server(db_path=str(tmp_path / "auth.db"), locales_dir="locales", config_path=tmp_path / "missing.toml")
    assert srv._ws_max_message_size == DEFAULT_WS_MAX_MESSAGE_BYTES
