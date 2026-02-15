"""Targeted unit tests to raise coverage on core.server helpers."""

from __future__ import annotations

import asyncio
import os
from datetime import datetime, timedelta, timezone
from types import SimpleNamespace

import pytest

from server.core.server import (
    BOOTSTRAP_WARNING_ENV,
    LOCALIZATION_GATE_ID,
    Server,
    ServerMode,
)
from server.core.state import ModeSnapshot


class FakeDBCount:
    def __init__(self, count: int):
        self.count = count

    def get_user_count(self):
        return self.count


class FakeLoop:
    def __init__(self):
        self.tasks = []

    def create_task(self, coro):
        task = asyncio.create_task(coro)
        self.tasks.append(task)
        return task


@pytest.fixture
def server(tmp_path):
    return Server(host="127.0.0.1", port=0, db_path=tmp_path / "db.sqlite", preload_locales=True)


def test_validate_transport_conflict_raises(server):
    server._allow_insecure_ws = True
    server._ssl_cert = "cert.pem"

    with pytest.raises(SystemExit):
        server._validate_transport_security()


def test_validate_transport_requires_tls_or_opt_out(server):
    server._allow_insecure_ws = False
    server._ssl_cert = None
    server._ssl_key = None

    with pytest.raises(SystemExit):
        server._validate_transport_security()


def test_warn_if_no_users_respects_env(server, capsys, monkeypatch):
    monkeypatch.setenv(BOOTSTRAP_WARNING_ENV, "1")
    server._db = FakeDBCount(0)

    server._warn_if_no_users()

    captured = capsys.readouterr()
    assert "WARNING: No user accounts exist" not in captured.out


def test_warn_if_no_users_prints_when_empty(server, capsys, monkeypatch):
    monkeypatch.delenv(BOOTSTRAP_WARNING_ENV, raising=False)
    server._db = FakeDBCount(0)

    server._warn_if_no_users()

    assert "WARNING: No user accounts exist" in capsys.readouterr().out


def test_warn_if_no_users_silent_when_existing(server, capsys, monkeypatch):
    monkeypatch.delenv(BOOTSTRAP_WARNING_ENV, raising=False)
    server._db = FakeDBCount(2)

    server._warn_if_no_users()

    assert capsys.readouterr().out == ""


def test_record_login_failure_ignored_when_limit_zero(server):
    server._login_user_limit = 0
    server._login_attempts_user.clear()

    server._record_login_failure("alice")

    assert server._login_attempts_user == {}


def test_calculate_retry_after_variants(server):
    future = datetime.now(timezone.utc) + timedelta(seconds=12)
    snap_future = ModeSnapshot(ServerMode.MAINTENANCE, "m", future)
    snap_init = ModeSnapshot(ServerMode.INITIALIZING, None, None)
    snap_maint = ModeSnapshot(ServerMode.MAINTENANCE, None, None)
    snap_running = ModeSnapshot(ServerMode.RUNNING, None, None)

    assert server._calculate_retry_after(snap_future) >= 11
    assert server._calculate_retry_after(snap_init) == 5
    assert server._calculate_retry_after(snap_maint) == 30
    assert server._calculate_retry_after(snap_running) == 5


def test_format_status_and_datetime(server):
    dt = datetime(2025, 1, 1, 12, 0, 0)  # naive should get Z suffix
    snap = ModeSnapshot(ServerMode.MAINTENANCE, "msg", dt)

    formatted = server._format_datetime(dt)
    assert formatted.endswith("Z")
    message = server._format_status_message(snap)
    assert "Expected availability" in message


def test_load_config_settings_applies_limits(tmp_path):
    cfg = tmp_path / "config.toml"
    cfg.write_text(
        """
[auth]
username_min_length = 5
username_max_length = 4  # should clamp to min
password_min_length = 12
password_max_length = 10  # should clamp
refresh_token_ttl_seconds = 30

[auth.rate_limits]
login_per_minute = 0
registration_per_minute = 2
refresh_per_minute = 0

[network]
max_message_bytes = 2048
allow_insecure_ws = true

[localization]
default_locale = "es"
        """,
        encoding="utf-8",
    )

    srv = Server(
        host="127.0.0.1",
        port=0,
        db_path=tmp_path / "db.sqlite",
        config_path=cfg,
        preload_locales=True,
    )

    assert srv._username_min_length == 5
    assert srv._username_max_length == 5  # clamped
    assert srv._password_min_length == 12
    assert srv._password_max_length == 12  # clamped
    assert srv._refresh_token_ttl_seconds == 60  # minimum clamp
    assert srv._login_ip_limit == 0
    assert srv._registration_ip_limit == 2
    assert srv._refresh_ip_limit == 0
    assert srv._ws_max_message_size == 2048
    assert srv._allow_insecure_ws is True
    assert srv._default_locale == "es"


def test_check_registration_rate_limit_blocked(monkeypatch, server):
    monkeypatch.setattr(server, "_allow_attempt", lambda *args, **kwargs: False)
    msg = server._check_registration_rate_limit("1.2.3.4")
    assert "Too many registration attempts" in msg


def test_check_refresh_rate_limit_blocked(monkeypatch, server):
    monkeypatch.setattr(server, "_allow_attempt", lambda *args, **kwargs: False)
    msg = server._check_refresh_rate_limit("1.2.3.4")
    assert "Too many refresh attempts" in msg


@pytest.mark.asyncio
async def test_preload_locales_if_requested_runs(monkeypatch, server):
    called = {}

    def fake_preload():
        called["ran"] = True

    monkeypatch.setattr("server.messages.localization.Localization.preload_bundles", fake_preload)
    server._preload_locales = True

    await server._preload_locales_if_requested()

    assert called.get("ran")
    assert LOCALIZATION_GATE_ID not in server._lifecycle._gates


@pytest.mark.asyncio
async def test_start_localization_warmup_schedules(monkeypatch, server):
    server._preload_locales = False
    server._localization_warmup_task = None
    async def dummy():
        return None
    monkeypatch.setattr(server, "_warm_locales_async", dummy)
    loop = FakeLoop()
    monkeypatch.setattr(asyncio, "get_running_loop", lambda: loop)

    server._start_localization_warmup()

    assert server._localization_gate_registered is True
    assert loop.tasks, "expected task scheduling"


@pytest.mark.asyncio
async def test_start_localization_warmup_skips_when_preload(monkeypatch, server):
    server._preload_locales = True
    loop = FakeLoop()
    monkeypatch.setattr(asyncio, "get_running_loop", lambda: loop)

    server._start_localization_warmup()

    assert not loop.tasks
