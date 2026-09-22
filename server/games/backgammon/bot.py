"""Bot AI for Backgammon — GNUBG engine with random/simple fallback.

GNUBG queries run in a background thread to avoid blocking the server.
bot_think() returns None while waiting for a result, and the BotHelper
will retry on the next tick.
"""

from __future__ import annotations

import logging
import random
from concurrent.futures import Future, ThreadPoolExecutor
from typing import TYPE_CHECKING

log = logging.getLogger(__name__)

from .gnubg import GnubgProcess, is_gnubg_available, resolve_next_action
from .moves import BackgammonMove, generate_legal_moves, has_any_legal_move
from .state import (
    bar_count,
    color_sign,
    off_count,
    opponent_color,
    point_count,
    point_owner,
)

if TYPE_CHECKING:
    from .game import BackgammonGame, BackgammonPlayer

# Shared thread pool for GNUBG queries (1 thread — GNUBG is single-process)
_gnubg_pool = ThreadPoolExecutor(max_workers=1, thread_name_prefix="gnubg")


def bot_think(game: BackgammonGame, player: BackgammonPlayer) -> str | None:
    """Decide the bot's next action."""
    gs = game.game_state
    color = player.color

    # Check if we're waiting for an async GNUBG result
    pending = _check_pending(game)
    if pending is not None:
        return pending
    if _is_pending(game):
        return None  # Still waiting

    if gs.turn_phase == "pre_roll":
        game._bot_goals.clear()
        # GNUBG bots consider doubling before rolling
        cube_action = _maybe_offer_double(game, player)
        if cube_action is _WAITING:
            return None
        if cube_action:
            return cube_action
        return "point_0"

    if gs.turn_phase == "doubling":
        return _decide_take_or_drop(game, player)

    if gs.turn_phase == "moving":
        if not has_any_legal_move(gs, color):
            game._end_moving_phase()
            return None
        # Resolve next action from GNUBG goals if available
        if game._bot_goals:
            action = resolve_next_action(game._bot_goals, gs, color, forced_dice=game._forced_dice)
            if action:
                return action
            # Goals exhausted or stuck — fall through to pick a new move
            game._bot_goals.clear()
        return _pick_move(game, player)

    return None


# Sentinel value meaning "query submitted, wait for it"
_WAITING = object()


def _submit_async(game: BackgammonGame, fn, *args) -> None:
    """Submit a GNUBG query to the thread pool."""
    game._gnubg_future = _gnubg_pool.submit(fn, *args)


def _is_pending(game: BackgammonGame) -> bool:
    """Check if there's an in-flight GNUBG query."""
    future = getattr(game, "_gnubg_future", None)
    return future is not None and not future.done()


def _check_pending(game: BackgammonGame) -> str | None:
    """Check if a pending GNUBG query has completed. Returns action or None."""
    future: Future | None = getattr(game, "_gnubg_future", None)
    if future is None or not future.done():
        return None

    game._gnubg_future = None
    try:
        result = future.result(timeout=0)
    except Exception:
        result = None

    # Move queries return a goals list — store them for bot_think to resolve
    if isinstance(result, list):
        game._bot_goals = result
        return None  # bot_think will resolve on the current state

    # Cube/other queries return an action string
    if result is not None:
        return result

    # Future completed but returned None — GNUBG failed.
    log.warning("GNUBG future returned None (phase=%s)", game.game_state.turn_phase)
    _notify_fallback(game)
    gs = game.game_state
    color = gs.current_color
    if gs.turn_phase == "moving":
        return _pick_simple_move(game, color)
    if gs.turn_phase == "pre_roll":
        return "point_0"  # Just roll
    if gs.turn_phase == "doubling":
        return "accept_double"
    return None


def _maybe_offer_double(game: BackgammonGame, player: BackgammonPlayer):
    """Check if a GNUBG-backed bot should offer a double before rolling.

    Returns an action string, None (no double), or _WAITING.
    """
    from .game import DIFFICULTY_PLY

    difficulty = game.options.bot_difficulty
    if difficulty in ("random", "simple"):
        return None

    ply = DIFFICULTY_PLY.get(difficulty)
    if ply is None:
        return None

    if difficulty == "whackgammon":
        return None

    if not game._can_double(player):
        return None

    gnubg_proc = _get_gnubg_process(game, ply)
    if gnubg_proc is None:
        return None

    # Submit async query
    def _query():
        decision = gnubg_proc.get_cube_decision(game.game_state, player.color)
        if decision in ("double-take", "double-pass"):
            # Store decision so the opponent's take/drop can use it
            game._gnubg_cube_decision = decision
            return "offer_double"
        return "point_0"  # No double, just roll

    _submit_async(game, _query)
    return _WAITING


def _decide_take_or_drop(game: BackgammonGame, player: BackgammonPlayer) -> str | None:
    """Decide whether to take or drop a double offer.

    Uses the cube decision stored by _maybe_offer_double when the opponent
    doubled. GNUBG's analysis is always from the doubler's perspective —
    "double-pass" means the receiver should drop, "double-take" means take.
    """
    from .game import DIFFICULTY_PLY

    difficulty = game.options.bot_difficulty
    if difficulty in ("random", "simple"):
        return "accept_double"

    ply = DIFFICULTY_PLY.get(difficulty)
    if ply is None:
        return "accept_double"

    if difficulty == "whackgammon":
        return "accept_double"

    # Use the stored decision from the doubler's GNUBG query
    stored = getattr(game, "_gnubg_cube_decision", None)
    if stored == "double-pass":
        game._gnubg_cube_decision = None
        return "drop_double"
    # "double-take", unknown, or no stored decision — accept
    game._gnubg_cube_decision = None
    return "accept_double"


