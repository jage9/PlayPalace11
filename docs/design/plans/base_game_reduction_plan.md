# Plan: Extract Mixins from games/base.py

## Overview

**Goal:** Reduce `games/base.py` file size by extracting cohesive functionality into reusable mixins while keeping core game infrastructure intact.

**Why:** The base Game class became too large (2,277 lines), making it hard to navigate and maintain. Extracting into mixins improves organization and allows games to potentially opt out of certain functionality.

**Approach:**
- Each mixin is a standalone class in `game_utils/`
- Uses `TYPE_CHECKING` imports to avoid circular dependencies
- Mixins define abstract method stubs for methods they expect the Game class to provide
- Game class inherits from all mixins via multiple inheritance
- Mixins are exported from `game_utils/__init__.py`

**What stays in base.py (core functions):**
- Game state fields and `__post_init__`
- Abstract methods (`get_name`, `get_type`, `on_start`)
- Player/user management (`get_user`, `attach_user`, `get_player_by_id`)
- Action system core (`execute_action`, `find_action`, `resolve_action`, action sets)
- Event handling (`handle_event`)
- `current_player` property and `end_turn`

**To continue extraction:** Follow the existing mixin pattern - create a new file, define the class with docstring listing expected attributes/methods, add TYPE_CHECKING imports, implement methods, then remove from base.py and add to inheritance chain.

---

## Progress Summary

| Phase | Starting Lines | Ending Lines | Reduction |
|-------|---------------|--------------|-----------|
| Phase 1 | 2,277 | 1,687 | 590 (26%) |
| Phase 2 | 1,687 | 1,136 | 551 (33%) |
| Phase 3 | 1,136 | 493 | 643 (57%) |
| Phase 3.1 | 493 | 316 | 177 (36%) |
| **Total** | **2,277** | **316** | **1,961 (86%)** |

---

## Phase 1: Initial Mixin Extraction

### Goal
Reduce `games/base.py` (2,277 lines) by at least 30% (~683 lines) by extracting functionality into reusable mixins.

### Mixins Created

| Mixin | Lines to Extract | Approx. Size |
|-------|------------------|--------------|
| `GameSoundMixin` | 898-952, 1029-1067 | ~95 lines |
| `GameCommunicationMixin` | 956-1028 | ~72 lines |
| `GameResultMixin` | 298-451 | ~154 lines |
| `DurationEstimateMixin` | 2105-2277 | ~172 lines |
| `GameScoresMixin` | 1901-1932 | ~32 lines |
| `GamePredictionMixin` | 1934-1996 | ~62 lines |
| **Total** | | **~587 lines** |

### Mixin Specifications

#### 1. GameSoundMixin (`game_utils/game_sound_mixin.py`)
**Methods:**
- `schedule_sound()` - Schedule sound with delay
- `schedule_sound_sequence()` - Schedule multiple sounds
- `clear_scheduled_sounds()` - Clear scheduled sounds
- `process_scheduled_sounds()` - Process and play scheduled sounds
- `broadcast_sound()` - Play sound for all players
- `play_sound()` - Alias for broadcast_sound
- `play_music()` - Play music for all players
- `play_ambience()` - Play ambient sounds
- `stop_ambience()` - Stop ambient sounds

**Expects on Game class:**
- `self.scheduled_sounds: list`
- `self.sound_scheduler_tick: int`
- `self.current_music: str`
- `self.current_ambience: str`
- `self.players: list[Player]`
- `self.get_user(player) -> User | None`

#### 2. GameCommunicationMixin (`game_utils/game_communication_mixin.py`)
**Methods:**
- `broadcast()` - Send text to all players
- `broadcast_l()` - Send localized message to all
- `broadcast_personal_l()` - Personal vs others messages
- `label_l()` - Create localized label callable

**Expects on Game class:**
- `self.players: list[Player]`
- `self.get_user(player) -> User | None`

