import json

from server.games.holdem.game import HoldemGame, HoldemOptions
from server.users.test_user import MockUser
from server.users.bot import Bot


def test_holdem_game_creation():
    game = HoldemGame()
    assert game.get_name() == "Texas Hold'em"
    assert game.get_type() == "holdem"
    assert game.get_category() == "category-poker"
    assert game.get_min_players() == 2
    assert game.get_max_players() == 12


def test_holdem_options_defaults():
    game = HoldemGame()
    assert game.options.starting_chips == 20000
    assert game.options.big_blind == 200
    assert game.options.ante == 0


def test_holdem_serialization_round_trip():
    game = HoldemGame()
    user1 = MockUser("Alice")
    user2 = MockUser("Bob")
    game.add_player("Alice", user1)
    game.add_player("Bob", user2)
    game.on_start()
    json_str = game.to_json()
    data = json.loads(json_str)
    assert data["hand_number"] >= 1
    loaded = HoldemGame.from_json(json_str)
    assert loaded.hand_number == game.hand_number


def test_holdem_bot_game_completes():
    options = HoldemOptions(starting_chips=200, big_blind=200, ante=0)
    game = HoldemGame(options=options)
    for i in range(2):
        bot = Bot(f"Bot{i}")
        game.add_player(f"Bot{i}", bot)
    game.on_start()
    for _ in range(20000):
        if game.status == "finished":
            break
        game.on_tick()
    assert game.status == "finished"


def test_holdem_raise_too_large_rejected():
    game = HoldemGame()
    user1 = MockUser("Alice")
    user2 = MockUser("Bob")
    game.add_player("Alice", user1)
    game.add_player("Bob", user2)
    game.on_start()
    player = game.current_player
    assert player is not None
    player.chips = 5
    pot_before = game.pot_manager.total_pot()
    bet_before = game.betting.bets.get(player.id, 0) if game.betting else 0
    game._action_raise(player, "10", "raise")
    assert game.pot_manager.total_pot() == pot_before
    assert game.betting.bets.get(player.id, 0) == bet_before


def test_holdem_short_stack_raise_becomes_call():
    game = HoldemGame()
    user1 = MockUser("Alice")
    user2 = MockUser("Bob")
    game.add_player("Alice", user1)
    game.add_player("Bob", user2)
    game.on_start()
    player = game.current_player
    assert player is not None
    player.chips = 5
    if game.betting:
        game.betting.current_bet = 10
        game.betting.bets[player.id] = 0
    pot_before = game.pot_manager.total_pot()
    game._action_raise(player, "1", "raise")
    assert game.pot_manager.total_pot() == pot_before + 5
    if game.betting:
        assert game.betting.current_bet == 10
