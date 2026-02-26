# Monopoly Wave 3 Classic Breadth Design

## Decision Summary
- Wave size: Top 25 classic special boards.
- Selection strategy: catalog-ranked franchise continuity.
- Manual policy: mixed gate (include high-priority boards, track fallback for manual gaps).
- Gameplay scope: Wave 2 parity only (`partial_rules`, startup announcement, pass-GO override path).

## Goal
Onboard a third batch of 25 high-signal classic-themed Monopoly boards as selectable profiles with deterministic partial-rule fallback behavior, while keeping runtime mechanics stable.

## Scope
- Add 25 new `classic_standard`-compatible board profiles.
- Add 25 rule-pack registry entries and 25 stub rule-pack modules.
- Add localization labels for all new board IDs across required locales.
- Add Wave 3 targeted tests mirroring Wave 2 coverage.
- Update backlog statuses for selected editions to `partial_rules`.

## Non-Goals
- No new gameplay mechanics beyond existing capability hooks.
- No full-rule implementation for any Wave 3 board.
- No changes to non-Monopoly game systems.

## Selection Method
Use local curated artifacts only:
- `docs/plans/2026-02-26-monopoly-themed-board-backlog.md`
- `server/games/monopoly/catalog/monopoly_editions_curated.json`
- `server/games/monopoly/catalog/monopoly_manual_variants_curated.json`

Deterministic ranking inputs:
1. `en-us` manual exists
2. total manual variant count
3. franchise signal strength (Disney/Marvel/Star Wars/Fortnite/etc.)

## Approved Wave 3 Top 25
| board_id | edition_id | bucket | manual_en_us | status_target |
|---|---|---|---|---|
| disney_star_wars_dark_side | monopoly-f6167 | disney | yes | partial_rules |
| disney_legacy | monopoly-19643 | disney | yes | partial_rules |
| disney_the_edition | monopoly-40224 | disney | yes | partial_rules |
| lord_of_the_rings_trilogy | monopoly-41603 | lotr | yes | partial_rules |
| star_wars_saga | monopoly-42452 | star_wars | yes | partial_rules |
| marvel_avengers_legacy | monopoly-b0323 | marvel | yes | partial_rules |
| star_wars_legacy | monopoly-b0324 | star_wars | yes | partial_rules |
| star_wars_classic_edition | monopoly-b8613 | star_wars | yes | partial_rules |
| star_wars_solo | monopoly-e1702 | star_wars | yes | partial_rules |
| game_of_thrones | monopoly-e3278 | game_of_thrones | yes | partial_rules |
| deadpool_collectors | monopoly-e4833 | marvel | yes | partial_rules |
| toy_story | monopoly-e5065 | toy_story | yes | partial_rules |
| black_panther | monopoly-e5797 | marvel | yes | partial_rules |
| stranger_things_collectors | monopoly-e8194 | stranger_things | yes | partial_rules |
| ghostbusters | monopoly-e9479 | ghostbusters | yes | partial_rules |
| marvel_eternals | monopoly-f1659 | marvel | yes | partial_rules |
| transformers | monopoly-f1660 | transformers | yes | partial_rules |
| stranger_things_netflix | monopoly-f2544 | stranger_things | yes | partial_rules |
| fortnite_collectors | monopoly-f2546 | fortnite | yes | partial_rules |
| star_wars_mandalorian_s2 | monopoly-f4257 | star_wars | yes | partial_rules |
| transformers_beast_wars | monopoly-f5269 | transformers | yes | partial_rules |
| marvel_falcon_winter_soldier | monopoly-f5851 | marvel | yes | partial_rules |
| fortnite_flip | monopoly-f7774 | fortnite | yes | partial_rules |
| marvel_flip | monopoly-f9931 | marvel | yes | partial_rules |
| pokemon | monopoly-g0716 | pokemon | yes | partial_rules |

Deferred fallback candidate:
- `monopoly-e8714` (`friends_tv`) for replacement if any selected row becomes invalid during implementation.

## Architecture
Reuse existing Wave 1/Wave 2 structure with data-driven extension:
- `board_profile.py` for board metadata and resolver compatibility.
- `board_rules_registry.py` for capability declarations and module mappings.
- `board_rules/*.py` for per-board stub constants.
- locale files for board labels.
- runtime stays on current `partial` fallback semantics.

No new abstraction layer is introduced in Wave 3.

## Data Flow
1. Materialize Wave 3 source artifact with exact 25 rows.
2. Add matching board profiles and rule-pack registry rows.
3. Add matching stub modules and module exports.
4. Add matching localization keys.
5. Validate with targeted Wave 3 tests and Monopoly regression tests.
6. Mark selected backlog rows as `partial_rules`.

## Error Handling and Risk Controls
- If a selected edition loses usable manual linkage, swap in deferred fallback candidate and note the change in source artifact.
- Prefer data corrections over runtime behavior changes.
- Keep commits task-scoped and reversible.

## Test Strategy
- New Wave 3 tests for:
  - profile resolution matrix
  - registry coverage
  - module constants/importability
  - localization key presence
  - pass-GO override capability path
  - startup matrix and preset auto-fix sample
- Regression:
  - focused Wave 3 suite
  - `pytest -k monopoly -v`
  - existing integration smoke checks

## Done Definition
1. Wave 3 Top-25 source file exists with approved rows.
2. 25 new board profiles resolve correctly in `auto`.
3. 25 rule packs and 25 modules are registered and mapped.
4. Board labels exist in all required locale files.
5. Pass-GO override path is verified for at least one Wave 3 board.
6. Startup matrix tests pass for all 25.
7. Backlog statuses updated for the selected 25 editions.
8. Monopoly regression and smoke integration tests pass.
