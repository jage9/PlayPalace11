"""Shared lifecycle checks: result persistence, retained seats, and fresh game state."""

from unittest.mock import Mock

import pytest

from server.core.tables.table import Table
from server.core.users.test_user import MockUser
from server.game_utils.game_result import GameResult
from server.game_utils.game_status import GameStatus
from server.game_utils.actions import Action, ActionSet
from server.games.registry import GameRegistry
from server.games.pig.game import PigGame
from server.games.farkle.game import FarkleGame
from server.games.threes.game import ThreesGame
from server.games.chess.game import ChessGame
from server.games.metalpipe.game import MetalPipeGame
from server.games.snakesandladders.game import SnakesAndLaddersGame


def make_table(game_class, count=None):
    table = Table("repeat", game_class.get_type(), "Alice")
    game = game_class()
    game._table = table
    game.host = table.host
    for i in range(count or game.get_min_players()):
        user = MockUser("Alice" if i == 0 else f"Player{i}")
        table.add_member(user.username, user)
        game.add_player(user.username, user)
    game.setup_keybinds()
    table.game = game
    return table


@pytest.mark.parametrize("game_class", GameRegistry.get_all(), ids=lambda cls: cls.get_type())
def test_each_game_can_save_finish_and_start_again_at_the_same_table(game_class):
    table = make_table(game_class)
    old = table.game
    old.on_start()
    for sets in old.player_action_sets.values():
        for action_set in sets:
            for action in action_set._actions.values():
                for name in ("handler", "is_enabled", "is_hidden", "get_label", "get_sound"):
                    callback = getattr(action, name)
                    assert not callback or callable(getattr(old, callback, None)), (old.get_type(), action.id, name)
    tick = old.sound_scheduler_tick
    old.on_tick()
    assert old.sound_scheduler_tick == tick + 1
    # Exercise persistence with the same runtime restoration used by the server.
    game = game_class.from_json(old.to_json())
    game.rebuild_runtime_state()
    game._table = table
    game.setup_keybinds()
    for player in game.players:
        game.attach_user(player.id, old.get_user(player))
    table.game = game
    game.finish_game()
    result = game._last_game_result
    assert result is not None
    saved = game_class.from_json(game.to_json())
    assert saved._last_game_result.get_player_ids() == result.get_player_ids()
    members = list(table.members)
    options = getattr(game, "options", None)
    assert table.prepare_next_game("Alice")
    fresh = table.game
    assert fresh is not game
    assert table.members == members
    assert fresh.status == table.status == GameStatus.WAITING
    assert fresh._last_game_result is None
    assert fresh.sound_scheduler_tick == 0
    assert not fresh.event_queue and not fresh.scheduled_sounds
    if options is not None:
        assert fresh.options == options and fresh.options is not options
    fresh.on_start()
    fresh.on_tick()
    assert fresh.game_active


def test_end_screen_replay_authorization_and_switching_games():
    table = make_table(PigGame)
    game = table.game
    host, guest = game.players
    assert not table.prepare_next_game(host.name)
    game.on_start()
    assert not table.prepare_next_game(host.name, "chess")
    game.finish_game()
    assert not table.prepare_next_game(guest.name, "chess")
    assert not table.prepare_next_game(host.name, "unknown")
    game.handle_event(host, {"type": "menu", "menu_id": "game_over", "selection_id": "score_line"})
    assert not game._pending_actions
    game.handle_event(host, {"type": "menu", "menu_id": "change_game", "selection_id": "chess"})
    assert isinstance(table.game, ChessGame)
    assert [p.id for p in table.game.players] == [host.id, guest.id]
    table.game._action_start_game(table.game.players[0], "start_game")
    assert table.game.game_active


