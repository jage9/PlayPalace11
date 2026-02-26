"""Integration tests for Wave 1 Monopoly Mario board runtime behavior."""

import pytest

from server.games.monopoly.game import MonopolyGame, MonopolyOptions
from server.users.test_user import MockUser


def _start_two_player_game(options: MonopolyOptions | None = None) -> MonopolyGame:
    game = MonopolyGame(options=options or MonopolyOptions())
    game.add_player("Host", MockUser("Host"))
    game.add_player("Guest", MockUser("Guest"))
    game.host = "Host"
    game.on_start()
    return game


def test_board_rules_auto_applies_pass_go_override(monkeypatch):
    game = _start_two_player_game(
        MonopolyOptions(
            preset_id="classic_standard",
            board_id="mario_kart",
            board_rules_mode="auto",
        )
    )
    host = game.current_player
    assert host is not None

    monkeypatch.setattr(
        "server.games.monopoly.board_rules.mario_kart.PASS_GO_CREDIT_OVERRIDE",
        275,
    )
    host.position = 39
    rolls = iter([1, 1])
    monkeypatch.setattr("server.games.monopoly.game.random.randint", lambda a, b: next(rolls))

    game.execute_action(host, "roll_dice")

    assert host.cash == 1775


@pytest.mark.parametrize(
    ("board_id", "preset_id"),
    (
        ("mario_collectors", "classic_standard"),
        ("mario_kart", "classic_standard"),
        ("mario_celebration", "classic_standard"),
        ("mario_movie", "classic_standard"),
        ("junior_super_mario", "junior"),
    ),
)
def test_wave1_board_starts_with_resolved_mode(board_id: str, preset_id: str):
    game = _start_two_player_game(
        MonopolyOptions(
            preset_id=preset_id,
            board_id=board_id,
            board_rules_mode="auto",
        )
    )
    assert game.active_board_id == board_id
    assert game.active_board_effective_mode == "board_rules"


def test_skin_only_override_disables_board_rule_path(monkeypatch):
    game = _start_two_player_game(
        MonopolyOptions(
            preset_id="classic_standard",
            board_id="mario_kart",
            board_rules_mode="skin_only",
        )
    )
    host = game.current_player
    assert host is not None

    monkeypatch.setattr(
        "server.games.monopoly.board_rules.mario_kart.PASS_GO_CREDIT_OVERRIDE",
        275,
    )
    host.position = 39
    rolls = iter([1, 1])
    monkeypatch.setattr("server.games.monopoly.game.random.randint", lambda a, b: next(rolls))

    game.execute_action(host, "roll_dice")

    assert host.cash == 1700


def test_mario_kart_board_rules_remaps_card_to_advance_to_go(monkeypatch):
    game = _start_two_player_game(
        MonopolyOptions(
            preset_id="classic_standard",
            board_id="mario_kart",
            board_rules_mode="auto",
        )
    )
    host = game.current_player
    assert host is not None

    host.position = 5
    monkeypatch.setattr(game, "_draw_card", lambda deck_type: "bank_dividend_50")
    rolls = iter([1, 1])
    monkeypatch.setattr("server.games.monopoly.game.random.randint", lambda a, b: next(rolls))

    game.execute_action(host, "roll_dice")

    assert host.position == 0
    assert host.cash == 1700


def test_mario_kart_skin_only_keeps_original_card(monkeypatch):
    game = _start_two_player_game(
        MonopolyOptions(
            preset_id="classic_standard",
            board_id="mario_kart",
            board_rules_mode="skin_only",
        )
    )
    host = game.current_player
    assert host is not None

    host.position = 5
    monkeypatch.setattr(game, "_draw_card", lambda deck_type: "bank_dividend_50")
    rolls = iter([1, 1])
    monkeypatch.setattr("server.games.monopoly.game.random.randint", lambda a, b: next(rolls))

    game.execute_action(host, "roll_dice")

    assert host.position == 7
    assert host.cash == 1550
