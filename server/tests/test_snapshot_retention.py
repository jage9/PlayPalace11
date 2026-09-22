"""Integration coverage for retaining failed table snapshots."""

from __future__ import annotations

import asyncio
import json
import sqlite3

from server.core.server import Server
from server.core.users.test_user import MockUser
from server.games.pig.game import PigGame


def test_load_tables_keeps_failed_snapshots_and_continues(tmp_path, caplog):
    server = Server(db_path=tmp_path / "tables.db", preload_locales=True)
    server._db.connect()
    user = MockUser("host")
    server._users[user.username] = user
    cursor = server._db._conn.cursor()
    valid_game = PigGame().to_json()
    rows = [
        ("unknown", "missing-game", "host", "[]", "{}", "waiting"),
        ("bad-game", "pig", "host", "[]", "not-json", "waiting"),
        ("bad-members", "pig", "host", "not-json", valid_game, "waiting"),
        ("valid", "pig", "host", json.dumps([]), valid_game, "waiting"),
    ]
    cursor.executemany(
        "INSERT INTO tables (table_id, game_type, host, members_json, game_json, status) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        rows,
    )
    server._db._conn.commit()

    with caplog.at_level("ERROR", logger="playpalace"):
        server._load_tables()

    assert [table.table_id for table in server._tables.get_all_tables()] == ["valid"]
    assert "missing-game" in caplog.text
    assert "bad-game" in caplog.text
    assert "bad-members" in caplog.text
    assert user.messages == []
    expected_failed = {row[0]: row[1:] for row in rows[:-1]}
    assert {
        row[0]: tuple(row[1:]) for row in cursor.execute(
            "SELECT table_id, game_type, host, members_json, game_json, status FROM tables"
        )
    } == expected_failed

    asyncio.run(server.stop())
    connection = sqlite3.connect(tmp_path / "tables.db")
    remaining = {
        row[0]: row[1:]
        for row in connection.execute(
            "SELECT table_id, game_type, host, members_json, game_json, status FROM tables"
        )
    }
    assert set(remaining) == {"unknown", "bad-game", "bad-members", "valid"}
    assert {key: remaining[key] for key in expected_failed} == expected_failed
    connection.close()
