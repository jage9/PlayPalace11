"""Additional unit tests for core.tables.table."""

from __future__ import annotations

from server.core.tables.table import Table, TableMember


class DummyUser:
    def __init__(self, name: str):
        self.username = name
        self.spoken: list[tuple[str, str]] = []
        self.sounds: list[tuple[str, int]] = []

    def speak(self, text: str, buffer: str):
        self.spoken.append((text, buffer))

    def play_sound(self, name: str, volume: int):
        self.sounds.append((name, volume))


class DummyGame:
    def __init__(self):
        self.players = []
        self.events: list[tuple[str, dict]] = []
        self.saved = 0
        self.ticks = 0

    def handle_event(self, player, event):
        self.events.append((player.name, event))

    def to_json(self):
        self.saved += 1
        return f"saved-{self.saved}"

    def on_tick(self):
        self.ticks += 1

    def get_player_by_id(self, pid):
        return None


def test_add_member_does_not_duplicate():
    table = Table(table_id="t1", game_type="poker", host="host")
    user = DummyUser("alice")
    table.add_member("alice", user)
    table.add_member("alice", user)  # duplicate should be ignored

    assert len(table.members) == 1
    assert table.get_user("alice") is user


def test_remove_member_triggers_destroy_when_empty():
    destroyed = []

    class Manager:
        def on_table_destroy(self, tbl):
            destroyed.append(tbl)

    table = Table(table_id="t1", game_type="poker", host="host")
    table._manager = Manager()
    table.add_member("alice", DummyUser("alice"))

    table.remove_member("alice")

    assert destroyed == [table]


def test_get_players_and_spectators_and_count():
    table = Table(table_id="t1", game_type="poker", host="host")
    table.members = [
        TableMember(username="p1", is_spectator=False),
        TableMember(username="s1", is_spectator=True),
    ]

    assert [m.username for m in table.get_players()] == ["p1"]
    assert [m.username for m in table.get_spectators()] == ["s1"]
    assert table.player_count == 1


def test_broadcast_sends_to_users():
    table = Table(table_id="t1", game_type="poker", host="host")
    u1 = DummyUser("a")
    u2 = DummyUser("b")
    table._users = {"a": u1, "b": u2}

    table.broadcast("hi", buffer="chat")

    assert u1.spoken == [("hi", "chat")]
    assert u2.spoken == [("hi", "chat")]


def test_broadcast_sound_sends_to_users():
    table = Table(table_id="t1", game_type="poker", host="host")
    u1 = DummyUser("a")
    table._users = {"a": u1}

    table.broadcast_sound("ding", volume=5)

    assert u1.sounds == [("ding", 5)]


def test_on_tick_and_save_game_state_call_game_hooks():
    table = Table(table_id="t1", game_type="poker", host="host")
    game = DummyGame()
    table._game = game

    table.on_tick()
    table.save_game_state()

    assert game.ticks == 1
    assert table.game_json == "saved-1"


def test_handle_event_routes_to_matching_player():
    table = Table(table_id="t1", game_type="poker", host="host")

    class Player:
        def __init__(self, name):
            self.name = name

    game = DummyGame()
    player = Player("alice")
    game.players = [player]
    table._game = game

    table.handle_event("alice", {"move": "bet"})

    assert game.events == [("alice", {"move": "bet"})]


def test_can_start_uses_player_count():
    table = Table(table_id="t1", game_type="poker", host="host")
    table.members = [TableMember(username="p1", is_spectator=False)]

    assert table.can_start(1) is True
    assert table.can_start(2) is False


def test_save_and_close_notifies_server():
    called = []

    class Server:
        def on_table_save(self, table, username):
            called.append((table.table_id, username))

    table = Table(table_id="t1", game_type="poker", host="host")
    table._server = Server()

    table.save_and_close("alice")

    assert called == [("t1", "alice")]


def test_save_game_result_notifies_server():
    received = []

    class Server:
        def on_game_result(self, result):
            received.append(result)

    table = Table(table_id="t1", game_type="poker", host="host")
    table._server = Server()

    table.save_game_result({"winner": "alice"})

    assert received == [{"winner": "alice"}]
