# Debian/Ubuntu Packaging Skeleton

The `client/` and `server/` folders hold placeholder `control` files and notes for producing `.deb` packages. Expectations:

- Use the PyInstaller artifacts (`client/dist/PlayPalace`, `server/dist/PlayPalaceServer`) as payloads.
- Install files under `/opt/playpalace/<component>/` and expose launchers or systemd units.
- Keep configurations under `/etc/playpalace/` and preserve user edits across upgrades.
- Build packages via `dpkg-deb --build <component>` once `DEBIAN/` metadata (control, postinst, prerm, etc.) is complete.

Separate packages ensure lightweight installs and align with repository layout.
