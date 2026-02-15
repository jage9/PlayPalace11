#!/usr/bin/env python3
"""Run Xenon complexity budget checks via uv."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

MAX_ABSOLUTE = "B"
MAX_MODULES = "B"
MAX_AVERAGE = "B"
TARGETS = ["server", "clients/desktop"]


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    uv = shutil.which("uv")
    if not uv:
        print("uv is required to run Xenon.")
        return 1

    cmd = [
        uv,
        "tool",
        "run",
        "xenon",
        *TARGETS,
        "--max-absolute",
        MAX_ABSOLUTE,
        "--max-modules",
        MAX_MODULES,
        "--max-average",
        MAX_AVERAGE,
    ]
    print("Running:", " ".join(cmd))
    proc = subprocess.run(cmd, cwd=repo_root, check=False)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
