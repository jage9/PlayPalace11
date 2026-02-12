# RPM Packaging Skeleton

This directory is split into `client/` and `server/` placeholders. Each contains a `.spec` template referencing a tarball built from the corresponding PyInstaller artifact (client: `client/dist/PlayPalace`, server: `server/dist/PlayPalaceServer`).

The automation for steps (1)-(4) now lives in `installer/linux/scripts/build_rpm.sh`, which tars the PyInstaller outputs, copies the systemd unit/desktop entry as `Source1`, rewrites `Version` fields, and invokes `rpmbuild -ba` with `_topdir` pointing at `installer/linux/build/rpm`.
