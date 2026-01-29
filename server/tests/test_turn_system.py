"""
Tests for turn tracking utilities.
"""

from dataclasses import dataclass

from server.games.base import Game, Player


@dataclass
class DummyGame(Game):
    """Minimal game for turn tracker tests."""

    @classmethod
    def get_name(cls) -> str:
        return "Dummy"

    @classmethod
    def get_type(cls) -> str:
        return "dummy"

    def on_start(self) -> None:
        pass


class TestTurnSystem:
    def test_turn_tracking_flow(self) -> None:
        game = DummyGame()
        p1 = Player(id="p1", name="Alice")
        p2 = Player(id="p2", name="Bob")
        game.players = [p1, p2]
        game.set_turn_players(game.players)

        # Start first turn
        game.on_turn_start()
        for _ in range(5):
            game.tick_turn_tracker()

        # End turn via default end_turn() to exercise integration hooks
        game.end_turn()

        assert len(game.rounds) == 1
        current_round = game.rounds[0]
        assert len(current_round.turns) == 1
        assert current_round.turns[0].players == {"p1"}
        assert current_round.turns[0].ticks == 5

        # Next turn should be running for player 2
        assert game.current_player == p2
        assert current_round.turn_timer.running is True
        assert current_round.turn_timer.ticks == 0

    def test_turn_totals_and_scores(self) -> None:
        game = DummyGame()
        p1 = Player(id="p1", name="Alice")
        p2 = Player(id="p2", name="Bob")
        game.players = [p1, p2]
        game.set_turn_players(game.players)

        # First turn
        game.on_turn_start()
        for _ in range(3):
            game.tick_turn_tracker()
        game.end_turn()

        # Second turn
        for _ in range(2):
            game.tick_turn_tracker()
        game.end_turn()

        assert game.get_total_turns() == 2
        assert game.get_total_cycles() == 1
        assert game.get_total_ticks() == 5

        # Record scores
        p1.score = 10  # type: ignore[attr-defined]
        p2.score = 7  # type: ignore[attr-defined]
        game.on_round_end([p1, p2])

        scores = game.rounds[0].final_scores
        assert scores["p1"] == 10
        assert scores["p2"] == 7
