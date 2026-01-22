from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
import random

from ..base import Game, Player, GameOptions
from ..registry import register_game
from ...game_utils.actions import Action, ActionSet, Visibility, EditboxInput
from ...game_utils.bot_helper import BotHelper
from ...game_utils.game_result import GameResult, PlayerResult
from ...game_utils.options import IntOption, MenuOption, option_field
from ...game_utils.cards import Card, Deck, DeckFactory, read_cards, sort_cards, card_name
from ...game_utils.poker_betting import PokerBettingRound
from ...game_utils.poker_pot import PokerPotManager
from ...game_utils.poker_table import PokerTableState
from ...game_utils.poker_timer import PokerTurnTimer
from ...game_utils.poker_evaluator import best_hand, describe_hand, describe_partial_hand
from ...messages.localization import Localization
from ...ui.keybinds import KeybindState


TURN_TIMER_CHOICES = ["5", "10", "15", "20", "30", "45", "60", "90", "0"]
TURN_TIMER_LABELS = {
    "5": "poker-timer-5",
    "10": "poker-timer-10",
    "15": "poker-timer-15",
    "20": "poker-timer-20",
    "30": "poker-timer-30",
    "45": "poker-timer-45",
    "60": "poker-timer-60",
    "90": "poker-timer-90",
    "0": "poker-timer-unlimited",
}


@dataclass
class FiveCardDrawPlayer(Player):
    hand: list[Card] = field(default_factory=list)
    chips: int = 0
    folded: bool = False
    all_in: bool = False
    bet_this_round: int = 0
    to_discard: set[int] = field(default_factory=set)


@dataclass
class FiveCardDrawOptions(GameOptions):
    starting_chips: int = option_field(
        IntOption(
            default=20000,
            min_val=100,
            max_val=1000000,
            value_key="count",
            label="draw-set-starting-chips",
            prompt="draw-enter-starting-chips",
            change_msg="draw-option-changed-starting-chips",
        )
    )
    ante: int = option_field(
        IntOption(
            default=100,
            min_val=0,
            max_val=1000000,
            value_key="count",
            label="draw-set-ante",
            prompt="draw-enter-ante",
            change_msg="draw-option-changed-ante",
        )
    )
    turn_timer: str = option_field(
        MenuOption(
            choices=TURN_TIMER_CHOICES,
            choice_labels=TURN_TIMER_LABELS,
            default="0",
            label="draw-set-turn-timer",
            prompt="draw-select-turn-timer",
            change_msg="draw-option-changed-turn-timer",
        )
    )
    max_raises: int = option_field(
        IntOption(
            default=0,
            min_val=0,
            max_val=10,
            value_key="count",
            label="draw-set-max-raises",
            prompt="draw-enter-max-raises",
            change_msg="draw-option-changed-max-raises",
        )
    )


