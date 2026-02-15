"""Tests for startup error branches and stop cleanup in core.server."""

from __future__ import annotations

import asyncio
import sys
from types import SimpleNamespace

import pytest

from server.core.server import Server, STARTUP_GATE_ID


class DummyDB:
    def __init__(self):
        self.connected = False
        self.closed = False
        self.trust_initialized = False

    def connect(self):
        self.connected = True

    def initialize_trust_levels(self):
        self.trust_initialized = True
        return None

    def load_all_tables(self):
        return []

    def delete_all_tables(self):
        return None

    def close(self):
        self.closed = True

    def save_all_tables(self, tables):
        return None


class DummyWS:
    def __init__(self):
        self.started = False
        self.stopped = False
        self.clients = {}
        self.host = "::"
        self.port = 0

    async def start(self):
        self.started = True

    async def stop(self):
        self.stopped = True

    def get_client_by_username(self, username):
        return None


class DummyTick:
    def __init__(self):
        self.started = False
        self.stopped = False

    async def start(self):
        self.started = True

    async def stop(self):
        self.stopped = True


class DummyBots:
    def __init__(self, raise_config=False):
        self.raise_config = raise_config
        self.saved = False
        self.loaded = 0

    def load_config(self):
        if self.raise_config:
            raise ValueError("bad config")

    def load_state(self):
        return self.loaded

    def save_state(self):
        self.saved = True


class DummyTables:
    def __init__(self):
        self.loaded = False
        self.saved = False

    def add_table(self, table):
        return None

    def save_all(self):
        self.saved = True
        return []


@pytest.mark.asyncio
async def test_start_invalid_tick_interval_raises(tmp_path, capsys, monkeypatch):
    cfg = tmp_path / "config.toml"
    cfg.write_text("tick_interval_ms = \"oops\"")
    srv = Server(host="127.0.0.1", port=0, db_path=tmp_path / "db.sqlite", config_path=cfg, preload_locales=True)
    srv._validate_transport_security = lambda: None  # bypass TLS requirement
    srv._preload_locales = False
    srv._db = DummyDB()
    srv._virtual_bots = DummyBots()
    srv._start_localization_warmup = lambda: None
    srv._lifecycle.resolve_gate = lambda gid: None
    monkeypatch.setattr("server.core.server.TickScheduler", lambda callback, interval=None: srv._tick_scheduler)
    monkeypatch.setattr("server.core.server.WebSocketServer", lambda *args, **kwargs: srv._ws_server)
    monkeypatch.setattr("server.core.server.load_server_config", lambda path: {"tick_interval_ms": "oops"})

    with pytest.raises(SystemExit):
        await srv.start()

    out = capsys.readouterr().err
    assert "Invalid tick_interval_ms" in out


@pytest.mark.asyncio
async def test_start_virtual_bot_config_error(tmp_path, capsys, monkeypatch):
    srv = Server(host="127.0.0.1", port=0, db_path=tmp_path / "db.sqlite", preload_locales=True)
    srv._validate_transport_security = lambda: None
    srv._preload_locales = False
    srv._db = DummyDB()
    srv._ws_server = DummyWS()
    srv._tick_scheduler = DummyTick()
    srv._virtual_bots = DummyBots(raise_config=True)
    srv._tables = DummyTables()
    # skip actual WebSocket/Tick setup
    srv._start_localization_warmup = lambda: None
    srv._lifecycle.resolve_gate = lambda gid: None
    monkeypatch.setattr("server.core.server.TickScheduler", lambda callback, interval=None: srv._tick_scheduler)
    monkeypatch.setattr("server.core.server.WebSocketServer", lambda *args, **kwargs: srv._ws_server)
    monkeypatch.setattr("server.core.server.load_server_config", lambda path: {})

    with pytest.raises(SystemExit):
        await srv.start()

    err = capsys.readouterr().err
    assert "Invalid virtual bot configuration" in err


@pytest.mark.asyncio
async def test_stop_cleans_resources(tmp_path):
    srv = Server(host="127.0.0.1", port=0, db_path=tmp_path / "db.sqlite", preload_locales=True)
    srv._preload_locales = False
    srv._db = DummyDB()
    srv._ws_server = DummyWS()
    srv._tick_scheduler = DummyTick()
    srv._virtual_bots = DummyBots()
    srv._tables = DummyTables()

    await srv.stop()

    assert srv._db.closed is True
    assert srv._virtual_bots.saved is True
    assert srv._tick_scheduler.stopped is True
    assert srv._ws_server.stopped is True


@pytest.mark.asyncio
async def test_start_with_restored_bots_message(tmp_path, capsys):
    monkeypatch = pytest.MonkeyPatch()
    srv = Server(host="127.0.0.1", port=0, db_path=tmp_path / "db.sqlite", preload_locales=True)
    srv._validate_transport_security = lambda: None
    srv._preload_locales = False
    srv._db = DummyDB()
    srv._virtual_bots = DummyBots()
    srv._virtual_bots.loaded = 2
    srv._ws_server = DummyWS()
    srv._tick_scheduler = DummyTick()
    srv._start_localization_warmup = lambda: None
    srv._lifecycle.resolve_gate = lambda gid: None
    srv._tables = DummyTables()
    monkeypatch.setattr("server.core.server.TickScheduler", lambda callback, interval=None: srv._tick_scheduler)
    monkeypatch.setattr("server.core.server.WebSocketServer", lambda *args, **kwargs: srv._ws_server)
    monkeypatch.setattr("server.core.server.load_server_config", lambda path: {})

    await srv.start()
    out = capsys.readouterr().out
    assert "Restored 2 virtual bots" in out
