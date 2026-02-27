"""Completeness checks for all special-board manual rule payloads."""

import pytest

from server.games.monopoly.board_profile import BOARD_PROFILES, DEFAULT_BOARD_ID
from server.games.monopoly.game import CHANCE_CARD_IDS, COMMUNITY_CHEST_CARD_IDS
from server.games.monopoly.manual_rules.loader import load_manual_rule_set


ALL_SPECIAL_BOARD_IDS = sorted(
    board_id for board_id in BOARD_PROFILES if board_id != DEFAULT_BOARD_ID
)

DECK_ID_OVERRIDES = {
    "marvel_avengers_legacy": {
        "chance": [
            "shield_advance_to_go",
            "shield_bank_dividend_50",
            "shield_go_back_three",
            "shield_go_to_jail",
            "shield_poor_tax_15",
        ],
        "community_chest": [
            "villains_bank_error_collect_215",
            "villains_doctor_fee_pay_50",
            "villains_income_tax_refund_20",
            "villains_go_to_jail",
            "villains_jail_release_options",
        ],
    },
    "marvel_flip": {
        "chance": [
            "event_advance_to_go",
            "event_go_to_jail_primary",
            "event_go_back_three",
            "event_go_to_jail_secondary",
            "event_poor_tax_15",
        ],
        "community_chest": [
            "team_up_bank_error_collect_200",
            "team_up_doctor_fee_pay_50",
            "team_up_income_tax_refund_20",
            "team_up_go_to_jail",
            "team_up_jail_release_options",
        ],
    },
}


@pytest.mark.parametrize("board_id", ALL_SPECIAL_BOARD_IDS)
def test_all_special_boards_have_executable_manual_payload(board_id: str):
    rule_set = load_manual_rule_set(board_id)

    spaces = rule_set.board.get("spaces", [])
    chance_rows = rule_set.cards.get("chance", [])
    chest_rows = rule_set.cards.get("community_chest", [])
    mechanics = rule_set.mechanics
    citation_paths = {citation.rule_path for citation in rule_set.citations}
    deck_override = DECK_ID_OVERRIDES.get(board_id, {})
    expected_chance_ids = deck_override.get("chance", CHANCE_CARD_IDS)
    expected_chest_ids = deck_override.get("community_chest", COMMUNITY_CHEST_CARD_IDS)

    assert isinstance(spaces, list)
    assert len(spaces) == 40
    assert [row.get("id") for row in chance_rows] == expected_chance_ids
    assert [row.get("id") for row in chest_rows] == expected_chest_ids

    assert mechanics.get("mode") != "manual_core_candidate"
    source = mechanics.get("manual_source", {})
    assert isinstance(source, dict)
    assert isinstance(source.get("instruction_url"), str)
    assert source.get("instruction_url")
    assert isinstance(source.get("pdf_url"), str)
    assert source.get("pdf_url")

    assert "mechanics.manual_source" in citation_paths
