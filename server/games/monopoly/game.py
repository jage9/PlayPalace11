"""Monopoly game scaffold wired to generated preset artifacts."""

from __future__ import annotations

from dataclasses import dataclass, field

from ..base import Game, Player, GameOptions
from ..registry import register_game
from ...game_utils.action_guard_mixin import ActionGuardMixin
from ...game_utils.actions import Action, ActionSet, Visibility
from ...game_utils.options import MenuOption, option_field
from ...messages.localization import Localization
from ...ui.keybinds import KeybindState
from .presets import (
    DEFAULT_PRESET_ID,
    MonopolyPreset,
    get_available_preset_ids as _catalog_preset_ids,
    get_default_preset_id as _catalog_default_preset_id,
    get_preset as _catalog_get_preset,
)


PRESET_LABEL_KEYS = {
    "classic_standard": "monopoly-preset-classic-standard",
    "junior": "monopoly-preset-junior",
    "cheaters": "monopoly-preset-cheaters",
    "electronic_banking": "monopoly-preset-electronic-banking",
    "voice_banking": "monopoly-preset-voice-banking",
    "sore_losers": "monopoly-preset-sore-losers",
    "speed": "monopoly-preset-speed",
    "builder": "monopoly-preset-builder",
    "city": "monopoly-preset-city",
    "bid_card_game": "monopoly-preset-bid-card-game",
    "deal_card_game": "monopoly-preset-deal-card-game",
    "knockout": "monopoly-preset-knockout",
    "free_parking_jackpot": "monopoly-preset-free-parking-jackpot",
}


@dataclass
class MonopolyPlayer(Player):
    """Player state for Monopoly scaffold."""


@dataclass
class MonopolyOptions(GameOptions):
    """Lobby options for Monopoly scaffold."""

    preset_id: str = option_field(
        MenuOption(
            default=DEFAULT_PRESET_ID,
            choices=lambda game, player: game.get_available_preset_ids(),
            value_key="preset",
            choice_labels=PRESET_LABEL_KEYS,
            label="monopoly-set-preset",
            prompt="monopoly-select-preset",
            change_msg="monopoly-option-changed-preset",
        )
    )


@dataclass
@register_game
class MonopolyGame(ActionGuardMixin, Game):
    """Catalog-backed Monopoly scaffold.

    This class intentionally wires preset selection and metadata loading first.
    Gameplay mechanics are added incrementally in later milestones.
    """

    players: list[MonopolyPlayer] = field(default_factory=list)
    options: MonopolyOptions = field(default_factory=MonopolyOptions)

    active_preset_id: str = DEFAULT_PRESET_ID
    active_preset_name: str = ""
    active_family_key: str = ""
    active_edition_ids: list[str] = field(default_factory=list)
    active_anchor_edition_id: str = ""

    @classmethod
    def get_name(cls) -> str:
        return "Monopoly"

    @classmethod
    def get_type(cls) -> str:
        return "monopoly"

    @classmethod
    def get_category(cls) -> str:
        return "category-uncategorized"

    @classmethod
    def get_min_players(cls) -> int:
        return 2

    @classmethod
    def get_max_players(cls) -> int:
        return 6

    def create_player(
        self, player_id: str, name: str, is_bot: bool = False
    ) -> MonopolyPlayer:
        """Create a Monopoly player."""
        return MonopolyPlayer(id=player_id, name=name, is_bot=is_bot)

    def setup_keybinds(self) -> None:
        """Define keybinds for lobby + scaffold status checks."""
        super().setup_keybinds()
        self.define_keybind(
            "p",
            "Announce current preset",
            ["announce_preset"],
            state=KeybindState.ACTIVE,
            include_spectators=True,
        )

    def create_standard_action_set(self, player: MonopolyPlayer) -> ActionSet:
        """Add preset announcement action to standard action set."""
        action_set = super().create_standard_action_set(player)
        user = self.get_user(player)
        locale = user.locale if user else "en"
        action_set.add(
            Action(
                id="announce_preset",
                label=Localization.get(locale, "monopoly-announce-preset"),
                handler="_action_announce_preset",
                is_enabled="_is_announce_preset_enabled",
                is_hidden="_is_announce_preset_hidden",
            )
        )
        return action_set

    def get_available_preset_ids(self) -> list[str]:
        """Return selectable preset ids from generated catalog artifacts."""
        return _catalog_preset_ids()

    def _fallback_preset(self) -> MonopolyPreset:
        """Return a safe fallback preset if artifacts are missing."""
        fallback_id = _catalog_default_preset_id()
        fallback = _catalog_get_preset(fallback_id)
        if fallback:
            return fallback
        return MonopolyPreset(
            preset_id=DEFAULT_PRESET_ID,
            family_key="classic_and_themed_standard",
            name="Classic and Themed Standard",
            description="Fallback preset when catalog artifacts are unavailable.",
            anchor_edition_id="",
            edition_ids=(),
        )

    def _resolve_selected_preset(self) -> MonopolyPreset:
        """Resolve currently selected lobby preset, applying fallback when needed."""
        selected = _catalog_get_preset(self.options.preset_id)
        if selected:
            return selected
        fallback = self._fallback_preset()
        self.options.preset_id = fallback.preset_id
        return fallback

    def _localize_preset_name(self, locale: str, preset_id: str, fallback: str) -> str:
        """Resolve localized preset label for speech."""
        preset_key = PRESET_LABEL_KEYS.get(preset_id)
        if not preset_key:
            return fallback
        text = Localization.get(locale, preset_key)
        if text == preset_key:
            return fallback
        return text

    def _is_announce_preset_enabled(self, player: Player) -> str | None:
        """Enable preset announcements during active play."""
        return self.guard_game_active()

    def _is_announce_preset_hidden(self, player: Player) -> Visibility:
        """Hide announce action from menus (keybind only)."""
        return Visibility.HIDDEN

    def _action_announce_preset(self, player: Player, action_id: str) -> None:
        """Speak current preset details to one player."""
        user = self.get_user(player)
        if not user:
            return
        preset_name = self._localize_preset_name(
            user.locale, self.active_preset_id, self.active_preset_name
        )
        user.speak_l(
            "monopoly-current-preset",
            preset=preset_name,
            count=len(self.active_edition_ids),
        )

    def on_start(self) -> None:
        """Start scaffold mode using the selected preset metadata."""
        self.status = "playing"
        self.game_active = True
        self.round = 1

        active_players = self.get_active_players()
        self._team_manager.team_mode = "individual"
        self._team_manager.setup_teams([player.name for player in active_players])
        self.set_turn_players(active_players)

        preset = self._resolve_selected_preset()
        self.active_preset_id = preset.preset_id
        self.active_preset_name = preset.name
        self.active_family_key = preset.family_key
        self.active_edition_ids = list(preset.edition_ids)
        self.active_anchor_edition_id = preset.anchor_edition_id

        self.broadcast_l(
            "monopoly-scaffold-started",
            preset=preset.name,
            count=len(self.active_edition_ids),
        )
        self.rebuild_all_menus()
