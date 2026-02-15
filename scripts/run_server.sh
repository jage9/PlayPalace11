#!/usr/bin/env bash
# PlayPalace Server Launcher via pinned Nix flake

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SERVER_DIR="$PROJECT_ROOT/server"

cd "$SERVER_DIR"

nix --extra-experimental-features "nix-command flakes" \
  develop "$PROJECT_ROOT" \
  --command bash -c 'uv run python main.py "$@"' run-server "$@"
