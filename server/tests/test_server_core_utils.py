"""Focused unit tests for helper logic inside core.server."""

from __future__ import annotations

import asyncio
import itertools
from collections import deque
from datetime import datetime, timedelta, timezone
from pathlib import Path
import sys
from types import SimpleNamespace

import pytest

# Ensure the repository root (which contains the 'server' package) is importable.
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from server.core import server as server_module
from server.core.server import (
    LOCALIZATION_GATE_ID,
    STARTUP_GATE_ID,
    Server,
    _coerce_bool,
    _ensure_var_server_dir,
)
from server.core.state import ModeSnapshot, ServerMode


@pytest.fixture
def make_server(tmp_path):
    counter = itertools.count()

    def _factory(**overrides):
        idx = next(counter)
        defaults = {
            "host": "127.0.0.1",
            "port": 0,
            "db_path": tmp_path / f"db_{idx}.sqlite",
            "config_path": tmp_path / f"config_{idx}.toml",
            "preload_locales": True,
        }
        defaults.update(overrides)
        return Server(**defaults)

    return _factory


def test_coerce_bool_handles_varied_inputs():
    assert _coerce_bool(True, False) is True
    assert _coerce_bool(" YES ", False) is True
    assert _coerce_bool("0", True) is False
    assert _coerce_bool(0, True) is False
    assert _coerce_bool("unknown", True) is True


def test_ensure_var_server_dir_uses_monkeypatched_path(tmp_path, monkeypatch):
    target = tmp_path / "var" / "server"
    monkeypatch.setattr(server_module, "_VAR_SERVER_DIR", target)

    result = _ensure_var_server_dir()

    assert result == target
    assert target.exists()


def test_validate_transport_security_allows_explicit_insecure(make_server):
    srv = make_server()
    srv._allow_insecure_ws = True
    srv._ssl_cert = None
    srv._ssl_key = None

    # Should not raise when insecure mode is explicitly allowed without TLS.
    srv._validate_transport_security()


def test_validate_transport_security_rejects_mixed_tls(make_server):
    srv = make_server()
    srv._allow_insecure_ws = True
    srv._ssl_cert = "cert.pem"

    with pytest.raises(SystemExit):
        srv._validate_transport_security()


def test_validate_transport_security_requires_tls_material(make_server):
    srv = make_server()
    srv._allow_insecure_ws = False
    srv._ssl_cert = None
    srv._ssl_key = None

    with pytest.raises(SystemExit):
        srv._validate_transport_security()


def test_validate_transport_security_passes_with_cert_and_key(make_server):
    srv = make_server(ssl_cert="cert.pem", ssl_key="key.pem")

    srv._validate_transport_security()


def test_validate_credentials_enforces_lengths(make_server):
    srv = make_server()
    username, password, error = srv._validate_credentials("ab", "pass")
    assert error and "Username" in error

    username, password, error = srv._validate_credentials("valid", "pw")
    assert error and "Password" in error


def test_validate_credentials_sanitizes_inputs(make_server):
    srv = make_server()
    username, password, error = srv._validate_credentials("  Alice  ", "  secret  ")
    assert error is None
    assert username == "Alice"
    assert password == "  secret  "


def test_allow_attempt_enforces_window(make_server):
    srv = make_server()
    bucket: dict[str, deque[float]] = {"ip": deque([0.0])}

    assert srv._allow_attempt(bucket, "ip", limit=1, window=10, now=0.0) is False
    assert srv._allow_attempt(bucket, "ip", limit=1, window=0.5, now=1.0) is True


def test_get_attempt_count_cleans_empty_bucket(make_server):
    srv = make_server()
    bucket: dict[str, deque[float]] = {"ip": deque([0.0])}

    count = srv._get_attempt_count(bucket, "ip", window=0.5, now=2.0)

    assert count == 0
    assert "ip" not in bucket


def test_record_attempt_appends_timestamp(make_server):
    srv = make_server()
    bucket: dict[str, deque[float]] = {}

    srv._record_attempt(bucket, "ip", now=1.23)

    assert bucket["ip"][-1] == 1.23


