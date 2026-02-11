#!/usr/bin/env python3
"""Build and smoke-test the server container image with Podman."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

BASE_IMAGE = "playpalace/base:latest"
SERVER_IMAGE = "playpalace/server:smoke"


def run(cmd: list[str], cwd: Path | None = None) -> int:
    print("Running:", " ".join(cmd))
    proc = subprocess.run(cmd, cwd=cwd, check=False)
    return proc.returncode


def ensure_podman() -> str:
    podman = shutil.which("podman")
    if not podman:
        raise SystemExit("podman is required for the smoke test.")
    return podman


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    podman = ensure_podman()

    base_build = [
        podman,
        "build",
        "-f",
        "containers/base/Containerfile",
        "-t",
        BASE_IMAGE,
        ".",
    ]
    if run(base_build, cwd=repo_root) != 0:
        return 1

    server_build = [
        podman,
        "build",
        "-f",
        "server/Containerfile",
        "-t",
        SERVER_IMAGE,
        "server",
    ]
    if run(server_build, cwd=repo_root) != 0:
        return 1

    smoke_cmd = [
        podman,
        "run",
        "--rm",
        SERVER_IMAGE,
        "python",
        "main.py",
        "--help",
    ]
    return run(smoke_cmd, cwd=repo_root)


if __name__ == "__main__":
    raise SystemExit(main())
