# Nix vs. Containerfile workflows

PlayPalace already ships `flake.nix`, `shell.nix`, and multiple Containerfiles. This note captures when to reach for each approach and how their tooling overlaps.

## When Nix shines
- **Single-source dependency lock:** the flake captures Python, system libs, and tooling (uv, pre-commit, etc.) so contributors on Linux, macOS, or WSL get the same versions without rebuilding images.
- **Fast iteration:** `nix develop` enters the environment instantly after the first build, which suits frequent test runs or hook development.
- **Composable CI:** Nix derivations already power `scripts/nix_server_pytest.sh`; CI jobs can reuse the same derivation to guarantee parity with local dev.

## When a Containerfile is preferable
- **Deployment parity:** images (built via `podman build`, then run with `podman run`) mirror production packaging, so server binaries, OS hardening, and runtime flags match what gets deployed.
- **Multi-platform distribution:** containers can be pushed to registries for QA or player-hosted servers without requiring Nix.
- **Toolchain isolation:** images decouple from host package managers, which helps Windows hosts running PlayPalace via WSL or bare metal.

## Containerfiles in this repo
- `packaging/containers/base/Containerfile` defines the uv-enabled base image shared by every other image. Build it first via `podman build packaging/containers/base -t playpalace/base:latest`.
- `server/Containerfile` builds the websocket game server. Build with `podman build -f server/Containerfile server -t playpalace/server:latest` (after the base image exists) and run via `podman run --rm -p 8000:8000 playpalace/server:latest`.
- `clients/desktop/Containerfile` bundles the wxPython desktop client for headless testing or remote GUI sessions. Build with `podman build -f clients/desktop/Containerfile clients/desktop -t playpalace/client:latest`. Run with X11/Wayland forwarding, e.g. `podman run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix playpalace/client:latest python client.py`.

## Blended workflows
- **Hadolint as a bridge:** use the `hadolint-containerfiles` manual hook (`uv tool run pre-commit run hadolint-containerfiles`) or directly invoke `podman run --rm --mount type=bind,source=$PWD,target=/workspace,ro docker.io/hadolint/hadolint:latest packaging/containers/base/Containerfile server/Containerfile clients/desktop/Containerfile` so devs and CI lint identical Containerfiles before builds.
- **Podman smoke hooks:** run `uv tool run pre-commit run podman-smoke-server` or `podman-smoke-client` to build the base + component image and execute a quick runtime check. CI can reuse the same hooks via `uv tool run pre-commit run --hook-stage manual --all-files`.
- **Nix inside containers:** if desired, the Containerfile can call `nix develop` to produce artifacts that are then copied into the image, keeping single-source dependency logic while still shipping containerized images.

## Choosing between them
| Scenario | Prefer Nix | Prefer Containerfile |
| --- | --- | --- |
| Editing Python/game logic daily | ✅ fastest with `nix develop` | ❌ unnecessary rebuilds |
| Validating production packaging | ⚠️ requires extra scripts | ✅ `podman build` tests exact image |
| Third-party distribution | ⚠️ users need Nix tooling | ✅ ship container or tarball |
| Hook/CI tooling | ✅ `scripts/nix_*.sh` already wrap it | ✅ reuse manual hooks via `podman` + hadolint |

In short: keep day-to-day dev flows inside Nix shells, then rely on Containerfile + podman (linted by hadolint) when verifying deployable artifacts or publishing images. Both paths share the same uv/pre-commit hooks, so guardrails remain consistent regardless of the environment.