def test_check_login_rate_limit_blocks_ip(monkeypatch, make_server):
    srv = make_server()
    srv._login_ip_limit = 1
    srv._login_ip_window = 10
    srv._login_attempts_ip = {"1.2.3.4": deque([0.0])}
    monkeypatch.setattr(server_module.time, "monotonic", lambda: 0.0)

    message = srv._check_login_rate_limit("1.2.3.4", "user")

    assert message and "login attempts" in message


def test_check_login_rate_limit_blocks_username(monkeypatch, make_server):
    srv = make_server()
    srv._login_ip_limit = 0  # disable IP throttling for this test
    srv._login_user_limit = 1
    srv._login_user_window = 10
    srv._login_attempts_user = {"alice": deque([0.0])}
    monkeypatch.setattr(server_module.time, "monotonic", lambda: 0.0)

    message = srv._check_login_rate_limit("5.6.7.8", "alice")

    assert message and "failed login attempts" in message


def test_record_login_failure_prunes_old_entries(monkeypatch, make_server):
    srv = make_server()
    srv._login_user_limit = 1
    srv._login_user_window = 1
    srv._login_attempts_user = {"bob": deque([-5.0])}
    monkeypatch.setattr(server_module.time, "monotonic", lambda: 10.0)

    srv._record_login_failure("bob")

    assert srv._login_attempts_user["bob"] == deque([10.0])


def test_check_registration_rate_limit(monkeypatch, make_server):
    srv = make_server()
    srv._registration_ip_limit = 1
    srv._registration_ip_window = 10
    srv._registration_attempts_ip = {"ip": deque([0.0])}
    monkeypatch.setattr(server_module.time, "monotonic", lambda: 0.0)

    message = srv._check_registration_rate_limit("ip")

    assert message and "registration attempts" in message


def test_check_refresh_rate_limit(monkeypatch, make_server):
    srv = make_server()
    srv._refresh_ip_limit = 1
    srv._refresh_ip_window = 10
    srv._refresh_attempts_ip = {"ip": deque([0.0])}
    monkeypatch.setattr(server_module.time, "monotonic", lambda: 0.0)

    message = srv._check_refresh_rate_limit("ip")

    assert message and "refresh attempts" in message


def test_build_status_packets_include_optional_fields(make_server):
    srv = make_server()
    resume_at = datetime(2025, 1, 1, tzinfo=timezone.utc)
    snapshot = ModeSnapshot(ServerMode.MAINTENANCE, "Upgrading", resume_at)

    status = srv._build_status_packet(snapshot, retry_after=42)
    disconnect = srv._build_status_disconnect(snapshot, retry_after=42)

    assert status["message"] == "Upgrading"
    assert status["resume_at"].endswith("Z")
    assert disconnect["status_mode"] == ServerMode.MAINTENANCE.value
    assert "Expected availability" in disconnect["message"]


def test_format_status_message_handles_missing_resume():
    snapshot = ModeSnapshot(ServerMode.MAINTENANCE, None, None)
    message = Server._format_status_message(snapshot)

    assert "Server is temporarily unavailable" in message


def test_format_datetime_normalizes_timezone():
    naive = datetime(2024, 1, 1, 12, 0, 0)
    formatted = Server._format_datetime(naive)

    assert formatted.endswith("Z")


def test_calculate_retry_after_prefers_resume(monkeypatch, make_server):
    class FixedDateTime(datetime):
        @classmethod
        def now(cls, tz=None):  # type: ignore[override]
            return cls(2025, 1, 1, tzinfo=timezone.utc)

    monkeypatch.setattr(server_module, "datetime", FixedDateTime)

    srv = make_server()
    resume_at = FixedDateTime(2025, 1, 1, 0, 0, 10, tzinfo=timezone.utc)
    snapshot = ModeSnapshot(ServerMode.MAINTENANCE, None, resume_at)

    retry = srv._calculate_retry_after(snapshot)

    assert retry >= 1


def test_get_client_ip_handles_missing_address():
    client = SimpleNamespace(address=None)
    assert Server._get_client_ip(client) == "unknown"

    client = SimpleNamespace(address="10.0.0.1:1234")
    assert Server._get_client_ip(client) == "10.0.0.1"


def test_sanitize_credentials_strips_and_defaults():
    username, password = Server._sanitize_credentials(None, None)
    assert username == ""
    assert password == ""

    username, password = Server._sanitize_credentials("  Foo  ", "bar")
    assert username == "Foo"
    assert password == "bar"


