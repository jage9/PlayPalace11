"""Tests for ServerLifecycleState helpers."""

from __future__ import annotations

from datetime import datetime

from server.core.state import ServerLifecycleState, ServerMode


def test_enter_maintenance_normalizes_naive_datetime():
    state = ServerLifecycleState()
    resume = datetime(2025, 1, 1, 12, 0, 0)

    state.enter_maintenance(message="maint", resume_at=resume)
    snapshot = state.snapshot()

    assert snapshot.mode == ServerMode.MAINTENANCE
    assert snapshot.resume_at.tzinfo is not None


def test_exit_maintenance_with_pending_gates_sets_initializing():
    state = ServerLifecycleState()
    state.add_gate("load")
    state.enter_maintenance(message="maint")

    state.exit_maintenance()

    assert state.snapshot().mode == ServerMode.INITIALIZING


def test_select_gate_message_prefers_sorted_gate_message():
    state = ServerLifecycleState()
    state.add_gate("b_gate", message="second")
    state.add_gate("a_gate", message="first")

    snap = state.snapshot()

    assert snap.message == "first"
