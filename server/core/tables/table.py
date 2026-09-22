"""Table management for games."""

from dataclasses import dataclass, field
from copy import deepcopy
from typing import TYPE_CHECKING, Any

from mashumaro.mixins.json import DataClassJSONMixin

from server.game_utils.game_status import GameStatus

if TYPE_CHECKING:
    from server.games.base import Game
    from server.core.users.base import User
    from server.core.tables.manager import TableManager
    from server.core.server import Server
    from server.persistence.database import Database


@dataclass
class TableMember:
    """Member of a table (player or spectator).

    Attributes:
        username: Member username.
        is_spectator: True if spectating.
    """

    username: str
    is_spectator: bool = False


@dataclass
class Table(DataClassJSONMixin):
    """Game table holding members and a game instance.

    Tables track membership and forward events to the game. Role logic
    (player vs spectator) is handled by the game.
    """

    table_id: str
    game_type: str
    host: str
    members: list[TableMember] = field(default_factory=list)
    game_json: str | None = None  # Serialized game state
    status: str = GameStatus.WAITING

    # Not serialized
    _game: "Game | None" = field(default=None, repr=False)
    _users: dict[str, "User"] = field(default_factory=dict, repr=False)
    _manager: "TableManager | None" = field(default=None, repr=False)
    _server: "Server | None" = field(default=None, repr=False)
    _db: "Database | None" = field(default=None, repr=False)

    def __post_init__(self):
        """Initialize non-serialized runtime references."""
        self._game = None
        self._users = {}
        self._manager = None
        self._server = None
        self._db = None

    @property
    def game(self) -> "Game | None":
        """Return the current game instance."""
        return self._game

    @game.setter
    def game(self, value: "Game | None") -> None:
        """Set the game instance and update serialized state."""
        self._game = value
        if value:
            self.game_json = value.to_json()

    def add_member(self, username: str, user: "User", as_spectator: bool = False) -> None:
        """Add a member to the table.

        Args:
            username: Member username.
            user: User instance.
            as_spectator: True to join as spectator.
        """
        # Check if already a member
        for member in self.members:
            if member.username == username:
                return

        self.members.append(TableMember(username=username, is_spectator=as_spectator))
        self._users[username] = user

    def remove_member(self, username: str) -> None:
        """Remove a member from the table."""
        self.members = [m for m in self.members if m.username != username]
        self._users.pop(username, None)

        # Destroy table if it's empty
        if not self.members:
            self.destroy()

    def get_user(self, username: str) -> "User | None":
        """Get a user by username."""
        return self._users.get(username)

    def attach_user(self, username: str, user: "User") -> None:
        """Attach a user to a member (e.g., after deserialization)."""
        self._users[username] = user

    def get_players(self) -> list[TableMember]:
        """Get all non-spectator members."""
        return [m for m in self.members if not m.is_spectator]

    def get_spectators(self) -> list[TableMember]:
        """Get all spectator members."""
        return [m for m in self.members if m.is_spectator]

    @property
    def player_count(self) -> int:
        """Get the number of players (non-spectators)."""
        return len(self.get_players())

    @property
    def listing_game_type(self) -> str:
        """Keep roulette tables listed together while their current game changes."""
        return "roulette" if self.game and self.game.roulette else self.game_type

    def broadcast(self, text: str, buffer: str = "misc") -> None:
        """Send a message to all members."""
        for username, user in self._users.items():
            user.speak(text, buffer)

    def broadcast_sound(self, name: str, volume: int = 100) -> None:
        """Play a sound for all members."""
        for user in self._users.values():
            user.play_sound(name, volume)

    def on_tick(self) -> None:
        """Called every tick. Forwards to game."""
        if self._game:
            self._game.on_tick()

    def handle_event(self, username: str, event: dict) -> None:
        """Handle an event from a member."""
        if self._game:
            # Find the player
            for player in self._game.players:
                if player.name == username:
                    self._game.handle_event(player, event)
                    break

    def save_game_state(self) -> None:
        """Save the current game state to game_json."""
        if self._game:
            self.game_json = self._game.to_json()

    def can_start(self, min_players: int) -> bool:
        """Check if the game can start."""
        return self.player_count >= min_players

    def prepare_next_game(self, username: str, game_type: str | None = None) -> bool:
        """Keep the table and seats, but replace a finished game with a fresh lobby.

        Replays retain options. Switching games uses the new game's defaults.
        A fresh instance prevents hands, timers, and queued actions leaking between games.
        """
        from server.games.registry import get_game_class

        previous = self.game
        if not previous or previous.status != GameStatus.FINISHED or username != previous.host:
            return False
        game_class = get_game_class(game_type or self.game_type)
        if game_class is None:
            return False
        member_names = {member.username for member in self.members}
        players = [p for p in previous.players
                   if not p.replaced_human or p.name in member_names]
        if sum(not p.is_spectator or p.eliminated for p in players) > game_class.get_max_players():
            user = self.get_user(username)
            if user:
                user.speak_l("action-table-full")
            return False

        game = game_class()
        if game.get_type() == previous.get_type() and hasattr(previous, "options"):
            game.options = deepcopy(previous.options)
        elif game.get_type() == "roulette" and previous.roulette:
            for name in ("included_games", "finish_mode", "total_rounds", "target_score"):
                setattr(game.options, name, deepcopy(getattr(previous.roulette, name)))
        self._replace_game(game, players)
        return True

    def _replace_game(self, game: "Game", players: list) -> None:
        """Install fresh player state while retaining this table's users and seats."""
        previous = self.game
        game.host = previous.host
        game._table = self
        game.setup_keybinds()
        for old_player in players:
            player = game.create_player(old_player.id, old_player.name, is_bot=old_player.is_bot)
            player.is_virtual_bot = old_player.is_virtual_bot
            player.is_spectator = old_player.is_spectator and not old_player.eliminated
            game.players.append(player)
            user = previous.get_user(old_player)
            if user:
                user.stop_music()
                user.stop_ambience()
                for menu_id in ("game_over", "change_game", "leave_game_confirm", "actions_menu"):
                    user.remove_menu(menu_id)
                game.attach_user(player.id, user)
            game.setup_player_actions(player)
            for member in self.members:
                if member.username == player.name:
                    member.is_spectator = player.is_spectator

        previous._destroyed = True
        previous._table = None
        previous._pending_actions.clear()
        self.game_type = game.get_type()
        self.host = game.host
        self.status = GameStatus.WAITING
        self.game = game
        game._reset_transcripts()
        game.rebuild_all_menus()

    def get_roulette_games(self, included_games: list[str]) -> list[type]:
        """Only offer games whose default rules support every seated participant."""
        from server.games.registry import get_game_class

        previous = self.game
        members = {member.username for member in self.members}
        players = [p for p in previous.get_result_players()
                   if not p.replaced_human or p.name in members]
        choices = []
        for game_type in dict.fromkeys(included_games):
            cls = get_game_class(game_type)
            if cls is None or game_type == "roulette":
                continue
            if not cls.get_min_players() <= len(players) <= cls.get_max_players():
                continue
            candidate = cls()
            candidate.players = [candidate.create_player(p.id, p.name, is_bot=p.is_bot)
                                 for p in players]
            if not candidate.prestart_validate():
                choices.append(cls)
        return choices

    def start_roulette_round(self) -> bool:
        """Draw a compatible game and start one round with fresh game state."""
        import random

        previous = self.game
        session = previous.roulette
        if session is None or session.finished:
            return False
        choices = self.get_roulette_games(session.included_games)
        if not choices:
            previous.broadcast_l("roulette-no-compatible-games")
            return False
        alternatives = [cls for cls in choices if cls.get_type() != session.previous_game]
        game = random.choice(alternatives or choices)()
        game.roulette = session
        session.round_number += 1
        session.previous_game = game.get_type()
        members = {member.username for member in self.members}
        players = [p for p in previous.players if not p.replaced_human or p.name in members]
        self._replace_game(game, players)
        for player in game.players:
            user = game.get_user(player)
            if user:
                from server.messages.localization import Localization
                game.send_table_message(player, Localization.get(
                    user.locale, "roulette-round-start", round=session.round_number,
                    game=Localization.get(user.locale, game.get_name_key())))
        game.on_start()
        game._sync_table_status()
        game.validate_actions()
        self.save_game_state()
        return True

    def destroy(self) -> None:
        """Destroy this table. Called by Game.destroy()."""
        if self._manager:
            self._manager.on_table_destroy(self)

    def save_and_close(self, username: str) -> None:
        """Save game state and close table. Called by game save action."""
        if self._server:
            self._server.on_table_save(self, username)

    def save_game_result(self, result: Any) -> None:
        """Save a game result to the database. Called by game when it finishes."""
        if self._server:
            self._server.on_game_result(result)
