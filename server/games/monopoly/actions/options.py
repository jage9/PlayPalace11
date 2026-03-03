"""Option helpers for Monopoly turn actions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ...base import Player

if TYPE_CHECKING:
    from ..game import MonopolyGame


def encode_banking_transfer_option(game: MonopolyGame, target: Player, amount: int) -> str:
    """Encode one banking transfer option for menu selection."""
    _ = game
    return f"Transfer {amount} to {target.name} ## target={target.id};amount={amount}"


def parse_banking_transfer_option(game: MonopolyGame, option: str) -> tuple[str, int] | None:
    """Parse one banking transfer option from menu input."""
    _ = game
    if "##" not in option:
        return None
    _, raw_meta = option.split("##", 1)
    meta: dict[str, str] = {}
    for part in raw_meta.strip().split(";"):
        if "=" not in part:
            continue
        key, value = part.split("=", 1)
        meta[key.strip()] = value.strip()

    target_id = meta.get("target", "")
    if not target_id:
        return None
    try:
        amount = int(meta.get("amount", "0"))
    except ValueError:
        return None
    if amount <= 0:
        return None
    return target_id, amount


def options_for_banking_transfer(game: MonopolyGame, player: Player) -> list[str]:
    """Menu options for player-to-player transfers in electronic mode."""
    mono_player = player  # type: ignore[assignment]
    if (
        not game._is_electronic_banking_preset()
        or game.banking_state is None
        or game.banking_profile is None
        or not game.banking_profile.allow_manual_transfers
    ):
        return []

    balance = game._current_liquid_balance(mono_player)
    if balance <= 0:
        return []

    base_amounts = [10, 20, 50, 100, 200, 500]
    options: list[str] = []
    for target in game.turn_players:
        if target.id == mono_player.id or target.bankrupt:
            continue
        target_amounts = sorted(
            {
                amount
                for amount in [*base_amounts, balance]
                if amount > 0 and amount <= balance
            }
        )
        for amount in target_amounts:
            options.append(encode_banking_transfer_option(game, target, amount))
    return options


def options_for_auction_bid(game: MonopolyGame, player: Player) -> list[str]:
    """Menu options for bidding in the active interactive auction."""
    mono_player = player  # type: ignore[assignment]
    current_bidder = game._current_auction_bidder()
    if current_bidder is None or current_bidder.id != mono_player.id:
        return []
    min_bid = game._auction_min_bid()
    if game._current_liquid_balance(mono_player) < min_bid:
        return []

    max_bid = game._current_liquid_balance(mono_player)
    increment = max(1, min_bid - game.pending_auction_current_bid)
    spread_steps = [0, 1, 3, 6]
    options: set[int] = {min_bid, max_bid}
    for step in spread_steps:
        candidate = min(max_bid, min_bid + (step * increment))
        if candidate >= min_bid:
            options.add(candidate)

    return [str(value) for value in sorted(options)]


def bot_select_auction_bid(game: MonopolyGame, player: Player, options: list[str]) -> str | None:
    """Pick a practical bid for bots in interactive auctions."""
    if not options:
        return None
    space = game._pending_auction_space()
    if not space:
        return options[0]

    cap = min(space.price, int(game._current_liquid_balance(player) * 0.85))
    affordable = []
    for option in options:
        try:
            value = int(option)
        except ValueError:
            continue
        if value <= cap:
            affordable.append(value)

    if affordable:
        return str(max(affordable))
    return options[0]


def options_for_mortgage_property(game: MonopolyGame, player: Player) -> list[str]:
    """Menu options for unmortgaged owned properties."""
    mono_player = player  # type: ignore[assignment]
    options: list[str] = []
    for space_id in mono_player.owned_space_ids:
        if game.property_owners.get(space_id) != mono_player.id:
            continue
        if space_id in game.mortgaged_space_ids:
            continue
        space = game.active_space_by_id.get(space_id)
        if not space:
            continue
        if game._is_street_property(space) and game._group_has_any_buildings(space.color_group):
            continue
        options.append(space_id)
    return sorted(options)


def options_for_unmortgage_property(game: MonopolyGame, player: Player) -> list[str]:
    """Menu options for mortgaged owned properties."""
    mono_player = player  # type: ignore[assignment]
    return sorted(
        [
            space_id
            for space_id in mono_player.owned_space_ids
            if game.property_owners.get(space_id) == mono_player.id
            and space_id in game.mortgaged_space_ids
        ]
    )


def options_for_build_house(game: MonopolyGame, player: Player) -> list[str]:
    """Menu options for buildable street properties."""
    mono_player = player  # type: ignore[assignment]
    options: list[str] = []
    for space_id in mono_player.owned_space_ids:
        if game.property_owners.get(space_id) != mono_player.id:
            continue
        space = game.active_space_by_id.get(space_id)
        if not space or not game._is_street_property(space):
            continue
        if space_id in game.mortgaged_space_ids:
            continue
        if game.rule_profile.require_full_set_for_build:
            if not game._owner_has_full_color_set(mono_player.id, space.color_group):
                continue
            if game._group_has_mortgage(space.color_group):
                continue
            levels = game._group_levels(space.color_group)
        else:
            if game._group_has_mortgage(space.color_group, owner_id=mono_player.id):
                continue
            levels = game._group_levels(space.color_group, owner_id=mono_player.id)
        level = game._building_level(space_id)
        if level >= 5:
            continue
        if not game._can_raise_building_level(space_id):
            continue
        if not levels or level != min(levels):
            continue
        if game.rule_profile.builder_block_required_for_build and mono_player.builder_blocks <= 0:
            continue
        if game._current_liquid_balance(mono_player) < space.house_cost:
            continue
        options.append(space_id)
    return sorted(options)


def options_for_sell_house(game: MonopolyGame, player: Player) -> list[str]:
    """Menu options for sellable street properties."""
    mono_player = player  # type: ignore[assignment]
    options: list[str] = []
    for space_id in mono_player.owned_space_ids:
        if game.property_owners.get(space_id) != mono_player.id:
            continue
        space = game.active_space_by_id.get(space_id)
        if not space or not game._is_street_property(space):
            continue
        level = game._building_level(space_id)
        if level <= 0:
            continue
        if not game._can_lower_building_level(space_id):
            continue
        levels = game._group_levels(space.color_group)
        if not levels or level != max(levels):
            continue
        options.append(space_id)
    return sorted(options)


def bot_select_mortgage_property(game: MonopolyGame, player: Player, options: list[str]) -> str | None:
    """Pick the mortgage option that raises the most cash."""
    _ = player
    if not options:
        return None
    return max(
        options,
        key=lambda space_id: game._mortgage_value(game.active_space_by_id[space_id]),
    )


def bot_select_unmortgage_property(
    game: MonopolyGame, player: Player, options: list[str]
) -> str | None:
    """Pick the cheapest affordable unmortgage option."""
    affordable = [
        space_id
        for space_id in options
        if game._current_liquid_balance(player)
        >= game._unmortgage_cost(game.active_space_by_id[space_id])
    ]
    if not affordable:
        return options[0] if options else None
    return min(
        affordable,
        key=lambda space_id: game._unmortgage_cost(game.active_space_by_id[space_id]),
    )


def bot_select_build_house(game: MonopolyGame, player: Player, options: list[str]) -> str | None:
    """Pick the build option with strongest rent gain for cost."""
    if not options:
        return None

    def _score(space_id: str) -> tuple[int, int, str]:
        space = game.active_space_by_id[space_id]
        level = game._building_level(space_id)
        if space.rents:
            current_rent = space.rents[min(level, len(space.rents) - 1)]
            if level == 0 and game._owner_has_full_color_set(player.id, space.color_group):
                current_rent = space.rents[0] * 2
            next_rent = space.rents[min(level + 1, len(space.rents) - 1)]
        else:
            current_rent = space.rent
            next_rent = space.rent
        gain = max(0, next_rent - current_rent)
        return (gain, -space.house_cost, game._space_label(space_id))

    return max(options, key=_score)
