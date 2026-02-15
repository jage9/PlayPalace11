"""Tests covering TableManager behavior."""

from __future__ import annotations

from core.tables.manager import TableManager
from core.tables.table import Table


class DummyUser:
    def __init__(self, username: str):
        self.username = username


class DummyServer:
    def __init__(self):
        self._db = object()
        self.destroyed: list[Table] = []

    def on_table_destroy(self, table: Table) -> None:  # pragma: no cover - exercised indirectly
        self.destroyed.append(table)


def _make_manager_with_server() -> tuple[TableManager, DummyServer]:
    manager = TableManager()
    server = DummyServer()
    manager._server = server
    return manager, server


def test_create_table_sets_context_and_registers_host():
    manager, server = _make_manager_with_server()
    host_user = DummyUser("host")

    table = manager.create_table("yahtzee", "host", host_user)

    assert manager.get_table(table.table_id) is table
    assert table._manager is manager
    assert table._server is server
    assert table._db is server._db
    assert table.members[0].username == "host"
    assert table.get_user("host") is host_user


def test_table_queries_filter_by_type_and_status():
    manager, _ = _make_manager_with_server()
    t1 = manager.create_table("poker", "alice", DummyUser("alice"))
    t2 = manager.create_table("poker", "bob", DummyUser("bob"))
    t3 = manager.create_table("yahtzee", "carol", DummyUser("carol"))
    t2.status = "playing"

    poker_tables = {t.table_id for t in manager.get_tables_by_type("poker")}
    assert poker_tables == {t1.table_id, t2.table_id}

    waiting_all = {t.table_id for t in manager.get_waiting_tables()}
    assert waiting_all == {t1.table_id, t3.table_id}

    waiting_poker = manager.get_waiting_tables("poker")
    assert [t.table_id for t in waiting_poker] == [t1.table_id]


def test_find_user_table_returns_owner():
    manager, _ = _make_manager_with_server()
    table = manager.create_table("poker", "host", DummyUser("host"))
    extra_user = DummyUser("dave")
    table.add_member("dave", extra_user)

    assert manager.find_user_table("dave") is table
    assert manager.find_user_table("ghost") is None


def test_on_tick_ticks_games_and_removes_empty_tables():
    manager, server = _make_manager_with_server()
    table = manager.create_table("poker", "host", DummyUser("host"))

    class DummyGame:
        def __init__(self):
            self.tick_count = 0

        def to_json(self) -> str:
            return "{}"

        def on_tick(self) -> None:
            self.tick_count += 1

    table.game = DummyGame()

    empty_table = Table(table_id="empty", game_type="poker", host="ghost")
    manager.add_table(empty_table)
    empty_table.members.clear()

    manager.on_tick()

    assert table.game.tick_count == 1
    assert manager.get_table("empty") is None
    assert server.destroyed == [empty_table]


def test_add_table_and_save_all_rehydrate_state():
    manager, _ = _make_manager_with_server()
    table = Table(table_id="loaded", game_type="poker", host="host")

    class DummyGame:
        def __init__(self):
            self.saved = 0

        def to_json(self) -> str:
            self.saved += 1
            return f"{{\"saved\": {self.saved}}}"

    table._game = DummyGame()
    manager.add_table(table)

    saved_tables = manager.save_all()

    assert table._manager is manager
    assert table.game_json == '{"saved": 1}'
    assert saved_tables[0] is table
