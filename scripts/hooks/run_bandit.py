#!/usr/bin/env python3
"""Run Bandit via uv against server and client sources."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

# Keep tests and vendored environments out of Bandit runs to avoid noise.
EXCLUDES = [
    "server/tests",
    "clients/desktop/tests",
    "server/.venv",
    "clients/desktop/.venv",
    ".venv",
]


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    uv = shutil.which("uv")
    if not uv:
        print("uv is required to run Bandit.")
        return 1

    exclude_arg = ",".join(EXCLUDES)
    cmd = [
        uv,
        "tool",
        "run",
        "bandit",
        "-q",
        "-r",
        "server",
        "clients/desktop",
        "-x",
        exclude_arg,
    ]
    print("Running:", " ".join(cmd))
    proc = subprocess.run(cmd, cwd=repo_root, check=False)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
