# RPM Packaging Skeleton

This directory is split into `client/` and `server/` placeholders. Each contains a `.spec` template referencing a tarball built from the corresponding PyInstaller artifact (client: `clients/desktop/dist/PlayPalace`, server: `server/dist/PlayPalaceServer`).

Run `./packaging/installers/linux/scripts/build_rpm.sh` (location-agnostic) to automate steps (1)-(4): the script tars the PyInstaller outputs, copies the systemd unit/desktop entry as `Source1`, rewrites `Version` fields, and invokes `rpmbuild -ba` with `_topdir` pointing at `packaging/installers/linux/build/rpm`.
