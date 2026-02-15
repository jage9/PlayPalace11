#!/usr/bin/env python3
"""Build and smoke-test the client container image with Podman."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

BASE_IMAGE = "playpalace/base:latest"
CLIENT_IMAGE = "playpalace/client:smoke"


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
        "packaging/containers/base/Containerfile",
        "-t",
        BASE_IMAGE,
        ".",
    ]
    if run(base_build, cwd=repo_root) != 0:
        return 1

    client_build = [
        podman,
        "build",
        "-f",
        "clients/desktop/Containerfile",
        "-t",
        CLIENT_IMAGE,
        ".",
    ]
    if run(client_build, cwd=repo_root) != 0:
        return 1

    smoke_cmd = [
        podman,
        "run",
        "--rm",
        "-e",
        "DISPLAY=",
        CLIENT_IMAGE,
        "python",
        "-m",
        "compileall",
        "clients/desktop",
    ]
    return run(smoke_cmd, cwd=repo_root)


if __name__ == "__main__":
    raise SystemExit(main())
