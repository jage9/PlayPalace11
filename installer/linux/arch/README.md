# Arch Linux Packaging Skeleton

`client/` and `server/` provide PKGBUILD stubs that install the PyInstaller builds into `/opt/playpalace/<component>/` and expose simple launchers. `installer/linux/scripts/build_arch.sh` handles tarball generation, rewrites `pkgver`, copies the desktop entry/systemd unit into `source`, and drives `makepkg` in an Arch container.

To publish packages manually:
1. Update `pkgver/pkgrel` (handled automatically in CI, but document expected values).
2. Run `updpkgsums` after pointing `source` to actual tarballs if you build by hand.
3. Use `makepkg -si` or push to AUR repositories (`playpalace-client-bin`, `playpalace-server-bin`).
4. Ensure systemd units/configs live under `/usr/lib/systemd/system/` and `/etc/playpalace/` (current PKGBUILD installs the unit from `installer/linux/systemd`). 
