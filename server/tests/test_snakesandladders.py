"""
Tests for the Snakes and Ladders game.
"""

import pytest
import random
import json

from server.games.snakesandladders.game import SnakesAndLaddersGame, SnakesPlayer
from server.users.test_user import MockUser
from server.users.bot import Bot


class TestSnakesAndLaddersUnit:
    """Unit tests."""

    def test_game_creation(self):
        """Test creating a new game."""
        game = SnakesAndLaddersGame()
        assert game.get_name() == "Snakes and Ladders"
        assert game.get_type() == "snakesandladders"
        assert game.get_category() == "category-board-games"
        assert game.get_min_players() == 2
        assert game.get_max_players() == 4

    def test_player_creation(self):
        """Test creating a player."""
        game = SnakesAndLaddersGame()
        user = MockUser("Alice")
        player = game.add_player("Alice", user)

        assert player.name == "Alice"
        assert isinstance(player, SnakesPlayer)
        assert player.position == 1
        assert player.finished is False

    def test_serialization(self):
        """Test state serialization."""
        game = SnakesAndLaddersGame()
        user1 = MockUser("Alice")
        user2 = MockUser("Bob")
        game.add_player("Alice", user1)
        game.add_player("Bob", user2)
        game.on_start()
        
        # Modify state
        game.players[0].position = 50
        game.players[0].finished = False
        
        # Serialize
        json_str = game.to_json()
        loaded = SnakesAndLaddersGame.from_json(json_str)
        
        assert loaded.players[0].position == 50
        assert loaded.players[0].finished is False
        assert loaded.round == 0 # Base game has round 0 usually unless incremented


class TestSnakesAndLaddersGameFlow:
    """Test game flow logic."""

    def setup_method(self):
        self.game = SnakesAndLaddersGame()
        self.user1 = MockUser("Alice")
        self.user2 = MockUser("Bob")
        self.p1 = self.game.add_player("Alice", self.user1)
        self.p2 = self.game.add_player("Bob", self.user2)
        self.game.on_start()
        self.game.reset_turn_order() # Ensure Alice starts

    def test_roll_moves_player(self):
        """Test that rolling moves the player."""
        # We can't easily mock the random inside the function without patching,
        # but we can verify position changed.
        old_pos = self.p1.position
        self.game.execute_action(self.p1, "roll")
        
        # The move is queued in event_queue, not immediate
        # Must process ticks
        
        # Move events happen after delays.
        # Check event queue
        assert len(self.game.event_queue) > 0
        
        # Process enough ticks
        for _ in range(100):
            self.game.on_tick()
            
        assert self.p1.position > old_pos

    def test_ladder_interaction(self):
        """Test hitting a ladder."""
        # Manually verify ladder logic by forcing position (after movement logic)
        # But here we want to test the _handle_event logic mostly.
        
        # Let's inject a ladder event directly to test logic
        self.game._handle_event("ladder", {"player_id": self.p1.id, "start": 1, "end": 38})
        assert self.p1.position == 38

    def test_snake_interaction(self):
        """Test hitting a snake."""
        self.game._handle_event("snake", {"player_id": self.p1.id, "start": 98, "end": 78})
        assert self.p1.position == 78

    def test_check_positions(self):
        """Test check positions action."""
        self.p1.position = 10
        self.p2.position = 20
        
        self.game.execute_action(self.p1, "check_positions")
        
        messages = self.user1.get_spoken_messages()
        assert any("Alice 10" in m and "Bob 20" in m for m in messages)


class TestSnakesAndLaddersPlayTest:
    """Full game completion tests."""

    def test_bot_game_completes(self):
        """Run a full game with bots."""
        game = SnakesAndLaddersGame()
        bot1 = Bot("Bot1")
        bot2 = Bot("Bot2")
        game.add_player("Bot1", bot1)
        game.add_player("Bot2", bot2)
        game.on_start()

        max_ticks = 50000 
        for tick in range(max_ticks):
            if not game.game_active:
                break
            
            # Save/Load occasionally
            if tick % 500 == 0 and tick > 0:
                json_str = game.to_json()
                game = SnakesAndLaddersGame.from_json(json_str)
                game.attach_user("Bot1", bot1)
                game.attach_user("Bot2", bot2)
                game.rebuild_runtime_state()
                for p in game.players:
                    game.setup_player_actions(p)
            
            game.on_tick()
            
        assert not game.game_active
        assert game.winner is not None
        assert game.winner.position == 100
