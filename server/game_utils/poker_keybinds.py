from __future__ import annotations

from server.core.ui.keybinds import KeybindState


def setup_poker_keybinds(
    game,
    *,
    check_pot: str = "check_pot",
    fold: str = "fold",
    call: str = "call",
    raise_action: str = "raise",
    all_in: str = "all_in",
    read_hand: str = "speak_hand",
    hand_value: str = "speak_hand_value",
    check_dealer: str = "check_button",
    dealer_label: str = "Dealer/Button",
    check_position: str = "check_position",
    check_bet: str = "check_bet",
    check_min_raise: str = "check_min_raise",
    check_hand_players: str = "check_hand_players",
    check_turn_timer: str = "check_turn_timer",
    turn_timer_key: str = "shift+t",
    read_table: str | None = None,
    check_blind_timer: str | None = None,
    reveal_both: str | None = None,
    reveal_first: str | None = None,
    reveal_second: str | None = None,
    read_cards_count: int = 0,
    draw_cards: str | None = None,
) -> None:
    """Define standard poker keybinds on a game instance.

    Args:
        game: Game instance with define_keybind method.
        check_pot: Action id for pot check.
        fold: Action id for fold.
        call: Action id for call/check.
        raise_action: Action id for raise.
        all_in: Action id for all-in.
        read_hand: Action id for reading hand.
        hand_value: Action id for hand value.
        check_dealer: Action id for dealer/button check.
        dealer_label: Label for dealer/button keybind.
        check_position: Action id for position check.
        check_bet: Action id for current bet check.
        check_min_raise: Action id for min-raise check.
        check_hand_players: Action id for players-in-hand.
        check_turn_timer: Action id for turn timer check.
        turn_timer_key: Keybind string for timer check.
        read_table: Optional action id for reading table.
        check_blind_timer: Optional action id for blind timer.
        reveal_both: Optional action id for reveal both.
        reveal_first: Optional action id for reveal first.
        reveal_second: Optional action id for reveal second.
        read_cards_count: Number of per-card read actions to bind.
        draw_cards: Optional action id for draw cards.
    """
    game.define_keybind("p", "Check pot", [check_pot], include_spectators=True)
    game.define_keybind("f", "Fold", [fold])
    game.define_keybind("c", "Call/Check", [call])
    game.define_keybind("r", "Raise", [raise_action])
    game.define_keybind("shift+a", "All in", [all_in])
    game.define_keybind("w", "Read hand", [read_hand], include_spectators=False)
    game.define_keybind("g", "Hand value", [hand_value], include_spectators=False)
    game.define_keybind("x", dealer_label, [check_dealer], include_spectators=True)
    game.define_keybind("z", "Position", [check_position], include_spectators=True)
    game.define_keybind("n", "Current bet", [check_bet], include_spectators=True)
    game.define_keybind("m", "Minimum raise", [check_min_raise], include_spectators=True)
    game.define_keybind("h", "Players in hand", [check_hand_players], include_spectators=True)
    game.define_keybind(
        turn_timer_key,
        "Turn timer",
        [check_turn_timer],
        include_spectators=True,
    )
    if read_table:
        game.define_keybind("e", "Read table", [read_table], include_spectators=True)
    if check_blind_timer:
        game.define_keybind("v", "Blind timer", [check_blind_timer], include_spectators=True)
    if draw_cards:
        game.define_keybind("d", "Draw cards", [draw_cards], state=KeybindState.ACTIVE)
    if reveal_both:
        game.define_keybind("o", "Reveal both", [reveal_both], include_spectators=False)
    if reveal_first:
        game.define_keybind("u", "Reveal first", [reveal_first], include_spectators=False)
    if reveal_second:
        game.define_keybind("i", "Reveal second", [reveal_second], include_spectators=False)
    for i in range(1, read_cards_count + 1):
        game.define_keybind(str(i), f"Read card {i}", [f"speak_card_{i}"], include_spectators=False)
