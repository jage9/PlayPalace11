"""Coverage for Disney/Marvel-family manual rule payloads."""

from __future__ import annotations

import pytest

from server.games.monopoly.game import (
    CHANCE_CARD_IDS,
    COMMUNITY_CHEST_CARD_IDS,
    MonopolyGame,
    MonopolyOptions,
)
from server.games.monopoly.manual_rules.loader import load_manual_rule_set
from server.users.test_user import MockUser


DISNEY_MARVEL_FAMILY_BOARD_IDS = [
    "disney_princesses",
    "disney_animation",
    "disney_lion_king",
    "disney_mickey_friends",
    "disney_villains",
    "disney_lightyear",
    "disney_legacy",
    "disney_the_edition",
    "marvel_80_years",
    "marvel_avengers",
    "marvel_spider_man",
    "marvel_black_panther_wf",
    "marvel_super_villains",
    "marvel_deadpool",
    "marvel_avengers_legacy",
    "marvel_eternals",
    "marvel_falcon_winter_soldier",
    "marvel_flip",
]

DISNEY_MARVEL_LITERAL_TEXT_BOARD_IDS = [
    "disney_animation",
    "disney_legacy",
    "disney_lightyear",
    "disney_lion_king",
    "disney_mickey_friends",
    "disney_villains",
    "marvel_80_years",
    "marvel_avengers",
    "marvel_black_panther_wf",
    "marvel_deadpool",
    "marvel_eternals",
    "marvel_falcon_winter_soldier",
    "marvel_spider_man",
    "marvel_super_villains",
]

