#!/usr/bin/env python3
"""Rebuild packet schemas whenever packet models change."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    server_dir = repo_root / "server"
    uv = shutil.which("uv")
    if not uv:
        print("uv is required to regenerate packet schemas.")
        return 1

    cmd = [uv, "run", "python", "tools/export_packet_schema.py"]
    print("Running:", " ".join(cmd))
    proc = subprocess.run(cmd, cwd=server_dir, check=False)
    if proc.returncode == 0:
        print("Packet schemas regenerated.")
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
