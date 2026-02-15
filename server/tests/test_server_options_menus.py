"""Tests for options and language/dice style menu handlers in core.server."""

from __future__ import annotations

import asyncio
from types import SimpleNamespace

import pytest

from server.core.server import Server
from server.core.users.preferences import UserPreferences, DiceKeepingStyle


class DummyDB:
    def __init__(self):
        self.preferences_updates: list[tuple[str, str]] = []
        self.locale_updates: list[tuple[str, str]] = []

    def update_user_preferences(self, username: str, prefs_json: str) -> None:
        self.preferences_updates.append((username, prefs_json))

    def update_user_locale(self, username: str, locale: str) -> None:
        self.locale_updates.append((username, locale))


class DummyUser:
    def __init__(self, username: str, locale: str = "en"):
        self.username = username
        self.locale = locale
        self.preferences = UserPreferences()
        self.spoken: list[tuple[str, dict]] = []
        self.menu_id: str | None = None
        async def _send(payload):
            return None
        self.connection = SimpleNamespace(send=_send)

    def speak_l(self, message_id: str, buffer: str = "misc", **kwargs) -> None:
        self.spoken.append((message_id, kwargs))

    def show_menu(self, menu_id: str, *args, **kwargs) -> None:
        self.menu_id = menu_id

    def set_locale(self, locale: str) -> None:
        self.locale = locale


@pytest.fixture
def server(tmp_path, monkeypatch):
    srv = Server(host="127.0.0.1", port=0, db_path=tmp_path / "db.sqlite", preload_locales=True)
    srv._db = DummyDB()
    # simplify localization helpers
    monkeypatch.setattr(
        "server.messages.localization.Localization.get",
        lambda _locale, key, **kwargs: f"{key}:{kwargs}" if kwargs else key,
    )
    monkeypatch.setattr(
        "server.messages.localization.Localization.get_available_languages",
        lambda _locale="en", fallback="en": {"en": "English", "es": "Español"},
    )
    return srv


@pytest.mark.asyncio
async def test_handle_options_selection_toggle_turn_sound(server, monkeypatch):
    user = DummyUser("alice")
    user.preferences.play_turn_sound = True
    shown = {}
    monkeypatch.setattr(server, "_show_options_menu", lambda u: shown.setdefault("called", True))

    await server._handle_options_selection(user, "turn_sound")

    assert user.preferences.play_turn_sound is False
    assert server._db.preferences_updates  # saved
    assert shown.get("called")


@pytest.mark.asyncio
async def test_handle_options_selection_language_opens_menu(server, monkeypatch):
    user = DummyUser("alice")
    opened = {}
    monkeypatch.setattr(server, "_show_language_menu", lambda u: opened.setdefault("lang", True))

    await server._handle_options_selection(user, "language")

    assert opened.get("lang")


@pytest.mark.asyncio
async def test_handle_dice_style_selection_changes_pref(server, monkeypatch):
    user = DummyUser("alice")
    user.preferences.dice_keeping_style = DiceKeepingStyle.PLAYPALACE
    shown = {}
    monkeypatch.setattr(server, "_show_options_menu", lambda u: shown.setdefault("options", True))
    monkeypatch.setattr(server, "_save_user_preferences", lambda u: shown.setdefault("saved", True))

    await server._handle_dice_keeping_style_selection(user, "style_quentin_c")

    assert user.preferences.dice_keeping_style == DiceKeepingStyle.QUENTIN_C
    assert shown.get("saved")
    assert shown.get("options")
    assert ("dice-keeping-style-changed", {"style": "dice-keeping-style-values"}) in user.spoken


@pytest.mark.asyncio
async def test_handle_language_selection_updates_locale(server, monkeypatch):
    user = DummyUser("alice")
    shown = {}
    monkeypatch.setattr(server, "_show_options_menu", lambda u: shown.setdefault("options", True))

    await server._handle_language_selection(user, "lang_es")

    assert user.locale == "es"
    assert server._db.locale_updates == [("alice", "es")]
    assert ("language-changed", {"language": "Español"}) in user.spoken
    assert shown.get("options")
