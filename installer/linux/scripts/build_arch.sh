#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
DIST_DIR="$ROOT/installer/dist/linux/arch"
BUILD_ROOT="$ROOT/installer/linux/build/arch"

mkdir -p "$DIST_DIR" "$BUILD_ROOT"

source "$ROOT/installer/scripts/version_utils.sh"

ensure_pyinstaller() {
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

prepare_sources() {
  local tmp
  tmp=$(mktemp -d)
  rsync -a "$ROOT/client/dist/PlayPalace/" "$tmp/PlayPalaceClient/"
  cp "$ROOT/LICENSE" "$tmp/PlayPalaceClient/"
  tar -C "$tmp" -czf "$BUILD_ROOT/PlayPalaceClient.tar.gz" PlayPalaceClient
  rm -rf "$tmp"

  tmp=$(mktemp -d)
  mkdir -p "$tmp/PlayPalaceServer"
  cp "$ROOT/server/dist/PlayPalaceServer" "$tmp/PlayPalaceServer/PlayPalaceServer"
  cp "$ROOT/server/config.example.toml" "$tmp/PlayPalaceServer/"
  cp "$ROOT/LICENSE" "$tmp/PlayPalaceServer/"
  tar -C "$tmp" -czf "$BUILD_ROOT/PlayPalaceServer.tar.gz" PlayPalaceServer
  rm -rf "$tmp"

  cp "$ROOT/installer/linux/systemd/playpalace-server.service" "$BUILD_ROOT/"
  cp "$ROOT/installer/linux/client/playpalace.desktop" "$BUILD_ROOT/"
}

build_pkg() {
  local component=$1
  local version=$2
  local src_tar=$3
  local extra_source=$4

  local pkgwork="$BUILD_ROOT/${component}-pkg"
  rm -rf "$pkgwork"
  mkdir -p "$pkgwork"
  cp "$ROOT/installer/linux/arch/$component/PKGBUILD" "$pkgwork/PKGBUILD"
  sed -i "s/^pkgver=.*/pkgver=$version/" "$pkgwork/PKGBUILD"
  cp "$src_tar" "$pkgwork/$(basename "$src_tar")"
  if [ -n "$extra_source" ]; then
    cp "$extra_source" "$pkgwork/"
  fi
  pushd "$pkgwork" >/dev/null
  makepkg --clean --force --noconfirm --skipinteg
  if [[ -n "${PLAYPALACE_SIGNING_KEY_ID:-}" ]]; then
    gpg --batch --yes --detach-sign --local-user "$PLAYPALACE_SIGNING_KEY_ID" "$pkgwork"/*.pkg.tar.*
  fi
  popd >/dev/null
  cp "$pkgwork"/*.pkg.tar.* "$DIST_DIR/"
}

ensure_pyinstaller
prepare_sources

build_pkg "client" "$CLIENT_VERSION" "$BUILD_ROOT/PlayPalaceClient.tar.gz" "$BUILD_ROOT/playpalace.desktop"
build_pkg "server" "$SERVER_VERSION" "$BUILD_ROOT/PlayPalaceServer.tar.gz" "$BUILD_ROOT/playpalace-server.service"

echo "Arch packages written to $DIST_DIR"
