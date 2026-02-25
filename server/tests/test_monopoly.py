"""Tests for Monopoly scaffold and preset wiring."""

from server.games.monopoly.game import MonopolyGame, MonopolyOptions
from server.games.monopoly.presets import (
    DEFAULT_PRESET_ID,
    get_available_preset_ids,
    get_default_preset_id,
    get_preset,
)
from server.games.registry import get_game_class
from server.users.test_user import MockUser


def _create_two_player_game(options: MonopolyOptions | None = None) -> MonopolyGame:
    """Create a Monopoly game with two human players."""
    game = MonopolyGame(options=options or MonopolyOptions())
    host_user = MockUser("Host")
    guest_user = MockUser("Guest")
    game.add_player("Host", host_user)
    game.add_player("Guest", guest_user)
    game.host = "Host"
    return game


def test_monopoly_game_creation():
    game = MonopolyGame()
    assert game.get_name() == "Monopoly"
    assert game.get_name_key() == "game-name-monopoly"
    assert game.get_type() == "monopoly"
    assert game.get_category() == "category-uncategorized"
    assert game.get_min_players() == 2
    assert game.get_max_players() == 6
    assert game.options.preset_id == DEFAULT_PRESET_ID


def test_monopoly_registered():
    assert get_game_class("monopoly") is MonopolyGame


def test_monopoly_preset_catalog_includes_classic():
    preset_ids = get_available_preset_ids()
    assert DEFAULT_PRESET_ID in preset_ids

    default_preset = get_preset(get_default_preset_id())
    assert default_preset is not None
    assert default_preset.edition_count > 0


def test_monopoly_options_present_catalog_preset_choices():
    game = _create_two_player_game()
    host_player = game.players[0]
    options_action_set = game.get_action_set(host_player, "options")
    assert options_action_set is not None

    set_preset_action = options_action_set.get_action("set_preset_id")
    assert set_preset_action is not None

    menu_options = game._get_menu_options_for_action(set_preset_action, host_player)
    assert menu_options is not None
    assert DEFAULT_PRESET_ID in menu_options


def test_monopoly_on_start_uses_selected_preset():
    game = _create_two_player_game(MonopolyOptions(preset_id="junior"))
    game.on_start()

    assert game.status == "playing"
    assert game.game_active is True
    assert game.active_preset_id == "junior"
    assert game.active_preset_name
    assert game.active_edition_ids
    assert len(game.team_manager.teams) == 2


def test_monopoly_on_start_falls_back_to_default_preset():
    game = _create_two_player_game(MonopolyOptions(preset_id="not-a-real-preset"))
    game.on_start()

    assert game.active_preset_id == get_default_preset_id()
    assert game.options.preset_id == get_default_preset_id()
