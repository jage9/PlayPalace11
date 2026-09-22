"""Tests for persistence.database.Database."""

import json

import pytest

from server.persistence.database import Database
from server.core.tables.table import Table, TableMember
from server.core.users.base import TrustLevel


@pytest.fixture
def db(tmp_path):
    database = Database(db_path=tmp_path / "test.db")
    database.connect()
    try:
        yield database
    finally:
        database.close()


def _insert_user(db: Database, username: str, trust=None, approved=1):
    cursor = db._conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, password_hash, uuid, trust_level, approved) VALUES (?, ?, ?, ?, ?)",
        (username, "hash", f"uuid-{username}", trust, approved),
    )
    db._conn.commit()


@pytest.mark.parametrize("session_points", [None, 1, 350])
def test_server_result_round_trip_retains_team_winners_and_scores(db, session_points):
    from server.core.server import Server
    from server.game_utils.game_result import GameResult, PlayerResult

    server = Server.__new__(Server)
    server._db = db
    result = GameResult(
        game_type="pig", timestamp="2026-09-22T12:00:00", duration_ticks=100,
        player_results=[PlayerResult("alice", "Alice", False, score=100, team_id="0",
                                     session_points=session_points),
                        PlayerResult("bob", "Bob", False, score=100, team_id="0")],
        winner_ids=["alice", "bob"],
        custom_data={"winner_name": "Team 1", "final_scores": {"Team 1": 100}},
    )
    server.on_game_result(result)
    restored = server._get_game_results("pig")[0]
    assert restored.get_winner_ids() == result.winner_ids
    assert restored.player_results == result.player_results


def test_initialize_trust_levels_promotes_first_user(db):
    _insert_user(db, "owner", trust=None)

    promoted = db.initialize_trust_levels()

    assert promoted == "owner"
    cursor = db._conn.cursor()
    cursor.execute("SELECT trust_level FROM users WHERE username = ?", ("owner",))
    assert cursor.fetchone()[0] == TrustLevel.SERVER_OWNER.value


def test_initialize_trust_levels_defaults_to_user(db):
    _insert_user(db, "alice", trust=None)
    _insert_user(db, "bob", trust=None)

    promoted = db.initialize_trust_levels()

    assert promoted is None
    cursor = db._conn.cursor()
    cursor.execute("SELECT username, trust_level FROM users ORDER BY username")
    levels = {row[0]: row[1] for row in cursor.fetchall()}
    assert levels == {"alice": TrustLevel.USER.value, "bob": TrustLevel.USER.value}


def test_save_and_load_table_round_trip(db):
    table = Table(
        table_id="table-1",
        game_type="pig",
        host="host",
        members=[TableMember("host"), TableMember("spectator", is_spectator=True)],
        game_json=json.dumps({"state": "playing"}),
        status="playing",
    )

    db.save_table(table)
    loaded = db.load_table("table-1")

    assert loaded is not None
    assert loaded.table_id == table.table_id
    assert loaded.game_type == "pig"
    assert loaded.host == "host"
    assert loaded.status == "playing"
    assert [m.username for m in loaded.members] == ["host", "spectator"]
    assert loaded.members[1].is_spectator is True


def test_delete_all_tables_removes_saved_entries(db):
    table = Table(
        table_id="table-2",
        game_type="pig",
        host="host",
        members=[TableMember("host")],
    )

    db.save_table(table)
    assert db.load_table("table-2") is not None

    db.delete_all_tables()

    assert db.load_all_tables() == []


def test_save_user_table_and_get_list(db):
    rec1 = db.save_user_table(
        "player",
        "first",
        "pig",
        json.dumps({"state": 1}),
        json.dumps([{"username": "player"}]),
    )
    rec2 = db.save_user_table(
        "player",
        "second",
        "pig",
        json.dumps({"state": 2}),
        json.dumps([{"username": "player"}]),
    )

    saved = db.get_user_saved_tables("player")
    assert [record.save_name for record in saved] == [rec2.save_name, rec1.save_name]


def test_get_and_delete_saved_table(db):
    rec = db.save_user_table(
        "player",
        "snapshot",
        "pig",
        json.dumps({"state": 42}),
        json.dumps([{"username": "player"}]),
    )

    fetched = db.get_saved_table(rec.id)
    assert fetched is not None and fetched.save_name == "snapshot"

    db.delete_saved_table(rec.id)
    assert db.get_saved_table(rec.id) is None


