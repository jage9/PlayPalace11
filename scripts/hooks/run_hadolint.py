#!/usr/bin/env python3
"""Run hadolint over all Containerfiles using podman."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

CONTAINERFILES = (
    "containers/base/Containerfile",
    "server/Containerfile",
    "client/Containerfile",
)
IMAGE = "docker.io/hadolint/hadolint:latest"


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    podman = shutil.which("podman")
    if not podman:
        print("podman is required for hadolint checks; install Podman and retry.")
        return 1

    targets = []
    for relative in CONTAINERFILES:
        path = repo_root / relative
        if not path.exists():
            print(f"Skipping missing Containerfile: {relative}")
            continue
        targets.append(relative)

    if not targets:
        print("No Containerfiles found; skipping hadolint run.")
        return 0

    mount_arg = f"type=bind,source={repo_root},target=/workspace,ro"
    cmd = [
        podman,
        "run",
        "--rm",
        "--mount",
        mount_arg,
        "-w",
        "/workspace",
        "--entrypoint",
        "hadolint",
        IMAGE,
        *targets,
    ]
    print("Running:", " ".join(cmd))
    proc = subprocess.run(cmd, check=False)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
