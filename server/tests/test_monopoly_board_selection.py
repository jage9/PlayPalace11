"""Integration tests for Monopoly board selection and preset compatibility."""

from server.games.monopoly.game import MonopolyGame, MonopolyOptions
from server.users.test_user import MockUser


def _start(options: MonopolyOptions) -> MonopolyGame:
    game = MonopolyGame(options=options)
    game.add_player("Host", MockUser("Host"))
    game.add_player("Guest", MockUser("Guest"))
    game.host = "Host"
    game.on_start()
    return game


def test_board_selection_sets_active_board_fields():
    game = _start(MonopolyOptions(preset_id="classic_standard", board_id="mario_kart"))
    assert game.active_board_id == "mario_kart"
    assert game.active_board_effective_mode == "board_rules"


def test_incompatible_board_autofixes_preset():
    game = _start(MonopolyOptions(preset_id="classic_standard", board_id="junior_super_mario"))
    assert game.active_preset_id == "junior"
