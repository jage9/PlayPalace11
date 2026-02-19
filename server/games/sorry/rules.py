"""Rules profile models for Sorry editions."""

from dataclasses import dataclass
from typing import Protocol


class SorryRulesProfile(Protocol):
    """Protocol implemented by each Sorry ruleset profile."""

    profile_id: str
    display_name: str
    pawns_per_player: int

    def card_faces(self) -> tuple[str, ...]:
        """Return supported card faces for this profile."""
        ...

    def can_leave_start_with_card(self, card_face: str) -> bool:
        """Return whether this card can move a pawn from start."""
        ...

    def forward_steps_for_card(self, card_face: str) -> tuple[int, ...]:
        """Return forward step options contributed by this card."""
        ...

    def backward_steps_for_card(self, card_face: str) -> tuple[int, ...]:
        """Return backward step options contributed by this card."""
        ...

    def allows_split_seven(self, card_face: str) -> bool:
        """Return whether this card allows split-seven move generation."""
        ...

    def allows_swap(self, card_face: str) -> bool:
        """Return whether this card allows swap move generation."""
        ...

    def allows_sorry(self, card_face: str) -> bool:
        """Return whether this card allows Sorry replacement moves."""
        ...

    def card_two_grants_extra_turn(self) -> bool:
        """Return whether card 2 grants another turn."""
        ...


@dataclass(frozen=True)
class Classic00390Rules:
    """Classic Sorry rules profile based on Hasbro 00390."""

    profile_id: str = "classic_00390"
    display_name: str = "Classic 00390"
    pawns_per_player: int = 4
    _faces: tuple[str, ...] = (
        "1",
        "2",
        "3",
        "4",
        "5",
        "7",
        "8",
        "10",
        "11",
        "12",
        "sorry",
    )

    def card_faces(self) -> tuple[str, ...]:
        return self._faces

    def can_leave_start_with_card(self, card_face: str) -> bool:
        return card_face in {"1", "2"}

    def forward_steps_for_card(self, card_face: str) -> tuple[int, ...]:
        if card_face in {"1", "2", "3", "5", "7", "8", "10", "11", "12"}:
            return (int(card_face),)
        return ()

    def backward_steps_for_card(self, card_face: str) -> tuple[int, ...]:
        if card_face == "4":
            return (4,)
        if card_face == "10":
            return (1,)
        return ()

    def allows_split_seven(self, card_face: str) -> bool:
        return card_face == "7"

    def allows_swap(self, card_face: str) -> bool:
        return card_face == "11"

    def allows_sorry(self, card_face: str) -> bool:
        return card_face == "sorry"

    def card_two_grants_extra_turn(self) -> bool:
        return True


@dataclass(frozen=True)
class A5065CoreRules:
    """A5065 core profile scaffold.

    Milestone 2 wiring uses classic-equivalent behavior until profile deltas
    are implemented in later milestones.
    """

    profile_id: str = "a5065_core"
    display_name: str = "A5065 Core"
    pawns_per_player: int = 3

    def card_faces(self) -> tuple[str, ...]:
        return Classic00390Rules().card_faces()

    def can_leave_start_with_card(self, card_face: str) -> bool:
        return Classic00390Rules().can_leave_start_with_card(card_face)

    def forward_steps_for_card(self, card_face: str) -> tuple[int, ...]:
        return Classic00390Rules().forward_steps_for_card(card_face)

    def backward_steps_for_card(self, card_face: str) -> tuple[int, ...]:
        return Classic00390Rules().backward_steps_for_card(card_face)

    def allows_split_seven(self, card_face: str) -> bool:
        return Classic00390Rules().allows_split_seven(card_face)

    def allows_swap(self, card_face: str) -> bool:
        return Classic00390Rules().allows_swap(card_face)

    def allows_sorry(self, card_face: str) -> bool:
        return Classic00390Rules().allows_sorry(card_face)

    def card_two_grants_extra_turn(self) -> bool:
        return Classic00390Rules().card_two_grants_extra_turn()


RULES_PROFILES: dict[str, SorryRulesProfile] = {
    "classic_00390": Classic00390Rules(),
    "a5065_core": A5065CoreRules(),
}


def get_rules_profile_by_id(profile_id: str | None) -> SorryRulesProfile | None:
    """Return profile object for a known profile id."""
    if profile_id is None:
        return None
    return RULES_PROFILES.get(profile_id)


def get_supported_profile_ids() -> tuple[str, ...]:
    """Return known profile ids in stable option order."""
    return tuple(RULES_PROFILES.keys())
