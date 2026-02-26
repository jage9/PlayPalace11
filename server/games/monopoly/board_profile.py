"""Board profile and resolver utilities for Monopoly themed boards."""

from __future__ import annotations

from dataclasses import dataclass


DEFAULT_BOARD_ID = "classic_default"
DEFAULT_BOARD_RULES_MODE = "auto"
BOARD_RULES_MODES: tuple[str, ...] = ("auto", "skin_only")


@dataclass(frozen=True)
class BoardProfile:
    """Static metadata for one selectable Monopoly board profile."""

    board_id: str
    label_key: str
    anchor_edition_id: str
    compatible_preset_ids: tuple[str, ...]
    fallback_preset_id: str
    rule_pack_id: str | None = None
    rule_pack_status: str = "none"


@dataclass(frozen=True)
class ResolvedBoardPlan:
    """Normalized board selection plan for runtime startup."""

    requested_preset_id: str
    requested_board_id: str
    requested_mode: str
    effective_preset_id: str
    effective_board_id: str
    effective_mode: str
    rule_pack_id: str | None
    rule_pack_status: str
    auto_fixed_from_preset_id: str | None = None


BOARD_PROFILES: dict[str, BoardProfile] = {
    DEFAULT_BOARD_ID: BoardProfile(
        board_id=DEFAULT_BOARD_ID,
        label_key="monopoly-board-classic-default",
        anchor_edition_id="monopoly-00009",
        compatible_preset_ids=(
            "classic_standard",
            "junior",
            "junior_modern",
            "junior_legacy",
            "cheaters",
            "electronic_banking",
            "voice_banking",
            "speed",
            "builder",
            "sore_losers",
            "free_parking_jackpot",
            "city",
            "bid_card_game",
            "deal_card_game",
            "knockout",
        ),
        fallback_preset_id="classic_standard",
        rule_pack_id=None,
        rule_pack_status="none",
    ),
    "mario_collectors": BoardProfile(
        board_id="mario_collectors",
        label_key="monopoly-board-mario-collectors",
        anchor_edition_id="monopoly-c4382",
        compatible_preset_ids=("classic_standard",),
        fallback_preset_id="classic_standard",
        rule_pack_id="mario_collectors",
        rule_pack_status="partial",
    ),
    "mario_kart": BoardProfile(
        board_id="mario_kart",
        label_key="monopoly-board-mario-kart",
        anchor_edition_id="monopoly-e1870",
        compatible_preset_ids=("classic_standard",),
        fallback_preset_id="classic_standard",
        rule_pack_id="mario_kart",
        rule_pack_status="partial",
    ),
    "mario_celebration": BoardProfile(
        board_id="mario_celebration",
        label_key="monopoly-board-mario-celebration",
        anchor_edition_id="monopoly-e9517",
        compatible_preset_ids=("classic_standard",),
        fallback_preset_id="classic_standard",
        rule_pack_id="mario_celebration",
        rule_pack_status="partial",
    ),
    "mario_movie": BoardProfile(
        board_id="mario_movie",
        label_key="monopoly-board-mario-movie",
        anchor_edition_id="monopoly-f6818",
        compatible_preset_ids=("classic_standard",),
        fallback_preset_id="classic_standard",
        rule_pack_id="mario_movie",
        rule_pack_status="partial",
    ),
    "junior_super_mario": BoardProfile(
        board_id="junior_super_mario",
        label_key="monopoly-board-junior-super-mario",
        anchor_edition_id="monopoly-f4817",
        compatible_preset_ids=("junior", "junior_modern", "junior_legacy"),
        fallback_preset_id="junior",
        rule_pack_id="junior_super_mario",
        rule_pack_status="partial",
    ),
}


def get_board_profile(board_id: str) -> BoardProfile:
    """Return board profile, falling back to default board profile."""
    return BOARD_PROFILES.get(board_id, BOARD_PROFILES[DEFAULT_BOARD_ID])


def get_available_board_ids() -> list[str]:
    """Return selectable board ids with default board first."""
    ids = [DEFAULT_BOARD_ID]
    ids.extend(board_id for board_id in sorted(BOARD_PROFILES) if board_id != DEFAULT_BOARD_ID)
    return ids


def get_available_board_rules_modes() -> list[str]:
    """Return selectable board rules mode ids."""
    return list(BOARD_RULES_MODES)


def resolve_board_plan(
    preset_id: str,
    board_id: str,
    mode: str,
) -> ResolvedBoardPlan:
    """Resolve a deterministic runtime board plan.

    The resolver enforces board compatibility and normalizes mode handling:
    - unknown board id -> default board profile
    - incompatible preset -> fallback preset with auto-fix metadata
    - `skin_only` forces skin-only behavior
    - `auto` enables board-rules only when a rule pack exists
    """
    profile = get_board_profile(board_id)

    requested_mode = mode if mode in BOARD_RULES_MODES else DEFAULT_BOARD_RULES_MODE
    effective_preset_id = preset_id
    auto_fixed_from: str | None = None
    if effective_preset_id not in profile.compatible_preset_ids:
        auto_fixed_from = effective_preset_id
        effective_preset_id = profile.fallback_preset_id

    if requested_mode == "skin_only":
        effective_mode = "skin_only"
    elif profile.rule_pack_id and profile.rule_pack_status in {"partial", "full"}:
        effective_mode = "board_rules"
    else:
        effective_mode = "skin_only"

    return ResolvedBoardPlan(
        requested_preset_id=preset_id,
        requested_board_id=board_id,
        requested_mode=requested_mode,
        effective_preset_id=effective_preset_id,
        effective_board_id=profile.board_id,
        effective_mode=effective_mode,
        rule_pack_id=profile.rule_pack_id,
        rule_pack_status=profile.rule_pack_status,
        auto_fixed_from_preset_id=auto_fixed_from,
    )
