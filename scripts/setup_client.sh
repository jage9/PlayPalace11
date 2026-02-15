#!/usr/bin/env bash
# Sync client dependencies inside the pinned Nix environment

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CLIENT_DIR="$PROJECT_ROOT/clients/desktop"

cd "$CLIENT_DIR"

nix --extra-experimental-features "nix-command flakes" \
  develop "$PROJECT_ROOT" \
  --command uv sync --no-install-project
