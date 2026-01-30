"""Tests for DurationEstimateMixin helpers and completion flow."""

import threading

from server.game_utils.duration_estimate_mixin import DurationEstimateMixin


class DeadThread:
    def is_alive(self) -> bool:
        return False


class DummyGame(DurationEstimateMixin):
    TICKS_PER_SECOND = 20

    def __init__(self):
        self._estimate_threads: list[DeadThread] = []
        self._estimate_results: list[int] = []
        self._estimate_errors: list[str] = []
        self._estimate_running: bool = False
        self._estimate_lock = threading.Lock()
        self.players = []
        self.broadcast_events: list[tuple[str, dict]] = []

    def broadcast_l(self, message_id: str, **kwargs) -> None:
        self.broadcast_events.append((message_id, kwargs))

    def broadcast(self, message: str) -> None:
        self.broadcast_events.append(("raw", {"text": message}))

    # Methods referenced by the mixin but not used in these tests
    def get_user(self, _player):
        return None

    def get_type(self) -> str:
        return "dummy"

    def get_min_players(self) -> int:
        return 1


def test_check_estimate_completion_broadcasts_results_and_resets():
    game = DummyGame()
    game._estimate_threads = [DeadThread(), DeadThread()]
    game._estimate_results = [1200, 1800, 2400, 3000]
    game._estimate_errors = []
    game._estimate_running = True

    game.check_estimate_completion()

    assert not game._estimate_threads
    assert not game._estimate_results
    assert not game._estimate_errors
    assert game._estimate_running is False

    message_id, payload = game.broadcast_events[-1]
    assert message_id == "estimate-result"
    # Average of sample ticks -> 2100 ticks = 105 seconds -> 1:45
    assert payload["bot_time"] == "1:45"
    assert "human_time" in payload


def test_detect_outliers_and_std_dev_helpers():
    game = DummyGame()
    values = [10, 11, 12, 13, 100]
    mean = sum(values) / len(values)
    std_dev = game._calculate_std_dev(values, mean)
    assert std_dev > 0

    outliers = game._detect_outliers(values)
    assert 100 in outliers and len(outliers) == 1


def test_format_duration_handles_seconds_and_hours():
    game = DummyGame()
    assert game._format_duration(40) == "2 seconds"
    assert game._format_duration(20 * 75) == "1:15"
    assert game._format_duration(20 * 3700) == "1:01:40"
