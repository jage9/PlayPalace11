"""Focused tests for menu, preference, and chat flows in core.server.Server."""

from types import SimpleNamespace
import json

import pytest

from server.core.server import Server
from server.core.users.network_user import NetworkUser
from server.core.users.base import TrustLevel
from server.core.users.preferences import DiceKeepingStyle
from server.messages.localization import Localization


class DummyConnection:
    def __init__(self):
        self.sent = []

    async def send(self, payload):
        self.sent.append(payload)


def make_network_user(name="Player", locale="en", trust=TrustLevel.USER, approved=True):
    user = NetworkUser(name, locale, DummyConnection(), approved=approved)
    user.set_trust_level(trust)
    user.set_approved(approved)
    return user


@pytest.fixture
def server(tmp_path):
    db_path = tmp_path / "menu.db"
    srv = Server(db_path=str(db_path), locales_dir="locales", config_path=tmp_path / "missing.toml")
    return srv


@pytest.mark.slow
def test_show_main_menu_includes_admin_option(server):
    user = make_network_user("Admin", trust=TrustLevel.ADMIN)

    server._show_main_menu(user)

    assert server._user_states[user.username]["menu"] == "main_menu"
    menu_state = user._current_menus["main_menu"]
    admin_items = [
        item
        for item in menu_state["items"]
        if isinstance(item, dict) and item.get("id") == "administration"
    ]
    assert admin_items, "expected administration option in main menu"


@pytest.mark.asyncio
@pytest.mark.slow
async def test_handle_menu_dispatches_events_when_in_table(server):
    user = make_network_user("Alice")
    server._users[user.username] = user

    class DummyGame:
        def __init__(self, owner):
            self._users = {owner.uuid: owner}
            self.handled = []

        def get_player_by_id(self, uuid):
            return SimpleNamespace(id=uuid)

        def handle_event(self, player, packet):
            self.handled.append((player.id, packet["selection_id"]))

    class DummyTable:
        def __init__(self, game):
            self.game = game
            self.removed = []

        def remove_member(self, username):
            self.removed.append(username)

    game = DummyGame(user)
    table = DummyTable(game)
    server._tables = SimpleNamespace(find_user_table=lambda username: table)

    client = SimpleNamespace(username=user.username)
    packet = {"selection_id": "any"}

    await server._handle_menu(client, packet)

    assert game.handled == [(user.uuid, "any")]
    assert table.removed == []


@pytest.mark.asyncio
@pytest.mark.slow
async def test_handle_menu_routes_main_menu_selection(server):
    user = make_network_user("MenuFan")
    server._users[user.username] = user
    server._user_states[user.username] = {"menu": "main_menu"}
    server._tables = SimpleNamespace(find_user_table=lambda username: None)

    called = []
    server._show_options_menu = lambda target: called.append(target.username)

    client = SimpleNamespace(username=user.username)

    await server._handle_menu(client, {"selection_id": "options"})

    assert called == [user.username]


@pytest.mark.asyncio
@pytest.mark.slow
async def test_options_selection_toggles_turn_sound(server):
    user = make_network_user("Prefs")
    server._users[user.username] = user
    saved = []
    server._db = SimpleNamespace(
        update_user_preferences=lambda username, data: saved.append((username, data))
    )

    await server._handle_options_selection(user, "turn_sound")

    assert user.preferences.play_turn_sound is False
    assert saved and saved[0][0] == user.username
    payload = json.loads(saved[0][1])
    assert payload["play_turn_sound"] is False


@pytest.mark.asyncio
@pytest.mark.slow
async def test_options_selection_toggles_clear_kept(server):
    user = make_network_user("Keeper")
    server._users[user.username] = user
    saved = []
    server._db = SimpleNamespace(
        update_user_preferences=lambda username, data: saved.append((username, data))
    )

    await server._handle_options_selection(user, "clear_kept")

    assert user.preferences.clear_kept_on_roll is True
    payload = json.loads(saved[-1][1])
    assert payload["clear_kept_on_roll"] is True


@pytest.mark.slow
def test_show_dice_keeping_style_menu_marks_current(server):
    user = make_network_user("Dicey")
    user.preferences.dice_keeping_style = DiceKeepingStyle.QUENTIN_C

    server._show_dice_keeping_style_menu(user)

    menu = user._current_menus["dice_keeping_style_menu"]
    assert any(
        isinstance(item, dict)
        and item.get("id") == f"style_{DiceKeepingStyle.QUENTIN_C.value}"
        and item.get("text", "").startswith("* ")
        for item in menu["items"]
    ), "expected selected dice style to be starred"


@pytest.mark.asyncio
@pytest.mark.slow
async def test_dice_style_selection_updates_preferences(server):
    user = make_network_user("DiceSel")
    server._users[user.username] = user
    saved = []
    server._db = SimpleNamespace(
        update_user_preferences=lambda username, data: saved.append((username, data))
    )
    shown = []
    server._show_options_menu = lambda target: shown.append(target.username)

    style_value = DiceKeepingStyle.QUENTIN_C.value
    await server._handle_dice_keeping_style_selection(user, f"style_{style_value}")

    assert user.preferences.dice_keeping_style == DiceKeepingStyle.QUENTIN_C
    payload = json.loads(saved[-1][1])
    assert payload["dice_keeping_style"] == style_value
    assert shown == [user.username]


@pytest.mark.asyncio
@pytest.mark.slow
async def test_language_selection_updates_locale(server):
    user = make_network_user("Polyglot")
    server._users[user.username] = user
    updated = []
    server._db = SimpleNamespace(
        update_user_locale=lambda username, locale: updated.append((username, locale))
    )
    called = []
    server._show_options_menu = lambda target: called.append(target.username)

    await server._handle_language_selection(user, "lang_pl")

    assert user.locale == "pl"
    assert updated == [(user.username, "pl")]
    assert called == [user.username]


