# Poker Roadmap (5-Card Draw + Hold'em)

## Goals
- Add two poker games (5-Card Draw and Texas Hold’em) with shared infrastructure.
- Keep rules extensible for future variants (Omaha, Stud, etc.).
- Standardize betting actions, pot handling, and hand evaluation outputs.
- Add a new game category: **Poker**.

## File Placement
This plan lives in `docs/design/plans/poker.md` to align with other design docs.

## Shared Helpers (New)
### Core Poker Helpers
- **`poker_evaluator.py`** (already added): best 5-card hand from 5–7 cards, plus short text description.
- **`poker_pretty`** (in evaluator): hand description for G key (even with fewer than 5 cards; see below).
- **`poker_pot.py`**: pot manager with side pots, eligibility sets, and split payouts.
- **`poker_betting.py`**: betting round controller (actions, min-raise rules, round completion).
- **`poker_table.py`**: dealer button, blind/ante logic, seat order helpers.
- **`poker_timer.py`**: per-turn timer (option). Consider later adding banked time.

### Hand Evaluation for <5 Cards (G key)
Add a “hand potential” description function:
- **Input:** 1–4 cards (private hand only or partial board).
- **Output:** “High card Ace” or “Pair of Aces”.
- **Rules:** Don’t invent outcomes; only evaluate the visible cards.

## Table Formats
### Tournament (Fixed Stack)
- Everyone starts with X chips.
- Blind/ante schedule increases on a timer or per-hand count.
- Elimination reduces player count until winner.

### Cash (“SAG” / Come-and-Go)
- Players can join/leave between hands.
- Blinds still rotate (Hold’em), ante optional.
- No escalating blind schedule.

## Standard Commands (All Poker Games)
- **P**: Show pot(s) and eligibility (main + side pots).
- **F**: Fold.
- **C**: Call (or “Check” if no bet to call).
- **R**: Raise → prompt for amount (text input).
- **Shift+A**: All‑in (auto‑creates/updates side pots).
- **D**: Read all cards in your hand (full names).
- **E**: Read community/table cards.
- **G**: Read current hand value (evaluator/printer).
- **X**: Who has the button (Hold’em).
- **Z**: Your position relative to the button (Hold’em).
- **S**: Scores/stack sizes (uses TeamManager or poker-specific scoreboard).
- **N**: Current bet + amount to call.
- **M**: Minimum raise amount.
- **L**: Action log for the current betting round.
- **Shift+T**: Turn timer remaining (fallback message if timer is disabled).
- **V**: Blind/ante timer remaining, or “Blinds will raise next hand.”

### Card Readout Shortcuts
- **O**: Reveal both hole cards (end of hand only).
- **U**: Reveal first hole card (end of hand only).
- **I**: Reveal second hole card (end of hand only).
- **1–5**: Speak each of the 5 cards (5‑card draw).
- **1–7** (Hold’em): Speak each card (1–2 = hole cards, 3–7 = community).

## Betting Rules (Shared)
- Round ends when all active players have:
  - matched the current bet, or
  - folded, or
  - are all‑in (no further action required).
- A round must continue after any raise until all remaining players have matched the new bet (re‑raises allowed within the cap).
- Minimum raise: must be at least the size of the previous raise (unless all‑in).
- Validate bet sizes (illegal raises, insufficient chips).
- Posting blinds/antes when short‑stacked: treat as all‑in for that forced bet.
- **Side pots** created when one or more players go all‑in below the current bet.
- **Split pots**: divide evenly; odd chips handled deterministically (e.g., earliest seat).
- **Short‑circuit showdown**: if all remaining players are all‑in and only one player is still eligible to bet, reveal remaining community cards immediately.
- **Side‑pot resolution order**: pay main pot first, then each side pot by eligibility set.

## Showdown & Visibility
- **Showdown order**: auto‑reveal all non‑folded hands at showdown.
- **No reveal**: if only one player remains (everyone else folded), skip hand reveal.

## Hold’em Cosmetics
- Burn cards between streets (optional cosmetic).

