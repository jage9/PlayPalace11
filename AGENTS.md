# Repository Guidelines

## Project Structure & Module Organization
- `server/` is the v11 game server (modern Python). Core modules live in `server/core/`, game implementations in `server/games/`, shared game helpers in `server/game_utils/`, auth in `server/auth/`, persistence in `server/persistence/`, and localization in `server/messages/`.
- `server/tests/` contains pytest test suites (unit, integration, and play tests).
- `client/` is a wxPython desktop client with UI code under `client/ui/`.
- Design notes live in `server/plans/`.

## Build, Test, and Development Commands
This repo uses Python 3.11+ and `uv` for dependency management.

- Server dev:
  - `cd server && uv sync` — install server deps.
  - `cd server && uv run python main.py` — run server on default `0.0.0.0:8000`.
  - `cd server && uv run python main.py --help` — view server flags (e.g., `--ssl-cert`, `--ssl-key`).
- Client dev:
  - `cd client && uv sync` — install client deps.
  - `cd client && uv run python client.py` — run client.
- Tests:
  - `cd server && uv run pytest` — run all server tests.
  - `cd server && uv run pytest -v` — verbose output.
  - Inside `nix develop .`, helper scripts are available from repo root:
    - `./scripts/nix_server_pytest.sh`
    - `./scripts/nix_client_pytest.sh` (installs pytest/pydantic into `.nix-python/` automatically)

## Coding Style & Naming Conventions
- Python uses 4-space indentation and standard PEP 8 naming: `snake_case` for functions/vars, `CapWords` for classes, `UPPER_SNAKE_CASE` for constants.
- Server state is largely dataclass-based; prefer explicit, imperative state changes in game logic.
- Follow existing patterns in `server/games/` and `server/game_utils/` rather than introducing new abstractions.
- Keep changes minimal and focused; reuse existing helpers and avoid over-engineering.
- Docstrings use Google-style format; keep them updated when behavior changes.

## Testing Guidelines
- Frameworks: `pytest` and `pytest-asyncio`.
- Naming: test files in `server/tests/` use `test_*.py` and test functions use `test_*`.
- Include play tests when adding new games or changing serialization/persistence logic.
## Localization Notes
- When adding or changing strings, update all locales in `server/locales/` (and `languages.ftl` if applicable).

## Commit & Pull Request Guidelines
- Recent commit messages are short, sentence-case descriptions (e.g., “Modernize server networking…”). Follow that style; keep it one line and descriptive.
- PRs should include: a clear summary, testing notes (commands + results), and links to relevant issues/threads if applicable.

## Security & Configuration Tips
- Use `wss://` in production by passing `--ssl-cert` and `--ssl-key`. Self-signed certs are OK for local testing.
- If you change networking or auth flows, update both server and client paths and add tests when possible.
