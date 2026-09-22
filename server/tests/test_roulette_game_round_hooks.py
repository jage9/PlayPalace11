"""Focused checks for game boundaries used by roulette."""

from server.core.users.bot import Bot
from server.core.users.test_user import MockUser
from server.game_utils.game_status import GameStatus
from server.game_utils.roulette import RouletteSession
from server.games.threes.game import ThreesGame
from server.games.yahtzee.game import YahtzeeGame
from server.games.scopa.game import ScopaGame
from server.games.lastcard.game import LastCardGame
from server.game_utils.cards import Card


def test_yahtzee_roulette_stops_after_one_category_per_player():
    game = YahtzeeGame()
    game.roulette = RouletteSession(["yahtzee"], total_rounds=1)
    game.add_player("Bot1", Bot("Bot1"))
    game.add_player("Bot2", Bot("Bot2"))

    game.on_start()
    for _ in range(1000):
        if game.status == GameStatus.FINISHED:
            break
        game.on_tick()

    assert game.status == GameStatus.FINISHED
    assert all(sum(score is not None for score in player.scores.values()) == 1
               for player in game.players)


def test_threes_roulette_inverts_low_score_for_score_mode():
    game = ThreesGame()
    game.roulette = RouletteSession(["threes"], finish_mode="score", target_score=2)
    first = game.add_player("Alice", MockUser("Alice"))
    second = game.add_player("Bob", MockUser("Bob"))
    first.total_score = 26
    second.total_score = 28
    game.round = 1

    game._on_round_end()

    assert game.status == GameStatus.FINISHED
    assert game._last_game_result is not None
    assert game._last_game_result.get_winner_ids() == [first.id]
    assert game.roulette.scores[first.id] == 4
    assert game.roulette.scores[second.id] == 2
    assert [(p.score, p.session_points) for p in game._last_game_result.player_results] == [(26, 4), (28, 2)]


def test_inverse_scopa_uses_target_minus_penalty_and_lowest_score_wins():
    game = ScopaGame()
    game.roulette = RouletteSession(["scopa"], finish_mode="score")
    game.options.inverse_scopa = True
    game.options.target_score = 500
    game.options.scopa_mechanic = "only_scopas"
    first = game.add_player("Alice", MockUser("Alice"))
    second = game.add_player("Bob", MockUser("Bob"))
    game.on_start()
    game.team_manager.get_team(first.name).round_score = 150
    game.team_manager.get_team(second.name).round_score = 200
    game._end_round()
    assert game.roulette.scores == {first.id: 350, second.id: 300}
    assert game._last_game_result.get_winner_ids() == [first.id]
    assert [(p.score, p.session_points) for p in game._last_game_result.player_results] == [(150, 350), (200, 300)]
    restored = ScopaGame.from_json(game.to_json())
    assert restored._last_game_result == game._last_game_result
    assert restored.roulette.scores == game.roulette.scores


def test_negative_lastcard_still_counts_the_hand_winner():
    game = LastCardGame()
    game.roulette = RouletteSession(["lastcard"])
    game.options.scoring_mode = "negative"
    first = game.add_player("Alice", MockUser("Alice"))
    second = game.add_player("Bob", MockUser("Bob"))
    game.on_start()
    first.hand = []
    second.hand = [Card(1, 5, 1)]
    game._end_round(first)
    assert game.roulette.scores == {first.id: 1, second.id: 0}
