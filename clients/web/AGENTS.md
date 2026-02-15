# Web Client Notes

## Scope
- This folder contains the browser client for PlayPalace v11.
- Keep changes focused and aligned with server packet behavior.

## Versioning
- `version.js` is the single source of truth for web client version.
- Increment `window.PLAYPALACE_WEB_VERSION` on every commit in this branch.
- Format is `YYYY.MM.DD.N`.
- `N` is monotonic and should not reset when the date changes (example: after `2026.02.08.32`, use `2026.02.09.33`).
- `index.html` uses that value for `app.js?v=...` cache busting and footer display.

## Deployment Config
- Deployment-specific settings belong in `config.js` (copied from `config.sample.js`).
- Do not put maintainer-only values (like app version) in deployment config.

## Packet Schema Sync
- Keep `clients/web/packet_schema.json` in sync with `clients/desktop/packet_schema.json`.
- After packet model changes, regenerate schema from `server/tools/export_packet_schema.py` and copy the updated client schema into `clients/web/packet_schema.json`.

## Input/Accessibility
- Preserve keyboard-first behavior and screen-reader friendliness.
- Avoid focus jumps unless explicitly required by flow (dialogs, reconnect, etc.).
- Keep menu selection stable across refresh packets unless server sends an explicit selection.

## Audio
- Default sound base URL is `./sounds`.
- Keep music/effects/ambience handling consistent with the desktop client where practical.
