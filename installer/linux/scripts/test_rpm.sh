#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}" )/../../.." && pwd)"
DIST_DIR="$ROOT/installer/dist/linux/rpm"
CLIENT_RPM=$(ls -1 "$DIST_DIR"/playpalace-client-*.rpm | sort | tail -n1)
SERVER_RPM=$(ls -1 "$DIST_DIR"/playpalace-server-*.rpm | sort | tail -n1)
CLIENT_REL=${CLIENT_RPM#"$ROOT/"}
SERVER_REL=${SERVER_RPM#"$ROOT/"}

IMAGE=${PLAYPALACE_RPM_TEST_IMAGE:-quay.io/centos/centos:stream9}
CONTAINER="playpalace-rpm-test-$$"
COMMON_FLAGS=(--privileged --name "$CONTAINER" --systemd=true --tmpfs /tmp --tmpfs /run -v "$ROOT:/workspace:Z" -v /sys/fs/cgroup:/sys/fs/cgroup:ro)

podman run "${COMMON_FLAGS[@]}" -d "$IMAGE"
trap 'podman rm -f "$CONTAINER" >/dev/null 2>&1 || true' EXIT

podman exec "$CONTAINER" bash -c "set -euo pipefail
dnf install -y systemd sudo
rpm -i /workspace/$CLIENT_REL || dnf install -y /workspace/$CLIENT_REL
rpm -i /workspace/$SERVER_REL || dnf install -y /workspace/$SERVER_REL
systemctl daemon-reload
systemctl enable playpalace-server.service
systemctl start playpalace-server.service
systemctl status playpalace-server.service --no-pager
/opt/playpalace/server/PlayPalaceServer --help >/dev/null 2>&1 || true
/opt/playpalace/client/PlayPalace --help >/dev/null 2>&1 || true"

echo "RPM package smoke test passed"
