#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
DIST_DIR="$ROOT/packaging/installers/dist/linux/arch"
CLIENT_PKG=$(ls -1 "$DIST_DIR"/playpalace-client-*.pkg.tar.* | sort | tail -n1)
SERVER_PKG=$(ls -1 "$DIST_DIR"/playpalace-server-*.pkg.tar.* | sort | tail -n1)
CLIENT_REL=${CLIENT_PKG#"$ROOT/"}
SERVER_REL=${SERVER_PKG#"$ROOT/"}

IMAGE=${PLAYPALACE_ARCH_TEST_IMAGE:-docker.io/jrei/systemd-arch:latest}
CONTAINER="playpalace-arch-test-$$"
COMMON_FLAGS=(--privileged --name "$CONTAINER" --systemd=true --tmpfs /tmp --tmpfs /run -v "$ROOT:/workspace:Z" -v /sys/fs/cgroup:/sys/fs/cgroup:ro)

podman run "${COMMON_FLAGS[@]}" -d "$IMAGE"
trap 'podman rm -f "$CONTAINER" >/dev/null 2>&1 || true' EXIT

podman exec "$CONTAINER" bash -c "set -euo pipefail
pacman -Sy --noconfirm --needed base-devel
pacman -U --noconfirm /workspace/$CLIENT_REL
pacman -U --noconfirm /workspace/$SERVER_REL
systemctl daemon-reload
systemctl enable playpalace-server.service
systemctl start playpalace-server.service
systemctl status playpalace-server.service --no-pager
/opt/playpalace/client/PlayPalace --help >/dev/null 2>&1 || true"

echo "Arch package smoke test passed"
