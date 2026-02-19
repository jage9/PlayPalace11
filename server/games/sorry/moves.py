"""Move models and generation/application helpers for Sorry."""

from dataclasses import dataclass

from .rules import SorryRulesProfile
from .state import (
    SAFETY_LENGTH,
    SorryGameState,
    SorryPawnState,
    SorryPlayerState,
    clockwise_distance,
    normalize_track_position,
)

_SLIDE_START_TO_STEPS_BY_OFFSET: dict[int, int] = {
    5: 4,
    12: 3,
}


@dataclass(frozen=True)
class PawnDestination:
    """Destination for a pawn movement."""

    zone: str
    track_position: int | None = None
    home_steps: int = 0


@dataclass(frozen=True)
class SorryMove:
    """A legal move candidate for a player."""

    action_id: str
    move_type: str
    description: str
    pawn_index: int | None = None
    steps: int | None = None
    secondary_pawn_index: int | None = None
    secondary_steps: int | None = None
    target_player_id: str | None = None
    target_pawn_index: int | None = None


def _get_pawn(
    player_state: SorryPlayerState,
    pawn_index: int | None,
) -> SorryPawnState | None:
    if pawn_index is None:
        return None
    if pawn_index < 1 or pawn_index > len(player_state.pawns):
        return None
    return player_state.pawns[pawn_index - 1]


def _player_by_id(
    state: SorryGameState,
    player_id: str | None,
) -> SorryPlayerState | None:
    if player_id is None:
        return None
    return state.player_states.get(player_id)


def _compute_forward_destination(
    player_state: SorryPlayerState,
    pawn: SorryPawnState,
    steps: int,
) -> PawnDestination | None:
    if steps <= 0:
        return None

    if pawn.zone == "home":
        return None

    if pawn.zone == "home_path":
        next_steps = pawn.home_steps + steps
        if next_steps <= SAFETY_LENGTH:
            return PawnDestination(zone="home_path", home_steps=next_steps)
        if next_steps == SAFETY_LENGTH + 1:
            return PawnDestination(zone="home")
        return None

    if pawn.zone != "track" or pawn.track_position is None:
        return None

    distance_to_home_entry = clockwise_distance(
        pawn.track_position,
        player_state.home_entry_track,
    )

    if steps <= distance_to_home_entry:
        return PawnDestination(
            zone="track",
            track_position=normalize_track_position(pawn.track_position + steps),
        )

    remaining = steps - distance_to_home_entry
    if remaining <= SAFETY_LENGTH:
        return PawnDestination(zone="home_path", home_steps=remaining)
    if remaining == SAFETY_LENGTH + 1:
        return PawnDestination(zone="home")
    return None


def _compute_backward_destination(
    pawn: SorryPawnState,
    steps: int,
) -> PawnDestination | None:
    if steps <= 0:
        return None
    if pawn.zone != "track" or pawn.track_position is None:
        return None
    return PawnDestination(
        zone="track",
        track_position=normalize_track_position(pawn.track_position - steps),
    )


def _is_destination_legal_for_player(
    player_state: SorryPlayerState,
    destination: PawnDestination,
    *,
    ignore_pawn_indexes: set[int] | None = None,
) -> bool:
    ignore = ignore_pawn_indexes or set()
    for pawn in player_state.pawns:
        if pawn.pawn_index in ignore:
            continue
        if destination.zone == "track":
            if (
                pawn.zone == "track"
                and pawn.track_position is not None
                and normalize_track_position(pawn.track_position)
                == normalize_track_position(destination.track_position or 0)
            ):
                return False
        elif destination.zone == "home_path":
            if pawn.zone == "home_path" and pawn.home_steps == destination.home_steps:
                return False
    return True


def _iter_track_pawns(
    player_state: SorryPlayerState,
) -> list[SorryPawnState]:
    return [
        pawn
        for pawn in player_state.pawns
        if pawn.zone == "track" and pawn.track_position is not None
    ]


def _generate_start_moves(
    state: SorryGameState,
    player_state: SorryPlayerState,
) -> list[SorryMove]:
    destination = PawnDestination(
        zone="track",
        track_position=player_state.start_track,
    )
    if not _is_destination_legal_for_player(player_state, destination):
        return []

    moves: list[SorryMove] = []
    for pawn in player_state.pawns:
        if pawn.zone != "start":
            continue
        moves.append(
            SorryMove(
                action_id=f"start_p{pawn.pawn_index}",
                move_type="start",
                description=f"Move pawn {pawn.pawn_index} out of start",
                pawn_index=pawn.pawn_index,
            )
        )
    _ = state
    return moves


