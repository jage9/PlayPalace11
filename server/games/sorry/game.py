"""Sorry game scaffold for PlayPalace."""

from dataclasses import dataclass, field

from ..base import Game, Player
from ..registry import register_game
from ...game_utils.actions import Action, ActionSet, Visibility
from ...game_utils.options import BoolOption, GameOptions, MenuOption, option_field
from ...messages.localization import Localization
from server.core.ui.keybinds import KeybindState
from .bot import choose_move
from .moves import SorryMove, apply_move, generate_legal_moves
from .rules import (
    Classic00390Rules,
    SorryRulesProfile,
    get_rules_profile_by_id,
    get_supported_profile_ids,
)
from .state import (
    SorryGameState,
    SorryPlayerState,
    build_initial_game_state,
    discard_current_card,
    draw_next_card,
)


@dataclass
class SorryPlayer(Player):
    """Player state for Sorry."""

    pawns_in_start: int = 4
    pawns_in_home: int = 0


@dataclass
class SorryOptions(GameOptions):
    """Configurable options for Sorry."""

    rules_profile: str = option_field(
        MenuOption(
            default="classic_00390",
            value_key="rules_profile",
            choices=list(get_supported_profile_ids()),
            choice_labels={
                "classic_00390": "sorry-rules-profile-classic-00390",
                "a5065_core": "sorry-rules-profile-a5065-core",
            },
            label="sorry-option-rules-profile",
            prompt="sorry-option-select-rules-profile",
            change_msg="sorry-option-changed-rules-profile",
        )
    )
    auto_apply_single_move: bool = option_field(
        BoolOption(
            default=False,
            value_key="auto_apply_single_move",
            label="sorry-option-auto-apply-single-move",
            change_msg="sorry-option-changed-auto-apply-single-move",
        )
    )
    faster_setup_one_pawn_out: bool = option_field(
        BoolOption(
            default=False,
            value_key="faster_setup_one_pawn_out",
            label="sorry-option-faster-setup-one-pawn-out",
            change_msg="sorry-option-changed-faster-setup-one-pawn-out",
        )
    )


