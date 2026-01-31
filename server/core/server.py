"""Main server class that ties everything together."""

import asyncio
import logging
import os
import shutil
import sys
import time
from collections import deque
from getpass import getpass
from pathlib import Path

import json
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python <3.11 fallback when available
    import tomli as tomllib  # type: ignore[import]

from .tick import TickScheduler, load_server_config
from .administration import AdministrationMixin
from .virtual_bots import VirtualBotManager
from ..network.websocket_server import WebSocketServer, ClientConnection
from ..persistence.database import Database
from ..auth.auth import AuthManager, AuthResult
from ..tables.manager import TableManager
from ..users.network_user import NetworkUser
from ..users.base import MenuItem, EscapeBehavior, TrustLevel
from ..users.preferences import UserPreferences, DiceKeepingStyle
from ..games.registry import GameRegistry, get_game_class
from ..messages.localization import Localization


VERSION = "11.0.0"
BOOTSTRAP_WARNING_ENV = "PLAYPALACE_SUPPRESS_BOOTSTRAP_WARNING"

DEFAULT_USERNAME_MIN_LENGTH = 3
DEFAULT_USERNAME_MAX_LENGTH = 32
DEFAULT_PASSWORD_MIN_LENGTH = 8
DEFAULT_PASSWORD_MAX_LENGTH = 128
DEFAULT_WS_MAX_MESSAGE_BYTES = 1_048_576  # 1 MB
DEFAULT_LOGIN_ATTEMPTS_PER_MINUTE = 5
DEFAULT_LOGIN_FAILURES_PER_MINUTE = 3
DEFAULT_REGISTRATION_ATTEMPTS_PER_MINUTE = 2
LOGIN_RATE_WINDOW_SECONDS = 60
REGISTRATION_RATE_WINDOW_SECONDS = 60


def _coerce_bool(value: Any, default: bool) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"1", "true", "yes", "on"}:
            return True
        if lowered in {"0", "false", "no", "off"}:
            return False
    if isinstance(value, (int, float)):
        return bool(value)
    return default

# Default paths based on module location
_MODULE_DIR = Path(__file__).parent.parent
_DEFAULT_LOCALES_DIR = _MODULE_DIR / "locales"