def _pick_move(game: BackgammonGame, player: BackgammonPlayer) -> str | None:
    """Pick a move based on the configured difficulty."""
    from .game import DIFFICULTY_PLY

    gs = game.game_state
    color = player.color
    difficulty = game.options.bot_difficulty

    if difficulty == "random":
        return _pick_random_move(game, color)

    if difficulty == "simple":
        return _pick_simple_move(game, color)

    # GNUBG-based difficulties — run async
    ply = DIFFICULTY_PLY.get(difficulty)
    if ply is None:
        return _pick_random_move(game, color)

    is_whack = difficulty == "whackgammon"
    gnubg_proc = _get_gnubg_process(game, ply)
    if gnubg_proc is None:
        _notify_fallback(game)
        return _pick_simple_move(game, color)

    def _query():
        if is_whack:
            goals = gnubg_proc.get_worst_move(gs, color)
        else:
            goals = gnubg_proc.get_best_move(gs, color)
        if goals:
            return goals  # Return goals; bot_think resolves with current state
        return None  # GNUBG failed

    _submit_async(game, _query)
    return None  # Wait for result


def _pick_random_move(game: BackgammonGame, color: str) -> str | None:
    """Pick a random legal move, trying all unused die values."""
    gs = game.game_state
    for die_val in game._get_usable_dice():
        moves = generate_legal_moves(gs, color, die_val)
        if moves:
            move = random.choice(moves)  # nosec B311
            return f"point_{move.source}_{move.destination}"
    return None


def _pick_simple_move(game: BackgammonGame, color: str) -> str | None:
    """Pick a move using simple heuristics.

    Priority scoring:
    - Bearing off is great
    - Hitting an opponent blot is good
    - Making a new point (landing where we have exactly 1) is good
    - Escaping from opponent's home board is decent
    - Leaving a blot in a dangerous area is bad
    """
    gs = game.game_state
    best_move: BackgammonMove | None = None
    best_score = -9999

    for die_val in game._get_usable_dice():
        for move in generate_legal_moves(gs, color, die_val):
            score = _score_move(gs, move, color)
            if score > best_score:
                best_score = score
                best_move = move

    if best_move is None:
        return None
    return f"point_{best_move.source}_{best_move.destination}"


def _score_move(gs, move: BackgammonMove, color: str) -> int:
    """Score a move with simple heuristics. Higher is better."""
    score = 0
    sign = color_sign(color)
    opp = opponent_color(color)

    # Bear off: strongly prefer
    if move.is_bear_off:
        score += 100

    # Hit: good, especially in our home board
    if move.is_hit:
        score += 40
        # Hitting in our home board is even better (harder to re-enter)
        if color == "red" and move.destination <= 5:
            score += 20
        elif color == "white" and move.destination >= 18:
            score += 20

    # Making a point (landing where we have exactly 1 checker already)
    if not move.is_bear_off and move.destination >= 0 and move.destination <= 23:
        current = gs.board.points[move.destination]
        if current * sign == 1:
            # We have 1 there — this makes a 2-stack (a point!)
            score += 35
            # Making points in our home board is premium
            if color == "red" and move.destination <= 5:
                score += 15
            elif color == "white" and move.destination >= 18:
                score += 15

    # Leaving a blot (source had 2, now will have 1)
    if move.source >= 0:
        src_count = abs(gs.board.points[move.source])
        if src_count == 2:
            # We're exposing a blot
            score -= 15
            # Worse if in opponent's home board
            if color == "red" and move.source >= 18:
                score -= 15
            elif color == "white" and move.source <= 5:
                score -= 15

    # Landing alone (creating a blot) on an empty point
    if not move.is_bear_off and move.destination >= 0 and move.destination <= 23:
        dest_val = gs.board.points[move.destination]
        if dest_val * sign == 0 and not move.is_hit:
            # Landing alone on empty point = blot
            score -= 10
            # Worse in dangerous territory
            if color == "red" and move.destination >= 18:
                score -= 10
            elif color == "white" and move.destination <= 5:
                score -= 10

    # Prefer advancing runners from opponent's home board
    if move.source >= 0:
        if color == "red" and move.source >= 18:
            score += 8
        elif color == "white" and move.source <= 5:
            score += 8

    # Bar entry: just do it (no penalty, no bonus beyond the hit check)
    if move.source == -1:
        score += 5

    # Small tiebreaker: prefer moving from higher points (advance)
    if move.source >= 0:
        if color == "red":
            score += move.source // 6
        else:
            score += (23 - move.source) // 6

    return score


def _notify_fallback(game: BackgammonGame) -> None:
    """Notify players once that GNUBG is unavailable and bot is using fallback."""
    if getattr(game, "_gnubg_fallback_notified", False):
        return
    game._gnubg_fallback_notified = True
    game.broadcast_l("backgammon-gnubg-fallback")


def _get_gnubg_process(game: BackgammonGame, ply: int) -> GnubgProcess | None:
    """Get or create the GNUBG process for this game."""
    proc = getattr(game, "_gnubg_proc", None)
    if proc is not None:
        return proc

    if not is_gnubg_available():
        return None

    proc = GnubgProcess(ply=ply)
    if proc.start():
        game._gnubg_proc = proc
        return proc

    return None


def cleanup_gnubg(game: BackgammonGame) -> None:
    """Stop GNUBG processes when the game ends."""
    for attr in ("_gnubg_proc", "_hint_proc"):
        proc = getattr(game, attr, None)
        if proc is not None:
            proc.stop()
            setattr(game, attr, None)
