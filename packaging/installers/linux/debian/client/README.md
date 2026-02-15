# Debian/Ubuntu Client Package Skeleton

- `control` captures the basic metadata. Update Version/Depends per release.
- Add `postinst` script to register a desktop entry under `/usr/share/applications/playpalace.desktop` and copy icons into `/usr/share/icons/hicolor/...`.
- Payload should copy the PyInstaller client folder to `/opt/playpalace/client/` and symlink `/usr/bin/playpalace-client` to its launcher script.

Separate Debian packages (`playpalace-server` and `playpalace-client`) keep deployments minimal and align with upstream repository layout.
