"""Turn system utilities: turn tracking and round transition timers."""

from dataclasses import dataclass, field
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ..games.base import Game


class RoundTransitionTimer:
    """
    Stateless helper for managing delays between rounds.

    All timer state is stored in Game fields for serialization:
    - game.round_timer_state: "idle", "counting", or "paused"
    - game.round_timer_ticks: Remaining ticks in countdown
    """

    # Timer states (stored in game.round_timer_state)
    IDLE = "idle"  # Not running
    COUNTING = "counting"  # Counting down
    PAUSED = "paused"  # Paused by host

    def __init__(
        self,
        game: "Game",
        delay_seconds: float = 15.0,
        pause_message: str = "round-timer-paused",
    ) -> None:
        """
        Initialize the round transition timer.

        Args:
            game: The game instance.
            delay_seconds: Seconds to wait between rounds (default 15).
            pause_message: Localization key for pause announcement.
        """
        self._game = game
        self._delay_ticks = int(delay_seconds * 20)  # 20 ticks per second (50ms tick)
        self._pause_message = pause_message

    @property
    def is_active(self) -> bool:
        """Check if the timer is running (counting or paused)."""
        return self._game.round_timer_state in (self.COUNTING, self.PAUSED)

    @property
    def is_paused(self) -> bool:
        """Check if the timer is paused."""
        return self._game.round_timer_state == self.PAUSED

    @property
    def remaining_seconds(self) -> int:
        """Get remaining seconds (rounded up)."""
        return (self._game.round_timer_ticks + 19) // 20

    def start(self, delay_seconds: float | None = None) -> None:
        """
        Start the countdown timer.

        Args:
            delay_seconds: Override the default delay for this countdown.
        """
        if delay_seconds is not None:
            self._game.round_timer_ticks = int(delay_seconds * 20)
        else:
            self._game.round_timer_ticks = self._delay_ticks
        self._game.round_timer_state = self.COUNTING

    def stop(self) -> None:
        """Stop the timer without triggering the callback."""
        self._game.round_timer_state = self.IDLE
        self._game.round_timer_ticks = 0

    def toggle_pause(self, player_name: str | None = None) -> None:
        """
        Toggle pause state. Called when host presses 'p'.

        - If counting: pause the timer
        - If paused: skip remaining time and start next round
        - If idle: do nothing

        Args:
            player_name: Name of the player who triggered the action.
        """
        if self._game.round_timer_state == self.COUNTING:
            # Pause the countdown
            self._game.round_timer_state = self.PAUSED
            self._game.broadcast_l(self._pause_message, player=player_name or "")
        elif self._game.round_timer_state == self.PAUSED:
            # Skip to next round
            self._game.round_timer_state = self.IDLE
            self._game.round_timer_ticks = 0
            self._game.on_round_timer_ready()

    def on_tick(self) -> None:
        """Called every game tick. Decrements timer if counting."""
        if self._game.round_timer_state != self.COUNTING:
            return

        self._game.round_timer_ticks -= 1

        # Check if timer expired
        if self._game.round_timer_ticks <= 0:
            self._game.round_timer_state = self.IDLE
            self._game.on_round_timer_ready()


@dataclass
class TurnTimer:
    """Simple per-turn timer (counts up in ticks)."""

    ticks: int = 0
    running: bool = False

    def start(self) -> None:
        self.running = True

    def stop(self) -> None:
        self.running = False

    def reset(self) -> None:
        self.ticks = 0

    def tick(self) -> None:
        if self.running:
            self.ticks += 1


@dataclass
class GameTurn:
    """Represents one turn in a game round."""

    turn_number: int
    cycle: int
    ticks: int
    players: set[str] = field(default_factory=set)


@dataclass
class GameRound:
    """Represents a round of turns."""

    round_number: int
    cycle_count: int = 0
    max_turn_cycles: int = 0  # Force end after this many cycles (0 = no limit)
    turns: list[GameTurn] = field(default_factory=list)
    turn_timer: TurnTimer = field(default_factory=TurnTimer)
    final_scores: dict[str, int] = field(default_factory=dict)

    def add_turn(self, player_ids: set[str] | None = None) -> GameTurn:
        """Record a completed turn and return it."""
        turn = GameTurn(
            turn_number=len(self.turns),
            cycle=self.cycle_count,
            ticks=self.turn_timer.ticks,
            players=player_ids or set(),
        )
        self.turns.append(turn)
        return turn

    def get_turns_in_cycles(
        self, min_cycle: int | None = None, max_cycle: int | None = None
    ) -> list[GameTurn]:
        """Return turns within the requested cycle range (inclusive)."""
        if min_cycle is None and max_cycle is None:
            min_cycle = max_cycle = self.cycle_count
        if min_cycle is None:
            min_cycle = 0
        if max_cycle is None:
            max_cycle = self.cycle_count
        return [turn for turn in self.turns if min_cycle <= turn.cycle <= max_cycle]

    def get_turns_for_player(
        self, player_id: str, min_turn: int | None = None, max_turn: int | None = None
    ) -> list[GameTurn]:
        """Return turns taken by the specified player."""
        played_turns = [turn for turn in self.turns if player_id in turn.players]
        if min_turn is None and max_turn is None:
            return played_turns[-1:]  # last turn only
        if min_turn is None:
            min_turn = 0
        if max_turn is None:
            return played_turns[min_turn:]
        return played_turns[min_turn : max_turn + 1]

    def get_ticks_in_turns(self, turns: list[GameTurn] | None = None) -> int:
        """Return total ticks across the selected turns."""
        if turns is None:
            turns = self.turns
        return sum(turn.ticks for turn in turns)

    def record_scores(self, players: list) -> dict[str, int]:
        """Record final scores for the round."""
        self.turn_timer.stop()
        self.turn_timer.reset()
        self.final_scores.update({p.id: getattr(p, "score", 0) for p in players})
        return self.final_scores


