"""Options for the Roulette game."""

from copy import deepcopy
from dataclasses import dataclass, field, fields

from ...game_utils.options import (
    GameOptions,
    IntOption,
    MenuOption,
    MultiSelectOption,
    option_field,
)
from ...game_utils.roulette import RouletteSession
from ..registry import GameRegistry


def get_game_types() -> list[str]:
    """Return all registered game types except Roulette itself."""

    game_classes = GameRegistry.get_all()
    return sorted(
        game_class.get_type()
        for game_class in game_classes
        if game_class.get_type() != "roulette"
    )


def get_game_name_keys() -> dict[str, str]:
    """Return registry game types mapped to their standard name keys."""

    game_classes = GameRegistry.get_all()
    return {
        game_class.get_type(): game_class.get_name_key()
        for game_class in game_classes
        if game_class.get_type() != "roulette"
    }


_GAME_NAME_KEYS = get_game_name_keys()


@dataclass
class RouletteOptions(GameOptions):
    """Configurable limits and game pool for a Roulette session."""

    @classmethod
    def from_session(cls, session: RouletteSession) -> "RouletteOptions":
        """Create options copied from a Roulette session."""
        return cls(
            **{
                option.name: deepcopy(getattr(session, option.name))
                for option in fields(cls)
            }
        )

    def update_session(self, session: RouletteSession) -> None:
        """Copy these options into an existing Roulette session."""
        for option in fields(self):
            setattr(session, option.name, deepcopy(getattr(self, option.name)))

    finish_mode: str = option_field(
        MenuOption(
            default="rounds",
            value_key="mode",
            choices=["rounds", "score"],
            choice_labels={
                "rounds": "roulette-finish-mode-rounds",
                "score": "roulette-finish-mode-score",
            },
            label="roulette-set-finish-mode",
            prompt="roulette-select-finish-mode",
            change_msg="roulette-option-changed-finish-mode",
            description="roulette-desc-finish-mode",
        )
    )
    total_rounds: int = option_field(
        IntOption(
            default=7,
            min_val=1,
            max_val=1000,
            value_key="rounds",
            label="roulette-set-total-rounds",
            prompt="roulette-enter-total-rounds",
            change_msg="roulette-option-changed-total-rounds",
            description="roulette-desc-total-rounds",
        ),
        visible_when=("finish_mode", lambda value: value == "rounds"),
    )
    target_score: int = option_field(
        IntOption(
            default=2000,
            min_val=1,
            max_val=100000,
            value_key="score",
            label="roulette-set-target-score",
            prompt="roulette-enter-target-score",
            change_msg="roulette-option-changed-target-score",
            description="roulette-desc-target-score",
        ),
        visible_when=("finish_mode", lambda value: value == "score"),
    )
    jokers: int = option_field(
        IntOption(
            default=1,
            min_val=0,
            max_val=10,
            value_key="jokers",
            label="roulette-set-jokers",
            prompt="roulette-enter-jokers",
            change_msg="roulette-option-changed-jokers",
            description="roulette-desc-jokers",
        )
    )
    included_games: list[str] = field(
        default_factory=get_game_types,
        metadata={
            "option_meta": MultiSelectOption(
                default=[],
                choices=get_game_types,
                min_selected=1,
                choice_labels=_GAME_NAME_KEYS,
                show_bulk_actions=True,
                label="roulette-set-included-games",
                change_msg="roulette-option-changed-included-games",
                description="roulette-desc-included-games",
            )
        },
    )


__all__ = ["RouletteOptions", "get_game_name_keys", "get_game_types"]
