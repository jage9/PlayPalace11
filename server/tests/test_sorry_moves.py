"""Unit tests for Sorry move generation and application."""

from server.games.sorry.moves import (
    SorryMove,
    apply_move,
    generate_legal_moves,
)
from server.games.sorry.rules import A5065CoreRules, Classic00390Rules
from server.games.sorry.state import (
    SAFETY_LENGTH,
    build_initial_game_state,
    normalize_track_position,
)


def _set_track(pawn, position: int) -> None:
    pawn.zone = "track"
    pawn.track_position = normalize_track_position(position)
    pawn.home_steps = 0


def _set_home_path(pawn, steps: int) -> None:
    pawn.zone = "home_path"
    pawn.track_position = None
    pawn.home_steps = steps


def _find_move(
    moves: list[SorryMove],
    *,
    move_type: str,
    pawn_index: int | None = None,
    steps: int | None = None,
) -> SorryMove:
    for move in moves:
        if move.move_type != move_type:
            continue
        if pawn_index is not None and move.pawn_index != pawn_index:
            continue
        if steps is not None and move.steps != steps:
            continue
        return move
    raise AssertionError(
        f"Could not find move type={move_type}, pawn_index={pawn_index}, steps={steps}"
    )


def test_card_one_allows_start_moves() -> None:
    state = build_initial_game_state(["p1", "p2"], shuffle_deck=False)
    p1 = state.player_states["p1"]
    moves = generate_legal_moves(state, p1, "1", Classic00390Rules())
    start_moves = [move for move in moves if move.move_type == "start"]
    assert len(start_moves) == 4


def test_start_move_blocked_by_own_pawn_on_entry() -> None:
    state = build_initial_game_state(["p1", "p2"], shuffle_deck=False)
    p1 = state.player_states["p1"]
    _set_track(p1.pawns[0], p1.start_track)
    moves = generate_legal_moves(state, p1, "1", Classic00390Rules())
    assert not any(move.move_type == "start" for move in moves)


def test_card_ten_generates_forward_and_backward_options() -> None:
    state = build_initial_game_state(["p1", "p2"], shuffle_deck=False)
    p1 = state.player_states["p1"]
    _set_track(p1.pawns[0], 10)
    moves = generate_legal_moves(state, p1, "10", Classic00390Rules())
    assert any(move.move_type == "forward" and move.steps == 10 for move in moves)
    assert any(move.move_type == "backward" and move.steps == 1 for move in moves)


def test_card_eleven_generates_swap_when_targets_exist() -> None:
    state = build_initial_game_state(["p1", "p2"], shuffle_deck=False)
    p1 = state.player_states["p1"]
    p2 = state.player_states["p2"]
    _set_track(p1.pawns[0], 5)
    _set_track(p2.pawns[0], 20)

    moves = generate_legal_moves(state, p1, "11", Classic00390Rules())
    assert any(move.move_type == "swap" for move in moves)
    assert any(move.move_type == "forward" and move.steps == 11 for move in moves)


def test_a5065_card_three_allows_start_moves() -> None:
    state = build_initial_game_state(["p1", "p2"], pawns_per_player=3, shuffle_deck=False)
    p1 = state.player_states["p1"]

    moves = generate_legal_moves(state, p1, "3", A5065CoreRules())
    start_moves = [move for move in moves if move.move_type == "start"]
    assert len(start_moves) == 3


def test_sorry_card_moves_from_start_and_captures_target() -> None:
    state = build_initial_game_state(["p1", "p2"], shuffle_deck=False)
    p1 = state.player_states["p1"]
    p2 = state.player_states["p2"]
    _set_track(p2.pawns[0], 22)

    moves = generate_legal_moves(state, p1, "sorry", Classic00390Rules())
    move = _find_move(moves, move_type="sorry", pawn_index=1)
    apply_move(state, p1, move, Classic00390Rules())

    assert p1.pawns[0].zone == "track"
    assert p1.pawns[0].track_position == 22
    assert p2.pawns[0].zone == "start"
    assert p2.pawns[0].track_position is None


