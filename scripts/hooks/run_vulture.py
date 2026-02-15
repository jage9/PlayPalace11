#!/usr/bin/env python3
"""Run Vulture dead-code scanning via uv."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

TARGETS = ["server", "clients/desktop"]
MIN_CONFIDENCE = "80"
# Ignore vendored deps and virtualenvs to focus on project code only.
EXCLUDES = [
    "server/vendor",
    "client/vendor",
    "server/.venv",
    "client/.venv",
    ".venv",
]


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    uv = shutil.which("uv")
    if not uv:
        print("uv is required to run Vulture.")
        return 1

    exclude_arg = ",".join(EXCLUDES)
    cmd = [
        uv,
        "tool",
        "run",
        "vulture",
        *TARGETS,
        "--min-confidence",
        MIN_CONFIDENCE,
        "--exclude",
        exclude_arg,
    ]
    print("Running:", " ".join(cmd))
    proc = subprocess.run(cmd, cwd=repo_root, check=False)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
