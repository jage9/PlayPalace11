"""Tests for Monopoly board rules registry."""

import pytest

from server.games.monopoly.board_rules_registry import (
    get_card_cash_override,
    get_card_id_remap,
    get_rule_pack,
    supports_capability,
)


def test_wave1_mario_packs_are_registered():
    assert get_rule_pack("mario_kart") is not None
    assert get_rule_pack("mario_movie") is not None


def test_capability_lookup_handles_missing_pack():
    assert supports_capability("missing", "pass_go_credit") is False


def test_mario_kart_card_id_remap_contract():
    assert get_card_id_remap("mario_kart", "chance", "bank_dividend_50") == "advance_to_go"


def test_card_id_remap_falls_back_to_original_card():
    assert get_card_id_remap("mario_kart", "chance", "does_not_exist") == "does_not_exist"


def test_mario_movie_card_cash_override_contract():
    assert get_card_cash_override("mario_movie", "bank_dividend_50") == 120


def test_card_cash_override_returns_none_when_missing():
    assert get_card_cash_override("mario_movie", "advance_to_go") is None


def test_mario_collectors_card_id_remap_contract():
    assert get_card_id_remap("mario_collectors", "chance", "go_back_three") == "bank_dividend_50"


def test_mario_collectors_card_cash_override_contract():
    assert get_card_cash_override("mario_collectors", "bank_error_collect_200") == 250


def test_mario_celebration_card_id_remap_contract():
    assert get_card_id_remap("mario_celebration", "chance", "poor_tax_15") == "bank_dividend_50"


def test_mario_celebration_card_cash_override_contract():
    assert get_card_cash_override("mario_celebration", "income_tax_refund_20") == 60


def test_junior_super_mario_manual_core_capability_contract():
    assert supports_capability("junior_super_mario", "junior_manual_core") is True


def test_junior_super_mario_sound_ready_capability_contract():
    assert supports_capability("junior_super_mario", "junior_powerup_sound_ready") is True


def test_star_wars_mandalorian_card_id_remap_contract():
    assert (
        get_card_id_remap("star_wars_mandalorian", "chance", "bank_dividend_50")
        == "go_back_three"
    )


def test_star_wars_complete_saga_card_id_remap_contract():
    assert (
        get_card_id_remap("star_wars_complete_saga", "community_chest", "bank_error_collect_200")
        == "income_tax_refund_20"
    )


def test_star_wars_complete_saga_card_cash_override_contract():
    assert get_card_cash_override("star_wars_complete_saga", "income_tax_refund_20") == 80


def test_star_wars_mandalorian_audio_capability_contract():
    assert supports_capability("star_wars_mandalorian", "audio_theme_event") is True


def test_disney_princesses_card_id_remap_contract():
    assert get_card_id_remap("disney_princesses", "chance", "poor_tax_15") == "bank_dividend_50"


def test_disney_princesses_card_cash_override_contract():
    assert get_card_cash_override("disney_princesses", "bank_dividend_50") == 90


def test_marvel_avengers_card_id_remap_contract():
    assert (
        get_card_id_remap("marvel_avengers", "community_chest", "doctor_fee_pay_50")
        == "bank_error_collect_200"
    )


def test_marvel_avengers_card_cash_override_contract():
    assert get_card_cash_override("marvel_avengers", "bank_error_collect_200") == 220


def test_harry_potter_card_id_remap_contract():
    assert get_card_id_remap("harry_potter", "chance", "go_back_three") == "bank_dividend_50"


def test_harry_potter_card_cash_override_contract():
    assert get_card_cash_override("harry_potter", "bank_dividend_50") == 70


def test_fortnite_card_id_remap_contract():
    assert (
        get_card_id_remap("fortnite", "community_chest", "doctor_fee_pay_50")
        == "income_tax_refund_20"
    )


def test_fortnite_card_cash_override_contract():
    assert get_card_cash_override("fortnite", "income_tax_refund_20") == 65


def test_stranger_things_card_id_remap_contract():
    assert get_card_id_remap("stranger_things", "chance", "bank_dividend_50") == "go_to_jail"


