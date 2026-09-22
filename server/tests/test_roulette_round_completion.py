"""Play every Roulette game from a fresh deal to its natural round boundary."""

import random
from unittest.mock import Mock, patch

import pytest

from server.core.tables.table import Table
from server.core.users.bot import Bot
from server.game_utils.game_status import GameStatus
from server.games.registry import GameRegistry
from server.games.roulette.game import RouletteGame


WHOLE_GAME_BOUNDARIES = {
    "battleship", "chaosbear", "chess", "coup", "metalpipe", "senet",
    "snakesandladders", "sorry",
}


@pytest.fixture
def seeded_random(request):
    state = random.getstate()
    random.seed(request.param)
    yield
    random.setstate(state)


@pytest.mark.parametrize("seeded_random", [734, 2026], indirect=True)
@pytest.mark.parametrize("mode", ["rounds", "score"])
@pytest.mark.parametrize("game_class", [cls for cls in GameRegistry.get_all()
                                       if cls.get_type() != "roulette"], ids=lambda cls: cls.get_type())
def test_each_game_completes_one_natural_roulette_round(game_class, mode, seeded_random):
    game_type = game_class.get_type()
    table = Table(f"round-{game_type}", "roulette", "Bot0")
    table._server = Mock()
    lobby = RouletteGame()
    lobby._table = table
    lobby.host = table.host
    lobby.options.included_games = [game_type]
    lobby.options.finish_mode = mode
    lobby.options.total_rounds = 1
    lobby.options.target_score = 1
    lobby.options.jokers = 0
    table.game = lobby
    for index in range(max(2, game_class.get_min_players())):
        bot = Bot(f"Bot{index}", uuid=f"bot-{index}")
        table.add_member(bot.username, bot)
        player = lobby.add_player(bot.username, bot)
        # Keep completed tables available for inspection and aggregate persistence.
        player.is_virtual_bot = True
    assert not lobby.prestart_validate()
    lobby.start_game()
    for _ in range(200):
        table.on_tick()
    game = table.game
    assert isinstance(game, game_class)
    assert game.game_active
    assert getattr(game, "options", None) == getattr(game_class(), "options", None)

    # Observe the real scoring hooks; never force completion or alter game state.
    with patch.object(game, "finish_round", wraps=game.finish_round) as finish_round:
        for _ in range(50000):
            table.on_tick()
            if not game.game_active:
                break
        assert game.status == GameStatus.FINISHED, f"{game_type} stalled before its first result"
        if game_type in WHOLE_GAME_BOUNDARIES:
            assert finish_round.call_count == 0
        elif game_type == "pirates" and game.total_gems == 0:
            assert finish_round.call_count <= 1  # The last gem can end play mid-cycle.
        elif game_type == "rollingballs" and not game.pipe:
            assert finish_round.call_count <= 1  # An empty pipe ends play immediately.
        else:
            assert finish_round.call_count == 1
    # Some games deal immediately; others begin their first hand after an intro.
    assert game.round <= 1, f"{game_type} started a second round"
    if game_type == "scopa":
        assert game.current_round == 1
    if game_type in {"blackjack", "fivecarddraw", "holdem"}:
        assert game.hand_number == 1
    if game_type == "yahtzee":
        assert all(sum(score is not None for score in player.scores.values()) == 1
                   for player in game.players)
    result = game._last_game_result
    assert result is not None
    session = game.roulette
    assert session.round_number == 1
    assert result.game_type == game_type
    assert set(session.scores) == {p.id for p in game.players}
    assert session.scores == {p.player_id: p.session_points for p in result.player_results}
    if mode == "rounds":
        assert session.scores == {p.id: int(p.id in result.get_winner_ids()) for p in game.players}
    else:
        assert all(score >= 0 for score in session.scores.values())
    assert table._server.on_game_result.call_count == int(session.finished)

    # Finished games must not deal again, award twice, or advance the session on ticks.
    awards = dict(session.scores)
    finished_round = game.round
    for _ in range(200):
        table.on_tick()
    assert game._last_game_result is result
    assert game.status == GameStatus.FINISHED
    assert game.round == finished_round
    assert session.round_number == 1 and session.scores == awards
    assert table._server.on_game_result.call_count == int(session.finished)
