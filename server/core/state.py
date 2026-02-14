"""Server lifecycle and readiness state helpers."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
import threading


class ServerMode(str, Enum):
    """Possible high-level server lifecycle states."""

    INITIALIZING = "initializing"
    RUNNING = "running"
    MAINTENANCE = "maintenance"


@dataclass(frozen=True)
class ModeSnapshot:
    """Simple snapshot of the current lifecycle mode."""

    mode: ServerMode
    message: str | None
    resume_at: datetime | None


class ServerLifecycleState:
    """Tracks readiness/maintenance gates in a thread-safe way."""

    def __init__(self) -> None:
        self._mode: ServerMode = ServerMode.INITIALIZING
        self._message_override: str | None = "Server is starting up."
        self._resume_at: datetime | None = None
        self._gates: dict[str, str | None] = {}
        self._lock = threading.RLock()

    def add_gate(self, gate_id: str, *, message: str | None = None) -> None:
        """Register a readiness gate that must resolve before running."""

        with self._lock:
            self._gates[gate_id] = message
            self._mode = ServerMode.INITIALIZING
            self._message_override = message or self._message_override
            self._resume_at = None

    def resolve_gate(self, gate_id: str) -> None:
        """Mark a readiness gate as finished; run when all gates clear."""

        with self._lock:
            self._gates.pop(gate_id, None)
            if not self._gates and self._mode == ServerMode.INITIALIZING:
                self._mode = ServerMode.RUNNING
                self._message_override = None
                self._resume_at = None

    def enter_maintenance(self, *, message: str, resume_at: datetime | None = None) -> None:
        """Switch to maintenance mode with an optional resume time."""

        with self._lock:
            self._mode = ServerMode.MAINTENANCE
            self._message_override = message
            if resume_at and resume_at.tzinfo is None:
                resume_at = resume_at.replace(tzinfo=timezone.utc)
            self._resume_at = resume_at

    def exit_maintenance(self) -> None:
        """Return to running mode (respecting outstanding gates)."""

        with self._lock:
            if self._gates:
                self._mode = ServerMode.INITIALIZING
            else:
                self._mode = ServerMode.RUNNING
            self._message_override = None
            self._resume_at = None

    def snapshot(self) -> ModeSnapshot:
        """Return the current lifecycle snapshot."""

        with self._lock:
            message = self._message_override
            resume_at = self._resume_at
            if self._mode == ServerMode.INITIALIZING:
                message = self._select_gate_message(default=message)
                resume_at = None
            return ModeSnapshot(self._mode, message, resume_at)

    def _select_gate_message(self, default: str | None) -> str:
        """Pick a deterministic message for initialization gates."""

        if self._gates:
            for gate_id in sorted(self._gates.keys()):
                gate_msg = self._gates[gate_id]
                if gate_msg:
                    return gate_msg
        return default or "Server is initializing."