@dataclass
@register_game
class FiveCardDrawGame(Game):
    players: list[FiveCardDrawPlayer] = field(default_factory=list)
    options: FiveCardDrawOptions = field(default_factory=FiveCardDrawOptions)
    deck: Deck | None = None
    discard_pile: list[Card] = field(default_factory=list)
    pot_manager: PokerPotManager = field(default_factory=PokerPotManager)
    betting: PokerBettingRound | None = None
    table_state: PokerTableState = field(default_factory=PokerTableState)
    timer: PokerTurnTimer = field(default_factory=PokerTurnTimer)
    hand_number: int = 0
    phase: str = "lobby"
    current_bet_round: int = 0
    action_log: list[tuple[str, dict]] = field(default_factory=list)

    @classmethod
    def get_name(cls) -> str:
        return "Five Card Draw"

    @classmethod
    def get_type(cls) -> str:
        return "fivecarddraw"

    @classmethod
    def get_category(cls) -> str:
        return "category-poker"

    @classmethod
    def get_min_players(cls) -> int:
        return 2

    @classmethod
    def get_max_players(cls) -> int:
        return 5

    def create_player(self, player_id: str, name: str, is_bot: bool = False) -> FiveCardDrawPlayer:
        return FiveCardDrawPlayer(id=player_id, name=name, is_bot=is_bot, chips=0)

    # ==========================================================================
    # Action availability
    # ==========================================================================
    def _is_turn_action_enabled(self, player: Player) -> str | None:
        if self.status != "playing":
            return "action-not-playing"
        if player.is_spectator:
            return "action-spectator"
        if self.current_player != player:
            return "action-not-your-turn"
        return None

    def _is_turn_action_hidden(self, player: Player) -> Visibility:
        if self.status != "playing" or player.is_spectator:
            return Visibility.HIDDEN
        if self.current_player != player:
            return Visibility.HIDDEN
        return Visibility.VISIBLE

    def _is_always_hidden(self, player: Player) -> Visibility:
        return Visibility.HIDDEN

    # ==========================================================================
    # Action sets / keybinds
    # ==========================================================================
    def create_turn_action_set(self, player: FiveCardDrawPlayer) -> ActionSet:
        user = self.get_user(player)
        locale = user.locale if user else "en"
        action_set = ActionSet(name="turn")

        action_set.add(
            Action(
                id="fold",
                label=Localization.get(locale, "poker-fold"),
                handler="_action_fold",
                is_enabled="_is_turn_action_enabled",
                is_hidden="_is_turn_action_hidden",
            )
        )
        action_set.add(
            Action(
                id="call",
                label=Localization.get(locale, "poker-call"),
                handler="_action_call",
                is_enabled="_is_turn_action_enabled",
                is_hidden="_is_turn_action_hidden",
            )
        )
        action_set.add(
            Action(
                id="raise",
                label=Localization.get(locale, "poker-raise"),
                handler="_action_raise",
                is_enabled="_is_turn_action_enabled",
                is_hidden="_is_turn_action_hidden",
                input_request=EditboxInput(
                    prompt="poker-enter-raise",
                    default="",
                    bot_input="_bot_input_raise",
                ),
            )
        )
        action_set.add(
            Action(
                id="all_in",
                label=Localization.get(locale, "poker-all-in"),
                handler="_action_all_in",
                is_enabled="_is_turn_action_enabled",
                is_hidden="_is_turn_action_hidden",
            )
        )
        action_set.add(
            Action(
                id="draw_cards",
                label=Localization.get(locale, "draw-draw-cards"),
                handler="_action_draw_cards",
                is_enabled="_is_draw_enabled",
                is_hidden="_is_draw_hidden",
            )
        )
        for i in range(1, 6):
            action_set.add(
                Action(
                    id=f"toggle_discard_{i}",
                    label=Localization.get(locale, "draw-toggle-discard", index=i),
                    handler="_action_toggle_discard",
                    is_enabled="_is_discard_toggle_enabled",
                    is_hidden="_is_discard_toggle_hidden",
                )
            )
        return action_set

    def create_standard_action_set(self, player: Player) -> ActionSet:
        action_set = super().create_standard_action_set(player)
        user = self.get_user(player)
        locale = user.locale if user else "en"
        action_set.add(
            Action(
                id="check_pot",
                label=Localization.get(locale, "poker-check-pot"),
                handler="_action_check_pot",
                is_enabled="_is_check_enabled",
                is_hidden="_is_check_hidden",
            )
        )
        action_set.add(
            Action(
                id="check_bet",
                label=Localization.get(locale, "poker-check-bet"),
                handler="_action_check_bet",
                is_enabled="_is_check_enabled",
                is_hidden="_is_check_hidden",
            )
        )
        action_set.add(
            Action(
                id="check_min_raise",
                label=Localization.get(locale, "poker-check-min-raise"),
                handler="_action_check_min_raise",
                is_enabled="_is_check_enabled",
                is_hidden="_is_check_hidden",
            )
        )
        action_set.add(
            Action(
                id="check_log",
                label=Localization.get(locale, "poker-check-log"),
                handler="_action_check_log",
                is_enabled="_is_check_enabled",
                is_hidden="_is_check_hidden",
            )
        )
        action_set.add(
            Action(
                id="check_turn_timer",
                label=Localization.get(locale, "poker-check-turn-timer"),
                handler="_action_check_turn_timer",
                is_enabled="_is_check_enabled",
                is_hidden="_is_check_hidden",
            )
        )
        action_set.add(
            Action(
                id="speak_hand",
                label=Localization.get(locale, "poker-read-hand"),
                handler="_action_read_hand",
                is_enabled="_is_check_enabled",
                is_hidden="_is_check_hidden",
            )
        )
        action_set.add(
            Action(
                id="speak_hand_value",
                label=Localization.get(locale, "poker-hand-value"),
                handler="_action_read_hand_value",
                is_enabled="_is_check_enabled",
                is_hidden="_is_check_hidden",
            )
        )
        action_set.add(
            Action(
                id="check_dealer",
                label=Localization.get(locale, "poker-check-dealer"),
                handler="_action_check_dealer",
                is_enabled="_is_check_enabled",
                is_hidden="_is_check_hidden",
            )
        )
        action_set.add(
            Action(
                id="check_position",
                label=Localization.get(locale, "poker-check-position"),
                handler="_action_check_position",
                is_enabled="_is_check_enabled",
                is_hidden="_is_check_hidden",
            )
        )
        for i in range(1, 6):
            action_set.add(
                Action(
                    id=f"speak_card_{i}",
                    label=Localization.get(locale, "poker-read-card", index=i),
                    handler="_action_read_card",
                    is_enabled="_is_check_enabled",
                    is_hidden="_is_always_hidden",
                )
            )
        return action_set

    def setup_keybinds(self) -> None:
        super().setup_keybinds()
        self.define_keybind("p", "Check pot", ["check_pot"], include_spectators=True)
        self.define_keybind("f", "Fold", ["fold"])
        self.define_keybind("c", "Call/Check", ["call"])
        self.define_keybind("r", "Raise", ["raise"])
        self.define_keybind("A", "All in", ["all_in"])
        self.define_keybind("d", "Read hand", ["speak_hand"], include_spectators=False)
        self.define_keybind("g", "Hand value", ["speak_hand_value"], include_spectators=False)
        self.define_keybind("x", "Dealer", ["check_dealer"], include_spectators=True)
        self.define_keybind("z", "Position", ["check_position"], include_spectators=True)
        self.define_keybind("b", "Current bet", ["check_bet"], include_spectators=True)
        self.define_keybind("m", "Minimum raise", ["check_min_raise"], include_spectators=True)
        self.define_keybind("l", "Action log", ["check_log"], include_spectators=True)
        self.define_keybind("T", "Turn timer", ["check_turn_timer"], include_spectators=True)
        for i in range(1, 6):
            self.define_keybind(str(i), f"Read card {i}", [f"speak_card_{i}"], include_spectators=False)

    # ==========================================================================
    # Game flow
    # ==========================================================================
    def on_start(self) -> None:
        self.status = "playing"
        self.game_active = True
        for player in self.players:
            player.chips = self.options.starting_chips
        self._team_manager.team_mode = "individual"
        self._team_manager.setup_teams([p.name for p in self.players])
        self._sync_team_scores()
        self.set_turn_players(self.get_active_players())
        self.play_music("game_3cardpoker/mus.ogg")
        self._start_new_hand()

    def _start_new_hand(self) -> None:
        self.hand_number += 1
        self.phase = "deal"
        self.action_log = []
        self.current_bet_round = 0
        self.pot_manager.reset()
        self.discard_pile = []
        self.deck, _ = DeckFactory.standard_deck()
        self.deck.shuffle()

        active = [p for p in self.get_active_players() if p.chips > 0]
        if len(active) <= 1:
            self._end_game(active[0] if active else None)
            return

        self.table_state.advance_button([p.id for p in active])
        for p in active:
            p.hand = []
            p.folded = False
            p.all_in = False
            p.bet_this_round = 0
            p.to_discard = set()

        self.play_sound("game_cards/small_shuffle.ogg")
        self._post_ante(active)
        self._deal_cards(active, 5)
        self._start_betting_round(start_index=-1)

    def _post_ante(self, active: list[FiveCardDrawPlayer]) -> None:
        ante = self.options.ante
        if ante <= 0:
            return
        self.play_sound("game_3cardpoker/bet.ogg")
        for p in active:
            pay = min(p.chips, ante)
            p.chips -= pay
            if p.chips == 0:
                p.all_in = True
            self.pot_manager.add_contribution(p.id, pay)
        self._sync_team_scores()
        self.broadcast_l("draw-antes-posted", amount=ante)

    def _deal_cards(self, players: list[FiveCardDrawPlayer], count: int) -> None:
        if not players:
            return
        start_index = (self.table_state.button_index + 1) % len(players)
        order = players[start_index:] + players[:start_index]
        delay_ticks = 0
        for _ in range(count):
            for p in order:
                card = self.deck.draw_one() if self.deck else None
                if card:
                    p.hand.append(card)
            sound = f"game_cards/draw{random.randint(1,4)}.ogg"
            self.schedule_sound(sound, delay_ticks, volume=70)
            delay_ticks += 6
        for p in players:
            p.hand = sort_cards(p.hand)

    def _start_betting_round(self, start_index: int) -> None:
        self.current_bet_round += 1
        active_ids = [p.id for p in self.get_active_players() if p.chips > 0 and not p.folded]
        order = [p.id for p in self.get_active_players() if p.id in active_ids]
        self.betting = PokerBettingRound(
            order=order, max_raises=self.options.max_raises or None
        )
        self.betting.reset()
        if not order:
            self._showdown()
            return
        if start_index < 0:
            # default: left of button
            start_index = (self.table_state.button_index + 1) % len(order)
        self._set_turn_by_index(start_index, order)
        self._announce_betting_round()

    def _announce_betting_round(self) -> None:
        if self.current_bet_round == 1:
            self.broadcast_l("draw-betting-round-1")
        else:
            self.broadcast_l("draw-betting-round-2")

    def _set_turn_by_index(self, start_index: int, order: list[str]) -> None:
        if not order:
            return
        idx = start_index % len(order)
        self.turn_player_ids = order
        self.turn_index = idx
        self._start_turn()

    def _start_turn(self) -> None:
        player = self.current_player
        if not player:
            return
        p = player if isinstance(player, FiveCardDrawPlayer) else None
        if not p or p.folded or (p.all_in and self.phase != "draw"):
            self._advance_turn()
            return
        if self.phase == "draw" and p.is_bot and p.all_in:
            self.bot_think(p)
            self._action_draw_cards(p, "draw_cards")
            return
        self.announce_turn(turn_sound="game_3cardpoker/turn.ogg")
        if p.is_bot:
            BotHelper.jolt_bot(p, ticks=random.randint(5, 10))
        self._start_turn_timer()
        self.rebuild_all_menus()

    def _advance_turn(self) -> None:
        if not self.betting:
            return
        active_ids = self._active_betting_ids()
        next_id = self.betting.next_player(self.current_player.id if self.current_player else None, active_ids)
        if next_id is None:
            return
        self.turn_index = self.turn_player_ids.index(next_id)
        self._start_turn()

    def _start_turn_timer(self) -> None:
        try:
            seconds = int(self.options.turn_timer)
        except ValueError:
            seconds = 0
        if seconds <= 0:
            self.timer.clear()
            return
        self.timer.start(seconds)

    def on_tick(self) -> None:
        super().on_tick()
        if not self.game_active:
            return
        if self.timer.tick():
            self._handle_turn_timeout()
        BotHelper.on_tick(self)

    def bot_think(self, player: FiveCardDrawPlayer) -> str | None:
        if self.current_player != player:
            return None
        if self.phase == "draw":
            if len(player.hand) >= 5:
                score, _ = best_hand(player.hand)
                category = score[0]
            else:
                category = 0
            ranks = [card.rank for card in player.hand]
            counts = {}
            for r in ranks:
                counts[r] = counts.get(r, 0) + 1
            # Determine discard indices based on hand strength
            keep_ranks: set[int] = set()
            if category >= 4:  # straight or better
                keep_ranks = set(ranks)
            elif category == 3:  # three of a kind
                keep_ranks = {r for r, c in counts.items() if c == 3}
            elif category == 2:  # two pair
                keep_ranks = {r for r, c in counts.items() if c == 2}
            elif category == 1:  # one pair
                keep_ranks = {r for r, c in counts.items() if c == 2}
            else:  # high card
                keep_ranks = set()

            discard_indices = [i for i, card in enumerate(player.hand) if card.rank not in keep_ranks]
            max_discards = 4 if any(card.rank == 1 for card in player.hand) else 3
            if len(discard_indices) > max_discards:
                discard_indices = discard_indices[:max_discards]
            player.to_discard = set(discard_indices)
            return "draw_cards"
        if self.betting:
            to_call = self.betting.amount_to_call(player.id)
            if len(player.hand) >= 5:
                score, _ = best_hand(player.hand)
                category = score[0]
            else:
                category = 0
            min_raise = max(self.betting.last_raise_size, 1)
            can_raise = self.betting.can_raise() and (to_call + min_raise) <= player.chips
            if to_call == 0:
                if can_raise and category >= 1:
                    return "raise"
                return "call"
            # Simple strength check
            if to_call >= player.chips:
                return "call"
            if category >= 2 and to_call <= max(1, player.chips // 6):
                return "call"
            if category >= 1 and to_call <= max(1, player.chips // 12):
                return "call"
            if to_call <= max(1, player.chips // 25):
                return "call"
            return "fold"
        return None

    # ==========================================================================
    # Action handlers
    # ==========================================================================
    def _action_fold(self, player: Player, action_id: str) -> None:
        p = self._require_active_player(player)
        if not p:
            return
        p.folded = True
        self.pot_manager.mark_folded(p.id)
        self.action_log.append(("poker-log-fold", {"player": p.name}))
        self.broadcast_l("poker-player-folds", player=p.name)
        self._after_action()

    def _action_call(self, player: Player, action_id: str) -> None:
        p = self._require_active_player(player)
        if not p or not self.betting:
            return
        to_call = self.betting.amount_to_call(p.id)
        pay = min(p.chips, to_call)
        p.chips -= pay
        if p.chips == 0:
            p.all_in = True
        self.pot_manager.add_contribution(p.id, pay)
        self.betting.record_bet(p.id, pay, is_raise=False)
        if to_call == 0:
            self.action_log.append(("poker-log-check", {"player": p.name}))
            self.broadcast_l("poker-player-checks", player=p.name)
        else:
            self.play_sound("game_3cardpoker/bet.ogg")
            self.action_log.append(("poker-log-call", {"player": p.name, "amount": pay}))
            self.broadcast_l("poker-player-calls", player=p.name, amount=pay)
        self._sync_team_scores()
        self._after_action()

    def _action_raise(self, player: Player, amount_str: str, action_id: str) -> None:
        p = self._require_active_player(player)
        if not p or not self.betting:
            return
        try:
            amount = int(amount_str)
        except ValueError:
            return
        if amount <= 0:
            return
        if not self.betting.can_raise():
            self.broadcast_l("poker-raise-cap-reached")
            return
        min_raise = max(self.betting.last_raise_size, 1)
        if amount > p.chips:
            self.broadcast_personal_l(p, "poker-raise-too-large", "poker-raise-too-large")
            return
        if amount == p.chips:
            self._action_all_in(p, "all_in")
            return
        if amount < min_raise:
            self.broadcast_l("poker-raise-too-small", amount=min_raise)
            return
        to_call = self.betting.amount_to_call(p.id)
        total = to_call + amount
        if total > p.chips:
            total = p.chips
        if total < to_call + min_raise:
            # Treat short stack as all-in (does not reopen betting)
            self._action_all_in(p, "all_in")
            return
        p.chips -= total
        if p.chips == 0:
            p.all_in = True
        self.play_sound("game_3cardpoker/bet.ogg")
        self.pot_manager.add_contribution(p.id, total)
        self.betting.record_bet(p.id, total, is_raise=True)
        self.action_log.append(("poker-log-raise", {"player": p.name, "amount": total}))
        self.broadcast_l("poker-player-raises", player=p.name, amount=total)
        self._sync_team_scores()
        self._after_action()

    def _bot_input_raise(self, player: Player) -> str:
        if isinstance(player, FiveCardDrawPlayer):
            if not self.betting:
                return "1"
            to_call = self.betting.amount_to_call(player.id)
            min_raise = max(self.betting.last_raise_size, 1)
            max_raise = max(0, player.chips - to_call)
            if max_raise < min_raise:
                return str(min_raise)
            desired = max(min_raise, min(100, player.chips // 3))
            amount = min(desired, max_raise)
            return str(amount)
        return "1"

    def _action_all_in(self, player: Player, action_id: str) -> None:
        p = self._require_active_player(player)
        if not p or not self.betting:
            return
        amount = p.chips
        if amount <= 0:
            return
        to_call = self.betting.amount_to_call(p.id)
        min_raise = max(self.betting.last_raise_size, 1)
        pay = amount
        if self.betting and self.betting.max_raises == 1:
            pot_total = self.pot_manager.total_pot()
            cap = pot_total + to_call * 2
            pay = min(pay, cap)
        p.chips -= pay
        p.all_in = p.chips == 0
        self.play_sound("game_3cardpoker/bet.ogg")
        self.pot_manager.add_contribution(p.id, pay)
        raise_amount = pay - to_call
        is_raise = raise_amount >= min_raise and pay > to_call
        self.betting.record_bet(p.id, pay, is_raise=is_raise)
        if pay > to_call:
            self.action_log.append(("poker-log-raise", {"player": p.name, "amount": pay}))
            self.broadcast_l("poker-player-raises", player=p.name, amount=pay)
        elif to_call == 0:
            self.action_log.append(("poker-log-check", {"player": p.name}))
            self.broadcast_l("poker-player-checks", player=p.name)
        else:
            self.action_log.append(("poker-log-call", {"player": p.name, "amount": pay}))
            self.broadcast_l("poker-player-calls", player=p.name, amount=pay)
        self._sync_team_scores()
        self._after_action()

    def _action_draw_cards(self, player: Player, action_id: str) -> None:
        p = self._require_active_player(player)
        if not p or self.phase != "draw":
            return
        if not p.to_discard:
            self.broadcast_personal_l(p, "draw-you-stand-pat", "draw-player-stands-pat")
            self._advance_after_draw(p)
            return
        indices = sorted(p.to_discard)
        for idx in reversed(indices):
            if 0 <= idx < len(p.hand):
                self.discard_pile.append(p.hand.pop(idx))
        for _ in range(len(indices)):
            card = self.deck.draw_one() if self.deck else None
            if card:
                p.hand.append(card)
        p.hand = sort_cards(p.hand)
        self._play_draw_sounds(len(indices))
        self.broadcast_personal_l(p, "draw-you-draw", "draw-player-draws", count=len(indices))
        p.to_discard = set()
        self._advance_after_draw(p)

    def _action_toggle_discard(self, player: Player, action_id: str) -> None:
        p = self._require_active_player(player)
        if not p or self.phase != "draw":
            return
        try:
            idx = int(action_id.split("_")[-1]) - 1
        except ValueError:
            return
        if idx < 0 or idx >= len(p.hand):
            return
        if idx in p.to_discard:
            p.to_discard.remove(idx)
        else:
            max_discards = 4 if any(card.rank == 1 for card in p.hand) else 3
            if len(p.to_discard) >= max_discards:
                self.broadcast_personal_l(
                    p, "draw-you-discard-limit", "draw-player-discard-limit", count=max_discards
                )
                return
            p.to_discard.add(idx)
        self.rebuild_all_menus()

    # ==========================================================================
    # Action helpers
    # ==========================================================================
    def _after_action(self) -> None:
        if not self.betting:
            return
        active_ids = self._active_betting_ids()
        if len(active_ids) <= 1:
            self._award_uncontested(active_ids)
            return
        if active_ids and active_ids.issubset(self._all_in_ids()):
            if self.current_bet_round == 1:
                self.phase = "draw"
                self._start_draw_phase()
            else:
                self._showdown()
            return
        if self.betting.is_complete(active_ids, self._all_in_ids()):
            if self.current_bet_round == 1:
                self.phase = "draw"
                self._start_draw_phase()
            else:
                self._showdown()
            return
        self._advance_turn()

    def _start_draw_phase(self) -> None:
        self.broadcast_l("draw-begin-draw")
        self.turn_player_ids = [p.id for p in self.get_active_players() if not p.folded]
        self.turn_index = 0
        self._start_turn()

    def _advance_after_draw(self, player: FiveCardDrawPlayer) -> None:
        if self.current_player != player:
            return
        self.advance_turn(announce=False)
        if self.current_player is None or (
            self.current_player and self.current_player.id == self.turn_player_ids[0]
        ):
            self.phase = "bet2"
            self._start_betting_round(start_index=0)
        else:
            self._start_turn()

    def _showdown(self) -> None:
        self.phase = "showdown"
        self.broadcast_l("poker-showdown")
        self._resolve_pots()
        self._start_new_hand()

    def _award_uncontested(self, active_ids: set[str]) -> None:
        winner = self.get_player_by_id(next(iter(active_ids))) if active_ids else None
        if not winner:
            return
        amount = self.pot_manager.total_pot()
        if isinstance(winner, FiveCardDrawPlayer):
            winner.chips += amount
        self.play_sound(random.choice(["game_blackjack/win1.ogg", "game_blackjack/win2.ogg", "game_blackjack/win3.ogg"]))
        self.broadcast_l("poker-player-wins-pot", player=winner.name, amount=amount)
        self._sync_team_scores()
        self._start_new_hand()

    def _resolve_pots(self) -> None:
        pots = self.pot_manager.get_pots()
        for pot in pots:
            eligible_players = [self.get_player_by_id(pid) for pid in pot.eligible_player_ids]
            eligible_players = [p for p in eligible_players if isinstance(p, FiveCardDrawPlayer)]
            if not eligible_players:
                continue
            best_score = None
            winners: list[FiveCardDrawPlayer] = []
            for p in eligible_players:
                score, _ = best_hand(p.hand)
                if best_score is None or score > best_score:
                    best_score = score
                    winners = [p]
                elif score == best_score:
                    winners.append(p)
            if not best_score:
                continue
            share = pot.amount // len(winners)
            remainder = pot.amount % len(winners)
            ordered_winners = self._order_winners_by_button(winners)
            for w in ordered_winners:
                w.chips += share
            if remainder > 0:
                ordered_winners[0].chips += remainder
            desc = describe_hand(best_score, "en")
            if len(winners) == 1:
                self.play_sound(random.choice(["game_blackjack/win1.ogg", "game_blackjack/win2.ogg", "game_blackjack/win3.ogg"]))
                self.broadcast_l("poker-player-wins-pot-hand", player=winners[0].name, amount=pot.amount, hand=desc)
            else:
                names = ", ".join(w.name for w in winners)
                self.play_sound(random.choice(["game_blackjack/win1.ogg", "game_blackjack/win2.ogg", "game_blackjack/win3.ogg"]))
                self.broadcast_l("poker-players-split-pot", players=names, amount=pot.amount, hand=desc)
        self._sync_team_scores()

    def _order_winners_by_button(self, winners: list[FiveCardDrawPlayer]) -> list[FiveCardDrawPlayer]:
        if len(winners) <= 1:
            return winners
        active_ids = [p.id for p in self.get_active_players()]
        if not active_ids:
            return winners
        button_id = self.table_state.get_button_id(active_ids)
        if button_id in active_ids:
            start_index = (active_ids.index(button_id) + 1) % len(active_ids)
            order = active_ids[start_index:] + active_ids[:start_index]
        else:
            order = active_ids
        return sorted(winners, key=lambda p: order.index(p.id) if p.id in order else len(order))

    # ==========================================================================
    # Utility / status actions
    # ==========================================================================
    def _action_check_pot(self, player: Player, action_id: str) -> None:
        user = self.get_user(player)
        if not user:
            return
        pots = self.pot_manager.get_pots()
        if not pots:
            user.speak_l("poker-pot-total", amount=0)
            return
        user.speak_l("poker-pot-total", amount=self.pot_manager.total_pot())
        if pots:
            user.speak_l("poker-pot-main", amount=pots[0].amount)
        for idx, pot in enumerate(pots[1:], start=1):
            user.speak_l("poker-pot-side", index=idx, amount=pot.amount)

    def _action_check_bet(self, player: Player, action_id: str) -> None:
        if not self.betting:
            return
        to_call = self.betting.amount_to_call(player.id)
        user = self.get_user(player)
        if user:
            user.speak_l("poker-to-call", amount=to_call)

    def _action_check_min_raise(self, player: Player, action_id: str) -> None:
        if not self.betting:
            return
        min_raise = max(self.betting.last_raise_size, 1)
        user = self.get_user(player)
        if user:
            user.speak_l("poker-min-raise", amount=min_raise)

    def _action_check_log(self, player: Player, action_id: str) -> None:
        user = self.get_user(player)
        if user:
            if not self.action_log:
                user.speak_l("poker-log-empty")
            else:
                lines = [Localization.get(user.locale, mid, **kwargs) for mid, kwargs in self.action_log]
                user.speak(", ".join(lines))

    def _action_read_hand(self, player: Player, action_id: str) -> None:
        p = player if isinstance(player, FiveCardDrawPlayer) else None
        if not p:
            return
        user = self.get_user(player)
        if user:
            user.speak_l("poker-your-hand", cards=read_cards(p.hand, user.locale))

    def _action_read_hand_value(self, player: Player, action_id: str) -> None:
        p = player if isinstance(player, FiveCardDrawPlayer) else None
        if not p:
            return
        user = self.get_user(player)
        if user:
            desc = describe_partial_hand(p.hand, user.locale)
            user.speak(desc)

    def _action_read_card(self, player: Player, action_id: str) -> None:
        p = player if isinstance(player, FiveCardDrawPlayer) else None
        if not p:
            return
        try:
            idx = int(action_id.split("_")[-1]) - 1
        except ValueError:
            return
        if idx < 0 or idx >= len(p.hand):
            return
        user = self.get_user(player)
        if user:
            user.speak(card_name(p.hand[idx], user.locale))

    def _action_check_turn_timer(self, player: Player, action_id: str) -> None:
        user = self.get_user(player)
        if not user:
            return
        remaining = self.timer.seconds_remaining()
        if remaining <= 0:
            user.speak_l("poker-timer-disabled")
        else:
            user.speak_l("poker-timer-remaining", seconds=remaining)

    def _action_check_dealer(self, player: Player, action_id: str) -> None:
        user = self.get_user(player)
        if not user:
            return
        active = [p for p in self.get_active_players() if p.chips > 0 or p.all_in]
        dealer_id = self.table_state.get_button_id([p.id for p in active])
        dealer_player = self.get_player_by_id(dealer_id) if dealer_id else None
        if dealer_player:
            user.speak_l("poker-dealer-is", player=dealer_player.name)

    def _action_check_position(self, player: Player, action_id: str) -> None:
        user = self.get_user(player)
        if not user:
            return
        active = [p for p in self.get_active_players() if p.chips > 0 or p.all_in]
        if not active:
            return
        dealer_id = self.table_state.get_button_id([p.id for p in active])
        order = [p.id for p in active]
        if dealer_id and player.id in order:
            idx = (order.index(player.id) - order.index(dealer_id)) % len(order)
            user.speak_l("poker-position-dealer", position=idx)

    # ==========================================================================
    # Helpers
    # ==========================================================================
    def _active_betting_ids(self) -> set[str]:
        return {
            p.id
            for p in self.get_active_players()
            if isinstance(p, FiveCardDrawPlayer) and not p.folded and (p.chips > 0 or p.all_in)
        }

    def _all_in_ids(self) -> set[str]:
        return {p.id for p in self.get_active_players() if isinstance(p, FiveCardDrawPlayer) and p.all_in}

    def _require_active_player(self, player: Player) -> FiveCardDrawPlayer | None:
        if not isinstance(player, FiveCardDrawPlayer):
            return None
        if self.current_player != player:
            return None
        if player.folded:
            return None
        return player

    def _is_draw_enabled(self, player: Player) -> str | None:
        if self.phase != "draw":
            return "action-not-playing"
        return self._is_turn_action_enabled(player)

    def _is_draw_hidden(self, player: Player) -> Visibility:
        if self.phase != "draw":
            return Visibility.HIDDEN
        return self._is_turn_action_hidden(player)

    def _is_discard_toggle_enabled(self, player: Player) -> str | None:
        if self.phase != "draw":
            return "action-not-playing"
        return self._is_turn_action_enabled(player)

    def _is_discard_toggle_hidden(self, player: Player) -> Visibility:
        if self.phase != "draw":
            return Visibility.HIDDEN
        return self._is_turn_action_hidden(player)

    def _is_check_enabled(self, player: Player) -> str | None:
        if self.status != "playing":
            return "action-not-playing"
        return None

    def _is_check_hidden(self, player: Player) -> Visibility:
        return Visibility.HIDDEN

    def _handle_turn_timeout(self) -> None:
        player = self.current_player
        if not isinstance(player, FiveCardDrawPlayer):
            return
        if self.betting and self.betting.amount_to_call(player.id) > 0:
            self._action_fold(player, "fold")
        else:
            self._action_call(player, "call")

    def _play_draw_sounds(self, count: int) -> None:
        delay_ticks = 0
        for _ in range(count):
            self.schedule_sound(f"game_cards/draw{random.randint(1,4)}.ogg", delay_ticks, volume=70)
            delay_ticks += 6

    def _sync_team_scores(self) -> None:
        for team in self._team_manager.teams:
            team.total_score = 0
        for p in self.players:
            team = self._team_manager.get_team(p.name)
            if team:
                team.total_score = p.chips

    def build_game_result(self) -> GameResult:
        active = self.get_active_players()
        winner = max(active, key=lambda p: p.chips, default=None)
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
                for p in active
            ],
            custom_data={
                "winner_name": winner.name if winner else None,
                "winner_chips": winner.chips if winner else 0,
            },
        )

    def _end_game(self, winner: FiveCardDrawPlayer | None) -> None:
        self.play_sound(random.choice(["game_blackjack/win1.ogg", "game_blackjack/win2.ogg"]))
        if winner:
            self.broadcast_l("poker-player-wins-game", player=winner.name)
        self.finish_game()
