"""Base game class and player dataclass."""

from dataclasses import dataclass, field
from typing import Any, Callable
from abc import ABC, abstractmethod
import subprocess
import sys
import json as json_module
from pathlib import Path
import threading

from mashumaro.mixins.json import DataClassJSONMixin
from mashumaro.config import BaseConfig

from ..users.base import User, MenuItem, EscapeBehavior
from ..users.bot import Bot
from ..game_utils.actions import (
    Action,
    ActionSet,
    MenuInput,
    EditboxInput,
    Visibility,
    ResolvedAction,
)
from ..game_utils.options import (
    GameOptions as DeclarativeGameOptions,
    get_option_meta,
    MenuOption,
)
from ..game_utils.game_result import GameResult, PlayerResult
from ..game_utils.stats_helpers import RatingHelper
from ..game_utils.teams import TeamManager
from ..messages.localization import Localization
from ..ui.keybinds import Keybind, KeybindState


@dataclass
class ActionContext:
    """Context passed to action handlers when triggered by keybind."""

    menu_item_id: str | None = None  # ID of selected menu item when keybind pressed
    menu_index: int | None = None  # 1-based index of selected menu item
    from_keybind: bool = (
        False  # True if triggered by keybind, False if by menu selection
    )


# Default bot names available for selection
BOT_NAMES = [
    "Alice",
    "Bob",
    "Charlie",
    "Diana",
    "Eve",
    "Frank",
    "Grace",
    "Henry",
    "Ivy",
    "Jack",
    "Kate",
    "Leo",
    "Mia",
    "Noah",
    "Olivia",
    "Pete",
    "Quinn",
    "Rose",
    "Sam",
    "Tina",
    "Uma",
    "Vic",
    "Wendy",
    "Xander",
    "Yara",
    "Zack",
]


@dataclass
class Player(DataClassJSONMixin):
    """
    A player in a game.

    This is a dataclass that gets serialized with the game state.
    The user field is not serialized - it's reattached on load.
    """

    id: str  # UUID - unique identifier (from user.uuid for humans, generated for bots)
    name: str  # Display name
    is_bot: bool = False
    is_spectator: bool = False
    # Bot AI state (serialized for persistence)
    bot_think_ticks: int = 0  # Ticks until bot can act
    bot_pending_action: str | None = None  # Action to execute when ready
    bot_target: int | None = None  # Game-specific target (e.g., score to reach)


# Re-export GameOptions from options module for backwards compatibility
GameOptions = DeclarativeGameOptions


