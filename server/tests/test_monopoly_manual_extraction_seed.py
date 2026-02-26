from __future__ import annotations

import json
from pathlib import Path

import pytest

from server.games.monopoly.manual_rules.loader import load_manual_rule_set


REPO_ROOT = Path(__file__).resolve().parents[2]
ANCHOR_INDEX_PATH = REPO_ROOT / "server/games/monopoly/catalog/special_board_anchor_index.json"
MANIFEST_PATH = REPO_ROOT / "server/games/monopoly/manual_rules/extracted/manifest.json"
TARGET_FAMILIES = {"marvel", "star"}


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _target_board_ids() -> list[str]:
    anchor_rows = _load_json(ANCHOR_INDEX_PATH)
    return sorted(
        row["board_id"]
        for row in anchor_rows
        if row.get("family") in TARGET_FAMILIES
    )


def test_marvel_and_star_rules_include_extraction_seed_metadata() -> None:
    manifest_rows = _load_json(MANIFEST_PATH)
    manifest_by_board = {row["board_id"]: row for row in manifest_rows}

    for board_id in _target_board_ids():
        row = manifest_by_board[board_id]
        rule_set = load_manual_rule_set(board_id)
        mechanics = rule_set.mechanics

        manual_extraction = mechanics.get("manual_extraction")
        assert isinstance(manual_extraction, dict), board_id
        assert manual_extraction.get("status") == "seeded_from_extracted_manual_text"
        assert manual_extraction.get("text_sha256") == row.get("text_sha256")
        assert manual_extraction.get("pdf_sha256") == row.get("pdf_sha256")
        assert manual_extraction.get("page_count") == row.get("page_count")
        assert manual_extraction.get("extraction_mode") == row.get("extraction_mode", "pypdf")

        citation_paths = {citation.rule_path for citation in rule_set.citations}
        assert "mechanics.manual_extraction" in citation_paths


@pytest.mark.parametrize(
    ("board_id", "expected"),
    [
        (
            "star_wars_classic_edition",
            {
                "chance_1": "Use the Force",
                "chance_2": "Use the Force",
                "chance_3": "Use the Force",
                "community_chest_1": "Hyperspace",
                "community_chest_2": "Hyperspace",
                "community_chest_3": "Hyperspace",
                "income_tax": "Galactic Empire Tax",
                "luxury_tax": "Galactic Empire Tax",
            },
        ),
        (
            "star_wars_legacy",
            {
                "chance_1": "Use the Force",
                "chance_2": "Use the Force",
                "chance_3": "Use the Force",
                "community_chest_1": "Hyperspace",
                "community_chest_2": "Hyperspace",
                "community_chest_3": "Hyperspace",
                "income_tax": "Galactic Empire Tax",
                "luxury_tax": "Galactic Empire Tax",
            },
        ),
        (
            "star_wars_mandalorian",
            {
                "chance_1": "Signet",
                "chance_2": "Signet",
                "chance_3": "Signet",
                "community_chest_1": "Hyperspace Jump",
                "community_chest_2": "Hyperspace Jump",
                "community_chest_3": "Hyperspace Jump",
                "income_tax": "Imperial Credits",
                "luxury_tax": "Imperial Advance",
            },
        ),
        (
            "star_wars_mandalorian_s2",
            {
                "chance_1": "Signet",
                "chance_2": "Signet",
                "chance_3": "Signet",
                "community_chest_1": "Hyperspace Jump",
                "community_chest_2": "Hyperspace Jump",
                "community_chest_3": "Hyperspace Jump",
                "income_tax": "Imperial Credits",
                "luxury_tax": "Imperial Advance",
            },
        ),
    ],
)
def test_star_wars_seed_applies_manual_action_space_labels(
    board_id: str,
    expected: dict[str, str],
) -> None:
    rule_set = load_manual_rule_set(board_id)
    by_space_id = {
        row["space_id"]: row["name"]
        for row in rule_set.board.get("spaces", [])
    }
    for space_id, expected_name in expected.items():
        assert by_space_id.get(space_id) == expected_name


@pytest.mark.parametrize(
    ("board_id", "expected_names", "expected_decks"),
    [
        (
            "marvel_spider_man",
            {
                "chance_1": "Daily Bugle",
                "chance_2": "Daily Bugle",
                "chance_3": "Daily Bugle",
                "community_chest_1": "Spider-Sense",
                "community_chest_2": "Spider-Sense",
                "community_chest_3": "Spider-Sense",
            },
            {
                "chance": "Daily Bugle",
                "community_chest": "Spider-Sense",
            },
        ),
        (
            "marvel_super_villains",
            {
                "chance_1": "Chance",
                "chance_2": "Chance",
                "chance_3": "Chance",
                "community_chest_1": "Reshape the Universe",
                "community_chest_2": "Reshape the Universe",
                "community_chest_3": "Reshape the Universe",
            },
            {
                "chance": "Chance",
                "community_chest": "Reshape the Universe",
            },
        ),
    ],
)
def test_marvel_seed_applies_manual_action_labels_and_deck_metadata(
    board_id: str,
    expected_names: dict[str, str],
    expected_decks: dict[str, str],
) -> None:
    rule_set = load_manual_rule_set(board_id)
    by_space_id = {
        row["space_id"]: row["name"]
        for row in rule_set.board.get("spaces", [])
    }
    for space_id, expected_name in expected_names.items():
        assert by_space_id.get(space_id) == expected_name

    assert rule_set.mechanics.get("decks") == expected_decks
