# PlayPalace - Running on NixOS

## Quick Start

### Server (Ready to Use)
```bash
# Start the server
./scripts/run_server.sh

# Or with custom port
./scripts/run_server.sh --port 9000

# With SSL
./scripts/run_server.sh --ssl-cert /path/to/cert.pem --ssl-key /path/to/key.pem
```

### Client

**Status:** Client works in **silent mode** (no sound effects) unless audio is configured.

```bash
# Run client (silent mode is OK)
./scripts/run_client.sh

# Headless GUI smoke tests (launches Xvfb screen 0 @ 1024x768x24)
PLAYPALACE_USE_XVFB=1 ./scripts/run_client.sh
```

The launcher now enters the pinned flake devshell automatically—no extra `.venv` or manual `pip install` needed.

**Expected Warnings (can be ignored):**
- `Gtk-WARNING`: UI layout warnings (cosmetic only)
- `Cannot find Speech Dispatcher`: Accessibility feature (optional)
- `Cannot find espeak`: Text-to-speech (optional)
- `Warning: Could not initialize audio output`: Audio device not available (silent mode)

The client functions normally for gameplay despite these warnings.

#### Creating Your Account

**There are no default accounts!** You need to register:

1. **First user registered** = Auto-approved as Server Owner (full admin)
2. **Additional users** = Require admin approval

To create your admin account:
1. Start server: `./scripts/run_server.sh`
2. Start client: `./scripts/run_client.sh`
3. Click "Register" and choose your username/password
4. You'll be logged in as Server Owner (first user only)

#### Enabling Audio (Optional)

If you want sound effects, configure an audio system:

```bash
# Check if audio works
speaker-test -t wav -c 2

# For PulseAudio
pulseaudio --start

# For PipeWire
systemctl --user start pipewire pipewire-pulse
```

Then restart the client.

## What Works

✅ Server - fully functional  
✅ Client - fully functional (silent mode)  
⚠️  Client audio - requires audio device configuration

## Built Packages

Pre-built wheels are available in:
- `server/dist/playpalace_server-11.0.0-py3-none-any.whl` (637 KB)
- `clients/desktop/dist/playpalace_client-11.0.0-py3-none-any.whl` (53 MB)

## Development

### Running Tests
```bash
# Server tests (enter the flake devshell)
nix --extra-experimental-features "nix-command flakes" \
  develop . \
  --command bash -c "cd server && uv run pytest"

# Quick verification
./scripts/test_run.sh
```

### Building from Source
```bash
./scripts/build.sh
```

## Recent Fixes (2026-01-30)

- ✅ Fixed audio initialization gracefully falls back to silent mode
- ✅ Fixed wxAssertionError spam from menu_list.py
- ✅ Fixed RuntimeError when closing client window
- ✅ Fixed ambience playback crash in silent mode

## Technical Notes

- **Pinned environment:** `flake.nix` / `flake.lock` capture the exact nixpkgs revision plus Python wheels (wxPython, websockets 16, accessible-output2, sound-lib, etc.).
- **Server:** Uses uv for dependency management but now runs inside the pinned flake devshell.
- **Client:** Uses wxPython + the same pinned Python deps—no ad-hoc `.venv`.
- **Audio:** Client uses the BASS audio library which requires a functional audio device.
- **Silent/headless:** When no audio device is found, the client runs without sound. Set `PLAYPALACE_USE_XVFB=1` for GUI testing on headless builders.

## Future: Removing Legacy `nix-shell`

When the team is ready to drop legacy tooling entirely:

1. **Delete `shell.nix`:** remove the compatibility file (or replace it with an error) so contributors must use `nix develop`. Update docs/scripts to reference flakes only.
2. **Purge `nix-shell` references:** run `rg 'nix-shell' -n` and replace remaining instructions, CI snippets, or helper scripts with `nix --extra-experimental-features "nix-command flakes" develop …` (or rely on default experimental features if configured globally).
3. **Enable flakes globally:** set `experimental-features = nix-command flakes` in `/etc/nix/nix.conf` or `~/.config/nix/nix.conf` so scripts no longer need to pass the flag explicitly.
4. **Update docs/README:** clearly state that flakes are mandatory and that `nix develop` is the supported entrypoint.
5. **Validate automation:** ensure CI and `test_run.sh` (or any other automation) invoke `nix develop` directly, then delete any fallback wrappers.

Following those steps will leave the repository fully flake-based with no legacy `nix-shell` path.