#### 3. GameResultMixin (`game_utils/game_result_mixin.py`)
**Methods:**
- `finish_game()` - Mark game finished, persist, show end
- `build_game_result()` - Build GameResult object
- `format_end_screen()` - Format end screen lines
- `_persist_result()` - Save to database
- `_update_ratings()` - Update player ratings
- `get_rankings_for_rating()` - Get rankings for rating
- `_show_end_screen()` - Display end screen
- `show_game_end_menu()` - Deprecated legacy method

**Expects on Game class:**
- `self.game_active: bool`
- `self.status: str`
- `self.players: list[Player]`
- `self.sound_scheduler_tick: int`
- `self._table: Any`
- `self.get_user(player) -> User | None`
- `self.get_type() -> str`
- `self.get_active_players() -> list[Player]`
- `self.destroy()`

#### 4. DurationEstimateMixin (`game_utils/duration_estimate_mixin.py`)
**Constants:**
- `NUM_ESTIMATE_SIMULATIONS = 10`
- `HUMAN_SPEED_MULTIPLIER = 2`

**Methods:**
- `_action_estimate_duration()` - Start CLI simulations
- `check_estimate_completion()` - Check if done (called from on_tick)
- `_calculate_std_dev()` - Calculate standard deviation
- `_detect_outliers()` - Detect outliers using IQR
- `_format_duration()` - Format ticks as readable time

**Expects on Game class:**
- `self._estimate_threads: list`
- `self._estimate_results: list`
- `self._estimate_errors: list`
- `self._estimate_running: bool`
- `self._estimate_lock: threading.Lock`
- `self.players: list[Player]`
- `self.get_user(player) -> User | None`
- `self.broadcast_l()` / `self.broadcast()`
- `self.get_type() -> str`
- `self.get_min_players() -> int`
- `self.TICKS_PER_SECOND: int`

#### 5. GameScoresMixin (`game_utils/game_scores_mixin.py`)
**Methods:**
- `_action_whose_turn()` - Announce current player
- `_action_check_scores()` - Brief score announcement
- `_action_check_scores_detailed()` - Detailed scores in status box

**Expects on Game class:**
- `self.current_player: Player | None`
- `self.team_manager: TeamManager`
- `self.players: list[Player]`
- `self.get_user(player) -> User | None`
- `self.status_box(player, lines)`

#### 6. GamePredictionMixin (`game_utils/game_prediction_mixin.py`)
**Methods:**
- `_action_predict_outcomes()` - Show win probability predictions

**Expects on Game class:**
- `self._table: Any`
- `self.players: list[Player]`
- `self.get_user(player) -> User | None`
- `self.get_type() -> str`
- `self.status_box(player, lines)`

---

## Phase 2: Additional Mixin Extraction

### Goal
Reduce `games/base.py` from 1,687 lines by another 30% (~506 lines) to approximately 1,181 lines.

### Mixins Created

| Mixin | Lines to Extract | Approx. Size |
|-------|------------------|--------------|
| `TurnManagementMixin` | 646-746 | ~100 lines |
| `MenuManagementMixin` | 748-818 | ~70 lines |
| `LobbyActionsMixin` | 1404-1579 | ~175 lines |
| `ActionVisibilityMixin` | 985-1160 | ~175 lines |
| **Total** | | **~520 lines** |

### Mixin Specifications

#### 1. TurnManagementMixin (`game_utils/turn_management_mixin.py`)
**Methods:**
- `set_turn_players()` - Set players in turn order
- `advance_turn()` - Move to next player's turn
- `skip_next_players()` - Queue players to skip
- `on_player_skipped()` - Called when player is skipped (hook)
- `reverse_turn_direction()` - Reverse turn order
- `reset_turn_order()` - Reset to first player
- `announce_turn()` - Announce current player's turn
- `turn_players` property - Get players in turn order