NATIVE_MARVEL_DECK_ID_OVERRIDES = {
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


@pytest.mark.parametrize("board_id", DISNEY_MARVEL_FAMILY_BOARD_IDS)
def test_disney_marvel_manual_rule_payload_has_full_card_and_space_baseline(board_id: str):
    rule_set = load_manual_rule_set(board_id)

    spaces = rule_set.board.get("spaces", [])
    chance_rows = rule_set.cards.get("chance", [])
    community_rows = rule_set.cards.get("community_chest", [])
    deck_override = NATIVE_MARVEL_DECK_ID_OVERRIDES.get(board_id, {})
    expected_chance_ids = deck_override.get("chance", CHANCE_CARD_IDS)
    expected_community_ids = deck_override.get("community_chest", COMMUNITY_CHEST_CARD_IDS)

    assert len(spaces) == 40
    assert [row["id"] for row in chance_rows] == expected_chance_ids
    assert [row["id"] for row in community_rows] == expected_community_ids


@pytest.mark.parametrize(
    ("board_id", "card_id", "expected_amount"),
    [
        ("disney_princesses", "bank_dividend_50", 90),
        ("disney_lightyear", "bank_dividend_50", 88),
        ("disney_lion_king", "income_tax_refund_20", 75),
        ("disney_villains", "bank_dividend_50", 68),
        ("disney_legacy", "bank_error_collect_200", 210),
        ("marvel_80_years", "bank_dividend_50", 92),
        ("marvel_avengers", "bank_error_collect_200", 220),
        ("marvel_black_panther_wf", "income_tax_refund_20", 70),
        ("marvel_avengers_legacy", "villains_bank_error_collect_215", 215),
        ("marvel_eternals", "bank_dividend_50", 85),
    ],
)
def test_disney_marvel_manual_rule_payload_encodes_card_amount_overrides(
    board_id: str,
    card_id: str,
    expected_amount: int,
):
    rule_set = load_manual_rule_set(board_id)
    rows = rule_set.cards.get("chance", []) + rule_set.cards.get("community_chest", [])
    row = next(row for row in rows if row.get("id") == card_id)
    effect = row.get("effect", {})

    assert effect.get("amount") == expected_amount


def test_disney_marvel_manual_rule_payload_executes_manual_effect_for_remapped_card(monkeypatch):
    game = _start_game("disney_mickey_friends")
    host = game.current_player
    assert host is not None

    host.position = 5
    monkeypatch.setattr(game, "_draw_card", lambda deck_type: "bank_dividend_50")
    rolls = iter([1, 1])
    monkeypatch.setattr("server.games.monopoly.game.random.randint", lambda a, b: next(rolls))

    original = game._apply_manual_card_effect
    seen_effect_types: list[str] = []

    def _wrapped_apply(player, effect_spec, *, depth, dice_total):
        effect_type = effect_spec.get("type")
        if isinstance(effect_type, str):
            seen_effect_types.append(effect_type)
        return original(player, effect_spec, depth=depth, dice_total=dice_total)

    monkeypatch.setattr(game, "_apply_manual_card_effect", _wrapped_apply)

    game.execute_action(host, "roll_dice")

    assert "move_absolute" in seen_effect_types
    assert host.position == 0
    assert host.cash == 1700


@pytest.mark.parametrize(
    ("board_id", "space_before_roll", "deck_type", "drawn_card", "expected_deck_label"),
    [
        ("marvel_avengers_legacy", 5, "chance", "advance_to_go", "S.H.I.E.L.D."),
        (
            "marvel_avengers_legacy",
            0,
            "community_chest",
            "bank_error_collect_200",
            "Villains",
        ),
        ("marvel_flip", 5, "chance", "bank_dividend_50", "Event"),
        ("marvel_flip", 0, "community_chest", "bank_error_collect_200", "Team-Up"),
    ],
)
def test_disney_marvel_manual_rule_payload_uses_manual_deck_labels_in_card_draw_broadcast(
    board_id: str,
    space_before_roll: int,
    deck_type: str,
    drawn_card: str,
    expected_deck_label: str,
    monkeypatch,
) -> None:
    game = _start_game(board_id)
    host = game.current_player
    assert host is not None

    host.position = space_before_roll
    def _draw_expected(card_deck: str) -> str:
        assert card_deck == deck_type
        return drawn_card

    monkeypatch.setattr(game, "_draw_card", _draw_expected)
    rolls = iter([1, 1])
    monkeypatch.setattr("server.games.monopoly.game.random.randint", lambda a, b: next(rolls))

    seen_events: list[tuple[str, dict[str, object]]] = []

    def _capture_broadcast(message_key: str, **kwargs):
        seen_events.append((message_key, kwargs))

    monkeypatch.setattr(game, "broadcast_l", _capture_broadcast)
    game.execute_action(host, "roll_dice")

    card_draw_events = [kwargs for key, kwargs in seen_events if key == "monopoly-card-drawn"]
    assert card_draw_events
    assert card_draw_events[0].get("deck") == expected_deck_label


@pytest.mark.parametrize("board_id", DISNEY_MARVEL_LITERAL_TEXT_BOARD_IDS)
@pytest.mark.parametrize(
    ("deck_type", "card_id", "expected_substring"),
    [
        ("chance", "advance_to_go", "GO"),
        ("chance", "go_to_jail", "In Jail"),
        ("community_chest", "go_to_jail", "In Jail"),
        ("community_chest", "get_out_of_jail_free", "Get Out of Jail Free"),
    ],
)
def test_disney_marvel_manual_rule_payload_includes_literal_card_text(
    board_id: str,
    deck_type: str,
    card_id: str,
    expected_substring: str,
) -> None:
    rule_set = load_manual_rule_set(board_id)
    deck_rows = rule_set.cards.get(deck_type, [])
    row = next(row for row in deck_rows if row.get("id") == card_id)
    literal_text = row.get("text")
    assert isinstance(literal_text, str)
    assert expected_substring in literal_text


@pytest.mark.parametrize(
    ("deck_type", "card_id", "expected_substring"),
    [
        ("chance", "advance_to_go", "CASA DE PARTIDA"),
        ("chance", "go_to_jail", "Prisão"),
        ("community_chest", "go_to_jail", "Prisão"),
        ("community_chest", "get_out_of_jail_free", "Estás Livre Da Prisão"),
    ],
)
def test_disney_marvel_manual_rule_payload_includes_literal_card_text_for_disney_princesses(
    deck_type: str,
    card_id: str,
    expected_substring: str,
) -> None:
    rule_set = load_manual_rule_set("disney_princesses")
    deck_rows = rule_set.cards.get(deck_type, [])
    row = next(row for row in deck_rows if row.get("id") == card_id)
    literal_text = row.get("text")
    assert isinstance(literal_text, str)
    assert expected_substring in literal_text


@pytest.mark.parametrize(
    ("deck_type", "card_id", "expected_substring"),
    [
        ("chance", "advance_to_go", "advance to go"),
        ("chance", "go_to_jail", "go directly to jail"),
        ("community_chest", "go_to_jail", "go directly to jail"),
        ("community_chest", "get_out_of_jail_free", "get out of jail free"),
    ],
)
def test_disney_marvel_manual_rule_payload_includes_literal_card_text_for_disney_the_edition(
    deck_type: str,
    card_id: str,
    expected_substring: str,
) -> None:
    rule_set = load_manual_rule_set("disney_the_edition")
    deck_rows = rule_set.cards.get(deck_type, [])
    row = next(row for row in deck_rows if row.get("id") == card_id)
    literal_text = row.get("text")
    assert isinstance(literal_text, str)
    assert expected_substring in literal_text.lower()


@pytest.mark.parametrize(
    ("board_id", "deck_type", "card_id"),
    [
        ("marvel_avengers_legacy", "chance", "shield_go_to_jail"),
        ("marvel_avengers_legacy", "community_chest", "villains_go_to_jail"),
        ("marvel_flip", "chance", "event_go_to_jail_primary"),
        ("marvel_flip", "community_chest", "team_up_go_to_jail"),
    ],
)
def test_disney_marvel_manual_rule_payload_includes_partial_literal_card_text_for_remaining_marvel_boards(
    board_id: str,
    deck_type: str,
    card_id: str,
) -> None:
    rule_set = load_manual_rule_set(board_id)
    deck_rows = rule_set.cards.get(deck_type, [])
    row = next(row for row in deck_rows if row.get("id") == card_id)
    literal_text = row.get("text")
    assert isinstance(literal_text, str)
    assert "Do not pass GO." in literal_text


@pytest.mark.parametrize(
    ("board_id", "deck_type", "card_id", "expected_evidence_substring"),
    [
        (
            "marvel_avengers_legacy",
            "chance",
            "shield_advance_to_go",
            "Chance and Community Chest cards",
        ),
        (
            "marvel_avengers_legacy",
            "community_chest",
            "villains_jail_release_options",
            "How do I get out of Jail?",
        ),
        (
            "marvel_flip",
            "chance",
            "event_advance_to_go",
            "Team-Up Cards",
        ),
        (
            "marvel_flip",
            "community_chest",
            "team_up_jail_release_options",
            "pay BP or roll",
        ),
    ],
)
def test_disney_marvel_manual_rule_payload_marks_unobserved_literal_card_text_for_remaining_marvel_boards(
    board_id: str,
    deck_type: str,
    card_id: str,
    expected_evidence_substring: str,
) -> None:
    rule_set = load_manual_rule_set(board_id)
    deck_rows = rule_set.cards.get(deck_type, [])
    row = next(row for row in deck_rows if row.get("id") == card_id)

    assert row.get("text_status") == "not_observed_in_available_manual_sources"
    note = row.get("text_note")
    assert isinstance(note, str)
    assert "deck modeling" in note
    evidence = row.get("text_evidence")
    assert isinstance(evidence, str)
    assert expected_evidence_substring in evidence
