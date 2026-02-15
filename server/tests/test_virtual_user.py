"""Tests for the VirtualUser helper class."""

from server.core.users.virtual_user import VirtualUser
from server.core.users.base import MenuItem, TrustLevel, generate_virtual_bot_uuid


def test_virtual_user_deterministic_uuid_and_flags():
    user = VirtualUser("GuideBot", locale="es")

    assert user.uuid == generate_virtual_bot_uuid("GuideBot")
    assert user.username == "GuideBot"
    assert user.locale == "es"
    assert user.is_bot and user.is_virtual_bot
    assert user.approved
    assert user.trust_level == TrustLevel.USER
    assert user.get_queued_messages() == []


def test_virtual_user_tracks_menu_state_and_clear():
    user = VirtualUser("Navigator")
    menu_items = ["play", MenuItem(text="Settings", id="settings")]

    user.show_menu("main", menu_items)
    assert user.current_menu_id == "main"
    assert user.current_menu_items == menu_items

    user.update_menu("main", ["hosts"])
    assert user.current_menu_items == ["hosts"]

    user.update_menu("other", ["ignored"])
    assert user.current_menu_items == ["hosts"]

    user.remove_menu("main")
    assert user.current_menu_id is None
    assert user.current_menu_items == []

    user.show_menu("lobby", ["tables"])
    assert user.current_menu_id == "lobby"

    user.clear_ui()
    assert user.current_menu_id is None
    assert user.current_menu_items == []
