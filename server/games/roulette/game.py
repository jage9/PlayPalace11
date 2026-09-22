"""Choose a fresh game for each round while keeping the same table."""

from dataclasses import dataclass, field
import random

from ..base import Game, Player
from ..registry import GameRegistry, register_game
from ...core.ui.keybinds import KeybindState
from ...game_utils.actions import Action, ActionSet, Visibility
from ...game_utils.game_status import GameStatus
from ...game_utils.roulette import RouletteSession
from ...messages.localization import Localization
from .options import RouletteOptions


@register_game
@dataclass
class RouletteGame(Game):
    options: RouletteOptions = field(default_factory=RouletteOptions)
    selection_phase: str = "idle"
    selection_ticks: int = 0
    selected_game: str = ""
    blocked_games: list[str] = field(default_factory=list)

    @classmethod
    def get_name(cls) -> str:
        return "Game Roulette"

    @classmethod
    def get_type(cls) -> str:
        return "roulette"

    @classmethod
    def get_max_players(cls) -> int:
        return max(game.get_max_players() for game in GameRegistry.get_all()
                   if game.get_type() != "roulette")

    def prestart_validate(self) -> list:
        errors = super().prestart_validate()
        if self._table and not self._table.get_roulette_games(self.options.included_games):
            errors.append("roulette-no-compatible-games")
        return errors

    def create_estimate_action_set(self, player: Player) -> ActionSet:
        # The duration depends on the randomly selected games.
        return ActionSet(name="estimate")

    def on_start(self) -> None:
        if self._destroyed or self.selection_phase != "idle" or not self._table or self.prestart_validate():
            return
        if self.roulette is None:
            self.roulette = RouletteSession(included_games=[])
        for name in ("included_games", "finish_mode", "total_rounds", "target_score", "jokers"):
            value = getattr(self.options, name)
            setattr(self.roulette, name, list(value) if isinstance(value, list) else value)
        for player in self.get_active_players():
            self.roulette.jokers_remaining.setdefault(player.id, self.roulette.jokers)
        self.blocked_games.clear()
        self.status = GameStatus.PLAYING
        self.game_active = True
        self._sync_table_status()
        self._spin_wheel()

    def _available_games(self) -> list[type]:
        if not self._table or not self.roulette:
            return []
        return [cls for cls in self._table.get_roulette_games(self.roulette.included_games)
                if cls.get_type() not in self.blocked_games]

    def _spin_wheel(self) -> None:
        """Restart the five-second spin without consuming a round."""
        self.selection_phase = "spinning"
        self.selection_ticks = 5 * self.TICKS_PER_SECOND
        self.selected_game = ""
        self.clear_scheduled_sounds()
        # Reuse the short click at progressively wider intervals as the wheel slows.
        tick = 0
        while tick < self.selection_ticks:
            self.schedule_sound("click.ogg", delay_ticks=tick)
            tick += 2 + tick // 20
        self.broadcast_l("roulette-spinning")
        self.rebuild_all_menus()

    def on_tick(self) -> None:
        if self._destroyed:
            return
        super().on_tick()
        if self.status != GameStatus.PLAYING or self.selection_ticks <= 0:
            return
        self.selection_ticks -= 1
        if self.selection_ticks:
            return
        if self.selection_phase == "joker":
            if not self._table.play_roulette_game(self.selected_game):
                self._spin_wheel()
            return
        choices = self._available_games()
        if not choices:
            self.selection_phase = "idle"
            self.game_active = False
            self.status = GameStatus.WAITING
            self._sync_table_status()
            self.broadcast_l("roulette-no-compatible-games")
            self.rebuild_all_menus()
            return
        alternatives = [cls for cls in choices if cls.get_type() != self.roulette.previous_game]
        selected = random.choice(alternatives or choices)
        self.selected_game = selected.get_type()
        self.selection_phase = "joker"
        self.selection_ticks = 5 * self.TICKS_PER_SECOND
        self.play_sound("game_squares/diceroll1.ogg")
        for player in self.players:
            user = self.get_user(player)
            if user:
                self.send_table_message(player, self._get_selection_label(player, ""))
        self.broadcast_l("roulette-joker-window")
        self.rebuild_all_menus()

    def setup_keybinds(self) -> None:
        super().setup_keybinds()
        self.define_keybind("j", "Play joker", ["play_joker"], state=KeybindState.ACTIVE)

    def create_turn_action_set(self, player: Player) -> ActionSet:
        actions = ActionSet(name="turn")
        actions.add(Action(
            id="wheel_status", label="", handler="_action_wheel_status", is_enabled="",
            is_hidden="_is_selection_hidden", get_label="_get_selection_label",
            include_spectators=True,
        ))
        actions.add(Action(
            id="play_joker", label="", handler="_action_play_joker",
            is_enabled="_is_joker_enabled", is_hidden="_is_selection_hidden",
            get_label="_get_joker_label",
        ))
        return actions

    def _is_selection_hidden(self, player: Player) -> Visibility:
        return Visibility.VISIBLE if self.status == GameStatus.PLAYING else Visibility.HIDDEN

    def _get_selection_label(self, player: Player, action_id: str) -> str:
        user = self.get_user(player)
        locale = user.locale if user else "en"
        if self.selected_game:
            cls = GameRegistry.get(self.selected_game)
            return Localization.get(locale, "roulette-selected-game",
                                    game=Localization.get(locale, cls.get_name_key()))
        return Localization.get(locale, "roulette-spinning")

    def _action_wheel_status(self, player: Player, action_id: str) -> None:
        user = self.get_user(player)
        if user:
            user.speak(self._get_selection_label(player, action_id))

    def _get_joker_label(self, player: Player, action_id: str) -> str:
        user = self.get_user(player)
        count = self.roulette.jokers_remaining.get(player.id, 0) if self.roulette else 0
        return Localization.get(user.locale if user else "en", "roulette-joker-action", count=count)

    def _is_joker_enabled(self, player: Player) -> str | None:
        if (self._destroyed or player.is_spectator or self.status != GameStatus.PLAYING
                or self.selection_phase != "joker" or self.selection_ticks <= 0):
            return "roulette-joker-unavailable"
        if not self.roulette or self.roulette.jokers_remaining.get(player.id, 0) <= 0:
            return "roulette-no-jokers"
        if not any(cls.get_type() != self.selected_game for cls in self._available_games()):
            return "roulette-no-alternative"
        return None

    def _action_play_joker(self, player: Player, action_id: str) -> None:
        """Close the window synchronously so only the first valid joker is spent."""
        error = self._is_joker_enabled(player)
        if error:
            user = self.get_user(player)
            if user:
                user.speak_l(error)
            return
        self.selection_phase = "spinning"
        self.roulette.jokers_remaining[player.id] -= 1
        self.blocked_games.append(self.selected_game)
        self.broadcast_l("roulette-joker-used", player=player.name,
                         remaining=self.roulette.jokers_remaining[player.id])
        self._spin_wheel()
