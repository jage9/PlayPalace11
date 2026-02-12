#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
DIST_DIR="$ROOT/installer/dist/linux/deb"
BUILD_ROOT="$ROOT/installer/linux/build/deb"

mkdir -p "$DIST_DIR" "$BUILD_ROOT"

source "$ROOT/installer/scripts/version_utils.sh"

pushd "$ROOT/client" >/dev/null
if [ ! -d dist/PlayPalace ]; then
  ./build.sh
fi
popd >/dev/null

pushd "$ROOT/server" >/dev/null
if [ ! -f dist/PlayPalaceServer ] && [ ! -d dist/PlayPalaceServer ]; then
  ./build.sh
fi
popd >/dev/null

CLIENT_VERSION=$(get_client_version)
SERVER_VERSION=$(get_server_version)

sign_deb() {
  local deb="$1"
  if [[ -n "${PLAYPALACE_SIGNING_KEY_ID:-}" ]]; then
    echo "Signing $(basename "$deb") with key $PLAYPALACE_SIGNING_KEY_ID"
    dpkg-sig --sign builder -k "$PLAYPALACE_SIGNING_KEY_ID" "$deb"
  else
    echo "Skipping signing for $(basename "$deb")"
  fi
}

build_client() {
  local pkgdir="$BUILD_ROOT/playpalace-client"
  rm -rf "$pkgdir"
  mkdir -p "$pkgdir/DEBIAN" "$pkgdir/opt/playpalace/client" "$pkgdir/usr/bin" "$pkgdir/usr/share/applications"
  cp "$ROOT/installer/linux/debian/client/control" "$pkgdir/DEBIAN/control"
  sed -i "s/^Version:.*/Version: $CLIENT_VERSION/" "$pkgdir/DEBIAN/control"
  cp "$ROOT/installer/linux/debian/client/postinst" "$pkgdir/DEBIAN/postinst"
  chmod 0755 "$pkgdir/DEBIAN/postinst"
  rsync -a --delete "$ROOT/client/dist/PlayPalace/" "$pkgdir/opt/playpalace/client/"
  cat <<'LAUNCH' > "$pkgdir/usr/bin/playpalace-client"
#!/bin/sh
exec /opt/playpalace/client/PlayPalace "$@"
LAUNCH
  chmod 0755 "$pkgdir/usr/bin/playpalace-client"
  install -m 0644 "$ROOT/installer/linux/client/playpalace.desktop" "$pkgdir/usr/share/applications/playpalace.desktop"
  local deb="$DIST_DIR/playpalace-client_${CLIENT_VERSION}_amd64.deb"
  dpkg-deb --build "$pkgdir" "$deb"
  sign_deb "$deb"
}

build_server() {
  local pkgdir="$BUILD_ROOT/playpalace-server"
  rm -rf "$pkgdir"
  mkdir -p "$pkgdir/DEBIAN" "$pkgdir/opt/playpalace/server" "$pkgdir/usr/bin" "$pkgdir/lib/systemd/system"
  cp "$ROOT/installer/linux/debian/server/control" "$pkgdir/DEBIAN/control"
  sed -i "s/^Version:.*/Version: $SERVER_VERSION/" "$pkgdir/DEBIAN/control"
  cp "$ROOT/installer/linux/debian/server/postinst" "$pkgdir/DEBIAN/postinst"
  cp "$ROOT/installer/linux/debian/server/prerm" "$pkgdir/DEBIAN/prerm"
  chmod 0755 "$pkgdir/DEBIAN/postinst" "$pkgdir/DEBIAN/prerm"
  install -m 0755 "$ROOT/server/dist/PlayPalaceServer" "$pkgdir/opt/playpalace/server/PlayPalaceServer"
  install -m 0644 "$ROOT/server/config.example.toml" "$pkgdir/opt/playpalace/server/config.example.toml"
  cat <<'LAUNCH' > "$pkgdir/usr/bin/playpalace-server"
#!/bin/sh
exec /opt/playpalace/server/PlayPalaceServer "$@"
LAUNCH
  chmod 0755 "$pkgdir/usr/bin/playpalace-server"
  install -m 0644 "$ROOT/installer/linux/systemd/playpalace-server.service" "$pkgdir/lib/systemd/system/playpalace-server.service"
  local deb="$DIST_DIR/playpalace-server_${SERVER_VERSION}_amd64.deb"
  dpkg-deb --build "$pkgdir" "$deb"
  sign_deb "$deb"
}

build_client
build_server

echo "Debian packages written to $DIST_DIR"
