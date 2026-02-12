#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
DIST_DIR="$ROOT/installer/dist/linux/rpm"
RPM_TOP="$ROOT/installer/linux/build/rpm"

mkdir -p "$DIST_DIR" "$RPM_TOP"/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

source "$ROOT/installer/scripts/version_utils.sh"

build_pyinstaller() {
  pushd "$ROOT/client" >/dev/null
  if [ ! -d dist/PlayPalace ]; then
    ./build.sh
  fi
  popd >/dev/null

  pushd "$ROOT/server" >/dev/null
  if [ ! -f dist/PlayPalaceServer ]; then
    ./build.sh
  fi
  popd >/dev/null
}

CLIENT_VERSION=$(get_client_version)
SERVER_VERSION=$(get_server_version)

stage_source_archives() {
  local tmp
  # Client tarball
  tmp=$(mktemp -d)
  rsync -a "$ROOT/client/dist/PlayPalace/" "$tmp/PlayPalaceClient/"
  cp "$ROOT/LICENSE" "$tmp/PlayPalaceClient/"
  tar -C "$tmp" -czf "$RPM_TOP/SOURCES/PlayPalaceClient.tar.gz" PlayPalaceClient
  rm -rf "$tmp"

  # Server tarball
  tmp=$(mktemp -d)
  mkdir -p "$tmp/PlayPalaceServer"
  cp "$ROOT/server/dist/PlayPalaceServer" "$tmp/PlayPalaceServer/"
  cp "$ROOT/server/config.example.toml" "$tmp/PlayPalaceServer/"
  cp "$ROOT/LICENSE" "$tmp/PlayPalaceServer/"
  tar -C "$tmp" -czf "$RPM_TOP/SOURCES/PlayPalaceServer.tar.gz" PlayPalaceServer
  rm -rf "$tmp"

  cp "$ROOT/installer/linux/systemd/playpalace-server.service" "$RPM_TOP/SOURCES/"
  cp "$ROOT/installer/linux/client/playpalace.desktop" "$RPM_TOP/SOURCES/"
}

prepare_spec() {
  sed "s/^Version:.*/Version: $CLIENT_VERSION/" "$ROOT/installer/linux/rpm/client/playpalace-client.spec" > "$RPM_TOP/SPECS/playpalace-client.spec"
  sed "s/^Version:.*/Version: $SERVER_VERSION/" "$ROOT/installer/linux/rpm/server/playpalace-server.spec" > "$RPM_TOP/SPECS/playpalace-server.spec"
}

build_rpms() {
  rpmbuild --define "_topdir $RPM_TOP" -ba "$RPM_TOP/SPECS/playpalace-client.spec"
  rpmbuild --define "_topdir $RPM_TOP" -ba "$RPM_TOP/SPECS/playpalace-server.spec"
  mkdir -p "$DIST_DIR"
  cp "$RPM_TOP/RPMS/x86_64"/*.rpm "$DIST_DIR"/
  if [[ -n "${PLAYPALACE_SIGNING_KEY_ID:-}" ]]; then
    echo "Signing RPMs with $PLAYPALACE_SIGNING_KEY_ID"
    rpm --addsign "$DIST_DIR"/*.rpm --define "_gpg_name $PLAYPALACE_SIGNING_KEY_ID"
  else
    echo "Skipping RPM signing"
  fi
}

build_pyinstaller
stage_source_archives
prepare_spec
build_rpms

echo "RPM packages written to $DIST_DIR"
