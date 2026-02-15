"""Lifecycle- and status-related tests for core.server gameplay lifecycle hooks."""

from __future__ import annotations

import asyncio
from datetime import datetime, timezone, timedelta
from types import SimpleNamespace

import pytest

from server.core.server import Server
from server.core.state import ModeSnapshot, ServerMode


class FakeClient:
    def __init__(self):
        self.sent: list[dict] = []
        self.closed = False
        self.username = None
        self.address = "1.2.3.4:9999"
        self.authenticated = False

    async def send(self, payload):
        self.sent.append(payload)

    async def close(self):
        self.closed = True


class FakeWebSocketServer:
    def __init__(self, clients):
        self.clients = clients


@pytest.fixture
def server(tmp_path):
    return Server(host="127.0.0.1", port=0, db_path=tmp_path / "db.sqlite", preload_locales=True)


@pytest.mark.asyncio
async def test_send_status_and_disconnect_builds_payloads(server):
    client = FakeClient()
    snapshot = ModeSnapshot(ServerMode.MAINTENANCE, "maint", None)

    await server._send_status_and_disconnect(client, snapshot)

    assert client.closed is True
    assert any(pkt.get("type") == "server_status" for pkt in client.sent)
    assert any(pkt.get("type") == "disconnect" for pkt in client.sent)


@pytest.mark.asyncio
async def test_disconnect_clients_for_status_handles_all(server):
    c1, c2 = FakeClient(), FakeClient()
    ws = FakeWebSocketServer({"a": c1, "b": c2})
    server._ws_server = ws
    snapshot = ModeSnapshot(ServerMode.MAINTENANCE, "msg", None)

    await server._disconnect_clients_for_status(snapshot)

    assert c1.closed and c2.closed


@pytest.mark.asyncio
async def test_maintenance_mode_context_resets(server):
    # give ws server so disconnect path runs
    c1 = FakeClient()
    server._ws_server = FakeWebSocketServer({"a": c1})

    async with server.maintenance_mode("Updating", resume_at=None):
        snap = server._lifecycle.snapshot()
        assert snap.mode == ServerMode.MAINTENANCE
    # After maintenance, if gates remain, mode returns to INITIALIZING; otherwise RUNNING.
    assert server._lifecycle.snapshot().mode in {ServerMode.RUNNING, ServerMode.INITIALIZING}


@pytest.mark.asyncio
async def test_reject_client_during_unavailable(server):
    client = FakeClient()
    snapshot = ModeSnapshot(ServerMode.MAINTENANCE, "down", None)

    await server._reject_client_during_unavailable(client, snapshot)

    assert client.closed is True
    assert any(pkt.get("type") == "disconnect" for pkt in client.sent)


def test_calculate_retry_after_with_resume(server):
    future = datetime.now(timezone.utc) + timedelta(seconds=42)
    snap = ModeSnapshot(ServerMode.MAINTENANCE, "m", future)
    retry = server._calculate_retry_after(snap)
    assert 40 <= retry <= 42
