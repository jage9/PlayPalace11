"""Tests for the core.config_paths helpers."""

from __future__ import annotations

from pathlib import Path

from core import config_paths


def test_running_on_windows_is_case_insensitive(monkeypatch):
    monkeypatch.setattr(config_paths.platform, "system", lambda: "WiNdOwS")
    assert config_paths._running_on_windows() is True


def test_get_default_config_dir_prefers_module_when_example_exists(monkeypatch, tmp_path):
    module_dir = tmp_path / "module"
    module_dir.mkdir()
    (module_dir / "config.example.toml").write_text("# example")
    monkeypatch.setattr(config_paths, "_MODULE_DIR", module_dir)

    assert config_paths.get_default_config_dir() == module_dir


def test_get_default_config_dir_uses_programdata_on_windows(monkeypatch, tmp_path):
    module_dir = tmp_path / "module"
    module_dir.mkdir()
    monkeypatch.setattr(config_paths, "_MODULE_DIR", module_dir)
    monkeypatch.setattr(config_paths, "_running_on_windows", lambda: True)
    monkeypatch.delenv("PROGRAMDATA", raising=False)
    program_data = tmp_path / "ProgramData"
    monkeypatch.setenv("PROGRAMDATA", str(program_data))

    expected = program_data / config_paths._WINDOWS_APP_DIR
    assert config_paths.get_default_config_dir() == expected


def test_get_default_config_dir_falls_back_to_module_on_non_windows(monkeypatch, tmp_path):
    module_dir = tmp_path / "module"
    module_dir.mkdir()
    monkeypatch.setattr(config_paths, "_MODULE_DIR", module_dir)
    monkeypatch.setattr(config_paths, "_running_on_windows", lambda: False)

    assert config_paths.get_default_config_dir() == module_dir


def test_get_default_config_path_appends_filename(monkeypatch, tmp_path):
    config_dir = tmp_path / "config"
    monkeypatch.setattr(config_paths, "get_default_config_dir", lambda: config_dir)

    assert config_paths.get_default_config_path() == config_dir / "config.toml"


def test_get_example_config_path_tracks_module_dir(monkeypatch, tmp_path):
    module_dir = tmp_path / "module"
    module_dir.mkdir()
    monkeypatch.setattr(config_paths, "_MODULE_DIR", module_dir)

    assert config_paths.get_example_config_path() == module_dir / "config.example.toml"


def test_ensure_default_config_dir_creates_directory(monkeypatch, tmp_path):
    target = tmp_path / "config"
    monkeypatch.setattr(config_paths, "get_default_config_dir", lambda: target)

    assert config_paths.ensure_default_config_dir() == target
    assert target.exists() and target.is_dir()


def test_load_full_config_returns_empty_when_missing(tmp_path):
    missing_path = tmp_path / "config.toml"

    assert config_paths.load_full_config(missing_path) == {}


def test_load_full_config_parses_toml(tmp_path):
    config_path = tmp_path / "config.toml"
    config_path.write_text("""foo = \"bar\"\n[section]\nvalue = 7\n""")

    data = config_paths.load_full_config(config_path)
    assert data == {"foo": "bar", "section": {"value": 7}}