**Expects on Game class:**
- `self.turn_player_ids: list[str]`
- `self.turn_index: int`
- `self.turn_direction: int`
- `self.turn_skip_count: int`
- `self.get_player_by_id(player_id) -> Player | None`
- `self.get_user(player) -> User | None`
- `self.broadcast_l(message_id, **kwargs)`
- `self.rebuild_all_menus()`
- `self.current_player` property

#### 2. MenuManagementMixin (`game_utils/menu_management_mixin.py`)
**Methods:**
- `rebuild_player_menu()` - Rebuild menu for one player
- `rebuild_all_menus()` - Rebuild menus for all players
- `update_player_menu()` - Update menu preserving focus
- `update_all_menus()` - Update all menus preserving focus
- `status_box()` - Show status box to player

**Expects on Game class:**
- `self._destroyed: bool`
- `self.status: str`
- `self.players: list[Player]`
- `self._status_box_open: set[str]`
- `self.get_user(player) -> User | None`
- `self.get_all_visible_actions(player) -> list[ResolvedAction]`

#### 3. LobbyActionsMixin (`game_utils/lobby_actions_mixin.py`)
**Methods:**
- `_action_start_game()` - Start the game
- `_bot_input_add_bot()` - Get bot name automatically
- `_action_add_bot()` - Add bot to game
- `_action_remove_bot()` - Remove bot from game
- `_action_toggle_spectator()` - Toggle spectator mode
- `_action_leave_game()` - Leave the game
- `_action_show_actions_menu()` - Show F5 actions menu
- `_action_save_table()` - Save table state

**Expects on Game class:**
- `self.status: str`
- `self.host: str`
- `self.players: list[Player]`
- `self._table: Any`
- `self._users: dict`
- `self._actions_menu_open: set[str]`
- `self.player_action_sets: dict`
- `self.get_user(player) -> User | None`
- `self.broadcast_l()`, `self.broadcast_sound()`
- `self.prestart_validate()`, `self.on_start()`
- `self.create_player()`, `self.setup_player_actions()`
- `self.attach_user()`, `self.rebuild_all_menus()`
- `self.destroy()`
- `self.get_all_enabled_actions()`
- `self._get_keybind_for_action()`

#### 4. ActionVisibilityMixin (`game_utils/action_visibility_mixin.py`)
**Methods (all is_enabled/is_hidden/get_label):**
- `_is_start_game_enabled()`, `_is_start_game_hidden()`
- `_is_add_bot_enabled()`, `_is_add_bot_hidden()`
- `_is_remove_bot_enabled()`, `_is_remove_bot_hidden()`
- `_is_toggle_spectator_enabled()`, `_is_toggle_spectator_hidden()`
- `_get_toggle_spectator_label()`
- `_is_leave_game_enabled()`, `_is_leave_game_hidden()`
- `_is_option_enabled()`, `_is_option_hidden()`
- `_is_estimate_duration_enabled()`, `_is_estimate_duration_hidden()`
- `_is_show_actions_enabled()`, `_is_show_actions_hidden()`
- `_is_save_table_enabled()`, `_is_save_table_hidden()`
- `_is_whose_turn_enabled()`, `_is_whose_turn_hidden()`
- `_is_check_scores_enabled()`, `_is_check_scores_hidden()`
- `_is_check_scores_detailed_enabled()`, `_is_check_scores_detailed_hidden()`
- `_is_predict_outcomes_enabled()`, `_is_predict_outcomes_hidden()`

**Expects on Game class:**
- `self.status: str`
- `self.host: str`
- `self.players: list[Player]`
- `self.team_manager: TeamManager`
- `self.get_user(player) -> User | None`
- `self.get_min_players()`, `self.get_max_players()`
- `self.get_active_player_count()`

---

## Final Inheritance Structure

```python
@dataclass
class Game(
    ABC,
    DataClassJSONMixin,
    GameSoundMixin,
    GameCommunicationMixin,
    GameResultMixin,
    DurationEstimateMixin,
    GameScoresMixin,
    GamePredictionMixin,
    TurnManagementMixin,
    MenuManagementMixin,
    ActionVisibilityMixin,
    LobbyActionsMixin,
):
    """Abstract base class for all games."""
    ...
```