def _generate_forward_moves(
    player_state: SorryPlayerState,
    steps: int,
) -> list[SorryMove]:
    moves: list[SorryMove] = []
    for pawn in player_state.pawns:
        destination = _compute_forward_destination(player_state, pawn, steps)
        if destination is None:
            continue
        if not _is_destination_legal_for_player(
            player_state,
            destination,
            ignore_pawn_indexes={pawn.pawn_index},
        ):
            continue
        moves.append(
            SorryMove(
                action_id=f"forward{steps}_p{pawn.pawn_index}",
                move_type="forward",
                description=f"Move pawn {pawn.pawn_index} forward {steps}",
                pawn_index=pawn.pawn_index,
                steps=steps,
            )
        )
    return moves


def _generate_backward_moves(
    player_state: SorryPlayerState,
    steps: int,
) -> list[SorryMove]:
    moves: list[SorryMove] = []
    for pawn in player_state.pawns:
        destination = _compute_backward_destination(pawn, steps)
        if destination is None:
            continue
        if not _is_destination_legal_for_player(
            player_state,
            destination,
            ignore_pawn_indexes={pawn.pawn_index},
        ):
            continue
        moves.append(
            SorryMove(
                action_id=f"backward{steps}_p{pawn.pawn_index}",
                move_type="backward",
                description=f"Move pawn {pawn.pawn_index} backward {steps}",
                pawn_index=pawn.pawn_index,
                steps=steps,
            )
        )
    return moves


def _generate_swap_moves(
    state: SorryGameState,
    player_state: SorryPlayerState,
) -> list[SorryMove]:
    own_track = _iter_track_pawns(player_state)
    if not own_track:
        return []

    moves: list[SorryMove] = []
    for own_pawn in own_track:
        for opponent_id, opponent_state in state.player_states.items():
            if opponent_id == player_state.player_id:
                continue
            for target in _iter_track_pawns(opponent_state):
                moves.append(
                    SorryMove(
                        action_id=(
                            f"swap_p{own_pawn.pawn_index}_"
                            f"{opponent_id}_p{target.pawn_index}"
                        ),
                        move_type="swap",
                        description=(
                            f"Swap pawn {own_pawn.pawn_index} with "
                            f"{opponent_id} pawn {target.pawn_index}"
                        ),
                        pawn_index=own_pawn.pawn_index,
                        target_player_id=opponent_id,
                        target_pawn_index=target.pawn_index,
                    )
                )
    return moves


def _generate_sorry_moves(
    state: SorryGameState,
    player_state: SorryPlayerState,
) -> list[SorryMove]:
    start_pawns = [pawn for pawn in player_state.pawns if pawn.zone == "start"]
    if not start_pawns:
        return []

    moves: list[SorryMove] = []
    for own_pawn in start_pawns:
        for opponent_id, opponent_state in state.player_states.items():
            if opponent_id == player_state.player_id:
                continue
            for target in _iter_track_pawns(opponent_state):
                destination = PawnDestination(
                    zone="track",
                    track_position=target.track_position,
                )
                if not _is_destination_legal_for_player(
                    player_state,
                    destination,
                    ignore_pawn_indexes={own_pawn.pawn_index},
                ):
                    continue
                moves.append(
                    SorryMove(
                        action_id=(
                            f"sorry_p{own_pawn.pawn_index}_"
                            f"{opponent_id}_p{target.pawn_index}"
                        ),
                        move_type="sorry",
                        description=(
                            f"Move pawn {own_pawn.pawn_index} to replace "
                            f"{opponent_id} pawn {target.pawn_index}"
                        ),
                        pawn_index=own_pawn.pawn_index,
                        target_player_id=opponent_id,
                        target_pawn_index=target.pawn_index,
                    )
                )
    return moves


