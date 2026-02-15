# Installer Overview

This directory now groups platform-specific packaging assets. Current layout:

- `windows/` – WiX v4 project, PowerShell helpers, and documentation for producing the MSI that bundles the PyInstaller client/server builds.
- `linux/` – packaging notes and stubs for future `.deb`, `.rpm`, and Arch packages (each split into `client/` and `server/` payloads).

Add additional platforms (e.g., macOS) as peer directories when needed so each environment keeps its own tooling without stepping on others.