@pytest.mark.asyncio
@pytest.mark.slow
async def test_handle_list_online_speaks_usernames(server):
    requester = make_network_user("Requester")
    friend = make_network_user("Buddy")
    server._users = {requester.username: requester, friend.username: friend}
    server._tables = SimpleNamespace(find_user_table=lambda username: None)

    client = SimpleNamespace(username=requester.username)

    await server._handle_list_online(client)

    messages = requester.get_queued_messages()
    assert messages and messages[-1]["type"] == "speak"


@pytest.mark.asyncio
@pytest.mark.slow
async def test_handle_list_online_with_games_uses_status_box(server):
    user = make_network_user("Spectator")
    server._users[user.username] = user

    class DummyGame:
        def __init__(self):
            self._users = {user.uuid: user}
            self.calls = []

        def get_player_by_id(self, uuid):
            return SimpleNamespace(id=uuid)

        def status_box(self, player, lines):
            self.calls.append((player.id, lines))

    game = DummyGame()

    class DummyTable:
        def __init__(self, game):
            self.game = game
            self.game_type = "pig"
            self.members = []

    table = DummyTable(game)

    server._tables = SimpleNamespace(find_user_table=lambda username: table)

    client = SimpleNamespace(username=user.username)
    await server._handle_list_online_with_games(client)

    assert game.calls and game.calls[0][0] == user.uuid


@pytest.mark.asyncio
@pytest.mark.slow
async def test_handle_list_online_with_games_shows_menu_when_not_in_table(server):
    user = make_network_user("Observant")
    server._users[user.username] = user
    server._tables = SimpleNamespace(find_user_table=lambda username: None)
    shown = []
    server._show_online_users_menu = lambda target: shown.append(target.username)

    client = SimpleNamespace(username=user.username)
    await server._handle_list_online_with_games(client)

    assert shown == [user.username]


@pytest.mark.asyncio
@pytest.mark.slow
async def test_handle_chat_local_only_reaches_approved(server):
    host = make_network_user("Host")
    approved = make_network_user("ApprovedFriend")
    pending = make_network_user("Pending", approved=False)
    server._users = {
        host.username: host,
        approved.username: approved,
        pending.username: pending,
    }

    members = [SimpleNamespace(username=name) for name in server._users]

    class DummyTable:
        def __init__(self):
            self.members = members
            self.game_type = "pig"

    table = DummyTable()
    server._tables = SimpleNamespace(find_user_table=lambda username: table)

    client = SimpleNamespace(username=host.username)
    await server._handle_chat(client, {"convo": "local", "message": "hi"})

    assert approved.connection.sent and approved.connection.sent[-1]["type"] == "chat"
    assert approved.connection.sent[-1]["message"] == "hi"
    assert not pending.connection.sent


@pytest.mark.asyncio
async def test_handle_chat_local_not_in_table_reaches_lobby(server):
    host = make_network_user("Host")
    lobby_friend = make_network_user("LobbyFriend")
    in_table = make_network_user("InTable")
    pending = make_network_user("Pending", approved=False)
    server._users = {
        host.username: host,
        lobby_friend.username: lobby_friend,
        in_table.username: in_table,
        pending.username: pending,
    }

    class DummyTable:
        def __init__(self):
            self.members = [SimpleNamespace(username="InTable")]

    table = DummyTable()

    def find_user_table(username):
        return table if username == "InTable" else None

    server._tables = SimpleNamespace(find_user_table=find_user_table)

    client = SimpleNamespace(username=host.username)
    await server._handle_chat(client, {"convo": "local", "message": "hi"})

    assert lobby_friend.connection.sent
    assert lobby_friend.connection.sent[-1]["type"] == "chat"
    assert lobby_friend.connection.sent[-1]["message"] == "hi"
    assert host.connection.sent
    assert host.connection.sent[-1]["type"] == "chat"
    assert host.connection.sent[-1]["message"] == "hi"
    assert not in_table.connection.sent
    assert not pending.connection.sent


@pytest.mark.asyncio
@pytest.mark.slow
async def test_handle_chat_global_reaches_all_approved(server):
    sender = make_network_user("Sender")
    approved = make_network_user("ApprovedFriend")
    pending = make_network_user("Pending", approved=False)
    server._users = {
        sender.username: sender,
        approved.username: approved,
        pending.username: pending,
    }

    client = SimpleNamespace(username=sender.username)
    await server._handle_chat(client, {"convo": "global", "message": "wave"})

    assert sender.connection.sent and sender.connection.sent[-1]["message"] == "wave"
    assert approved.connection.sent and approved.connection.sent[-1]["message"] == "wave"
    assert not pending.connection.sent


@pytest.mark.asyncio
async def test_handle_keybind_whos_at_table_when_not_in_game(server):
    caller = make_network_user("Caller")
    lobby_friend = make_network_user("LobbyFriend")
    in_table = make_network_user("InTable")
    server._users = {
        caller.username: caller,
        lobby_friend.username: lobby_friend,
        in_table.username: in_table,
    }

    class DummyTable:
        pass

    table = DummyTable()

    def find_user_table(username):
        return table if username == "InTable" else None

    server._tables = SimpleNamespace(find_user_table=find_user_table)

    client = SimpleNamespace(username=caller.username)
    await server._handle_keybind(
        client,
        {"key": "w", "control": True},
    )

    messages = caller.get_queued_messages()
    assert messages, "expected speak message for ctrl+w"
    assert messages[-1]["type"] == "speak"
    assert "Caller" in messages[-1]["text"]
    assert "LobbyFriend" in messages[-1]["text"]
    assert "user" in messages[-1]["text"].lower()
