"""Tests for Monopoly board profile resolution."""

from server.games.monopoly.board_profile import (
    DEFAULT_BOARD_ID,
    resolve_board_plan,
)


def test_resolve_board_plan_keeps_compatible_preset():
    plan = resolve_board_plan("classic_standard", "mario_kart", "auto")
    assert plan.effective_preset_id == "classic_standard"
    assert plan.effective_mode == "board_rules"


def test_resolve_board_plan_autofixes_incompatible_preset():
    plan = resolve_board_plan("classic_standard", "junior_super_mario", "auto")
    assert plan.effective_preset_id == "junior"
    assert plan.auto_fixed_from_preset_id == "classic_standard"


def test_resolve_board_plan_forces_skin_only_override():
    plan = resolve_board_plan("classic_standard", "mario_movie", "skin_only")
    assert plan.effective_mode == "skin_only"


def test_resolve_board_plan_unknown_board_falls_back_to_default():
    plan = resolve_board_plan("classic_standard", "does_not_exist", "auto")
    assert plan.effective_board_id == DEFAULT_BOARD_ID
