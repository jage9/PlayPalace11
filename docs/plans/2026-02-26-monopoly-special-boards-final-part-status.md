# Monopoly Special Boards Final-Part Completion Status and Follow-Up

Date: 2026-02-27  
Branch: `monopoly`  
Head: tracked via git history on `monopoly`

## Current Snapshot

- Special boards tracked: `55`
- Manual rule data files: `55` (`server/games/monopoly/manual_rules/data/*.json`)
- Fidelity statuses:
  - `manual_core`: `55`
  - `near_full`: `0`
- Boards with hardware capability flags: `junior_super_mario`, `star_wars_mandalorian`
- Pac-Man game-unit behavior remains intentionally out of scope.

## Verification Evidence (2026-02-27)

- `cd server && ../.venv/bin/pytest tests/test_monopoly_manual_rule_payload_completeness.py -v`
  - Result: `55 passed`
- `cd server && ../.venv/bin/pytest tests/test_monopoly_star_wars_manual_rule_payload.py tests/test_monopoly_disney_marvel_manual_rule_payload.py tests/test_monopoly_manual_card_draw_text.py tests/test_monopoly_manual_rule_payload_completeness.py -v`
  - Result: `222 passed`
- `cd server && ../.venv/bin/pytest tests/test_monopoly_special_board_manual_core_conformance.py tests/test_monopoly_special_board_anchor_index.py tests/test_monopoly_manual_core_fidelity_alignment.py tests/test_monopoly_hybrid_lane_exception_contract.py -q`
  - Result: `62 passed`
- `cd server && ../.venv/bin/pytest -k monopoly -q`
  - Result: `1280 passed, 598 deselected`

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
  - Disney mirror/manual fallback seeding: `disney_the_edition` (`advance_to_go`, `go_to_jail`, `get_out_of_jail_free`)
    - Source mirror used for literal text recovery: `https://www.manualsdir.com/manuals/613579/hasbro-monopoly-disney-edition-2010.html`
  - Additional partial seeding: `marvel_avengers_legacy`, `marvel_flip` (`go_to_jail` canonical card text in both decks)
  - Remaining canonical literal card ids on `marvel_avengers_legacy` and `marvel_flip` are now explicitly marked as `not_observed_in_available_manual_sources` with manual evidence notes:
    - `chance.advance_to_go`
    - `community_chest.get_out_of_jail_free`
  - Native manual deck-id modeling is now active for the two remaining Marvel boards:
    - `marvel_avengers_legacy`: `shield_*` and `villains_*` card ids
    - `marvel_flip`: `event_*` and `team_up_*` card ids
  - Native manual deck-id modeling has now been expanded across the full Disney/Marvel family rollout boards via deck-name-prefixed ids plus `legacy_id` compatibility aliases.
  - Legacy canonical ids remain backward compatible via board rule remaps.
  - Runtime now resolves canonical compatibility ids to native deck ids by canonical card-slot index when board-specific manual decks are active.
  - Card-draw announcements now use `mechanics.decks` labels (for example `S.H.I.E.L.D.`, `Villains`, `Event`, `Team-Up`) instead of hardcoded `Chance`/`Community Chest` labels.
  - Option-2 kick-off: started replacing synthesized effects with manual-evidenced native effects by promoting `marvel_avengers_legacy` Villains slot-2 (`legacy_id=doctor_fee_pay_50`) to the board's verified `+215` credit outcome directly in native payload data.
  - Option-2 targeted OCR sweep (2026-02-27) re-ran high-DPI card/manual extraction for `marvel_avengers_legacy` and `marvel_flip`; evidence quality improved, but the remaining hybrid exceptions are still unresolved because no literal card lines uniquely bind to the four native ids:
    - `shield_advance_to_go`
    - `villains_jail_release_options`
    - `event_advance_to_go`
    - `team_up_jail_release_options`
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

## Final-Part Completion

The final-part promotion target is complete:

- all `55` special boards are now marked `manual_core` in parity and anchor artifacts;
- conformance tests enforce `manual_core` status across all special boards;
- cross-artifact alignment tests ensure parity + anchor index remain synchronized.

## Follow-Up Work

1. Continue manual-source quality improvements for image-heavy manuals and OCR stability.
2. Preserve explicit hybrid-lane evidence notes for unresolved literal cards where text is not observable in available manuals.
3. Expand hardware/audio mappings when manuals provide deterministic trigger behavior.
4. Keep parity matrix and plan docs synchronized with any future board-rule revisions.

## Current Blockers

- No blockers for `manual_core` status rollout remain.
- Ongoing limitation: deterministic literal text recovery remains incomplete for two canonical slots across `marvel_avengers_legacy` and `marvel_flip` (represented by four native ids listed above); all remain explicitly marked with `text_status=not_observed_in_available_manual_sources` and evidence notes.
- Environment-specific network/OCR tooling reliability can still affect extraction refresh throughput, but no longer blocks conformance due cached extraction fallback.

## Definition of Done for the Final Part

- `fidelity_status == manual_core` for all `55` special boards.
- Board/economy/card/mechanics payloads are manual-authentic per board.
- Citation coverage is complete and page-precise.
- Monopoly regression remains green.