## Hand History / Logs
- Record key actions (bets, raises, folds, all‑ins, pots).
- Useful for bug reports, bot tuning, and replay.

## Reconnection Handling (look at how this is handled globally)
- Restore hand state, player stacks, and timers on reconnect.

## Blind Timer Behavior (Tournament)
- Timer counts down per hand; when it reaches 0, announce “Blinds will raise next hand.”
- When blinds increase, reset the timer.

## Audio & Music (Placeholder Assets)
- **Music**: use 3‑Card Poker music for now.
- **Win sounds**: reuse Blackjack win sounds for hand wins.
- **Deal/Bet**: reuse 3‑Card Poker deal/bet sounds.
- **Draw sounds**: use `game_cards/draw*.ogg` (cycle variants when drawing multiple cards).
  - Delay **300 ms** between draw sounds when drawing multiple cards.
  - Use draw sounds for Hold’em community cards (flop/turn/river) and draw replacements.
- **New hand**: `game_cards/small_shuffle.ogg` once per hand, then deal sounds
  (2 cards in Hold’em, 5 cards in Draw).
- **Turn sound**: use the standard “your turn” sound from other games.

### Raise Modes (Options)
- **No‑Limit** (default): raise to any amount up to stack.
- **Pot‑Limit**: max raise = current pot + call.
- **Double Pot‑Limit**: max raise = 2× pot + call.
- (Optional later) **Fixed‑Limit**.
- **Max Raises**: configurable cap per betting round (e.g., 3, 4, unlimited).

## 5-Card Draw
### Core Flow
1. **Ante** (optional; no blinds).
2. Deal 5 cards to each player.
3. **Betting round 1**.
4. **Draw round** (1 draw only):
   - Keep/Drop up to 3 cards (4 allowed if holding an Ace).
   - Replace dropped cards from deck.
5. **Betting round 2**.
6. **Showdown** → evaluate hands → pay pot(s).

### Options
- Starting chips: 100–1,000,000 (default 20,000).
- Turn timer (seconds): 5, 10, 15, 20, 30, 45, 60, 90, unlimited.
- Ante amount (draw only): 0–stack size (default 100).

## Texas Hold’em
### Core Flow
1. **Post blinds** (SB/BB), optional ante.
2. Deal 2 hole cards.
3. **Pre‑flop betting** (SB acts first in 2‑player, otherwise UTG).
4. **Flop** (3 community) → betting.
5. **Turn** (1 community) → betting.
6. **River** (1 community) → betting.
7. **Showdown** → evaluate best 5 from 7 cards.

### Heads‑Up Rules
- Button is **small blind**.
- Small blind (button) acts first pre‑flop.
- Big blind acts first post‑flop.

### Options
- Starting chips: 100–1,000,000 (default 20,000).
- Small blind / big blind (default 100/200).
- Ante amount (optional, default 0; can phase in with blind schedule).
- Turn timer (seconds): 5, 10, 15, 20, 30, 45, 60, 90, unlimited.
- Raise mode (no‑limit / pot‑limit / double‑pot‑limit).
- Max raises per betting round (including “unlimited”).
- Blind/ante increase timer (tournament only): 5, 10, 15, 20, 30 minutes.

## Scoring/Scoreboard
- Use the standard TeamManager scoreboard to report chip counts.

## Bot Logic
- Add a basic bot that:
  - Folds weak hands to large bets.
  - Calls small bets with medium strength.
  - Raises strong made hands.
  - Prioritizes all‑in only when pot odds justify it.

## Payout Messaging (Standard)
- “Bob wins 1500 chips with Ace‑high Straight Flush.”
- “Bill wins 800 chips in side pot with Two Pair, Kings and Fives, with Nine.”
- “Bill and Joe split the main pot with Queen‑high Straight.”

## Testing Plan
1. Unit tests for:
   - Pot creation, side‑pot eligibility, split logic.
   - Betting round completion.
   - Heads‑up blind/button logic.
2. Game tests:
   - Single‑hand win.
   - All‑in side pot scenarios.
   - Tie and split pot.
   - Draw/replace validation.
