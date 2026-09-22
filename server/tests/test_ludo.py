"""Tests for the Ludo game."""

import json

from server.games.ludo.game import LudoGame, LudoOptions
from server.core.users.test_user import MockUser
from server.core.users.bot import Bot


def test_game_creation():
    game = LudoGame()
    assert game.get_name() == "Ludo"
    assert game.get_type() == "ludo"
    assert game.get_category() == "category-board-games"
    assert game.get_min_players() == 2
    assert game.get_max_players() == 4


def test_serialization_round_trip():
    game = LudoGame(options=LudoOptions(max_consecutive_sixes=2))
    user1 = MockUser("Alice")
    user2 = MockUser("Bob")
    game.add_player("Alice", user1)
    game.add_player("Bob", user2)
    game.on_start()

    game.last_roll = 4
    game.players[0].finished_count = 1
    game.turn_index = 1

    json_str = game.to_json()
    data = json.loads(json_str)
    assert data["last_roll"] == 4
    assert data["players"][0]["finished_count"] == 1

    loaded = LudoGame.from_json(json_str)
    assert loaded.last_roll == 4
    assert loaded.players[0].finished_count == 1
    assert loaded.options.max_consecutive_sixes == 2


def test_ludo_bot_game_completes():
    game = LudoGame()
    for i in range(2):
        bot = Bot(f"Bot{i}")
        game.add_player(f"Bot{i}", bot)
    game.on_start()

    for _ in range(40000):
        if game.status == "finished":
            break
        game.on_tick()

    assert game.status == "finished"


def test_safe_start_squares_protect_every_player_start() -> None:
    game = LudoGame()
    for name in ("Alice", "Bob"):
        game.add_player(name, MockUser(name))
    game.on_start()

    alice, bob = game.players
    bob.tokens[0].state = "track"
    bob.tokens[0].position = game._get_start_position(bob)
    alice.tokens[0].state = "track"
    alice.tokens[0].position = bob.tokens[0].position

    game._check_capture(alice, alice.tokens[0])

    assert bob.tokens[0].state == "track"