class _DummyClient:
    def __init__(self):
        self.sent: list[dict] = []
        self.closed = False

    async def send(self, payload: dict) -> None:
        self.sent.append(payload)

    async def close(self) -> None:
        self.closed = True


@pytest.mark.asyncio
async def test_send_status_and_disconnect_sequences_packets(make_server):
    srv = make_server()
    snapshot = ModeSnapshot(
        ServerMode.MAINTENANCE,
        "Updating",
        datetime(2025, 1, 1, tzinfo=timezone.utc),
    )
    client = _DummyClient()

    await srv._send_status_and_disconnect(client, snapshot)

    assert len(client.sent) == 2
    assert client.sent[0]["type"] == "server_status"
    assert client.sent[1]["type"] == "disconnect"
    assert client.closed is True


@pytest.mark.asyncio
async def test_maintenance_mode_enters_and_exits(monkeypatch, make_server):
    srv = make_server()
    srv._lifecycle.resolve_gate(STARTUP_GATE_ID)

    snapshots: list[ModeSnapshot] = []

    async def fake_disconnect(snapshot: ModeSnapshot) -> None:
        snapshots.append(snapshot)

    monkeypatch.setattr(srv, "_disconnect_clients_for_status", fake_disconnect)

    resume_at = datetime(2025, 1, 1, tzinfo=timezone.utc) + timedelta(hours=1)
    async with srv.maintenance_mode("Upgrading", resume_at=resume_at):
        assert snapshots
        assert snapshots[-1].mode == ServerMode.MAINTENANCE
        assert snapshots[-1].resume_at == resume_at
        assert srv._lifecycle.snapshot().mode == ServerMode.MAINTENANCE

    assert srv._lifecycle.snapshot().mode == ServerMode.RUNNING


@pytest.mark.asyncio
async def test_start_localization_warmup_creates_background_task(monkeypatch, make_server):
    srv = make_server()
    srv._preload_locales = False
    called = asyncio.Event()

    async def fake_warm():
        called.set()

    monkeypatch.setattr(srv, "_warm_locales_async", fake_warm)

    srv._start_localization_warmup()

    assert srv._localization_gate_registered is True
    assert srv._localization_warmup_task is not None
    await asyncio.wait_for(called.wait(), 1)
    await srv._localization_warmup_task


@pytest.mark.asyncio
async def test_preload_locales_if_requested_runs_in_thread(monkeypatch, make_server):
    srv = make_server(preload_locales=True)
    srv._lifecycle.resolve_gate(STARTUP_GATE_ID)
    called = False

    def fake_preload():
        nonlocal called
        called = True

    monkeypatch.setattr(server_module.Localization, "preload_bundles", fake_preload)

    await srv._preload_locales_if_requested()

    assert called is True
    assert srv._lifecycle.snapshot().mode == ServerMode.RUNNING


@pytest.mark.asyncio
async def test_warm_locales_async_resolves_gate(monkeypatch, make_server):
    srv = make_server()
    srv._lifecycle.resolve_gate(STARTUP_GATE_ID)
    srv._ensure_localization_gate()
    resolved = False

    def fake_preload():
        nonlocal resolved
        resolved = True

    monkeypatch.setattr(server_module.Localization, "preload_bundles", fake_preload)

    await srv._warm_locales_async()

    assert resolved is True
    snapshot = srv._lifecycle.snapshot()
    assert snapshot.mode == ServerMode.RUNNING


@pytest.mark.asyncio
async def test_warm_locales_async_failure_enters_maintenance(monkeypatch, make_server):
    srv = make_server()
    srv._lifecycle.resolve_gate(STARTUP_GATE_ID)
    srv._ensure_localization_gate()

    def fake_preload():
        raise RuntimeError("boom")

    monkeypatch.setattr(server_module.Localization, "preload_bundles", fake_preload)

    captured: list[ModeSnapshot] = []

    async def fake_disconnect(snapshot: ModeSnapshot) -> None:
        captured.append(snapshot)

    monkeypatch.setattr(srv, "_disconnect_clients_for_status", fake_disconnect)

    await srv._warm_locales_async()

    assert srv._lifecycle.snapshot().mode == ServerMode.MAINTENANCE
    assert captured and captured[-1].mode == ServerMode.MAINTENANCE
