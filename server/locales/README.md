# Localization Files

This directory contains all localization files for PlayPalace v11, using Mozilla Fluent (.ftl format).

## Structure

Each subdirectory represents a language/locale:
- `en/` - English (reference locale)
- `de/`, `es/`, `fr/`, etc. - Other supported languages

Each locale directory contains:
- **`main.ftl`** - Core UI strings (menus, lobby, system messages)
- **`games.ftl`** - Game category names and shared game strings
- **`languages.ftl`** - Language names (translated into this language)
- **`poker.ftl`** - Shared poker strings (used by multiple poker variants)
- **Game-specific files** - One `.ftl` file per game (e.g., `ludo.ftl`, `yahtzee.ftl`)

## Supported Languages

Currently supported (28 languages):
- ar (Arabic), cs (Czech), de (German), en (English), es (Spanish)
- fa (Persian), fr (French), hi (Hindi), hr (Croatian), hu (Hungarian)
- id (Indonesian), it (Italian), ja (Japanese), ko (Korean), mn (Mongolian)
- nl (Dutch), pl (Polish), pt (Portuguese), ro (Romanian), ru (Russian)
- sk (Slovak), sl (Slovenian), sv (Swedish), th (Thai), tr (Turkish)
- uk (Ukrainian), vi (Vietnamese), zh (Chinese), zu (Zulu)

## Adding a New Game's Localization

When you add a new game to PlayPalace:

1. Create the English locale file: `server/locales/en/yourgame.ftl`
2. Copy it to all other languages:
   ```bash
   cd server
   python3 tools/check_locales.py --fix
   ```
3. Verify completeness:
   ```bash
   cd server
   python3 tools/check_locales.py --verbose
   ```

**Important**: All languages must have the same set of `.ftl` files. If a translation doesn't exist yet, copy the English text as a placeholder. The automated test suite will fail if any files are missing.

## Adding a New Language

To add support for a new language:

1. Create a new directory: `server/locales/XX/` (where XX is the language code)
2. Copy all `.ftl` files from `en/` to `XX/`:
   ```bash
   cp -r server/locales/en/* server/locales/XX/
   ```
3. Update `XX/languages.ftl` to translate language names into that language
4. Add the language code to the expected list in `server/tests/test_locale_completeness.py`
5. Run tests to verify: `cd server && uv run pytest tests/test_locale_completeness.py`

## Translation Guidelines

- Follow [Mozilla Fluent syntax](https://projectfluent.org/)
- Use `_self`, `_target`, `_other` message variants where appropriate (see existing games for examples)
- Keep variable names (`{ $player }`, `{ $score }`, etc.) unchanged
- Test your translations in-game to ensure they fit the UI
- Prefer natural phrasing over literal translation

## Verification Tools

### check_locales.py
Manual script to check and fix locale completeness:
```bash
cd server
python3 tools/check_locales.py           # Check only
python3 tools/check_locales.py --fix     # Copy missing files from English
python3 tools/check_locales.py --verbose # Detailed output
```

### Automated Tests
The pytest suite includes locale completeness tests:
```bash
cd server
uv run pytest tests/test_locale_completeness.py -v
```

These tests verify:
- All locales have the same files as English
- No files are empty or corrupted
- Required system files exist
- All expected languages are present

## Cache Behavior

The localization system uses compiled caches for performance. If you modify `.ftl` files during development:
- The cache automatically refreshes when files change
- Set `PLAYPALACE_DISABLE_LOCALE_CACHE=1` to disable caching during development
- Compiled caches are stored in `.locale_cache/` (gitignored)

## File Naming Convention

- **System files**: lowercase (main.ftl, games.ftl)
- **Game files**: match the game's Python package name (e.g., `crazyeights.ftl` for `server/games/crazyeights/`)
- **Shared helpers**: descriptive name (e.g., `poker.ftl` for shared poker strings)

## Questions?

See `docs/design/plans/localization_and_messages.md` for design decisions and architecture notes.