def test_update_user_preferences_and_locale(db):
    _insert_user(db, "prefUser", trust=TrustLevel.USER.value, approved=1)
    prefs = json.dumps({"play_turn_sound": False})

    db.update_user_preferences("prefUser", prefs)
    db.update_user_locale("prefUser", "pl")

    cursor = db._conn.cursor()
    cursor.execute("SELECT preferences_json, locale FROM users WHERE username = ?", ("prefUser",))
    row = cursor.fetchone()
    assert row[0] == prefs
    assert row[1] == "pl"


def test_revoke_user_refresh_tokens_revokes_only_target(db):
    db.store_refresh_token("alice", "tok-a1", 100, 1)
    db.store_refresh_token("Alice", "tok-a2", 100, 1)
    db.store_refresh_token("bob", "tok-b1", 100, 1)

    db.revoke_user_refresh_tokens("alice", 50)

    assert db.get_refresh_token("tok-a1").revoked_at == 50
    assert db.get_refresh_token("tok-a2").revoked_at == 50
    assert db.get_refresh_token("tok-b1").revoked_at is None


def test_fluent_languages_default_empty(db):
    user = db.create_user("alice", "hash", approved=True)
    assert user.fluent_languages == []


def test_set_and_get_fluent_languages(db):
    db.create_user("alice", "hash", approved=True)
    db.set_user_fluent_languages("alice", ["en", "fr"])
    assert db.get_user_fluent_languages("alice") == ["en", "fr"]

    db.set_user_fluent_languages("alice", ["de"])
    assert db.get_user_fluent_languages("alice") == ["de"]


def test_fluent_languages_in_user_record(db):
    db.create_user("alice", "hash", approved=True)
    db.set_user_fluent_languages("alice", ["en", "es"])
    user = db.get_user("alice")
    assert user.fluent_languages == ["en", "es"]


def test_add_and_get_transcriber_assignments(db):
    db.create_user("alice", "hash", approved=True)
    assert db.add_transcriber_assignment("alice", "en") is True
    assert db.add_transcriber_assignment("alice", "fr") is True
    assert db.get_transcriber_languages("alice") == ["en", "fr"]


def test_get_transcribers_for_language(db):
    db.create_user("alice", "hash", approved=True)
    db.create_user("bob", "hash", approved=True)
    db.add_transcriber_assignment("alice", "en")
    db.add_transcriber_assignment("bob", "en")
    db.add_transcriber_assignment("alice", "fr")

    assert db.get_transcribers_for_language("en") == ["alice", "bob"]
    assert db.get_transcribers_for_language("fr") == ["alice"]
    assert db.get_transcribers_for_language("de") == []


def test_remove_transcriber_assignment(db):
    db.create_user("alice", "hash", approved=True)
    db.add_transcriber_assignment("alice", "en")
    assert db.remove_transcriber_assignment("alice", "en") is True
    assert db.get_transcriber_languages("alice") == []
    assert db.remove_transcriber_assignment("alice", "en") is False


def test_transcriber_cascade_on_user_delete(db):
    db.create_user("alice", "hash", approved=True)
    db.add_transcriber_assignment("alice", "en")
    db.add_transcriber_assignment("alice", "fr")
    db.delete_user("alice")
    # Assignments should be gone due to ON DELETE CASCADE
    cursor = db._conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM transcriber_assignments")
    assert cursor.fetchone()[0] == 0


def test_duplicate_transcriber_assignment(db):
    db.create_user("alice", "hash", approved=True)
    assert db.add_transcriber_assignment("alice", "en") is True
    assert db.add_transcriber_assignment("alice", "en") is False


def test_get_all_transcribers(db):
    db.create_user("alice", "hash", approved=True)
    db.create_user("bob", "hash", approved=True)
    db.add_transcriber_assignment("alice", "en")
    db.add_transcriber_assignment("alice", "fr")
    db.add_transcriber_assignment("bob", "de")
    result = db.get_all_transcribers()
    assert result == {"alice": ["en", "fr"], "bob": ["de"]}


def test_approve_and_delete_user(db):
    _insert_user(db, "pending", trust=TrustLevel.USER.value, approved=0)

    assert db.approve_user("pending") is True
    cursor = db._conn.cursor()
    cursor.execute("SELECT approved FROM users WHERE username = ?", ("pending",))
    assert cursor.fetchone()[0] == 1

    assert db.delete_user("pending") is True
    assert db.get_user("pending") is None
