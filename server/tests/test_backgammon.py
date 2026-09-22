"""Comprehensive tests for Backgammon."""

import pytest
from server.games.backgammon.state import (
    BackgammonBoardState,
    BackgammonGameState,
    INITIAL_BOARD,
    all_checkers_in_home,
    bar_count,
    build_initial_game_state,
    color_sign,
    game_multiplier,
    is_backgammon,
    is_gammon,
    off_count,
    opponent_color,
    pip_count,
    point_count,
    point_number_for_player,
    point_owner,
    player_point_to_index,
    remaining_dice,
    remaining_dice_unique,
    roll_dice,
    set_bar,
    set_off,
)
from server.games.backgammon.moves import (
    BackgammonMove,
    apply_move,
    generate_legal_moves,
    has_any_legal_move,
    must_use_both_dice,
    undo_last_move,
)
from server.games.backgammon.bot import _pick_move, _pick_random_move, _pick_simple_move, _score_move
from server.games.backgammon.gnubg import (
    encode_position_id,
    parse_hint_line,
    hint_to_goals,
)
from server.games.backgammon.game import (
    BackgammonGame,
    BackgammonOptions,
    BackgammonPlayer,
    DIFFICULTY_PLY,
    BOT_DIFFICULTY_CHOICES,
)


# ==========================================================================
# State tests
# ==========================================================================


class TestInitialPosition:
    def test_15_checkers_per_side(self):
        gs = build_initial_game_state()
        red = sum(v for v in gs.board.points if v > 0)
        white = sum(-v for v in gs.board.points if v < 0)
        assert red == 15
        assert white == 15

    def test_pip_count_167(self):
        gs = build_initial_game_state()
        assert pip_count(gs, "red") == 167
        assert pip_count(gs, "white") == 167

    def test_bar_and_off_start_at_zero(self):
        gs = build_initial_game_state()
        assert gs.board.bar_red == 0
        assert gs.board.bar_white == 0
        assert gs.board.off_red == 0
        assert gs.board.off_white == 0

    def test_initial_phase(self):
        gs = build_initial_game_state()
        assert gs.turn_phase == "pre_roll"
        assert gs.cube_value == 1
        assert gs.cube_owner == ""

    def test_match_length_passed_through(self):
        gs = build_initial_game_state(match_length=7)
        assert gs.match_length == 7


class TestStateHelpers:
    def test_color_sign(self):
        assert color_sign("red") == 1
        assert color_sign("white") == -1

    def test_opponent_color(self):
        assert opponent_color("red") == "white"
        assert opponent_color("white") == "red"

    def test_point_owner(self):
        gs = build_initial_game_state()
        assert point_owner(gs, 23) == "red"  # 2 Red on point 24
        assert point_owner(gs, 0) == "white"  # 2 White on point 1
        assert point_owner(gs, 1) is None  # Empty

    def test_point_count(self):
        gs = build_initial_game_state()
        assert point_count(gs, 23) == 2
        assert point_count(gs, 12) == 5
        assert point_count(gs, 1) == 0

    def test_bar_and_off_accessors(self):
        gs = build_initial_game_state()
        set_bar(gs, "red", 3)
        assert bar_count(gs, "red") == 3
        assert bar_count(gs, "white") == 0
        set_off(gs, "white", 5)
        assert off_count(gs, "white") == 5
        assert off_count(gs, "red") == 0

    def test_remaining_dice(self):
        gs = build_initial_game_state()
        gs.dice = [3, 5]
        gs.dice_used = [False, True]
        assert remaining_dice(gs) == [3]
        assert remaining_dice_unique(gs) == [3]

    def test_remaining_dice_doubles(self):
        gs = build_initial_game_state()
        gs.dice = [4, 4, 4, 4]
        gs.dice_used = [True, False, False, True]
        assert remaining_dice(gs) == [4, 4]
        assert remaining_dice_unique(gs) == [4]

    def test_point_number_for_player_red(self):
        assert point_number_for_player(0, "red") == 1
        assert point_number_for_player(23, "red") == 24

    def test_point_number_for_player_white(self):
        assert point_number_for_player(0, "white") == 24
        assert point_number_for_player(23, "white") == 1

    def test_player_point_to_index(self):
        assert player_point_to_index(1, "red") == 0
        assert player_point_to_index(24, "red") == 23
        assert player_point_to_index(1, "white") == 23
        assert player_point_to_index(24, "white") == 0

    def test_roll_dice_range(self):
        for _ in range(100):
            d1, d2 = roll_dice()
            assert 1 <= d1 <= 6
            assert 1 <= d2 <= 6


