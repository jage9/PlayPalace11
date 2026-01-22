import json

from server.games.fivecarddraw.game import FiveCardDrawGame, FiveCardDrawOptions
from server.users.test_user import MockUser
from server.users.bot import Bot


def test_draw_game_creation():
    game = FiveCardDrawGame()
    assert game.get_name() == "Five Card Draw"
    assert game.get_type() == "fivecarddraw"
    assert game.get_category() == "category-poker"
    assert game.get_min_players() == 2
    assert game.get_max_players() == 5


def test_draw_options_defaults():
    game = FiveCardDrawGame()
    assert game.options.starting_chips == 20000
    assert game.options.ante == 100


def test_draw_serialization_round_trip():
    game = FiveCardDrawGame()
    user1 = MockUser("Alice")
    user2 = MockUser("Bob")
    game.add_player("Alice", user1)
    game.add_player("Bob", user2)
    game.on_start()
    json_str = game.to_json()
    data = json.loads(json_str)
    assert data["hand_number"] >= 1
    loaded = FiveCardDrawGame.from_json(json_str)
    assert loaded.hand_number == game.hand_number


def test_draw_bot_game_completes():
    options = FiveCardDrawOptions(starting_chips=200, ante=100)
    game = FiveCardDrawGame(options=options)
    for i in range(2):
        bot = Bot(f"Bot{i}")
        game.add_player(f"Bot{i}", bot)
    game.on_start()
    for _ in range(40000):
        if game.status == "finished":
            break
        game.on_tick()
    assert game.status == "finished"


def test_draw_raise_too_large_rejected():
    game = FiveCardDrawGame()
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


def test_draw_short_stack_raise_becomes_call():
    game = FiveCardDrawGame()
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
