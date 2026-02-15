from pathlib import Path
from types import SimpleNamespace

import pytest

from server.cli import bootstrap_owner
from server.persistence.database import Database
from server.core.users.base import TrustLevel
from server.auth.auth import AuthManager
from server.core.server import Server, BOOTSTRAP_WARNING_ENV

LOCALES_DIR = Path(__file__).resolve().parents[1] / "locales"


def test_bootstrap_owner_creates_new_owner(tmp_path):
    db_path = tmp_path / "playpalace.db"

    bootstrap_owner(
        db_path=str(db_path),
        username="admin",
        password="secret-pass",
        locale="en",
        force=False,
        quiet=True,
    )

    database = Database(db_path)
    database.connect()
    try:
        user = database.get_user("admin")
        assert user is not None
        assert user.trust_level == TrustLevel.SERVER_OWNER
        assert user.approved

        auth = AuthManager(database)
        assert auth.verify_password("secret-pass", user.password_hash)
    finally:
        database.close()


def test_bootstrap_owner_requires_force_when_users_exist(tmp_path):
    db_path = tmp_path / "existing.db"
    database = Database(db_path)
    database.connect()
    try:
        auth = AuthManager(database)
        database.create_user(
            username="existing",
            password_hash=auth.hash_password("pw"),
            trust_level=TrustLevel.USER,
            approved=False,
        )
    finally:
        database.close()

    with pytest.raises(RuntimeError):
        bootstrap_owner(
            db_path=str(db_path),
            username="admin",
            password="secret",
            force=False,
            quiet=True,
        )


def test_bootstrap_owner_force_updates_existing_user(tmp_path):
    db_path = tmp_path / "override.db"
    database = Database(db_path)
    database.connect()
    try:
        auth = AuthManager(database)
        database.create_user(
            username="admin",
            password_hash=auth.hash_password("old"),
            trust_level=TrustLevel.USER,
            approved=False,
        )
    finally:
        database.close()

    bootstrap_owner(
        db_path=str(db_path),
        username="admin",
        password="new-secret",
        force=True,
        quiet=True,
    )

    database = Database(db_path)
    database.connect()
    try:
        user = database.get_user("admin")
        assert user.trust_level == TrustLevel.SERVER_OWNER
        assert user.approved
        auth = AuthManager(database)
        assert auth.verify_password("new-secret", user.password_hash)
    finally:
        database.close()


def test_warn_if_no_users_prints_message(capsys, tmp_path):
    server = Server(db_path=str(tmp_path / "db.sqlite"), locales_dir=LOCALES_DIR)
    server._db = SimpleNamespace(get_user_count=lambda: 0)
    server._warn_if_no_users()
    out = capsys.readouterr().out
    assert "bootstrap-owner" in out


def test_warn_if_no_users_respects_env(monkeypatch, capsys, tmp_path):
    server = Server(db_path=str(tmp_path / "db.sqlite"), locales_dir=LOCALES_DIR)
    server._db = SimpleNamespace(get_user_count=lambda: 0)
    monkeypatch.setenv(BOOTSTRAP_WARNING_ENV, "1")
    server._warn_if_no_users()
    out = capsys.readouterr().out
    assert out == ""
