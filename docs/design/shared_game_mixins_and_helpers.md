# Shared Game Mixins and Helpers

This document is the operational reference for reusable game infrastructure in `server/game_utils/`.

It is intended to be the first document a human or AI contributor reads before:
- building a new game
- refactoring common game infrastructure
- deciding whether logic belongs in a game file or a shared helper

This doc is deliberately broader than individual docstrings. It explains:
- what shared mixins and helpers exist
- what `Game` already includes by default
- what must be opted into explicitly
- what each shared piece expects from a game
- representative examples in the codebase
- when not to use a shared abstraction

Code docstrings remain the detailed source of truth for exact method signatures and behavior.

## Core Rule

Extract infrastructure, not rules.

Shared modules are a good fit for:
- menu plumbing
- turn order
- action wiring
- common timers
- options systems
- card/dice primitives
- team management
- poker-family mechanics that are actually shared

Shared modules are usually a bad fit for:
- scoring rules unique to one game
- win conditions unique to one game
- special card/piece powers unique to one game
- heavily branching phase logic that only one game uses

If two games only “sound similar” but their rules diverge quickly, keep the rule engine local.

## Big Picture

There are three broad layers in `server/game_utils/`:

1. Core mixins used by `Game`
   - broad infrastructure most games already get automatically
2. Optional mixins
   - specialized behavior a game opts into explicitly
3. Helper modules
   - reusable dataclasses/functions for actions, options, cards, dice, teams, poker, and so on

## What `Game` Already Includes