@dataclass
@register_game
class SorryGame(Game):
    """Classic Sorry scaffold with rules-profile extension point."""

    players: list[SorryPlayer] = field(default_factory=list)
    options: SorryOptions = field(default_factory=SorryOptions)

    rules_profile_id: str = "classic_00390"
    game_state: SorryGameState = field(default_factory=SorryGameState)
    max_move_slots: int = 64

    @classmethod
    def get_name(cls) -> str:
        return "Sorry!"

    @classmethod
    def get_type(cls) -> str:
        return "sorry"

    @classmethod
    def get_category(cls) -> str:
        return "category-board-games"

    @classmethod
    def get_min_players(cls) -> int:
        return 2

    @classmethod
    def get_max_players(cls) -> int:
        return 4

    def create_player(
        self, player_id: str, name: str, is_bot: bool = False
    ) -> SorryPlayer:
        """Create a new Sorry player."""
        return SorryPlayer(
            id=player_id,
            name=name,
            is_bot=is_bot,
            pawns_in_start=self.get_rules_profile().pawns_per_player,
        )

    def _resolve_rules_profile_id(self) -> str:
        requested = self.options.rules_profile or self.rules_profile_id
        if get_rules_profile_by_id(requested) is None:
            requested = Classic00390Rules().profile_id
        self.rules_profile_id = requested
        self.options.rules_profile = requested
        return requested

    def get_rules_profile(self) -> SorryRulesProfile:
        """Return active rules profile object."""
        profile_id = self._resolve_rules_profile_id()
        profile = get_rules_profile_by_id(profile_id)
        if profile is not None:
            return profile
        return Classic00390Rules()

    def _parse_move_slot(self, action_id: str) -> int | None:
        if not action_id.startswith("move_slot_"):
            return None
        try:
            slot = int(action_id.split("_")[-1])
        except ValueError:
            return None
        if slot < 1:
            return None
        return slot

    def _player_locale(self, player: Player) -> str:
        user = self.get_user(player)
        if user:
            return user.locale
        return "en"

    def _card_display_text(self, locale: str, card_face: str) -> str:
        if card_face == "sorry":
            return Localization.get(locale, "sorry-card-sorry")
        return card_face

    def _target_player_name(self, player_id: str | None) -> str:
        if not player_id:
            return "Unknown"
        target = self.get_player_by_id(player_id)
        if target:
            return target.name
        return player_id

    def _move_label(self, locale: str, move: SorryMove) -> str:
        if move.move_type == "start":
            return Localization.get(
                locale,
                "sorry-move-start",
                pawn=move.pawn_index or 0,
            )
        if move.move_type == "forward":
            return Localization.get(
                locale,
                "sorry-move-forward",
                pawn=move.pawn_index or 0,
                steps=move.steps or 0,
            )
        if move.move_type == "backward":
            return Localization.get(
                locale,
                "sorry-move-backward",
                pawn=move.pawn_index or 0,
                steps=move.steps or 0,
            )
        if move.move_type == "swap":
            return Localization.get(
                locale,
                "sorry-move-swap",
                pawn=move.pawn_index or 0,
                target_player=self._target_player_name(move.target_player_id),
                target_pawn=move.target_pawn_index or 0,
            )
        if move.move_type == "sorry":
            return Localization.get(
                locale,
                "sorry-move-sorry",
                pawn=move.pawn_index or 0,
                target_player=self._target_player_name(move.target_player_id),
                target_pawn=move.target_pawn_index or 0,
            )
        if move.move_type == "split7":
            return Localization.get(
                locale,
                "sorry-move-split7",
                pawn_a=move.pawn_index or 0,
                steps_a=move.steps or 0,
                pawn_b=move.secondary_pawn_index or 0,
                steps_b=move.secondary_steps or 0,
            )
        return move.description

    def _announce_move(self, player: Player, move: SorryMove) -> None:
        if move.move_type == "start":
            self.broadcast_l(
                "sorry-play-start",
                player=player.name,
                pawn=move.pawn_index or 0,
            )
            return
        if move.move_type == "forward":
            self.broadcast_l(
                "sorry-play-forward",
                player=player.name,
                pawn=move.pawn_index or 0,
                steps=move.steps or 0,
            )
            return
        if move.move_type == "backward":
            self.broadcast_l(
                "sorry-play-backward",
                player=player.name,
                pawn=move.pawn_index or 0,
                steps=move.steps or 0,
            )
            return
        if move.move_type == "swap":
            self.broadcast_l(
                "sorry-play-swap",
                player=player.name,
                pawn=move.pawn_index or 0,
                target_player=self._target_player_name(move.target_player_id),
                target_pawn=move.target_pawn_index or 0,
            )
            return
        if move.move_type == "sorry":
            self.broadcast_l(
                "sorry-play-sorry",
                player=player.name,
                pawn=move.pawn_index or 0,
                target_player=self._target_player_name(move.target_player_id),
                target_pawn=move.target_pawn_index or 0,
            )
            return
        if move.move_type == "split7":
            self.broadcast_l(
                "sorry-play-split7",
                player=player.name,
                pawn_a=move.pawn_index or 0,
                steps_a=move.steps or 0,
                pawn_b=move.secondary_pawn_index or 0,
                steps_b=move.secondary_steps or 0,
            )
            return

    def get_player_state(self, player: Player) -> SorryPlayerState | None:
        """Return serializable board state for a player."""
        return self.game_state.player_states.get(player.id)

    def get_legal_moves_for_card(
        self,
        player: Player,
        card_face: str,
    ) -> list[SorryMove]:
        """Get legal moves for the player's current board state."""
        player_state = self.get_player_state(player)
        if player_state is None:
            return []
        return generate_legal_moves(
            state=self.game_state,
            player_state=player_state,
            card_face=card_face,
            rules=self.get_rules_profile(),
        )

    def _get_current_legal_moves(self, player: Player) -> list[SorryMove]:
        if self.game_state.turn_phase != "choose_move":
            return []
        if self.game_state.current_card is None:
            return []
        return self.get_legal_moves_for_card(player, self.game_state.current_card)

    def apply_legal_move(self, player: Player, move: SorryMove) -> None:
        """Apply a move chosen from legal move generation."""
        player_state = self.get_player_state(player)
        if player_state is None:
            raise ValueError("Player state missing for move application")
        apply_move(
            state=self.game_state,
            player_state=player_state,
            move=move,
            rules=self.get_rules_profile(),
        )

    def _sync_player_counts(self) -> None:
        """Recompute start/home pawn counts from serializable board state."""
        for player in self.players:
            state = self.get_player_state(player)
            if state is None:
                continue
            player.pawns_in_start = sum(1 for pawn in state.pawns if pawn.zone == "start")
            player.pawns_in_home = sum(1 for pawn in state.pawns if pawn.zone == "home")

    def _has_player_won(self, player: Player) -> bool:
        state = self.get_player_state(player)
        if state is None:
            return False
        return all(pawn.zone == "home" for pawn in state.pawns)

    def _finish_game(self, winner: Player) -> None:
        self.game_active = False
        self.status = "finished"
        self.broadcast_l("game-winner", player=winner.name)
        self.rebuild_all_menus()

    def _start_turn(self, *, announce: bool = True) -> None:
        self._resolve_rules_profile_id()
        self.game_state.turn_phase = "draw"
        self.game_state.current_card = None
        if announce:
            self.announce_turn()
        self.rebuild_all_menus()

    def _end_turn_after_card(self, card_face: str) -> None:
        self.game_state.turn_number += 1
        self.game_state.turn_phase = "draw"
        self.game_state.current_card = None
        if card_face == "2" and self.get_rules_profile().card_two_grants_extra_turn():
            # Classic Sorry gives another turn on 2.
            self.announce_turn()
            self.rebuild_all_menus()
            return
        self.advance_turn(announce=True)

    def create_turn_action_set(self, player: SorryPlayer) -> ActionSet:
        """Create turn actions: draw + move slots (dynamic by phase)."""
        locale = self._player_locale(player)
        action_set = ActionSet(name="turn")
        action_set.add(
            Action(
                id="draw_card",
                label=Localization.get(locale, "sorry-draw-card"),
                handler="_action_draw_card",
                is_enabled="_is_draw_enabled",
                is_hidden="_is_draw_hidden",
                show_in_actions_menu=False,
            )
        )
        for slot in range(1, self.max_move_slots + 1):
            action_set.add(
                Action(
                    id=f"move_slot_{slot}",
                    label=Localization.get(locale, "sorry-move-slot", slot=slot),
                    handler="_action_choose_move",
                    is_enabled="_is_move_slot_enabled",
                    is_hidden="_is_move_slot_hidden",
                    get_label="_get_move_slot_label",
                    show_in_actions_menu=False,
                )
            )
        return action_set

    def setup_keybinds(self) -> None:
        """Define keybinds for draw and the first move slots."""
        super().setup_keybinds()
        self.define_keybind("d", "Draw card", ["draw_card"], state=KeybindState.ACTIVE)
        self.define_keybind("space", "Draw card", ["draw_card"], state=KeybindState.ACTIVE)
        for slot in range(1, 10):
            self.define_keybind(
                str(slot),
                f"Choose move {slot}",
                [f"move_slot_{slot}"],
                state=KeybindState.ACTIVE,
            )

    def _is_draw_enabled(self, player: Player) -> str | None:
        if self.status != "playing":
            return "action-not-playing"
        if self.current_player != player:
            return "action-not-your-turn"
        if self.game_state.turn_phase != "draw":
            return "action-not-available"
        return None

    def _is_draw_hidden(self, player: Player) -> Visibility:
        if self.status != "playing":
            return Visibility.HIDDEN
        if self.current_player != player:
            return Visibility.HIDDEN
        if self.game_state.turn_phase != "draw":
            return Visibility.HIDDEN
        return Visibility.VISIBLE

    def _is_move_slot_enabled(self, player: Player, action_id: str) -> str | None:
        if self.status != "playing":
            return "action-not-playing"
        if self.current_player != player:
            return "action-not-your-turn"
        if self.game_state.turn_phase != "choose_move":
            return "action-not-available"
        slot = self._parse_move_slot(action_id)
        if slot is None:
            return "action-not-available"
        legal = self._get_current_legal_moves(player)
        if slot > len(legal):
            return "action-not-available"
        return None

    def _is_move_slot_hidden(self, player: Player, action_id: str) -> Visibility:
        if self.status != "playing":
            return Visibility.HIDDEN
        if self.current_player != player:
            return Visibility.HIDDEN
        if self.game_state.turn_phase != "choose_move":
            return Visibility.HIDDEN
        slot = self._parse_move_slot(action_id)
        if slot is None:
            return Visibility.HIDDEN
        legal = self._get_current_legal_moves(player)
        if slot > len(legal):
            return Visibility.HIDDEN
        return Visibility.VISIBLE

    def _get_move_slot_label(self, player: Player, action_id: str) -> str:
        locale = self._player_locale(player)
        slot = self._parse_move_slot(action_id)
        if slot is None:
            return Localization.get(locale, "sorry-move-slot-fallback")
        legal = self._get_current_legal_moves(player)
        if 1 <= slot <= len(legal):
            return self._move_label(locale, legal[slot - 1])
        return Localization.get(locale, "sorry-move-slot", slot=slot)

    def _action_draw_card(self, player: Player, action_id: str) -> None:
        """Draw a card and transition into move selection/application."""
        _ = action_id
        if self._is_draw_enabled(player) is not None:
            return

        card_face = draw_next_card(self.game_state)
        if card_face is None:
            self._end_turn_after_card(card_face="0")
            return
        self.broadcast_l(
            "sorry-draw-announcement",
            player=player.name,
            card=self._card_display_text("en", card_face),
        )

        legal_moves = self.get_legal_moves_for_card(player, card_face)

        if not legal_moves:
            self.broadcast_l(
                "sorry-no-legal-moves",
                player=player.name,
                card=self._card_display_text("en", card_face),
            )
            discard_current_card(self.game_state)
            self._end_turn_after_card(card_face=card_face)
            return

        if self.options.auto_apply_single_move and len(legal_moves) == 1:
            self.apply_legal_move(player, legal_moves[0])
            self._sync_player_counts()
            if self._has_player_won(player):
                self._finish_game(player)
                return
            discard_current_card(self.game_state)
            self._end_turn_after_card(card_face=card_face)
            return

        self.game_state.turn_phase = "choose_move"
        self.rebuild_all_menus()

    def _action_choose_move(self, player: Player, action_id: str) -> None:
        """Apply the selected move slot."""
        if self._is_move_slot_enabled(player, action_id=action_id) is not None:
            return
        slot = self._parse_move_slot(action_id)
        if slot is None:
            return

        legal = self._get_current_legal_moves(player)
        if slot < 1 or slot > len(legal):
            return
        move = legal[slot - 1]
        card_face = self.game_state.current_card
        if card_face is None:
            return

        self.apply_legal_move(player, move)
        self._announce_move(player, move)
        self._sync_player_counts()
        if self._has_player_won(player):
            self._finish_game(player)
            return

        discard_current_card(self.game_state)
        self._end_turn_after_card(card_face=card_face)

    def on_start(self) -> None:
        """Start the game.

        Milestone 1 scaffold: initialize serializable player/deck state and turn order.
        """
        self._resolve_rules_profile_id()
        rules = self.get_rules_profile()
        self.status = "playing"
        self.game_active = True
        self.round = 0

        active_players = self.get_active_players()
        self.set_turn_players(active_players)
        self.reset_turn_order(announce=False)

        self.game_state = build_initial_game_state(
            [player.id for player in active_players],
            pawns_per_player=rules.pawns_per_player,
            faster_setup_one_pawn_out=self.options.faster_setup_one_pawn_out,
        )

        pawns_in_start = (
            rules.pawns_per_player - 1
            if self.options.faster_setup_one_pawn_out
            else rules.pawns_per_player
        )
        for player in active_players:
            player.pawns_in_start = pawns_in_start
            player.pawns_in_home = 0

        self._start_turn(announce=True)

    def on_tick(self) -> None:
        """Drive bot turns in draw/choose phases."""
        super().on_tick()
        if self.status != "playing":
            return
        current = self.current_player
        if not current or not current.is_bot:
            return
        if self.game_state.turn_phase == "draw":
            self.execute_action(current, "draw_card")
            return
        if self.game_state.turn_phase == "choose_move":
            legal = self._get_current_legal_moves(current)
            if not legal:
                return
            player_state = self.get_player_state(current)
            if player_state is None:
                return
            selected = choose_move(
                self.game_state,
                player_state,
                legal,
                self.get_rules_profile(),
            )
            if selected is None:
                return
            slot_index = next(
                (
                    idx
                    for idx, move in enumerate(legal, start=1)
                    if move.action_id == selected.action_id
                ),
                None,
            )
            if slot_index is None:
                return
            self.execute_action(current, f"move_slot_{slot_index}")
