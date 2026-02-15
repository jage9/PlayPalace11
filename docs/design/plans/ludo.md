# Ludo (Plan)

## Summary
Classic Ludo: race four tokens around the track and into the home column. First player to finish all 4 tokens wins the game.

## Player Count
- Min: 2
- Max: 4

## Options
- Max consecutive sixes (range 0–5, default 3):
  - 0 = disabled (no forced rollback).
  - If enabled and the player rolls this many sixes in a row, restore the turn‑start state and end the turn.
- Safe start squares (default true): starting square is safe from capture.

## Board Model
- Track length: 52 squares (wrap‑around).
- Home column length: 6 squares.
- Safe squares: 1, 9, 14, 22, 27, 35, 40, 48 (+ optional safe start squares).
- Color start positions: Red 1, Blue 14, Green 27, Yellow 40.
- Home entry positions: Red 51, Blue 12, Green 25, Yellow 38.

## Turn Flow
1) Roll die.
2) Determine moveable tokens for the roll.
3) If one option, auto‑select. If multiple, prompt to choose token.
4) Move token, resolve captures, check for home/finish.
5) If roll is 6, grant extra turn (unless max‑six rule triggers rollback).

## Captures
- If a token lands on an opponent’s token **on the track** and the square is **not safe**, the opponent’s token is sent back to the yard (state = `yard`, position = 0).
- Captures do not occur on safe squares (including optional safe start squares).

## Actions & Keybinds
- Turn menu:
  - Roll die (`R`).
  - View board status (`V`).
- Actions menu:
  - View board status (`V`).
- Global actions (standard): save, scores, whose turn, who’s at table, leave table.

## What `V` shows (board status)
- Per player:
  - “Name (Color): X/4 finished”
  - Each token: state and position
    - Yard: “Token 1 (yard)”
    - Track: “Token 2 (position 17)”
    - Home column: “Token 3 (home column 3/6)”
    - Finished: “Token 4 (finished)”
- Last roll, if any.

## Sounds & Music
- Music: use Pig music (`game_pig/mus.ogg`).
- Roll: `game_pig/roll.ogg`
- Move: `game_dominos/play.ogg`
- Home/finish: `game_pig/win.ogg`
- Capture: `game_pig/lose.ogg`

## Bot Strategy (simple)
- Prefer finishing home‑column tokens.
- Prefer capturing if possible.
- Prefer advancing the token furthest along the track.
- If few tokens in play, prioritize entering from yard.

## Win Condition
- First player to finish all 4 tokens wins; game ends immediately.