The base [Game](/home/jjm/code/PlayPalace11/server/games/base.py#L86) class already inherits these mixins:
- `GameSoundMixin`
- `GameCommunicationMixin`
- `GameResultMixin`
- `DurationEstimateMixin`
- `GameScoresMixin`
- `GamePredictionMixin`
- `TurnManagementMixin`
- `MenuManagementMixin`
- `ActionVisibilityMixin`
- `LobbyActionsMixin`
- `EventHandlingMixin`
- `ActionSetCreationMixin`
- `ActionExecutionMixin`
- `OptionsHandlerMixin`
- `ActionSetSystemMixin`

That means most games already have this infrastructure without needing extra inheritance.

Representative standard games that rely mostly on `Game` plus local logic:
- [PigGame](/home/jjm/code/PlayPalace11/server/games/pig/game.py)
- [ScopaGame](/home/jjm/code/PlayPalace11/server/games/scopa/game.py)
- [HoldemGame](/home/jjm/code/PlayPalace11/server/games/holdem/game.py)
- [BlackjackGame](/home/jjm/code/PlayPalace11/server/games/blackjack/game.py)

## Optional Mixins a Game Adds Explicitly

Some mixins are not built into `Game` and are added only by games that need them.

Current examples:
- `ActionGuardMixin`
  - used by [RollingBallsGame](/home/jjm/code/PlayPalace11/server/games/rollingballs/game.py#L131), [LeftRightCenterGame](/home/jjm/code/PlayPalace11/server/games/leftrightcenter/game.py#L53)
- `RoundBasedGameMixin`
  - used by [PigGame](/home/jjm/code/PlayPalace11/server/games/pig/game.py#L87), [TossUpGame](/home/jjm/code/PlayPalace11/server/games/tossup/game.py#L81), [MidnightGame](/home/jjm/code/PlayPalace11/server/games/midnight/game.py#L55)
- `PushYourLuckBotMixin`
  - used by [PigGame](/home/jjm/code/PlayPalace11/server/games/pig/game.py#L87), [TossUpGame](/home/jjm/code/PlayPalace11/server/games/tossup/game.py#L81)
- `DiceGameMixin`
  - used by [YahtzeeGame](/home/jjm/code/PlayPalace11/server/games/yahtzee/game.py#L202), [MidnightGame](/home/jjm/code/PlayPalace11/server/games/midnight/game.py#L55), [ThreesGame](/home/jjm/code/PlayPalace11/server/games/threes/game.py#L55)

Use these only when the game structure genuinely matches the existing abstraction.

## Core Mixins Included by `Game`

### `GameSoundMixin`
File: [server/game_utils/game_sound_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/game_sound_mixin.py)

Purpose:
- Centralized sound scheduling and playback for games.

What it gives you:
- delayed sound scheduling
- queued sound processing on tick
- broadcast sound/music/ambience helpers
- `play_sound()` convenience use throughout game code

Typical expectations on `Game`:
- `players`
- `get_user(player)`
- serialized scheduler state fields already present on `Game`

Representative consumers:
- almost every game through base `Game`
- examples with heavy scheduled audio use:
  - [HoldemGame](/home/jjm/code/PlayPalace11/server/games/holdem/game.py)
  - [FiveCardDrawGame](/home/jjm/code/PlayPalace11/server/games/fivecarddraw/game.py)
  - [CrazyEightsGame](/home/jjm/code/PlayPalace11/server/games/crazyeights/game.py)

When not to use extra abstraction:
- if a game just needs to call `play_sound`, use the mixin as-is
- do not create a second per-game sound framework unless the existing scheduler is insufficient

### `GameCommunicationMixin`
File: [server/game_utils/game_communication_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/game_communication_mixin.py)

Purpose:
- Shared localized communication helpers.

What it gives you:
- `broadcast()`
- `broadcast_l()`
- `broadcast_personal_l()`
- `label_l()`

Typical expectations on `Game`:
- `players`
- `get_user(player)`

Representative consumers:
- effectively all games through base `Game`
- clear examples of personal-vs-table messaging:
  - [ScopaGame](/home/jjm/code/PlayPalace11/server/games/scopa/game.py)
  - [BlackjackGame](/home/jjm/code/PlayPalace11/server/games/blackjack/game.py)

When not to use:
- use `user.speak()` / `user.speak_l()` for direct command responses, not table transcript events

### `GameResultMixin`
File: [server/game_utils/game_result_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/game_result_mixin.py)

Purpose:
- Standard end-of-game result lifecycle.

What it gives you:
- `finish_game()`
- result persistence
- ratings update
- end-screen presentation pipeline

Games call `make_game_result(custom_data=...)` from `build_game_result()` to reuse
participant, score, team, and winner handling. Consumers use `get_winner_ids()`
and `get_player_score()` rather than interpreting each game's display strings.
Use `eliminate_player()` when a participant sits out the rest of a game; their
result remains recorded even though they no longer take turns.

`finish_game()` saves once and retains the result for reconnects. After completion,
the host can play again or select another game at the same table. The table's
`prepare_next_game()` creates a fresh game and player state, retains seats and
spectator roles, and copies options only for a replay of the same game. New games
must keep authoritative state in dataclass fields; do not add per-game replay reset
methods. This separates table lifetime from individual games without introducing
a tournament or mixed-game round controller.

Typical expectations on `Game`:
- `build_game_result()`
- `format_end_screen()`
- `get_type()`
- `get_active_players()`
- `destroy()`

Representative consumers:
- [HoldemGame](/home/jjm/code/PlayPalace11/server/games/holdem/game.py)
- [FiveCardDrawGame](/home/jjm/code/PlayPalace11/server/games/fivecarddraw/game.py)
- [ScopaGame](/home/jjm/code/PlayPalace11/server/games/scopa/game.py)

When not to use:
- if the game ends in the standard PlayPalace way, use this
- do not bypass it unless the game truly has a different result lifecycle

### `DurationEstimateMixin`
File: [server/game_utils/duration_estimate_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/duration_estimate_mixin.py)

Purpose:
- Simulation-based duration estimation.

What it gives you:
- estimate action entry point
- simulation thread management
- result aggregation

Typical expectations on `Game`:
- estimate state fields already present on `Game`
- `broadcast`/`broadcast_l`
- `get_type()`
- `get_min_players()`

When to use:
- if the game supports estimation and can be safely simulated

When not to use:
- if the game’s simulation path is not stable or not representative

### `GameScoresMixin`
File: [server/game_utils/game_scores_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/game_scores_mixin.py)

Purpose:
- Standard score and “whose turn” reporting.

What it gives you:
- common score readout actions
- current-player announcement action

Typical expectations on `Game`:
- `current_player`
- `players`
- `get_user(player)`
- `status_box(...)`
- team-based score state if using the default score path

Representative consumers:
- many standard games via base `Game`

When not to use:
- if the game has custom score semantics or a custom status model

Examples that often override adjacent score/status behavior:
- [ScopaGame](/home/jjm/code/PlayPalace11/server/games/scopa/game.py)
- [PiratesGame](/home/jjm/code/PlayPalace11/server/games/pirates/game.py)

### `GamePredictionMixin`
File: [server/game_utils/game_prediction_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/game_prediction_mixin.py)

Purpose:
- Shared rating-based outcome prediction action.

What it gives you:
- player rating collection
- prediction formatting

Typical expectations on `Game`:
- `_table`
- `players`
- `get_user(player)`
- `status_box(...)`
- `get_type()`

### `TurnManagementMixin`
File: [server/game_utils/turn_management_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/turn_management_mixin.py)

Purpose:
- Standard turn-order operations.

What it gives you:
- `current_player` property
- `set_turn_players()`
- `advance_turn()`
- skip/reverse/reset helpers
- standard turn announcement

Typical expectations on `Game`:
- `turn_player_ids`
- `turn_index`
- `turn_direction`
- `turn_skip_count`
- `get_player_by_id(...)`
- `get_user(player)`
- `broadcast_l(...)`
- `rebuild_all_menus()`

Representative consumers:
- almost every turn-based game
- good examples:
  - [PigGame](/home/jjm/code/PlayPalace11/server/games/pig/game.py)
  - [NinetyNineGame](/home/jjm/code/PlayPalace11/server/games/ninetynine/game.py)
  - [CrazyEightsGame](/home/jjm/code/PlayPalace11/server/games/crazyeights/game.py)

When not to use:
- if the game has no concept of sequential turns
- if the game has a radically different control loop that cannot be modeled with `turn_player_ids`

### `MenuManagementMixin`
File: [server/game_utils/menu_management_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/menu_management_mixin.py)

Purpose:
- Standard menu rebuild/update/status-box flow.

What it gives you:
- rebuild menu for one or all players
- update menu while preserving selection where possible
- status box support

Typical expectations on `Game`:
- `players`
- `_destroyed`
- `status`
- `_status_box_open`
- `get_user(player)`
- `get_all_visible_actions(player)`

Representative consumers:
- nearly all games through `Game`
- examples with custom rebuild behavior layered on top:
  - [ChessGame](/home/jjm/code/PlayPalace11/server/games/chess/game.py)
  - [RollingBallsGame](/home/jjm/code/PlayPalace11/server/games/rollingballs/game.py)

When not to use:
- custom menu layout should extend or override this, not replace the whole system casually

### `ActionVisibilityMixin`
File: [server/game_utils/action_visibility_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/action_visibility_mixin.py)

Purpose:
- Visibility filtering for actions and menus.

What it gives you:
- common visible/hidden filtering pipeline
- support for action guard methods returning visibility states

Typical expectations on `Game`:
- action-set system from the other shared mixins

Representative consumers:
- all standard action-driven games

### `LobbyActionsMixin`
File: [server/game_utils/lobby_actions_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/lobby_actions_mixin.py)

Purpose:
- Standard pregame lobby behavior.

What it gives you:
- start-game flow
- host/bot/lobby actions
- standard lobby naming support

Typical expectations on `Game`:
- host/player management from `Game`
- menu/action system

Representative consumers:
- most standard games

When not to use:
- if a game has a radically custom lobby or pregame configuration flow, override selectively rather than reimplementing all lobby behavior

### `EventHandlingMixin`
File: [server/game_utils/event_handling_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/event_handling_mixin.py)

Purpose:
- Shared scheduled-event dispatch.

What it gives you:
- event queue processing
- event dispatch hooks

Representative consumers:
- event-heavy or animation-heavy games
- examples:
  - [AgeOfHeroesGame](/home/jjm/code/PlayPalace11/server/games/ageofheroes/game.py)

### `ActionSetCreationMixin`
File: [server/game_utils/action_set_creation_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/action_set_creation_mixin.py)

Purpose:
- Shared creation of standard/lobby/turn action sets.

What it gives you:
- common scaffolding for building action menus

Typical expectations on `Game`:
- game-specific `create_turn_action_set(...)` where appropriate

### `ActionExecutionMixin`
File: [server/game_utils/action_execution_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/action_execution_mixin.py)

Purpose:
- Standard action invocation pipeline.

What it gives you:
- action lookup
- pending-input flow
- handler invocation

When not to bypass:
- almost never bypass this in a normal game; it is part of the platform contract

### `ActionSetSystemMixin`
File: [server/game_utils/action_set_system_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/action_set_system_mixin.py)

Purpose:
- Registration and organization of action sets.

What it gives you:
- player action-set storage helpers
- action-set lookup plumbing

### `OptionsHandlerMixin`
File: [server/game_utils/options.py](/home/jjm/code/PlayPalace11/server/game_utils/options.py)

Purpose:
- Standard options menu behavior for declarative options.

What it gives you:
- option action generation
- grouped options
- multiselect options
- menu navigation for option screens

Typical expectations on `Game`:
- `options` dataclass built from `GameOptions`
- normal action/menu system

Representative consumers:
- [BlackjackOptions and BlackjackGame](/home/jjm/code/PlayPalace11/server/games/blackjack/game.py)
- [ScopaOptions and ScopaGame](/home/jjm/code/PlayPalace11/server/games/scopa/game.py)
- [HoldemOptions and HoldemGame](/home/jjm/code/PlayPalace11/server/games/holdem/game.py)

When not to use:
- if a game needs an unusual setup flow that does not map to standard options menus

## Optional Mixins

These are added directly by games that fit their pattern.

### `ActionGuardMixin`
File: [server/game_utils/action_guard_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/action_guard_mixin.py)

Purpose:
- Lightweight organization around guard-style action checks.

Use when:
- the game has many `_is_*_enabled` / `_is_*_hidden` style helpers
- guard code benefits from a common pattern

Representative consumers:
- [RollingBallsGame](/home/jjm/code/PlayPalace11/server/games/rollingballs/game.py#L131)
- [FarkleGame](/home/jjm/code/PlayPalace11/server/games/farkle/game.py#L288)

When not to use:
- if the game has only a handful of straightforward guards, local methods are usually enough

### `RoundBasedGameMixin`
File: [server/game_utils/round_based_game_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/round_based_game_mixin.py)

Purpose:
- Shared scaffolding for games whose top-level structure is explicitly round-based.

Use when:
- the game repeatedly runs a round lifecycle with consistent reset/start/end hooks

Representative consumers:
- [PigGame](/home/jjm/code/PlayPalace11/server/games/pig/game.py#L87)
- [TossUpGame](/home/jjm/code/PlayPalace11/server/games/tossup/game.py#L81)
- [MidnightGame](/home/jjm/code/PlayPalace11/server/games/midnight/game.py#L55)

When not to use:
- if “rounds” exist only loosely and most logic is still hand-authored state transitions

### `PushYourLuckBotMixin`
File: [server/game_utils/push_your_luck_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/push_your_luck_mixin.py)

Purpose:
- Shared bot target/decision rhythm for push-your-luck games.

Use when:
- bots choose whether to continue pushing or bank/stop based on a dynamic target

Representative consumers:
- [PigGame](/home/jjm/code/PlayPalace11/server/games/pig/game.py#L87)
- [TossUpGame](/home/jjm/code/PlayPalace11/server/games/tossup/game.py#L81)

When not to use:
- if bot logic is not actually target-based push-your-luck logic

### `DiceGameMixin`
File: [server/game_utils/dice_game_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/dice_game_mixin.py)

Purpose:
- Shared support for dice-centric games.

Use when:
- the game has recurring dice interaction patterns already covered by the mixin

Representative consumers:
- [YahtzeeGame](/home/jjm/code/PlayPalace11/server/games/yahtzee/game.py#L202)
- [MidnightGame](/home/jjm/code/PlayPalace11/server/games/midnight/game.py#L55)
- [ThreesGame](/home/jjm/code/PlayPalace11/server/games/threes/game.py#L55)

## Generic Helper Modules

These are reusable modules, not mixins.

### Actions
File: [server/game_utils/actions.py](/home/jjm/code/PlayPalace11/server/game_utils/actions.py)

Use for:
- action dataclasses
- action inputs
- action-set definitions

Includes:
- `Action`
- `ActionSet`
- `MenuInput`
- `EditboxInput`

Representative consumer:
- nearly every game file

### Options
File: [server/game_utils/options.py](/home/jjm/code/PlayPalace11/server/game_utils/options.py)

Use for:
- declarative game options
- menu-driven game setup

Includes:
- `GameOptions`
- `option_field(...)`
- option metadata classes such as `IntOption`, `BoolOption`, `MenuOption`

Representative consumers:
- [BlackjackGame](/home/jjm/code/PlayPalace11/server/games/blackjack/game.py)
- [ScopaGame](/home/jjm/code/PlayPalace11/server/games/scopa/game.py)
- [HoldemGame](/home/jjm/code/PlayPalace11/server/games/holdem/game.py)

### Results and Ratings
Files:
- [server/game_utils/game_result.py](/home/jjm/code/PlayPalace11/server/game_utils/game_result.py)
- [server/game_utils/stats_helpers.py](/home/jjm/code/PlayPalace11/server/game_utils/stats_helpers.py)

Use for:
- structured game result payloads
- leaderboard/rating helpers

### Timers
Files:
- [server/game_utils/round_timer.py](/home/jjm/code/PlayPalace11/server/game_utils/round_timer.py)
- [server/game_utils/poker_timer.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_timer.py)

Use for:
- round transitions and pauses: `RoundTransitionTimer`
- simple turn countdowns: `PokerTurnTimer`

Representative consumers:
- [ScopaGame](/home/jjm/code/PlayPalace11/server/games/scopa/game.py) uses `RoundTransitionTimer`
- [BlackjackGame](/home/jjm/code/PlayPalace11/server/games/blackjack/game.py) uses `PokerTurnTimer`
- [HoldemGame](/home/jjm/code/PlayPalace11/server/games/holdem/game.py) uses `PokerTurnTimer`

### Teams
File: [server/game_utils/teams.py](/home/jjm/code/PlayPalace11/server/game_utils/teams.py)

Use for:
- team assignment
- team score aggregation
- team mode selection helpers

Representative consumers:
- [ScopaGame](/home/jjm/code/PlayPalace11/server/games/scopa/game.py)
- many games indirectly through `Game`’s `_team_manager`

### Cards
File: [server/game_utils/cards.py](/home/jjm/code/PlayPalace11/server/game_utils/cards.py)

Use for:
- `Card`
- `Deck`
- `DeckFactory`
- card naming and reading helpers
- generic card sorting

Representative consumers:
- [ScopaGame](/home/jjm/code/PlayPalace11/server/games/scopa/game.py)
- [BlackjackGame](/home/jjm/code/PlayPalace11/server/games/blackjack/game.py)
- [CrazyEightsGame](/home/jjm/code/PlayPalace11/server/games/crazyeights/game.py)
- [NinetyNineGame](/home/jjm/code/PlayPalace11/server/games/ninetynine/game.py)
- [HoldemGame](/home/jjm/code/PlayPalace11/server/games/holdem/game.py)
- [FiveCardDrawGame](/home/jjm/code/PlayPalace11/server/games/fivecarddraw/game.py)

When not to use:
- if a game uses a nonstandard deck model with very different semantics, extend carefully or keep custom card primitives local

### Dice
File: [server/game_utils/dice.py](/home/jjm/code/PlayPalace11/server/game_utils/dice.py)

Use for:
- dice rolling
- dice counting/pattern helpers
- reusable dice scoring predicates

Representative consumers:
- [YahtzeeGame](/home/jjm/code/PlayPalace11/server/games/yahtzee/game.py)
- [FarkleGame](/home/jjm/code/PlayPalace11/server/games/farkle/game.py)

## Poker-Specific Shared Helpers

These helpers are for poker-family games, not for all card games.

### Betting and Table State
Files:
- [server/game_utils/poker_betting.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_betting.py)
- [server/game_utils/poker_table.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_table.py)
- [server/game_utils/poker_state.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_state.py)
- [server/game_utils/poker_actions.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_actions.py)

Purpose:
- shared betting-round state
- button/blind positioning
- order-after-button helpers
- raise-cap helpers for limit modes

Representative consumers:
- [HoldemGame](/home/jjm/code/PlayPalace11/server/games/holdem/game.py)
- [FiveCardDrawGame](/home/jjm/code/PlayPalace11/server/games/fivecarddraw/game.py)

### Hand Evaluation and Showdown
Files:
- [server/game_utils/poker_evaluator.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_evaluator.py)
- [server/game_utils/poker_showdown.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_showdown.py)

Purpose:
- shared poker hand scoring
- best-hand selection
- human-readable hand descriptions
- showdown ordering/formatting

Representative consumers:
- [HoldemGame](/home/jjm/code/PlayPalace11/server/games/holdem/game.py)
- [FiveCardDrawGame](/home/jjm/code/PlayPalace11/server/games/fivecarddraw/game.py)
- potentially future poker-family games

### Pot Computation and Payout
Files:
- [server/game_utils/poker_pot.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_pot.py)
- [server/game_utils/poker_payout.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_payout.py)

Purpose:
- compute main/side pots from contributions
- resolve winners for a pot
- split payouts in winner order
- handle odd chips correctly
- resolve multiple pots and optionally apply awards

What is shared now:
- contribution-to-pot conversion
- winner ordering
- odd-chip distribution
- multi-pot payout resolution

What still stays local to each game:
- sound effects
- localized winner announcements
- phase transitions after showdown
- game-specific winner tracking fields

Representative consumers:
- [HoldemGame](/home/jjm/code/PlayPalace11/server/games/holdem/game.py#L891)
- [FiveCardDrawGame](/home/jjm/code/PlayPalace11/server/games/fivecarddraw/game.py#L770)

This is the right pattern for future poker games:
- keep payout math shared
- keep presentation and phase control local

### Poker UX Helpers
Files:
- [server/game_utils/poker_keybinds.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_keybinds.py)
- [server/game_utils/poker_log.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_log.py)
- [server/game_utils/poker_timer.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_timer.py)

Purpose:
- consistent keybind wiring
- simple action-log helpers
- reusable turn countdown support

## Exported Surface Versus Internal Modules

The exported surface in [server/game_utils/__init__.py](/home/jjm/code/PlayPalace11/server/game_utils/__init__.py) is the broad, intended reusable API for many games.

Not every file in `game_utils/` is exported there.

Specialized modules such as poker helpers are often imported directly from their file because they are family-specific rather than globally shared.

## How to Decide Where New Logic Should Go

### Put logic in a shared mixin or helper when:
- at least two games already need the same infrastructure
- the abstraction boundary is stable
- the behavior is mostly rule-agnostic
- future games are likely to reuse it

### Keep logic in a game file when:
- it is a rule engine
- it is mostly unique to one game
- extracting it would require many game-specific conditionals
- the only commonality is superficial

### Prefer helper modules over new mixins when:
- the logic is mostly pure functions or small data helpers
- the game does not need stateful multiple inheritance

### Prefer mixins over helper modules when:
- the logic expects a `Game` instance shape
- it naturally extends game behavior through methods/hooks
- many methods operate on shared `Game` state

## Representative Starting Points for New Contributors

If you are trying to understand the shared system through real games:

- Basic turn/action game:
  - [PigGame](/home/jjm/code/PlayPalace11/server/games/pig/game.py)
- Card game with direct `cards.py` use:
  - [ScopaGame](/home/jjm/code/PlayPalace11/server/games/scopa/game.py)
- Poker-family shared helpers:
  - [HoldemGame](/home/jjm/code/PlayPalace11/server/games/holdem/game.py)
  - [FiveCardDrawGame](/home/jjm/code/PlayPalace11/server/games/fivecarddraw/game.py)
- Dice-game shared helpers:
  - [YahtzeeGame](/home/jjm/code/PlayPalace11/server/games/yahtzee/game.py)
- Grid/menu customization:
  - [ChessGame](/home/jjm/code/PlayPalace11/server/games/chess/game.py)

## Appendix: `server/game_utils` Module Index

This appendix is a compact inventory of every top-level module in `server/game_utils/`.

- [__init__.py](/home/jjm/code/PlayPalace11/server/game_utils/__init__.py): Broad export surface for commonly reused shared utilities.
- [action_execution_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/action_execution_mixin.py): Core action execution pipeline, including handler dispatch and pending-input flow.
- [action_guard_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/action_guard_mixin.py): Optional lightweight helper for organizing guard-style action checks.
- [action_set_creation_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/action_set_creation_mixin.py): Shared scaffolding for building standard action sets.
- [action_set_system_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/action_set_system_mixin.py): Shared registration and lookup support for action sets.
- [action_visibility_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/action_visibility_mixin.py): Shared visibility filtering for action/menu presentation.
- [actions.py](/home/jjm/code/PlayPalace11/server/game_utils/actions.py): Core action dataclasses such as `Action`, `ActionSet`, and menu/editbox input models.
- [bot_helper.py](/home/jjm/code/PlayPalace11/server/game_utils/bot_helper.py): Shared bot timing and pending-action execution helpers used by many games.
- [cards.py](/home/jjm/code/PlayPalace11/server/game_utils/cards.py): Generic card, deck, deck-factory, naming, and card-reading helpers.
- [dice.py](/home/jjm/code/PlayPalace11/server/game_utils/dice.py): Dice primitives plus counting and scoring-pattern helpers.
- [dice_game_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/dice_game_mixin.py): Optional mixin for recurring dice-game behavior.
- [duration_estimate_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/duration_estimate_mixin.py): Simulation-based duration estimate support.
- [event_handling_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/event_handling_mixin.py): Shared scheduled-event dispatch machinery.
- [game_communication_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/game_communication_mixin.py): Shared localized table/player communication helpers.
- [game_prediction_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/game_prediction_mixin.py): Rating-based prediction action support.
- [game_result.py](/home/jjm/code/PlayPalace11/server/game_utils/game_result.py): Structured result dataclasses used for persistence and end screens.
- [game_result_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/game_result_mixin.py): Standard end-of-game lifecycle and persistence flow.
- [game_scores_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/game_scores_mixin.py): Standard score and current-turn reporting actions.
- [game_sound_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/game_sound_mixin.py): Shared sound scheduling and playback support.
- [lobby_actions_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/lobby_actions_mixin.py): Standard lobby actions and pregame table-management behavior.
- [menu_management_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/menu_management_mixin.py): Shared menu rebuild/update and status-box behavior.
- [options.py](/home/jjm/code/PlayPalace11/server/game_utils/options.py): Declarative options framework and options-menu handling mixin.
- [poker_actions.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_actions.py): Shared raise-cap and pot-limit helper functions for poker-family games.
- [poker_betting.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_betting.py): Betting-round state model for poker-family games.
- [poker_evaluator.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_evaluator.py): Poker hand scoring and human-readable hand-description helpers.
- [poker_keybinds.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_keybinds.py): Shared keybind wiring for poker-family games.
- [poker_log.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_log.py): Small action-log helpers for poker-family games.
- [poker_payout.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_payout.py): Shared poker pot winner resolution and payout splitting, including odd-chip handling.
- [poker_pot.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_pot.py): Main/side-pot computation from player contributions.
- [poker_showdown.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_showdown.py): Shared showdown ordering and formatting helpers for poker-family games.
- [poker_state.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_state.py): Shared seat-order helpers for poker-family games.
- [poker_table.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_table.py): Shared button and blind-position state for poker-family games.
- [poker_timer.py](/home/jjm/code/PlayPalace11/server/game_utils/poker_timer.py): Simple per-turn countdown timer used by poker-family and similar games.
- [push_your_luck_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/push_your_luck_mixin.py): Optional bot helper mixin for push-your-luck games.
- [round_based_game_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/round_based_game_mixin.py): Optional mixin for round-structured games.
- [round_timer.py](/home/jjm/code/PlayPalace11/server/game_utils/round_timer.py): Pauseable round transition timer.
- [stats_helpers.py](/home/jjm/code/PlayPalace11/server/game_utils/stats_helpers.py): Shared leaderboard and rating helper classes.
- [teams.py](/home/jjm/code/PlayPalace11/server/game_utils/teams.py): Team data model and team-management helpers.
- [turn_management_mixin.py](/home/jjm/code/PlayPalace11/server/game_utils/turn_management_mixin.py): Shared turn order, current-player, skip, reverse, and announcement helpers.

## Related Docs

- [Game Developer's Guide](/home/jjm/code/PlayPalace11/docs/design/plans/game_development_guide.md)
- [Plan: Extract Mixins from games/base.py](/home/jjm/code/PlayPalace11/docs/design/plans/base_game_reduction_plan.md)
- [2026-03-19 Card Game Helper Modernization Plan](/home/jjm/code/PlayPalace11/docs/plans/2026-03-19-card-game-helper-modernization-plan.md)