def _generate_sorry_fallback_forward_moves(
    player_state: SorryPlayerState,
    steps: int,
) -> list[SorryMove]:
    moves: list[SorryMove] = []
    for pawn in player_state.pawns:
        destination = _compute_forward_destination(player_state, pawn, steps)
        if destination is None:
            continue
        if not _is_destination_legal_for_player(
            player_state,
            destination,
            ignore_pawn_indexes={pawn.pawn_index},
        ):
            continue
        moves.append(
            SorryMove(
                action_id=f"sorry_fwd{steps}_p{pawn.pawn_index}",
                move_type="sorry_fallback_forward",
                description=f"Move pawn {pawn.pawn_index} forward {steps}",
                pawn_index=pawn.pawn_index,
                steps=steps,
            )
        )
    return moves


def _generate_split_seven_moves(
    player_state: SorryPlayerState,
) -> list[SorryMove]:
    movable = [
        pawn.pawn_index
        for pawn in player_state.pawns
        if pawn.zone in {"track", "home_path"}
    ]
    if len(movable) < 2:
        return []

    moves: list[SorryMove] = []
    for i, pawn_a_index in enumerate(movable):
        for pawn_b_index in movable[i + 1 :]:
            pawn_a = _get_pawn(player_state, pawn_a_index)
            pawn_b = _get_pawn(player_state, pawn_b_index)
            if pawn_a is None or pawn_b is None:
                continue

            for first_steps in range(1, 7):
                second_steps = 7 - first_steps
                destination_a = _compute_forward_destination(
                    player_state,
                    pawn_a,
                    first_steps,
                )
                destination_b = _compute_forward_destination(
                    player_state,
                    pawn_b,
                    second_steps,
                )
                if destination_a is None or destination_b is None:
                    continue

                if (
                    destination_a.zone == destination_b.zone == "track"
                    and destination_a.track_position == destination_b.track_position
                ):
                    continue
                if (
                    destination_a.zone == destination_b.zone == "home_path"
                    and destination_a.home_steps == destination_b.home_steps
                ):
                    continue

                ignore = {pawn_a_index, pawn_b_index}
                if not _is_destination_legal_for_player(
                    player_state,
                    destination_a,
                    ignore_pawn_indexes=ignore,
                ):
                    continue
                if not _is_destination_legal_for_player(
                    player_state,
                    destination_b,
                    ignore_pawn_indexes=ignore,
                ):
                    continue

                moves.append(
                    SorryMove(
                        action_id=(
                            f"split7_p{pawn_a_index}_{first_steps}"
                            f"_p{pawn_b_index}_{second_steps}"
                        ),
                        move_type="split7",
                        description=(
                            f"Split 7: pawn {pawn_a_index} moves {first_steps}, "
                            f"pawn {pawn_b_index} moves {second_steps}"
                        ),
                        pawn_index=pawn_a_index,
                        steps=first_steps,
                        secondary_pawn_index=pawn_b_index,
                        secondary_steps=second_steps,
                    )
                )
    return moves


def generate_legal_moves(
    state: SorryGameState,
    player_state: SorryPlayerState,
    card_face: str,
    rules: SorryRulesProfile,
) -> list[SorryMove]:
    """Generate legal moves for a player and card."""
    if card_face not in rules.card_faces():
        return []

    moves: list[SorryMove] = []

    if rules.can_leave_start_with_card(card_face):
        moves.extend(_generate_start_moves(state, player_state))

    for forward_steps in rules.forward_steps_for_card(card_face):
        moves.extend(_generate_forward_moves(player_state, forward_steps))

    for backward_steps in rules.backward_steps_for_card(card_face):
        moves.extend(_generate_backward_moves(player_state, backward_steps))

    if rules.allows_split_seven(card_face):
        moves.extend(_generate_split_seven_moves(player_state))

    if rules.allows_swap(card_face):
        moves.extend(_generate_swap_moves(state, player_state))

    if rules.allows_sorry(card_face):
        sorry_moves = _generate_sorry_moves(state, player_state)
        moves.extend(sorry_moves)
        if not sorry_moves:
            for fallback_steps in rules.sorry_fallback_forward_steps(card_face):
                moves.extend(
                    _generate_sorry_fallback_forward_moves(player_state, fallback_steps)
                )

    return sorted(moves, key=lambda move: move.action_id)


def _send_pawn_to_start(pawn: SorryPawnState) -> None:
    pawn.zone = "start"
    pawn.track_position = None
    pawn.home_steps = 0


