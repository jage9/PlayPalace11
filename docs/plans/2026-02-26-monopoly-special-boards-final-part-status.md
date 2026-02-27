# Monopoly Special Boards Final-Part Status and Remaining Work

Date: 2026-02-27  
Branch: `monopoly`  
Head: `98c6150` (plus working-tree updates)

## Current Snapshot

- Special boards tracked: `55`
- Manual rule data files: `55` (`server/games/monopoly/manual_rules/data/*.json`)
- Fidelity statuses:
  - `manual_core`: `5`
  - `near_full`: `50`
- Boards with hardware capability flags: `junior_super_mario`, `star_wars_mandalorian`
- Pac-Man game-unit behavior remains intentionally out of scope.

## Verification Evidence (2026-02-27)

- `cd server && ../.venv/bin/pytest tests/test_monopoly_manual_rule_payload_completeness.py -v`
  - Result: `55 passed`
- `cd server && ../.venv/bin/pytest tests/test_monopoly_star_wars_manual_rule_payload.py tests/test_monopoly_disney_marvel_manual_rule_payload.py tests/test_monopoly_manual_card_draw_text.py tests/test_monopoly_manual_rule_payload_completeness.py -v`
  - Result: `216 passed`
- `cd server && ../.venv/bin/pytest -k monopoly -q`
  - Result: `1260 passed, 598 deselected`

## New Progress: Manual Source Extraction (All Special Boards)

- Added extractor: `server/scripts/monopoly/extract_manual_text.py`
- Added card-candidate miner: `server/scripts/monopoly/extract_manual_card_candidates.py`
- Added extracted artifacts:
  - `server/games/monopoly/manual_rules/extracted/manifest.json`
  - `server/games/monopoly/manual_rules/extracted/*.txt`
  - `server/games/monopoly/manual_rules/extracted/*.ocr.txt` (image-heavy manual sidecars)
  - `server/games/monopoly/manual_rules/extracted/*.json`
- Added coverage test:
  - `server/tests/test_monopoly_manual_source_extraction_artifacts.py`
- Extraction run status:
  - selected boards: `55`
  - extracted successfully: `55`
  - `marvel_flip` uses `strings_fallback` mode after bounded `pypdf` retry.
  - Preferred extraction metadata now records:
    - `preferred_text_path` / `preferred_text_sha256` / `preferred_text_source`
    - `ocr_text_path` / `ocr_text_sha256` when OCR sidecars are present.
- Rerun command:
  - `./.venv/bin/python server/scripts/monopoly/extract_manual_text.py --family ...` (all families from anchor index)
  - OCR-assisted rerun (optional): add `--ocr-when-text-below <chars>` and/or `--ocr-board-id <id>`.
  - Candidate-line extraction: `./.venv/bin/python server/scripts/monopoly/extract_manual_card_candidates.py --board-id <id>`
- Candidate coverage snapshot (all 55 boards):
  - zero candidates: `disney_the_edition`, `fortnite`, `marvel_flip`
  - low candidates (<=10): `disney_princesses` (5)
  - strongest candidate density examples: `disney_star_wars_dark_side` (73), `lord_of_the_rings` (69), `transformers_beast_wars` (60)

## New Progress: Payload Seeding from Extracted Manuals

- Added seed applier: `server/scripts/monopoly/apply_manual_extraction_seed.py`
- Applied extraction-backed metadata into all `55` special-board payloads:
  - `mechanics.manual_extraction` now records extraction mode, checksums, page count, and preferred/manual text artifact path.
  - `mechanics.manual_extraction` keeps raw and OCR-aware traceability fields (`raw_text_*`, `ocr_text_*`, `preferred_text_source`).
  - `citations` now include `mechanics.manual_extraction`.
- Applied manual-derived Star Wars action labels:
  - `star_wars_classic_edition`, `star_wars_legacy`: `Use the Force`, `Hyperspace`, `Galactic Empire Tax`
  - `star_wars_mandalorian`, `star_wars_mandalorian_s2`: `Signet`, `Hyperspace Jump`, `Imperial Credits`, `Imperial Advance`
