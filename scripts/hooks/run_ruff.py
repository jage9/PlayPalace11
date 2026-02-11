#!/usr/bin/env python3
"""Wrapper to run Ruff via uv/uvx in a cross-platform way.

The script intentionally limits the linting rule set to the most critical
runtime errors (configured in ruff.toml) so it can run quickly during
pre-commit without forcing a full repo cleanup.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def find_uv() -> str:
    uv = shutil.which("uv")
    if uv:
        return uv
    raise SystemExit("uv is required to run Ruff; install via https://astral.sh/uv")


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    uv = find_uv()
    cmd = [uv, "tool", "run", "ruff", "check", "server", "client"]
    print("Running:", " ".join(cmd))
    proc = subprocess.run(cmd, cwd=repo_root, check=False)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
