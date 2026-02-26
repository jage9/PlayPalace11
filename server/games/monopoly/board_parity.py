"""Special-board parity manifest for staged fidelity rollout."""

from __future__ import annotations

from dataclasses import dataclass

from .board_profile import BOARD_PROFILES, DEFAULT_BOARD_ID
from .board_rules_registry import get_rule_pack


@dataclass(frozen=True)
class BoardParityProfile:
    """Normalized parity metadata for one special board."""

    board_id: str
    rule_pack_id: str
    anchor_edition_id: str
    canonical_manual_edition_id: str
    fidelity_status: str
    deck_mode: str
    capability_ids: tuple[str, ...]
    hardware_capability_ids: tuple[str, ...]


_FIDELITY_OVERRIDES: dict[str, str] = {
    "mario_kart": "partial_plus",
    "mario_movie": "partial_plus",
    "mario_collectors": "partial_plus",
    "mario_celebration": "partial_plus",
    "junior_super_mario": "manual_core",
    "disney_star_wars_dark_side": "partial_plus",
    "star_wars_40th": "partial_plus",
    "star_wars_boba_fett": "partial_plus",
    "star_wars_light_side": "partial_plus",
    "star_wars_the_child": "partial_plus",
    "star_wars_mandalorian": "partial_plus",
    "star_wars_complete_saga": "partial_plus",
    "star_wars_saga": "partial_plus",
    "star_wars_legacy": "partial_plus",
    "star_wars_classic_edition": "partial_plus",
    "star_wars_solo": "partial_plus",
    "star_wars_mandalorian_s2": "partial_plus",
    "disney_animation": "partial_plus",
    "disney_legacy": "partial_plus",
    "disney_lightyear": "partial_plus",
    "disney_lion_king": "partial_plus",
    "disney_mickey_friends": "partial_plus",
    "disney_princesses": "partial_plus",
    "disney_the_edition": "partial_plus",
    "disney_villains": "partial_plus",
    "marvel_80_years": "partial_plus",
    "marvel_avengers": "partial_plus",
    "marvel_avengers_legacy": "partial_plus",
    "marvel_black_panther_wf": "partial_plus",
    "marvel_deadpool": "partial_plus",
    "marvel_eternals": "partial_plus",
    "marvel_falcon_winter_soldier": "partial_plus",
    "marvel_flip": "partial_plus",
    "marvel_spider_man": "partial_plus",
    "marvel_super_villains": "partial_plus",
    "harry_potter": "partial_plus",
    "fortnite": "partial_plus",
    "stranger_things": "partial_plus",
}


def _resolve_fidelity_status(board_id: str) -> str:
    """Resolve current parity fidelity status for board."""
    return _FIDELITY_OVERRIDES.get(board_id, "partial")


def _resolve_deck_mode(capability_ids: tuple[str, ...]) -> str:
    """Resolve deck mode from declared card/manual capabilities."""
    deck_capabilities = {"card_id_remap", "card_cash_override", "junior_manual_core"}
    if any(capability_id in deck_capabilities for capability_id in capability_ids):
        return "board_specific"
    return "classic"


def _resolve_hardware_capability_ids(capability_ids: tuple[str, ...]) -> tuple[str, ...]:
    """Filter capability ids that represent hardware/audio paths."""
    hardware_ids = [
        capability_id
        for capability_id in capability_ids
        if (
            "hardware" in capability_id
            or "audio" in capability_id
            or "sound" in capability_id
        )
    ]
    return tuple(hardware_ids)


def _build_profiles() -> dict[str, BoardParityProfile]:
    """Build parity profiles for all special boards currently onboarded."""
    profiles: dict[str, BoardParityProfile] = {}
    for board_id, profile in BOARD_PROFILES.items():
        if board_id == DEFAULT_BOARD_ID:
            continue
        rule_pack_id = profile.rule_pack_id or board_id
        pack = get_rule_pack(rule_pack_id)
        capability_ids = pack.capability_ids if pack is not None else ()
        profiles[board_id] = BoardParityProfile(
            board_id=board_id,
            rule_pack_id=rule_pack_id,
            anchor_edition_id=profile.anchor_edition_id,
            canonical_manual_edition_id=profile.anchor_edition_id,
            fidelity_status=_resolve_fidelity_status(board_id),
            deck_mode=_resolve_deck_mode(capability_ids),
            capability_ids=capability_ids,
            hardware_capability_ids=_resolve_hardware_capability_ids(capability_ids),
        )
    return profiles


BOARD_PARITY_PROFILES: dict[str, BoardParityProfile] = _build_profiles()


def get_board_parity_profile(board_id: str) -> BoardParityProfile | None:
    """Return parity profile for a board when available."""
    return BOARD_PARITY_PROFILES.get(board_id)


def get_parity_board_ids() -> list[str]:
    """Return sorted board ids represented by parity manifest."""
    return sorted(BOARD_PARITY_PROFILES)
