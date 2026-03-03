"""Guard helpers for Monopoly turn actions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ....game_utils.actions import Visibility
from ...base import Player

if TYPE_CHECKING:
    from ..game import MonopolyGame


def is_banking_balance_enabled(game: MonopolyGame, player: Player) -> str | None:
    """Enable bank balance checks only for electronic banking preset."""
    error = game.guard_turn_action_enabled(player)
    if error:
        return error
    mono_player = player  # type: ignore[assignment]
    if mono_player.bankrupt:
        return "monopoly-bankrupt-player"
    if not game._is_electronic_banking_preset() or game.banking_state is None:
        return "monopoly-action-disabled-for-preset"
    return None


def is_banking_balance_hidden(game: MonopolyGame, player: Player) -> Visibility:
    """Show bank balance action only in electronic banking mode."""
    return game.turn_action_visibility(
        player,
        extra_condition=game._is_electronic_banking_preset(),
    )


def is_banking_transfer_enabled(game: MonopolyGame, player: Player) -> str | None:
    """Enable manual transfer only when options are available."""
    error = is_banking_balance_enabled(game, player)
    if error:
        return error
    if not game._options_for_banking_transfer(player):
        return "monopoly-not-enough-cash"
    return None


def is_banking_transfer_hidden(game: MonopolyGame, player: Player) -> Visibility:
    """Show transfer action only when electronic transfer options exist."""
    return game.turn_action_visibility(
        player,
        extra_condition=game._is_electronic_banking_preset()
        and bool(game._options_for_banking_transfer(player)),
    )


def is_banking_ledger_enabled(game: MonopolyGame, player: Player) -> str | None:
    """Enable ledger announcements in electronic banking mode."""
    return is_banking_balance_enabled(game, player)


def is_banking_ledger_hidden(game: MonopolyGame, player: Player) -> Visibility:
    """Show ledger action only in electronic banking mode."""
    return game.turn_action_visibility(
        player,
        extra_condition=game._is_electronic_banking_preset(),
    )


def is_voice_command_enabled(game: MonopolyGame, player: Player) -> str | None:
    """Enable voice command entry only for voice banking preset."""
    error = game.guard_turn_action_enabled(player)
    if error:
        return error
    mono_player = player  # type: ignore[assignment]
    if mono_player.bankrupt:
        return "monopoly-bankrupt-player"
    if game.active_preset_id != "voice_banking":
        return "monopoly-action-disabled-for-preset"
    return None


def is_voice_command_hidden(game: MonopolyGame, player: Player) -> Visibility:
    """Show voice command entry only during voice banking games."""
    return game.turn_action_visibility(
        player,
        extra_condition=game.active_preset_id == "voice_banking",
    )


def is_auction_property_enabled(game: MonopolyGame, player: Player) -> str | None:
    """Enable auction action for pending unpurchased property."""
    error = game.guard_turn_action_enabled(player)
    if error:
        return error
    if game._is_auction_active():
        return "monopoly-auction-active"
    if not game.turn_has_rolled:
        return "monopoly-roll-first"
    if game._pending_purchase_space() is None:
        return "monopoly-no-property-to-auction"
    return None


def is_auction_property_hidden(game: MonopolyGame, player: Player) -> Visibility:
    """Show auction only when property purchase is pending."""
    return game.turn_action_visibility(
        player,
        extra_condition=not game._is_auction_active()
        and game.turn_has_rolled
        and game._pending_purchase_space() is not None,
    )


def is_auction_bid_enabled(game: MonopolyGame, player: Player) -> str | None:
    """Enable placing a bid when it is this player's auction turn."""
    error = game.guard_turn_action_enabled(player, require_current_player=False)
    if error:
        return error
    if not game._is_auction_active():
        return "monopoly-no-auction-active"
    mono_player = player  # type: ignore[assignment]
    if mono_player.bankrupt:
        return "monopoly-bankrupt-player"
    current_bidder = game._current_auction_bidder()
    if current_bidder is None or current_bidder.id != mono_player.id:
        return "monopoly-not-your-auction-turn"
    if not game._options_for_auction_bid(player):
        return "monopoly-not-enough-cash"
    return None


def is_auction_bid_hidden(game: MonopolyGame, player: Player) -> Visibility:
    """Show bid action only to the active auction bidder."""
    current_bidder = game._current_auction_bidder()
    return game.turn_action_visibility(
        player,
        require_current_player=False,
        extra_condition=game._is_auction_active()
        and current_bidder is not None
        and current_bidder.id == player.id,
    )


