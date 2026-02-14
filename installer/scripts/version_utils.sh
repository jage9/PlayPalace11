#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}" )/.." && pwd)"

read_pyproject_version() {
  local project_dir="$1"
  python - <<PY
import pathlib, tomllib
path = pathlib.Path(r"${ROOT}") / pathlib.Path("$project_dir/pyproject.toml")
data = tomllib.loads(path.read_text())
print(data["project"]["version"])
PY
}

maybe_append_sha() {
  local base="$1"
  if [[ "${PLAYPALACE_APPEND_SHA:-0}" == "1" ]]; then
    local sha
    sha=$(git -C "$ROOT" rev-parse --short HEAD)
    echo "${base}+g${sha}"
  else
    echo "$base"
  fi
}

get_client_version() {
  local version
  version=$(read_pyproject_version client)
  maybe_append_sha "$version"
}

get_server_version() {
  local version
  version=$(read_pyproject_version server)
  maybe_append_sha "$version"
}
