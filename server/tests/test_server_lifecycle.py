from datetime import datetime, timedelta, timezone
from types import SimpleNamespace

import pytest

from server.core.server import Server


class StubClient:
    def __init__(self, address="127.0.0.1:9999"):
        self.address = address
        self.sent = []
        self.closed = False
        self.username = None
        self.authenticated = False

    async def send(self, payload):
        self.sent.append(payload)

    async def close(self):
        self.closed = True


@pytest.fixture
def server(tmp_path):
    db_path = tmp_path / "lifecycle.db"
    srv = Server(db_path=str(db_path), locales_dir="locales", config_path=tmp_path / "missing.toml")
    return srv


@pytest.mark.asyncio
async def test_client_blocked_while_initializing(server):
    server._lifecycle.resolve_gate("startup")
    server._lifecycle.add_gate("custom-task", message="Warming up")

    client = StubClient()
    await server._on_client_connect(client)

    assert [packet["type"] for packet in client.sent] == ["server_status", "disconnect"]
    status_packet = client.sent[0]
    assert status_packet["mode"] == "initializing"
    assert status_packet["retry_after"] >= 1
    assert client.sent[1]["status_mode"] == "initializing"
    assert "Warming up" in client.sent[1]["message"]
    assert client.closed is True


@pytest.mark.asyncio
async def test_client_allowed_when_running(server):
    server._lifecycle.resolve_gate("startup")
    client = StubClient()

    await server._on_client_connect(client)

    assert client.sent == []
    assert client.closed is False


@pytest.mark.asyncio
async def test_maintenance_mode_disconnects_clients(server):
    server._lifecycle.resolve_gate("startup")
    client = StubClient()
    server._ws_server = SimpleNamespace(clients={"1": client})

    resume_at = datetime.now(timezone.utc) + timedelta(minutes=5)
    async with server.maintenance_mode("Applying updates", resume_at=resume_at):
        pass

    assert [packet["type"] for packet in client.sent] == ["server_status", "disconnect"]
    assert client.sent[0]["mode"] == "maintenance"
    assert client.sent[1]["retry_after"] >= 1
    assert "Applying updates" in client.sent[1]["message"]
    assert client.closed is True