def test_eliminated_player_remains_in_results_and_rejoins_next_game():
    table = make_table(FarkleGame, 3)
    game = table.game
    game.on_start()
    a, b, c = game.players
    a.score = b.score = game.options.target_score
    c.score = 100
    game._on_round_end()
    assert c.is_spectator and c.eliminated
    a.score += 100
    game._on_round_end()
    assert game._last_game_result.get_player_ids() == [a.id, b.id, c.id]
    assert game._last_game_result.custom_data["final_scores"][c.name] == 100
    assert table.prepare_next_game("Alice")
    assert all(not p.is_spectator and not p.eliminated for p in table.game.players)


def test_winner_formats_and_ties_have_one_result_contract():
    pig = make_table(PigGame, 4).game
    pig.options.team_mode = "2v2"
    pig.on_start()
    pig.team_manager.teams[0].total_score = 100
    pig.team_manager.teams[1].total_score = 20
    result = GameResult.from_json(pig.build_game_result().to_json())
    winners = {p.id for p in pig.players if p.name in pig.team_manager.teams[0].members}
    assert set(result.get_winner_ids()) == winners
    assert {result.get_player_score(p) for p in result.player_results} == {100, 20}

    threes = make_table(ThreesGame, 3).game
    for p, score in zip(threes.players, (5, 5, 12)):
        p.total_score = score
    assert threes.build_game_result().get_winner_ids() == [p.id for p in threes.players[:2]]
    chess = make_table(ChessGame).game
    chess._winner_id = chess.players[0].id
    assert chess.build_game_result().get_winner_ids() == [chess.players[0].id]
    pipe = make_table(MetalPipeGame).game
    pipe._winner_names = [pipe.players[0].name]
    assert pipe.build_game_result().get_winner_ids() == [pipe.players[0].id]
    snakes = make_table(SnakesAndLaddersGame).game
    snakes.players[1].position = 100
    lines = snakes.format_end_screen(snakes.build_game_result(), "en")
    assert snakes.players[1].name in lines[1]


def test_finishing_twice_only_saves_once_and_transfers_host_after_leaving():
    table = make_table(PigGame)
    table._server = Mock()
    game = table.game
    game.on_start()
    game.finish_game()
    game.finish_game()
    assert table._server.on_game_result.call_count == 1
    host, guest = game.players
    game._perform_leave_game(host)
    assert table.host == game.host == guest.name
    assert table.prepare_next_game(guest.name)


def test_replay_preserves_bots_and_spectators_and_rejects_smaller_games():
    table = make_table(PigGame, 3)
    game = table.game
    host = game.players[0]
    game._action_add_bot(host, "Bot", "add_bot")
    watcher = MockUser("Watcher")
    table.add_member(watcher.username, watcher, as_spectator=True)
    game.add_spectator(watcher.username, watcher)
    game.on_start()
    game.finish_game()
    assert watcher.uuid not in game._last_game_result.get_player_ids()
    assert not table.prepare_next_game(host.name, "chess")
    assert table.game is game
    game.handle_event(host, {"type": "menu", "menu_id": "game_over", "selection_id": "play_again"})
    fresh = table.game
    assert fresh.get_player_by_id(watcher.uuid).is_spectator
    assert fresh.get_player_by_name("Bot").is_bot
    assert len(fresh.get_active_players()) == 4


def test_missing_action_guards_do_not_enable_an_action():
    game = make_table(PigGame).game
    for guard in ("is_enabled", "is_hidden"):
        callbacks = {"is_enabled": None, "is_hidden": None, guard: "missing"}
        action = Action(id="bad", label="Bad", handler="_action_start_game", **callbacks)
        resolved = ActionSet(name="test").resolve_action(game, game.players[0], action)
        assert not resolved.enabled


def test_switch_menu_excludes_departed_replacement_bots_from_seat_count():
    table = make_table(PigGame, 3)
    game = table.game
    game.on_start()
    departed = game.players[-1]
    game._perform_leave_game(departed)
    table.remove_member(departed.name)
    game.finish_game()
    host = game.players[0]
    game._show_change_game_menu(host)
    items = game.get_user(host).menus["change_game"]["items"]
    assert any(item.id == "chess" for item in items)
    assert table.prepare_next_game(host.name, "chess")
    assert len(table.game.players) == 2
