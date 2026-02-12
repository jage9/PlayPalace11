# Debian/Ubuntu Server Package Skeleton

Files in this folder provide placeholders for a `playpalace-server` `.deb`:

- `control` – edit metadata, dependencies, and version before running `dpkg-deb --build`.
- Create `postinst`/`prerm` scripts later to copy `/opt/playpalace/server/config.example.toml` into `/etc/playpalace/config.toml` and manage the systemd unit.
- Package payload should include the PyInstaller server build (from `server/dist/PlayPalaceServer`) and install it under `/opt/playpalace/server/`, plus `/lib/systemd/system/playpalace-server.service`.

Use the same `%PROGRAMDATA%` config layout by defaulting to `/etc/playpalace/` on Linux, ensuring upgrades don’t clobber user configs.