@pytest.mark.parametrize(
    ("rule_pack_id", "deck_type", "source_card_id", "target_card_id"),
    (
        ("disney_star_wars_dark_side", "chance", "poor_tax_15", "bank_dividend_50"),
        ("star_wars_40th", "chance", "bank_dividend_50", "advance_to_go"),
        ("star_wars_boba_fett", "chance", "bank_dividend_50", "go_back_three"),
        ("star_wars_classic_edition", "chance", "go_back_three", "bank_dividend_50"),
        ("star_wars_legacy", "community_chest", "doctor_fee_pay_50", "income_tax_refund_20"),
        ("star_wars_light_side", "chance", "bank_dividend_50", "go_to_jail"),
        ("star_wars_mandalorian_s2", "chance", "poor_tax_15", "bank_dividend_50"),
        ("star_wars_saga", "community_chest", "doctor_fee_pay_50", "bank_error_collect_200"),
        ("star_wars_solo", "chance", "go_back_three", "advance_to_go"),
        ("star_wars_the_child", "chance", "bank_dividend_50", "go_to_jail"),
    ),
)
def test_star_wars_family_card_id_remap_contract(
    rule_pack_id: str,
    deck_type: str,
    source_card_id: str,
    target_card_id: str,
):
    assert get_card_id_remap(rule_pack_id, deck_type, source_card_id) == target_card_id


@pytest.mark.parametrize(
    ("rule_pack_id", "card_id", "amount"),
    (
        ("disney_star_wars_dark_side", "bank_dividend_50", 95),
        ("star_wars_classic_edition", "bank_dividend_50", 75),
        ("star_wars_legacy", "income_tax_refund_20", 65),
        ("star_wars_mandalorian_s2", "bank_dividend_50", 85),
        ("star_wars_saga", "bank_error_collect_200", 205),
    ),
)
def test_star_wars_family_card_cash_override_contract(
    rule_pack_id: str,
    card_id: str,
    amount: int,
):
    assert get_card_cash_override(rule_pack_id, card_id) == amount


@pytest.mark.parametrize(
    ("rule_pack_id", "deck_type", "source_card_id", "target_card_id"),
    (
        ("disney_animation", "chance", "bank_dividend_50", "go_back_three"),
        ("disney_lightyear", "chance", "poor_tax_15", "bank_dividend_50"),
        ("disney_lion_king", "community_chest", "doctor_fee_pay_50", "income_tax_refund_20"),
        ("disney_mickey_friends", "chance", "bank_dividend_50", "advance_to_go"),
        ("disney_villains", "chance", "go_back_three", "bank_dividend_50"),
        ("disney_legacy", "community_chest", "doctor_fee_pay_50", "bank_error_collect_200"),
        ("disney_the_edition", "chance", "bank_dividend_50", "go_to_jail"),
        ("marvel_80_years", "chance", "poor_tax_15", "bank_dividend_50"),
        ("marvel_spider_man", "chance", "bank_dividend_50", "go_back_three"),
        ("marvel_black_panther_wf", "community_chest", "doctor_fee_pay_50", "income_tax_refund_20"),
        ("marvel_super_villains", "chance", "bank_dividend_50", "go_to_jail"),
        ("marvel_deadpool", "chance", "go_back_three", "advance_to_go"),
        ("marvel_avengers_legacy", "community_chest", "doctor_fee_pay_50", "bank_error_collect_200"),
        ("marvel_eternals", "chance", "poor_tax_15", "bank_dividend_50"),
        ("marvel_falcon_winter_soldier", "chance", "bank_dividend_50", "go_back_three"),
        ("marvel_flip", "chance", "bank_dividend_50", "go_to_jail"),
    ),
)
def test_disney_marvel_family_card_id_remap_contract(
    rule_pack_id: str,
    deck_type: str,
    source_card_id: str,
    target_card_id: str,
):
    assert get_card_id_remap(rule_pack_id, deck_type, source_card_id) == target_card_id


@pytest.mark.parametrize(
    ("rule_pack_id", "card_id", "amount"),
    (
        ("disney_lightyear", "bank_dividend_50", 88),
        ("disney_lion_king", "income_tax_refund_20", 75),
        ("disney_villains", "bank_dividend_50", 68),
        ("disney_legacy", "bank_error_collect_200", 210),
        ("marvel_80_years", "bank_dividend_50", 92),
        ("marvel_black_panther_wf", "income_tax_refund_20", 70),
        ("marvel_avengers_legacy", "bank_error_collect_200", 215),
        ("marvel_eternals", "bank_dividend_50", 85),
    ),
)
def test_disney_marvel_family_card_cash_override_contract(
    rule_pack_id: str,
    card_id: str,
    amount: int,
):
    assert get_card_cash_override(rule_pack_id, card_id) == amount
