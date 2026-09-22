"""Mixin for turn timer logic in games."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..games.base import Player


class TurnTimerMixin:
    """Mixin for managing turn timers.

    Requires the class to have:
    - self.timer: PokerTurnTimer
    - self.options: object with 'turn_timer' attribute (str)
    - self.play_sound(sound: str)
    - _on_turn_timeout() -> implement this!
    """

    def start_turn_timer(self) -> None:
        """Start the turn timer based on game options."""
        self._reset_timer_warning()

        try:
            # Handle both string "30" and int 30
            seconds = int(self.options.turn_timer)
        except (TypeError, ValueError, AttributeError):
            seconds = 0

        if seconds <= 0:
            self.timer.clear()
            return

        self.timer.start(seconds)

    # Existing game code and saved callbacks use this name.
    _start_turn_timer = start_turn_timer

    def stop_turn_timer(self) -> None:
        """Stop/clear the turn timer."""
        self.timer.clear()
        self._reset_timer_warning()

    def on_tick_turn_timer(self) -> None:
        """Called every tick to update timer and check for timeout."""
        if self.timer.tick():
            self._on_turn_timeout()

        self._maybe_play_timer_warning()

    def _action_check_turn_timer(self, player: "Player", action_id: str) -> None:
        """Speak the remaining turn time to the requesting player."""
        user = self.get_user(player)
        if not user:
            return
        remaining = self.timer.seconds_remaining()
        if remaining <= 0:
            user.speak_l("poker-timer-disabled")
        else:
            user.speak_l("poker-timer-remaining", seconds=remaining)

    def _reset_timer_warning(self) -> None:
        """Reset the warning state when the game has a serialized warning flag."""
        warning_attr = self._timer_warning_attr()
        if warning_attr:
            setattr(self, warning_attr, False)

    def _timer_warning_attr(self) -> str | None:
        """Return the serialized warning field used by the game."""
        if hasattr(self, "timer_warning_played"):
            return "timer_warning_played"
        if hasattr(self, "_timer_warning_played"):
            return "_timer_warning_played"
        return None

    def _maybe_play_timer_warning(self) -> None:
        """Play warning sound if time is running out."""
        warning_attr = self._timer_warning_attr()
        if not warning_attr:
            return
        if getattr(self, warning_attr):
            return

        # Check if actual timer is active/has meaningful duration
        try:
            total_seconds = int(self.options.turn_timer)
        except (TypeError, ValueError, AttributeError):
            total_seconds = 0

        # Don't warn for very short timers or unlimited
        if total_seconds < 20:
            return

        remaining = self.timer.seconds_remaining()
        if remaining == 5:
            setattr(self, warning_attr, True)
            self.play_sound(self.timer_warning_sound)

    @property
    def timer_warning_sound(self) -> str:
        """
        Get the warning sound file path.

        Subclasses with warnings should override this property.
        """
        return "game_crazyeights/fivesec.ogg"

    def _on_turn_timeout(self) -> None:
        """Dispatch expiry to the existing game timeout callback."""
        self._handle_turn_timeout()
