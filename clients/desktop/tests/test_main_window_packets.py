import types

import pytest

from ui import main_window as main_mod


class StubMenuList:
    def __init__(self):
        self.items = []
        self.selection = main_mod.wx.NOT_FOUND
        self.client_data = {}
        self.multiletter = True
        self.grid = (False, 1)

    def Clear(self):
        self.items.clear()
        self.selection = main_mod.wx.NOT_FOUND

    def Append(self, text):
        self.items.append(text)

    def GetCount(self):
        return len(self.items)

    def GetString(self, index):
        return self.items[index]

    def SetString(self, index, text):
        self.items[index] = text

    def Delete(self, index):
        del self.items[index]

    def Insert(self, text, index):
        self.items.insert(index, text)

    def SetSelection(self, index):
        self.selection = index

    def GetSelection(self):
        return self.selection

    def SetClientData(self, index, data):
        self.client_data[index] = data

    def enable_multiletter_navigation(self, enabled):
        self.multiletter = enabled

    def enable_grid_mode(self, enabled, grid_width):
        self.grid = (enabled, grid_width)

    def SetFocus(self):
        pass

    def Hide(self):
        pass

    def Show(self):
        pass


@pytest.fixture(autouse=True)
def no_focus(monkeypatch):
    class DummyWindow:
        @classmethod
        def FindFocus(cls):
            return None

    monkeypatch.setattr(main_mod.wx, "Window", DummyWindow)


def make_window():
    window = main_mod.MainWindow.__new__(main_mod.MainWindow)
    window.menu_list = StubMenuList()
    window.chat_input = object()
    window.history_text = object()
    window.speaker = types.SimpleNamespace(speak=lambda *args, **kwargs: None)
    window.sound_manager = types.SimpleNamespace(
        remove_all_playlists=lambda: window.sound_events.append("remove"),
        stop_music=lambda fade=True: window.sound_events.append(f"stop_music:{fade}"),
        stop_ambience=lambda force=False: window.sound_events.append(f"stop_ambience:{force}"),
    )
    window.sound_events = []
    window.network = types.SimpleNamespace(send_packet=lambda packet: window.sent_packets.append(packet))
    window.sent_packets = []
    window.buffer_system = types.SimpleNamespace()
    window.current_mode = "list"
    window.current_menu_id = None
    window.current_menu_state = None
    window.current_menu_item_ids = []
    window.switch_to_list_mode = lambda: setattr(window, "current_mode", "list")
    window.switch_to_edit_mode = lambda *args, **kwargs: None
    window.set_multiletter_navigation = main_mod.MainWindow.set_multiletter_navigation.__get__(window)
    window.set_grid_mode = main_mod.MainWindow.set_grid_mode.__get__(window)
    window.on_server_clear_ui = main_mod.MainWindow.on_server_clear_ui.__get__(window)
    window.on_server_menu = main_mod.MainWindow.on_server_menu.__get__(window)
    window.on_server_request_input = main_mod.MainWindow.on_server_request_input.__get__(window)
    window.on_server_clear_ui = main_mod.MainWindow.on_server_clear_ui.__get__(window)
    window.switch_to_edit_mode_calls = []

    def fake_switch_to_edit_mode(prompt, callback, default, multiline, read_only):
        window.switch_to_edit_mode_calls.append(
            {
                "prompt": prompt,
                "default": default,
                "multiline": multiline,
                "read_only": read_only,
                "callback": callback,
            }
        )

    window.switch_to_edit_mode = fake_switch_to_edit_mode
    return window


def test_on_server_menu_builds_new_menu():
    window = make_window()
    packet = {
        "menu_id": "main",
        "items": [
            {"text": "Play", "id": "play", "sound": "click.ogg"},
            {"text": "Options", "id": "options"},
        ],
        "position": 1,
        "multiletter_enabled": False,
        "grid_enabled": True,
        "grid_width": 2,
    }

    window.on_server_menu(packet)

    assert window.menu_list.items == ["Play", "Options"]
    assert window.menu_list.selection == 1
    assert window.menu_list.client_data[0] == {"sound": "click.ogg"}
    assert window.current_menu_id == "main"
    assert window.menu_list.multiletter is False
    assert window.menu_list.grid == (True, 2)


def test_on_server_menu_diff_updates_existing_items():
    window = make_window()
    window.current_menu_id = "main"
    window.current_menu_state = {"menu_id": "main", "items": ["Play", "Options"]}
    window.current_menu_item_ids = ["play", "options"]
    window.menu_list.items = ["Play", "Options"]
    window.menu_list.selection = 0

    packet = {
        "menu_id": "main",
        "items": [
            {"text": "Play", "id": "play"},
            {"text": "Quit", "id": "quit"},
        ],
        "selection_id": "quit",
    }

    window.on_server_menu(packet)

    assert window.menu_list.items == ["Play", "Quit"]
    assert window.menu_list.selection == 1


def test_on_server_request_input_switches_to_edit_mode_and_sends_packet():
    window = make_window()
    packet = {
        "type": "request_input",
        "prompt": "Enter name",
        "input_id": "invite",
        "default_value": "Alice",
        "multiline": True,
        "read_only": False,
    }

    window.on_server_request_input(packet)

    assert window.switch_to_edit_mode_calls
    call = window.switch_to_edit_mode_calls[-1]
    assert call["prompt"] == "Enter name"
    assert call["default"] == "Alice"
    assert call["multiline"] is True
    callback = call["callback"]
    callback("hello")
    assert window.sent_packets[-1] == {"type": "editbox", "text": "hello", "input_id": "invite"}


def test_on_server_clear_ui_resets_menu_and_audio():
    window = make_window()
    window.menu_list.items = ["A"]
    window.current_mode = "edit"

    window.on_server_clear_ui({})

    assert window.menu_list.items == []
    assert window.current_menu_id is None
    assert window.current_mode == "list"
    assert window.sound_events == ["remove", "stop_music:True", "stop_ambience:False"]


def test_on_server_status_records_last_message():
    window = make_window()
    packet = {
        "type": "server_status",
        "mode": "maintenance",
        "message": "Server maintenance in progress.",
        "resume_at": "2026-02-07T18:00:00Z",
        "retry_after": 120,
    }

    window.on_server_status(packet)

    assert window.last_server_status_packet == packet
    assert "Server maintenance in progress" in window.last_status_announcement
