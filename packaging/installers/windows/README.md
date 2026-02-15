# Windows Installer Notes

This directory hosts early WiX v4 scaffolding for the single MSI that packages both the PlayPalace client and server.

## Current Layout
- `wix/PlayPalace.wxs` – base product definition with placeholder features, directory tree, component groups, and WiX custom actions.
- `wix/locales/en-us.wxl` – default localization strings; add one file per locale using the same IDs.
- `wix/assets/` – temporary banner/dialog/icon bitmaps plus `LICENSE_PLACEHOLDER.rtf`. Replace these when final artwork and EULA text are ready.
- `configure_server.ps1` – helper invoked by custom actions to ensure `%PROGRAMDATA%\PlayPalace\config.toml` exists and to apply wizard-provided host/port/SSL values.
- `generate_self_signed.ps1` – optional utility to mint a self-signed certificate using PowerShell's `New-SelfSignedCertificate`. The installer dialog can call this when the user requests automatic cert creation.

## Building the MSI (draft workflow)
1. Build the client binary via `clients/desktop/build.ps1` so `clients/desktop/dist/PlayPalace/PlayPalace.exe` exists.
2. Build the server binary via `server/build.ps1` so `server/dist/PlayPalaceServer.exe` exists.
3. From `packaging/installers/windows/wix/`, run WiX v4 (after installing `wix.exe` and ensuring it is on PATH):
   ```powershell
   wix build PlayPalace.wxs -arch x64 -loc locales/en-us.wxl -out ..\dist\PlayPalace.msi
   ```
   The `ClientSource` and `ServerSource` defines inside `PlayPalace.wxs` point at the default PyInstaller output folders; adjust if artifacts move.

## Custom action inputs
The MSI defines the following public properties, intended to be bound to a custom dialog:

| Property | Purpose | Default |
| --- | --- | --- |
| `SERVERHOST` | Service bind address, passed to `PlayPalaceServer.exe --host`. | `0.0.0.0` |
| `SERVERPORT` | TCP port exposed by the Windows service. | `8000` |
| `SERVERALLOWINSECURE` | `1` to set `[network].allow_insecure_ws = true`. | `0` |
| `SERVERENABLESSL` | `1` if certificates are provided/generated (forces `[network].allow_insecure_ws = false`). | `0` |
| `SERVERCERTPATH` | Absolute path to an existing certificate. | empty |
| `SERVERKEYPATH` | Absolute path to the key/private bundle. | empty |

When `ServerFeature` is selected, the installer sets a deferred `ConfigureServerAction` command (via `CustomActionData`) and runs `packaging\installers\windows\configure_server.ps1` after `InstallFiles`. The script copies `config.example.toml` into `%PROGRAMDATA%\PlayPalace\config.toml` (if missing), clamps `[network].allow_insecure_ws`, and stores any SSL paths so the Windows service and the user’s edits share one config file.

## Installer UI
`PlayPalace.wxs` now injects a `ServerConfigDlg` after the standard `InstallDirDlg` whenever the Server feature is selected on a fresh install. The dialog captures host, port, insecure toggle, and SSL settings while dynamically disabling the insecure checkbox once TLS is enabled. Certificate/key path fields only activate when the SSL checkbox is checked. The “Generate self-signed” button writes files to `%PROGRAMDATA%\PlayPalace\ssl\` and automatically populates the certificate/key fields; the “Validate paths” button ensures both files exist before the installer proceeds. `VerifyReadyDlg`’s Back button also returns to the config dialog in this case so values are easy to adjust before installation continues.

## Pending Work
1. Add Start Menu shortcuts/icons for the server config wizard, documentation URL, and service troubleshooting notes.
2. Localize `*.wxl` for additional languages alongside the Fluent client/server translations.
3. Replace banner/icon/license placeholders with branded assets and the final EULA.
4. Document how to import the self-signed Authenticode cert for internal builds (see `docs/trust-setup.md`); once we obtain a CA-issued cert, replace this with standard signing instructions.
5. Hook automated builds (CI) so PyInstaller outputs flow into `packaging/installers/dist/` and WiX runs on each tagged release (currently covered by `.github/workflows/installers.yml` but still considered draft).
