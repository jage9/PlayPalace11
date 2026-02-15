"""Tests for core.ui.keybinds helpers."""

from __future__ import annotations

import pytest

from server.core.ui.keybinds import Keybind, KeybindScope, KeybindState


class DummyGame:
    def __init__(self, status: str):
        self.status = status


class DummyPlayer:
    def __init__(self, name: str):
        self.name = name


def test_is_state_active_by_status():
    game_playing = DummyGame(status="playing")
    game_waiting = DummyGame(status="waiting")

    assert Keybind("k", "k", [], state=KeybindState.NEVER).is_state_active(game_playing) is False
    assert Keybind("k", "k", [], state=KeybindState.ALWAYS).is_state_active(game_playing) is True
    assert Keybind("k", "k", [], state=KeybindState.IDLE).is_state_active(game_waiting) is True
    assert Keybind("k", "k", [], state=KeybindState.IDLE).is_state_active(game_playing) is False
    assert Keybind("k", "k", [], state=KeybindState.ACTIVE).is_state_active(game_playing) is True
    assert Keybind("k", "k", [], state=KeybindState.ACTIVE).is_state_active(game_waiting) is False


def test_can_player_use_respects_spectators_and_whitelist():
    game = DummyGame(status="playing")
    player = DummyPlayer("alice")
    spectator = True

    kb = Keybind(
        "action",
        "a",
        ["do"],
        state=KeybindState.ALWAYS,
        include_spectators=False,
        players=["alice"],
    )

    assert kb.can_player_use(game, player, is_spectator=False) is True
    assert kb.can_player_use(game, player, is_spectator=spectator) is False

    kb.include_spectators = True
    assert kb.can_player_use(game, player, is_spectator=True) is True

    other = DummyPlayer("bob")
    assert kb.can_player_use(game, other, is_spectator=False) is False


def test_is_state_active_falls_back_to_false_on_unknown_state():
    game = DummyGame(status="playing")
    kb = Keybind("x", "x", [], state=KeybindState.ALWAYS)
    kb.state = None  # type: ignore[assignment]

    assert kb.is_state_active(game) is False


def test_can_player_use_short_circuits_when_inactive():
    game = DummyGame(status="waiting")
    kb = Keybind("x", "x", [], state=KeybindState.NEVER)

    assert kb.can_player_use(game, DummyPlayer("a"), is_spectator=False) is False


def test_keybind_scope_enum_values():
    assert KeybindScope.GLOBAL.name == "GLOBAL"
    assert KeybindScope.TABLE.name == "TABLE"
