# Crazy Eights Plan (PlayPalace)

## Overview
Crazy Eights is a classic shedding game. Players try to get rid of all cards by matching suit or value of the discard top. Eights are wild and change suit. In this variant, special faces have actions:
- 8 = Wild (choose suit)
- Jack = Reverse
- Queen = Skip
- King = Draw Two

Game uses **2 standard 52-card decks**. Player count **2–8**. Starting hand size **5**. The game is round-based with cumulative scoring; first to **500+** wins (configurable).

## Core Rules
- **Playable cards**: must match **suit or value** of top discard, or be a **Wild Eight**.
- **Wild Eight**: choose suit via **C/H/S/D** (clubs/hearts/spades/diamonds). These keys are reserved during suit-choose phase.
- **Special cards**:
  - **Skip (Queen)**: next player is skipped.
  - **Reverse (Jack)**: direction reverses. With 2 players, acts like Skip.
  - **Draw Two (King)**: next player draws 2 and is skipped. No stacking.
- **Draw**: If no playable cards, player must draw one. If playable, player may choose to play it or pass. (Passing is always allowed after draw.) Drawing resets the turn timer if enabled.
- **Discard top at start**: must be a **numbered card**. If the top is a special card or 8, reshuffle it back and draw again until numbered.
- **Empty draw pile**: reshuffle discard pile (except top card) into draw pile.
- **Going out**:
  - If last card is **Draw Two**, the next player draws 2 **before scoring** (no skip needed).
  - Score round by summing remaining cards in opponents’ hands.

## Scoring
- **8 (Wild)** = 50 points
- **Skip/Reverse/Draw Two (Q/J/K)** = 20 points
- **Ace** = 1 point
- **Other cards** = face value

Round winner earns sum of opponents’ cards. Announce per-opponent points:
- “Bob wins 82 points. 60 from Janet, 22 from Jim.”

Game ends when any player reaches **winning score** (default 500, range 1–10000).

## Turn Flow
1. Announce turn + start turn timer (optional).
2. Player selects a playable card, or draws, or passes (if allowed).
3. Apply special effects (skip/reverse/draw 2), change suit if wild.
4. End turn → advance to next player based on direction and effects.

## Controls / Keybinds
- **Arrow keys + Enter**: select card or action from turn menu, normal menu
- **Space**: Draw (only when allowed). Also in turn menu under cards.
- **P**: Pass (only when allowed). Also in turn menu under cards.
- **C**: Read current top card. No label, just the card itself, 7 of clubs, or reverse of spades. If a wild, say the suit (“Wild, hearts”).
- **E**: read each player and number of cards they have remaining. bob 4, jane 3. read in table order, not sorted.
- **T**: Whose turn (global)
- **Shift+T**: Turn timer status (global)
- **S/Shift+S**: Score summaries (global)
- **Ctrl+Q**: Leave table (global)

**Note:** Card items should not appear in Escape actions menu. space/P only when applicable.

## Options
- **Turn timer**: same choices as poker. If timer expires, perform default bot action for that turn or have bot complete the turn if already draw/played wild without suit. Resets on drawing a card or entering wild suit selection. Five-second warning should still play during suit selection if possible.
- **Winning score**: default 500, range 1–10000.

## Sounds (client/sounds/game_crazyeights)
- **Intro**: `intro.ogg` (play at start of game, delay ~8s before first hand) at this point, the mainmenu music stops.
- **New hand**: `newhand.ogg`
- **Turn loop**: `yourturn.ogg` (loop during turn, stop after action ends). Do not use the global yourturn sound.
- **Normal play**: `discarded.ogg`
- **Draw 2**: `discdraw.ogg`
- **Reverse**: `discrev.ogg`
- **Skip**: `discskip.ogg`
- **Wild**: `discwild.ogg` + `morf.ogg`, then after 10 ticks play suit sound: `clubs.ogg` / `diamonds.ogg` / `hearts.ogg` / `spades.ogg`
- **Draw card**: `draw.ogg`, if playable then `drawPlayable.ogg`
- **Pass**: `pass.ogg`
- **Empty draw pile**: `pileempty.ogg`
- **One card left**: `onecard.ogg`
- **Win hand**: `youwin.ogg`, or `bigwin.ogg` if >= 100 points
- **Lose hand**: `youlose.ogg`, or `loser.ogg` if >= 50 points against you
- **End of game**: `hitmark.ogg`
- **Time warning**: `fivesec.ogg` (only if timer option >= 20 seconds)
- **Time expired**: `expired.ogg`
- **Join/leave**: `botsit.ogg`, `botleave.ogg`, `personsit.ogg`, `personleave.ogg`

## Data Model
- `CrazyEightsOptions`: winning_score, turn_timer.
- `CrazyEightsPlayer`: hand, score, is_bot, flags for draw/pass availability.
- `CrazyEightsState`:
  - `deck`, `discard_pile`, `direction` (1/-1), `current_suit`, `draw_pile_empty`, `pending_draw_count`, `skip_next`.

## Special Handling
- **Start card selection**: loop until numbered card is drawn; shuffle special cards back into deck.
- **Reverse with 2 players**: treat as skip (current player goes again).
- **Draw 2 resolution**: immediate draw + skip (no stacking).
- **Empty draw pile**: reshuffle discard pile excluding top card.
- **Timer**: if expires, call bot decision for current player.

## UI / Menu Behavior
- Turn menu shows playable cards + draw/pass when allowed.
- Escape actions menu excludes per-card items.
- Wild suit selection is a submenu phase: only C/H/S/D accepted. Pirates and other games use submenus like this.

## Bot Logic (Initial), in separate file.
- Prioritize playing a matching card that reduces hand size and/or forces opponent to draw.
- Prefer action cards late in hand (skip/reverse/draw 2), but avoid setting up opponents with easy matches.
- If forced to draw, play drawn card if it reduces hand and does not give opponent an obvious match; otherwise pass.

## Implementation Steps
1. Create `server/games/crazyeights/` with `game.py`, `bot.py`, `__init__.py`.
2. Add options, player/state structures.
3. Implement game flow: deal, start discard, turn loop, effects, reshuffle.
4. Implement actions + keybinds (Space/P/C/E, arrow menu).
5. Add sounds from `game_crazyeights` folder.
6. Implement scoring and round end + game end.
7. Register game + locales.
8. Add tests: basic round completion, draw pile reshuffle, special card effects, scoring.

## Shared Modules to Reuse
- `game_utils/cards.py` for card names, read lists, and deck helpers.
- `game_utils/game_scores_mixin.py` and `team_manager` for score reporting.
- `game_utils/poker_timer.py` (or turn timer utility) for countdown + warning sound.
- `game_utils/game_sound_mixin.py` for sound scheduling/looping.
