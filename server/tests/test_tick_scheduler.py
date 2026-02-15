"""Tests for the TickScheduler utility."""

import asyncio

import pytest

from server.core.tick import TickScheduler, load_server_config, DEFAULT_TICK_INTERVAL_MS


@pytest.mark.asyncio
async def test_tick_scheduler_runs_and_stops_quickly():
    calls = []

    def on_tick():
        calls.append(object())

    # Use 10ms tick interval for tests (Windows timer resolution is ~15ms)
    scheduler = TickScheduler(on_tick, tick_interval_ms=10)

    await scheduler.start()
    await asyncio.sleep(0.1)  # 100ms should allow ~10 ticks
    await scheduler.stop()

    assert not scheduler._running
    assert scheduler._task is None or scheduler._task.cancelled()
    assert len(calls) >= 3  # multiple ticks occurred


@pytest.mark.asyncio
async def test_tick_scheduler_swallows_callback_errors():
    calls = {"count": 0}
    fail_once = {"raised": False}

    def on_tick():
        calls["count"] += 1
        if not fail_once["raised"]:
            fail_once["raised"] = True
            raise RuntimeError("boom")

    # Use 10ms tick interval for tests
    scheduler = TickScheduler(on_tick, tick_interval_ms=10)

    await scheduler.start()
    await asyncio.sleep(0.1)  # 100ms should allow ~10 ticks
    await scheduler.stop()

    assert calls["count"] >= 2  # continued after exception


def test_tick_scheduler_default_interval():
    """Test that default tick interval is used when not specified."""
    scheduler = TickScheduler(lambda: None)
    assert scheduler.tick_interval_ms == DEFAULT_TICK_INTERVAL_MS
    assert scheduler.tick_interval_s == DEFAULT_TICK_INTERVAL_MS / 1000.0


def test_tick_scheduler_custom_interval():
    """Test that custom tick interval is used when specified."""
    scheduler = TickScheduler(lambda: None, tick_interval_ms=100)
    assert scheduler.tick_interval_ms == 100
    assert scheduler.tick_interval_s == 0.1


def test_load_server_config_missing_file():
    """Test that missing config file returns empty dict."""
    config = load_server_config("/nonexistent/path/config.toml")
    assert config == {}


def test_load_server_config_invalid_toml(tmp_path, capsys):
    bad = tmp_path / "bad.toml"
    bad.write_text("server = { invalid = }")

    with pytest.raises(SystemExit):
        load_server_config(bad)

    captured = capsys.readouterr()
    assert "Failed to parse configuration file" in captured.err


def test_load_server_config_os_error(monkeypatch, tmp_path, capsys):
    cfg = tmp_path / "cfg.toml"
    cfg.write_text("[server]\nvalue = 1\n")

    def boom(*_, **__):
        raise OSError("nope")

    monkeypatch.setattr("builtins.open", boom)

    with pytest.raises(SystemExit):
        load_server_config(cfg)

    assert "Failed to read configuration file" in capsys.readouterr().err


def test_load_server_config_from_actual_file():
    """Test loading tick_interval_ms from actual config.toml."""
    from pathlib import Path

    config_path = Path(__file__).parent.parent / "config.toml"
    if config_path.exists():
        config = load_server_config(config_path)
        # Config should have tick_interval_ms if [server] section exists
        if config:
            assert "tick_interval_ms" in config
            assert isinstance(config["tick_interval_ms"], int)
            assert config["tick_interval_ms"] > 0


def test_load_server_config_uses_default_path(monkeypatch, tmp_path):
    default_cfg = tmp_path / "default.toml"
    default_cfg.write_text("[server]\ntick_interval_ms = 75\n")
    monkeypatch.setattr("server.core.tick.get_default_config_path", lambda: default_cfg)

    cfg = load_server_config()

    assert cfg["tick_interval_ms"] == 75
