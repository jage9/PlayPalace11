"""Alignment checks for manual-core fidelity across Monopoly artifacts."""

from __future__ import annotations

import json
from pathlib import Path

from server.games.monopoly.board_parity import (
    get_board_parity_profile,
    get_parity_board_ids,
)


def _index_path() -> Path:
    return (
        Path(__file__).resolve().parents[1]
        / "games"
        / "monopoly"
        / "catalog"
        / "special_board_anchor_index.json"
    )


def test_board_parity_and_anchor_index_fidelity_match():
    rows = json.loads(_index_path().read_text(encoding="utf-8"))
    anchor_by_id = {row["board_id"]: row for row in rows}
    parity_ids = set(get_parity_board_ids())

    assert set(anchor_by_id) == parity_ids
    for board_id in sorted(anchor_by_id):
        assert anchor_by_id[board_id].get("fidelity_status") == "manual_core"
        profile = get_board_parity_profile(board_id)
        assert profile is not None
        assert profile.fidelity_status == "manual_core"