---

## Phase 3: Further Mixin Extraction

### Goal
Reduce `games/base.py` from 1,136 lines by extracting event handling, action execution, action set creation, and options handling.

### Mixins Created

| Mixin | Lines Extracted | Approx. Size |
|-------|-----------------|--------------|
| `EventHandlingMixin` | handle_event, menu/keybind events | ~175 lines |
| `ActionSetCreationMixin` | create_*_action_set, setup_keybinds | ~220 lines |
| `ActionExecutionMixin` | execute_action, input handling | ~180 lines |
| `OptionsHandlerMixin` | options methods (consolidated into options.py) | ~70 lines |
| **Total** | | **~645 lines** |

### Mixin Specifications

#### 1. EventHandlingMixin (`game_utils/event_handling_mixin.py`)
**Methods:**
- `handle_event()` - Main event dispatcher
- `_handle_menu_event()` - Handle menu selections
- `_handle_editbox_event()` - Handle editbox submissions
- `_handle_keybind_event()` - Handle keybind presses
- `_handle_actions_menu_selection()` - Handle F5 menu selection

**Expects on Game class:**
- `self._actions_menu_open: set[str]`
- `self._pending_actions: dict[str, str]`
- `self._status_box_open: set[str]`
- `self._keybinds: dict[str, list[Keybind]]`
- `self.get_user(player) -> User | None`
- `self.find_action()`, `self.resolve_action()`, `self.execute_action()`
- `self.get_all_visible_actions()`, `self.rebuild_player_menu()`, `self.rebuild_all_menus()`

#### 2. ActionSetCreationMixin (`game_utils/action_set_creation_mixin.py`)
**Methods:**
- `create_lobby_action_set()` - Create lobby actions (start, add bot, etc.)
- `create_estimate_action_set()` - Create duration estimate action
- `create_standard_action_set()` - Create standard actions (F5, save, scores)
- `setup_keybinds()` - Define all keybinds
- `create_turn_action_set()` - Override for game-specific turn actions
- `setup_player_actions()` - Set up all action sets for a player

**Expects on Game class:**
- `self.players: list[Player]`
- `self.player_action_sets: dict`
- `self._keybinds: dict`
- `self.get_user()`, `self.add_action_set()`, `self.define_keybind()`

#### 3. ActionExecutionMixin (`game_utils/action_execution_mixin.py`)
**Methods:**
- `execute_action()` - Execute an action for a player
- `get_action_context()` - Get current action context
- `_get_menu_options_for_action()` - Get menu options for action
- `_get_bot_input()` - Get automatic input for bots
- `_request_action_input()` - Request input from human players
- `end_turn()` - End current player's turn

**Expects on Game class:**
- `self._pending_actions: dict[str, str]`
- `self._action_context: dict[str, ActionContext]`
- `self.get_user()`, `self.find_action()`, `self.resolve_action()`, `self.advance_turn()`

#### 4. OptionsHandlerMixin (`game_utils/options.py` - consolidated)
**Methods:**
- `create_options_action_set()` - Create options action set
- `_handle_option_change()` - Handle option value changes
- `_handle_option_toggle()` - Handle boolean option toggles
- `_action_set_option()` - Generic set option handler
- `_action_toggle_option()` - Generic toggle option handler

**Expects on Game class:**
- `self.options: GameOptions`
- `self.get_user()`, `self.rebuild_all_menus()`

---

## Final Inheritance Structure (Phase 3)

```python
@dataclass
class Game(
    ABC,
    DataClassJSONMixin,
    GameSoundMixin,
    GameCommunicationMixin,
    GameResultMixin,
    DurationEstimateMixin,
    GameScoresMixin,
    GamePredictionMixin,
    TurnManagementMixin,
    MenuManagementMixin,
    ActionVisibilityMixin,
    LobbyActionsMixin,
    EventHandlingMixin,
    ActionSetCreationMixin,
    ActionExecutionMixin,
    OptionsHandlerMixin,
):
    """Abstract base class for all games."""
    ...
```

