"""Tests for Server table load/save helpers."""

import json
from types import SimpleNamespace

import pytest

from server.core.server import Server


class DummyTable:
    def __init__(self, table_id, game_type, game_json=None):
        self.table_id = table_id
        self.game_type = game_type
        self.game_json = game_json
        self.game = None


class DummyTablesManager:
    def __init__(self):
        self.added = []
        self.saved = []
        self.waiting_find = {}

    def add_table(self, table):
        self.added.append(table)

    def save_all(self):
        return list(self.saved)

    def on_tick(self):
        pass

    def get_table(self, table_id):
        return self.waiting_find.get(table_id)

    def find_user_table(self, username):
        return None


class DummyGame:
    def __init__(self):
        self.players = [SimpleNamespace(is_bot=True, name="BotOne", id="bot-1")]
        self.rebuilt = False
        self.keybinds_setup = False
        self.rebuilt_players = []

    @classmethod
    def from_json(cls, data):
        return cls()

    def rebuild_runtime_state(self):
        self.rebuilt = True

    def setup_keybinds(self):
        self.keybinds_setup = True

    def attach_user(self, player_id, bot_user):
        self.rebuilt_players.append(bot_user.username)


@pytest.fixture
def server(tmp_path):
    db_path = tmp_path / "tables.db"
    srv = Server(db_path=str(db_path), locales_dir="locales")
    return srv


@pytest.mark.slow
def test_save_tables_calls_db_and_manager(monkeypatch, server):
    tables_manager = DummyTablesManager()
    tables_manager.saved = [DummyTable("t1", "pig"), DummyTable("t2", "farkle")]
    server._tables = tables_manager

    saved_to_db = []
    server._db = SimpleNamespace(
        save_all_tables=lambda tables: saved_to_db.extend(tables)
    )

    server._save_tables()

    assert saved_to_db == tables_manager.saved


@pytest.mark.slow
def test_load_tables_restores_games_and_clears_db(monkeypatch, server):
    dummy_game_json = json.dumps({"state": "dummy"})
    table_with_game = DummyTable("table-game", "test_game", game_json=dummy_game_json)
    plain_table = DummyTable("table-plain", "test_game")

    called_delete = []
    server._db = SimpleNamespace(
        load_all_tables=lambda: [table_with_game, plain_table],
        delete_all_tables=lambda: called_delete.append(True),
    )
    dummy_tables = DummyTablesManager()
    server._tables = dummy_tables

    class DummyBot:
        def __init__(self, name):
            self.username = name

    monkeypatch.setattr("server.core.server.Bot", DummyBot, raising=False)
    monkeypatch.setattr("server.core.server.get_game_class", lambda game_type: DummyGame)

    server._load_tables()

    assert dummy_tables.added == [table_with_game, plain_table]
    assert isinstance(table_with_game.game, DummyGame)
    assert table_with_game.game.rebuilt
    assert table_with_game.game.keybinds_setup
    assert table_with_game.game.rebuilt_players == ["BotOne"]
    assert table_with_game.game._table is table_with_game
    assert called_delete == [True]
