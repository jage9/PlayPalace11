from pathlib import Path

import pytest

from server.core.server import Server
from server.network import websocket_server as websocket_module


def _write_config(tmp_path: Path, allow_insecure: bool, tick_interval: int | None = None) -> Path:
    lines = ["[network]", f"allow_insecure_ws = {'true' if allow_insecure else 'false'}", ""]
    if tick_interval is not None:
        lines.extend(["[server]", f"tick_interval_ms = {tick_interval}", ""])
    config_path = tmp_path / "config.toml"
    config_path.write_text("\n".join(lines), encoding="utf-8")
    return config_path


def test_localization_missing_directory(tmp_path, capsys):
    missing_locales = tmp_path / "missing_locales"
    with pytest.raises(SystemExit):
        Server(locales_dir=missing_locales)
    captured = capsys.readouterr()
    assert "Localization directory" in captured.err


@pytest.mark.asyncio
async def test_tls_certificate_load_failure(tmp_path, capsys):
    server = Server(
        db_path=str(tmp_path / "db.sqlite"),
        config_path=tmp_path / "missing.toml",
        ssl_cert=tmp_path / "missing_cert.pem",
        ssl_key=tmp_path / "missing_key.pem",
    )
    with pytest.raises(SystemExit):
        await server.start()
    captured = capsys.readouterr()
    assert "Failed to load TLS certificate or key" in captured.err


@pytest.mark.asyncio
async def test_websocket_bind_failure(tmp_path, monkeypatch, capsys):
    config_path = _write_config(tmp_path, allow_insecure=True)

    class FailingServe:
        async def __aenter__(self):
            raise OSError("address already in use")

        async def __aexit__(self, exc_type, exc, tb):
            return False

    def fake_serve(*args, **kwargs):
        return FailingServe()

    monkeypatch.setattr(websocket_module, "serve", fake_serve)

    server = Server(
        db_path=str(tmp_path / "db.sqlite"),
        config_path=config_path,
    )
    with pytest.raises(SystemExit):
        await server.start()
    captured = capsys.readouterr()
    assert "Failed to bind WebSocket server" in captured.err


@pytest.mark.asyncio
async def test_database_connection_failure(tmp_path, capsys):
    config_path = _write_config(tmp_path, allow_insecure=True)
    db_path = tmp_path / "dbdir"
    db_path.mkdir()
    server = Server(
        db_path=str(db_path),
        config_path=config_path,
    )
    with pytest.raises(SystemExit):
        await server.start()
    captured = capsys.readouterr()
    assert "Failed to open database" in captured.err


@pytest.mark.asyncio
async def test_tick_interval_invalid(tmp_path, capsys):
    config_path = _write_config(tmp_path, allow_insecure=True, tick_interval=0)
    server = Server(
        db_path=str(tmp_path / "db.sqlite"),
        config_path=config_path,
    )
    with pytest.raises(SystemExit):
        await server.start()
    captured = capsys.readouterr()
    assert "tick_interval_ms must be at least 1" in captured.err


@pytest.mark.asyncio
async def test_tls_required_without_cert(tmp_path, capsys):
    config_path = _write_config(tmp_path, allow_insecure=False)
    server = Server(
        db_path=str(tmp_path / "db.sqlite"),
        config_path=config_path,
    )
    with pytest.raises(SystemExit):
        await server.start()
    captured = capsys.readouterr()
    assert "TLS is required" in captured.err


@pytest.mark.asyncio
async def test_insecure_mode_with_cert_conflict(tmp_path, capsys):
    config_path = _write_config(tmp_path, allow_insecure=True)
    server = Server(
        db_path=str(tmp_path / "db.sqlite"),
        config_path=config_path,
        ssl_cert="cert.pem",
        ssl_key="key.pem",
    )
    with pytest.raises(SystemExit):
        await server.start()
    captured = capsys.readouterr()
    assert "allow_insecure_ws=true cannot be combined" in captured.err