---

## Remaining in base.py (493 lines)

Core infrastructure that should stay in base.py:
- `ActionContext` dataclass
- `Player` dataclass
- `Game` class with:
  - Dataclass fields and `__post_init__`
  - Abstract methods (`get_name`, `get_type`, `on_start`)
  - Player management (`get_user`, `attach_user`, `get_player_by_*`)
  - Action set system core (`get_action_sets`, `find_action`, `resolve_action`)
  - Keybind definition (`define_keybind`, `_get_keybind_for_action`)
  - Player helpers (`get_active_players`, `get_human_count`, `create_player`)
  - `current_player` property and `team_manager` property
  - `destroy()`, `initialize_lobby()`

---

## Phase 3.1: Consolidation into Existing Mixins

### Goal
Further reduce `games/base.py` from 493 lines by moving methods into existing mixins and creating one new mixin for the action set system.

### Changes Made

| Move | Lines Moved | Target |
|------|-------------|--------|
| `define_keybind()`, `_get_keybind_for_action()` | ~43 | ActionSetCreationMixin |
| `_is_player_spectator()`, `get_active_players()`, `get_active_player_count()` | ~11 | ActionVisibilityMixin |
| `get_human_count()`, `get_bot_count()`, `create_player()`, `add_player()`, `destroy()`, `initialize_lobby()` | ~38 | LobbyActionsMixin |
| `current_player` property (getter/setter) | ~15 | TurnManagementMixin |
| Action set methods (new mixin) | ~60 | ActionSetSystemMixin |
| **Total** | **~167 lines** | |

### New Mixin Created

#### ActionSetSystemMixin (`game_utils/action_set_system_mixin.py`)
**Methods:**
- `get_action_sets()` - Get ordered list of action sets for a player
- `get_action_set()` - Get a specific action set by name
- `add_action_set()` - Add an action set to a player
- `remove_action_set()` - Remove an action set by name
- `find_action()` - Find an action by ID across all action sets
- `resolve_action()` - Resolve a single action's state
- `get_all_visible_actions()` - Get all visible actions
- `get_all_enabled_actions()` - Get all enabled actions

**Expects on Game class:**
- `self.player_action_sets: dict[str, list[ActionSet]]`

---

## Final Inheritance Structure (Phase 3.1)

```python
@dataclass
class Game(
    ABC,
    DataClassJSONMixin,
    GameSoundMixin,
    GameCommunicationMixin,
    GameResultMixin,
    DurationEstimateMixin,
    GameScoresMixin,
    GamePredictionMixin,
    TurnManagementMixin,
    MenuManagementMixin,
    ActionVisibilityMixin,
    LobbyActionsMixin,
    EventHandlingMixin,
    ActionSetCreationMixin,
    ActionExecutionMixin,
    OptionsHandlerMixin,
    ActionSetSystemMixin,
):
    """Abstract base class for all games."""
    ...
```

---

## Remaining in base.py (316 lines)

Core infrastructure that must stay in base.py:
- `ActionContext` dataclass (~10 lines)
- `Player` dataclass (~18 lines)
- `Game` class with:
  - Dataclass fields and `__post_init__` (~50 lines)
  - `rebuild_runtime_state()` hook (~12 lines)
  - Abstract/class methods: `get_name`, `get_type`, `get_name_key`, `get_category`, `get_min_players`, `get_max_players`, `get_leaderboard_types` (~56 lines)
  - `prestart_validate()`, `_validate_team_mode()` (~34 lines)
  - `on_start` (abstract), `on_tick`, `on_round_timer_ready` (~16 lines)
  - Player lookup: `attach_user`, `get_user`, `get_player_by_id`, `get_player_by_name` (~28 lines)
  - `team_manager` property (~4 lines)

Current base.py is at **316 lines** - an 86% reduction from the original 2,277 lines.
