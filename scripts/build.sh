#!/usr/bin/env bash
# Build PlayPalace distribution packages

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

read -r -d '' BUILD_COMMAND <<'RUN'
echo "Building PlayPalace packages..."
echo "================================"

echo "Building server..."
cd "$PROJECT_ROOT/server"
uv sync --all-extras
uv build

echo "Building client..."
cd "$PROJECT_ROOT/clients/desktop"
uv sync
uv build

echo ""
echo "Build complete!"
echo "Packages created in:"
echo "  $PROJECT_ROOT/server/dist/"
echo "  $PROJECT_ROOT/clients/desktop/dist/"
RUN

nix --extra-experimental-features "nix-command flakes" \
  develop "$PROJECT_ROOT" \
  --command bash -c "$BUILD_COMMAND"