def _apply_destination(
    pawn: SorryPawnState,
    destination: PawnDestination,
) -> None:
    pawn.zone = destination.zone
    if destination.zone == "track":
        pawn.track_position = destination.track_position
        pawn.home_steps = 0
    elif destination.zone == "home_path":
        pawn.track_position = None
        pawn.home_steps = destination.home_steps
    elif destination.zone == "home":
        pawn.track_position = None
        pawn.home_steps = SAFETY_LENGTH + 1
    else:
        raise ValueError(f"Unsupported destination zone: {destination.zone}")


def _capture_opponents_on_track(
    state: SorryGameState,
    player_state: SorryPlayerState,
    track_position: int | None,
) -> None:
    if track_position is None:
        return
    normalized = normalize_track_position(track_position)
    for other_id, other_state in state.player_states.items():
        if other_id == player_state.player_id:
            continue
        for pawn in other_state.pawns:
            if pawn.zone == "track" and pawn.track_position is not None:
                if normalize_track_position(pawn.track_position) == normalized:
                    _send_pawn_to_start(pawn)


def _resolve_slide_for_pawn(
    state: SorryGameState,
    player_state: SorryPlayerState,
    pawn: SorryPawnState,
    rules: SorryRulesProfile,
) -> None:
    if pawn.zone != "track" or pawn.track_position is None:
        return

    start = normalize_track_position(pawn.track_position)
    side_offset = start % 15
    slide_steps = _SLIDE_START_TO_STEPS_BY_OFFSET.get(side_offset)
    if slide_steps is None:
        return

    slide_owner_seat = start // 15
    same_color_slide = slide_owner_seat == player_state.seat_index

    policy_id = rules.slide_policy_id()
    if policy_id == "a5065_core":
        should_slide = same_color_slide
    else:
        # Classic and unknown policy ids keep classic behavior.
        should_slide = not same_color_slide
    if not should_slide:
        return

    end = normalize_track_position(start + slide_steps)
    slide_positions = {
        normalize_track_position(start + step)
        for step in range(slide_steps + 1)
    }
    for other_state in state.player_states.values():
        for other_pawn in other_state.pawns:
            if other_pawn is pawn:
                continue
            if other_pawn.zone != "track" or other_pawn.track_position is None:
                continue
            if normalize_track_position(other_pawn.track_position) in slide_positions:
                _send_pawn_to_start(other_pawn)

    pawn.track_position = end


