# Developer hook workflow

These notes cover how to enable the shared git hooks on Windows, WSL, and Linux.

## Prerequisites
- Python 3.13+ (already required by the repo)
- [`uv`](https://astral.sh/uv) available on `PATH`
- [`pre-commit`](https://pre-commit.com); install it into the uv tool space via `uv tool install pre-commit`

## One-time setup
1. From the repo root run `uv tool run pre-commit install --install-hooks`.
2. (Optional) Run `uv tool run pre-commit run --all-files` to warm caches.
3. On Windows/WSL, ensure the hook scripts remain executable:
   - WSL/git-bash automatically honors the `chmod +x` bits.
   - If you clone via Windows-native Git, run `git update-index --chmod=+x scripts/hooks/*.py` once or rerun `pre-commit install` from WSL.

## What runs on each commit?
- **General hygiene:** `check-added-large-files`, `check-merge-conflict`, `detect-private-key`, `end-of-file-fixer`, `trailing-whitespace` (markdown-aware).
- **Dependency safety:** `uv-lock` re-locks `server/uv.lock` or `clients/desktop/uv.lock` when the corresponding `pyproject.toml` changes. `sync-with-uv` keeps tool versions in `.pre-commit-config.yaml` synchronized with the `uv.lock` entries.
- **Source checks:**
  - `scripts/hooks/regen_packet_schema.py` reruns `uv run python tools/export_packet_schema.py` any time `server/network/packet_models.py` changes, so generated JSON stays fresh.
  - `scripts/hooks/run_ruff.py` runs `uv tool run ruff check` over `server/` and `clients/desktop/` with only the fatal rule set (`E9`, `F63`, `F7`). This catches syntax errors, undefined names, and stray break/continue issues without blocking stylistic cleanups.
  - `scripts/hooks/check_packet_schema_sync.py` fails if `server/packet_schema.json` and `clients/desktop/packet_schema.json` drift even after regeneration.

## Tips for different environments
- **Windows-only devs:** set `core.autocrlf true` (default) and leave `.gitattributes` as checked in; LF endings are enforced for Python/JSON/TOML while `.bat`/`.ps1` stay CRLF.
- **WSL devs editing via Windows IDEs:** run `git config core.autocrlf input` inside WSL to avoid back-and-forth conversions, and rely on `.gitattributes` to normalize on commit.
- **Linux/macOS devs:** nothing special beyond having `uv` on PATH. Hooks work inside plain bash/zsh.

## Manual execution
- Run every hook (default stage): `uv tool run pre-commit run --all-files`.
- Run all manual/pre-push hooks (Bandit, Xenon, Vulture, Trivy, hadolint, Podman smoke tests): `uv tool run pre-commit run --hook-stage manual --all-files`.
- Run one hook by name, e.g. `uv tool run pre-commit run hadolint-containerfiles` or `uv tool run pre-commit run bandit-security`.
- Update hook versions quarterly (matching `ci.autoupdate_schedule`): `uv tool run pre-commit autoupdate && uv tool run pre-commit run --all-files`.

## Manual/pre-push hooks available now
- **Security/compliance:** `bandit-security`, `trivy-vulnerability-scan`, `trivy-sbom`.
- **Code quality:** `xenon-complexity`, `vulture-deadcode`.
- **Containers:** `hadolint-containerfiles`, `podman-smoke-server`, `podman-smoke-client` (both rebuild the shared base and component image via Podman).
- All of the above are optional locally but wired into the config so CI can invoke them with `uv tool run pre-commit run --hook-stage manual --all-files`.
