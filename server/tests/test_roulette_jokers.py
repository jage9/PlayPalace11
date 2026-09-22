"""Wheel timing, authoritative joker use, and saved selection state."""

from server.core.users.test_user import MockUser
from server.games.roulette.game import RouletteGame
from server.tests.test_roulette import advance_selection, make_table


def press_j(table, player):
    table.handle_event(player.name, {"type": "keybind", "key": "j"})


def restore_wheel(table):
    old = table.game
    restored = RouletteGame.from_json(old.to_json())
    restored.rebuild_runtime_state()
    restored.setup_keybinds()
    restored._table = table
    for player in restored.players:
        restored.attach_user(player.id, old.get_user(player))
    table.game = restored
    return restored


def test_spin_lands_after_five_seconds_and_allows_five_seconds_for_jokers():
    table = make_table()
    wheel = table.game
    wheel.options.included_games = ["chess"]
    user = wheel.get_user(wheel.players[0])
    wheel.on_start()
    advance_selection(table, 99)
    assert wheel.selection_phase == "spinning" and not wheel.selected_game
    assert "click.ogg" in user.get_sounds_played()
    assert "game_squares/diceroll1.ogg" not in user.get_sounds_played()
    advance_selection(table, 1)
    assert wheel.selection_phase == "joker" and wheel.selected_game == "chess"
    assert "game_squares/diceroll1.ogg" in user.get_sounds_played()
    assert any("Selected game: Chess" in text for text in user.get_spoken_messages())
    assert not table.play_roulette_game("chess")
    advance_selection(table, 99)
    assert table.game is wheel and wheel.roulette.round_number == 0
    wheel.status_box(wheel.players[0], ["Wheel status"])
    advance_selection(table, 1)
    assert table.game.get_type() == "chess" and table.game.game_active
    assert table.game.roulette.round_number == 1
    assert "transient_display" not in user.menus


def test_first_valid_joker_blocks_game_and_survives_restore_and_next_round():
    table = make_table()
    wheel = table.game
    wheel.options.included_games = ["chess", "pig"]
    wheel.on_start()
    alice, guest = wheel.players
    press_j(table, alice)
    assert wheel.selection_phase == "spinning" and wheel.roulette.jokers_remaining[alice.id] == 1
    advance_selection(table, 100)
    blocked = wheel.selected_game
    press_j(table, alice)
    press_j(table, guest)
    assert wheel.selection_phase == "spinning"
    assert wheel.roulette.jokers_remaining == {alice.id: 0, guest.id: 1}
    assert wheel.blocked_games == [blocked] and wheel.roulette.round_number == 0
    advance_selection(table, 37)
    wheel = restore_wheel(table)
    assert wheel.selection_ticks == 63 and wheel.blocked_games == [blocked]
    advance_selection(table, 63)
    assert wheel.selected_game != blocked and wheel.selection_phase == "joker"
    press_j(table, alice)
    assert "You have no jokers remaining." in wheel.get_user(alice).get_spoken_messages()
    press_j(table, guest)
    assert wheel.roulette.jokers_remaining[guest.id] == 1  # Only one unblocked game remains.
    advance_selection(table, 42)
    wheel = restore_wheel(table)
    assert wheel.selection_ticks == 58 and wheel.selection_phase == "joker"
    advance_selection(table, 58)
    game = table.game
    assert game.get_type() != blocked and game.roulette.round_number == 1
    game.finish_round(winner_ids=[alice.id])
    assert table.start_roulette_round()
    assert table.game.selection_phase == "spinning" and not table.game.blocked_games
    assert table.game.roulette.jokers_remaining == {alice.id: 0, guest.id: 1}
    advance_selection(table)
    assert table.game.get_type() == blocked and table.game.roulette.round_number == 2


def test_zero_jokers_and_spectators_cannot_veto():
    table = make_table()
    wheel = table.game
    wheel.options.included_games = ["chess", "pig"]
    wheel.options.jokers = 0
    watcher = MockUser("Watcher")
    table.add_member(watcher.username, watcher, as_spectator=True)
    spectator = wheel.add_spectator(watcher.username, watcher)
    wheel.on_start()
    alice = wheel.players[0]
    press_j(table, alice)  # Too early, even if a player had jokers.
    advance_selection(table, 100)
    selected = wheel.selected_game
    press_j(table, alice)
    press_j(table, spectator)
    assert wheel.selection_phase == "joker" and wheel.selected_game == selected
    assert not any(wheel.roulette.jokers_remaining.values())
    assert spectator.id not in wheel.roulette.jokers_remaining
    assert "You have no jokers remaining." in wheel.get_user(alice).get_spoken_messages()
    advance_selection(table, 100)
    assert table.game.get_type() == selected
