"""Apply extracted manual metadata into Monopoly manual rule payloads."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


TARGET_FAMILIES = {"marvel", "star"}

MARVEL_ACTION_SPACE_NAME_OVERRIDES: dict[str, dict[str, str]] = {
    "marvel_spider_man": {
        "chance_1": "Daily Bugle",
        "chance_2": "Daily Bugle",
        "chance_3": "Daily Bugle",
        "community_chest_1": "Spider-Sense",
        "community_chest_2": "Spider-Sense",
        "community_chest_3": "Spider-Sense",
    },
    "marvel_super_villains": {
        "chance_1": "Chance",
        "chance_2": "Chance",
        "chance_3": "Chance",
        "community_chest_1": "Reshape the Universe",
        "community_chest_2": "Reshape the Universe",
        "community_chest_3": "Reshape the Universe",
    },
}

MARVEL_DECK_METADATA_OVERRIDES: dict[str, dict[str, str]] = {
    "marvel_spider_man": {
        "chance": "Daily Bugle",
        "community_chest": "Spider-Sense",
    },
    "marvel_super_villains": {
        "chance": "Chance",
        "community_chest": "Reshape the Universe",
    },
}

STAR_WARS_ACTION_SPACE_NAME_OVERRIDES: dict[str, dict[str, str]] = {
    "star_wars_classic_edition": {
        "chance_1": "Use the Force",
        "chance_2": "Use the Force",
        "chance_3": "Use the Force",
        "community_chest_1": "Hyperspace",
        "community_chest_2": "Hyperspace",
        "community_chest_3": "Hyperspace",
        "income_tax": "Galactic Empire Tax",
        "luxury_tax": "Galactic Empire Tax",
    },
    "star_wars_legacy": {
        "chance_1": "Use the Force",
        "chance_2": "Use the Force",
        "chance_3": "Use the Force",
        "community_chest_1": "Hyperspace",
        "community_chest_2": "Hyperspace",
        "community_chest_3": "Hyperspace",
        "income_tax": "Galactic Empire Tax",
        "luxury_tax": "Galactic Empire Tax",
    },
    "star_wars_mandalorian": {
        "chance_1": "Signet",
        "chance_2": "Signet",
        "chance_3": "Signet",
        "community_chest_1": "Hyperspace Jump",
        "community_chest_2": "Hyperspace Jump",
        "community_chest_3": "Hyperspace Jump",
        "income_tax": "Imperial Credits",
        "luxury_tax": "Imperial Advance",
    },
    "star_wars_mandalorian_s2": {
        "chance_1": "Signet",
        "chance_2": "Signet",
        "chance_3": "Signet",
        "community_chest_1": "Hyperspace Jump",
        "community_chest_2": "Hyperspace Jump",
        "community_chest_3": "Hyperspace Jump",
        "income_tax": "Imperial Credits",
        "luxury_tax": "Imperial Advance",
    },
}


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, data: Any) -> None:
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    path.write_text(path.read_text(encoding="utf-8").rstrip() + "\n", encoding="utf-8")


def _upsert_citation(payload: dict[str, Any], *, anchor_edition_id: str, extraction_mode: str) -> None:
    citations = payload.get("citations")
    if not isinstance(citations, list):
        return
    for row in citations:
        if row.get("rule_path") == "mechanics.manual_extraction":
            row.update(
                {
                    "edition_id": anchor_edition_id,
                    "page_ref": (
                        "manual-extract:pypdf"
                        if extraction_mode == "pypdf"
                        else "manual-extract:strings-fallback"
                    ),
                    "confidence": "medium" if extraction_mode != "pypdf" else "high",
                }
            )
            return
    citations.append(
        {
            "rule_path": "mechanics.manual_extraction",
            "edition_id": anchor_edition_id,
            "page_ref": (
                "manual-extract:pypdf"
                if extraction_mode == "pypdf"
                else "manual-extract:strings-fallback"
            ),
            "confidence": "medium" if extraction_mode != "pypdf" else "high",
        }
    )


def _upsert_simple_citation(
    payload: dict[str, Any],
    *,
    rule_path: str,
    edition_id: str,
    page_ref: str,
    confidence: str,
) -> None:
    citations = payload.get("citations")
    if not isinstance(citations, list):
        return
    for row in citations:
        if row.get("rule_path") == rule_path:
            row.update(
                {
                    "edition_id": edition_id,
                    "page_ref": page_ref,
                    "confidence": confidence,
                }
            )
            return
    citations.append(
        {
            "rule_path": rule_path,
            "edition_id": edition_id,
            "page_ref": page_ref,
            "confidence": confidence,
        }
    )


def _apply_action_space_name_overrides(payload: dict[str, Any], board_id: str) -> None:
    overrides = MARVEL_ACTION_SPACE_NAME_OVERRIDES.get(board_id)
    if overrides is None:
        overrides = STAR_WARS_ACTION_SPACE_NAME_OVERRIDES.get(board_id)
    if not overrides:
        return

    board = payload.get("board")
    if not isinstance(board, dict):
        return
    spaces = board.get("spaces")
    if not isinstance(spaces, list):
        return

    for space in spaces:
        if not isinstance(space, dict):
            continue
        space_id = space.get("space_id")
        if not isinstance(space_id, str):
            continue
        new_name = overrides.get(space_id)
        if new_name is not None:
            space["name"] = new_name


def _apply_deck_metadata_overrides(payload: dict[str, Any], board_id: str) -> None:
    deck_overrides = MARVEL_DECK_METADATA_OVERRIDES.get(board_id)
    if not deck_overrides:
        return
    mechanics = payload.get("mechanics")
    if not isinstance(mechanics, dict):
        return
    mechanics["decks"] = {
        "chance": deck_overrides["chance"],
        "community_chest": deck_overrides["community_chest"],
    }


def run_seed(
    *,
    anchor_index_path: Path,
    manifest_path: Path,
    manual_rules_dir: Path,
) -> None:
    anchor_rows = _load_json(anchor_index_path)
    manifest_rows = _load_json(manifest_path)

    target_board_ids = {
        row["board_id"] for row in anchor_rows if row.get("family") in TARGET_FAMILIES
    }
    manifest_by_board = {
        row["board_id"]: row
        for row in manifest_rows
        if row.get("board_id") in target_board_ids and row.get("status") == "ok"
    }

    changed = 0
    for board_id in sorted(target_board_ids):
        row = manifest_by_board.get(board_id)
        if row is None:
            continue

        path = manual_rules_dir / f"{board_id}.json"
        if not path.exists():
            continue
        payload = _load_json(path)

        mechanics = payload.get("mechanics")
        if not isinstance(mechanics, dict):
            mechanics = {}
            payload["mechanics"] = mechanics

        extraction_mode = str(row.get("extraction_mode", "pypdf"))
        mechanics["manual_extraction"] = {
            "status": "seeded_from_extracted_manual_text",
            "extraction_mode": extraction_mode,
            "manifest_path": str(manifest_path),
            "text_path": row.get("text_path"),
            "text_sha256": row.get("text_sha256"),
            "pdf_sha256": row.get("pdf_sha256"),
            "pdf_size_bytes": row.get("pdf_size_bytes"),
            "page_count": row.get("page_count"),
        }

        _apply_action_space_name_overrides(payload, board_id)
        _apply_deck_metadata_overrides(payload, board_id)
        _upsert_citation(
            payload,
            anchor_edition_id=str(payload.get("anchor_edition_id", row.get("anchor_edition_id", ""))),
            extraction_mode=extraction_mode,
        )
        edition_id = str(payload.get("anchor_edition_id", row.get("anchor_edition_id", "")))
        if board_id in MARVEL_ACTION_SPACE_NAME_OVERRIDES or board_id in STAR_WARS_ACTION_SPACE_NAME_OVERRIDES:
            _upsert_simple_citation(
                payload,
                rule_path="board.spaces.chance.name",
                edition_id=edition_id,
                page_ref="manual-extract:action-space-labels",
                confidence="medium",
            )
            _upsert_simple_citation(
                payload,
                rule_path="board.spaces.community_chest.name",
                edition_id=edition_id,
                page_ref="manual-extract:action-space-labels",
                confidence="medium",
            )
        if board_id in MARVEL_DECK_METADATA_OVERRIDES:
            _upsert_simple_citation(
                payload,
                rule_path="mechanics.decks",
                edition_id=edition_id,
                page_ref="manual-extract:deck-labels",
                confidence="medium",
            )
        _write_json(path, payload)
        changed += 1

    print(f"Seeded manual extraction metadata into {changed} board payload files")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Apply extracted manual metadata into Marvel/Star manual rule payloads."
    )
    parser.add_argument(
        "--anchor-index",
        type=Path,
        default=Path("server/games/monopoly/catalog/special_board_anchor_index.json"),
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("server/games/monopoly/manual_rules/extracted/manifest.json"),
    )
    parser.add_argument(
        "--manual-rules-dir",
        type=Path,
        default=Path("server/games/monopoly/manual_rules/data"),
    )
    args = parser.parse_args()

    run_seed(
        anchor_index_path=args.anchor_index,
        manifest_path=args.manifest,
        manual_rules_dir=args.manual_rules_dir,
    )


if __name__ == "__main__":
    main()
