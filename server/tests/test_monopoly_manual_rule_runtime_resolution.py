"""Tests for runtime loading of manual Monopoly rule artifacts."""

from server.games.monopoly.game import MonopolyGame, MonopolyOptions
from server.games.monopoly.manual_rules.models import ManualRuleSet
from server.users.test_user import MockUser


def _build_manual_rule_set(board_id: str) -> ManualRuleSet:
    return ManualRuleSet.from_dict(
        {
            "board_id": board_id,
            "anchor_edition_id": "monopoly-e1870",
            "board": {"spaces": []},
            "economy": {"properties": {}},
            "cards": {"chance": [], "community_chest": []},
            "mechanics": {},
            "win_condition": {"type": "bankruptcy"},
            "citations": [
                {
                    "rule_path": "board.spaces",
                    "edition_id": "monopoly-e1870",
                    "page_ref": "p.2",
                    "confidence": "high",
                }
            ],
        }
    )


def _start_game(board_id: str) -> MonopolyGame:
    game = MonopolyGame(
        options=MonopolyOptions(
            preset_id="classic_standard",
            board_id=board_id,
            board_rules_mode="auto",
        )
    )
    game.add_player("Host", MockUser("Host"))
    game.add_player("Guest", MockUser("Guest"))
    game.host = "Host"
    game.on_start()
    return game


def test_board_rules_mode_uses_loaded_manual_rule_set(monkeypatch):
    expected_rules = _build_manual_rule_set("mario_kart")
    monkeypatch.setattr(
        "server.games.monopoly.game.load_manual_rule_set",
        lambda board_id: expected_rules,
    )

    game = _start_game("mario_kart")

    assert game.active_board_effective_mode == "board_rules"
    assert game.active_manual_rule_set is not None
    assert game.active_manual_rule_set.board_id == "mario_kart"


def test_board_rules_mode_falls_back_when_manual_rule_file_missing():
    game = _start_game("mario_kart")

    assert game.active_board_effective_mode == "board_rules"
    assert game.active_manual_rule_set is None