def is_auction_pass_enabled(game: MonopolyGame, player: Player) -> str | None:
    """Enable passing in an active interactive auction."""
    error = game.guard_turn_action_enabled(player, require_current_player=False)
    if error:
        return error
    if not game._is_auction_active():
        return "monopoly-no-auction-active"
    mono_player = player  # type: ignore[assignment]
    if mono_player.bankrupt:
        return "monopoly-bankrupt-player"
    current_bidder = game._current_auction_bidder()
    if current_bidder is None or current_bidder.id != mono_player.id:
        return "monopoly-not-your-auction-turn"
    return None


def is_auction_pass_hidden(game: MonopolyGame, player: Player) -> Visibility:
    """Show pass action only to the active auction bidder."""
    current_bidder = game._current_auction_bidder()
    return game.turn_action_visibility(
        player,
        require_current_player=False,
        extra_condition=game._is_auction_active()
        and current_bidder is not None
        and current_bidder.id == player.id,
    )


def is_mortgage_property_enabled(game: MonopolyGame, player: Player) -> str | None:
    """Enable mortgage action when player owns eligible properties."""
    error = game.guard_turn_action_enabled(player)
    if error:
        return error
    if game._is_junior_preset():
        return "monopoly-action-disabled-for-preset"
    mono_player = player  # type: ignore[assignment]
    if mono_player.bankrupt:
        return "monopoly-bankrupt-player"
    if not game._options_for_mortgage_property(player):
        return "monopoly-no-mortgage-options"
    return None


def is_mortgage_property_hidden(game: MonopolyGame, player: Player) -> Visibility:
    """Show mortgage action when options exist."""
    if game._is_junior_preset():
        return Visibility.HIDDEN
    return game.turn_action_visibility(
        player, extra_condition=bool(game._options_for_mortgage_property(player))
    )


def is_unmortgage_property_enabled(game: MonopolyGame, player: Player) -> str | None:
    """Enable unmortgage action when player has mortgaged properties."""
    error = game.guard_turn_action_enabled(player)
    if error:
        return error
    if game._is_junior_preset():
        return "monopoly-action-disabled-for-preset"
    mono_player = player  # type: ignore[assignment]
    if mono_player.bankrupt:
        return "monopoly-bankrupt-player"
    if not game._options_for_unmortgage_property(player):
        return "monopoly-no-unmortgage-options"
    return None


def is_unmortgage_property_hidden(game: MonopolyGame, player: Player) -> Visibility:
    """Show unmortgage action only when options exist."""
    if game._is_junior_preset():
        return Visibility.HIDDEN
    return game.turn_action_visibility(
        player, extra_condition=bool(game._options_for_unmortgage_property(player))
    )


def is_build_house_enabled(game: MonopolyGame, player: Player) -> str | None:
    """Enable house-building when at least one valid build exists."""
    error = game.guard_turn_action_enabled(player)
    if error:
        return error
    if game._is_junior_preset():
        return "monopoly-action-disabled-for-preset"
    if game.turn_pending_purchase_space_id:
        return "monopoly-resolve-property-first"
    mono_player = player  # type: ignore[assignment]
    if mono_player.bankrupt:
        return "monopoly-bankrupt-player"
    if not game._options_for_build_house(player):
        return "monopoly-no-build-options"
    return None


def is_build_house_hidden(game: MonopolyGame, player: Player) -> Visibility:
    """Show build action when options exist."""
    if game._is_junior_preset():
        return Visibility.HIDDEN
    return game.turn_action_visibility(
        player, extra_condition=bool(game._options_for_build_house(player))
    )


def is_sell_house_enabled(game: MonopolyGame, player: Player) -> str | None:
    """Enable house selling when at least one valid sell exists."""
    error = game.guard_turn_action_enabled(player)
    if error:
        return error
    if game._is_junior_preset():
        return "monopoly-action-disabled-for-preset"
    if game.turn_pending_purchase_space_id:
        return "monopoly-resolve-property-first"
    mono_player = player  # type: ignore[assignment]
    if mono_player.bankrupt:
        return "monopoly-bankrupt-player"
    if not game._options_for_sell_house(player):
        return "monopoly-no-sell-options"
    return None


def is_sell_house_hidden(game: MonopolyGame, player: Player) -> Visibility:
    """Show sell action when options exist."""
    if game._is_junior_preset():
        return Visibility.HIDDEN
    return game.turn_action_visibility(
        player, extra_condition=bool(game._options_for_sell_house(player))
    )