- Applied manual-derived Mario action/deck labels:
  - `mario_celebration`: `Question Block`, `Community Chest`; tax labels `Chain Chomp`, `Piranha Plant`
  - `mario_collectors`: `? Block`, `Warp Pipe`
  - `mario_kart`: `Power-Up`, `Grand Prix`
  - `mario_movie`: `Question Block`, `Bowser's Fury`
- Added seed verification tests:
  - `server/tests/test_monopoly_manual_extraction_seed.py`
  - Includes extraction metadata coverage for all 55 boards plus Star/Marvel/Disney/Mario/long-tail label assertions.

## New Progress: Marvel Set Coverage

- Manual-extraction seed now covers the full Marvel board set with explicit action/deck labels where extract confidence is high:
  - `marvel_80_years`: `Catalog` + tax labels `Infinity Gauntlet`, `Cable & Deadpool`
  - `marvel_avengers`: `Stark Industries`, `Infinity Gauntlet`, tax labels `Ultron`, `Hela`
  - `marvel_avengers_legacy`: `S.H.I.E.L.D.`, `Villains`
  - `marvel_black_panther_wf`: `Wakandan`, `Talokanil`
  - `marvel_deadpool`: `Dumb Luck`, `Pouches`
  - `marvel_eternals`: `Uni-Mind`, `Arishem's Judgement`
  - `marvel_falcon_winter_soldier`: `The Shield`, `The Flag Smashers`
  - `marvel_flip`: `Event`, `Team-Up`
  - `marvel_spider_man`: `Daily Bugle`, `Spider-Sense`
  - `marvel_super_villains`: `Chance`, `Reshape the Universe`

## New Progress: Disney Set Coverage

- Manual-extraction seed now covers Disney boards with explicit action/deck labels where extract confidence is high:
  - `disney_animation`: `Magic Mirror`, `Ariel's Treasure Chest`; tax labels `The Evil Queen's Spell`, `Maleficent's Curse`
  - `disney_legacy`: `Show Time`, `Magic Moments`
  - `disney_lightyear`: `Hyperspeed`, `Crystallic Fusion`; tax labels `Bugs`, `Zyclops`
  - `disney_lion_king`: `Destiny`; tax labels `Water Fowl`, `Wild Fire`
  - `disney_mickey_friends`: `Friendship`, `Magic Moments`; tax labels `Hot Dog Snack Break`, `Popcorn Snack Break`
  - `disney_princesses`: `Sorte`, `Magia`; tax labels `Imposto`
  - `disney_the_edition`: `Show Time`, `Magic Moments`; tax labels `Scrooge McDuck's Tax`, `Prince John's Tax`
  - `disney_star_wars_dark_side`: `The Empire`, `The Dark Side`; tax labels `Rebel Escape`, `Rebel Attack`
  - `disney_villains`: `Chance`, `Poison Apple`

## New Progress: Long-Tail Set Coverage

- Added manual-derived action/deck labels for:
  - `animal_crossing`: `Chance`, `Nook Miles`
  - `barbie`: `Dream Career`, `Dream Closet`
  - `black_panther`: `Kimoyo Beads`, `Heart-Shaped Herb`
  - `deadpool_collectors`: `Dumb Luck`, `Pouches`
  - `fortnite`: `Storm`, `Loot Chest`
  - `fortnite_collectors`: `Storm`, `Loot Chest`
  - `fortnite_flip`: `Game Mode`, `Loot Chest`
  - `game_of_thrones`: `Chance Cards`; tax labels `The Dothraki Tribute`, `Iron Bank Tax`
  - `ghostbusters`: `Roaming Vapor`
  - `harry_potter`: `Owl Post`; tax labels `Filch and Mrs. Norris`
  - `junior_super_mario`: `Chance`
  - `jurassic_park`: `Impact Tremor`, `Cold Storage`
  - `lord_of_the_rings`: `Quest`
  - `lord_of_the_rings_trilogy`: `People`, `Event`
  - `pokemon`: `Adventure`, `Challenge`
  - `stranger_things`: `Walkie-Talkie`, `Blinking Lights`
  - `stranger_things_collectors`: `Transmission`, `Upside Down`
  - `stranger_things_netflix`: `Cerebro`, `Hellfire Club`
  - `toy_story`: `Toy Chest`, `The Claw`
  - `transformers`: `Autobot`, `Decepticon`
  - `transformers_beast_wars`: `Maximal`, `Predacon`
