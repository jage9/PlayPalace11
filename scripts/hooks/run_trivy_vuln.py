#!/usr/bin/env python3
"""Run Trivy vulnerability scan via Podman."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

IMAGE = "docker.io/aquasec/trivy:0.52.1"


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    cache_dir = repo_root / "var" / "cache" / "trivy"
    cache_dir.mkdir(parents=True, exist_ok=True)

    podman = shutil.which("podman")
    if not podman:
        print("podman is required to run Trivy scans.")
        return 1

    mounts = [
        f"type=bind,source={repo_root},target=/workspace,ro",
        f"type=bind,source={cache_dir},target=/root/.cache",
    ]

    cmd = [
        podman,
        "run",
        "--rm",
        "--security-opt",
        "label=disable",
        "--mount",
        mounts[0],
        "--mount",
        mounts[1],
        "-w",
        "/workspace",
        IMAGE,
        "fs",
        "--exit-code",
        "1",
        "--severity",
        "HIGH,CRITICAL",
        "--scanners",
        "vuln,misconfig",
        "/workspace",
    ]
    print("Running:", " ".join(cmd))
    proc = subprocess.run(cmd, check=False)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
