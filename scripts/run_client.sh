#!/usr/bin/env bash
# PlayPalace Client Launcher via pinned Nix flake

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CLIENT_DIR="$PROJECT_ROOT/clients/desktop"

cd "$CLIENT_DIR"

read -r -d '' LAUNCH_SCRIPT <<'INNER'
export G_MESSAGES_DEBUG=""
export GTK_DISABLE_GAIL_WARNING=1
if [ -n "${PLAYPALACE_USE_XVFB:-}" ]; then
  xvfb-run -s "-screen 0 ${PLAYPALACE_XVFB_SIZE:-1024x768x24}" python client.py "$@"
else
  python client.py "$@"
fi
INNER

nix --extra-experimental-features "nix-command flakes" \
  develop "$PROJECT_ROOT" \
  --command bash -c "$LAUNCH_SCRIPT" run-client "$@"
