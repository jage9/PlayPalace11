"""Manual-core behavior tests for Monopoly Junior Super Mario board rules."""

from __future__ import annotations

import pytest

from server.games.monopoly.game import MonopolyGame, MonopolyOptions
from server.users.test_user import MockUser


def _start_manual_board_game(player_count: int = 2) -> MonopolyGame:
    """Start a junior Super Mario board-rules game with N players."""
    game = MonopolyGame(
        options=MonopolyOptions(
            preset_id="classic_standard",
            board_id="junior_super_mario",
            board_rules_mode="auto",
        )
    )
    for index in range(player_count):
        name = f"P{index + 1}"
        game.add_player(name, MockUser(name))
    game.host = "P1"
    game.on_start()
    return game


@pytest.mark.parametrize(
    ("player_count", "expected_cash"),
    (
        (2, 20),
        (3, 18),
        (4, 16),
    ),
)
def test_junior_super_mario_starting_cash_uses_player_count_table(
    player_count: int, expected_cash: int
):
    game = _start_manual_board_game(player_count)

    for player in game.turn_players:
        assert player.cash == expected_cash


def test_junior_super_mario_roll_moves_by_numbered_die_only(monkeypatch):
    game = _start_manual_board_game(2)
    host = game.current_player
    assert host is not None

    host.position = 9
    rolls = iter([4, 6])  # numbered die, power-up die
    monkeypatch.setattr("server.games.monopoly.game.random.randint", lambda a, b: next(rolls))

    game.execute_action(host, "roll_dice")

    assert host.position == 13
    assert game.turn_last_roll == [4, 6]
