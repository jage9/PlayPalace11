"""Roulette session checks through real tables, games, and saved state."""

from unittest.mock import Mock

import pytest

from server.core.tables.table import Table
from server.core.users.test_user import MockUser
from server.game_utils.game_result import GameResult, PlayerResult
from server.game_utils.game_status import GameStatus
from server.game_utils.roulette import RouletteSession
from server.games.registry import GameRegistry
from server.games.roulette.game import RouletteGame
from server.games.roulette.options import RouletteOptions


def make_table(count=2):
    table = Table("roulette-test", "roulette", "Alice")
    game = RouletteGame()
    game._table = table
    game.host = "Alice"
    game.setup_keybinds()
    for name in ["Alice", *[f"Guest{i}" for i in range(count - 1)]]:
        user = MockUser(name)
        table.add_member(name, user)
        game.add_player(name, user)
    table.game = game
    return table


def advance_selection(table, ticks=200):
    for _ in range(ticks):
        table.on_tick()


def test_options_defaults_and_exclusive_limits():
    options = RouletteOptions()
    assert options.total_rounds == 7 and options.target_score == 2000
    assert options.jokers == 1
    joker_option = options.get_option_metas()["jokers"]
    assert joker_option.validate_and_convert("0") == (True, 0)
    assert joker_option.validate_and_convert("10") == (True, 10)
    assert joker_option.validate_and_convert("-1") == (True, 0)
    assert joker_option.validate_and_convert("11") == (True, 10)
    assert set(options.included_games) == {cls.get_type() for cls in GameRegistry.get_all()
                                           if cls is not RouletteGame}
    assert options._is_option_visible("total_rounds")
    assert not options._is_option_visible("target_score")
    options.finish_mode = "score"
    assert options._is_option_visible("target_score")
    assert not options._is_option_visible("total_rounds")


def test_session_switches_games_restores_and_finishes_once():
    table = make_table()
    table._server = Mock()
    lobby = table.game
    lobby.options.included_games = ["pig", "chess"]
    lobby.options.total_rounds = 2
    ids = [p.id for p in lobby.players]
    lobby.on_start()
    advance_selection(table)
    first = table.game
    assert first.game_active and first.roulette.round_number == 1
    assert table.listing_game_type == "roulette" and table.game_type == first.get_type()
    assert [p.id for p in first.players] == ids
    assert first.finish_round(winner_ids=[ids[0]])
    first.finish_game()
    assert first.roulette.scores[ids[0]] == 1
    table._server.on_game_result.assert_not_called()

    restored = type(first).from_json(first.to_json())
    restored.rebuild_runtime_state()
    restored._table = table
    for player in restored.players:
        restored.attach_user(player.id, first.get_user(player))
    table.game = restored
    guest = restored.players[1]
    restored.handle_event(guest, {"type": "menu", "menu_id": "game_over",
                                  "selection_id": "roulette_next"})
    assert table.game is restored
    restored.handle_event(restored.players[0], {"type": "menu", "menu_id": "game_over",
                                               "selection_id": "roulette_next"})
    advance_selection(table)
    second = table.game
    assert second.get_type() != first.get_type()
    assert second.roulette.round_number == 2 and second.game_active
    second.finish_round(winner_ids=[ids[1]])
    assert second.roulette.finished
    assert second.roulette.scores == dict.fromkeys(ids, 1)
    table._server.on_game_result.assert_called_once()
    result = table._server.on_game_result.call_args.args[0]
    assert result.game_type == "roulette" and set(result.get_winner_ids()) == set(ids)
    assert not table.start_roulette_round()
    assert table.prepare_next_game("Alice", "roulette")
    assert table.game.options.included_games == ["pig", "chess"]
    assert table.game.options.total_rounds == 2
    assert table.game.roulette is None