@dataclass
class TurnTrackerMixin:
    """Mixin providing round/cycle/turn tracking utilities."""

    rounds: list[GameRound] = field(default_factory=list)

    def _get_turn_tracker_callbacks(self) -> dict[str, Callable] | None:
        return getattr(self, "_turn_tracker_callbacks", None)

    def set_turn_tracker_callbacks(
        self,
        *,
        start_round: Callable | None = None,
        end_round: Callable | None = None,
        start_cycle: Callable | None = None,
        end_cycle: Callable | None = None,
        start_turn: Callable | None = None,
        end_turn: Callable | None = None,
    ) -> None:
        """Register callbacks for turn tracker lifecycle events (runtime-only)."""
        self._turn_tracker_callbacks = {
            "start_round": start_round,
            "end_round": end_round,
            "start_cycle": start_cycle,
            "end_cycle": end_cycle,
            "start_turn": start_turn,
            "end_turn": end_turn,
        }

    def _call_turn_tracker_callback(self, name: str, *args, **kwargs) -> None:
        callbacks = self._get_turn_tracker_callbacks()
        if not callbacks:
            return
        callback = callbacks.get(name)
        if callback:
            callback(*args, **kwargs)

    def on_round_start(self, *args, **kwargs) -> GameRound:
        """Start a new round and record it."""
        round_number = len(self.rounds) + 1
        current_round = GameRound(round_number=round_number)
        self.rounds.append(current_round)
        self._call_turn_tracker_callback("start_round", *args, **kwargs)
        return current_round

    def on_round_end(self, players: list | None = None, *args, **kwargs) -> None:
        """End the current round and record scores."""
        if not self.rounds:
            return
        current_round = self.rounds[-1]
        if players is None:
            players = getattr(self, "players", [])
        current_round.record_scores(players)
        self._call_turn_tracker_callback("end_round", *args, **kwargs)

    def on_turn_cycle_start(self, *args, **kwargs) -> None:
        """Start a new turn cycle within the current round."""
        if not self.rounds:
            self.on_round_start()
        current_round = self.rounds[-1]
        current_round.cycle_count += 1
        self._call_turn_tracker_callback("start_cycle", *args, **kwargs)

    def on_turn_cycle_end(self, *args, **kwargs) -> None:
        """End the current turn cycle and optionally end round."""
        if not self.rounds:
            return
        current_round = self.rounds[-1]
        self._call_turn_tracker_callback("end_cycle", *args, **kwargs)
        if current_round.max_turn_cycles > 0 and current_round.cycle_count >= current_round.max_turn_cycles:
            self.on_round_end(getattr(self, "players", []))

    def on_turn_start(self, *args, **kwargs) -> None:
        """Start a new turn within the current round."""
        if not self.rounds:
            self.on_round_start()
        current_round = self.rounds[-1]
        if current_round.cycle_count == 0:
            self.on_turn_cycle_start()
        current_round.turn_timer.reset()
        current_round.turn_timer.start()
        self._call_turn_tracker_callback("start_turn", *args, **kwargs)

    def on_turn_end(self, player_ids: set[str] | None = None, *args, **kwargs) -> GameTurn | None:
        """End the current turn and record it."""
        if not self.rounds:
            return None
        current_round = self.rounds[-1]
        current_round.turn_timer.stop()
        if player_ids is None:
            current_player = getattr(self, "current_player", None)
            if current_player is not None:
                player_ids = {current_player.id}
        turn = current_round.add_turn(player_ids)
        current_round.turn_timer.reset()
        self._call_turn_tracker_callback("end_turn", *args, **kwargs)
        return turn

    def ensure_turn_started(self) -> None:
        """Ensure the turn tracker is running for the current turn."""
        if not self.rounds or not self.rounds[-1].turn_timer.running:
            self.on_turn_start()

    def tick_turn_tracker(self) -> None:
        """Advance the active turn timer by one tick (call from on_tick)."""
        if not self.rounds:
            return
        current_round = self.rounds[-1]
        current_round.turn_timer.tick()

    def get_total_turns(self) -> int:
        """Return total number of turns across all rounds."""
        return sum(len(round_.turns) for round_ in self.rounds)

    def get_total_cycles(self) -> int:
        """Return total number of turn cycles across all rounds."""
        return sum(round_.cycle_count for round_ in self.rounds)

    def get_total_ticks(self) -> int:
        """Return total number of ticks across all rounds."""
        return sum(round_.get_ticks_in_turns() for round_ in self.rounds)


# Backwards-compatible alias
RoundTimer = RoundTransitionTimer
