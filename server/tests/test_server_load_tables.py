"""Tests for _load_tables restoring games and handling missing game classes."""

from __future__ import annotations

from types import SimpleNamespace

from server.core.server import Server


class StubTableManager:
    def __init__(self):
        self.added = []

    def add_table(self, table):
        self.added.append(table)


class StubDB:
    def __init__(self, tables):
        self.tables = tables
        self.deleted = False

    def load_all_tables(self):
        return self.tables

    def delete_all_tables(self):
        self.deleted = True


class StubGameClass:
    def __init__(self):
        self.instances = []

    def get_type(self):
        return "stub"

    def get_name_key(self):
        return "stub"

    @staticmethod
    def from_json(game_json):
        # create game with a bot player to exercise attach bot path
        bot_player = SimpleNamespace(id="bot-id", name="botty", is_bot=True)
        human_player = SimpleNamespace(id="human-id", name="alice", is_bot=False)
        return StubGame([bot_player, human_player])


class StubGame:
    def __init__(self, players):
        self.players = players
        self._users = {}
        self._table = None
        self.game_type = "stub"

    def rebuild_runtime_state(self):
        return None

    def setup_keybinds(self):
        return None

    def _reset_transcripts(self):
        return None

    def get_player_by_id(self, pid):
        return None

    def get_player_by_name(self, name):
        for p in self.players:
            if getattr(p, "name", None) == name:
                return p
        return None

    def attach_user(self, pid, user):
        self._users[pid] = user


def test_load_tables_handles_missing_game_class_and_restores(monkeypatch, tmp_path):
    # Unknown game type table triggers warning path; known stub restores bots
    t_unknown = SimpleNamespace(game_json="{}", game_type="missing", game=None)
    t_known = SimpleNamespace(game_json="{}", game_type="stub", game=None)
    tables = [t_unknown, t_known]

    srv = Server(host="127.0.0.1", port=0, db_path=tmp_path / "db.sqlite", preload_locales=True)
    stub_tables = StubTableManager()
    srv._tables = stub_tables  # type: ignore[assignment]
    srv._db = StubDB(tables)  # type: ignore[assignment]

    # patch GameRegistry lookups
    monkeypatch.setattr("server.core.server.get_game_class", lambda gt: StubGameClass() if gt == "stub" else None)

    srv._load_tables()

    # unknown game should still be added but skipped restore
    assert t_unknown in stub_tables.added
    # known game restored and bots attached
    assert t_known.game is not None
    assert any(u.username == "botty" for u in t_known.game._users.values())
    assert srv._db.deleted is True
