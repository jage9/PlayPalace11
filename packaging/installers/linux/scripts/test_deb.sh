#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
DIST_DIR="$ROOT/packaging/installers/dist/linux/deb"
CLIENT_DEB=$(ls -1 "$DIST_DIR"/playpalace-client_*_amd64.deb | sort | tail -n1)
SERVER_DEB=$(ls -1 "$DIST_DIR"/playpalace-server_*_amd64.deb | sort | tail -n1)
CLIENT_REL=${CLIENT_DEB#"$ROOT/"}
SERVER_REL=${SERVER_DEB#"$ROOT/"}

IMAGE=${PLAYPALACE_DEB_TEST_IMAGE:-docker.io/jrei/systemd-ubuntu:24.04}
CONTAINER="playpalace-deb-test-$$"
COMMON_FLAGS=(--privileged --name "$CONTAINER" --systemd=true --tmpfs /tmp --tmpfs /run -v "$ROOT:/workspace:Z" -v /sys/fs/cgroup:/sys/fs/cgroup:ro)

podman run "${COMMON_FLAGS[@]}" -d "$IMAGE"
trap 'podman rm -f "$CONTAINER" >/dev/null 2>&1 || true' EXIT

for i in $(seq 1 30); do
  if podman inspect -f '{{.State.Running}}' "$CONTAINER" 2>/dev/null | grep -q true; then break; fi
  sleep 1
done

podman exec "$CONTAINER" bash -c "set -euo pipefail
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y ca-certificates
apt-get install -y /workspace/$CLIENT_REL
apt-get install -y /workspace/$SERVER_REL
systemctl daemon-reload
systemctl enable playpalace-server.service
systemctl start playpalace-server.service
systemctl status playpalace-server.service --no-pager
/opt/playpalace/client/PlayPalace --help >/dev/null 2>&1 || true
test -f /etc/playpalace/config.toml"

echo "Debian package smoke test passed"
