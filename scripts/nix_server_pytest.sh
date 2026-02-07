#!/usr/bin/env bash
set -euo pipefail

# Helper for running server pytest suites inside `nix develop`.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

cd "${REPO_ROOT}/server"
if [[ $# -gt 0 ]]; then
    uv run pytest "$@"
else
    uv run pytest
fi