def apply_move(
    state: SorryGameState,
    player_state: SorryPlayerState,
    move: SorryMove,
    rules: SorryRulesProfile,
) -> None:
    """Apply a legal move to mutable game state."""

    if move.move_type == "start":
        pawn = _get_pawn(player_state, move.pawn_index)
        if pawn is None or pawn.zone != "start":
            raise ValueError("Invalid start move pawn")
        destination = PawnDestination(
            zone="track",
            track_position=player_state.start_track,
        )
        if not _is_destination_legal_for_player(
            player_state,
            destination,
            ignore_pawn_indexes={pawn.pawn_index},
        ):
            raise ValueError("Start square blocked by own pawn")
        _apply_destination(pawn, destination)
        _capture_opponents_on_track(state, player_state, pawn.track_position)
        _resolve_slide_for_pawn(state, player_state, pawn, rules)
        return

    if move.move_type in {"forward", "sorry_fallback_forward"}:
        pawn = _get_pawn(player_state, move.pawn_index)
        if pawn is None or move.steps is None:
            raise ValueError("Invalid forward move payload")
        destination = _compute_forward_destination(player_state, pawn, move.steps)
        if destination is None:
            raise ValueError("Forward move is no longer legal")
        if not _is_destination_legal_for_player(
            player_state,
            destination,
            ignore_pawn_indexes={pawn.pawn_index},
        ):
            raise ValueError("Forward destination blocked by own pawn")
        _apply_destination(pawn, destination)
        if pawn.zone == "track":
            _capture_opponents_on_track(state, player_state, pawn.track_position)
            _resolve_slide_for_pawn(state, player_state, pawn, rules)
        return

    if move.move_type == "backward":
        pawn = _get_pawn(player_state, move.pawn_index)
        if pawn is None or move.steps is None:
            raise ValueError("Invalid backward move payload")
        destination = _compute_backward_destination(pawn, move.steps)
        if destination is None:
            raise ValueError("Backward move is no longer legal")
        if not _is_destination_legal_for_player(
            player_state,
            destination,
            ignore_pawn_indexes={pawn.pawn_index},
        ):
            raise ValueError("Backward destination blocked by own pawn")
        _apply_destination(pawn, destination)
        _capture_opponents_on_track(state, player_state, pawn.track_position)
        _resolve_slide_for_pawn(state, player_state, pawn, rules)
        return

    if move.move_type == "swap":
        pawn = _get_pawn(player_state, move.pawn_index)
        opponent_state = _player_by_id(state, move.target_player_id)
        opponent_pawn = (
            _get_pawn(opponent_state, move.target_pawn_index)
            if opponent_state is not None
            else None
        )
        if (
            pawn is None
            or opponent_pawn is None
            or pawn.zone != "track"
            or opponent_pawn.zone != "track"
            or pawn.track_position is None
            or opponent_pawn.track_position is None
        ):
            raise ValueError("Invalid swap move")
        pawn.track_position, opponent_pawn.track_position = (
            opponent_pawn.track_position,
            pawn.track_position,
        )
        _resolve_slide_for_pawn(state, player_state, pawn, rules)
        return

    if move.move_type == "sorry":
        pawn = _get_pawn(player_state, move.pawn_index)
        opponent_state = _player_by_id(state, move.target_player_id)
        opponent_pawn = (
            _get_pawn(opponent_state, move.target_pawn_index)
            if opponent_state is not None
            else None
        )
        if (
            pawn is None
            or opponent_pawn is None
            or pawn.zone != "start"
            or opponent_pawn.zone != "track"
            or opponent_pawn.track_position is None
        ):
            raise ValueError("Invalid Sorry move")
        destination = PawnDestination(
            zone="track",
            track_position=opponent_pawn.track_position,
        )
        if not _is_destination_legal_for_player(
            player_state,
            destination,
            ignore_pawn_indexes={pawn.pawn_index},
        ):
            raise ValueError("Sorry destination blocked by own pawn")
        _send_pawn_to_start(opponent_pawn)
        _apply_destination(pawn, destination)
        _capture_opponents_on_track(state, player_state, pawn.track_position)
        _resolve_slide_for_pawn(state, player_state, pawn, rules)
        return

    if move.move_type == "split7":
        primary = _get_pawn(player_state, move.pawn_index)
        secondary = _get_pawn(player_state, move.secondary_pawn_index)
        if (
            primary is None
            or secondary is None
            or move.steps is None
            or move.secondary_steps is None
            or primary.pawn_index == secondary.pawn_index
        ):
            raise ValueError("Invalid split-7 payload")

        first_destination = _compute_forward_destination(
            player_state,
            primary,
            move.steps,
        )
        second_destination = _compute_forward_destination(
            player_state,
            secondary,
            move.secondary_steps,
        )
        if first_destination is None or second_destination is None:
            raise ValueError("Split-7 move is no longer legal")

        ignore = {primary.pawn_index, secondary.pawn_index}
        if not _is_destination_legal_for_player(
            player_state,
            first_destination,
            ignore_pawn_indexes=ignore,
        ):
            raise ValueError("Primary split destination blocked")
        if not _is_destination_legal_for_player(
            player_state,
            second_destination,
            ignore_pawn_indexes=ignore,
        ):
            raise ValueError("Secondary split destination blocked")
        if (
            first_destination.zone == second_destination.zone == "track"
            and first_destination.track_position == second_destination.track_position
        ):
            raise ValueError("Split-7 cannot stack on same track square")
        if (
            first_destination.zone == second_destination.zone == "home_path"
            and first_destination.home_steps == second_destination.home_steps
        ):
            raise ValueError("Split-7 cannot stack on same home-path square")

        _apply_destination(primary, first_destination)
        if primary.zone == "track":
            _capture_opponents_on_track(state, player_state, primary.track_position)
            _resolve_slide_for_pawn(state, player_state, primary, rules)
        _apply_destination(secondary, second_destination)
        if secondary.zone == "track":
            _capture_opponents_on_track(state, player_state, secondary.track_position)
            _resolve_slide_for_pawn(state, player_state, secondary, rules)
        return

    raise ValueError(f"Unsupported move type: {move.move_type}")
