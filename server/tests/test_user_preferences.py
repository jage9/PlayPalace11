"""Tests for user preference helpers."""

from server.core.users.preferences import (
    DiceKeepingStyle,
    UserPreferences,
)


def test_dice_keeping_style_from_str_defaults_to_playpalace():
    assert DiceKeepingStyle.from_str("quentin_c") == DiceKeepingStyle.QUENTIN_C
    assert DiceKeepingStyle.from_str("invalid") == DiceKeepingStyle.PLAYPALACE


def test_user_preferences_to_dict_and_from_dict_round_trip():
    prefs = UserPreferences(
        play_turn_sound=False,
        clear_kept_on_roll=True,
        dice_keeping_style=DiceKeepingStyle.QUENTIN_C,
    )
    data = prefs.to_dict()
    assert data == {
        "play_turn_sound": False,
        "clear_kept_on_roll": True,
        "dice_keeping_style": "quentin_c",
    }

    rebuilt = UserPreferences.from_dict(
        {"clear_kept_on_roll": True, "dice_keeping_style": "unknown"}
    )
    assert rebuilt.play_turn_sound  # defaulted to True
    assert rebuilt.clear_kept_on_roll is True
    assert rebuilt.dice_keeping_style == DiceKeepingStyle.PLAYPALACE
