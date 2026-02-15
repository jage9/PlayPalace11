from __future__ import annotations

from pathlib import Path


def test_client_schema_matches_server_copy() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    client_schema = (repo_root / "clients" / "desktop" / "packet_schema.json").read_text(encoding="utf-8")
    server_schema = (repo_root / "server" / "packet_schema.json").read_text(encoding="utf-8")
    assert client_schema == server_schema
