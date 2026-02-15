"""Tests covering admin/approval/ban editbox flows and leaderboards menus."""

from __future__ import annotations

import asyncio
from types import SimpleNamespace

import pytest

from server.core.server import Server
from server.core.users.base import TrustLevel


class DummyUser:
    def __init__(self, username: str, trust=TrustLevel.ADMIN, approved=True):
        self.username = username
        self.uuid = f"uuid-{username}"
        self.locale = "en"
        self.trust_level = trust
        self.approved = approved
        self.spoken: list[tuple[str, dict]] = []
        self.menus: list[str] = []
        self.sounds: list[str] = []
        self.sent: list[dict] = []

    def speak_l(self, message_id: str, buffer: str = "misc", **kwargs):
        self.spoken.append((message_id, kwargs))

    def show_menu(self, menu_id: str, *args, **kwargs):
        self.menus.append(menu_id)

    def play_sound(self, name: str, **kwargs):
        self.sounds.append(name)

    def set_trust_level(self, trust_level):
        self.trust_level = trust_level

    def speak(self, text: str, buffer: str = "misc"):
        self.spoken.append((text, {"buffer": buffer}))

    def set_approved(self, approved: bool):
        self.approved = approved

    def get_queued_messages(self):
        return []

    @property
    def connection(self):
        async def send(payload):
            self.sent.append(payload)
        return SimpleNamespace(send=send)


class DummyDB:
    def __init__(self):
        self.updated: list[tuple[str, str, str]] = []
        self.pending = []
        self.non_admins = ["newbie", "trouble"]

    def update_user_trust(self, username, trust_level, approved):
        self.updated.append((username, trust_level, approved))

    def get_pending_users(self, exclude_banned=True):
        return self.pending

    def get_non_admin_users(self, exclude_banned=True):
        return [SimpleNamespace(username=u, trust_level=TrustLevel.USER, approved=False) for u in self.non_admins]

    def approve_user(self, username):
        self.updated.append((username, TrustLevel.USER, True))
        return True

    def delete_user(self, username):
        self.updated.append((username, "deleted", False))
        return True

    def update_user_trust_level(self, username, trust_level):
        self.updated.append((username, trust_level, True))

    def get_game_stats(self, game_type, limit=1):
        return [("row",)]  # signal data exists


@pytest.fixture
def server(tmp_path, monkeypatch):
    srv = Server(host="127.0.0.1", port=0, db_path=tmp_path / "db.sqlite", preload_locales=True)
    srv._db = DummyDB()
    monkeypatch.setattr(
        "server.messages.localization.Localization.get",
        lambda _locale, key, **kwargs: key,
    )
    monkeypatch.setattr(
        "server.messages.localization.Localization.get_available_languages",
        lambda _locale="en", fallback="en": {"en": "English"},
    )
    monkeypatch.setattr(
        "server.messages.localization.Localization.format_list_and",
        lambda _locale, names: ", ".join(names),
    )
    return srv


@pytest.mark.asyncio
async def test_handle_admin_menu_promote_path(server):
    admin = DummyUser("admin", trust=TrustLevel.ADMIN)
    server._users = {"admin": admin}
    server._user_states["admin"] = {"menu": "admin_menu"}
    await server._handle_admin_menu_selection(admin, "promote_admin")
    assert admin.menus[-1] == "promote_admin_menu"


@pytest.mark.asyncio
async def test_handle_account_approval_selection_accepts(server):
    admin = DummyUser("admin", trust=TrustLevel.ADMIN)
    pending_user = DummyUser("newbie", trust=TrustLevel.USER, approved=False)
    server._users = {"admin": admin, "newbie": pending_user}
    server._db.pending = [SimpleNamespace(username="newbie", trust_level=TrustLevel.USER, approved=False)]
    await server._handle_account_approval_selection(admin, "pending_newbie")
    # Should route to pending actions menu
    assert admin.menus[-1] == "pending_user_actions_menu"


@pytest.mark.asyncio
async def test_handle_pending_user_actions_ban(server):
    admin = DummyUser("admin", trust=TrustLevel.ADMIN)
    target = DummyUser("trouble", trust=TrustLevel.USER, approved=False)
    server._users = {"admin": admin, "trouble": target}
    state = {"pending_username": "trouble"}

    await server._handle_pending_user_actions_selection(admin, "approve", state)

    assert ("trouble", TrustLevel.USER, True) in server._db.updated
    assert admin.menus[-1] in {"account_approval_menu", "admin_menu"}


@pytest.mark.asyncio
async def test_handle_ban_reason_editbox_applies(server):
    admin = DummyUser("admin", trust=TrustLevel.ADMIN)
    target = DummyUser("trouble")
    server._users = {"admin": admin, "trouble": target}
    state = {"target_username": "trouble", "broadcast_scope": "nobody"}

    await server._handle_ban_reason_editbox(admin, "bye", state)

    assert any(u[0] == "trouble" and u[1] == TrustLevel.BANNED for u in server._db.updated)
    assert admin.menus[-1] in {"admin_menu", "ban_user_menu"}


def test_show_leaderboard_types_menu_with_data(server):
    user = DummyUser("alice")
    server._users = {"alice": user}
    # Stub registry: return a fake game class with leaderboard types
    fake_game = SimpleNamespace(
        get_name_key=lambda: "fake",
        get_leaderboard_types=lambda: [{"id": "custom_stat"}],
        get_type=lambda: "fake",
    )
    # monkeypatch GameRegistry.get_by_category and get_game_class inline
    from server.games import registry

    registry.GameRegistry.get_by_category = staticmethod(lambda: {"misc": [fake_game]})  # type: ignore[assignment]
    registry.get_game_class = lambda gt: fake_game  # type: ignore[assignment]
    import server.core.server as core_server_module
    core_server_module.get_game_class = registry.get_game_class  # type: ignore[assignment]

    server._show_leaderboard_types_menu(user, "fake")

    assert user.menus[-1] == "leaderboard_types_menu"
