# Linux Packaging Plan (Draft)

Linux distributions will ship separate packages for the server and client so administrators can install only what they need. The initial target families are:

1. **Debian/Ubuntu (dpkg/apt)** – build `playpalace-server` and `playpalace-client` `.deb` packages. Server package should install systemd units, drop configuration templates under `/etc/playpalace/`, and reuse the existing `server/config.example.toml` flow; client package installs the PyInstaller build plus desktop files.
2. **Red Hat / Oracle / Fedora (RPM)** – parallel spec files for `playpalace-server` and `playpalace-client`, installing units under `/usr/lib/systemd/system/` and SELinux policies if necessary.
3. **Arch Linux** – PKGBUILDs for each component, following the rolling-release guidelines and ideally publishing to an AUR namespace.

Scripts (run from anywhere, e.g., `./packaging/installers/linux/scripts/build_deb.sh`):
- `scripts/build_deb.sh` builds `.deb` artifacts for both client and server by invoking the new `clients/desktop/build.sh` and `server/build.sh` PyInstaller steps, staging files under `/opt/playpalace/`, and running `dpkg-deb`.
- `scripts/build_rpm.sh` mirrors the process for `.rpm` packages using `rpmbuild`, tarballing the PyInstaller outputs and installing the systemd unit/desktop entry from `packaging/installers/linux/systemd/` and `packaging/installers/linux/client/`.
- `scripts/build_arch.sh` runs `makepkg` in an Arch environment (CI uses `uraimo/run-on-arch-action`) after preparing tarballs and copying the desktop/service sources, emitting `.pkg.tar.zst` files per component.
- `scripts/test_deb.sh`, `test_rpm.sh`, `test_arch.sh` spin up rootless podman containers with systemd enabled to install the freshly built packages, start services, and capture status for CI smoke tests.

When we flesh the remaining formats out, place distro-specific tooling under `packaging/installers/linux/<family>/` (e.g., `debian/`, `rpm/`, `arch/`). Each package should:

- Pull artifacts from the same PyInstaller outputs used by the Windows MSI so binaries stay consistent.
- Provide post-install scripts to copy `config.example.toml` to `/etc/playpalace/config.toml` (server) without overwriting user edits on upgrades.
- Register appropriate system services (`systemd` units for now).
- Include localized desktop entries/icons on the client package.

These notes will expand as we prototype the first packages.
