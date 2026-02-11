#!/usr/bin/env python3
"""Ensure the generated packet schemas stay byte-identical across server/client."""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path


SCHEMA_COMMAND = "cd server && uv run python tools/export_packet_schema.py"


def file_digest(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    server_schema = repo_root / "server" / "packet_schema.json"
    client_schema = repo_root / "client" / "packet_schema.json"

    missing = [p for p in (server_schema, client_schema) if not p.exists()]
    if missing:
        print("Missing schema files:\n" + "\n".join(str(p) for p in missing))
        print(f"Regenerate them via `{SCHEMA_COMMAND}`.")
        return 1

    if server_schema.read_bytes() != client_schema.read_bytes():
        print("Server and client packet schemas differ.")
        print(f"Re-run `{SCHEMA_COMMAND}` and restage the files.")
        print(f"server hash: {file_digest(server_schema)}")
        print(f"client hash: {file_digest(client_schema)}")
        return 1

    print("Packet schemas match.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