def test_a5065_sorry_card_uses_forward_four_when_no_replace_target() -> None:
    state = build_initial_game_state(["p1", "p2"], pawns_per_player=3, shuffle_deck=False)
    p1 = state.player_states["p1"]
    _set_track(p1.pawns[0], 0)

    moves = generate_legal_moves(state, p1, "sorry", A5065CoreRules())
    assert not any(move.move_type == "sorry" for move in moves)

    move = _find_move(
        moves,
        move_type="sorry_fallback_forward",
        pawn_index=1,
        steps=4,
    )
    apply_move(state, p1, move, A5065CoreRules())
    assert p1.pawns[0].track_position == 4


def test_a5065_sorry_card_does_not_add_fallback_when_replace_exists() -> None:
    state = build_initial_game_state(["p1", "p2"], pawns_per_player=3, shuffle_deck=False)
    p1 = state.player_states["p1"]
    p2 = state.player_states["p2"]
    _set_track(p2.pawns[0], 22)

    moves = generate_legal_moves(state, p1, "sorry", A5065CoreRules())
    assert any(move.move_type == "sorry" for move in moves)
    assert not any(move.move_type == "sorry_fallback_forward" for move in moves)


def test_classic_slide_triggers_on_other_color_and_bumps_path() -> None:
    state = build_initial_game_state(["p1", "p2"], shuffle_deck=False)
    p1 = state.player_states["p1"]
    p2 = state.player_states["p2"]
    _set_track(p1.pawns[0], 19)
    _set_track(p2.pawns[0], 20)
    _set_track(p2.pawns[1], 22)
    _set_track(p2.pawns[2], 24)

    moves = generate_legal_moves(state, p1, "1", Classic00390Rules())
    move = _find_move(moves, move_type="forward", pawn_index=1, steps=1)
    apply_move(state, p1, move, Classic00390Rules())

    assert p1.pawns[0].zone == "track"
    assert p1.pawns[0].track_position == 24
    assert p2.pawns[0].zone == "start"
    assert p2.pawns[1].zone == "start"
    assert p2.pawns[2].zone == "start"


def test_classic_slide_does_not_trigger_on_own_color_start() -> None:
    state = build_initial_game_state(["p1", "p2"], shuffle_deck=False)
    p1 = state.player_states["p1"]
    _set_track(p1.pawns[0], 4)

    moves = generate_legal_moves(state, p1, "1", Classic00390Rules())
    move = _find_move(moves, move_type="forward", pawn_index=1, steps=1)
    apply_move(state, p1, move, Classic00390Rules())

    assert p1.pawns[0].track_position == 5


def test_a5065_slide_triggers_on_own_color_and_bumps_path() -> None:
    state = build_initial_game_state(["p1", "p2"], pawns_per_player=3, shuffle_deck=False)
    p1 = state.player_states["p1"]
    p2 = state.player_states["p2"]
    _set_track(p1.pawns[0], 4)
    _set_track(p1.pawns[1], 9)
    _set_track(p2.pawns[0], 7)

    moves = generate_legal_moves(state, p1, "1", A5065CoreRules())
    move = _find_move(moves, move_type="forward", pawn_index=1, steps=1)
    apply_move(state, p1, move, A5065CoreRules())

    assert p1.pawns[0].zone == "track"
    assert p1.pawns[0].track_position == 9
    assert p1.pawns[1].zone == "start"
    assert p2.pawns[0].zone == "start"


def test_a5065_slide_does_not_trigger_on_other_color_start() -> None:
    state = build_initial_game_state(["p1", "p2"], pawns_per_player=3, shuffle_deck=False)
    p1 = state.player_states["p1"]
    p2 = state.player_states["p2"]
    _set_track(p1.pawns[0], 19)
    _set_track(p2.pawns[0], 22)

    moves = generate_legal_moves(state, p1, "1", A5065CoreRules())
    move = _find_move(moves, move_type="forward", pawn_index=1, steps=1)
    apply_move(state, p1, move, A5065CoreRules())

    assert p1.pawns[0].track_position == 20
    assert p2.pawns[0].zone == "track"
    assert p2.pawns[0].track_position == 22


