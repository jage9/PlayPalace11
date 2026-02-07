#!/usr/bin/env bash
set -euo pipefail

# Helper for running client pytest suites inside `nix develop`.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
CLIENT_DIR="${REPO_ROOT}/client"
PY_PREFIX="${REPO_ROOT}/.nix-python"
PYTHON_SITE="${PY_PREFIX}/lib/python3.11/site-packages"
REQUIRED_PACKAGES=(pytest pydantic)

if [[ ! -d "${PYTHON_SITE}" ]]; then
    mkdir -p "${PYTHON_SITE}"
fi

echo "Ensuring client test dependencies are installed in ${PY_PREFIX}"
python -m pip install --quiet --prefix "${PY_PREFIX}" "${REQUIRED_PACKAGES[@]}"

export PYTHONPATH="${PYTHON_SITE}:${PYTHONPATH:-}:${CLIENT_DIR}"
cd "${CLIENT_DIR}"

DEFAULT_TESTS=("tests/test_network_manager.py" "tests/test_main_window_packets.py" "tests/test_main_window_startup.py")
if [[ $# -gt 0 ]]; then
    python -m pytest "$@"
else
    python -m pytest "${DEFAULT_TESTS[@]}"
fi
