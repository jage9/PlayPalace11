"""Safety tests for special-board fallback and skin-only invariance."""

from server.games.monopoly.game import MonopolyGame, MonopolyOptions
from server.users.test_user import MockUser


def _start(board_id: str, board_rules_mode: str) -> MonopolyGame:
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


def test_skin_only_mode_bypasses_special_deck_and_audio_paths(monkeypatch):
    game = _start("star_wars_mandalorian", "skin_only")
    game.active_sound_mode = "emulated"

    host = game.current_player
    assert host is not None
    host.position = 5
    monkeypatch.setattr(game, "_draw_card", lambda deck_type: "bank_dividend_50")
    rolls = iter([1, 1])
    monkeypatch.setattr("server.games.monopoly.game.random.randint", lambda a, b: next(rolls))

    game.execute_action(host, "roll_dice")

    assert host.position == 7
    assert host.cash == 1550
    assert game.last_hardware_event_id == ""
    assert game.last_hardware_event_status == "none"


def test_missing_capability_falls_back_without_crash(monkeypatch):
    game = _start("mario_kart", "auto")

    game.active_board_rule_pack_id = "missing_rule_pack"
    game.active_board_deck_mode = "board_specific"

    host = game.current_player
    assert host is not None
    host.position = 5
    monkeypatch.setattr(game, "_draw_card", lambda deck_type: "bank_dividend_50")
    rolls = iter([1, 1])
    monkeypatch.setattr("server.games.monopoly.game.random.randint", lambda a, b: next(rolls))

    game.execute_action(host, "roll_dice")

    assert host.position == 7
    assert host.cash == 1550
    assert game.active_board_deck_mode == "classic"
