# Sorry Classic Design (2026-02-19)

## Status

Approved design for implementation planning.

## Objective

Add a new playable `Sorry!` game to PlayPalace with:

- Classic rules baseline (`00390` ruleset)
- Human and bot play
- Deterministic, serializable state
- Test coverage including persistence/play loops

The design must support future addition of alternate editions (for example `A5065`) without rewriting the core game flow.

## Scope

### In scope (v1)

- Classic free-for-all gameplay
- 2 to 4 players
- 4 pawns per player
- Full classic card handling
- Basic bot strategy
- Two game options:
  - `auto_apply_single_move` (toggle)
  - `faster_setup_one_pawn_out` (toggle)
- Unit tests and play/persistence tests

### Out of scope (v1)

- Team mode
- Adult points mode
- New-edition `A5065` mechanics
- UI protocol changes beyond existing game/menu patterns

## Rules Baseline

Primary rules source for v1:

- Classic instructions PDF (`00390`): https://instructions.hasbro.com/api/download/00390_en-us_sorry-game.pdf

Secondary reference for future variant support:

- Newer edition instructions PDF (`A5065`): https://instructions.hasbro.com/api/download/A5065_en-us_Sorry%21-Game.pdf

## High-Level Architecture

Implement a new package:

- `server/games/sorry/__init__.py`
- `server/games/sorry/game.py`
- `server/games/sorry/state.py`
- `server/games/sorry/rules.py`
- `server/games/sorry/moves.py`
- `server/games/sorry/bot.py`

Design split:

- `game.py`: lifecycle, turn orchestration, action wiring, win checks
- `state.py`: all dataclasses for board/deck/pawns/turn phase
- `rules.py`: `SorryRulesProfile` + `Classic00390Rules`
- `moves.py`: legal move generation and deterministic application helpers
- `bot.py`: legal-move selection policy

## Rules Profile Strategy

Use a small rules profile abstraction:

- `SorryRulesProfile` defines card behavior and key variant rules
- `Classic00390Rules` implements v1 behavior
- Future variant (`A5065`) can be added as another profile without changing core turn loop

This keeps "what a card means" separate from "how a turn is processed."

## State Model

All game runtime state is dataclass-based and serializable.

Expected core entities:

- `SorryGameState`
  - draw pile
  - discard pile
  - current player index
  - current drawn card (if any)
  - pending turn phase
  - game options
- `SorryPlayerState`
  - player id
  - pawn states (4)
  - finished count
- `PawnState`
  - location type (`start`, `track`, `home_path`, `home`)
  - track/home coordinates as needed

No networking objects or non-serializable runtime handles are stored in game state.

## Turn and Action Flow

1. Active player draws a card.
2. Generate legal moves for the drawn card and current state.
3. If zero legal moves:
   - report no-move result
   - advance turn unless card grants extra turn (classic `2`)
4. If one legal move and `auto_apply_single_move=true`:
   - apply automatically
5. Otherwise:
   - present legal move actions in turn menu
   - player selects one
6. Apply move and resolve effects:
   - bump/send opponent pawn to start
   - slide movement and slide captures
   - swap when applicable
7. Resolve card post-action rules:
   - classic `2` grants same-player next turn
8. Check victory:
   - first player with all 4 pawns in `home` wins

## Card Behavior Coverage (Classic)

Cards to support:

- `1`: move forward 1 or move pawn out of start
- `2`: move forward 2 or move pawn out of start; draw/play again
- `3`: move forward 3
- `4`: move backward 4
- `5`: move forward 5
- `7`: move forward 7 or split across two pawns
- `8`: move forward 8
- `10`: move forward 10 or backward 1
- `11`: move forward 11 or swap with opponent pawn
- `12`: move forward 12
- `SORRY!`: from start, replace opponent pawn on track and send it to start

Additional classic constraints:

- Exact count required to enter home
- Own-color slide entry does not slide
- Opponent slide entry triggers full slide and capture behavior
- Discard reshuffle into draw pile when draw pile is empty

## Game Options

### `auto_apply_single_move` (bool)

- `false`: player must explicitly confirm every move
- `true`: auto-apply when exactly one legal move exists

### `faster_setup_one_pawn_out` (bool)

- `false`: all pawns begin in start
- `true`: each player begins with one pawn already at entry position

## UI and Menu Behavior

Turn actions:

- `Draw card`
- Move-selection actions derived from legal move list

Always-available table actions (in existing pattern):

- Read board summary
- Read my pawn positions
- Read discard/draw counts
- Announce whose turn

Keybind intent (following repo conventions):

- `D`: draw
- Numeric or generated selection keybinds for candidate moves
- Existing status/turn keybind patterns for read-only actions

## Bot Strategy (v1)

Simple deterministic priority:

1. Winning move into home
2. Capture move (including slide or `SORRY!`)
3. Bring pawn out of start (if meaningful)
4. Safer forward progress when possible
5. Fallback to maximum legal progress

Bots use the same legal move generator and move applier as human players.

## Testing Plan

### Unit tests

- Per-card legality and application behavior
- Split-7 validation and edge cases
- `10` branch behavior (forward/backward)
- `11` swap restrictions and outcomes
- `SORRY!` legality from start and replacement effects
- Slide resolution and captures
- Exact-home movement validation
- Deck exhaustion and discard reshuffle

### Integration/play tests

- Bot-vs-bot full game completion
- Save/load compatibility during progression
- No illegal state transitions under repeated ticks

### Option tests

- `auto_apply_single_move` on/off behavior
- `faster_setup_one_pawn_out` on/off startup behavior

## Milestone Definition

M1 is complete when:

- Humans can play Sorry end-to-end
- Basic bots can complete full games
- Tests above pass in server test suite

## Risks and Mitigations

- Ambiguous edge-case interpretation:
  - Mitigation: codify against `00390` behavior and test each edge case directly
- Rule complexity for move generation:
  - Mitigation: separate pure legal-move generation from orchestration
- Future variant drift:
  - Mitigation: maintain rules-profile boundary (`rules.py`)

## Next Step

Create an implementation plan from this design, split into small executable milestones (scaffold/state, legal moves, turn flow, bot, tests, polish).
