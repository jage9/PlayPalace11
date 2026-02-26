# Monopoly Special Boards Final-Part Status and Remaining Work

Date: 2026-02-26  
Branch: `monopoly`  
Head: `3db0285`

## Current Snapshot

- Special boards tracked: `55`
- Manual rule data files: `55` (`server/games/monopoly/manual_rules/data/*.json`)
- Fidelity statuses:
  - `manual_core`: `5`
  - `near_full`: `50`
- Boards with hardware capability flags: `junior_super_mario`, `star_wars_mandalorian`
- Pac-Man game-unit behavior remains intentionally out of scope.

## Verification Evidence (2026-02-26)

- `cd server && ../.venv/bin/pytest tests/test_monopoly_manual_rule_payload_completeness.py -v`
  - Result: `55 passed`
- `cd server && ../.venv/bin/pytest -k monopoly -q`
  - Result: `1090 passed, 598 deselected`

## New Progress: Manual Source Extraction (Marvel + Star Wars)

- Added extractor: `server/scripts/monopoly/extract_manual_text.py`
- Added extracted artifacts:
  - `server/games/monopoly/manual_rules/extracted/manifest.json`
  - `server/games/monopoly/manual_rules/extracted/*.txt`
  - `server/games/monopoly/manual_rules/extracted/*.json`
- Added coverage test:
  - `server/tests/test_monopoly_manual_source_extraction_artifacts.py`
- Extraction run status:
  - selected boards: `21`
  - extracted successfully: `21`
  - `marvel_flip` uses `strings_fallback` mode after bounded `pypdf` retry.
- Rerun command:
  - `./.venv/bin/python server/scripts/monopoly/extract_manual_text.py --family marvel --family star`

## New Progress: Payload Seeding from Extracted Manuals

- Added seed applier: `server/scripts/monopoly/apply_manual_extraction_seed.py`
- Applied extraction-backed metadata into `21` Marvel/Star board payloads:
  - `mechanics.manual_extraction` now records extraction mode, checksums, page count, and text artifact path.
  - `citations` now include `mechanics.manual_extraction`.
- Applied manual-derived Star Wars action labels:
  - `star_wars_classic_edition`, `star_wars_legacy`: `Use the Force`, `Hyperspace`, `Galactic Empire Tax`
  - `star_wars_mandalorian`, `star_wars_mandalorian_s2`: `Signet`, `Hyperspace Jump`, `Imperial Credits`, `Imperial Advance`
- Added seed verification tests:
  - `server/tests/test_monopoly_manual_extraction_seed.py`
  - Includes Marvel action/deck label assertions for:
    - `marvel_spider_man` (`Daily Bugle`, `Spider-Sense`)
    - `marvel_super_villains` (`Chance`, `Reshape the Universe`)

## What Has Been Done (Whole Rollout to Date)

1. Core Monopoly runtime and preset foundations were implemented (classic, junior, electronic banking, voice banking, cheaters, city).
2. Board selection/rules-mode, board profiles, and wave-based board rollouts were added.
3. Special-board parity framework was built:
   - anchor index/catalog artifacts,
   - deck provider framework,
   - hardware/sound-emulation scaffolding,
   - board-specific card behavior coverage across special families.
4. Manual-rule architecture was implemented:
   - rule schema models, loader, validator,
   - runtime board-rule resolution,
   - board-space/deck/effect execution from manual JSON payloads,
   - citation-backed promotion gate.
5. Special-board data payload completion was finished:
   - all `55` boards now have executable board/economy/card payloads with citations,
   - Mario family is promoted to `manual_core`,
   - Star Wars/Disney/Marvel payload expansions were merged,
   - initial manual-authentic metadata seeding was added for `marvel_avengers`.

## What the Final Part Is

Move the remaining `50` `near_full` boards to true `manual_core` by replacing synthesized placeholders with manual-authentic values per board edition:

- board-space labels and action behavior,
- Chance/Community-style card text and exact effects,
- economy and special-rule values,
- citation records tied to exact manual pages.

## Remaining Work

1. Manual source acquisition and indexing
   - Obtain canonical PDF/manual assets for each anchor edition.
   - Track source path/checksum/edition mapping for reproducibility.
2. PDF extraction pipeline
   - Add a reproducible parser/OCR flow for rule text and cards.
   - Normalize extracted rules into `manual_rules/data/*.json`.
   - Preserve `manual excerpt -> rule_path` traceability.
3. Family-by-family manual-auth pass
   - Priority:
     1. Marvel (10 boards)
     2. Star Wars (11 boards)
     3. Disney (9 boards)
     4. Remaining long-tail families
   - For each board: replace placeholders, update citations, then promote to `manual_core`.
4. Hardware and sound readiness continuity
   - Keep `hardware_capability_ids` aligned with manual evidence.
   - Continue audio-event mappings and stubs for later sound-pack integration.
   - Continue excluding Pac-Man game-unit emulation from this scope.
5. Conformance and docs synchronization
   - Add/extend tests that reject placeholder text for `manual_core` boards.
   - Keep parity matrix, anchor index, and backlog docs synchronized.

## Current Blockers

- `strings_fallback` extraction quality for `marvel_flip` is lower fidelity than structured PDF extraction.
- Several extracted manuals are image-heavy or layout-noisy, so card-by-card deterministic parsing still needs OCR/normalization work.

## Definition of Done for the Final Part

- `fidelity_status == manual_core` for all `55` special boards.
- Board/economy/card/mechanics payloads are manual-authentic per board.
- Citation coverage is complete and page-precise.
- Monopoly regression remains green.
