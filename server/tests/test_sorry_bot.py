"""Bot behavior tests for Sorry."""

from server.core.users.bot import Bot
from server.games.sorry.bot import choose_move
from server.games.sorry.game import SorryGame, SorryOptions
from server.games.sorry.moves import generate_legal_moves
from server.games.sorry.rules import A5065CoreRules, Classic00390Rules
from server.games.sorry.state import SAFETY_LENGTH, build_initial_game_state


def _set_track(pawn, position: int) -> None:
    pawn.zone = "track"
    pawn.track_position = position
    pawn.home_steps = 0


def _set_home(pawn) -> None:
    pawn.zone = "home"
    pawn.track_position = None
    pawn.home_steps = SAFETY_LENGTH + 1


def _set_home_path(pawn, steps: int) -> None:
    pawn.zone = "home_path"
    pawn.track_position = None
    pawn.home_steps = steps


def test_bot_prefers_winning_move() -> None:
    state = build_initial_game_state(["p1", "p2"], shuffle_deck=False)
    player_state = state.player_states["p1"]

    _set_home_path(player_state.pawns[0], SAFETY_LENGTH)
    _set_track(player_state.pawns[1], 5)
    _set_home(player_state.pawns[2])
    _set_home(player_state.pawns[3])

    moves = generate_legal_moves(state, player_state, "1", Classic00390Rules())
    choice = choose_move(state, player_state, moves, Classic00390Rules())

    assert choice is not None
    assert choice.move_type == "forward"
    assert choice.pawn_index == 1
    assert choice.steps == 1


def test_bot_prefers_capture_over_plain_progress() -> None:
    state = build_initial_game_state(["p1", "p2"], shuffle_deck=False)
    p1 = state.player_states["p1"]
    p2 = state.player_states["p2"]

    _set_track(p1.pawns[0], 10)  # non-capture move with +3
    _set_track(p1.pawns[1], 0)   # capture move with +3
    _set_track(p2.pawns[0], 3)

    moves = generate_legal_moves(state, p1, "3", Classic00390Rules())
    choice = choose_move(state, p1, moves, Classic00390Rules())

    assert choice is not None
    assert choice.move_type == "forward"
    assert choice.pawn_index == 2
    assert choice.steps == 3


def test_bot_prefers_leaving_start_when_other_move_is_plain() -> None:
    state = build_initial_game_state(["p1", "p2"], shuffle_deck=False)
    p1 = state.player_states["p1"]

    _set_track(p1.pawns[0], 10)
    # keep pawn 2 in start for leave-start option

    moves = generate_legal_moves(state, p1, "1", Classic00390Rules())
    choice = choose_move(state, p1, moves, Classic00390Rules())

    assert choice is not None
    assert choice.move_type == "start"
    assert choice.pawn_index == 2


def test_a5065_bot_handles_sorry_fallback_move_type() -> None:
    state = build_initial_game_state(["p1", "p2"], pawns_per_player=3, shuffle_deck=False)
    p1 = state.player_states["p1"]
    _set_track(p1.pawns[0], 0)

    moves = generate_legal_moves(state, p1, "sorry", A5065CoreRules())
    choice = choose_move(state, p1, moves, A5065CoreRules())

    assert choice is not None
    assert choice.move_type == "sorry_fallback_forward"
    assert choice.pawn_index == 1
    assert choice.steps == 4


def test_bot_on_tick_uses_heuristic_not_first_slot() -> None:
    game = SorryGame(
        options=SorryOptions(
            auto_apply_single_move=False,
            faster_setup_one_pawn_out=False,
        )
    )
    bot1 = Bot("Bot1")
    bot2 = Bot("Bot2")
    game.add_player("Bot1", bot1)
    game.add_player("Bot2", bot2)
    game.on_start()

    current = game.current_player
    assert current is not None
    assert current.id == bot1.uuid

    p1 = game.game_state.player_states[bot1.uuid]
    p2 = game.game_state.player_states[bot2.uuid]

    # Create two forward-3 moves where slot 1 is non-capture (pawn 1),
    # but heuristic should choose capture with pawn 2.
    _set_track(p1.pawns[0], 10)  # action_id forward3_p1
    _set_track(p1.pawns[1], 0)   # action_id forward3_p2 (capture)
    _set_track(p2.pawns[0], 3)

    game.game_state.turn_phase = "choose_move"
    game.game_state.current_card = "3"

    game.on_tick()

    assert p1.pawns[1].track_position == 3
    assert p2.pawns[0].zone == "start"


def test_bot_can_finish_turn_cycle_to_win() -> None:
    game = SorryGame(
        options=SorryOptions(
            auto_apply_single_move=True,
            faster_setup_one_pawn_out=False,
        )
    )
    bot1 = Bot("Bot1")
    bot2 = Bot("Bot2")
    game.add_player("Bot1", bot1)
    game.add_player("Bot2", bot2)
    game.on_start()

    current = game.current_player
    assert current is not None
    assert current.id == bot1.uuid

    p1 = game.game_state.player_states[bot1.uuid]
    _set_home_path(p1.pawns[0], SAFETY_LENGTH)
    _set_home(p1.pawns[1])
    _set_home(p1.pawns[2])
    _set_home(p1.pawns[3])
    game._sync_player_counts()

    game.game_state.draw_pile = ["1"]
    game.on_tick()

    assert game.status == "finished"
    assert game.game_active is False


def test_a5065_bot_can_finish_turn_cycle_to_win() -> None:
    game = SorryGame(
        options=SorryOptions(
            rules_profile="a5065_core",
            auto_apply_single_move=True,
            faster_setup_one_pawn_out=False,
        )
    )
    bot1 = Bot("Bot1")
    bot2 = Bot("Bot2")
    game.add_player("Bot1", bot1)
    game.add_player("Bot2", bot2)
    game.on_start()

    current = game.current_player
    assert current is not None
    assert current.id == bot1.uuid

    p1 = game.game_state.player_states[bot1.uuid]
    _set_home_path(p1.pawns[0], SAFETY_LENGTH)
    _set_home(p1.pawns[1])
    _set_home(p1.pawns[2])
    game._sync_player_counts()

    game.game_state.draw_pile = ["1"]
    game.on_tick()

    assert game.status == "finished"
    assert game.game_active is False
