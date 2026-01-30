"""Virtual bot management for simulating users on the server."""

import random
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .server import Server


class VirtualBotState(Enum):
    """State machine for virtual bots."""

    OFFLINE = "offline"
    ONLINE_IDLE = "online_idle"
    IN_GAME = "in_game"
    LEAVING_GAME = "leaving_game"


@dataclass
class VirtualBotConfig:
    """Configuration for virtual bots loaded from config.toml."""

    names: list[str] = field(default_factory=list)

    # Timing (in ticks, 50ms each = 20 ticks/sec)
    min_idle_ticks: int = 100  # 5 sec minimum between actions when idle
    max_idle_ticks: int = 600  # 30 sec maximum between actions when idle
    min_online_ticks: int = 1200  # 1 min minimum online before considering going offline
    max_online_ticks: int = 6000  # 5 min maximum online
    min_offline_ticks: int = 600  # 30 sec minimum offline
    max_offline_ticks: int = 3000  # 2.5 min maximum offline
    leave_game_delay_ticks: int = 200  # 10 sec - spread bot departures after game ends
    start_game_delay_ticks: int = 400  # 20 sec - wait for players before starting

    # Behavior probabilities (per decision tick when idle)
    join_game_chance: float = 0.3
    create_game_chance: float = 0.1
    go_offline_chance: float = 0.05

    # Post-game logout behavior
    logout_after_game_chance: float = 0.33  # 33% chance to log off after a game
    logout_after_game_min_ticks: int = 40  # 2 sec minimum delay before logout
    logout_after_game_max_ticks: int = 100  # 5 sec maximum delay before logout


@dataclass
class VirtualBot:
    """State tracking for a single virtual bot."""

    name: str
    state: VirtualBotState = VirtualBotState.OFFLINE

    # Timing state
    cooldown_ticks: int = 0  # Ticks until next state change allowed
    online_ticks: int = 0  # How long this bot has been online
    target_online_ticks: int = 0  # Random target for when to consider going offline
    think_ticks: int = 0  # Ticks until next decision when idle

    # Game state
    table_id: str | None = None  # Current table ID if in game
    game_join_tick: int = 0  # Tick when bot joined/created the game (for start delay)
    logout_after_game: bool = False  # If True, will log off shortly after leaving game