class Server(AdministrationMixin):
    """
    Main PlayPalace v11 server.

    Coordinates all components: network, auth, tables, games, and persistence.
    """

    def __init__(
        self,
        host: str = "::",
        port: int = 8000,
        db_path: str = "playpalace.db",
        locales_dir: str | Path | None = None,
        ssl_cert: str | Path | None = None,
        ssl_key: str | Path | None = None,
        config_path: str | Path | None = None,
    ):
        self.host = host
        self.port = port
        self._ssl_cert = ssl_cert
        self._ssl_key = ssl_key

        if db_path == "playpalace.db":
            db_path = str(_MODULE_DIR / "playpalace.db")

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

        # Virtual bot manager
        self._virtual_bots = VirtualBotManager(self)

        # Credential limits (overridable via config)
        self._username_min_length = DEFAULT_USERNAME_MIN_LENGTH
        self._username_max_length = DEFAULT_USERNAME_MAX_LENGTH
        self._password_min_length = DEFAULT_PASSWORD_MIN_LENGTH
        self._password_max_length = DEFAULT_PASSWORD_MAX_LENGTH
        self._ws_max_message_size = DEFAULT_WS_MAX_MESSAGE_BYTES
        self._config_path = Path(config_path) if config_path else _MODULE_DIR / "config.toml"
        self._allow_insecure_ws = False
        self._login_ip_limit = DEFAULT_LOGIN_ATTEMPTS_PER_MINUTE
        self._login_user_limit = DEFAULT_LOGIN_FAILURES_PER_MINUTE
        self._registration_ip_limit = DEFAULT_REGISTRATION_ATTEMPTS_PER_MINUTE
        self._login_ip_window = LOGIN_RATE_WINDOW_SECONDS
        self._login_user_window = LOGIN_RATE_WINDOW_SECONDS
        self._registration_ip_window = REGISTRATION_RATE_WINDOW_SECONDS
        self._login_attempts_ip: dict[str, deque[float]] = {}
        self._login_attempts_user: dict[str, deque[float]] = {}
        self._registration_attempts_ip: dict[str, deque[float]] = {}
        self._load_config_settings()

        # Initialize localization
        if locales_dir is None:
            resolved_locales = _DEFAULT_LOCALES_DIR
        else:
            provided_locales = Path(locales_dir)
            if not provided_locales.is_absolute():
                candidate = _MODULE_DIR / provided_locales
                if candidate.exists():
                    provided_locales = candidate
            resolved_locales = provided_locales
        Localization.init(resolved_locales)
        Localization.preload_bundles()

    async def start(self) -> None:
        """Start the server."""
        # Load server configuration early to surface config errors before DB/network init
        server_config = load_server_config(self._config_path)
        tick_interval_ms = server_config.get("tick_interval_ms")
        if tick_interval_ms is not None:
            try:
                tick_interval_ms = int(tick_interval_ms)
            except (TypeError, ValueError) as exc:
                print(
                    f"ERROR: Invalid tick_interval_ms value '{tick_interval_ms}' in server configuration: {exc}",
                    file=sys.stderr,
                )
                raise SystemExit(1) from exc
            if tick_interval_ms < 1:
                print(
                    "ERROR: tick_interval_ms must be at least 1 millisecond.",
                    file=sys.stderr,
                )
                raise SystemExit(1)

        # Enforce transport requirements before bringing up listeners
        self._validate_transport_security()

        # Connect to database
        self._db.connect()
        self._auth = AuthManager(self._db)

        # Initialize trust levels for users
        promoted_user = self._db.initialize_trust_levels()
        if promoted_user:
            print(f"User '{promoted_user}' has been promoted to server owner (trust level 3).")
        self._warn_if_no_users()

        # Load existing tables
        self._load_tables()

        # Initialize virtual bots
        try:
            self._virtual_bots.load_config()
        except ValueError as exc:
            print(f"ERROR: Invalid virtual bot configuration: {exc}", file=sys.stderr)
            raise SystemExit(1) from exc
        loaded = self._virtual_bots.load_state()
        if loaded > 0:
            print(f"Restored {loaded} virtual bots from previous session.")

        # Start WebSocket server
        self._ws_server = WebSocketServer(
            host=self.host,
            port=self.port,
            on_connect=self._on_client_connect,
            on_disconnect=self._on_client_disconnect,
            on_message=self._on_client_message,
            ssl_cert=self._ssl_cert,
            ssl_key=self._ssl_key,
            max_message_size=self._ws_max_message_size,
        )
        await self._ws_server.start()
        if not self._ssl_cert:
            print(
                "WARNING: Running without TLS (ws://). Credentials will be sent in plaintext."
            )
        if self._ws_max_message_size != DEFAULT_WS_MAX_MESSAGE_BYTES:
            print(f"Max inbound websocket message size: {self._ws_max_message_size} bytes")

        # Start tick scheduler
        self._tick_scheduler = TickScheduler(self._on_tick, tick_interval_ms)
        await self._tick_scheduler.start()
        # Tick interval message suppressed by default (configurable via config.toml).

        protocol = "wss" if self._ssl_cert else "ws"
        print(f"Server running on {protocol}://{self.host}:{self.port}")

    async def stop(self) -> None:
        """Stop the server."""
        print("Stopping server...")

        # Save all tables
        self._save_tables()

        # Save virtual bot state (they persist across restarts)
        self._virtual_bots.save_state()

        # Stop tick scheduler
        if self._tick_scheduler:
            await self._tick_scheduler.stop()

        # Stop WebSocket server
        if self._ws_server:
            await self._ws_server.stop()

        # Close database
        self._db.close()

        print("Server stopped.")

    def _load_config_settings(self) -> None:
        """Load credential and network limits from config.toml if available."""
        path_obj = Path(self._config_path) if self._config_path is not None else None
        if path_obj is None or not path_obj.exists():
            return

        try:
            with open(path_obj, "rb") as f:
                config: dict[str, Any] = tomllib.load(f)
        except (OSError, tomllib.TOMLDecodeError) as exc:  # pragma: no cover - logging only
            print(f"Failed to load config from {path_obj}: {exc}")
            return

        auth_cfg = config.get("auth")
        if not isinstance(auth_cfg, dict):
            auth_cfg = {}

        def _read_limit(source: dict[str, Any], key: str, current: int, minimum: int = 1) -> int:
            value = source.get(key)
            if value is None:
                return current
            try:
                value_int = int(value)
            except (TypeError, ValueError):
                return current
            return max(minimum, value_int)

        if auth_cfg:
            self._username_min_length = _read_limit(auth_cfg, "username_min_length", self._username_min_length)
            self._username_max_length = _read_limit(
                auth_cfg, "username_max_length", self._username_max_length, self._username_min_length
            )
            self._password_min_length = _read_limit(auth_cfg, "password_min_length", self._password_min_length)
            self._password_max_length = _read_limit(
                auth_cfg, "password_max_length", self._password_max_length, self._password_min_length
            )

            # Ensure ranges are sane
            if self._username_min_length > self._username_max_length:
                self._username_max_length = self._username_min_length
            if self._password_min_length > self._password_max_length:
                self._password_max_length = self._password_min_length

        net_cfg = config.get("network")
        if isinstance(net_cfg, dict):
            max_bytes = _read_limit(net_cfg, "max_message_bytes", self._ws_max_message_size, minimum=1)
            self._ws_max_message_size = max_bytes
            self._allow_insecure_ws = _coerce_bool(
                net_cfg.get("allow_insecure_ws"), self._allow_insecure_ws
            )

        rate_cfg = auth_cfg.get("rate_limits") if isinstance(auth_cfg, dict) else None
        if isinstance(rate_cfg, dict):
            self._login_ip_limit = _read_limit(rate_cfg, "login_per_minute", self._login_ip_limit, minimum=0)
            self._login_user_limit = _read_limit(
                rate_cfg, "login_failures_per_minute", self._login_user_limit, minimum=0
            )
            self._registration_ip_limit = _read_limit(
                rate_cfg, "registration_per_minute", self._registration_ip_limit, minimum=0
            )
            self._login_ip_window = _read_limit(
                rate_cfg, "login_window_seconds", self._login_ip_window, minimum=1
            )
            self._login_user_window = _read_limit(
                rate_cfg, "login_failure_window_seconds", self._login_user_window, minimum=1
            )
            self._registration_ip_window = _read_limit(
                rate_cfg, "registration_window_seconds", self._registration_ip_window, minimum=1
            )


    def _validate_transport_security(self) -> None:
        if self._allow_insecure_ws and (self._ssl_cert or self._ssl_key):
            print(
                "ERROR: allow_insecure_ws=true cannot be combined with SSL certificate or key. "
                "Remove the certificate settings or disable insecure mode.",
                file=sys.stderr,
            )
            raise SystemExit(1)

        if not self._allow_insecure_ws and (not self._ssl_cert or not self._ssl_key):
            print(
                "ERROR: TLS is required. Provide --ssl-cert and --ssl-key "
                "or set [network].allow_insecure_ws to true.",
                file=sys.stderr,
            )
            raise SystemExit(1)

    @staticmethod
    def _get_client_ip(client: ClientConnection) -> str:
        if not client.address:
            return "unknown"
        return client.address.split(":")[0]

    @staticmethod
    def _sanitize_credentials(username: str | None, password: str | None) -> tuple[str, str]:
        """Normalize credential fields before validation."""
        username = (username or "").strip()
        password = password or ""
        return username, password

    def _validate_credentials(self, username: str, password: str) -> tuple[str, str, str | None]:
        """Validate username/password lengths and return an error message if invalid."""
        username, password = self._sanitize_credentials(username, password)

        if len(username) < self._username_min_length or len(username) > self._username_max_length:
            return username, password, (
                f"Username must be between {self._username_min_length} and {self._username_max_length} characters."
            )

        if len(password) < self._password_min_length or len(password) > self._password_max_length:
            return username, password, (
                f"Password must be between {self._password_min_length} and {self._password_max_length} characters."
            )

        return username, password, None

    @staticmethod
    async def _send_credential_error(client: ClientConnection, message: str) -> None:
        """Send a credential validation error and disconnect the client."""
        await client.send({"type": "play_sound", "name": "accounterror.ogg"})
        await client.send({"type": "speak", "text": message})
        await client.send(
            {
                "type": "disconnect",
                "reconnect": False,
                "show_message": True,
                "return_to_login": True,
            }
        )

    def _allow_attempt(self, bucket: dict[str, deque[float]], key: str, limit: int, window: float, now: float) -> bool:
        if limit <= 0:
            return True
        dq = bucket.setdefault(key, deque())
        while dq and now - dq[0] > window:
            dq.popleft()
        if len(dq) >= limit:
            return False
        dq.append(now)
        return True

    def _get_attempt_count(self, bucket: dict[str, deque[float]], key: str, window: float, now: float) -> int:
        dq = bucket.get(key)
        if not dq:
            return 0
        while dq and now - dq[0] > window:
            dq.popleft()
        if not dq:
            bucket.pop(key, None)
            return 0
        return len(dq)

    def _record_attempt(self, bucket: dict[str, deque[float]], key: str, now: float) -> None:
        dq = bucket.setdefault(key, deque())
        dq.append(now)

    def _check_login_rate_limit(self, client_ip: str, username: str) -> str | None:
        now = time.monotonic()
        if not self._allow_attempt(
            self._login_attempts_ip, client_ip, self._login_ip_limit, self._login_ip_window, now
        ):
            return "Too many login attempts from this address. Please wait and try again."
        if username:
            failures = self._get_attempt_count(self._login_attempts_user, username, self._login_user_window, now)
            if self._login_user_limit > 0 and failures >= self._login_user_limit:
                return "Too many failed login attempts for this username. Please wait and try again."
        return None

    def _record_login_failure(self, username: str) -> None:
        if not username or self._login_user_limit <= 0:
            return
        now = time.monotonic()
        self._get_attempt_count(self._login_attempts_user, username, self._login_user_window, now)
        self._record_attempt(self._login_attempts_user, username, now)

    def _check_registration_rate_limit(self, client_ip: str) -> str | None:
        now = time.monotonic()
        if not self._allow_attempt(
            self._registration_attempts_ip,
            client_ip,
            self._registration_ip_limit,
            self._registration_ip_window,
            now,
        ):
            return "Too many registration attempts from this address. Please wait and try again."
        return None

    def _warn_if_no_users(self) -> None:
        """Print a warning if no user accounts exist yet."""
        if os.environ.get(BOOTSTRAP_WARNING_ENV):
            return
        try:
            if self._db.get_user_count() > 0:
                return
        except Exception:
            return

        print(
            "WARNING: No user accounts exist. Run "
            "`uv run python -m server.cli bootstrap-owner --username <name>` "
            "to create an initial administrator before exposing this server on the network. "
            f"Set {BOOTSTRAP_WARNING_ENV}=1 to suppress this warning for CI or local testing."
        )

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

        # Tick virtual bots (handle state transitions)
        self._virtual_bots.on_tick()

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
        username = client.username or "unknown"
        print(f"Client disconnected: {username}@{client.address}")
        if client.username:
            username = client.username
            table = self._tables.find_user_table(username)
            # Check user status before cleanup
            user = self._users.get(username)

            if table and user:
                if table.game:
                    player = table.game.get_player_by_id(user.uuid)
                    if player:
                        table.game._perform_leave_game(player)
                # Keep membership for rejoin unless this was the last member
                if len(table.members) <= 1:
                    table.remove_member(username)

            # Only broadcast offline if user was approved and not banned
            if user and user.approved and user.trust_level != TrustLevel.BANNED:
                is_admin = user.trust_level.value >= TrustLevel.ADMIN.value
                offline_sound = "offlineadmin.ogg" if is_admin else "offline.ogg"
                self._broadcast_presence_l("user-offline", username, offline_sound)

            # Clean up user state
            self._users.pop(username, None)
            self._user_states.pop(username, None)

    def _broadcast_presence_l(
        self, message_id: str, player_name: str, sound: str
    ) -> None:
        """Broadcast a localized presence announcement to all approved online users with sound."""
        for username, user in self._users.items():
            if not user.approved:
                continue  # Don't send broadcasts to unapproved users
            user.speak_l(message_id, buffer="activity", player=player_name)
            user.play_sound(sound)

    def _broadcast_admin_announcement(self, admin_name: str) -> None:
        """Broadcast an admin announcement to all approved online users."""
        for username, user in self._users.items():
            if not user.approved:
                continue  # Don't send broadcasts to unapproved users
            user.speak_l("user-is-admin", buffer="activity", player=admin_name)

    def _broadcast_server_owner_announcement(self, owner_name: str) -> None:
        """Broadcast a server owner announcement to all approved online users."""
        for username, user in self._users.items():
            if not user.approved:
                continue  # Don't send broadcasts to unapproved users
            user.speak_l("user-is-server-owner", buffer="activity", player=owner_name)

    def _broadcast_table_created(self, host_name: str, game_name: str) -> None:
        """Broadcast a table creation announcement to all approved online users."""
        for username, user in self._users.items():
            if not user.approved:
                continue  # Don't send broadcasts to unapproved users
            user.speak_l("table-created", buffer="activity", host=host_name, game=game_name)
            user.play_sound("table_created.ogg")

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
        elif packet_type == "ping":
            # Always allow ping to keep connection alive
            await self._handle_ping(client)
        elif packet_type == "menu":
            # Allow menu selections for all authenticated users (including unapproved)
            await self._handle_menu(client, packet)
        else:
            # For all other packets, check if user is approved
            user = self._users.get(client.username)
            if user and not user.approved:
                # Unapproved users can only ping and use menus - drop all other packets
                return

            if packet_type == "keybind":
                await self._handle_keybind(client, packet)
            elif packet_type == "editbox":
                await self._handle_editbox(client, packet)
            elif packet_type == "chat":
                await self._handle_chat(client, packet)
            elif packet_type == "list_online":
                await self._handle_list_online(client)
            elif packet_type == "list_online_with_games":
                await self._handle_list_online_with_games(client)

    async def _handle_authorize(self, client: ClientConnection, packet: dict) -> None:
        """Handle authorization packet."""
        username_raw = packet.get("username", "")
        password_raw = packet.get("password", "")
        locale = packet.get("locale", "en")

        username, password, error = self._validate_credentials(username_raw, password_raw)
        if error:
            await self._send_credential_error(client, error)
            return

        client_ip = self._get_client_ip(client)
        throttle_message = self._check_login_rate_limit(client_ip, username)
        if throttle_message:
            await self._send_credential_error(client, throttle_message)
            return

        # Try to authenticate or register
        auth_result = self._auth.authenticate(username, password)
        if auth_result != AuthResult.SUCCESS:
            if auth_result == AuthResult.WRONG_PASSWORD:
                self._record_login_failure(username)
                # Username exists but password is wrong - show error dialog
                error_message = Localization.get(locale, "incorrect-password")
                await client.send({"type": "play_sound", "name": "accounterror.ogg"})
                await client.send({"type": "speak", "text": error_message})
                await client.send({
                    "type": "disconnect",
                    "reconnect": False,
                    "show_message": True,
                    "return_to_login": True,
                })
                return

            # User not found - check if this will be a new user that needs approval
            needs_approval = self._db.get_user_count() > 0

            # Try to register
            if not self._auth.register(username, password):
                self._record_login_failure(username)
                # Registration failed (shouldn't happen if user not found, but handle anyway)
                error_message = Localization.get(locale, "incorrect-username")
                await client.send({"type": "play_sound", "name": "accounterror.ogg"})
                await client.send({"type": "speak", "text": error_message})
                await client.send({
                    "type": "disconnect",
                    "reconnect": False,
                    "show_message": True,
                    "return_to_login": True,
                })
                return

            # New user registered - notify admins if approval is needed
            if needs_approval:
                self._notify_admins("account-request", "accountrequest.ogg")

        # Check if user is already logged in
        if username in self._users:
            error_message = Localization.get(locale, "already-logged-in")
            await client.send({"type": "play_sound", "name": "accounterror.ogg"})
            await client.send({"type": "speak", "text": error_message})
            await client.send({
                "type": "disconnect",
                "reconnect": False,
                "show_message": True,
                "return_to_login": True,
            })
            return

        # Authentication successful
        client.username = username
        client.authenticated = True

        # Create network user with preferences and persistent UUID
        user_record = self._auth.get_user(username)
        locale = user_record.locale if user_record else "en"
        user_uuid = user_record.uuid if user_record else None
        trust_level = user_record.trust_level if user_record else TrustLevel.USER
        is_approved = user_record.approved if user_record else False
        preferences = UserPreferences()
        if user_record and user_record.preferences_json:
            try:
                prefs_data = json.loads(user_record.preferences_json)
                preferences = UserPreferences.from_dict(prefs_data)
            except (json.JSONDecodeError, KeyError):
                pass  # Use defaults on error
        user = NetworkUser(
            username, locale, client, uuid=user_uuid, preferences=preferences,
            trust_level=trust_level, approved=is_approved
        )
        self._users[username] = user

        # Send success response
        await client.send(
            {
                "type": "authorize_success",
                "username": username,
                "version": VERSION,
            }
        )
        print(f"Client authorized: {username}@{client.address}")

        # Send game list
        await self._send_game_list(client)

        # Check if user is banned
        if user.trust_level == TrustLevel.BANNED:
            user.play_sound("accountban.ogg")
            user.speak_l("account-banned", buffer="activity")
            for msg in user.get_queued_messages():
                await user.connection.send(msg)
            await user.connection.send({
                "type": "disconnect",
                "reconnect": False,
                "show_message": True,
            })
            return

        # Check if user is approved
        if not user.approved:
            # User needs approval - show limited main menu
            user.speak_l("waiting-for-approval", buffer="activity")
            self._show_main_menu(user)
            return

        # Broadcast online announcement (only for approved, non-banned users)
        online_sound = "onlineadmin.ogg" if trust_level.value >= TrustLevel.ADMIN.value else "online.ogg"
        self._broadcast_presence_l("user-online", username, online_sound)

        # If user is server owner, announce that; otherwise if admin, announce that
        if trust_level.value >= TrustLevel.SERVER_OWNER.value:
            self._broadcast_server_owner_announcement(username)
        elif trust_level.value >= TrustLevel.ADMIN.value:
            self._broadcast_admin_announcement(username)

        # Notify admin of pending account approvals (excluding banned users)
        if trust_level.value >= TrustLevel.ADMIN.value:
            pending_users = self._db.get_pending_users(exclude_banned=True)
            if pending_users:
                user.speak_l("account-request", buffer="activity")
                user.play_sound("accountrequest.ogg")

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
        username_raw = packet.get("username", "")
        password_raw = packet.get("password", "")
        # email and bio are sent but not stored yet

        username, password, error = self._validate_credentials(username_raw, password_raw)
        if error:
            await client.send({"type": "speak", "text": error})
            return

        client_ip = self._get_client_ip(client)
        throttle_message = self._check_registration_rate_limit(client_ip)
        if throttle_message:
            await client.send({"type": "speak", "text": throttle_message})
            return

        # All self-registered users require approval.
        needs_approval = True

        # Try to register the user
        if self._auth.register(username, password):
            await client.send({
                "type": "speak",
                "text": "Registration successful! Your account is waiting for approval."
            })
            # Notify admins of new account request (only if user needs approval)
            if needs_approval:
                self._notify_admins("account-request", "accountrequest.ogg")
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
        items = []
        if user.approved:
            # Full menu for approved users
            items = [
                MenuItem(text=Localization.get(user.locale, "play"), id="play"),
                MenuItem(
                    text=Localization.get(user.locale, "view-active-tables"),
                    id="active_tables",
                ),
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
            ]
            # Add administration menu for admins
            if user.trust_level.value >= TrustLevel.ADMIN.value:
                items.append(
                    MenuItem(text=Localization.get(user.locale, "administration"), id="administration")
                )
        else:
            # Limited menu for users waiting for approval
            items = [
                MenuItem(
                    text=Localization.get(user.locale, "leaderboards"), id="leaderboards"
                ),
                MenuItem(text=Localization.get(user.locale, "options"), id="options"),
            ]
        items.append(MenuItem(text=Localization.get(user.locale, "logout"), id="logout"))
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
            game_count = len(categories.get(category_key, []))
            items.append(
                MenuItem(
                    text=f"{category_name} ({game_count})",
                    id=f"category_{category_key}",
                )
            )
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
            member_count = len(table.members)
            member_names = [
                member.username
                for member in table.members
                if member.username != table.host
            ]
            members_str = Localization.format_list_and(user.locale, member_names)
            if member_count == 1:
                listing_key = "table-listing-one"
            elif member_names:
                listing_key = "table-listing-with"
            else:
                listing_key = "table-listing"
            items.append(
                MenuItem(
                    text=Localization.get(
                        user.locale,
                        listing_key,
                        host=table.host,
                        count=member_count,
                        members=members_str,
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

    def _show_active_tables_menu(self, user: NetworkUser) -> None:
        """Show available tables across all games."""
        tables = self._tables.get_waiting_tables()
        if not tables:
            user.speak_l("no-active-tables")
            self._show_main_menu(user)
            return
        items: list[MenuItem] = []
        for table in tables:
            game_class = get_game_class(table.game_type)
            game_name = (
                Localization.get(user.locale, game_class.get_name_key())
                if game_class
                else table.game_type
            )
            member_count = len(table.members)
            member_names = [
                member.username
                for member in table.members
                if member.username != table.host
            ]
            members_str = Localization.format_list_and(user.locale, member_names)
            if member_count == 1:
                listing_key = "table-listing-game-one"
            elif member_names:
                listing_key = "table-listing-game-with"
            else:
                listing_key = "table-listing-game"
            items.append(
                MenuItem(
                    text=Localization.get(
                        user.locale,
                        listing_key,
                        game=game_name,
                        host=table.host,
                        count=member_count,
                        members=members_str,
                    ),
                    id=f"table_{table.table_id}",
                )
            )
        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))
        user.show_menu(
            "active_tables_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {"menu": "active_tables_menu"}

    # Dice keeping style display names
    DICE_KEEPING_STYLES = {
        DiceKeepingStyle.PLAYPALACE: "dice-keeping-style-indexes",
        DiceKeepingStyle.QUENTIN_C: "dice-keeping-style-values",
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
        style_key = self.DICE_KEEPING_STYLES.get(
            prefs.dice_keeping_style, "dice-keeping-style-indexes"
        )
        dice_style_name = Localization.get(user.locale, style_key)

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
        elif current_menu == "active_tables_menu":
            await self._handle_active_tables_selection(user, selection_id)
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
        elif current_menu == "online_users":
            self._restore_previous_menu(user, state)
        elif current_menu == "admin_menu":
            await self._handle_admin_menu_selection(user, selection_id)
        elif current_menu == "account_approval_menu":
            await self._handle_account_approval_selection(user, selection_id)
        elif current_menu == "pending_user_actions_menu":
            await self._handle_pending_user_actions_selection(user, selection_id, state)
        elif current_menu == "promote_admin_menu":
            await self._handle_promote_admin_selection(user, selection_id)
        elif current_menu == "demote_admin_menu":
            await self._handle_demote_admin_selection(user, selection_id)
        elif current_menu == "promote_confirm_menu":
            await self._handle_promote_confirm_selection(user, selection_id, state)
        elif current_menu == "demote_confirm_menu":
            await self._handle_demote_confirm_selection(user, selection_id, state)
        elif current_menu == "broadcast_choice_menu":
            await self._handle_broadcast_choice_selection(user, selection_id, state)
        elif current_menu == "transfer_ownership_menu":
            await self._handle_transfer_ownership_selection(user, selection_id)
        elif current_menu == "transfer_ownership_confirm_menu":
            await self._handle_transfer_ownership_confirm_selection(user, selection_id, state)
        elif current_menu == "transfer_broadcast_choice_menu":
            await self._handle_transfer_broadcast_choice_selection(user, selection_id, state)
        elif current_menu == "ban_user_menu":
            await self._handle_ban_user_selection(user, selection_id)
        elif current_menu == "unban_user_menu":
            await self._handle_unban_user_selection(user, selection_id)
        elif current_menu == "ban_confirm_menu":
            await self._handle_ban_confirm_selection(user, selection_id, state)
        elif current_menu == "unban_confirm_menu":
            await self._handle_unban_confirm_selection(user, selection_id, state)
        elif current_menu == "virtual_bots_menu":
            await self._handle_virtual_bots_selection(user, selection_id)
        elif current_menu == "virtual_bots_clear_confirm_menu":
            await self._handle_virtual_bots_clear_confirm_selection(user, selection_id)

    def _ensure_user_approved(self, user: NetworkUser) -> bool:
        """Return True if user is approved or admin/server owner; otherwise show approval notice."""
        if user.approved:
            return True
        if user.trust_level.value >= TrustLevel.ADMIN.value:
            return True
        user.speak_l("waiting-for-approval", buffer="activity")
        self._show_main_menu(user)
        return False

    async def _handle_main_menu_selection(
        self, user: NetworkUser, selection_id: str
    ) -> None:
        """Handle main menu selection."""
        if selection_id == "play":
            if not self._ensure_user_approved(user):
                return
            self._show_categories_menu(user)
        elif selection_id == "active_tables":
            if not self._ensure_user_approved(user):
                return
            self._show_active_tables_menu(user)
        elif selection_id == "saved_tables":
            if not self._ensure_user_approved(user):
                return
            self._show_saved_tables_menu(user)
        elif selection_id == "leaderboards":
            if not self._ensure_user_approved(user):
                return
            self._show_leaderboards_menu(user)
        elif selection_id == "my_stats":
            if not self._ensure_user_approved(user):
                return
            self._show_my_stats_menu(user)
        elif selection_id == "options":
            self._show_options_menu(user)
        elif selection_id == "administration":
            if user.trust_level.value >= TrustLevel.ADMIN.value:
                self._show_admin_menu(user)
        elif selection_id == "logout":
            user.speak_l("goodbye", buffer="activity")
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
        for style, name_key in self.DICE_KEEPING_STYLES.items():
            prefix = "* " if style == current_style else ""
            name = Localization.get(user.locale, name_key)
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
            style_key = self.DICE_KEEPING_STYLES.get(style, "dice-keeping-style-indexes")
            style_name = Localization.get(user.locale, style_key)
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

                # Broadcast table creation to all users
                game_name = state.get("game_name", game_type)
                self._broadcast_table_created(user.username, game_name)

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
                self._auto_join_table(user, table, game_type)
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

    async def _handle_active_tables_selection(
        self, user: NetworkUser, selection_id: str
    ) -> None:
        """Handle active tables menu selection."""
        if selection_id.startswith("table_"):
            table_id = selection_id[6:]
            table = self._tables.get_table(table_id)
            if table:
                self._auto_join_table(user, table, table.game_type)
            else:
                user.speak_l("table-not-exists")
                self._show_active_tables_menu(user)
        elif selection_id == "back":
            self._show_main_menu(user)

    def _auto_join_table(
        self, user: NetworkUser, table: "Table", game_type: str
    ) -> None:
        """Automatically join a table as player or spectator.

        Joins as player if:
        - Game has not started yet (status is "waiting")
        - Game has room for more players (less than max_players)

        Otherwise joins as spectator.
        """
        game = table.game
        if not game:
            user.speak_l("table-not-exists")
            self._show_tables_menu(user, game_type)
            return

        table_id = table.table_id

        # Determine if user can join as player
        can_join_as_player = (
            game.status != "playing"
            and len(game.players) < game.get_max_players()
        )

        if can_join_as_player:
            # Join as player
            table.add_member(user.username, user, as_spectator=False)
            game.add_player(user.username, user)
            game.broadcast_l("table-joined", player=user.username)
            game.broadcast_sound("join.ogg")
            game.rebuild_all_menus()
        else:
            # Join as spectator
            table.add_member(user.username, user, as_spectator=True)
            game.add_spectator(user.username, user)
            user.speak_l("spectator-joined", host=table.host)
            game.broadcast_l("now-spectating", player=user.username)
            game.broadcast_sound("join_spectator.ogg")
            game.rebuild_all_menus()

        self._user_states[user.username] = {"menu": "in_game", "table_id": table_id}

    def _return_from_join_menu(self, user: NetworkUser, state: dict) -> None:
        """Return to the appropriate tables menu after join."""
        if state.get("return_menu") == "active_tables_menu":
            self._show_active_tables_menu(user)
        else:
            self._show_tables_menu(user, state.get("game_type", ""))

    async def _handle_join_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle join menu selection."""
        table_id = state.get("table_id")
        table = self._tables.get_table(table_id)

        if not table or not table.game:
            user.speak_l("table-not-exists")
            self._return_from_join_menu(user, state)
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
                    game.add_spectator(user.username, user)
                    user.speak_l("spectator-joined", host=table.host)
                    game.broadcast_l("now-spectating", player=user.username)
                    game.broadcast_sound("join_spectator.ogg")
                    game.rebuild_all_menus()
                    self._user_states[user.username] = {
                        "menu": "in_game",
                        "table_id": table_id,
                    }
                    return

            if len(game.players) >= game.get_max_players():
                user.speak_l("table-full")
                self._return_from_join_menu(user, state)
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
            game.add_spectator(user.username, user)
            user.speak_l("spectator-joined", host=table.host)
            game.broadcast_l("now-spectating", player=user.username)
            game.broadcast_sound("join_spectator.ogg")
            game.rebuild_all_menus()
            self._user_states[user.username] = {"menu": "in_game", "table_id": table_id}

        elif selection_id == "back":
            self._return_from_join_menu(user, state)

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
                    is_virtual_bot=p.get("is_virtual_bot", False),
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
                if p.is_bot and not p.is_virtual_bot:
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
                if p.is_bot and not p.is_virtual_bot:
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
                if p.is_bot and not p.is_virtual_bot:
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
                if p.is_bot and not p.is_virtual_bot:
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
                if p.is_bot and not p.is_virtual_bot:
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
                (p.player_id, p.player_name, p.is_bot, getattr(p, "is_virtual_bot", False))
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
        if not table and user:
            if packet.get("key") == "w" and packet.get("control"):
                players = [
                    u.username
                    for u in self._users.values()
                    if u.approved and not self._tables.find_user_table(u.username)
                ]
                if not players:
                    user.speak_l("online-users-none")
                    return
                names = Localization.format_list_and(user.locale, players)
                key = "online-users-one" if len(players) == 1 else "online-users-many"
                user.speak_l(key, count=len(players), users=names)
            return
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
        if not user:
            return

        # Check for admin editbox handlers
        state = self._user_states.get(username, {})
        current_menu = state.get("menu")

        if current_menu == "decline_reason_editbox":
            text = packet.get("text", "")
            await self._handle_decline_reason_editbox(user, text, state)
            return

        if current_menu == "ban_reason_editbox":
            text = packet.get("text", "")
            await self._handle_ban_reason_editbox(user, text, state)
            return

        if current_menu == "unban_reason_editbox":
            text = packet.get("text", "")
            await self._handle_unban_reason_editbox(user, text, state)
            return

        # Forward to game if user is in a table
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

    async def _handle_chat(self, client: ClientConnection, packet: dict) -> None:
        """Handle chat message."""
        username = client.username
        if not username:
            return

        convo = packet.get("convo", "local")
        message = packet.get("message", "")
        language = packet.get("language", "Other")

        chat_packet = {
            "type": "chat",
            "convo": convo,
            "sender": username,
            "message": message,
            "language": language,
        }

        if convo == "local":
            table = self._tables.find_user_table(username)
            if table:
                for member_name in [m.username for m in table.members]:
                    user = self._users.get(member_name)
                    if user and user.approved:  # Only send to approved users
                        await user.connection.send(chat_packet)
            else:
                for user in self._users.values():
                    if not user.approved:
                        continue
                    if self._tables.find_user_table(user.username):
                        continue
                    await user.connection.send(chat_packet)
        elif convo == "global":
            # Broadcast to all approved users only
            for user in self._users.values():
                if user.approved:
                    await user.connection.send(chat_packet)

    def _get_online_usernames(self) -> list[str]:
        """Return sorted list of online usernames."""
        return sorted(self._users.keys(), key=str.lower)

    def _format_online_users_lines(self, user: NetworkUser) -> list[str]:
        """Format online users with game names for menu display."""
        lines: list[str] = []
        for username in self._get_online_usernames():
            online_user = self._users.get(username)
            # Check if user is waiting for approval
            if online_user and not online_user.approved:
                status = Localization.get(user.locale, "online-user-waiting-approval")
                lines.append(f"{username}: {status}")
                continue

            table = self._tables.find_user_table(username)
            if table:
                game_class = get_game_class(table.game_type)
                game_name = (
                    Localization.get(user.locale, game_class.get_name_key())
                    if game_class
                    else table.game_type
                )
                lines.append(f"{username}: {game_name}")
            else:
                status = Localization.get(user.locale, "online-user-not-in-game")
                lines.append(f"{username}: {status}")
        if not lines:
            lines.append(Localization.get(user.locale, "online-users-none"))
        return lines

    def _show_online_users_menu(self, user: NetworkUser) -> None:
        """Show online users with games in a read-only menu."""
        current_state = self._user_states.get(user.username, {})
        previous_menu_id = current_state.get("menu")
        previous_menu = None
        if previous_menu_id:
            current_menus = getattr(user, "_current_menus", {})
            previous_menu = current_menus.get(previous_menu_id)

        items = [
            MenuItem(text=line, id="online_user")
            for line in self._format_online_users_lines(user)
        ]
        user.show_menu(
            "online_users",
            items,
            multiletter=False,
            escape_behavior=EscapeBehavior.SELECT_LAST,
            position=0,
        )
        self._user_states[user.username] = {
            "menu": "online_users",
            "return_menu_id": previous_menu_id,
            "return_menu": previous_menu,
            "return_state": dict(current_state),
        }

    def _restore_previous_menu(self, user: NetworkUser, state: dict) -> None:
        """Restore the previous menu after closing the online users list."""
        previous_menu_id = state.get("return_menu_id")
        previous_menu = state.get("return_menu")
        if not previous_menu_id or not previous_menu:
            self._show_main_menu(user)
            return

        user.show_menu(
            previous_menu_id,
            previous_menu.get("items", []),
            multiletter=previous_menu.get("multiletter_enabled", True),
            escape_behavior=EscapeBehavior(previous_menu.get("escape_behavior", "keybind")),
            position=previous_menu.get("position"),
            grid_enabled=previous_menu.get("grid_enabled", False),
            grid_width=previous_menu.get("grid_width", 1),
        )
        restored_state = dict(state.get("return_state", {}))
        restored_state["menu"] = previous_menu_id
        self._user_states[user.username] = restored_state

    async def _handle_list_online(self, client: ClientConnection) -> None:
        """Handle request for online users list."""
        username = client.username
        if not username:
            return

        user = self._users.get(username)
        if not user:
            return

        online = self._get_online_usernames()
        count = len(online)
        if count == 0:
            user.speak_l("online-users-none")
            return
        users_str = Localization.format_list_and(user.locale, online)
        if count == 1:
            user.speak_l("online-users-one", users=users_str)
        else:
            user.speak_l("online-users-many", count=count, users=users_str)

    async def _handle_list_online_with_games(self, client: ClientConnection) -> None:
        """Handle request for online users list with game info."""
        username = client.username
        if not username:
            return

        user = self._users.get(username)
        if not user:
            return

        table = self._tables.find_user_table(username)
        if table and table.game:
            player = table.game.get_player_by_id(user.uuid)
            if player:
                table.game.status_box(player, self._format_online_users_lines(user))
                return

        self._show_online_users_menu(user)

    async def _handle_ping(self, client: ClientConnection) -> None:
        """Handle ping request - respond immediately with pong."""
        await client.send({"type": "pong"})


async def run_server(
    host: str = "::",
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
    logging.basicConfig(
        filename="errors.log",
        level=logging.ERROR,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    def _log_uncaught(exc_type, exc, tb):
        if exc_type in (KeyboardInterrupt, asyncio.CancelledError):
            return
        logging.getLogger("playpalace").exception(
            "Uncaught exception", exc_info=(exc_type, exc, tb)
        )

    sys.excepthook = _log_uncaught
    loop = asyncio.get_running_loop()

    def _asyncio_exception_handler(loop, context):
        exc = context.get("exception")
        if isinstance(exc, asyncio.CancelledError):
            return
        if exc:
            logging.getLogger("playpalace").exception(
                "Asyncio exception", exc_info=exc
            )
        else:
            logging.getLogger("playpalace").error(
                "Asyncio error: %s", context.get("message")
            )

    loop.set_exception_handler(_asyncio_exception_handler)

    config_path = _MODULE_DIR / "config.toml"
    example_path = _MODULE_DIR / "config.example.toml"
    db_path = _MODULE_DIR / "playpalace.db"

    if not config_path.exists():
        if not example_path.exists():
            print(
                f"ERROR: Missing configuration template '{example_path}'.",
                file=sys.stderr,
            )
            raise SystemExit(1)
        try:
            shutil.copyfile(example_path, config_path)
        except OSError as exc:
            print(
                f"ERROR: Failed to create '{config_path}' from template: {exc}",
                file=sys.stderr,
            )
            raise SystemExit(1) from exc
        print(f"Created '{config_path}' from '{example_path}'.")

        print(
            "Review server/config.toml before running in production. "
            "TLS is required unless you explicitly allow insecure mode.\n"
            "Run the server with:\n"
            "  uv run python main.py --ssl-cert <cert> --ssl-key <key>\n"
            "or set [network].allow_insecure_ws=true for local development."
        )
        return

    db_created = False
    needs_owner = False
    if not db_path.exists():
        db_created = True
        needs_owner = True
    else:
        try:
            database = Database(str(db_path))
            database.connect()
            user_count = database.get_user_count()
            owner = database.get_server_owner()
            needs_owner = user_count == 0 or owner is None
            database.close()
        except Exception as exc:
            print(f"ERROR: Failed to open database '{db_path}': {exc}", file=sys.stderr)
            raise SystemExit(1) from exc

    if needs_owner:
        from server.cli import bootstrap_owner

        if db_created:
            print(f"Creating database at '{db_path}'.")
        else:
            print("No server owner found in the database. Creating one now.")

        min_user_len = DEFAULT_USERNAME_MIN_LENGTH
        max_user_len = DEFAULT_USERNAME_MAX_LENGTH
        min_pass_len = DEFAULT_PASSWORD_MIN_LENGTH
        max_pass_len = DEFAULT_PASSWORD_MAX_LENGTH
        try:
            with open(config_path, "rb") as f:
                data = tomllib.load(f)
            auth_cfg = data.get("auth")
            if isinstance(auth_cfg, dict):
                min_user_len = int(auth_cfg.get("username_min_length", min_user_len))
                max_user_len = int(auth_cfg.get("username_max_length", max_user_len))
                min_pass_len = int(auth_cfg.get("password_min_length", min_pass_len))
                max_pass_len = int(auth_cfg.get("password_max_length", max_pass_len))
        except Exception:
            pass

        print(
            f"Username must be between {min_user_len} and {max_user_len} characters."
        )
        while True:
            username = input("Server owner username: ").strip()
            if not username:
                print("Username cannot be empty.")
                continue
            if not (min_user_len <= len(username) <= max_user_len):
                print(
                    f"Username must be between {min_user_len} and {max_user_len} characters."
                )
                continue
            break
        print(
            f"Password must be between {min_pass_len} and {max_pass_len} characters."
        )
        while True:
            password = getpass("Server owner password: ")
            if not password:
                print("Password cannot be empty.")
                continue
            if not (min_pass_len <= len(password) <= max_pass_len):
                print(
                    f"Password must be between {min_pass_len} and {max_pass_len} characters."
                )
                continue
            confirm = getpass("Confirm password: ")
            if password != confirm:
                print("Passwords do not match. Try again.")
                continue
            break

        try:
            bootstrap_owner(
                db_path=str(db_path),
                username=username,
                password=password,
                quiet=True,
            )
            print(f"Created server owner '{username}'.")
        except RuntimeError as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            raise SystemExit(1) from exc

    print(f"Starting PlayPalace v{VERSION} server...")
    server = Server(
        host=host,
        port=port,
        ssl_cert=ssl_cert,
        ssl_key=ssl_key,
        db_path=str(db_path),
    )
    await server.start()

    try:
        # Run forever
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        await server.stop()
