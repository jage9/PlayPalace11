"""Main server class that ties everything together."""

import asyncio
from pathlib import Path

import json

from .tick import TickScheduler
from ..network.websocket_server import WebSocketServer, ClientConnection
from ..persistence.database import Database
from ..auth.auth import AuthManager
from ..tables.manager import TableManager
from ..users.network_user import NetworkUser
from ..users.base import MenuItem, EscapeBehavior
from ..users.preferences import UserPreferences, DiceKeepingStyle
from ..games.registry import GameRegistry, get_game_class
from ..messages.localization import Localization


VERSION = "11.0.0"

# Default paths based on module location
_MODULE_DIR = Path(__file__).parent.parent
_DEFAULT_LOCALES_DIR = _MODULE_DIR / "locales"


class Server:
    """
    Main PlayPalace v11 server.

    Coordinates all components: network, auth, tables, games, and persistence.
    """

    def __init__(
        self,
        host: str = "0.0.0.0",
        port: int = 8000,
        db_path: str = "playpalace.db",
        locales_dir: str | Path | None = None,
        ssl_cert: str | Path | None = None,
        ssl_key: str | Path | None = None,
    ):
        self.host = host
        self.port = port
        self._ssl_cert = ssl_cert
        self._ssl_key = ssl_key

        # Initialize components
        self._db = Database(db_path)
        self._auth: AuthManager | None = None
        self._tables = TableManager()
        self._tables._server = self  # Enable callbacks from TableManager
        self._ws_server: WebSocketServer | None = None
        self._tick_scheduler: TickScheduler | None = None

        # User tracking
        self._users: dict[str, NetworkUser] = {}  # username -> NetworkUser
        self._user_states: dict[str, dict] = {}  # username -> UI state

        # Initialize localization
        if locales_dir is None:
            locales_dir = _DEFAULT_LOCALES_DIR
        Localization.init(Path(locales_dir))
        Localization.preload_bundles()

    async def start(self) -> None:
        """Start the server."""
        print(f"Starting PlayPalace v{VERSION} server...")

        # Connect to database
        self._db.connect()
        self._auth = AuthManager(self._db)

        # Load existing tables
        self._load_tables()

        # Start WebSocket server
        self._ws_server = WebSocketServer(
            host=self.host,
            port=self.port,
            on_connect=self._on_client_connect,
            on_disconnect=self._on_client_disconnect,
            on_message=self._on_client_message,
            ssl_cert=self._ssl_cert,
            ssl_key=self._ssl_key,
        )
        await self._ws_server.start()

        # Start tick scheduler
        self._tick_scheduler = TickScheduler(self._on_tick)
        await self._tick_scheduler.start()

        protocol = "wss" if self._ssl_cert else "ws"
        print(f"Server running on {protocol}://{self.host}:{self.port}")

    async def stop(self) -> None:
        """Stop the server."""
        print("Stopping server...")

        # Save all tables
        self._save_tables()

        # Stop tick scheduler
        if self._tick_scheduler:
            await self._tick_scheduler.stop()

        # Stop WebSocket server
        if self._ws_server:
            await self._ws_server.stop()

        # Close database
        self._db.close()

        print("Server stopped.")

    def _load_tables(self) -> None:
        """Load tables from database and restore their games."""
        from ..users.bot import Bot

        tables = self._db.load_all_tables()
        for table in tables:
            self._tables.add_table(table)

            # Restore game from JSON if present
            if table.game_json:
                game_class = get_game_class(table.game_type)
                if not game_class:
                    print(f"WARNING: Could not find game class for {table.game_type}")
                    continue

                # Deserialize game and rebuild runtime state
                game = game_class.from_json(table.game_json)
                game.rebuild_runtime_state()
                table.game = game
                game._table = table

                # Setup keybinds (runtime only, not serialized)
                game.setup_keybinds()
                # Attach bots (humans will be attached when they reconnect)
                # Action sets are already restored from serialization
                for player in game.players:
                    if player.is_bot:
                        bot_user = Bot(player.name)
                        game.attach_user(player.id, bot_user)

        print(f"Loaded {len(tables)} tables from database.")

        # Delete all tables from database after loading to prevent stale data
        # on subsequent restarts. Tables will be re-saved on shutdown.
        self._db.delete_all_tables()

    def _save_tables(self) -> None:
        """Save all tables to database."""
        tables = self._tables.save_all()
        self._db.save_all_tables(tables)
        print(f"Saved {len(tables)} tables to database.")

    def _on_tick(self) -> None:
        """Called every tick (50ms)."""
        # Tick all tables
        self._tables.on_tick()

        # Flush queued messages for all users
        self._flush_user_messages()

    def _flush_user_messages(self) -> None:
        """Send all queued messages for all users."""
        for username, user in self._users.items():
            messages = user.get_queued_messages()
            if messages and self._ws_server:
                client = self._ws_server.get_client_by_username(username)
                if client:
                    for msg in messages:
                        asyncio.create_task(client.send(msg))

    async def _on_client_connect(self, client: ClientConnection) -> None:
        """Handle new client connection."""
        print(f"Client connected: {client.address}")

    async def _on_client_disconnect(self, client: ClientConnection) -> None:
        """Handle client disconnection."""
        print(f"Client disconnected: {client.address}")
        if client.username:
            # Broadcast offline announcement to all users (including the disconnecting user)
            self._broadcast_presence_l("user-offline", client.username, "offline.ogg")
            # Clean up user state
            self._users.pop(client.username, None)
            self._user_states.pop(client.username, None)

    def _broadcast_presence_l(
        self, message_id: str, player_name: str, sound: str
    ) -> None:
        """Broadcast a localized presence announcement to all online users with sound."""
        for username, user in self._users.items():
            user.speak_l(message_id, player=player_name)
            user.play_sound(sound)

    async def _on_client_message(self, client: ClientConnection, packet: dict) -> None:
        """Handle incoming message from client."""
        packet_type = packet.get("type")

        if packet_type == "authorize":
            await self._handle_authorize(client, packet)
        elif packet_type == "register":
            await self._handle_register(client, packet)
        elif not client.authenticated:
            # Ignore non-auth packets from unauthenticated clients
            return
        elif packet_type == "menu":
            await self._handle_menu(client, packet)
        elif packet_type == "keybind":
            await self._handle_keybind(client, packet)
        elif packet_type == "editbox":
            await self._handle_editbox(client, packet)
        elif packet_type == "chat":
            await self._handle_chat(client, packet)
        elif packet_type == "ping":
            await self._handle_ping(client)

    async def _handle_authorize(self, client: ClientConnection, packet: dict) -> None:
        """Handle authorization packet."""
        username = packet.get("username", "")
        password = packet.get("password", "")

        # Try to authenticate or register
        if not self._auth.authenticate(username, password):
            # Try to register
            if not self._auth.register(username, password):
                # Username taken with different password
                await client.send(
                    {
                        "type": "disconnect",
                        "reason": "Invalid credentials",
                        "reconnect": False,
                    }
                )
                return

        # Authentication successful
        client.username = username
        client.authenticated = True

        # Create network user with preferences and persistent UUID
        user_record = self._auth.get_user(username)
        locale = user_record.locale if user_record else "en"
        user_uuid = user_record.uuid if user_record else None
        preferences = UserPreferences()
        if user_record and user_record.preferences_json:
            try:
                prefs_data = json.loads(user_record.preferences_json)
                preferences = UserPreferences.from_dict(prefs_data)
            except (json.JSONDecodeError, KeyError):
                pass  # Use defaults on error
        user = NetworkUser(username, locale, client, uuid=user_uuid, preferences=preferences)
        self._users[username] = user

        # Broadcast online announcement to all users (including the new user)
        self._broadcast_presence_l("user-online", username, "online.ogg")

        # Send success response
        await client.send(
            {
                "type": "authorize_success",
                "username": username,
                "version": VERSION,
            }
        )

        # Send game list
        await self._send_game_list(client)

        # Check if user is in a table
        table = self._tables.find_user_table(username)

        if table and table.game:
            # Rejoin table - use same approach as _restore_saved_table
            game = table.game

            # Attach user to table and game
            table.attach_user(username, user)
            player = game.get_player_by_id(user.uuid)
            if player:
                game.attach_user(player.id, user)

                # Set user state so menu selections are handled correctly
                self._user_states[username] = {
                    "menu": "in_game",
                    "table_id": table.table_id,
                }

                # Rebuild menu for this player
                game.rebuild_player_menu(player)
        else:
            # Show main menu
            self._show_main_menu(user)

    async def _handle_register(self, client: ClientConnection, packet: dict) -> None:
        """Handle registration packet from registration dialog."""
        username = packet.get("username", "")
        password = packet.get("password", "")
        # email and bio are sent but not stored yet

        if not username or not password:
            await client.send({
                "type": "speak",
                "text": "Username and password are required."
            })
            return

        # Try to register the user
        if self._auth.register(username, password):
            await client.send({
                "type": "speak",
                "text": "Registration successful! You can now log in with your credentials."
            })
        else:
            await client.send({
                "type": "speak",
                "text": "Username already taken. Please choose a different username."
            })

    async def _send_game_list(self, client: ClientConnection) -> None:
        """Send the list of available games to the client."""
        games = []
        for game_class in GameRegistry.get_all():
            games.append(
                {
                    "type": game_class.get_type(),
                    "name": game_class.get_name(),
                }
            )

        await client.send(
            {
                "type": "update_options_lists",
                "games": games
            }
        )

    def _show_main_menu(self, user: NetworkUser) -> None:
        """Show the main menu to a user."""
        items = [
            MenuItem(text=Localization.get(user.locale, "play"), id="play"),
            MenuItem(
                text=Localization.get(user.locale, "saved-tables"), id="saved_tables"
            ),
            MenuItem(
                text=Localization.get(user.locale, "leaderboards"), id="leaderboards"
            ),
            MenuItem(
                text=Localization.get(user.locale, "my-stats"), id="my_stats"
            ),
            MenuItem(text=Localization.get(user.locale, "options"), id="options"),
            MenuItem(text=Localization.get(user.locale, "logout"), id="logout"),
        ]
        user.show_menu(
            "main_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        user.play_music("mainmus.ogg")
        user.stop_ambience()
        self._user_states[user.username] = {"menu": "main_menu"}

    def _show_categories_menu(self, user: NetworkUser) -> None:
        """Show game categories menu."""
        categories = GameRegistry.get_by_category()
        items = []
        for category_key in sorted(categories.keys()):
            category_name = Localization.get(user.locale, category_key)
            items.append(MenuItem(text=category_name, id=f"category_{category_key}"))
        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "categories_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {"menu": "categories_menu"}

    def _show_games_menu(self, user: NetworkUser, category: str) -> None:
        """Show games in a category."""
        categories = GameRegistry.get_by_category()
        games = categories.get(category, [])

        items = []
        for game_class in games:
            game_name = Localization.get(user.locale, game_class.get_name_key())
            items.append(MenuItem(text=game_name, id=f"game_{game_class.get_type()}"))
        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "games_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {"menu": "games_menu", "category": category}

    def _show_tables_menu(self, user: NetworkUser, game_type: str) -> None:
        """Show available tables for a game."""
        tables = self._tables.get_waiting_tables(game_type)
        game_class = get_game_class(game_type)
        game_name = (
            Localization.get(user.locale, game_class.get_name_key())
            if game_class
            else game_type
        )

        items = [
            MenuItem(
                text=Localization.get(user.locale, "create-table"), id="create_table"
            )
        ]

        for table in tables:
            player_count = table.player_count
            items.append(
                MenuItem(
                    text=Localization.get(
                        user.locale,
                        "table-listing",
                        host=table.host,
                        count=player_count,
                    ),
                    id=f"table_{table.table_id}",
                )
            )

        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "tables_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {
            "menu": "tables_menu",
            "game_type": game_type,
            "game_name": game_name,
        }

    # Dice keeping style display names
    DICE_KEEPING_STYLES = {
        DiceKeepingStyle.PLAYPALACE: "PlayPalace style",
        DiceKeepingStyle.QUENTIN_C: "Quentin C style",
    }

    def _show_options_menu(self, user: NetworkUser) -> None:
        """Show options menu."""
        languages = Localization.get_available_languages(user.locale, fallback= user.locale)
        current_lang = languages.get(user.locale, user.locale)
        prefs = user.preferences

        # Turn sound option
        turn_sound_status = Localization.get(
            user.locale,
            "option-on" if prefs.play_turn_sound else "option-off",
        )

        # Clear kept dice option
        clear_kept_status = Localization.get(
            user.locale,
            "option-on" if prefs.clear_kept_on_roll else "option-off",
        )

        # Dice keeping style option
        dice_style_name = self.DICE_KEEPING_STYLES.get(
            prefs.dice_keeping_style, "PlayPalace style"
        )

        items = [
            MenuItem(
                text=Localization.get(
                    user.locale, "language-option", language=current_lang
                ),
                id="language",
            ),
            MenuItem(
                text=Localization.get(
                    user.locale, "turn-sound-option", status=turn_sound_status
                ),
                id="turn_sound",
            ),
            MenuItem(
                text=Localization.get(
                    user.locale, "clear-kept-option", status=clear_kept_status
                ),
                id="clear_kept",
            ),
            MenuItem(
                text=Localization.get(
                    user.locale, "dice-keeping-style-option", style=dice_style_name
                ),
                id="dice_keeping_style",
            ),
            MenuItem(text=Localization.get(user.locale, "back"), id="back"),
        ]
        user.show_menu(
            "options_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {"menu": "options_menu"}

    def _show_language_menu(self, user: NetworkUser) -> None:
        """Show language selection menu."""
        # Get languages in their native names and in user's locale for comparison
        languages = Localization.get_available_languages(fallback = user.locale)
        localized_languages = Localization.get_available_languages(user.locale, fallback= user.locale)

        items = []
        for lang_code, lang_name in languages.items():
            prefix = "* " if lang_code == user.locale else ""
            localized_name = localized_languages.get(lang_code, lang_name)
            # Show localized name first, then native name in parentheses if different
            if localized_name != lang_name:
                display = f"{prefix}{localized_name} ({lang_name})"
            else:
                display = f"{prefix}{lang_name}"
            items.append(MenuItem(text=display, id=f"lang_{lang_code}"))
        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))
        user.show_menu(
            "language_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {"menu": "language_menu"}

    def _show_saved_tables_menu(self, user: NetworkUser) -> None:
        """Show saved tables menu."""
        saved = self._db.get_user_saved_tables(user.username)

        if not saved:
            user.speak_l("no-saved-tables")
            self._show_main_menu(user)
            return

        items = []
        for record in saved:
            items.append(MenuItem(text=record.save_name, id=f"saved_{record.id}"))
        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "saved_tables_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {"menu": "saved_tables_menu"}

    def _show_saved_table_actions_menu(self, user: NetworkUser, save_id: int) -> None:
        """Show actions for a saved table (restore, delete)."""
        items = [
            MenuItem(text=Localization.get(user.locale, "restore-table"), id="restore"),
            MenuItem(
                text=Localization.get(user.locale, "delete-saved-table"), id="delete"
            ),
            MenuItem(text=Localization.get(user.locale, "back"), id="back"),
        ]
        user.show_menu(
            "saved_table_actions_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {
            "menu": "saved_table_actions_menu",
            "save_id": save_id,
        }

    async def _handle_menu(self, client: ClientConnection, packet: dict) -> None:
        """Handle menu selection."""
        username = client.username
        if not username:
            return

        user = self._users.get(username)
        if not user:
            return

        selection_id = packet.get("selection_id", "")

        state = self._user_states.get(username, {})
        current_menu = state.get("menu")

        # Check if user is in a table - delegate all events to game
        table = self._tables.find_user_table(username)
        if table and table.game:
            player = table.game.get_player_by_id(user.uuid)
            if player:
                table.game.handle_event(player, packet)
                # Check if player left the game (user replaced by bot or removed)
                game_user = table.game._users.get(user.uuid)
                if game_user is not user:
                    table.remove_member(username)
                    self._show_main_menu(user)
            return

        # Handle menu selections based on current menu
        if current_menu == "main_menu":
            await self._handle_main_menu_selection(user, selection_id)
        elif current_menu == "categories_menu":
            await self._handle_categories_selection(user, selection_id, state)
        elif current_menu == "games_menu":
            await self._handle_games_selection(user, selection_id, state)
        elif current_menu == "tables_menu":
            await self._handle_tables_selection(user, selection_id, state)
        elif current_menu == "join_menu":
            await self._handle_join_selection(user, selection_id, state)
        elif current_menu == "options_menu":
            await self._handle_options_selection(user, selection_id)
        elif current_menu == "language_menu":
            await self._handle_language_selection(user, selection_id)
        elif current_menu == "dice_keeping_style_menu":
            await self._handle_dice_keeping_style_selection(user, selection_id)
        elif current_menu == "saved_tables_menu":
            await self._handle_saved_tables_selection(user, selection_id, state)
        elif current_menu == "saved_table_actions_menu":
            await self._handle_saved_table_actions_selection(user, selection_id, state)
        elif current_menu == "leaderboards_menu":
            await self._handle_leaderboards_selection(user, selection_id, state)
        elif current_menu == "leaderboard_types_menu":
            await self._handle_leaderboard_types_selection(user, selection_id, state)
        elif current_menu == "game_leaderboard":
            await self._handle_game_leaderboard_selection(user, selection_id, state)
        elif current_menu == "my_stats_menu":
            await self._handle_my_stats_selection(user, selection_id, state)
        elif current_menu == "my_game_stats":
            await self._handle_my_game_stats_selection(user, selection_id, state)

    async def _handle_main_menu_selection(
        self, user: NetworkUser, selection_id: str
    ) -> None:
        """Handle main menu selection."""
        if selection_id == "play":
            self._show_categories_menu(user)
        elif selection_id == "saved_tables":
            self._show_saved_tables_menu(user)
        elif selection_id == "leaderboards":
            self._show_leaderboards_menu(user)
        elif selection_id == "my_stats":
            self._show_my_stats_menu(user)
        elif selection_id == "options":
            self._show_options_menu(user)
        elif selection_id == "logout":
            user.speak_l("goodbye")
            await user.connection.send({"type": "disconnect", "reconnect": False})

    async def _handle_options_selection(
        self, user: NetworkUser, selection_id: str
    ) -> None:
        """Handle options menu selection."""
        if selection_id == "language":
            self._show_language_menu(user)
        elif selection_id == "turn_sound":
            # Toggle turn sound
            prefs = user.preferences
            prefs.play_turn_sound = not prefs.play_turn_sound
            self._save_user_preferences(user)
            self._show_options_menu(user)
        elif selection_id == "clear_kept":
            # Toggle clear kept on roll
            prefs = user.preferences
            prefs.clear_kept_on_roll = not prefs.clear_kept_on_roll
            self._save_user_preferences(user)
            self._show_options_menu(user)
        elif selection_id == "dice_keeping_style":
            self._show_dice_keeping_style_menu(user)
        elif selection_id == "back":
            self._show_main_menu(user)

    def _show_dice_keeping_style_menu(self, user: NetworkUser) -> None:
        """Show dice keeping style selection menu."""
        items = []
        current_style = user.preferences.dice_keeping_style
        for style, name in self.DICE_KEEPING_STYLES.items():
            prefix = "* " if style == current_style else ""
            items.append(MenuItem(text=f"{prefix}{name}", id=f"style_{style.value}"))
        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))
        user.show_menu(
            "dice_keeping_style_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {"menu": "dice_keeping_style_menu"}

    async def _handle_dice_keeping_style_selection(
        self, user: NetworkUser, selection_id: str
    ) -> None:
        """Handle dice keeping style selection."""
        if selection_id.startswith("style_"):
            style_value = selection_id[6:]  # Remove "style_" prefix
            style = DiceKeepingStyle.from_str(style_value)
            user.preferences.dice_keeping_style = style
            self._save_user_preferences(user)
            style_name = self.DICE_KEEPING_STYLES.get(style, "PlayPalace style")
            user.speak_l("dice-keeping-style-changed", style=style_name)
            self._show_options_menu(user)
            return
        # Back or invalid
        self._show_options_menu(user)

    def _save_user_preferences(self, user: NetworkUser) -> None:
        """Save user preferences to database."""
        prefs_json = json.dumps(user.preferences.to_dict())
        self._db.update_user_preferences(user.username, prefs_json)

    async def _handle_language_selection(
        self, user: NetworkUser, selection_id: str
    ) -> None:
        """Handle language selection."""
        if selection_id.startswith("lang_"):
            lang_code = selection_id[5:]  # Remove "lang_" prefix
            languages = Localization.get_available_languages(fallback= user.locale)
            if lang_code in languages:
                user.set_locale(lang_code)
                self._db.update_user_locale(user.username, lang_code)
                user.speak_l("language-changed", language=languages[lang_code])
                self._show_options_menu(user)
                return
        # Back or invalid
        self._show_options_menu(user)

    async def _handle_categories_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle category selection."""
        if selection_id.startswith("category_"):
            category = selection_id[9:]  # Remove "category_" prefix
            self._show_games_menu(user, category)
        elif selection_id == "back":
            self._show_main_menu(user)

    async def _handle_games_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle game selection."""
        if selection_id.startswith("game_"):
            game_type = selection_id[5:]  # Remove "game_" prefix
            self._show_tables_menu(user, game_type)
        elif selection_id == "back":
            self._show_categories_menu(user)

    async def _handle_tables_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle tables menu selection."""
        game_type = state.get("game_type", "")

        if selection_id == "create_table":
            table = self._tables.create_table(game_type, user.username, user)

            # Create game immediately and initialize lobby
            game_class = get_game_class(game_type)
            if game_class:
                game = game_class()
                table.game = game
                game._table = table  # Enable game to call table.destroy()
                game.initialize_lobby(user.username, user)

                user.speak_l(
                    "table-created",
                    host=user.username,
                    game=state.get("game_name", game_type),
                )
                min_players = game_class.get_min_players()
                max_players = game_class.get_max_players()
                user.speak_l(
                    "waiting-for-players",
                    current=len(game.players),
                    min=min_players,
                    max=max_players,
                )
            self._user_states[user.username] = {
                "menu": "in_game",
                "table_id": table.table_id,
            }

        elif selection_id.startswith("table_"):
            table_id = selection_id[6:]  # Remove "table_" prefix
            table = self._tables.get_table(table_id)
            if table:
                # Show join options
                items = [
                    MenuItem(
                        text=Localization.get(user.locale, "join-as-player"),
                        id="join_player",
                    ),
                    MenuItem(
                        text=Localization.get(user.locale, "join-as-spectator"),
                        id="join_spectator",
                    ),
                    MenuItem(text=Localization.get(user.locale, "back"), id="back"),
                ]
                user.show_menu(
                    "join_menu", items, escape_behavior=EscapeBehavior.SELECT_LAST
                )
                self._user_states[user.username] = {
                    "menu": "join_menu",
                    "table_id": table_id,
                    "game_type": game_type,
                }
            else:
                user.speak_l("table-not-exists")
                self._show_tables_menu(user, game_type)

        elif selection_id == "back":
            category = None
            for cat, games in GameRegistry.get_by_category().items():
                if any(g.get_type() == game_type for g in games):
                    category = cat
                    break
            if category:
                self._show_games_menu(user, category)
            else:
                self._show_categories_menu(user)

    async def _handle_join_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle join menu selection."""
        table_id = state.get("table_id")
        table = self._tables.get_table(table_id)

        if not table or not table.game:
            user.speak_l("table-not-exists")
            self._show_tables_menu(user, state.get("game_type", ""))
            return

        game = table.game

        if selection_id == "join_player":
            # Check if game is already in progress
            if game.status == "playing":
                # Look for a player with matching UUID that is now a bot
                matching_player = None
                for p in game.players:
                    if p.id == user.uuid and p.is_bot:
                        matching_player = p
                        break

                if matching_player:
                    # Take over from the bot
                    matching_player.is_bot = False
                    game.attach_user(matching_player.id, user)
                    table.add_member(user.username, user, as_spectator=False)
                    game.broadcast_l("player-took-over", player=user.username)
                    game.broadcast_sound("join.ogg")
                    game.rebuild_all_menus()
                    self._user_states[user.username] = {
                        "menu": "in_game",
                        "table_id": table_id,
                    }
                    return
                else:
                    # No matching player - join as spectator instead
                    table.add_member(user.username, user, as_spectator=True)
                    user.speak_l("spectator-joined", host=table.host)
                    self._user_states[user.username] = {
                        "menu": "in_game",
                        "table_id": table_id,
                    }
                    return

            if len(game.players) >= game.get_max_players():
                user.speak_l("table-full")
                self._show_tables_menu(user, state.get("game_type", ""))
                return

            # Add player to game
            table.add_member(user.username, user, as_spectator=False)
            game.add_player(user.username, user)
            game.broadcast_l("table-joined", player=user.username)
            game.broadcast_sound("join.ogg")
            game.rebuild_all_menus()
            self._user_states[user.username] = {"menu": "in_game", "table_id": table_id}

        elif selection_id == "join_spectator":
            table.add_member(user.username, user, as_spectator=True)
            user.speak_l("spectator-joined", host=table.host)
            # TODO: spectator viewing - for now just track membership
            self._user_states[user.username] = {"menu": "in_game", "table_id": table_id}

        elif selection_id == "back":
            self._show_tables_menu(user, state.get("game_type", ""))

    async def _handle_saved_tables_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle saved tables menu selection."""
        if selection_id.startswith("saved_"):
            save_id = int(selection_id[6:])  # Remove "saved_" prefix
            self._show_saved_table_actions_menu(user, save_id)
        elif selection_id == "back":
            self._show_main_menu(user)

    async def _handle_saved_table_actions_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle saved table actions (restore/delete)."""
        save_id = state.get("save_id")
        if not save_id:
            self._show_main_menu(user)
            return

        if selection_id == "restore":
            await self._restore_saved_table(user, save_id)
        elif selection_id == "delete":
            self._db.delete_saved_table(save_id)
            user.speak_l("saved-table-deleted")
            self._show_saved_tables_menu(user)
        elif selection_id == "back":
            self._show_saved_tables_menu(user)

    async def _restore_saved_table(self, user: NetworkUser, save_id: int) -> None:
        """Restore a saved table."""
        import json
        from ..users.bot import Bot

        record = self._db.get_saved_table(save_id)
        if not record:
            user.speak_l("table-not-exists")
            self._show_main_menu(user)
            return

        # Get the game class
        game_class = get_game_class(record.game_type)
        if not game_class:
            user.speak_l("game-type-not-found")
            self._show_main_menu(user)
            return

        # Parse members from saved state
        members_data = json.loads(record.members_json)
        human_players = [m for m in members_data if not m.get("is_bot", False)]

        # Check all human players are available
        missing_players = []
        for member in human_players:
            member_username = member.get("username")
            if member_username not in self._users:
                missing_players.append(member_username)
            else:
                # Check they're not already in a table
                existing_table = self._tables.find_user_table(member_username)
                if existing_table:
                    missing_players.append(member_username)

        if missing_players:
            user.speak_l("missing-players", players=", ".join(missing_players))
            self._show_saved_tables_menu(user)
            return

        # All players available - create table and restore game
        table = self._tables.create_table(record.game_type, user.username, user)

        # Load game from JSON and rebuild runtime state
        game = game_class.from_json(record.game_json)
        game.rebuild_runtime_state()
        table.game = game
        game._table = table  # Enable game to call table.destroy()

        # Update host to the restorer
        game.host = user.username

        # Attach users and transfer all human players
        # NOTE: We must attach users by player.id (UUID), not by username.
        # The deserialized game has player objects with their original IDs.
        for member in members_data:
            member_username = member.get("username")
            is_bot = member.get("is_bot", False)

            # Find the player object by name to get their ID
            player = game.get_player_by_name(member_username)
            if not player:
                continue

            if is_bot:
                # Recreate bot with the player's original ID
                bot_user = Bot(member_username, uuid=player.id)
                game.attach_user(player.id, bot_user)
            else:
                # Attach human user by player ID
                member_user = self._users.get(member_username)
                if member_user:
                    table.add_member(member_username, member_user, as_spectator=False)
                    game.attach_user(player.id, member_user)
                    self._user_states[member_username] = {
                        "menu": "in_game",
                        "table_id": table.table_id,
                    }

        # Setup keybinds (runtime only, not serialized)
        # Action sets are already restored from serialization
        game.setup_keybinds()

        # Rebuild menus for all players
        game.rebuild_all_menus()

        # Notify all players
        game.broadcast_l("table-restored")

        # Delete the saved table now that it's been restored
        self._db.delete_saved_table(save_id)

    def _show_leaderboards_menu(self, user: NetworkUser) -> None:
        """Show leaderboards game selection menu."""
        categories = GameRegistry.get_by_category()
        items = []

        # Add all games from all categories
        for category_key in sorted(categories.keys()):
            for game_class in categories[category_key]:
                game_name = Localization.get(user.locale, game_class.get_name_key())
                items.append(
                    MenuItem(text=game_name, id=f"lb_{game_class.get_type()}")
                )

        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "leaderboards_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {"menu": "leaderboards_menu"}

    def _show_leaderboard_types_menu(self, user: NetworkUser, game_type: str) -> None:
        """Show leaderboard type selection menu for a game."""
        game_class = get_game_class(game_type)
        if not game_class:
            user.speak_l("game-type-not-found")
            return

        # Check if there's any data for this game
        results = self._db.get_game_stats(game_type, limit=1)
        if not results:
            # No data - speak message and stay on game selection
            user.speak_l("leaderboard-no-data")
            return

        game_name = Localization.get(user.locale, game_class.get_name_key())

        # Available leaderboard types (common to all games)
        items = [
            MenuItem(
                text=Localization.get(user.locale, "leaderboard-type-wins"),
                id="type_wins",
            ),
            MenuItem(
                text=Localization.get(user.locale, "leaderboard-type-rating"),
                id="type_rating",
            ),
            MenuItem(
                text=Localization.get(user.locale, "leaderboard-type-total-score"),
                id="type_total_score",
            ),
            MenuItem(
                text=Localization.get(user.locale, "leaderboard-type-high-score"),
                id="type_high_score",
            ),
            MenuItem(
                text=Localization.get(user.locale, "leaderboard-type-games-played"),
                id="type_games_played",
            ),
        ]

        # Game-specific leaderboards (declared by each game class)
        for lb_config in game_class.get_leaderboard_types():
            lb_id = lb_config["id"]
            # Convert underscores to hyphens for localization key
            loc_key = f"leaderboard-type-{lb_id.replace('_', '-')}"
            items.append(
                MenuItem(
                    text=Localization.get(user.locale, loc_key),
                    id=f"type_{lb_id}",
                )
            )

        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "leaderboard_types_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {
            "menu": "leaderboard_types_menu",
            "game_type": game_type,
            "game_name": game_name,
        }

    def _get_game_results(self, game_type: str) -> list:
        """Get game results as GameResult objects."""
        from ..game_utils.game_result import GameResult, PlayerResult
        import json

        results = self._db.get_game_stats(game_type, limit=100)
        game_results = []

        for row in results:
            custom_data = json.loads(row[4]) if row[4] else {}
            player_rows = self._db.get_game_result_players(row[0])
            player_results = [
                PlayerResult(
                    player_id=p["player_id"],
                    player_name=p["player_name"],
                    is_bot=p["is_bot"],
                )
                for p in player_rows
            ]
            game_results.append(
                GameResult(
                    game_type=row[1],
                    timestamp=row[2],
                    duration_ticks=row[3],
                    player_results=player_results,
                    custom_data=custom_data,
                )
            )

        return game_results

    def _show_wins_leaderboard(
        self, user: NetworkUser, game_type: str, game_name: str
    ) -> None:
        """Show win leaders leaderboard."""
        from ..game_utils.stats_helpers import LeaderboardHelper

        game_results = self._get_game_results(game_type)

        # Build player stats: {player_id: {wins, losses, name}}
        player_stats: dict[str, dict] = {}
        for result in game_results:
            winner_name = result.custom_data.get("winner_name")
            for p in result.player_results:
                if p.is_bot:
                    continue
                if p.player_id not in player_stats:
                    player_stats[p.player_id] = {
                        "wins": 0,
                        "losses": 0,
                        "name": p.player_name,
                    }
                if winner_name == p.player_name:
                    player_stats[p.player_id]["wins"] += 1
                else:
                    player_stats[p.player_id]["losses"] += 1

        # Sort by wins descending
        sorted_players = sorted(
            player_stats.items(), key=lambda x: x[1]["wins"], reverse=True
        )

        items = []

        for rank, (player_id, stats) in enumerate(sorted_players[:10], 1):
            wins = stats["wins"]
            losses = stats["losses"]
            total = wins + losses
            percentage = round((wins / total * 100) if total > 0 else 0)
            items.append(
                MenuItem(
                    text=Localization.get(
                        user.locale,
                        "leaderboard-wins-entry",
                        rank=rank,
                        player=stats["name"],
                        wins=wins,
                        losses=losses,
                        percentage=percentage,
                    ),
                    id=f"entry_{rank}",
                )
            )

        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "game_leaderboard",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {
            "menu": "game_leaderboard",
            "game_type": game_type,
            "game_name": game_name,
        }

    def _show_rating_leaderboard(
        self, user: NetworkUser, game_type: str, game_name: str
    ) -> None:
        """Show skill rating leaderboard."""
        from ..game_utils.stats_helpers import RatingHelper

        rating_helper = RatingHelper(self._db, game_type)
        ratings = rating_helper.get_leaderboard(limit=10)

        items = []

        if not ratings:
            items.append(
                MenuItem(
                    text=Localization.get(user.locale, "leaderboard-no-ratings"),
                    id="no_data",
                )
            )
        else:
            for rank, rating in enumerate(ratings, 1):
                # Get player name from UUID - check recent game results
                player_name = rating.player_id
                # Look up name from game results
                results = self._db.get_game_stats(game_type, limit=100)
                for result in results:
                    players = self._db.get_game_result_players(result[0])
                    for p in players:
                        if p["player_id"] == rating.player_id:
                            player_name = p["player_name"]
                            break
                    if player_name != rating.player_id:
                        break

                items.append(
                    MenuItem(
                        text=Localization.get(
                            user.locale,
                            "leaderboard-rating-entry",
                            rank=rank,
                            player=player_name,
                            rating=round(rating.ordinal),
                            mu=round(rating.mu, 1),
                            sigma=round(rating.sigma, 1),
                        ),
                        id=f"entry_{rank}",
                    )
                )

        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "game_leaderboard",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {
            "menu": "game_leaderboard",
            "game_type": game_type,
            "game_name": game_name,
        }

    def _show_total_score_leaderboard(
        self, user: NetworkUser, game_type: str, game_name: str
    ) -> None:
        """Show total score leaderboard."""
        from ..game_utils.stats_helpers import LeaderboardHelper

        game_results = self._get_game_results(game_type)

        # Build total scores per player
        player_scores: dict[str, dict] = {}
        for result in game_results:
            final_scores = result.custom_data.get("final_scores", {})
            for p in result.player_results:
                if p.is_bot:
                    continue
                if p.player_id not in player_scores:
                    player_scores[p.player_id] = {"total": 0, "name": p.player_name}
                # Try to get score by player name
                score = final_scores.get(p.player_name, 0)
                if score:
                    player_scores[p.player_id]["total"] += score

        # Sort by total score descending
        sorted_players = sorted(
            player_scores.items(), key=lambda x: x[1]["total"], reverse=True
        )

        items = []

        for rank, (player_id, stats) in enumerate(sorted_players[:10], 1):
            items.append(
                MenuItem(
                    text=Localization.get(
                        user.locale,
                        "leaderboard-score-entry",
                        rank=rank,
                        player=stats["name"],
                        value=int(stats["total"]),
                    ),
                    id=f"entry_{rank}",
                )
            )

        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "game_leaderboard",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {
            "menu": "game_leaderboard",
            "game_type": game_type,
            "game_name": game_name,
        }

    def _show_high_score_leaderboard(
        self, user: NetworkUser, game_type: str, game_name: str
    ) -> None:
        """Show high score leaderboard."""
        game_results = self._get_game_results(game_type)

        # Build high scores per player
        player_high: dict[str, dict] = {}
        for result in game_results:
            final_scores = result.custom_data.get("final_scores", {})
            for p in result.player_results:
                if p.is_bot:
                    continue
                score = final_scores.get(p.player_name, 0)
                if p.player_id not in player_high:
                    player_high[p.player_id] = {"high": score, "name": p.player_name}
                elif score > player_high[p.player_id]["high"]:
                    player_high[p.player_id]["high"] = score

        # Sort by high score descending
        sorted_players = sorted(
            player_high.items(), key=lambda x: x[1]["high"], reverse=True
        )

        items = []

        for rank, (player_id, stats) in enumerate(sorted_players[:10], 1):
            items.append(
                MenuItem(
                    text=Localization.get(
                        user.locale,
                        "leaderboard-score-entry",
                        rank=rank,
                        player=stats["name"],
                        value=int(stats["high"]),
                    ),
                    id=f"entry_{rank}",
                )
            )

        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "game_leaderboard",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {
            "menu": "game_leaderboard",
            "game_type": game_type,
            "game_name": game_name,
        }

    def _show_games_played_leaderboard(
        self, user: NetworkUser, game_type: str, game_name: str
    ) -> None:
        """Show games played leaderboard."""
        game_results = self._get_game_results(game_type)

        # Count games per player
        player_games: dict[str, dict] = {}
        for result in game_results:
            for p in result.player_results:
                if p.is_bot:
                    continue
                if p.player_id not in player_games:
                    player_games[p.player_id] = {"count": 0, "name": p.player_name}
                player_games[p.player_id]["count"] += 1

        # Sort by games played descending
        sorted_players = sorted(
            player_games.items(), key=lambda x: x[1]["count"], reverse=True
        )

        items = []

        for rank, (player_id, stats) in enumerate(sorted_players[:10], 1):
            items.append(
                MenuItem(
                    text=Localization.get(
                        user.locale,
                        "leaderboard-games-entry",
                        rank=rank,
                        player=stats["name"],
                        value=stats["count"],
                    ),
                    id=f"entry_{rank}",
                )
            )

        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "game_leaderboard",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {
            "menu": "game_leaderboard",
            "game_type": game_type,
            "game_name": game_name,
        }

    def _extract_value_from_path(
        self, data: dict, path: str, player_id: str, player_name: str
    ) -> float | None:
        """Extract a value from custom_data using a dot-separated path.

        Supports {player_id} and {player_name} placeholders in path.
        """
        # Replace placeholders
        resolved_path = path.replace("{player_id}", player_id)
        resolved_path = resolved_path.replace("{player_name}", player_name)

        # Navigate the path
        parts = resolved_path.split(".")
        current = data
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return None

        # Convert to float if possible
        if isinstance(current, (int, float)):
            return float(current)
        return None

    def _show_custom_leaderboard(
        self,
        user: NetworkUser,
        game_type: str,
        game_name: str,
        config: dict,
    ) -> None:
        """Show a custom leaderboard using declarative config."""
        game_results = self._get_game_results(game_type)

        lb_id = config["id"]
        aggregate = config.get("aggregate", "sum")
        format_key = config.get("format", "score")
        decimals = config.get("decimals", 0)

        # Check if this is a ratio calculation or simple path
        is_ratio = "numerator" in config and "denominator" in config

        # Aggregate data per player
        player_data: dict[str, dict] = {}

        for result in game_results:
            custom_data = result.custom_data
            for p in result.player_results:
                if p.is_bot:
                    continue

                if p.player_id not in player_data:
                    player_data[p.player_id] = {
                        "name": p.player_name,
                        "values": [],
                        "numerators": [],
                        "denominators": [],
                    }

                if is_ratio:
                    num = self._extract_value_from_path(
                        custom_data, config["numerator"], p.player_id, p.player_name
                    )
                    denom = self._extract_value_from_path(
                        custom_data, config["denominator"], p.player_id, p.player_name
                    )
                    if num is not None and denom is not None:
                        player_data[p.player_id]["numerators"].append(num)
                        player_data[p.player_id]["denominators"].append(denom)
                else:
                    value = self._extract_value_from_path(
                        custom_data, config["path"], p.player_id, p.player_name
                    )
                    if value is not None:
                        player_data[p.player_id]["values"].append(value)

        # Calculate final values based on aggregate type
        player_scores: list[tuple[str, str, float]] = []

        for player_id, data in player_data.items():
            if is_ratio:
                total_num = sum(data["numerators"])
                total_denom = sum(data["denominators"])
                if total_denom > 0:
                    value = total_num / total_denom
                    player_scores.append((player_id, data["name"], value))
            else:
                values = data["values"]
                if not values:
                    continue

                if aggregate == "sum":
                    value = sum(values)
                elif aggregate == "max":
                    value = max(values)
                elif aggregate == "avg":
                    value = sum(values) / len(values)
                else:
                    value = sum(values)

                player_scores.append((player_id, data["name"], value))

        # Sort descending
        player_scores.sort(key=lambda x: x[2], reverse=True)

        # Build menu items
        items = []
        entry_key = f"leaderboard-{format_key}-entry"

        for rank, (player_id, name, value) in enumerate(player_scores[:10], 1):
            display_value = round(value, decimals) if decimals > 0 else int(value)
            items.append(
                MenuItem(
                    text=Localization.get(
                        user.locale,
                        entry_key,
                        rank=rank,
                        player=name,
                        value=display_value,
                    ),
                    id=f"entry_{rank}",
                )
            )

        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "game_leaderboard",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {
            "menu": "game_leaderboard",
            "game_type": game_type,
            "game_name": game_name,
        }

    async def _handle_leaderboards_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle leaderboards menu selection."""
        if selection_id.startswith("lb_"):
            game_type = selection_id[3:]  # Remove "lb_" prefix
            self._show_leaderboard_types_menu(user, game_type)
        elif selection_id == "back":
            self._show_main_menu(user)

    async def _handle_leaderboard_types_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle leaderboard type selection."""
        game_type = state.get("game_type", "")
        game_name = state.get("game_name", "")

        # Built-in leaderboard types
        if selection_id == "type_wins":
            self._show_wins_leaderboard(user, game_type, game_name)
        elif selection_id == "type_rating":
            self._show_rating_leaderboard(user, game_type, game_name)
        elif selection_id == "type_total_score":
            self._show_total_score_leaderboard(user, game_type, game_name)
        elif selection_id == "type_high_score":
            self._show_high_score_leaderboard(user, game_type, game_name)
        elif selection_id == "type_games_played":
            self._show_games_played_leaderboard(user, game_type, game_name)
        elif selection_id == "back":
            self._show_leaderboards_menu(user)
        elif selection_id.startswith("type_"):
            # Custom leaderboard type - look up config from game class
            lb_id = selection_id[5:]  # Remove "type_" prefix
            game_class = get_game_class(game_type)
            if game_class:
                for config in game_class.get_leaderboard_types():
                    if config["id"] == lb_id:
                        self._show_custom_leaderboard(
                            user, game_type, game_name, config
                        )
                        return

    async def _handle_game_leaderboard_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle game leaderboard menu selection."""
        if selection_id == "back":
            game_type = state.get("game_type", "")
            game_name = state.get("game_name", "")
            self._show_leaderboard_types_menu(user, game_type)
        # Other selections (entries, header) are informational only

    # =========================================================================
    # My Stats menu
    # =========================================================================

    def _show_my_stats_menu(self, user: NetworkUser) -> None:
        """Show game selection menu for personal stats (only games user has played)."""
        categories = GameRegistry.get_by_category()
        items = []

        # Add only games where the user has stats
        for category_key in sorted(categories.keys()):
            for game_class in categories[category_key]:
                game_type = game_class.get_type()
                # Check if user has played this game
                game_results = self._get_game_results(game_type)
                has_stats = any(
                    p.player_id == user.uuid
                    for result in game_results
                    for p in result.player_results
                )
                if has_stats:
                    game_name = Localization.get(user.locale, game_class.get_name_key())
                    items.append(
                        MenuItem(text=game_name, id=f"stats_{game_type}")
                    )

        if not items:
            user.speak_l("my-stats-no-games")
            self._show_main_menu(user)
            return

        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "my_stats_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {"menu": "my_stats_menu"}

    def _show_my_game_stats(self, user: NetworkUser, game_type: str) -> None:
        """Show personal stats for a specific game."""
        from ..game_utils.stats_helpers import RatingHelper

        game_class = get_game_class(game_type)
        if not game_class:
            user.speak_l("game-type-not-found")
            return

        game_name = Localization.get(user.locale, game_class.get_name_key())
        game_results = self._get_game_results(game_type)

        # Calculate player's personal stats
        wins = 0
        losses = 0
        total_score = 0
        high_score = 0
        games_played = 0

        for result in game_results:
            winner_name = result.custom_data.get("winner_name")
            final_scores = result.custom_data.get("final_scores", {})
            final_light = result.custom_data.get("final_light", {})

            for p in result.player_results:
                if p.player_id == user.uuid:
                    games_played += 1
                    if winner_name == p.player_name:
                        wins += 1
                    else:
                        losses += 1

                    # Get score from final_scores or final_light (for Light Turret)
                    score = final_scores.get(p.player_name, 0)
                    if not score:
                        score = final_light.get(p.player_name, 0)
                    total_score += score
                    if score > high_score:
                        high_score = score

        if games_played == 0:
            user.speak_l("my-stats-no-data")
            return

        items = []
        # Basic stats
        winrate = round((wins / games_played * 100) if games_played > 0 else 0)

        items.append(
            MenuItem(
                text=Localization.get(user.locale, "my-stats-games-played", value=games_played),
                id="games_played",
            )
        )
        items.append(
            MenuItem(
                text=Localization.get(user.locale, "my-stats-wins", value=wins),
                id="wins",
            )
        )
        items.append(
            MenuItem(
                text=Localization.get(user.locale, "my-stats-losses", value=losses),
                id="losses",
            )
        )
        items.append(
            MenuItem(
                text=Localization.get(user.locale, "my-stats-winrate", value=winrate),
                id="winrate",
            )
        )

        # Score stats (if applicable)
        if total_score > 0:
            items.append(
                MenuItem(
                    text=Localization.get(user.locale, "my-stats-total-score", value=total_score),
                    id="total_score",
                )
            )
            items.append(
                MenuItem(
                    text=Localization.get(user.locale, "my-stats-high-score", value=high_score),
                    id="high_score",
                )
            )

        # Skill rating
        rating_helper = RatingHelper(self._db, game_type)
        rating = rating_helper.get_rating(user.uuid)
        if rating.mu != 25.0 or rating.sigma != 25.0 / 3:  # Non-default rating
            items.append(
                MenuItem(
                    text=Localization.get(
                        user.locale,
                        "my-stats-rating",
                        value=round(rating.ordinal),
                        mu=round(rating.mu, 1),
                        sigma=round(rating.sigma, 1),
                    ),
                    id="rating",
                )
            )
        else:
            items.append(
                MenuItem(
                    text=Localization.get(user.locale, "my-stats-no-rating"),
                    id="no_rating",
                )
            )

        # Game-specific stats from custom leaderboard configs
        self._add_custom_stats(user, game_class, game_results, items)

        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "my_game_stats",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {
            "menu": "my_game_stats",
            "game_type": game_type,
            "game_name": game_name,
        }

    def _add_custom_stats(
        self,
        user: NetworkUser,
        game_class,
        game_results: list,
        items: list,
    ) -> None:
        """Add game-specific custom stats from leaderboard configs."""
        for config in game_class.get_leaderboard_types():
            lb_id = config["id"]
            path = config.get("path")
            numerator_path = config.get("numerator")
            denominator_path = config.get("denominator")
            aggregate = config.get("aggregate", "sum")
            decimals = config.get("decimals", 0)

            # Extract values for this player from all game results
            values = []
            num_values = []
            denom_values = []

            for result in game_results:
                # Check if player participated in this game
                player_name = None
                for p in result.player_results:
                    if p.player_id == user.uuid:
                        player_name = p.player_name
                        break

                if not player_name:
                    continue

                custom_data = result.custom_data

                if path:
                    # Simple path extraction
                    resolved_path = path.replace("{player_name}", player_name)
                    resolved_path = resolved_path.replace("{player_id}", user.uuid)
                    value = self._extract_path_value(custom_data, resolved_path)
                    if value is not None:
                        values.append(value)
                elif numerator_path and denominator_path:
                    # Ratio calculation
                    num_path = numerator_path.replace("{player_name}", player_name)
                    denom_path = denominator_path.replace("{player_name}", player_name)
                    num_val = self._extract_path_value(custom_data, num_path)
                    denom_val = self._extract_path_value(custom_data, denom_path)
                    if num_val is not None and denom_val is not None:
                        num_values.append(num_val)
                        denom_values.append(denom_val)

            # Calculate aggregated value
            final_value = None
            if values:
                if aggregate == "sum":
                    final_value = sum(values)
                elif aggregate == "max":
                    final_value = max(values)
                elif aggregate == "avg":
                    final_value = sum(values) / len(values)
            elif num_values and denom_values:
                total_num = sum(num_values)
                total_denom = sum(denom_values)
                if total_denom > 0:
                    final_value = total_num / total_denom

            if final_value is not None:
                # Format the value
                if decimals > 0:
                    formatted_value = f"{final_value:.{decimals}f}"
                else:
                    formatted_value = str(round(final_value))

                # Get localization key
                loc_key = f"my-stats-{lb_id.replace('_', '-')}"
                # Try game-specific key first, fall back to generic
                text = Localization.get(user.locale, loc_key, value=formatted_value)
                if text == loc_key:
                    # Key not found, use leaderboard type name
                    type_key = f"leaderboard-type-{lb_id.replace('_', '-')}"
                    type_name = Localization.get(user.locale, type_key)
                    text = f"{type_name}: {formatted_value}"

                items.append(MenuItem(text=text, id=f"custom_{lb_id}"))

    def _extract_path_value(self, data: dict, path: str) -> float | None:
        """Extract a value from nested dict using dot notation path."""
        parts = path.split(".")
        current = data
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return None
        if isinstance(current, (int, float)):
            return float(current)
        return None

    async def _handle_my_stats_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle my stats game selection."""
        if selection_id == "back":
            self._show_main_menu(user)
        elif selection_id.startswith("stats_"):
            game_type = selection_id[6:]  # Remove "stats_" prefix
            self._show_my_game_stats(user, game_type)

    async def _handle_my_game_stats_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle my game stats menu selection."""
        if selection_id == "back":
            self._show_my_stats_menu(user)
        # Other selections (stats entries) are informational only

    def on_table_destroy(self, table) -> None:
        """Handle table destruction. Called by TableManager."""
        if not table.game:
            return
        # Return all human players to main menu
        for player in table.game.players:
            if not player.is_bot:
                player_user = self._users.get(player.name)
                if player_user:
                    self._show_main_menu(player_user)

    def on_game_result(self, result) -> None:
        """Handle game result persistence. Called by Table when a game finishes."""
        from ..game_utils.game_result import GameResult

        if not isinstance(result, GameResult):
            return

        # Save to database
        self._db.save_game_result(
            game_type=result.game_type,
            timestamp=result.timestamp,
            duration_ticks=result.duration_ticks,
            players=[
                (p.player_id, p.player_name, p.is_bot)
                for p in result.player_results
            ],
            custom_data=result.custom_data,
        )

    def on_table_save(self, table, username: str) -> None:
        """Handle table save request. Called by TableManager."""
        import json
        from datetime import datetime

        game = table.game
        if not game:
            return

        # Generate save name
        save_name = f"{game.get_name()} - {datetime.now():%Y-%m-%d %H:%M}"

        # Get game JSON
        game_json = game.to_json()

        # Build members list (includes bot status)
        members_data = []
        for player in game.players:
            members_data.append(
                {
                    "username": player.name,
                    "is_bot": player.is_bot,
                }
            )
        members_json = json.dumps(members_data)

        # Save to database
        self._db.save_user_table(
            username=username,
            save_name=save_name,
            game_type=table.game_type,
            game_json=game_json,
            members_json=members_json,
        )

        # Broadcast save message and destroy the table
        game.broadcast_l("table-saved-destroying")
        game.destroy()

    async def _handle_keybind(self, client: ClientConnection, packet: dict) -> None:
        """Handle keybind press."""
        username = client.username
        if not username:
            return

        user = self._users.get(username)
        table = self._tables.find_user_table(username)
        if table and table.game and user:
            player = table.game.get_player_by_id(user.uuid)
            if player:
                table.game.handle_event(player, packet)
                # Check if player left the game (user replaced by bot or removed)
                game_user = table.game._users.get(user.uuid)
                if game_user is not user:
                    table.remove_member(username)
                    self._show_main_menu(user)

    async def _handle_editbox(self, client: ClientConnection, packet: dict) -> None:
        """Handle editbox submission."""
        username = client.username
        if not username:
            return

        user = self._users.get(username)
        table = self._tables.find_user_table(username)
        if table and table.game and user:
            player = table.game.get_player_by_id(user.uuid)
            if player:
                table.game.handle_event(player, packet)
                # Check if player left the game (user replaced by bot or removed)
                game_user = table.game._users.get(user.uuid)
                if game_user is not user:
                    table.remove_member(username)
                    self._show_main_menu(user)

    async def _handle_chat(self, client: ClientConnection, packet: dict) -> None:
        """Handle chat message."""
        username = client.username
        if not username:
            return

        convo = packet.get("convo", "table")
        message = packet.get("message", "")
        language = packet.get("language", "Other")

        if convo == "table":
            table = self._tables.find_user_table(username)
            if table:
                for member_name in [m.username for m in table.members]:
                    user = self._users.get(member_name)
                    if user:
                        await user.connection.send(
                            {
                                "type": "chat",
                                "convo": "table",
                                "sender": username,
                                "message": message,
                                "language": language,
                            }
                        )
        elif convo == "global":
            # Broadcast to all users
            if self._ws_server:
                await self._ws_server.broadcast(
                    {
                        "type": "chat",
                        "convo": "global",
                        "sender": username,
                        "message": message,
                        "language": language,
                    }
                )

    async def _handle_ping(self, client: ClientConnection) -> None:
        """Handle ping request - respond immediately with pong."""
        await client.send({"type": "pong"})


async def run_server(
    host: str = "0.0.0.0",
    port: int = 8000,
    ssl_cert: str | Path | None = None,
    ssl_key: str | Path | None = None,
) -> None:
    """Run the server.

    Args:
        host: Host address to bind to
        port: Port number to listen on
        ssl_cert: Path to SSL certificate file (for WSS support)
        ssl_key: Path to SSL private key file (for WSS support)
    """
    server = Server(host=host, port=port, ssl_cert=ssl_cert, ssl_key=ssl_key)
    await server.start()

    try:
        # Run forever
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        await server.stop()
