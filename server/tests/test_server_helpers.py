"""Targeted tests for helper methods inside core.server.Server."""

import asyncio

import pytest


from types import SimpleNamespace

from server.core.server import Server


class DummyNetworkUser:
    def __init__(self, approved=True):
        self.approved = approved
        self.spoken = []
        self.sounds = []
        self._queue = []

    def speak_l(self, message_id, **kwargs):
        self.spoken.append((message_id, kwargs))

    def play_sound(self, sound):
        self.sounds.append(sound)

    def queue(self, message):
        self._queue.append(message)

    def get_queued_messages(self):
        messages = list(self._queue)
        self._queue.clear()
        return messages


class DummyClient:
    def __init__(self):
        self.sent = []

    async def send(self, payload):
        self.sent.append(payload)


class DummyWebSocketServer:
    def __init__(self, mapping):
        self.mapping = mapping

    def get_client_by_username(self, username):
        return self.mapping.get(username)


@pytest.fixture
def server(tmp_path):
    db_path = tmp_path / "test.db"
    srv = Server(db_path=str(db_path), locales_dir="locales", config_path=tmp_path / "missing.toml")
    return srv


@pytest.mark.asyncio
@pytest.mark.slow
async def test_flush_user_messages_sends_only_to_connected_clients(server):
    alice = DummyNetworkUser()
    bob = DummyNetworkUser()
    alice.queue({"type": "ping"})
    bob.queue({"type": "pong"})
    server._users = {"alice": alice, "bob": bob}

    alice_client = DummyClient()
    ws = DummyWebSocketServer({"alice": alice_client})
    server._ws_server = ws

    server._flush_user_messages()
    await asyncio.sleep(0)  # allow scheduled tasks to run

    assert alice_client.sent == [{"type": "ping"}]
    assert bob.get_queued_messages() == []  # queue already drained


@pytest.mark.slow
def test_broadcast_helpers_respect_approval(server):
    approved = DummyNetworkUser(approved=True)
    unapproved = DummyNetworkUser(approved=False)
    server._users = {"ok": approved, "pending": unapproved}

    server._broadcast_presence_l("user-online", "Bot", "online.ogg")
    server._broadcast_admin_announcement("Admin")
    server._broadcast_server_owner_announcement("Owner")
    server._broadcast_table_created("Host", "GameName")

    # Only approved user should receive notifications
    assert len(approved.spoken) == 4
    assert approved.sounds == ["online.ogg", "table_created.ogg"]
    assert unapproved.spoken == []
    assert unapproved.sounds == []


def test_on_client_disconnect_broadcasts_only_for_approved(server):
    approved = DummyNetworkUser(approved=True)
    banned = DummyNetworkUser(approved=True)
    banned.trust_level = type("T", (), {"value": 0})()
    approved.trust_level = type("T", (), {"value": 2})()
    server._users = {"alice": approved, "bob": banned}
    server._user_states = {"alice": {}, "bob": {}}

    client = SimpleNamespace(username="alice", address="addr")

    server._on_client_disconnect = Server._on_client_disconnect.__get__(server, Server)

    asyncio.run(server._on_client_disconnect(client))
    assert server._users == {"bob": banned}
    assert server._user_states == {"bob": {}}
    assert approved.sounds[-1] == "offlineadmin.ogg"


def test_on_client_disconnect_keeps_members_when_not_last(server):
    user = DummyNetworkUser(approved=True)
    user.uuid = "user-1"
    user.trust_level = type("T", (), {"value": 1})()
    server._users = {"alice": user}
    server._user_states = {"alice": {}}

    class DummyGame:
        def __init__(self, player_id):
            self.player_id = player_id
            self.called = False

        def get_player_by_id(self, player_id):
            return SimpleNamespace(id=player_id) if player_id == self.player_id else None

        def _perform_leave_game(self, player):
            self.called = True

    members = [SimpleNamespace(username="alice"), SimpleNamespace(username="bob")]
    table = SimpleNamespace(
        members=members,
        game=DummyGame(user.uuid),
        remove_member=lambda username: members.__setitem__(
            slice(None), [m for m in members if m.username != username]
        ),
    )
    server._tables = SimpleNamespace(find_user_table=lambda username: table)

    client = SimpleNamespace(username="alice", address="addr")
    server._on_client_disconnect = Server._on_client_disconnect.__get__(server, Server)
    asyncio.run(server._on_client_disconnect(client))

    assert table.game.called
    assert [m.username for m in members] == ["alice", "bob"]


def test_on_client_disconnect_removes_last_member(server):
    user = DummyNetworkUser(approved=True)
    user.uuid = "user-1"
    user.trust_level = type("T", (), {"value": 1})()
    server._users = {"alice": user}
    server._user_states = {"alice": {}}

    class DummyGame:
        def __init__(self, player_id):
            self.player_id = player_id
            self.called = False

        def get_player_by_id(self, player_id):
            return SimpleNamespace(id=player_id) if player_id == self.player_id else None

        def _perform_leave_game(self, player):
            self.called = True

    members = [SimpleNamespace(username="alice")]
    table = SimpleNamespace(
        members=members,
        game=DummyGame(user.uuid),
        remove_member=lambda username: members.__setitem__(
            slice(None), [m for m in members if m.username != username]
        ),
    )
    server._tables = SimpleNamespace(find_user_table=lambda username: table)

    client = SimpleNamespace(username="alice", address="addr")
    server._on_client_disconnect = Server._on_client_disconnect.__get__(server, Server)
    asyncio.run(server._on_client_disconnect(client))

    assert table.game.called
    assert members == []


@pytest.mark.slow
def test_send_game_list_includes_all_games(server):
    async def capture_send(payload):
        capture_send.sent.append(payload)

    capture_send.sent = []
    client = SimpleNamespace(send=capture_send)

    asyncio.run(server._send_game_list(client))
    assert capture_send.sent
    games_payload = capture_send.sent[-1]
    assert games_payload["type"] == "update_options_lists"
    assert "games" in games_payload and games_payload["games"]
