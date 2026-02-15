"""Additional coverage for server core announcement and preference helpers."""

from __future__ import annotations

from types import SimpleNamespace

import pytest

from server.core.server import Server
from server.core.users.preferences import UserPreferences


class DummyUser:
    def __init__(self, approved: bool = True) -> None:
        self.approved = approved
        self.spoken: list[tuple[str, str, dict]] = []
        self.sounds: list[str] = []
        self.queued: list[dict] = []
        self.main_menu_shown = False

    def speak_l(self, message_id: str, buffer: str = "misc", **kwargs) -> None:
        self.spoken.append((message_id, buffer, kwargs))

    def play_sound(self, name: str, **_: object) -> None:
        self.sounds.append(name)

    def queue_packet(self, packet: dict) -> None:
        self.queued.append(packet)


class FakeDBPending:
    def __init__(self, pending: list[str]) -> None:
        self.pending = pending

    def get_pending_users(self, exclude_banned: bool = True):
        return self.pending


@pytest.fixture
def server(tmp_path):
    return Server(host="127.0.0.1", port=0, db_path=tmp_path / "db.sqlite", preload_locales=True)


def test_broadcast_admin_announcement_only_hits_approved(server):
    approved_user = DummyUser(approved=True)
    pending_user = DummyUser(approved=False)
    server._users = {"approved": approved_user, "pending": pending_user}

    server._broadcast_admin_announcement("moderator")

    assert approved_user.spoken == [("user-is-admin", "activity", {"player": "moderator"})]
    assert pending_user.spoken == []


def test_broadcast_owner_announcement_only_hits_approved(server):
    owner_user = DummyUser(approved=True)
    unapproved = DummyUser(approved=False)
    server._users = {"owner": owner_user, "waiting": unapproved}

    server._broadcast_server_owner_announcement("boss")

    assert owner_user.spoken == [("user-is-server-owner", "activity", {"player": "boss"})]
    assert unapproved.spoken == []


def test_notify_pending_account_requests_speaks_and_sounds(server):
    user = DummyUser()
    server._db = FakeDBPending(["someone"])

    server._notify_pending_account_requests(user)

    assert ("account-request", "activity", {}) in user.spoken
    assert "accountrequest.ogg" in user.sounds


def test_notify_pending_account_requests_no_pending_silent(server):
    user = DummyUser()
    server._db = FakeDBPending([])

    server._notify_pending_account_requests(user)

    assert user.spoken == []
    assert user.sounds == []


def test_load_user_preferences_invalid_json_returns_defaults(server):
    record = SimpleNamespace(preferences_json="not json")

    prefs = server._load_user_preferences(record)

    assert prefs == UserPreferences()


def test_handle_unapproved_login_routes_to_main_menu(server, monkeypatch):
    user = DummyUser(approved=False)

    def _mark_main_menu(target):
        target.main_menu_shown = True

    monkeypatch.setattr(server, "_show_main_menu", _mark_main_menu)

    result = server._handle_unapproved_login(user)

    assert result is True
    assert ("waiting-for-approval", "activity", {}) in user.spoken
    assert user.main_menu_shown is True


def test_queue_transcript_replay_enqueues_history(server):
    user = DummyUser()

    class DummyGame:
        def __init__(self):
            self.transcripts = {
                "player1": [
                    {"text": "line one"},
                    {"text": "line two", "buffer": "activity"},
                ]
            }

        def get_transcript(self, player_id):
            return self.transcripts.get(player_id)

    game = DummyGame()

    server._queue_transcript_replay(user, game, "player1")

    assert user.queued == [
        {"type": "speak", "text": "line one", "muted": True},
        {"type": "speak", "text": "line two", "muted": True, "buffer": "activity"},
    ]
