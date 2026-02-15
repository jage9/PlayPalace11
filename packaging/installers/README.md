# Installer Overview

This directory now groups platform-specific packaging assets. Current layout:

- `windows/` – WiX v4 project, PowerShell helpers, and documentation for producing the MSI that bundles the PyInstaller client/server builds.
- `linux/` – packaging notes and stubs for future `.deb`, `.rpm`, and Arch packages (each split into `client/` and `server/` payloads).

Add additional platforms (e.g., macOS) as peer directories when needed so each environment keeps its own tooling without stepping on others.

## Running packaging scripts

- Invoke helpers directly via repo-relative paths (for example `./packaging/installers/linux/scripts/build_deb.sh`). Each script computes the repository root from its own location, so you do **not** need to `cd` to the project root first.
- Export any environment variables (signing key IDs, `PLAYPALACE_APPEND_SHA`, custom container images) *before* running the scripts so those values are visible regardless of your current working directory.
- When documenting new commands, always include the explicit path to the script or binary you expect contributors to call. This avoids implying that CWD must be the repository root and keeps instructions resilient to future path changes.
