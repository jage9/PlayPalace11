#!/usr/bin/env python3
"""Generate a CycloneDX SBOM via Trivy."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

IMAGE = "docker.io/aquasec/trivy:0.52.1"
OUTPUT_NAME = "trivy-sbom.json"


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    artifacts_dir = repo_root / "artifacts" / "sbom"
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    output_path = artifacts_dir / OUTPUT_NAME

    podman = shutil.which("podman")
    if not podman:
        print("podman is required to run Trivy SBOM generation.")
        return 1

    cmd = [
        podman,
        "run",
        "--rm",
        "--security-opt",
        "label=disable",
        "--mount",
        f"type=bind,source={repo_root},target=/workspace,ro",
        "-w",
        "/workspace",
        IMAGE,
        "fs",
        "--format",
        "cyclonedx",
        "--output",
        f"/workspace/{output_path.relative_to(repo_root)}",
        "/workspace",
    ]
    print("Running:", " ".join(cmd))
    proc = subprocess.run(cmd, check=False)
    if proc.returncode == 0:
        print(f"SBOM saved to {output_path}")
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