@dataclass
class Game(ABC, DataClassJSONMixin):
    """
    Abstract base class for all games.

    Games are dataclasses that can be serialized with Mashumaro.
    All game state must be stored in dataclass fields.

    Games are synchronous and state-based. They expose actions that
    players can take, and these actions modify state imperatively.

    Games have three phases:
    - waiting: Lobby phase, host can add bots and start
    - playing: Game in progress
    - finished: Game over
    """

    class Config(BaseConfig):
        # Serialize all fields (don't omit defaults - breaks state restoration)
        serialize_by_alias = True

    # Game state
    players: list[Player] = field(default_factory=list)
    round: int = 0
    game_active: bool = False
    status: str = "waiting"  # waiting, playing, finished
    host: str = ""  # Username of the host
    current_music: str = ""  # Currently playing music track
    current_ambience: str = ""  # Currently playing ambience loop
    turn_index: int = 0  # Current turn index (serialized for persistence)
    turn_direction: int = 1  # Turn direction: 1 = forward, -1 = reverse
    turn_skip_count: int = 0  # Number of players to skip on next advance
    turn_player_ids: list[str] = field(
        default_factory=list
    )  # Player IDs in turn order (serialized)
    # Round timer state (serialized for persistence)
    round_timer_state: str = "idle"  # idle, counting, paused
    round_timer_ticks: int = 0  # Remaining ticks in countdown
    # Sound scheduler state (serialized for persistence)
    scheduled_sounds: list = field(
        default_factory=list
    )  # [[tick, sound, vol, pan, pitch], ...]
    sound_scheduler_tick: int = 0  # Current tick counter
    # Action sets (serialized - actions are pure data now)
    player_action_sets: dict[str, list[ActionSet]] = field(default_factory=dict)
    # Team manager (serialized for persistence)
    _team_manager: TeamManager = field(default_factory=TeamManager)

    def __post_init__(self):
        """Initialize non-serialized state."""
        # These are runtime-only, not serialized
        self._users: dict[str, User] = {}  # player_id -> User
        self._table: Any = None  # Reference to Table (set by server)
        self._keybinds: dict[
            str, list[Keybind]
        ] = {}  # key -> list of Keybinds (allows same key for different states)
        self._pending_actions: dict[
            str, str
        ] = {}  # player_id -> action_id (waiting for input)
        self._action_context: dict[
            str, ActionContext
        ] = {}  # player_id -> context during action execution
        self._status_box_open: set[str] = set()  # player_ids with status box open
        self._actions_menu_open: set[str] = set()  # player_ids with actions menu open
        self._destroyed: bool = False  # Whether game has been destroyed
        # Duration estimation state
        self._estimate_threads: list[threading.Thread] = []  # Running simulation threads
        self._estimate_results: list[int] = []  # Collected tick counts
        self._estimate_errors: list[str] = []  # Collected errors
        self._estimate_running: bool = False  # Whether estimation is in progress
        self._estimate_lock: threading.Lock = threading.Lock()  # Protect results list

    def rebuild_runtime_state(self) -> None:
        """
        Rebuild non-serialized runtime state after deserialization.

        Called after loading a game from JSON. Subclasses should override
        this to rebuild any runtime-only objects not stored in serialized fields.
        Turn management and sound scheduling are now built into the base class
        using serialized fields, so they don't need rebuilding.

        Note: Estimation state is initialized clean by __post_init__.
        """
        pass

    # Abstract methods games must implement

    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        """Return the display name of this game (English fallback)."""
        ...

    @classmethod
    @abstractmethod
    def get_type(cls) -> str:
        """Return the type identifier for this game."""
        ...

    @classmethod
    def get_name_key(cls) -> str:
        """Return the localization key for this game's name."""
        return f"game-name-{cls.get_type()}"

    @classmethod
    def get_category(cls) -> str:
        """Return the category localization key for this game."""
        return "category-uncategorized"

    @classmethod
    def get_min_players(cls) -> int:
        """Return minimum number of players."""
        return 2

    @classmethod
    def get_max_players(cls) -> int:
        """Return maximum number of players."""
        return 4

    @classmethod
    def get_leaderboard_types(cls) -> list[dict]:
        """Return additional leaderboard types this game supports.

        Override in subclasses to add game-specific leaderboards.
        Each dict should have:
        - "id": leaderboard type identifier (e.g., "best_single_turn")
        - "path": dot-separated path to value in custom_data
                  Use {player_id} or {player_name} as placeholders
                  e.g., "player_stats.{player_name}.best_turn"
                  OR for ratio calculations, use:
        - "numerator": path to numerator value
        - "denominator": path to denominator value
                  (values are summed across games, then divided)
        - "aggregate": how to combine values across games
                       "sum", "max", or "avg"
        - "format": entry format key suffix (e.g., "score" for leaderboard-score-entry)
        - "decimals": optional, number of decimal places (default 0)

        The server will look up localization keys like:
        - "leaderboard-type-{id}" for menu display (with underscores as hyphens)
        - "leaderboard-{format}-entry" for each entry
        """
        return []

    @abstractmethod
    def on_start(self) -> None:
        """Called when the game starts."""
        ...

    def on_tick(self) -> None:
        """Called every tick (50ms). Handle bot AI here.

        Subclasses should call super().on_tick() to ensure base functionality runs.
        """
        # Check if duration estimation has completed
        self.check_estimate_completion()

    def on_round_timer_ready(self) -> None:
        """Called when round timer expires. Override in subclasses that use RoundTimer."""
        pass

    def finish_game(self, show_end_screen: bool = True) -> None:
        """Mark the game as finished, persist result, and optionally show end screen.

        Call this instead of setting status directly to ensure proper cleanup.
        If no humans remain, the table is automatically destroyed.

        Args:
            show_end_screen: Whether to show the end screen (default True).
                             Set to False if you want to show it manually.
        """
        self.game_active = False
        self.status = "finished"

        # Build and persist the game result
        result = self.build_game_result()
        self._persist_result(result)

        # Show end screen
        if show_end_screen:
            self._show_end_screen(result)

        # Auto-destroy if no humans remain (bot-only games)
        has_humans = any(not p.is_bot for p in self.players)
        if not has_humans:
            self.destroy()

    def build_game_result(self) -> GameResult:
        """Build the game result. Override in subclasses for custom data.

        Returns:
            A GameResult with game-specific data in custom_data.
        """
        from datetime import datetime

        return GameResult(
            game_type=self.get_type(),
            timestamp=datetime.now().isoformat(),
            duration_ticks=self.sound_scheduler_tick,
            player_results=[
                PlayerResult(
                    player_id=p.id,
                    player_name=p.name,
                    is_bot=p.is_bot,
                )
                for p in self.get_active_players()
            ],
            custom_data={},
        )

    def format_end_screen(self, result: GameResult, locale: str) -> list[str]:
        """Format the end screen lines from a game result. Override for custom display.

        Args:
            result: The game result to format
            locale: The locale to use for localization

        Returns:
            List of lines to display on the end screen
        """
        # Default implementation - just show "Game Over" and player names
        lines = [Localization.get(locale, "game-over")]
        for p in result.player_results:
            lines.append(p.player_name)
        return lines

    def _persist_result(self, result: GameResult) -> None:
        """Persist the game result to the database and update ratings."""
        # Only persist if there are human players
        if not result.has_human_players():
            return

        if self._table:
            self._table.save_game_result(result)
            # Update player ratings
            self._update_ratings(result)

    def _update_ratings(self, result: GameResult) -> None:
        """Update player ratings based on game result."""
        if not self._table or not self._table._db:
            return

        rating_helper = RatingHelper(self._table._db, self.get_type())

        # Get rankings from the result
        rankings = self.get_rankings_for_rating(result)
        if not rankings or len(rankings) < 2:
            # Need at least 2 teams/players to update ratings
            return

        # Update ratings
        rating_helper.update_ratings(rankings)

    def get_rankings_for_rating(self, result: GameResult) -> list[list[str]]:
        """Get player rankings for rating update. Override for custom ranking logic.

        Returns a list of player ID groups ordered by placement.
        First group = 1st place, second = 2nd place, etc.
        Players in same group = tie for that position.

        Default: Winner first, everyone else tied for second.
        """
        winner_name = result.custom_data.get("winner_name")
        human_players = [p for p in result.player_results if not p.is_bot]

        if not human_players:
            return []

        if winner_name:
            winner_id = None
            others = []
            for p in human_players:
                if p.player_name == winner_name:
                    winner_id = p.player_id
                else:
                    others.append(p.player_id)

            if winner_id:
                if others:
                    return [[winner_id], others]
                return [[winner_id]]

        # No clear winner - everyone ties
        return [[p.player_id for p in human_players]]

    def _show_end_screen(self, result: GameResult) -> None:
        """Show the end screen to all players using structured result."""
        for player in self.players:
            user = self.get_user(player)
            if user:
                lines = self.format_end_screen(result, user.locale)
                items = [MenuItem(text=line, id="score_line") for line in lines]
                # Add Leave button at the end
                items.append(MenuItem(
                    text="Congratulations you did great!",
                    id="leave_game"
                ))
                user.show_menu("game_over", items, multiletter=False)

    def show_game_end_menu(self, score_lines: list[str]) -> None:
        """Show the game end menu to all players.

        DEPRECATED: Use finish_game() with build_game_result() and format_end_screen()
        instead. This method is kept for backwards compatibility during migration.

        Args:
            score_lines: List of score lines to display
                         (e.g., ["Final Scores:", "1. Alice: 100 points", ...])
        """
        for player in self.players:
            user = self.get_user(player)
            if user:
                items = [MenuItem(text=line, id="score_line") for line in score_lines]
                user.show_menu("game_over", items, multiletter=False)

    # Player management

    def attach_user(self, player_id: str, user: User) -> None:
        """Attach a user to a player by ID."""
        self._users[player_id] = user
        # Play current music/ambience for the joining user
        if self.current_music:
            user.play_music(self.current_music)
        if self.current_ambience:
            user.play_ambience(self.current_ambience)

    def get_user(self, player: Player) -> User | None:
        """Get the user for a player."""
        return self._users.get(player.id)

    def get_player_by_id(self, player_id: str) -> Player | None:
        """Get a player by ID (UUID)."""
        for player in self.players:
            if player.id == player_id:
                return player
        return None

    def get_player_by_name(self, name: str) -> Player | None:
        """Get a player by display name. Note: Names may not be unique."""
        for player in self.players:
            if player.name == name:
                return player
        return None

    @property
    def current_player(self) -> Player | None:
        """Get the current player based on turn_index and turn_player_ids."""
        if not self.turn_player_ids:
            return None
        index = self.turn_index % len(self.turn_player_ids)
        player_id = self.turn_player_ids[index]
        return self.get_player_by_id(player_id)

    @current_player.setter
    def current_player(self, player: Player | None) -> None:
        """Set the current player by updating turn_index."""
        if player is None or player.id not in self.turn_player_ids:
            return
        self.turn_index = self.turn_player_ids.index(player.id)

    @property
    def team_manager(self) -> TeamManager:
        """Get the team manager for this game."""
        return self._team_manager

    # Action Set System

    def get_action_sets(self, player: Player) -> list[ActionSet]:
        """Get ordered list of action sets for a player."""
        return self.player_action_sets.get(player.id, [])

    def get_action_set(self, player: Player, name: str) -> ActionSet | None:
        """Get a specific action set by name for a player."""
        for action_set in self.get_action_sets(player):
            if action_set.name == name:
                return action_set
        return None

    def add_action_set(self, player: Player, action_set: ActionSet) -> None:
        """Add an action set to a player (appended to end of list)."""
        if player.id not in self.player_action_sets:
            self.player_action_sets[player.id] = []
        self.player_action_sets[player.id].append(action_set)

    def remove_action_set(self, player: Player, name: str) -> None:
        """Remove an action set from a player by name."""
        if player.id in self.player_action_sets:
            self.player_action_sets[player.id] = [
                s for s in self.player_action_sets[player.id] if s.name != name
            ]

    def find_action(self, player: Player, action_id: str) -> Action | None:
        """Find an action by ID across all of a player's action sets."""
        for action_set in self.get_action_sets(player):
            action = action_set.get_action(action_id)
            if action:
                return action
        return None

    def resolve_action(self, player: Player, action: Action) -> ResolvedAction:
        """Resolve a single action's state for a player."""
        # Find the action set containing this action
        for action_set in self.get_action_sets(player):
            if action_set.get_action(action.id):
                return action_set.resolve_action(self, player, action)
        # Fallback - resolve with defaults
        return ResolvedAction(
            action=action,
            label=action.label,
            enabled=True,
            disabled_reason=None,
            visible=True,
        )

    def get_all_visible_actions(self, player: Player) -> list[ResolvedAction]:
        """Get all visible (enabled and not hidden) actions for a player, in order."""
        result = []
        for action_set in self.get_action_sets(player):
            result.extend(action_set.get_visible_actions(self, player))
        return result

    def get_all_enabled_actions(self, player: Player) -> list[ResolvedAction]:
        """Get all enabled actions for a player (for F5 menu), in order."""
        result = []
        for action_set in self.get_action_sets(player):
            result.extend(action_set.get_enabled_actions(self, player))
        return result

    def define_keybind(
        self,
        key: str,
        name: str,
        actions: list[str],
        *,
        requires_focus: bool = False,
        state: KeybindState = KeybindState.ALWAYS,
        players: list[str] | None = None,
        include_spectators: bool = False,
    ) -> None:
        """
        Define a keybind that triggers one or more actions.

        Args:
            key: The key combination (e.g., "space", "shift+b", "f5")
            name: Human-readable name for the keybind (e.g., "Roll dice")
            actions: List of action IDs this keybind triggers
            requires_focus: If True, must be focused on a valid menu item
            state: When the keybind is active (NEVER, IDLE, ACTIVE, ALWAYS)
            players: List of player names who can use (empty/None = all)
            include_spectators: Whether spectators can use this keybind
        """
        keybind = Keybind(
            name=name,
            default_key=key,
            actions=actions,
            requires_focus=requires_focus,
            state=state,
            players=players or [],
            include_spectators=include_spectators,
        )
        if key not in self._keybinds:
            self._keybinds[key] = []
        self._keybinds[key].append(keybind)

    def _get_keybind_for_action(self, action_id: str) -> str | None:
        """Get the keybind string for an action, if any."""
        for key, keybinds in self._keybinds.items():
            for keybind in keybinds:
                if action_id in keybind.actions:
                    return key
        return None

    def _is_player_spectator(self, player: Player) -> bool:
        """Check if a player is a spectator."""
        return player.is_spectator

    def get_active_players(self) -> list[Player]:
        """Get list of players who are not spectators (actually playing)."""
        return [p for p in self.players if not p.is_spectator]

    def get_active_player_count(self) -> int:
        """Get the number of active (non-spectator) players."""
        return len(self.get_active_players())

    def execute_action(
        self,
        player: Player,
        action_id: str,
        input_value: str | None = None,
        context: ActionContext | None = None,
    ) -> None:
        """Execute an action for a player, optionally with input value and context."""
        action = self.find_action(player, action_id)
        if not action:
            return

        # Check if action is enabled using declarative callback
        resolved = self.resolve_action(player, action)
        if not resolved.enabled:
            # Speak the reason to the player
            if resolved.disabled_reason:
                user = self.get_user(player)
                if user:
                    user.speak_l(resolved.disabled_reason)
            return

        # If action requires input and we don't have it yet
        if action.input_request is not None and input_value is None:
            # For bots, get input automatically
            if player.is_bot:
                # Set pending action so options methods can access action_id
                self._pending_actions[player.id] = action_id
                input_value = self._get_bot_input(action, player)
                # Clean up pending action for bot
                if player.id in self._pending_actions:
                    del self._pending_actions[player.id]
                if input_value is None:
                    return  # Bot couldn't provide input
            else:
                # For humans, request input and store pending action
                self._request_action_input(action, player)
                return

        # Look up the handler method by name on this game object
        handler = getattr(self, action.handler, None)
        if not handler:
            return

        # Store context for handlers that need it (e.g., keybind-triggered actions)
        self._action_context[player.id] = context or ActionContext()

        try:
            # Execute the action handler (always pass action_id for context)
            if action.input_request is not None and input_value is not None:
                # Handler expects input value: (player, input_value, action_id)
                handler(player, input_value, action_id)
            else:
                # Handler doesn't expect input: (player, action_id)
                handler(player, action_id)
        finally:
            # Clean up context
            self._action_context.pop(player.id, None)

    def get_action_context(self, player: Player) -> ActionContext:
        """Get the current action context for a player (for use in handlers)."""
        return self._action_context.get(player.id, ActionContext())

    def _get_menu_options_for_action(
        self, action: Action, player: Player
    ) -> list[str] | None:
        """Get menu options for an action, checking method first then MenuOption metadata."""
        req = action.input_request
        if not isinstance(req, MenuInput):
            return None

        # First try the method name
        options_method = getattr(self, req.options, None)
        if options_method:
            return options_method(player)

        # Fallback: check if this is a set_* action for a MenuOption
        if action.id.startswith("set_") and hasattr(self, "options"):
            option_name = action.id[4:]  # Remove "set_" prefix
            meta = get_option_meta(type(self.options), option_name)
            if meta and isinstance(meta, MenuOption):
                choices = meta.choices
                # Choices can be a list or a callable
                if callable(choices):
                    return choices(self, player)
                return list(choices)

        return None

    def _get_bot_input(self, action: Action, player: Player) -> str | None:
        """Get automatic input for a bot player."""
        req = action.input_request
        if isinstance(req, MenuInput):
            options = self._get_menu_options_for_action(action, player)
            if not options:
                return None
            if req.bot_select:
                # Look up bot_select method by name
                bot_select_method = getattr(self, req.bot_select, None)
                if bot_select_method:
                    return bot_select_method(player, options)
            # Default: pick first option
            return options[0]
        elif isinstance(req, EditboxInput):
            if req.bot_input:
                # Look up bot_input method by name
                bot_input_method = getattr(self, req.bot_input, None)
                if bot_input_method:
                    return bot_input_method(player)
            # Default: use default value
            return req.default
        return None

    def _request_action_input(self, action: Action, player: Player) -> None:
        """Request input from a human player for an action."""
        user = self.get_user(player)
        if not user:
            return

        req = action.input_request
        self._pending_actions[player.id] = action.id

        if isinstance(req, MenuInput):
            options = self._get_menu_options_for_action(action, player)
            if not options:
                # No options available
                del self._pending_actions[player.id]
                user.speak_l("no-options-available")
                return

            # Check if this is a MenuOption with localized choice labels
            menu_option_meta = None
            if action.id.startswith("set_") and hasattr(self, "options"):
                option_name = action.id[4:]  # Remove "set_" prefix
                meta = get_option_meta(type(self.options), option_name)
                if meta and isinstance(meta, MenuOption):
                    menu_option_meta = meta

            # Build menu items with localized labels if available
            items = []
            for opt in options:
                if menu_option_meta:
                    display_text = menu_option_meta.get_localized_choice(
                        opt, user.locale
                    )
                else:
                    display_text = opt
                items.append(MenuItem(text=display_text, id=opt))

            items.append(
                MenuItem(text=Localization.get(user.locale, "cancel"), id="_cancel")
            )
            user.show_menu(
                "action_input_menu",
                items,
                multiletter=True,
                escape_behavior=EscapeBehavior.SELECT_LAST,
            )

        elif isinstance(req, EditboxInput):
            # Show editbox for text input
            prompt = Localization.get(user.locale, req.prompt)
            user.show_editbox("action_input_editbox", prompt, req.default)

    def end_turn(self) -> None:
        """End the current player's turn. Call this from action handlers."""
        # Default behavior - can be overridden by games
        self.advance_turn()

    # ==========================================================================
    # Turn Management (built-in, no external manager needed)
    # ==========================================================================

    def set_turn_players(self, players: list[Player], reset_index: bool = True) -> None:
        """Set the list of players in turn order.

        Args:
            players: List of players to include in turn rotation.
            reset_index: If True, reset turn_index to 0.
        """
        self.turn_player_ids = [p.id for p in players]
        if reset_index:
            self.turn_index = 0

    def advance_turn(self, announce: bool = True) -> Player | None:
        """Advance to the next player's turn (respects turn_direction and skips).

        Args:
            announce: If True, announce the turn and play sound.

        Returns:
            The new current player.
        """
        if not self.turn_player_ids:
            return None

        # Handle skips first
        skipped_players: list[Player] = []
        while self.turn_skip_count > 0:
            self.turn_skip_count -= 1
            self.turn_index = (self.turn_index + self.turn_direction) % len(self.turn_player_ids)
            skipped = self.current_player
            if skipped:
                skipped_players.append(skipped)

        # Announce skipped players
        for skipped in skipped_players:
            self.on_player_skipped(skipped)

        # Normal advance
        self.turn_index = (self.turn_index + self.turn_direction) % len(self.turn_player_ids)
        if announce:
            self.announce_turn()
        self.rebuild_all_menus()
        return self.current_player

    def skip_next_players(self, count: int = 1) -> None:
        """Queue players to be skipped on next turn advance.

        Args:
            count: Number of players to skip (default 1).
        """
        self.turn_skip_count += count

    def on_player_skipped(self, player: Player) -> None:
        """Called when a player is skipped. Override to customize announcement.

        Args:
            player: The player who was skipped.
        """
        self.broadcast_l("game-player-skipped", player=player.name)

    def reverse_turn_direction(self) -> None:
        """Reverse the turn direction (forward <-> backward)."""
        self.turn_direction *= -1

    def reset_turn_order(self, announce: bool = False) -> None:
        """Reset to the first player in turn order.

        Args:
            announce: If True, announce the turn and play sound.
        """
        self.turn_index = 0
        self.turn_direction = 1  # Reset direction to forward
        self.turn_skip_count = 0  # Clear any pending skips
        if announce:
            self.announce_turn()

    def announce_turn(self, turn_sound: str = "game_pig/turn.ogg") -> None:
        """Announce the current player's turn with sound and message."""
        player = self.current_player
        if not player:
            return

        # Play turn sound to the current player (if they have it enabled)
        user = self.get_user(player)
        if user and user.preferences.play_turn_sound:
            user.play_sound(turn_sound)

        # Broadcast turn announcement to all players
        self.broadcast_l("game-turn-start", player=player.name)

    @property
    def turn_players(self) -> list[Player]:
        """Get the list of players in turn order."""
        return [
            p
            for player_id in self.turn_player_ids
            if (p := self.get_player_by_id(player_id)) is not None
        ]

    # ==========================================================================
    # Sound Scheduling (built-in, no external scheduler needed)
    # ==========================================================================

    TICKS_PER_SECOND = 20  # 50ms per tick

    def schedule_sound(
        self,
        sound: str,
        delay_ticks: int = 0,
        volume: int = 100,
        pan: int = 0,
        pitch: int = 100,
    ) -> None:
        """Schedule a sound to play after a delay.

        Args:
            sound: Sound file name to play.
            delay_ticks: Number of ticks to wait before playing (0 = next tick).
            volume: Volume (0-100).
            pan: Pan (-100 to 100, 0 = center).
            pitch: Pitch (100 = normal).
        """
        target_tick = self.sound_scheduler_tick + delay_ticks
        self.scheduled_sounds.append([target_tick, sound, volume, pan, pitch])

    def schedule_sound_sequence(
        self,
        sounds: list[tuple[str, int]],
        start_delay: int = 0,
    ) -> None:
        """Schedule a sequence of sounds with delays between them.

        Args:
            sounds: List of (sound_name, delay_after) tuples.
            start_delay: Initial delay before first sound.
        """
        current_tick = start_delay
        for sound, delay_after in sounds:
            self.schedule_sound(sound, delay_ticks=current_tick)
            current_tick += delay_after

    def clear_scheduled_sounds(self) -> None:
        """Clear all scheduled sounds."""
        self.scheduled_sounds.clear()

    def process_scheduled_sounds(self) -> None:
        """Process scheduled sounds. Called automatically in on_tick()."""
        current_tick = self.sound_scheduler_tick

        # Find and play sounds scheduled for this tick
        remaining = []
        for scheduled in self.scheduled_sounds:
            tick, sound, volume, pan, pitch = scheduled
            if tick <= current_tick:
                self.play_sound(sound, volume, pan, pitch)
            else:
                remaining.append(scheduled)

        self.scheduled_sounds = remaining
        self.sound_scheduler_tick += 1

    # Communication helpers

    def broadcast(
        self, text: str, buffer: str = "misc", exclude: Player | None = None
    ) -> None:
        """Send a message to all players, optionally excluding one."""
        for player in self.players:
            if player is exclude:
                continue
            user = self.get_user(player)
            if user:
                user.speak(text, buffer)

    def broadcast_l(
        self,
        message_id: str,
        buffer: str = "misc",
        exclude: Player | None = None,
        **kwargs,
    ) -> None:
        """Send a localized message to all players (each in their own locale)."""
        for player in self.players:
            if player is exclude:
                continue
            user = self.get_user(player)
            if user:
                user.speak_l(message_id, buffer, **kwargs)

    def broadcast_personal_l(
        self,
        player: Player,
        personal_message_id: str,
        others_message_id: str,
        buffer: str = "misc",
        **kwargs,
    ) -> None:
        """
        Send a personalized message to one player and a different message to everyone else.

        The player receives personal_message_id, while all other players receive
        others_message_id with an additional player=player.name argument.

        Args:
            player: The player who gets the personal message.
            personal_message_id: Message ID for the player (e.g., "you-rolled").
            others_message_id: Message ID for everyone else (e.g., "player-rolled").
            buffer: Audio buffer for speech.
            **kwargs: Additional arguments passed to all speak_l calls.
        """
        user = self.get_user(player)
        if user:
            user.speak_l(personal_message_id, buffer, **kwargs)

        for p in self.players:
            if p is player:
                continue
            u = self.get_user(p)
            if u:
                u.speak_l(others_message_id, buffer, player=player.name, **kwargs)

    def label_l(self, message_id: str) -> Callable[["Game", "Player"], str]:
        """
        Create a localized label callable for use in action definitions.

        Usage:
            self.define_action("roll", label=self.label_l("pig-roll"), ...)
        """

        def get_label(game: "Game", player: "Player") -> str:
            user = game.get_user(player)
            locale = user.locale if user else "en"
            return Localization.get(locale, message_id)

        return get_label

    def broadcast_sound(
        self, name: str, volume: int = 100, pan: int = 0, pitch: int = 100
    ) -> None:
        """Play a sound for all players."""
        for player in self.players:
            user = self.get_user(player)
            if user:
                user.play_sound(name, volume, pan, pitch)

    def play_sound(
        self, name: str, volume: int = 100, pan: int = 0, pitch: int = 100
    ) -> None:
        """Alias for broadcast_sound."""
        self.broadcast_sound(name, volume, pan, pitch)

    def play_music(self, name: str, looping: bool = True) -> None:
        """Play music for all players and store as current."""
        self.current_music = name
        for player in self.players:
            user = self.get_user(player)
            if user:
                user.play_music(name, looping)

    def play_ambience(self, loop: str, intro: str = "", outro: str = "") -> None:
        """Play ambient sound for all players."""
        self.current_ambience = loop
        for player in self.players:
            user = self.get_user(player)
            if user:
                user.play_ambience(loop, intro, outro)

    def stop_ambience(self) -> None:
        """Stop ambient sound for all players."""
        self.current_ambience = ""
        for player in self.players:
            user = self.get_user(player)
            if user:
                user.stop_ambience()

    # Menu management

    def rebuild_player_menu(self, player: Player) -> None:
        """Rebuild the turn menu for a player."""
        if self._destroyed:
            return  # Don't rebuild menus after game is destroyed
        if self.status == "finished":
            return  # Don't rebuild turn menu after game has ended
        user = self.get_user(player)
        if not user:
            return

        items: list[MenuItem] = []
        for resolved in self.get_all_visible_actions(player):
            items.append(MenuItem(text=resolved.label, id=resolved.action.id))

        user.show_menu(
            "turn_menu",
            items,
            multiletter=False,
            escape_behavior=EscapeBehavior.KEYBIND,
        )

    def rebuild_all_menus(self) -> None:
        """Rebuild menus for all players."""
        if self._destroyed:
            return  # Don't rebuild menus after game is destroyed
        for player in self.players:
            self.rebuild_player_menu(player)

    def update_player_menu(
        self, player: Player, selection_id: str | None = None
    ) -> None:
        """Update the turn menu for a player, preserving focus position."""
        if self._destroyed:
            return
        if self.status == "finished":
            return
        user = self.get_user(player)
        if not user:
            return

        items: list[MenuItem] = []
        for resolved in self.get_all_visible_actions(player):
            items.append(MenuItem(text=resolved.label, id=resolved.action.id))

        user.update_menu("turn_menu", items, selection_id=selection_id)

    def update_all_menus(self) -> None:
        """Update menus for all players, preserving focus position."""
        if self._destroyed:
            return
        for player in self.players:
            self.update_player_menu(player)

    def status_box(self, player: Player, lines: list[str]) -> None:
        """Show a status box (menu with text items) to a player.

        Press Enter on any item to close. No header or close button needed
        since screen readers speak list items and Enter always closes.
        """
        user = self.get_user(player)
        if user:
            items = [MenuItem(text=line, id="status_line") for line in lines]
            user.show_menu(
                "status_box",
                items,
                multiletter=False,
                escape_behavior=EscapeBehavior.SELECT_LAST,
            )
            self._status_box_open.add(player.id)

    # Event handling

    def handle_event(self, player: Player, event: dict) -> None:
        """Handle an event from a player."""
        event_type = event.get("type")

        if event_type == "menu":
            menu_id = event.get("menu_id")
            selection_id = event.get("selection_id", "")

            if menu_id == "turn_menu":
                # If interacting with turn_menu, actions menu is no longer open
                self._actions_menu_open.discard(player.id)
                # Try by ID first, then by index
                action = (
                    self.find_action(player, selection_id) if selection_id else None
                )
                if action:
                    resolved = self.resolve_action(player, action)
                    if resolved.enabled:
                        self.execute_action(player, selection_id)
                        # Don't rebuild if action is waiting for input
                        if player.id not in self._pending_actions:
                            self.rebuild_all_menus()
                else:
                    # Fallback to index-based selection - use visible actions only
                    selection = event.get("selection", 1) - 1  # Convert to 0-based
                    visible = self.get_all_visible_actions(player)
                    if 0 <= selection < len(visible):
                        resolved = visible[selection]
                        self.execute_action(player, resolved.action.id)
                        # Don't rebuild if action is waiting for input
                        if player.id not in self._pending_actions:
                            self.rebuild_all_menus()

            elif menu_id == "actions_menu":
                # F5 menu - use selection_id directly
                if selection_id:
                    self._handle_actions_menu_selection(player, selection_id)

            elif menu_id == "status_box":
                user = self.get_user(player)
                if user:
                    user.remove_menu("status_box")
                    user.speak_l("status-box-closed")
                    self._status_box_open.discard(player.id)
                    self.rebuild_player_menu(player)

            elif menu_id == "game_over":
                # Handle game over menu - leave_game is the only selectable action
                # It's always the last item
                if selection_id == "leave_game":
                    self.execute_action(player, "leave_game")
                else:
                    # Index-based - any selection triggers leave
                    self.execute_action(player, "leave_game")

            elif menu_id == "action_input_menu":
                # Handle action input menu selection
                if player.id in self._pending_actions:
                    action_id = self._pending_actions.pop(player.id)
                    if selection_id != "_cancel":
                        # Execute the action with the selected input
                        self.execute_action(player, action_id, selection_id)
                self.rebuild_player_menu(player)

        elif event_type == "editbox":
            input_id = event.get("input_id", "")
            text = event.get("text", "")

            if input_id == "action_input_editbox":
                # Handle action input editbox submission
                if player.id in self._pending_actions:
                    action_id = self._pending_actions.pop(player.id)
                    if text:  # Non-empty input
                        self.execute_action(player, action_id, text)
                self.rebuild_player_menu(player)

        elif event_type == "keybind":
            key = event.get("key", "").lower()  # Normalize to lowercase
            menu_item_id = event.get("menu_item_id")
            menu_index = event.get("menu_index")

            # Handle modifiers - reconstruct full key string
            if event.get("shift") and not key.startswith("shift+"):
                key = f"shift+{key}"
            if event.get("control") and not key.startswith("ctrl+"):
                key = f"ctrl+{key}"
            if event.get("alt") and not key.startswith("alt+"):
                key = f"alt+{key}"

            # Look up keybinds for this key
            keybinds = self._keybinds.get(key)
            if keybinds is None:
                return

            # Check if player is a spectator
            is_spectator = self._is_player_spectator(player)

            # Build context for action handlers
            context = ActionContext(
                menu_item_id=menu_item_id,
                menu_index=menu_index,
                from_keybind=True,
            )

            # Try each keybind for this key (allows same key for different states)
            executed_any = False
            for keybind in keybinds:
                # Check if keybind can be used by this player in current state
                if not keybind.can_player_use(self, player, is_spectator):
                    continue

                # Check focus requirement
                if keybind.requires_focus and menu_item_id not in keybind.actions:
                    continue

                # Execute all enabled actions in the keybind
                for action_id in keybind.actions:
                    action = self.find_action(player, action_id)
                    if action:
                        resolved = self.resolve_action(player, action)
                        if resolved.enabled:
                            self.execute_action(player, action_id, context=context)
                            executed_any = True
                        elif resolved.disabled_reason:
                            # Speak the disabled reason to the player
                            user = self.get_user(player)
                            if user:
                                user.speak_l(resolved.disabled_reason)

            # Don't rebuild if action is waiting for input, status box is open, or actions menu is open
            if (
                executed_any
                and player.id not in self._pending_actions
                and player.id not in self._status_box_open
                and player.id not in self._actions_menu_open
            ):
                self.rebuild_all_menus()

    def _handle_actions_menu_selection(self, player: Player, action_id: str) -> None:
        """Handle selection from the F5 actions menu."""
        # Actions menu is no longer open
        self._actions_menu_open.discard(player.id)
        # Handle "go back" - just return to turn menu
        if action_id == "go_back":
            self.rebuild_player_menu(player)
            return
        action = self.find_action(player, action_id)
        if action:
            resolved = self.resolve_action(player, action)
            if resolved.enabled:
                self.execute_action(player, action_id)
        # Don't rebuild if action is waiting for input
        if player.id not in self._pending_actions:
            self.rebuild_player_menu(player)

    # Lobby system

    def destroy(self) -> None:
        """Request destruction of this game/table."""
        self._destroyed = True
        if self._table:
            self._table.destroy()

    # ==========================================================================
    # Declarative is_enabled / is_hidden / get_label methods for base actions
    # ==========================================================================

    # --- Lobby actions ---

    def _is_start_game_enabled(self, player: Player) -> str | None:
        """Check if start_game action is enabled."""
        if self.status != "waiting":
            return "action-game-in-progress"
        if player.name != self.host:
            return "action-not-host"
        active_count = self.get_active_player_count()
        if active_count < self.get_min_players():
            return "action-need-more-players"
        return None

    def _is_start_game_hidden(self, player: Player) -> Visibility:
        """Check if start_game action is hidden."""
        if self.status != "waiting":
            return Visibility.HIDDEN
        return Visibility.VISIBLE

    def _is_add_bot_enabled(self, player: Player) -> str | None:
        """Check if add_bot action is enabled."""
        if self.status != "waiting":
            return "action-game-in-progress"
        if player.name != self.host:
            return "action-not-host"
        if len(self.players) >= self.get_max_players():
            return "action-table-full"
        return None

    def _is_add_bot_hidden(self, player: Player) -> Visibility:
        """Add bot is always hidden (F5/keybind only)."""
        return Visibility.HIDDEN

    def _is_remove_bot_enabled(self, player: Player) -> str | None:
        """Check if remove_bot action is enabled."""
        if self.status != "waiting":
            return "action-game-in-progress"
        if player.name != self.host:
            return "action-not-host"
        if not any(p.is_bot for p in self.players):
            return "action-no-bots"
        return None

    def _is_remove_bot_hidden(self, player: Player) -> Visibility:
        """Remove bot is always hidden (F5/keybind only)."""
        return Visibility.HIDDEN

    def _is_toggle_spectator_enabled(self, player: Player) -> str | None:
        """Check if toggle_spectator action is enabled."""
        if self.status != "waiting":
            return "action-game-in-progress"
        if player.is_bot:
            return "action-bots-cannot"
        return None

    def _is_toggle_spectator_hidden(self, player: Player) -> Visibility:
        """Toggle spectator is always hidden (F5/keybind only)."""
        return Visibility.HIDDEN

    def _get_toggle_spectator_label(self, player: Player) -> str:
        """Get dynamic label for toggle_spectator action."""
        user = self.get_user(player)
        locale = user.locale if user else "en"
        if player.is_spectator:
            return Localization.get(locale, "play")
        return Localization.get(locale, "spectate")

    def _is_leave_game_enabled(self, player: Player) -> str | None:
        """Leave game is always enabled."""
        return None

    def _is_leave_game_hidden(self, player: Player) -> Visibility:
        """Leave game is always hidden (F5/keybind only)."""
        return Visibility.HIDDEN

    # --- Option actions ---

    def _is_option_enabled(self, player: Player) -> str | None:
        """Check if option actions are enabled (waiting state, host only)."""
        if self.status != "waiting":
            return "action-game-in-progress"
        if player.name != self.host:
            return "action-not-host"
        return None

    def _is_option_hidden(self, player: Player) -> Visibility:
        """Options are visible in waiting state only."""
        if self.status != "waiting":
            return Visibility.HIDDEN
        return Visibility.VISIBLE

    # --- Estimate actions ---

    def _is_estimate_duration_enabled(self, player: Player) -> str | None:
        """Check if estimate_duration action is enabled."""
        if self.status != "waiting":
            return "action-game-in-progress"
        return None

    def _is_estimate_duration_hidden(self, player: Player) -> Visibility:
        """Estimate duration is visible in waiting state."""
        if self.status != "waiting":
            return Visibility.HIDDEN
        return Visibility.VISIBLE

    # --- Standard actions ---

    def _is_show_actions_enabled(self, player: Player) -> str | None:
        """Show actions menu is always enabled."""
        return None

    def _is_show_actions_hidden(self, player: Player) -> Visibility:
        """Show actions is always hidden (keybind only)."""
        return Visibility.HIDDEN

    def _is_save_table_enabled(self, player: Player) -> str | None:
        """Check if save_table action is enabled."""
        if player.name != self.host:
            return "action-not-host"
        return None

    def _is_save_table_hidden(self, player: Player) -> Visibility:
        """Save table is always hidden (keybind only)."""
        return Visibility.HIDDEN

    def _is_whose_turn_enabled(self, player: Player) -> str | None:
        """Check if whose_turn action is enabled."""
        if self.status != "playing":
            return "action-not-playing"
        return None

    def _is_whose_turn_hidden(self, player: Player) -> Visibility:
        """Whose turn is always hidden (keybind only)."""
        return Visibility.HIDDEN

    def _is_check_scores_enabled(self, player: Player) -> str | None:
        """Check if check_scores action is enabled."""
        if self.status != "playing":
            return "action-not-playing"
        if len(self.team_manager.teams) == 0:
            return "action-no-scores"
        return None

    def _is_check_scores_hidden(self, player: Player) -> Visibility:
        """Check scores is always hidden (keybind only)."""
        return Visibility.HIDDEN

    def _is_check_scores_detailed_enabled(self, player: Player) -> str | None:
        """Check if check_scores_detailed action is enabled."""
        if self.status != "playing":
            return "action-not-playing"
        if len(self.team_manager.teams) == 0:
            return "action-no-scores"
        return None

    def _is_check_scores_detailed_hidden(self, player: Player) -> Visibility:
        """Check scores detailed is always hidden (keybind only)."""
        return Visibility.HIDDEN

    def _is_predict_outcomes_enabled(self, player: Player) -> str | None:
        """Check if predict_outcomes action is enabled."""
        if self.status != "playing":
            return "action-not-playing"
        # Need at least 2 human players for meaningful predictions
        human_count = sum(1 for p in self.players if not p.is_bot and not p.is_spectator)
        if human_count < 2:
            return "action-need-more-humans"
        return None

    def _is_predict_outcomes_hidden(self, player: Player) -> Visibility:
        """Predict outcomes is always hidden (keybind only)."""
        return Visibility.HIDDEN

    # ==========================================================================
    # Action set creation
    # ==========================================================================

    def create_lobby_action_set(self, player: Player) -> ActionSet:
        """Create the lobby action set for a player."""
        user = self.get_user(player)
        locale = user.locale if user else "en"

        action_set = ActionSet(name="lobby")
        action_set.add(
            Action(
                id="start_game",
                label=Localization.get(locale, "start-game"),
                handler="_action_start_game",
                is_enabled="_is_start_game_enabled",
                is_hidden="_is_start_game_hidden",
            )
        )
        action_set.add(
            Action(
                id="add_bot",
                label=Localization.get(locale, "add-bot"),
                handler="_action_add_bot",
                is_enabled="_is_add_bot_enabled",
                is_hidden="_is_add_bot_hidden",
                input_request=EditboxInput(
                    prompt="enter-bot-name",
                    default="",
                    bot_input="_bot_input_add_bot",
                ),
            )
        )
        action_set.add(
            Action(
                id="remove_bot",
                label=Localization.get(locale, "remove-bot"),
                handler="_action_remove_bot",
                is_enabled="_is_remove_bot_enabled",
                is_hidden="_is_remove_bot_hidden",
            )
        )
        action_set.add(
            Action(
                id="toggle_spectator",
                label=Localization.get(locale, "spectate"),
                handler="_action_toggle_spectator",
                is_enabled="_is_toggle_spectator_enabled",
                is_hidden="_is_toggle_spectator_hidden",
                get_label="_get_toggle_spectator_label",
            )
        )
        action_set.add(
            Action(
                id="leave_game",
                label=Localization.get(locale, "leave-table"),
                handler="_action_leave_game",
                is_enabled="_is_leave_game_enabled",
                is_hidden="_is_leave_game_hidden",
            )
        )
        return action_set

    def create_estimate_action_set(self, player: Player) -> ActionSet:
        """Create the estimate duration action set for a player."""
        user = self.get_user(player)
        locale = user.locale if user else "en"

        action_set = ActionSet(name="estimate")
        action_set.add(
            Action(
                id="estimate_duration",
                label=Localization.get(locale, "estimate-duration"),
                handler="_action_estimate_duration",
                is_enabled="_is_estimate_duration_enabled",
                is_hidden="_is_estimate_duration_hidden",
            )
        )
        return action_set

    def create_standard_action_set(self, player: Player) -> ActionSet:
        """Create the standard action set (F5, save) for a player."""
        user = self.get_user(player)
        locale = user.locale if user else "en"

        action_set = ActionSet(name="standard")
        action_set.add(
            Action(
                id="show_actions",
                label=Localization.get(locale, "actions-menu"),
                handler="_action_show_actions_menu",
                is_enabled="_is_show_actions_enabled",
                is_hidden="_is_show_actions_hidden",
            )
        )
        action_set.add(
            Action(
                id="save_table",
                label=Localization.get(locale, "save-table"),
                handler="_action_save_table",
                is_enabled="_is_save_table_enabled",
                is_hidden="_is_save_table_hidden",
            )
        )

        # Common status actions (available during play)
        action_set.add(
            Action(
                id="whose_turn",
                label=Localization.get(locale, "whose-turn"),
                handler="_action_whose_turn",
                is_enabled="_is_whose_turn_enabled",
                is_hidden="_is_whose_turn_hidden",
            )
        )
        action_set.add(
            Action(
                id="check_scores",
                label=Localization.get(locale, "check-scores"),
                handler="_action_check_scores",
                is_enabled="_is_check_scores_enabled",
                is_hidden="_is_check_scores_hidden",
            )
        )
        action_set.add(
            Action(
                id="check_scores_detailed",
                label=Localization.get(locale, "check-scores-detailed"),
                handler="_action_check_scores_detailed",
                is_enabled="_is_check_scores_detailed_enabled",
                is_hidden="_is_check_scores_detailed_hidden",
            )
        )
        action_set.add(
            Action(
                id="predict_outcomes",
                label=Localization.get(locale, "predict-outcomes"),
                handler="_action_predict_outcomes",
                is_enabled="_is_predict_outcomes_enabled",
                is_hidden="_is_predict_outcomes_hidden",
            )
        )

        return action_set

    def setup_keybinds(self) -> None:
        """Define all keybinds for the game."""
        # Lobby keybinds
        self.define_keybind(
            "enter", "Start game", ["start_game"], state=KeybindState.IDLE
        )
        self.define_keybind("b", "Add bot", ["add_bot"], state=KeybindState.IDLE)
        self.define_keybind(
            "shift+b", "Remove bot", ["remove_bot"], state=KeybindState.IDLE
        )
        self.define_keybind(
            "f3",
            "Toggle spectator",
            ["toggle_spectator"],
            state=KeybindState.IDLE,
            include_spectators=True,
        )
        self.define_keybind(
            "q",
            "Leave table",
            ["leave_game"],
            state=KeybindState.ALWAYS,
            include_spectators=True,
        )
        # Standard keybinds
        self.define_keybind(
            "escape",
            "Actions menu",
            ["show_actions"],
            state=KeybindState.ALWAYS,
            include_spectators=True,
        )
        self.define_keybind(
            "ctrl+s", "Save table", ["save_table"], state=KeybindState.ALWAYS
        )

        # Status keybinds (during play)
        self.define_keybind(
            "t",
            "Whose turn",
            ["whose_turn"],
            state=KeybindState.ACTIVE,
            include_spectators=True,
        )
        self.define_keybind(
            "s",
            "Check scores",
            ["check_scores"],
            state=KeybindState.ACTIVE,
            include_spectators=True,
        )
        self.define_keybind(
            "shift+s",
            "Detailed scores",
            ["check_scores_detailed"],
            state=KeybindState.ACTIVE,
            include_spectators=True,
        )
        self.define_keybind(
            "ctrl+r",
            "Predict outcomes",
            ["predict_outcomes"],
            state=KeybindState.ACTIVE,
            include_spectators=True,
        )

    def create_turn_action_set(self, player: Player) -> ActionSet | None:
        """Create the turn action set for a player.

        Override in subclasses to add game-specific turn actions.
        Returns None by default (no turn actions).
        """
        return None

    def setup_player_actions(self, player: Player) -> None:
        """Set up action sets for a player. Called when player joins."""
        # Create and add action sets in order (first = appears first in menu)
        # Turn actions first (if any), then lobby, options, standard
        turn_set = self.create_turn_action_set(player)
        if turn_set:
            self.add_action_set(player, turn_set)

        lobby_set = self.create_lobby_action_set(player)
        self.add_action_set(player, lobby_set)

        # Only add options if the game defines them
        if hasattr(self, "options"):
            options_set = self.create_options_action_set(player)
            self.add_action_set(player, options_set)

        # Add estimate action set (after options)
        estimate_set = self.create_estimate_action_set(player)
        self.add_action_set(player, estimate_set)

        standard_set = self.create_standard_action_set(player)
        self.add_action_set(player, standard_set)

    # Lobby action handlers

    def _action_start_game(self, player: Player, action_id: str) -> None:
        """Start the game."""
        self.status = "playing"
        self.broadcast_l("game-starting")
        self.on_start()

    def _bot_input_add_bot(self, player: Player) -> str | None:
        """Get bot name for add_bot action."""
        return next(
            (
                n
                for n in BOT_NAMES
                if n.lower() not in {x.name.lower() for x in self.players}
            ),
            None,
        )

    def _action_add_bot(self, player: Player, bot_name: str, action_id: str) -> None:
        """Add a bot with the selected name."""
        # If blank, use an available name from the list
        if not bot_name.strip():
            bot_name = next(
                (
                    n
                    for n in BOT_NAMES
                    if n.lower() not in {x.name.lower() for x in self.players}
                ),
                None,
            )
            if not bot_name:
                # No names available
                user = self.get_user(player)
                if user:
                    user.speak_l("no-bot-names-available")
                return

        bot_user = Bot(bot_name)
        bot_player = self.create_player(bot_user.uuid, bot_name, is_bot=True)
        self.players.append(bot_player)
        self.attach_user(bot_player.id, bot_user)
        # Set up action sets for the bot
        self.setup_player_actions(bot_player)
        self.broadcast_l("table-joined", player=bot_name)
        self.rebuild_all_menus()

    def _action_remove_bot(self, player: Player, action_id: str) -> None:
        """Remove the last bot from the game."""
        for i in range(len(self.players) - 1, -1, -1):
            if self.players[i].is_bot:
                bot = self.players.pop(i)
                # Clean up action sets
                self.player_action_sets.pop(bot.id, None)
                self._users.pop(bot.id, None)
                self.broadcast_l("table-left", player=bot.name)
                break
        self.rebuild_all_menus()

    def _action_toggle_spectator(self, player: Player, action_id: str) -> None:
        """Toggle spectator mode for a player."""
        if self.status != "waiting":
            return  # Can only toggle before game starts

        player.is_spectator = not player.is_spectator
        if player.is_spectator:
            self.broadcast_l("now-spectating", player=player.name)
        else:
            self.broadcast_l("now-playing", player=player.name)

        self.rebuild_all_menus()

    def _action_leave_game(self, player: Player, action_id: str) -> None:
        """Leave the game."""
        from ..users.bot import Bot

        if self.status == "playing" and not player.is_bot:
            # Mid-game: replace human with bot instead of removing
            # Keep the same player ID so they can rejoin and take over
            player.is_bot = True
            self._users.pop(player.id, None)

            # Create a bot user with the same UUID to control this player
            bot_user = Bot(player.name, uuid=player.id)
            self.attach_user(player.id, bot_user)

            self.broadcast_l("player-replaced-by-bot", player=player.name)

            # Check if any humans remain
            has_humans = any(not p.is_bot for p in self.players)
            if not has_humans:
                # Destroy the game - no humans left
                self.destroy()
                return

            # Rebuild menus for remaining players
            self.rebuild_all_menus()
            return

        # Lobby or bot leaving: fully remove the player
        self.players = [p for p in self.players if p.id != player.id]
        self.player_action_sets.pop(player.id, None)
        self._users.pop(player.id, None)

        self.broadcast_l("table-left", player=player.name)

        # Check if any humans remain
        has_humans = any(not p.is_bot for p in self.players)
        if not has_humans:
            # Destroy the game - no humans left
            self.destroy()
            return

        if self.status == "waiting":
            # If host left, assign new host
            if player.name == self.host and self.players:
                # Find first human to be new host
                for p in self.players:
                    if not p.is_bot:
                        self.host = p.name
                        self.broadcast_l("new-host", player=p.name)
                        break

            self.rebuild_all_menus()

    # F5 Actions Menu

    def _action_show_actions_menu(self, player: Player, action_id: str) -> None:
        """Show the F5 actions menu."""
        items = []
        for resolved in self.get_all_enabled_actions(player):
            label = resolved.label
            keybind_key = self._get_keybind_for_action(resolved.action.id)
            if keybind_key:
                label += f" ({keybind_key.upper()})"
            items.append(MenuItem(text=label, id=resolved.action.id))

        user = self.get_user(player)
        if user and items:
            # Add "Go back" option at the end
            items.append(
                MenuItem(text=Localization.get(user.locale, "go-back"), id="go_back")
            )
            self._actions_menu_open.add(player.id)
            user.speak_l("context-menu")
            user.show_menu(
                "actions_menu",
                items,
                multiletter=True,
                escape_behavior=EscapeBehavior.SELECT_LAST,
            )
        elif user:
            user.speak_l("no-actions-available")

    def _action_save_table(self, player: Player, action_id: str) -> None:
        """Save the current table state (host only). This destroys the table."""
        if self._table:
            self._table.save_and_close(player.name)

    def _action_whose_turn(self, player: Player, action_id: str) -> None:
        """Announce whose turn it is."""
        user = self.get_user(player)
        if user:
            current = self.current_player
            if current:
                user.speak_l("game-turn-start", player=current.name)
            else:
                user.speak_l("game-no-turn")

    def _action_check_scores(self, player: Player, action_id: str) -> None:
        """Announce scores briefly."""
        user = self.get_user(player)
        if not user:
            return

        if self.team_manager.teams:
            user.speak(self.team_manager.format_scores_brief(user.locale))
        else:
            user.speak_l("no-scores-available")

    def _action_check_scores_detailed(self, player: Player, action_id: str) -> None:
        """Show detailed scores in a status box."""
        user = self.get_user(player)
        if not user:
            return

        if self.team_manager.teams:
            lines = self.team_manager.format_scores_detailed(user.locale)
            self.status_box(player, lines)
        else:
            self.status_box(player, ["No scores available."])

    def _action_predict_outcomes(self, player: Player, action_id: str) -> None:
        """Show predicted outcomes based on player ratings."""
        user = self.get_user(player)
        if not user:
            return

        if not self._table or not self._table._db:
            user.speak_l("predict-unavailable")
            return

        rating_helper = RatingHelper(self._table._db, self.get_type())

        # Get human players only (exclude spectators)
        human_players = [
            p for p in self.players if not p.is_bot and not p.is_spectator
        ]

        if len(human_players) < 2:
            user.speak_l("predict-need-players")
            return

        # Get ratings for all players
        player_ratings = []
        for p in human_players:
            rating = rating_helper.get_rating(p.id)
            player_ratings.append((p, rating))

        # Sort by ordinal (conservative skill estimate) descending
        player_ratings.sort(key=lambda x: x[1].ordinal, reverse=True)

        # Format predictions
        lines = [Localization.get(user.locale, "predict-header")]

        for rank, (p, rating) in enumerate(player_ratings, 1):
            # Calculate win probability against the field
            if len(player_ratings) == 2:
                # 2 players: show head-to-head probability
                other = player_ratings[1] if rank == 1 else player_ratings[0]
                win_prob = rating_helper.predict_win_probability(p.id, other[0].id)
                lines.append(
                    Localization.get(
                        user.locale,
                        "predict-entry-2p",
                        rank=rank,
                        player=p.name,
                        rating=round(rating.ordinal),
                        probability=round(win_prob * 100),
                    )
                )
            else:
                # 3+ players: show rating only (probabilities get complex)
                lines.append(
                    Localization.get(
                        user.locale,
                        "predict-entry",
                        rank=rank,
                        player=p.name,
                        rating=round(rating.ordinal),
                    )
                )

        self.status_box(player, lines)

    # Player helpers

    def get_human_count(self) -> int:
        """Get the number of human players."""
        return sum(1 for p in self.players if not p.is_bot)

    def get_bot_count(self) -> int:
        """Get the number of bot players."""
        return sum(1 for p in self.players if p.is_bot)

    def create_player(self, player_id: str, name: str, is_bot: bool = False) -> Player:
        """Create a new player. Override in subclasses for custom player types."""
        return Player(id=player_id, name=name, is_bot=is_bot)

    def add_player(self, name: str, user: User) -> Player:
        """Add a player to the game."""
        is_bot = hasattr(user, "is_bot") and user.is_bot
        player = self.create_player(user.uuid, name, is_bot=is_bot)
        self.players.append(player)
        self.attach_user(player.id, user)
        # Set up action sets for the new player
        self.setup_player_actions(player)
        return player

    def initialize_lobby(self, host_name: str, host_user: User) -> None:
        """Initialize the game in lobby mode with a host."""
        self.host = host_name
        self.status = "waiting"
        self.setup_keybinds()
        self.add_player(host_name, host_user)
        self.rebuild_all_menus()

    # Declarative options system support

    def create_options_action_set(self, player: Player) -> ActionSet:
        """Create the options action set for a player.

        If the game's options class uses declarative options (option_field),
        this will auto-generate the action set. Otherwise, subclasses should
        override this method.
        """
        if hasattr(self.options, "create_options_action_set"):
            return self.options.create_options_action_set(self, player)
        # Fallback for non-declarative options
        return ActionSet(name="options")

    def _handle_option_change(self, option_name: str, value: str) -> None:
        """Handle a declarative option change (for int/menu options).

        This is called by auto-generated option actions.
        No broadcast needed - screen readers speak the updated list item.
        """
        meta = get_option_meta(type(self.options), option_name)
        if not meta:
            return

        success, converted = meta.validate_and_convert(value)
        if not success:
            return

        # Set the option value
        setattr(self.options, option_name, converted)

        # Update labels and rebuild menus
        if hasattr(self.options, "update_options_labels"):
            self.options.update_options_labels(self)
        self.rebuild_all_menus()

    def _handle_option_toggle(self, option_name: str) -> None:
        """Handle a declarative boolean option toggle.

        This is called by auto-generated toggle actions.
        No broadcast needed - screen readers speak the updated list item.
        """
        meta = get_option_meta(type(self.options), option_name)
        if not meta:
            return

        # Toggle the value
        current = getattr(self.options, option_name)
        new_value = not current
        setattr(self.options, option_name, new_value)

        # Update labels and rebuild menus
        if hasattr(self.options, "update_options_labels"):
            self.options.update_options_labels(self)
        self.rebuild_all_menus()

    # Generic option action handlers (extract option_name from action_id)

    def _action_set_option(self, player: Player, value: str, action_id: str) -> None:
        """Generic handler for setting an option value.

        Extracts the option name from action_id (e.g., "set_total_rounds" -> "total_rounds")
        and delegates to _handle_option_change.
        """
        option_name = action_id.removeprefix("set_")
        self._handle_option_change(option_name, value)

    def _action_toggle_option(self, player: Player, action_id: str) -> None:
        """Generic handler for toggling a boolean option.

        Extracts the option name from action_id (e.g., "toggle_show_hints" -> "show_hints")
        and delegates to _handle_option_toggle.
        """
        option_name = action_id.removeprefix("toggle_")
        self._handle_option_toggle(option_name)

    # ==========================================================================
    # Duration Estimation
    # ==========================================================================

    NUM_ESTIMATE_SIMULATIONS = 10  # Number of simulations to run for estimation
    HUMAN_SPEED_MULTIPLIER = 2  # How much slower humans are than bots (override per game)

    def _action_estimate_duration(self, player: Player, action_id: str) -> None:
        """Start duration estimation by spawning CLI simulation threads."""
        if self._estimate_running:
            user = self.get_user(player)
            if user:
                user.speak_l("estimate-already-running")
            return

        # Build the options string for CLI
        options_args = []
        if hasattr(self, "options"):
            for field_name in self.options.__dataclass_fields__:
                value = getattr(self.options, field_name)
                options_args.extend(["-o", f"{field_name}={value}"])

        # Determine number of bots (use current player count, minimum 2)
        num_bots = max(len([p for p in self.players if not p.is_spectator]), self.get_min_players())

        # Build CLI command
        cli_path = Path(__file__).parent.parent / "cli.py"
        base_cmd = [
            sys.executable, str(cli_path), "simulate",
            self.get_type(),
            "--bots", str(num_bots),
            "--json", "--quiet"
        ] + options_args

        # Reset results
        self._estimate_results = []
        self._estimate_errors = []
        self._estimate_threads = []

        # Spawn simulation threads
        def run_simulation():
            try:
                result = subprocess.run(
                    base_cmd,
                    capture_output=True,
                    text=True,
                    timeout=600,  # 10 minute timeout per simulation
                )
                if result.returncode == 0 and result.stdout:
                    data = json_module.loads(result.stdout)
                    if "ticks" in data and not data.get("timed_out", False):
                        with self._estimate_lock:
                            self._estimate_results.append(data["ticks"])
                elif result.stderr:
                    with self._estimate_lock:
                        self._estimate_errors.append(result.stderr.strip()[:200])
            except Exception as e:
                with self._estimate_lock:
                    self._estimate_errors.append(str(e)[:200])

        for _ in range(self.NUM_ESTIMATE_SIMULATIONS):
            thread = threading.Thread(target=run_simulation, daemon=True)
            thread.start()
            self._estimate_threads.append(thread)

        if self._estimate_threads:
            self._estimate_running = True
            self.broadcast_l("estimate-computing")
        else:
            self.broadcast_l("estimate-error")

    def check_estimate_completion(self) -> None:
        """Check if duration estimation simulations have completed.

        Called automatically from on_tick().
        """
        if not self._estimate_running or not self._estimate_threads:
            return

        # Check if all threads have completed
        all_done = all(not t.is_alive() for t in self._estimate_threads)
        if not all_done:
            return

        # Get results (already collected by threads)
        with self._estimate_lock:
            tick_counts = list(self._estimate_results)
            errors = list(self._estimate_errors)

        # Clean up
        self._estimate_threads = []
        self._estimate_results = []
        self._estimate_errors = []
        self._estimate_running = False

        # Calculate and announce result
        if tick_counts:
            # Calculate statistics
            avg_ticks = sum(tick_counts) / len(tick_counts)
            std_dev_ticks = self._calculate_std_dev(tick_counts, avg_ticks)
            outliers = self._detect_outliers(tick_counts)

            # Format times
            bot_time = self._format_duration(avg_ticks)
            std_dev = self._format_duration(std_dev_ticks)
            human_time = self._format_duration(avg_ticks * self.HUMAN_SPEED_MULTIPLIER)

            # Format outlier info
            if outliers:
                outlier_info = f"{len(outliers)} outlier{'s' if len(outliers) > 1 else ''} removed. "
            else:
                outlier_info = ""

            self.broadcast_l(
                "estimate-result",
                bot_time=bot_time,
                std_dev=std_dev,
                outlier_info=outlier_info,
                human_time=human_time,
            )
        else:
            if errors:
                # Show the first error for debugging
                self.broadcast(f"Estimation failed: {errors[0][:200]}")
            else:
                self.broadcast_l("estimate-error")

    def _calculate_std_dev(self, values: list[int], mean: float) -> float:
        """Calculate standard deviation of a list of values."""
        if len(values) < 2:
            return 0.0
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return variance ** 0.5

    def _detect_outliers(self, values: list[int]) -> list[int]:
        """Detect outliers using IQR method. Returns list of outlier values."""
        if len(values) < 4:
            return []

        sorted_vals = sorted(values)
        n = len(sorted_vals)
        q1 = sorted_vals[n // 4]
        q3 = sorted_vals[(3 * n) // 4]
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        return [v for v in values if v < lower_bound or v > upper_bound]

    def _format_duration(self, ticks: float) -> str:
        """Format a tick count as a human-readable duration string.

        Args:
            ticks: Number of game ticks (50ms each).

        Returns:
            Formatted string like "1:23:45" or "5:30" or "45 seconds".
        """
        # Convert ticks to seconds (50ms per tick = 20 ticks per second)
        total_seconds = int(ticks / self.TICKS_PER_SECOND)

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        if hours > 0:
            return f"{hours}:{minutes:02d}:{seconds:02d}"
        elif minutes > 0:
            return f"{minutes}:{seconds:02d}"
        else:
            return f"{seconds} seconds"