def test_score_mode_uses_earned_points_or_unscored_win_award():
    session = RouletteSession(["chess", "pig"], finish_mode="score", target_score=450)
    session.record_round(GameResult(
        "chess", "now", 20, [PlayerResult("a", "Alice", False), PlayerResult("b", "Bob", False)],
        winner_ids=["a"],
    ))
    assert session.scores == {"a": 100, "b": 0}
    session.record_round(GameResult(
        "pig", "now", 40, [PlayerResult("a", "Alice", False, score=350),
                              PlayerResult("b", "Bob", False, score=50)], winner_ids=["a"],
    ))
    assert session.scores == {"a": 450, "b": 50} and session.finished
    assert session.duration_ticks == 60


def test_incompatible_pool_keeps_the_lobby_and_spectators_do_not_count():
    table = make_table(3)
    lobby = table.game
    lobby.options.included_games = ["chess"]
    assert lobby.prestart_validate() == ["roulette-no-compatible-games"]
    lobby.on_start()
    assert table.game is lobby and table.status == GameStatus.WAITING
    lobby.players[-1].is_spectator = True
    assert not lobby.prestart_validate()
    lobby.on_start()
    advance_selection(table)
    assert table.game.get_type() == "chess"
    assert table.game.players[-1].is_spectator


def test_departure_during_selection_returns_to_lobby_without_spending_a_round():
    table = make_table()
    wheel = table.game
    wheel.options.included_games = ["chess"]
    wheel.on_start()
    advance_selection(table, 100)
    guest = wheel.players[1]
    balances = dict(wheel.roulette.jokers_remaining)
    wheel._perform_leave_game(guest)
    table.remove_member(guest.name)
    advance_selection(table, 200)
    assert table.game is wheel
    assert wheel.status == GameStatus.WAITING and wheel.selection_phase == "idle"
    assert wheel.roulette.round_number == 0
    assert wheel.roulette.jokers_remaining == balances


@pytest.mark.parametrize("game_class", [cls for cls in GameRegistry.get_all()
                                       if cls is not RouletteGame], ids=lambda cls: cls.get_type())
def test_roulette_starts_every_game_with_its_own_defaults(game_class):
    table = make_table(max(RouletteGame.get_min_players(), game_class.get_min_players()))
    wheel = table.game
    wheel.options.included_games = [game_class.get_type()]
    wheel.options.total_rounds = 19
    wheel.options.target_score = 7654
    wheel.execute_action(wheel.players[0], "start_game")
    advance_selection(table)
    selected = table.game
    assert type(selected) is game_class
    assert selected.status == table.status == GameStatus.PLAYING
    assert getattr(selected, "options", None) == getattr(game_class(), "options", None)
    assert selected.roulette.total_rounds == 19
    assert selected.roulette.target_score == 7654


def test_stop_roulette_returns_to_session_lobby_and_repeated_games_use_defaults():
    table = make_table()
    table._server = Mock()
    wheel = table.game
    wheel.options.included_games = ["pig"]
    wheel.options.jokers = 4
    wheel.on_start()
    advance_selection(table)
    first = table.game
    defaults = type(first.options)()
    first.options.target_score += 100
    first.finish_round(winner_ids=[first.players[0].id])
    assert table.start_roulette_round()
    advance_selection(table)
    second = table.game
    assert second.options == defaults and second.options is not first.options
    second.execute_action(second.players[0], "stop_game")
    lobby = table.game
    assert isinstance(lobby, RouletteGame) and lobby.roulette is None
    assert lobby.options.included_games == ["pig"] and lobby.options.jokers == 4
    assert lobby.options.included_games is not first.roulette.included_games
    assert lobby.status == table.status == GameStatus.WAITING
    table._server.on_game_result.assert_not_called()


def test_legacy_wheel_countdown_restores_into_shared_timer():
    table = make_table()
    wheel = table.game
    wheel.on_start()
    saved = wheel.to_dict()
    saved["selection_ticks"] = 37
    saved["round_timer_ticks"] = 0
    saved["round_timer_state"] = "idle"
    restored = RouletteGame.from_dict(saved)
    assert restored.round_timer_ticks == 37 and restored.round_timer_state == "counting"
    assert restored.selection_ticks == 0
