"""Integration tests for Monopoly City preset behavior."""

from server.games.monopoly.game import MonopolyGame, MonopolyOptions
from server.users.test_user import MockUser


def _create_two_player_game(options: MonopolyOptions | None = None) -> MonopolyGame:
    game = MonopolyGame(options=options or MonopolyOptions())
    host_user = MockUser("Host")
    guest_user = MockUser("Guest")
    game.add_player("Host", host_user)
    game.add_player("Guest", guest_user)
    game.host = "Host"
    return game


def _start_two_player_city_game() -> MonopolyGame:
    game = _create_two_player_game(MonopolyOptions(preset_id="city"))
    game.on_start()
    return game


def test_city_on_start_initializes_profile_and_engine():
    game = _start_two_player_city_game()
    assert game.city_profile is not None
    assert game.city_engine is not None
    assert game.city_profile.anchor_edition_id == "monopoly-1790"


def test_city_pass_go_updates_progress_and_cash(monkeypatch):
    game = _start_two_player_city_game()
    host = game.current_player
    assert host is not None
    assert game.city_engine is not None

    host.position = 39
    rolls = iter([1, 1])
    monkeypatch.setattr("server.games.monopoly.game.random.randint", lambda a, b: next(rolls))

    game.execute_action(host, "roll_dice")

    assert host.cash == 1700
    assert game.city_engine.progress_for(host.id) >= 200


def test_city_game_finishes_when_anchor_win_condition_met():
    game = _start_two_player_city_game()
    host = game.current_player
    assert host is not None
    assert game.city_engine is not None
    assert game.city_profile is not None

    game.city_engine.record_progress(host.id, game.city_profile.win_threshold)
    game.turn_has_rolled = True

    game.execute_action(host, "end_turn")

    assert game.status == "finished"
    assert game.current_player is not None


def test_city_tie_break_rule_follows_anchor_notes():
    game = _start_two_player_city_game()
    host = game.current_player
    guest = game.players[1]
    assert host is not None
    assert game.city_engine is not None
    assert game.city_profile is not None

    threshold = game.city_profile.win_threshold
    game.city_engine.record_progress(host.id, threshold)
    game.city_engine.record_progress(guest.id, threshold)
    game.turn_has_rolled = True

    game.execute_action(host, "end_turn")

    assert game.status == "finished"
    assert game.current_player is not None
    assert game.current_player.id == host.id