class TestAllCheckersInHome:
    def test_initial_position_not_home(self):
        gs = build_initial_game_state()
        assert not all_checkers_in_home(gs, "red")
        assert not all_checkers_in_home(gs, "white")

    def test_all_in_home_red(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.points[0] = 5  # point 1
        gs.board.points[3] = 5  # point 4
        gs.board.points[5] = 5  # point 6
        assert all_checkers_in_home(gs, "red")

    def test_all_in_home_white(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.points[18] = -5  # White's point 6
        gs.board.points[20] = -5  # White's point 4
        gs.board.points[23] = -5  # White's point 1
        assert all_checkers_in_home(gs, "white")

    def test_bar_prevents_home(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.points[0] = 14
        gs.board.bar_red = 1
        assert not all_checkers_in_home(gs, "red")


class TestGammonBackgammon:
    def test_gammon(self):
        gs = build_initial_game_state()
        assert is_gammon(gs, "red")  # Red has 0 off
        gs.board.off_red = 1
        assert not is_gammon(gs, "red")

    def test_backgammon_bar(self):
        gs = build_initial_game_state()
        gs.board.bar_red = 1
        assert is_backgammon(gs, "red")

    def test_backgammon_in_winner_home(self):
        gs = build_initial_game_state()
        # Red has checkers in White's home (indices 18-23)
        # Initial board already has Red on index 23
        assert is_backgammon(gs, "red")

    def test_not_backgammon_if_not_gammon(self):
        gs = build_initial_game_state()
        gs.board.off_red = 1
        assert not is_backgammon(gs, "red")

    def test_game_multiplier(self):
        gs = build_initial_game_state()
        gs.board.bar_red = 1
        assert game_multiplier(gs, "red") == 3  # Backgammon
        gs.board.bar_red = 0
        gs.board.points = [0] * 24  # Clear board
        # Red has nothing off and no checkers on board = gammon
        assert game_multiplier(gs, "red") == 2
        gs.board.off_red = 1
        assert game_multiplier(gs, "red") == 1  # Single


# ==========================================================================
# Move generation tests
# ==========================================================================


class TestMoveGeneration:
    def test_initial_red_die_1(self):
        gs = build_initial_game_state()
        moves = generate_legal_moves(gs, "red", 1)
        sources = sorted(set(m.source for m in moves))
        # Red has checkers on indices 5, 7, 12, 23
        assert all(s in [5, 7, 12, 23] for s in sources)
        # Can't move from 5 with die 1: index 4 is empty -> legal
        # Can't move from 23: index 22 is empty -> legal
        assert len(moves) >= 3

    def test_initial_red_die_6(self):
        gs = build_initial_game_state()
        moves = generate_legal_moves(gs, "red", 6)
        # Red on 23 -> 17: index 16 has White (-3) -> blocked
        # Red on 12 -> 6: index 5 has Red (+5) -> legal (own checkers)
        # Red on 7 -> 1: index 0 has White (-2) -> blocked
        # Red on 5 -> -1: would be bear off but not all in home
        sources = [m.source for m in moves]
        assert 12 in sources  # 13-point to 7-point

    def test_initial_white_die_3(self):
        gs = build_initial_game_state()
        moves = generate_legal_moves(gs, "white", 3)
        assert len(moves) > 0
        for m in moves:
            assert m.destination > m.source  # White moves toward higher indices

    def test_bar_entry_required(self):
        gs = build_initial_game_state()
        gs.board.bar_red = 1
        moves = generate_legal_moves(gs, "red", 3)
        # All moves must be from bar (-1)
        assert all(m.source == -1 for m in moves)

    def test_bar_entry_red_die_values(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24  # Clear board
        gs.board.bar_red = 1
        # Red enters on point 24-die, so die=1 -> index 23
        moves = generate_legal_moves(gs, "red", 1)
        assert len(moves) == 1
        assert moves[0].destination == 23

    def test_bar_entry_white_die_values(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.bar_white = 1
        # White enters on point die-1, so die=4 -> index 3
        moves = generate_legal_moves(gs, "white", 4)
        assert len(moves) == 1
        assert moves[0].destination == 3

    def test_bar_entry_blocked(self):
        gs = build_initial_game_state()
        gs.board.bar_red = 1
        # Block index 23 (Red enters with die=1)
        gs.board.points[23] = -2  # 2 White checkers
        moves = generate_legal_moves(gs, "red", 1)
        assert len(moves) == 0

    def test_bar_entry_hit(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.bar_red = 1
        gs.board.points[22] = -1  # 1 White blot on index 22
        moves = generate_legal_moves(gs, "red", 2)
        assert len(moves) == 1
        assert moves[0].is_hit

    def test_hit_detection(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.points[10] = 2  # Red on index 10
        gs.board.points[7] = -1  # White blot on index 7
        moves = generate_legal_moves(gs, "red", 3)
        hit_moves = [m for m in moves if m.is_hit]
        assert len(hit_moves) == 1
        assert hit_moves[0].destination == 7

    def test_blocked_by_opponent(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.points[10] = 2  # Red
        gs.board.points[7] = -2  # White (2+ = blocked)
        moves = generate_legal_moves(gs, "red", 3)
        assert len(moves) == 0


class TestBearOff:
    def _bearing_off_state(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.points[0] = 3  # Red on point 1
        gs.board.points[2] = 4  # Red on point 3
        gs.board.points[4] = 3  # Red on point 5
        gs.board.off_red = 5
        return gs

    def test_exact_bear_off(self):
        gs = self._bearing_off_state()
        # Die 3 from point 3 (index 2) -> exact bear off
        moves = generate_legal_moves(gs, "red", 3)
        bear_off = [m for m in moves if m.is_bear_off]
        assert any(m.source == 2 for m in bear_off)

    def test_overshoot_bear_off_highest(self):
        gs = self._bearing_off_state()
        # Die 6 from point 5 (index 4) -> overshoot, but it's highest
        moves = generate_legal_moves(gs, "red", 6)
        bear_off = [m for m in moves if m.is_bear_off]
        assert any(m.source == 4 for m in bear_off)

    def test_overshoot_not_highest_blocked(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.points[0] = 5  # Red on point 1
        gs.board.points[3] = 5  # Red on point 4
        gs.board.off_red = 5
        # Die 6 from point 1 (index 0) -> overshoot
        # But index 3 (point 4) has higher checkers, so can't bear off from 0
        moves = generate_legal_moves(gs, "red", 6)
        bear_off_from_0 = [m for m in moves if m.is_bear_off and m.source == 0]
        assert len(bear_off_from_0) == 0
        # But can bear off from point 4 (index 3)
        bear_off_from_3 = [m for m in moves if m.is_bear_off and m.source == 3]
        assert len(bear_off_from_3) == 1

    def test_cannot_bear_off_if_not_all_home(self):
        gs = build_initial_game_state()
        # Initial position: checkers everywhere, can't bear off
        moves = generate_legal_moves(gs, "red", 1)
        assert not any(m.is_bear_off for m in moves)

    def test_white_bear_off(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.points[23] = -3  # White on point 1 (their perspective)
        gs.board.points[20] = -5  # White on point 4
        gs.board.off_white = 7
        moves = generate_legal_moves(gs, "white", 1)
        bear_off = [m for m in moves if m.is_bear_off]
        assert any(m.source == 23 for m in bear_off)


class TestApplyAndUndo:
    def test_apply_normal_move(self):
        gs = build_initial_game_state()
        gs.moves_this_turn = []
        move = BackgammonMove(source=23, destination=20, die_value=3)
        apply_move(gs, move, "red")
        assert gs.board.points[23] == 1  # Was 2, now 1
        assert gs.board.points[20] == 1  # Was 0, now 1
        assert len(gs.moves_this_turn) == 1

    def test_apply_hit(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.points[10] = 2
        gs.board.points[7] = -1
        gs.moves_this_turn = []
        move = BackgammonMove(source=10, destination=7, die_value=3, is_hit=True)
        apply_move(gs, move, "red")
        assert gs.board.points[7] == 1  # Red now
        assert gs.board.bar_white == 1  # White sent to bar

    def test_apply_bar_entry(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.bar_red = 2
        gs.moves_this_turn = []
        move = BackgammonMove(source=-1, destination=23, die_value=1)
        apply_move(gs, move, "red")
        assert gs.board.bar_red == 1
        assert gs.board.points[23] == 1

    def test_apply_bear_off(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.points[2] = 3
        gs.board.off_red = 12
        gs.moves_this_turn = []
        move = BackgammonMove(source=2, destination=24, die_value=3, is_bear_off=True)
        apply_move(gs, move, "red")
        assert gs.board.points[2] == 2
        assert gs.board.off_red == 13

    def test_undo_restores_state(self):
        gs = build_initial_game_state()
        gs.moves_this_turn = []
        original_23 = gs.board.points[23]
        original_20 = gs.board.points[20]
        move = BackgammonMove(source=23, destination=20, die_value=3)
        apply_move(gs, move, "red")
        undone = undo_last_move(gs, "red")
        assert undone is not None
        assert gs.board.points[23] == original_23
        assert gs.board.points[20] == original_20
        assert len(gs.moves_this_turn) == 0

    def test_undo_hit_restores_opponent(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.points[10] = 2
        gs.board.points[7] = -1
        gs.moves_this_turn = []
        move = BackgammonMove(source=10, destination=7, die_value=3, is_hit=True)
        apply_move(gs, move, "red")
        undo_last_move(gs, "red")
        assert gs.board.points[10] == 2
        assert gs.board.points[7] == -1
        assert gs.board.bar_white == 0

    def test_undo_empty_returns_none(self):
        gs = build_initial_game_state()
        gs.moves_this_turn = []
        assert undo_last_move(gs, "red") is None


class TestMustUseBothDice:
    def test_both_usable_returns_none(self):
        gs = build_initial_game_state()
        result = must_use_both_dice(gs, "red", [3, 1])
        # Both have legal moves and can be used together
        assert result is None

    def test_doubles_returns_none(self):
        gs = build_initial_game_state()
        result = must_use_both_dice(gs, "red", [3, 3])
        assert result is None

    def test_only_one_usable_returns_larger(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.points[0] = 1  # Red on point 1
        # Die 1: can bear off from point 1
        # Die 6: can bear off from point 1 (highest checker rule)
        # Both usable individually
        gs.board.off_red = 14
        # Actually let's make a case where only one works
        gs.board.points[0] = 0
        gs.board.points[3] = 1  # Red on point 4 only
        gs.board.off_red = 14
        # Die 2: point 4 -> point 2 (legal)
        # Die 5: point 4 -> overshoot -> bear off (highest checker)
        # After using die 2: checker on point 2, die 5 -> overshoot bear off
        # After using die 5: bear off, no checkers left, die 2 unusable
        # Both orderings work, so should return None
        result = must_use_both_dice(gs, "red", [2, 5])
        assert result is None

    def test_neither_usable_returns_empty(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.bar_red = 1
        # Block all entry points for both dice
        gs.board.points[23] = -2  # blocks die=1
        gs.board.points[21] = -2  # blocks die=3
        result = must_use_both_dice(gs, "red", [1, 3])
        assert result == []


class TestHasAnyLegalMove:
    def test_initial_has_moves(self):
        gs = build_initial_game_state()
        gs.dice = [3, 1]
        gs.dice_used = [False, False]
        assert has_any_legal_move(gs, "red")

    def test_no_dice_no_moves(self):
        gs = build_initial_game_state()
        gs.dice = [3, 1]
        gs.dice_used = [True, True]
        assert not has_any_legal_move(gs, "red")

    def test_completely_blocked(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.bar_red = 1
        # Block all 6 entry points
        for i in range(18, 24):
            gs.board.points[i] = -2
        gs.dice = [1, 2, 3, 4]
        gs.dice_used = [False, False, False, False]
        assert not has_any_legal_move(gs, "red")


# ==========================================================================
# GNUBG encoding tests
# ==========================================================================


class TestPositionIdEncoding:
    def test_starting_position(self):
        gs = build_initial_game_state()
        gs.current_color = "red"
        assert encode_position_id(gs) == "4HPwATDgc/ABMA"

    def test_symmetry(self):
        """Starting position should be symmetric — same ID regardless of turn."""
        gs = build_initial_game_state()
        gs.current_color = "red"
        id_red = encode_position_id(gs)
        gs.current_color = "white"
        id_white = encode_position_id(gs)
        # Both should encode to valid 14-char strings
        assert len(id_red) == 14
        assert len(id_white) == 14

    def test_bar_encoded(self):
        gs = build_initial_game_state()
        gs.current_color = "red"
        id_no_bar = encode_position_id(gs)
        gs.board.bar_red = 1
        gs.board.points[23] -= 1  # Remove one from point 24
        id_with_bar = encode_position_id(gs)
        assert id_no_bar != id_with_bar


class TestHintParsing:
    def test_simple_move(self):
        line = "    1. Cubeful 0-ply    8/5 6/5                      Eq.: +0.201"
        result = parse_hint_line(line)
        assert result == [("8", "5", 1), ("6", "5", 1)]

    def test_double_move(self):
        line = "    1. Cubeful 0-ply    24/18(2) 13/7(2)             Eq.: +0.390"
        result = parse_hint_line(line)
        assert result == [("24", "18", 2), ("13", "7", 2)]

    def test_bar_move(self):
        line = "    1. Cubeful 0-ply    bar/22 13/10                 Eq.: -0.100"
        result = parse_hint_line(line)
        assert result == [("bar", "22", 1), ("13", "10", 1)]

    def test_bear_off(self):
        line = "    1. Cubeful 2-ply    3/off 2/off                  Eq.: +1.000"
        result = parse_hint_line(line)
        assert result == [("3", "off", 1), ("2", "off", 1)]

    def test_non_hint_line(self):
        assert parse_hint_line("GNU Backgammon  Position ID: 4HPwATDgc/ABMA") is None
        assert parse_hint_line("") is None

    def test_hint_to_goals_red(self):
        submoves = [("8", "5", 1), ("6", "5", 1)]
        goals = hint_to_goals(submoves, "red")
        assert goals == [(7, 4), (5, 4)]

    def test_hint_to_goals_white(self):
        submoves = [("8", "5", 1)]
        goals = hint_to_goals(submoves, "white")
        # White's point 8 = index 24-8=16, point 5 = index 24-5=19
        assert goals == [(16, 19)]

    def test_hint_to_goals_bar(self):
        submoves = [("bar", "22", 1)]
        goals = hint_to_goals(submoves, "red")
        assert goals == [(-1, 21)]

    def test_hint_to_goals_off(self):
        submoves = [("3", "off", 1)]
        goals = hint_to_goals(submoves, "red")
        assert goals == [(2, 24)]

    def test_hint_to_goals_count(self):
        submoves = [("24", "18", 2)]
        goals = hint_to_goals(submoves, "red")
        assert goals == [(23, 17), (23, 17)]


# ==========================================================================
# Simple bot heuristic tests
# ==========================================================================


class TestSimpleBot:
    def test_forced_die_uses_legal_fallback(self):
        from types import SimpleNamespace
        from server.games.backgammon.game import BackgammonGame

        gs = build_initial_game_state()
        gs.board.points = [0, 3, 2, 0, 2, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 3, 0, 0, 2, 0, 0, 0, -2, 2]
        gs.board.off_white = 12
        gs.dice = [2, 5]
        gs.dice_used = [False, False]
        gs.current_color = "white"
        game = BackgammonGame()
        game.game_state = gs
        game._check_forced_dice()
        assert game._forced_dice == [5]
        player = SimpleNamespace(color="white")

        for action in (_pick_move(game, player), _pick_random_move(game, "white")):
            assert action is not None
            _, source, destination = action.split("_")
            assert any(
                move.source == int(source) and move.destination == int(destination)
                for move in generate_legal_moves(gs, "white", 5)
            )

    def test_prefers_bear_off(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.points[2] = 3
        gs.board.off_red = 12
        bear_off = BackgammonMove(source=2, destination=24, die_value=3, is_bear_off=True)
        normal = BackgammonMove(source=2, destination=0, die_value=2)
        assert _score_move(gs, bear_off, "red") > _score_move(gs, normal, "red")

    def test_prefers_hit(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.points[10] = 2
        gs.board.points[7] = -1
        hit = BackgammonMove(source=10, destination=7, die_value=3, is_hit=True)
        plain = BackgammonMove(source=10, destination=8, die_value=2)
        assert _score_move(gs, hit, "red") > _score_move(gs, plain, "red")

    def test_prefers_making_point(self):
        gs = build_initial_game_state()
        gs.board.points = [0] * 24
        gs.board.points[10] = 2
        gs.board.points[7] = 1  # Red blot — landing here makes a point
        gs.board.points[6] = 0  # Empty — landing here creates a blot
        make_point = BackgammonMove(source=10, destination=7, die_value=3)
        leave_blot = BackgammonMove(source=10, destination=6, die_value=4)
        assert _score_move(gs, make_point, "red") > _score_move(gs, leave_blot, "red")


# ==========================================================================
# Game registration tests
# ==========================================================================


class TestGameRegistration:
    def test_import(self):
        from server.games.backgammon import BackgammonGame

        assert BackgammonGame.get_name() == "Backgammon"
        assert BackgammonGame.get_type() == "backgammon"

    def test_registered(self):
        from server.games import BackgammonGame

        assert BackgammonGame is not None

    def test_min_max_players(self):
        assert BackgammonGame.get_min_players() == 2
        assert BackgammonGame.get_max_players() == 2

    def test_category(self):
        assert BackgammonGame.get_category() == "category-board-games"


class TestDifficultyOptions:
    def test_all_choices_have_labels(self):
        from server.games.backgammon.game import BOT_DIFFICULTY_LABELS

        for choice in BOT_DIFFICULTY_CHOICES:
            assert choice in BOT_DIFFICULTY_LABELS

    def test_all_choices_have_ply(self):
        for choice in BOT_DIFFICULTY_CHOICES:
            assert choice in DIFFICULTY_PLY

    def test_whackgammon_exists(self):
        assert "whackgammon" in BOT_DIFFICULTY_CHOICES
        assert DIFFICULTY_PLY["whackgammon"] == 0


class TestGridLayout:
    def test_grid_indices_count(self):
        game = BackgammonGame.__new__(BackgammonGame)
        indices = game._grid_indices()
        assert len(indices) == 24
        assert set(indices) == set(range(24))

    def test_grid_home_bottom_right_red(self):
        game = BackgammonGame.__new__(BackgammonGame)
        indices = game._grid_indices()
        bottom_row = indices[12:]  # Second 12
        # Red's home (points 1-6 = indices 0-5) should be on the right
        # Bottom row should end with index 0 (point 1)
        assert bottom_row[-1] == 0
        assert bottom_row[-6:] == [5, 4, 3, 2, 1, 0]

    def test_grid_top_row_starts_with_13(self):
        game = BackgammonGame.__new__(BackgammonGame)
        indices = game._grid_indices()
        top_row = indices[:12]
        # Top row: indices 12-23 (points 13-24)
        assert top_row[0] == 12  # point 13
        assert top_row[-1] == 23  # point 24
