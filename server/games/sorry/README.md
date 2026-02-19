# Sorry Developer Notes

This package implements the `sorry` board game with profile-selectable rules:
`classic_00390` and `a5065_core`.

## Module map

- `game.py`: game integration (turn flow, actions, menus, keybinds, bot ticks).
- `state.py`: serializable game/player/pawn state plus deck/track helpers.
- `rules.py`: rules-profile interface and profile declarations.
- `moves.py`: legal move generation and move application.
- `bot.py`: deterministic move chooser over legal move candidates.

## Core invariants

- Each player's pawn count is profile-driven (`4` classic, `3` A5065 core),
  with mutually exclusive zones:
  `start`, `track`, `home_path`, `home`.
- A player's own pawns cannot share a track position or home-path step.
- Entry to `home` requires exact count (no overshoot).
- Turn flow is phase-based:
  `draw -> choose_move (if needed) -> end/advance`.
- Card `2` extra-turn behavior is profile-driven.

## Rules profile matrix

- `classic_00390`:
  - 4 pawns per player
  - leave start with cards `1` and `2`
  - card `2` grants extra turn
  - `SORRY!` requires replacement target from start
  - slide triggers on other-color slide starts only
- `a5065_core`:
  - 3 pawns per player
  - leave start with any forward-value card
  - card `2` does not grant extra turn
  - `SORRY!` falls back to forward 4 when no replacement target exists
  - slide triggers on own-color slide starts only

## Action and keybind behavior

- Turn actions are `draw_card` and generated `move_slot_<n>` entries.
- `move_slot` actions are generated up to `max_move_slots` (currently `64`) so
  high-branching states (notably card `11` swap combinations in 4-player games)
  are not truncated.
- Keybinds:
  - `d` and `space` -> `draw_card`
  - `1` through `9` -> `move_slot_1` through `move_slot_9`

## Extension points

- Add new editions by implementing `SorryRulesProfile` and routing game options
  to select the profile.
- Keep `moves.py` deterministic for a given state/card/profile.
- Add tests for new card semantics, persistence, and bot behavior before adding
  profile toggles to the UI.
