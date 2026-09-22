"""Integration coverage for the shared game restoration path."""

from __future__ import annotations

import asyncio
import json
from types import SimpleNamespace

from server.core.server import Server
from server.core.tables.table import Table, TableMember
from server.core.users.test_user import MockUser
from server.game_utils.roulette import RouletteSession
from server.games.pig.game import PigGame


def _saved_pig() -> tuple[str, str]:
    game = PigGame()
    game.host = "old-host"
    game.options.target_score = 73
    game.roulette = RouletteSession(
        ["pig"], finish_mode="score", target_score=321, scores={"alice-id": 42}
    )
    game.players = [
        game.create_player("alice-id", "alice", is_bot=False),
        game.create_player("bot-id", "bot", is_bot=True),
    ]
    game.players[0].is_spectator = True
    return game.to_json(), json.dumps(
        [
            {"username": "alice", "is_bot": False},
            {"username": "bot", "is_bot": True},
        ]
    )


def test_load_tables_restores_real_pig_runtime_and_spectator(tmp_path, monkeypatch):
    game_json, _ = _saved_pig()
    table = Table(
        table_id="startup",
        game_type="pig",
        host="alice",
        members=[TableMember("alice", is_spectator=False)],
        game_json=game_json,
    )
    deleted = []
    server = Server(db_path=tmp_path / "db.sqlite", preload_locales=True)
    server._db = SimpleNamespace(
        load_all_tables=lambda: [table], delete_all_tables=lambda: deleted.append(True)
    )
    monkeypatch.setattr("server.core.server.get_game_class", lambda game_type: PigGame)

    server._load_tables()

    restored = table.game
    assert restored is not None
    assert restored.host == table.host == "alice"
    assert restored.options.target_score == 73
    assert restored.roulette is not None
    assert restored.roulette.scores == {"alice-id": 42}
    assert restored.roulette.target_score == 321
    assert restored._table is table
    assert restored._keybinds
    assert restored._transcripts == {"bot-id": []}
    assert restored.get_user(restored.players[1]).uuid == "bot-id"
    assert table.members[0].is_spectator is True
    assert deleted == [True]


def test_restore_saved_table_restores_real_pig_and_existing_spectator_host(
    tmp_path, monkeypatch
):
    game_json, members_json = _saved_pig()
    user = MockUser("alice", uuid="alice-id")
    record = SimpleNamespace(
        id=9, game_type="pig", game_json=game_json, members_json=members_json
    )
    deleted = []
    server = Server(db_path=tmp_path / "db.sqlite", preload_locales=True)
    server._users = {"alice": user}
    server._db = SimpleNamespace(
        get_saved_table=lambda save_id: record,
        delete_saved_table=lambda save_id: deleted.append(save_id),
    )
    monkeypatch.setattr("server.core.server.get_game_class", lambda game_type: PigGame)

    asyncio.run(server._restore_saved_table(user, record.id))

    table = server._tables.find_user_table("alice")
    assert table is not None
    assert table.host == "alice"
    assert table.members[0].is_spectator is True
    assert table.get_user("alice") is user
    assert table.game is not None
    assert table.game.options.target_score == 73
    assert table.game.roulette.scores == {"alice-id": 42}
    assert table.game.roulette.target_score == 321
    assert table.game.get_user(table.game.players[0]) is user
    assert table.game.get_user(table.game.players[1]).uuid == "bot-id"
    assert table.game._table is table
    assert table.game._keybinds
    assert server._user_states["alice"]["table_id"] == table.table_id
    assert deleted == [record.id]