- Expanded Star Wars label/deck coverage beyond the original 4 boards:
  - `star_wars_40th`, `star_wars_boba_fett`, `star_wars_complete_saga`,
    `star_wars_light_side`, `star_wars_solo`, `star_wars_the_child`.
- Final Star Wars Saga labels are seeded from manual OCR:
  - `star_wars_saga`: `Sith`, `Jedi`; tax labels `Trade Blockade`, `Bounty`
- Literal manual card-text seeding coverage now includes canonical card text fields (`advance_to_go`, `go_to_jail`, `get_out_of_jail_free`) for:
  - Star Wars family (`12` boards): `disney_star_wars_dark_side`, `star_wars_40th`, `star_wars_boba_fett`, `star_wars_classic_edition`, `star_wars_complete_saga`, `star_wars_legacy`, `star_wars_light_side`, `star_wars_mandalorian`, `star_wars_mandalorian_s2`, `star_wars_saga`, `star_wars_solo`, `star_wars_the_child`
  - Disney/Marvel high-confidence subset (`15` boards): `disney_animation`, `disney_legacy`, `disney_lightyear`, `disney_lion_king`, `disney_mickey_friends`, `disney_princesses`, `disney_villains`, `marvel_80_years`, `marvel_avengers`, `marvel_black_panther_wf`, `marvel_deadpool`, `marvel_eternals`, `marvel_falcon_winter_soldier`, `marvel_spider_man`, `marvel_super_villains`
  - Additional partial seeding: `marvel_avengers_legacy` (`go_to_jail` canonical card text in both decks)
- Remaining boards without deck-label seeding: `0` (all `55` covered)

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
   - manual card draw text now supports literal `cards.*[].text` (with safe fallback to localized classic keys),
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
   - Continue improving source quality for image-heavy manuals for card-by-card promotion and exact effect text extraction.
   - Continue tracking source path/checksum/edition mapping for reproducibility.
2. PDF extraction pipeline
   - Add a reproducible parser/OCR flow for image-heavy manuals and board-art-heavy PDFs.
   - Normalize extracted rules into `manual_rules/data/*.json`.
   - Preserve `manual excerpt -> rule_path` traceability.
3. Family-by-family manual-auth pass
   - Priority:
     1. Long-tail families with newly seeded extraction metadata (animal, barbie, black, deadpool, fortnite, game, ghostbusters, harry, jurassic, lord, pokemon, stranger, toy, transformers)
     2. Marvel/Star/Disney card-by-card effect verification against manuals
   - For each board: replace placeholders, update citations, then promote to `manual_core`.
4. Hardware and sound readiness continuity
   - Keep `hardware_capability_ids` aligned with manual evidence.
   - Continue audio-event mappings and stubs for later sound-pack integration.
   - Continue excluding Pac-Man game-unit emulation from this scope.
5. Conformance and docs synchronization
   - Add/extend tests that reject placeholder text for `manual_core` boards.
   - Keep parity matrix, anchor index, and backlog docs synchronized.

## Current Blockers

- No blockers remain for action/deck/tax label seeding coverage.
- Remaining blocker is card-by-card deterministic extraction from image-heavy manuals.
- Targeted extractor retry for `disney_the_edition` currently returns `<urlopen error [Errno 16] Device or resource busy>` in this environment.
- Literal card text seeding still pending deterministic/manual-auth capture for:
  - `disney_the_edition`
  - `marvel_flip`
  - Remaining canonical literals on `marvel_avengers_legacy` (`advance_to_go`, `get_out_of_jail_free`)

## Definition of Done for the Final Part

- `fidelity_status == manual_core` for all `55` special boards.
- Board/economy/card/mechanics payloads are manual-authentic per board.
- Citation coverage is complete and page-precise.
- Monopoly regression remains green.
