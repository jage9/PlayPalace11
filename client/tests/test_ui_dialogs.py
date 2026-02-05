from dataclasses import dataclass

import pytest
import wx

from ui.login_dialog import LoginDialog
from ui.server_manager import AccountEditorDialog


class StubConfigManager:
    def __init__(self):
        self.servers = {
            "srv-1": {
                "name": "Localhost",
                "accounts": {
                    "acct-1": {
                        "username": "alice",
                        "password": "secret",
                        "email": "alice@example.com",
                        "notes": "admin",
                    }
                },
            },
            "srv-2": {"name": "Production", "accounts": {}},
        }
        self.last_server = "srv-1"
        self.last_account = "acct-1"
        self.add_calls = []
        self.update_calls = []

    def get_all_servers(self):
        return self.servers

    def get_server_accounts(self, server_id):
        return self.servers[server_id]["accounts"]

    def get_last_server_id(self):
        return self.last_server

    def get_last_account_id(self, server_id):
        return self.last_account if server_id == self.last_server else None

    def add_account(self, server_id, username, password, email="", notes=""):
        self.add_calls.append(
            (server_id, {"username": username, "password": password, "email": email, "notes": notes})
        )
        return "acct-new"

    def update_account(self, server_id, account_id, **kwargs):
        self.update_calls.append((server_id, account_id, kwargs))

    def get_account_by_id(self, server_id, account_id):
        return self.servers[server_id]["accounts"].get(account_id)


@pytest.fixture
def messagebox_spy(monkeypatch):
    calls = []

    def fake_messagebox(message, caption, style):
        calls.append({"message": message, "caption": caption, "style": style})
        return wx.ID_OK

    monkeypatch.setattr(wx, "MessageBox", fake_messagebox)
    return calls


def test_login_dialog_populates_servers(wx_app, monkeypatch):
    stub = StubConfigManager()
    monkeypatch.setattr("ui.login_dialog.ConfigManager", lambda: stub)

    dlg = LoginDialog(None)
    try:
        assert dlg.server_combo.GetCount() == len(stub.servers)
        assert dlg.accounts_list.GetCount() == len(
            stub.servers[stub.last_server]["accounts"]
        )
        # selecting server without accounts should clear list
        dlg.server_combo.SetSelection(1)
        dlg.on_server_change(wx.CommandEvent())
        assert dlg.accounts_list.GetCount() == 0
    finally:
        dlg.Destroy()


def test_account_editor_dialog_creates_account(wx_app):
    stub = StubConfigManager()
    dlg = AccountEditorDialog(None, stub, "srv-1")
    try:
        dlg.username_input.SetValue("newuser")
        dlg.password_input.SetValue("p@ss")
        dlg.email_input.SetValue("new@example.com")
        dlg.notes_input.SetValue("note")

        assert dlg._save_if_needed()
        assert stub.add_calls

        # Toggle password visibility
        dlg.on_show_password(wx.CommandEvent())
        assert dlg.password_plain.IsShown()
    finally:
        dlg.Destroy()


def test_account_editor_dialog_updates_existing_account(wx_app):
    stub = StubConfigManager()
    dlg = AccountEditorDialog(None, stub, "srv-1", "acct-1")
    try:
        dlg.username_input.SetValue("alice-new")
        dlg.password_input.SetValue("new-secret")
        dlg.email_input.SetValue("alice+demo@example.com")
        dlg.notes_input.SetValue("updated")

        assert dlg._save_if_needed()
        assert stub.update_calls[-1] == (
            "srv-1",
            "acct-1",
            {
                "username": "alice-new",
                "password": "new-secret",
                "email": "alice+demo@example.com",
                "notes": "updated",
            },
        )
    finally:
        dlg.Destroy()


def test_account_editor_validation_requires_username(wx_app, messagebox_spy):
    stub = StubConfigManager()
    dlg = AccountEditorDialog(None, stub, "srv-1")
    try:
        dlg.username_input.SetValue("")
        dlg.password_input.SetValue("pass")
        assert dlg._validate_for_close() is False
        assert messagebox_spy[-1]["message"] == "Username cannot be empty."
    finally:
        dlg.Destroy()


def test_account_editor_validation_requires_password(wx_app, messagebox_spy):
    stub = StubConfigManager()
    dlg = AccountEditorDialog(None, stub, "srv-1")
    try:
        dlg.username_input.SetValue("bob")
        dlg.password_input.SetValue("")
        assert dlg._validate_for_close() is False
        assert messagebox_spy[-1]["message"] == "Password cannot be empty."
    finally:
        dlg.Destroy()


def test_account_editor_validation_rejects_invalid_email(wx_app, messagebox_spy):
    stub = StubConfigManager()
    dlg = AccountEditorDialog(None, stub, "srv-1")
    try:
        dlg.username_input.SetValue("carol")
        dlg.password_input.SetValue("pass")
        dlg.email_input.SetValue("bad-email@@example.com")
        assert dlg._validate_for_close() is False
        assert messagebox_spy[-1]["message"] == "Invalid email address format."
    finally:
        dlg.Destroy()
