"""Choose a fresh game for each round while keeping the same table."""

from dataclasses import dataclass, field

from ..base import Game, Player
from ..registry import GameRegistry, register_game
from ...game_utils.actions import ActionSet
from ...game_utils.roulette import RouletteSession
from .options import RouletteOptions


@register_game
@dataclass
class RouletteGame(Game):
    options: RouletteOptions = field(default_factory=RouletteOptions)

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
        if not self._table or self.prestart_validate():
            return
        self.roulette = RouletteSession(
            included_games=list(self.options.included_games),
            finish_mode=self.options.finish_mode,
            total_rounds=self.options.total_rounds,
            target_score=self.options.target_score,
        )
        self._table.start_roulette_round()