def test_classic_swap_into_other_color_slide_triggers_slide() -> None:
    state = build_initial_game_state(["p1", "p2"], shuffle_deck=False)
    p1 = state.player_states["p1"]
    p2 = state.player_states["p2"]
    _set_track(p1.pawns[0], 0)
    _set_track(p1.pawns[1], 22)
    _set_track(p2.pawns[0], 20)

    moves = generate_legal_moves(state, p1, "11", Classic00390Rules())
    swap_move = _find_move(moves, move_type="swap", pawn_index=1)
    apply_move(state, p1, swap_move, Classic00390Rules())

    assert p1.pawns[0].track_position == 24
    assert p1.pawns[1].zone == "start"
    assert p2.pawns[0].track_position == 0


def test_forward_move_captures_opponent_on_landing_square() -> None:
    state = build_initial_game_state(["p1", "p2"], shuffle_deck=False)
    p1 = state.player_states["p1"]
    p2 = state.player_states["p2"]
    _set_track(p1.pawns[0], 0)
    _set_track(p2.pawns[0], 3)

    moves = generate_legal_moves(state, p1, "3", Classic00390Rules())
    move = _find_move(moves, move_type="forward", pawn_index=1, steps=3)
    apply_move(state, p1, move, Classic00390Rules())

    assert p1.pawns[0].track_position == 3
    assert p2.pawns[0].zone == "start"


def test_swap_move_exchanges_track_positions() -> None:
    state = build_initial_game_state(["p1", "p2"], shuffle_deck=False)
    p1 = state.player_states["p1"]
    p2 = state.player_states["p2"]
    _set_track(p1.pawns[0], 1)
    _set_track(p2.pawns[0], 2)

    moves = generate_legal_moves(state, p1, "11", Classic00390Rules())
    swap_move = _find_move(moves, move_type="swap", pawn_index=1)
    apply_move(state, p1, swap_move, Classic00390Rules())

    assert p1.pawns[0].track_position == 2
    assert p2.pawns[0].track_position == 1


def test_card_seven_generates_split_moves() -> None:
    state = build_initial_game_state(["p1", "p2"], shuffle_deck=False)
    p1 = state.player_states["p1"]
    _set_track(p1.pawns[0], 0)
    _set_track(p1.pawns[1], 5)

    moves = generate_legal_moves(state, p1, "7", Classic00390Rules())
    split_moves = [move for move in moves if move.move_type == "split7"]
    assert split_moves
    assert any(
        move.steps is not None
        and move.secondary_steps is not None
        and move.steps + move.secondary_steps == 7
        for move in split_moves
    )


def test_split_seven_apply_moves_both_pawns() -> None:
    state = build_initial_game_state(["p1", "p2"], shuffle_deck=False)
    p1 = state.player_states["p1"]
    _set_track(p1.pawns[0], 0)
    _set_track(p1.pawns[1], 5)

    moves = generate_legal_moves(state, p1, "7", Classic00390Rules())
    move = next(move for move in moves if move.move_type == "split7")

    before_a = p1.pawns[0].track_position
    before_b = p1.pawns[1].track_position
    apply_move(state, p1, move, Classic00390Rules())

    assert p1.pawns[0].track_position != before_a
    assert p1.pawns[1].track_position != before_b


def test_forward_enters_home_path_and_requires_exact_home_count() -> None:
    state = build_initial_game_state(["p1", "p2"], shuffle_deck=False)
    p1 = state.player_states["p1"]
    _set_track(p1.pawns[0], p1.home_entry_track)

    one_moves = generate_legal_moves(state, p1, "1", Classic00390Rules())
    one_move = _find_move(one_moves, move_type="forward", pawn_index=1, steps=1)
    apply_move(state, p1, one_move, Classic00390Rules())
    assert p1.pawns[0].zone == "home_path"
    assert p1.pawns[0].home_steps == 1

    _set_home_path(p1.pawns[0], SAFETY_LENGTH)
    can_finish = generate_legal_moves(state, p1, "1", Classic00390Rules())
    finish_move = _find_move(can_finish, move_type="forward", pawn_index=1, steps=1)
    apply_move(state, p1, finish_move, Classic00390Rules())
    assert p1.pawns[0].zone == "home"

    _set_home_path(p1.pawns[0], SAFETY_LENGTH)
    cannot_overshoot = generate_legal_moves(state, p1, "2", Classic00390Rules())
    assert not any(
        move.move_type == "forward" and move.pawn_index == 1
        for move in cannot_overshoot
    )