class VirtualBotManager:
    """
    Manages virtual bots that simulate real users on the server.

    Virtual bots navigate menus, create/join games, and play autonomously.
    They come online and go offline on their own schedules to create
    a natural-feeling server population.
    """

    def __init__(self, server: "Server"):
        self._server = server
        self._config = VirtualBotConfig()
        self._bots: dict[str, VirtualBot] = {}  # name -> VirtualBot

    def load_config(self, path: str | Path | None = None) -> None:
        """Load bot configuration from config.toml."""
        if path is None:
            # Default to server/config.toml
            path = Path(__file__).parent.parent / "config.toml"

        path = Path(path)
        if not path.exists():
            print(f"Virtual bots config not found at {path}, using defaults")
            return

        try:
            import tomllib
        except ImportError:
            import tomli as tomllib

        with open(path, "rb") as f:
            data = tomllib.load(f)

        vb_config = data.get("virtual_bots", {})

        self._config = VirtualBotConfig(
            names=vb_config.get("names", []),
            min_idle_ticks=vb_config.get("min_idle_ticks", 100),
            max_idle_ticks=vb_config.get("max_idle_ticks", 600),
            min_online_ticks=vb_config.get("min_online_ticks", 1200),
            max_online_ticks=vb_config.get("max_online_ticks", 6000),
            min_offline_ticks=vb_config.get("min_offline_ticks", 600),
            max_offline_ticks=vb_config.get("max_offline_ticks", 3000),
            leave_game_delay_ticks=vb_config.get("leave_game_delay_ticks", 200),
            start_game_delay_ticks=vb_config.get("start_game_delay_ticks", 400),
            join_game_chance=vb_config.get("join_game_chance", 0.3),
            create_game_chance=vb_config.get("create_game_chance", 0.1),
            go_offline_chance=vb_config.get("go_offline_chance", 0.05),
            logout_after_game_chance=vb_config.get("logout_after_game_chance", 0.33),
            logout_after_game_min_ticks=vb_config.get("logout_after_game_min_ticks", 40),
            logout_after_game_max_ticks=vb_config.get("logout_after_game_max_ticks", 100),
        )

    def save_state(self) -> None:
        """Save all virtual bot state to the database for persistence."""
        db = self._server._db
        if not db:
            return

        # Clear existing saved state
        db.delete_all_virtual_bots()

        # Save each bot's state
        for bot in self._bots.values():
            db.save_virtual_bot(
                name=bot.name,
                state=bot.state.value,
                online_ticks=bot.online_ticks,
                target_online_ticks=bot.target_online_ticks,
                table_id=bot.table_id,
                game_join_tick=bot.game_join_tick,
            )

    def load_state(self) -> int:
        """
        Load virtual bot state from the database.

        Returns the number of bots loaded.
        """
        db = self._server._db
        if not db:
            return 0

        bot_data = db.load_all_virtual_bots()
        count = 0

        for data in bot_data:
            name = data["name"]
            # Only load bots that are in our config
            if name not in self._config.names:
                continue

            bot = VirtualBot(
                name=name,
                state=VirtualBotState(data["state"]),
                online_ticks=data["online_ticks"],
                target_online_ticks=data["target_online_ticks"],
                table_id=data["table_id"],
                game_join_tick=data["game_join_tick"],
            )
            self._bots[name] = bot
            count += 1

            # If the bot was online or in a game, recreate their VirtualUser
            if bot.state in (VirtualBotState.ONLINE_IDLE, VirtualBotState.IN_GAME, VirtualBotState.LEAVING_GAME):
                self._restore_bot_user(bot)

        return count

    def _restore_bot_user(self, bot: VirtualBot) -> None:
        """Restore a VirtualUser for a bot that was online."""
        from ..users.virtual_user import VirtualUser

        # Check if user already exists (e.g., from table loading for IN_GAME bots)
        existing_user = self._server._users.get(bot.name)
        if existing_user:
            # If it's already a VirtualUser, just update state
            if hasattr(existing_user, "is_virtual_bot") and existing_user.is_virtual_bot:
                if bot.state == VirtualBotState.ONLINE_IDLE:
                    self._server._user_states[bot.name] = {"menu": "main_menu"}
                elif bot.state in (VirtualBotState.IN_GAME, VirtualBotState.LEAVING_GAME):
                    self._server._user_states[bot.name] = {
                        "menu": "in_game",
                        "table_id": bot.table_id,
                    }
                return
            else:
                # Username taken by a real user - mark bot as offline
                bot.state = VirtualBotState.OFFLINE
                bot.cooldown_ticks = random.randint(200, 400)
                return

        # Create virtual user and add to server
        user = VirtualUser(bot.name)
        self._server._users[bot.name] = user

        if bot.state == VirtualBotState.ONLINE_IDLE:
            self._server._user_states[bot.name] = {"menu": "main_menu"}
        elif bot.state in (VirtualBotState.IN_GAME, VirtualBotState.LEAVING_GAME):
            self._server._user_states[bot.name] = {
                "menu": "in_game",
                "table_id": bot.table_id,
            }

    def fill_server(self) -> tuple[int, int]:
        """
        Instantiate bots from config that don't already exist.

        50% come online immediately, rest stay offline with random cooldowns.
        Does not replace existing bots or delete bots not in config.

        Returns tuple of (bots_added, bots_brought_online).
        """
        if not self._config.names:
            return 0, 0

        # Collect new bot names (not already instantiated)
        new_names = [name for name in self._config.names if name not in self._bots]
        if not new_names:
            return 0, 0

        # Shuffle so we get a random 50% online
        random.shuffle(new_names)
        half = len(new_names) // 2

        added = 0
        online = 0

        for i, name in enumerate(new_names):
            if i < half:
                # Bring online immediately
                bot = VirtualBot(
                    name=name,
                    state=VirtualBotState.OFFLINE,
                    cooldown_ticks=0,  # Will come online on next tick
                )
                self._bots[name] = bot
                # Actually bring them online now
                self._bring_bot_online(bot)
                online += 1
            else:
                # Stay offline with random long cooldown
                cooldown = random.randint(
                    self._config.min_offline_ticks, self._config.max_offline_ticks
                )
                self._bots[name] = VirtualBot(
                    name=name,
                    state=VirtualBotState.OFFLINE,
                    cooldown_ticks=cooldown,
                )
            added += 1

        return added, online

    def clear_bots(self) -> tuple[int, int]:
        """
        Remove all instantiated bots and kill tables they're in.

        Returns tuple of (bots_cleared, tables_killed).
        """
        bot_count = len(self._bots)
        tables_killed = set()

        for name, bot in list(self._bots.items()):
            # If bot is in a table, kill the table
            if bot.table_id:
                table = self._server._tables.get_table(bot.table_id)
                if table and bot.table_id not in tables_killed:
                    # Notify members that table is being closed
                    if table.game:
                        table.game.broadcast_l("virtual-bot-table-closed")
                    # Remove the table
                    self._server._tables.remove_table(bot.table_id)
                    tables_killed.add(bot.table_id)

            # Take bot offline (removes from server users)
            if bot.state in (VirtualBotState.ONLINE_IDLE, VirtualBotState.IN_GAME, VirtualBotState.LEAVING_GAME):
                self._take_bot_offline_silent(bot)

        self._bots.clear()

        # Also clear from database
        if self._server._db:
            self._server._db.delete_all_virtual_bots()

        return bot_count, len(tables_killed)

    def _take_bot_offline_silent(self, bot: VirtualBot) -> None:
        """Take a bot offline without broadcasting presence."""
        # Remove from server
        self._server._users.pop(bot.name, None)
        self._server._user_states.pop(bot.name, None)

        # Update bot state
        bot.state = VirtualBotState.OFFLINE
        bot.online_ticks = 0
        bot.table_id = None

    def get_status(self) -> dict[str, int]:
        """
        Get counts of bots in each state.

        Returns dict with keys: total, offline, online, in_game
        """
        offline = 0
        online = 0
        in_game = 0

        for bot in self._bots.values():
            if bot.state == VirtualBotState.OFFLINE:
                offline += 1
            elif bot.state == VirtualBotState.ONLINE_IDLE:
                online += 1
            elif bot.state in (VirtualBotState.IN_GAME, VirtualBotState.LEAVING_GAME):
                in_game += 1

        return {
            "total": len(self._bots),
            "offline": offline,
            "online": online,
            "in_game": in_game,
        }

    def on_tick(self) -> None:
        """Process bot decisions each server tick."""
        for bot in list(self._bots.values()):
            self._process_bot_tick(bot)

    def _process_bot_tick(self, bot: VirtualBot) -> None:
        """Process a single bot's tick."""
        # Handle cooldown
        if bot.cooldown_ticks > 0:
            bot.cooldown_ticks -= 1
            return

        if bot.state == VirtualBotState.OFFLINE:
            self._process_offline_bot(bot)
        elif bot.state == VirtualBotState.ONLINE_IDLE:
            self._process_online_idle_bot(bot)
        elif bot.state == VirtualBotState.IN_GAME:
            self._process_in_game_bot(bot)
        elif bot.state == VirtualBotState.LEAVING_GAME:
            self._process_leaving_game_bot(bot)

    def _process_offline_bot(self, bot: VirtualBot) -> None:
        """Process a bot that is currently offline - bring them online."""
        self._bring_bot_online(bot)

    def _process_online_idle_bot(self, bot: VirtualBot) -> None:
        """Process a bot that is online and idle."""
        bot.online_ticks += 1

        # Count down think time
        if bot.think_ticks > 0:
            bot.think_ticks -= 1
            return

        # Decision time!
        config = self._config

        # Consider going offline if we've been online long enough
        if (
            bot.online_ticks >= config.min_online_ticks
            and bot.online_ticks >= bot.target_online_ticks
            and random.random() < config.go_offline_chance
        ):
            self._take_bot_offline(bot)
            return

        # Try to join an existing game
        if random.random() < config.join_game_chance:
            if self._try_join_game(bot):
                return

        # Try to create a new game
        if random.random() < config.create_game_chance:
            if self._try_create_game(bot):
                return

        # Set next think delay
        bot.think_ticks = random.randint(config.min_idle_ticks, config.max_idle_ticks)

    def _process_in_game_bot(self, bot: VirtualBot) -> None:
        """Process a bot that is in a game."""
        bot.online_ticks += 1

        # Check if the game has ended
        if bot.table_id:
            table = self._server._tables.get_table(bot.table_id)
            if not table or not table.game:
                # Table or game no longer exists - transition to leaving
                self._start_leaving_game(bot)
                return

            game = table.game
            if game.status == "finished":
                # Game has ended - transition to leaving
                self._start_leaving_game(bot)
            elif game.status == "waiting":
                # Game hasn't started yet - check if we're host and should start
                # Wait for the configured delay to give players time to join
                ticks_in_game = bot.online_ticks - bot.game_join_tick
                if (
                    game.host == bot.name
                    and len(game.players) >= game.get_min_players()
                    and ticks_in_game >= self._config.start_game_delay_ticks
                ):
                    player = game.get_player_by_name(bot.name)
                    if player:
                        game.execute_action(player, "start_game")

    def _process_leaving_game_bot(self, bot: VirtualBot) -> None:
        """Process a bot that is leaving a game (staggered departure)."""
        bot.online_ticks += 1

        # Leave the table and return to idle (or go offline)
        self._leave_current_table(bot)

        # Decide whether to stay online or go offline
        if bot.logout_after_game:
            # Log off after a short delay (2-5 seconds)
            bot.logout_after_game = False  # Reset flag
            bot.state = VirtualBotState.ONLINE_IDLE
            bot.cooldown_ticks = random.randint(
                self._config.logout_after_game_min_ticks,
                self._config.logout_after_game_max_ticks,
            )
            # Set target so they go offline on next process_online_idle
            bot.target_online_ticks = 0
        elif bot.online_ticks >= bot.target_online_ticks:
            self._take_bot_offline(bot)
        else:
            bot.state = VirtualBotState.ONLINE_IDLE
            bot.think_ticks = random.randint(
                self._config.min_idle_ticks, self._config.max_idle_ticks
            )

    def _bring_bot_online(self, bot: VirtualBot) -> None:
        """Bring a bot online."""
        from ..users.virtual_user import VirtualUser

        # Check if username is already taken by a real user
        if bot.name in self._server._users:
            # Reschedule for later
            bot.cooldown_ticks = random.randint(200, 400)
            return

        # Create virtual user and add to server
        user = VirtualUser(bot.name)
        self._server._users[bot.name] = user
        self._server._user_states[bot.name] = {"menu": "main_menu"}

        # Set up bot state
        bot.state = VirtualBotState.ONLINE_IDLE
        bot.online_ticks = 0
        bot.target_online_ticks = random.randint(
            self._config.min_online_ticks, self._config.max_online_ticks
        )
        bot.think_ticks = random.randint(
            self._config.min_idle_ticks, self._config.max_idle_ticks
        )

        # Broadcast online announcement
        self._server._broadcast_presence_l("user-online", bot.name, "online.ogg")

    def _take_bot_offline(self, bot: VirtualBot) -> None:
        """Take a bot offline."""
        # Leave any table first
        self._leave_current_table(bot)

        # Remove from server
        self._server._users.pop(bot.name, None)
        self._server._user_states.pop(bot.name, None)

        # Broadcast offline announcement
        self._server._broadcast_presence_l("user-offline", bot.name, "offline.ogg")

        # Set up offline state
        bot.state = VirtualBotState.OFFLINE
        bot.cooldown_ticks = random.randint(
            self._config.min_offline_ticks, self._config.max_offline_ticks
        )
        bot.online_ticks = 0
        bot.table_id = None

    def _leave_current_table(self, bot: VirtualBot) -> None:
        """Leave the current table if in one."""
        if not bot.table_id:
            return

        table = self._server._tables.get_table(bot.table_id)
        if table and table.game:
            user = self._server._users.get(bot.name)
            if user:
                # Find player and handle leave properly
                player = table.game.get_player_by_name(bot.name)
                if player:
                    # The game's leave action will handle bot replacement etc.
                    table.game.execute_action(player, "leave")

            # Remove from table members
            table.remove_member(bot.name)

        bot.table_id = None

    def _start_leaving_game(self, bot: VirtualBot) -> None:
        """Start the leaving game process with a staggered delay."""
        bot.state = VirtualBotState.LEAVING_GAME
        bot.cooldown_ticks = random.randint(0, self._config.leave_game_delay_ticks)
        # Decide if this bot will log off after the game
        bot.logout_after_game = random.random() < self._config.logout_after_game_chance

    def _try_join_game(self, bot: VirtualBot) -> bool:
        """Try to join an existing waiting table. Returns True if joined."""
        # Get all waiting tables
        tables = self._server._tables.get_waiting_tables()
        if not tables:
            return False

        # Pick a random table
        table = random.choice(tables)
        game = table.game
        if not game:
            return False

        # Only join games that haven't started yet
        if game.status != "waiting":
            return False

        # Check if there's room
        if len(game.players) >= game.get_max_players():
            return False

        # Join the table
        user = self._server._users.get(bot.name)
        if not user:
            return False

        table.add_member(bot.name, user, as_spectator=False)
        game.add_player(bot.name, user)
        game.broadcast_l("table-joined", player=bot.name)
        game.broadcast_sound("join.ogg")
        game.rebuild_all_menus()

        # Update bot state
        bot.state = VirtualBotState.IN_GAME
        bot.table_id = table.table_id
        bot.game_join_tick = bot.online_ticks  # Track when we joined for start delay
        self._server._user_states[bot.name] = {
            "menu": "in_game",
            "table_id": table.table_id,
        }

        return True

    def _try_create_game(self, bot: VirtualBot) -> bool:
        """Try to create a new game table. Returns True if created."""
        from ..games.registry import GameRegistry, get_game_class

        # Get all available game types
        game_classes = GameRegistry.get_all()
        if not game_classes:
            return False

        # Pick a random game type
        game_class = random.choice(game_classes)
        game_type = game_class.get_type()

        user = self._server._users.get(bot.name)
        if not user:
            return False

        # Create table
        table = self._server._tables.create_table(game_type, bot.name, user)

        # Create game and initialize lobby
        game = game_class()
        table.game = game
        game._table = table
        game.initialize_lobby(bot.name, user)

        # Broadcast table creation to all approved users
        game_name = game_class.get_name()
        self._server._broadcast_table_created(bot.name, game_name)

        # Update bot state
        bot.state = VirtualBotState.IN_GAME
        bot.table_id = table.table_id
        bot.game_join_tick = bot.online_ticks  # Track when we created for start delay
        self._server._user_states[bot.name] = {
            "menu": "in_game",
            "table_id": table.table_id,
        }

        return True

    def on_game_ended(self, table_id: str) -> None:
        """
        Called when a game ends. Triggers bots to start leaving.

        This is called from the server when a table's game finishes.
        """
        for bot in self._bots.values():
            if bot.table_id == table_id and bot.state == VirtualBotState.IN_GAME:
                self._start_leaving_game(bot)
