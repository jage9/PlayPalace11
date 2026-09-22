"""Shared betting helpers for poker games."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Optional

from . import poker_log

if TYPE_CHECKING:
    from ..games.base import Game


@dataclass
class PotLimitCaps:
    """Pot-limit caps for a bet.

    Attributes:
        total_cap: Maximum total bet size allowed for the action.
    """

    total_cap: int


def compute_pot_limit_caps(
    pot_total: int,
    to_call: int,
    raise_mode: str,
) -> Optional[PotLimitCaps]:
    """Return total bet caps for pot-limit/double-pot modes.

    Args:
        pot_total: Current total pot size.
        to_call: Amount required to call.
        raise_mode: "no_limit", "pot_limit", or "double_pot".

    Returns:
        PotLimitCaps if limits apply, otherwise None.
    """
    if raise_mode == "no_limit":
        return None
    total_cap = pot_total + to_call * 2
    if raise_mode == "double_pot":
        total_cap = pot_total * 2 + to_call * 2
    return PotLimitCaps(total_cap=total_cap)


def clamp_total_to_cap(total: int, caps: Optional[PotLimitCaps]) -> int:
    """Clamp a total bet to a pot-limit cap when present."""
    if not caps:
        return total
    return min(total, caps.total_cap)


def apply_poker_fold(game: "Game", player: Any) -> None:
    """Apply the shared fold action for Hold'em-style poker games."""
    player.folded = True
    game.pot_manager.mark_folded(player.id)
    poker_log.log_fold(game.action_log, player.name)
    game.broadcast_l("poker-player-folds", player=player.name)
    game._after_action()


def apply_poker_call(game: "Game", player: Any) -> None:
    """Apply a call or check for Hold'em-style poker games."""
    to_call = game.betting.amount_to_call(player.id)
    pay = min(player.chips, to_call)
    player.chips -= pay
    if player.chips == 0:
        player.all_in = True
    game.pot_manager.add_contribution(player.id, pay)
    game.betting.record_bet(player.id, pay, is_raise=False)
    if to_call == 0:
        poker_log.log_check(game.action_log, player.name)
        game.broadcast_l("poker-player-checks", player=player.name)
    else:
        game.play_sound("game_3cardpoker/bet.ogg")
        poker_log.log_call(game.action_log, player.name, pay)
        game.broadcast_l("poker-player-calls", player=player.name, amount=pay)
    if player.all_in and pay > 0:
        game.broadcast_l("poker-player-all-in", player=player.name, amount=pay)
    game._sync_team_scores()
    game._after_action()


def apply_poker_all_in(game: "Game", player: Any) -> None:
    """Apply an all-in action while preserving the configured raise cap."""
    amount = player.chips
    if amount <= 0:
        return
    to_call = game.betting.amount_to_call(player.id)
    min_raise = max(game.betting.last_raise_size, 1)
    pay = clamp_total_to_cap(
        amount,
        compute_pot_limit_caps(game.pot_manager.total_pot(), to_call, game.options.raise_mode),
    )
    player.chips -= pay
    player.all_in = player.chips == 0
    game.play_sound("game_3cardpoker/bet.ogg")
    game.pot_manager.add_contribution(player.id, pay)
    raise_amount = pay - to_call
    is_raise = raise_amount >= min_raise and pay > to_call
    game.betting.record_bet(player.id, pay, is_raise=is_raise)
    if pay > to_call:
        poker_log.log_raise(game.action_log, player.name, pay)
        game.broadcast_l("poker-player-raises", player=player.name, amount=pay)
    elif to_call == 0:
        poker_log.log_check(game.action_log, player.name)
        game.broadcast_l("poker-player-checks", player=player.name)
    else:
        poker_log.log_call(game.action_log, player.name, pay)
        game.broadcast_l("poker-player-calls", player=player.name, amount=pay)
    if player.all_in:
        game.broadcast_l("poker-player-all-in", player=player.name, amount=pay)
    game._sync_team_scores()
    game._after_action()
