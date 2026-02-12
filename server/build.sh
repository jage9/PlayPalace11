#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if ! uv run --project . pyinstaller --version >/dev/null 2>&1; then
  echo "PyInstaller not found in uv environment. Installing..."
  uv add --dev pyinstaller pyinstaller-hooks-contrib
fi

echo "Building PlayPalace server executable..."
uv run --project . pyinstaller -y --clean --noconfirm --noconsole --name PlayPalaceServer --hidden-import babel --hidden-import fluent_compiler --hidden-import fluent_compiler.bundle --hidden-import fluent_compiler.resource --hidden-import fluent_compiler.runtime --collect-submodules server --collect-data server --onefile main.py

echo "Server build complete: dist/PlayPalaceServer"
