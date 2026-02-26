"""Expanded Disney/Marvel-family special card behavior tests."""

import pytest

from server.games.monopoly.board_parity import get_board_parity_profile
from server.games.monopoly.game import MonopolyGame, MonopolyOptions
from server.users.test_user import MockUser


DISNEY_MARVEL_FAMILY_BOARD_IDS = [
    "disney_animation",
    "disney_legacy",
    "disney_lightyear",
    "disney_lion_king",
    "disney_mickey_friends",
    "disney_princesses",
    "disney_the_edition",
    "disney_villains",
    "marvel_80_years",
    "marvel_avengers",
    "marvel_avengers_legacy",
    "marvel_black_panther_wf",
    "marvel_deadpool",
    "marvel_eternals",
    "marvel_falcon_winter_soldier",
    "marvel_flip",
    "marvel_spider_man",
    "marvel_super_villains",
]

DISNEY_MARVEL_EXPANDED_CASES = [
    ("disney_animation", 5, "bank_dividend_50", 4, 1300, False),
    ("disney_lightyear", 5, "poor_tax_15", 7, 1588, False),
    ("disney_lion_king", 0, "doctor_fee_pay_50", 2, 1575, False),
    ("disney_mickey_friends", 5, "bank_dividend_50", 0, 1700, False),
    ("disney_villains", 5, "go_back_three", 7, 1568, False),
    ("disney_legacy", 0, "doctor_fee_pay_50", 2, 1710, False),
    ("disney_the_edition", 5, "bank_dividend_50", 10, 1500, True),
    ("marvel_80_years", 5, "poor_tax_15", 7, 1592, False),
    ("marvel_spider_man", 5, "bank_dividend_50", 4, 1300, False),
    ("marvel_black_panther_wf", 0, "doctor_fee_pay_50", 2, 1570, False),
    ("marvel_super_villains", 5, "bank_dividend_50", 10, 1500, True),
    ("marvel_deadpool", 5, "go_back_three", 0, 1700, False),
    ("marvel_avengers_legacy", 0, "doctor_fee_pay_50", 2, 1715, False),
    ("marvel_eternals", 5, "poor_tax_15", 7, 1585, False),
    ("marvel_falcon_winter_soldier", 5, "bank_dividend_50", 4, 1300, False),
    ("marvel_flip", 5, "bank_dividend_50", 10, 1500, True),
]


def _start_board(board_id: str, board_rules_mode: str = "auto") -> MonopolyGame:
    game = MonopolyGame(
        options=MonopolyOptions(
            preset_id="classic_standard",
            board_id=board_id,
            board_rules_mode=board_rules_mode,
        )
    )
    game.add_player("Host", MockUser("Host"))
    game.add_player("Guest", MockUser("Guest"))
    game.host = "Host"
    game.on_start()
    return game


@pytest.mark.parametrize(
    ("board_id", "start_position", "drawn_card", "expected_position", "expected_cash", "expected_in_jail"),
    DISNEY_MARVEL_EXPANDED_CASES,
)
def test_disney_marvel_family_board_rules_uses_board_specific_card_content(
    board_id: str,
    start_position: int,
    drawn_card: str,
    expected_position: int,
    expected_cash: int,
    expected_in_jail: bool,
    monkeypatch,
):
    game = _start_board(board_id)
    host = game.current_player
    assert host is not None

    host.position = start_position
    monkeypatch.setattr(game, "_draw_card", lambda deck_type: drawn_card)
    rolls = iter([1, 1])
    monkeypatch.setattr("server.games.monopoly.game.random.randint", lambda a, b: next(rolls))

    game.execute_action(host, "roll_dice")

    assert host.position == expected_position
    assert host.cash == expected_cash
    assert host.in_jail is expected_in_jail


def test_disney_marvel_family_skin_only_keeps_classic_card_content(monkeypatch):
    game = _start_board("marvel_spider_man", board_rules_mode="skin_only")
    host = game.current_player
    assert host is not None

    host.position = 5
    monkeypatch.setattr(game, "_draw_card", lambda deck_type: "bank_dividend_50")
    rolls = iter([1, 1])
    monkeypatch.setattr("server.games.monopoly.game.random.randint", lambda a, b: next(rolls))

    game.execute_action(host, "roll_dice")

    assert host.position == 7
    assert host.cash == 1550


def test_disney_marvel_family_profiles_use_board_specific_deck_mode():
    for board_id in DISNEY_MARVEL_FAMILY_BOARD_IDS:
        profile = get_board_parity_profile(board_id)
        assert profile is not None
        assert profile.deck_mode == "board_specific"
