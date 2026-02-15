# Arch Linux Packaging Skeleton

`client/` and `server/` provide PKGBUILD stubs that install the PyInstaller builds into `/opt/playpalace/<component>/` and expose simple launchers. Invoke `./packaging/installers/linux/scripts/build_arch.sh` (from any directory) to handle tarball generation, rewrite `pkgver`, copy the desktop entry/systemd unit into `source`, and drive `makepkg` in an Arch container.

To publish packages manually:
1. Update `pkgver/pkgrel` (handled automatically in CI, but document expected values).
2. Run `updpkgsums` after pointing `source` to actual tarballs if you build by hand.
3. Use `makepkg -si` or push to AUR repositories (`playpalace-client-bin`, `playpalace-server-bin`).
4. Ensure systemd units/configs live under `/usr/lib/systemd/system/` and `/etc/playpalace/` (current PKGBUILD installs the unit from `packaging/installers/linux/systemd`).
