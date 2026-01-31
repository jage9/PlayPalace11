"""Server manager dialogs for managing servers and user accounts."""

import wx
import sys
from pathlib import Path

# Add parent directory to path to import config_manager
sys.path.insert(0, str(Path(__file__).parent.parent))
from config_manager import ConfigManager


class AccountEditorDialog(wx.Dialog):
    """Dialog for editing or creating a user account."""

    def __init__(
        self,
        parent,
        config_manager: ConfigManager,
        server_id: str,
        account_id: str = None,
    ):
        """Initialize the account editor dialog.

        Args:
            parent: Parent window
            config_manager: ConfigManager instance
            server_id: Server ID this account belongs to
            account_id: Account ID to edit, or None to create new account
        """
        title = "Edit Account" if account_id else "Add Account"
        super().__init__(parent, title=title, size=(400, 280))

        self.config_manager = config_manager
        self.server_id = server_id
        self.account_id = account_id
        self.account_data = None

        # Load existing account data if editing
        if account_id:
            self.account_data = config_manager.get_account_by_id(server_id, account_id)

        self._create_ui()
        self.CenterOnParent()

        # Bind escape key to close
        self.Bind(wx.EVT_CHAR_HOOK, self.on_key)

    def _create_ui(self):
        """Create the UI components."""
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Username
        username_label = wx.StaticText(panel, label="&Username:")
        sizer.Add(username_label, 0, wx.LEFT | wx.TOP, 10)

        username_value = ""
        if self.account_data:
            username_value = self.account_data.get("username", "")
        self.username_input = wx.TextCtrl(panel, value=username_value)
        sizer.Add(self.username_input, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Password
        password_label = wx.StaticText(panel, label="&Password:")
        sizer.Add(password_label, 0, wx.LEFT | wx.TOP, 10)

        password_value = ""
        if self.account_data:
            password_value = self.account_data.get("password", "")
        self.password_input = wx.TextCtrl(panel, value=password_value, style=wx.TE_PASSWORD)
        sizer.Add(self.password_input, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Notes
        notes_label = wx.StaticText(panel, label="&Notes:")
        sizer.Add(notes_label, 0, wx.LEFT | wx.TOP, 10)

        notes_value = ""
        if self.account_data:
            notes_value = self.account_data.get("notes", "")
        self.notes_input = wx.TextCtrl(
            panel, value=notes_value, style=wx.TE_MULTILINE, size=(-1, 60)
        )
        sizer.Add(self.notes_input, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        close_btn = wx.Button(panel, wx.ID_CANCEL, "&Close")
        button_sizer.Add(close_btn, 0)

        sizer.Add(button_sizer, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(sizer)

        # Bind events
        close_btn.Bind(wx.EVT_BUTTON, self.on_close)

        # Auto-save on field changes
        self.username_input.Bind(wx.EVT_KILL_FOCUS, self.on_field_change)
        self.password_input.Bind(wx.EVT_KILL_FOCUS, self.on_field_change)
        self.notes_input.Bind(wx.EVT_KILL_FOCUS, self.on_field_change)

        # Set focus
        self.username_input.SetFocus()

    def on_key(self, event):
        """Handle key events."""
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self._save_if_needed()
            self.EndModal(wx.ID_OK)
        else:
            event.Skip()

    def on_field_change(self, event):
        """Handle field change - auto-save."""
        self._save_if_needed()
        event.Skip()

    def _save_if_needed(self):
        """Save account data if there are changes."""
        username = self.username_input.GetValue().strip()
        password = self.password_input.GetValue()
        notes = self.notes_input.GetValue().strip()

        if not username:
            return  # Don't save without a username

        if self.account_id:
            # Update existing account
            self.config_manager.update_account(
                self.server_id,
                self.account_id,
                username=username,
                password=password,
                notes=notes,
            )
        else:
            # Create new account
            self.account_id = self.config_manager.add_account(
                self.server_id,
                username=username,
                password=password,
                notes=notes,
            )

    def on_close(self, event):
        """Handle close button click."""
        self._save_if_needed()
        self.EndModal(wx.ID_OK)

    def get_account_id(self) -> str:
        """Get the account ID (for newly created accounts)."""
        return self.account_id


class ServerEditorDialog(wx.Dialog):
    """Dialog for editing or creating a server with its accounts."""

    def __init__(
        self,
        parent,
        config_manager: ConfigManager,
        server_id: str = None,
    ):
        """Initialize the server editor dialog.

        Args:
            parent: Parent window
            config_manager: ConfigManager instance
            server_id: Server ID to edit, or None to create new server
        """
        title = "Edit Server" if server_id else "Add Server"
        super().__init__(parent, title=title, size=(450, 450))

        self.config_manager = config_manager
        self.server_id = server_id
        self.server_data = None

        # Load existing server data if editing
        if server_id:
            self.server_data = config_manager.get_server_by_id(server_id)

        self._create_ui()
        self.CenterOnParent()

        # Bind escape key to close
        self.Bind(wx.EVT_CHAR_HOOK, self.on_key)

    def _create_ui(self):
        """Create the UI components."""
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Server Name
        name_label = wx.StaticText(panel, label="Server &Name:")
        sizer.Add(name_label, 0, wx.LEFT | wx.TOP, 10)

        name_value = ""
        if self.server_data:
            name_value = self.server_data.get("name", "")
        self.name_input = wx.TextCtrl(panel, value=name_value)
        sizer.Add(self.name_input, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Host Address
        host_label = wx.StaticText(panel, label="&Host Address:")
        sizer.Add(host_label, 0, wx.LEFT | wx.TOP, 10)

        host_value = ""
        if self.server_data:
            host_value = self.server_data.get("host", "")
        self.host_input = wx.TextCtrl(panel, value=host_value)
        sizer.Add(self.host_input, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Port
        port_label = wx.StaticText(panel, label="&Port:")
        sizer.Add(port_label, 0, wx.LEFT | wx.TOP, 10)

        port_value = "8000"
        if self.server_data:
            port_value = self.server_data.get("port", "8000")
        self.port_input = wx.TextCtrl(panel, value=port_value)
        sizer.Add(self.port_input, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Notes
        notes_label = wx.StaticText(panel, label="N&otes:")
        sizer.Add(notes_label, 0, wx.LEFT | wx.TOP, 10)

        notes_value = ""
        if self.server_data:
            notes_value = self.server_data.get("notes", "")
        self.notes_input = wx.TextCtrl(
            panel, value=notes_value, style=wx.TE_MULTILINE, size=(-1, 50)
        )
        sizer.Add(self.notes_input, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Trusted certificate status
        cert_box = wx.BoxSizer(wx.HORIZONTAL)
        cert_label = wx.StaticText(panel, label="Trusted certificate:")
        cert_box.Add(cert_label, 0, wx.ALIGN_CENTER_VERTICAL)
        self.cert_status = wx.StaticText(panel, label="")
        cert_box.Add(self.cert_status, 1, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 8)
        self.forget_cert_btn = wx.Button(panel, label="Forget Certificate")
        self.forget_cert_btn.Bind(wx.EVT_BUTTON, self.on_forget_certificate)
        cert_box.Add(self.forget_cert_btn, 0)
        sizer.Add(cert_box, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10)

        # User Accounts section
        accounts_label = wx.StaticText(panel, label="&User Accounts:")
        sizer.Add(accounts_label, 0, wx.LEFT | wx.TOP, 10)

        self.accounts_list = wx.ListBox(panel, style=wx.LB_SINGLE, size=(-1, 100))
        sizer.Add(self.accounts_list, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Account buttons
        account_btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.edit_account_btn = wx.Button(panel, label="&Edit Account")
        account_btn_sizer.Add(self.edit_account_btn, 0, wx.RIGHT, 5)

        self.delete_account_btn = wx.Button(panel, label="&Delete Account")
        account_btn_sizer.Add(self.delete_account_btn, 0, wx.RIGHT, 5)

        self.add_account_btn = wx.Button(panel, label="&Add Account")
        account_btn_sizer.Add(self.add_account_btn, 0)

        sizer.Add(account_btn_sizer, 0, wx.ALL | wx.CENTER, 5)

        # Bind account button events
        self.edit_account_btn.Bind(wx.EVT_BUTTON, self.on_edit_account)
        self.delete_account_btn.Bind(wx.EVT_BUTTON, self.on_delete_account)
        self.add_account_btn.Bind(wx.EVT_BUTTON, self.on_add_account)

        # Populate accounts list
        self._account_ids = []
        self._refresh_accounts_list()
        self._refresh_certificate_status()

        # Main buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        close_btn = wx.Button(panel, wx.ID_CANCEL, "&Close")
        button_sizer.Add(close_btn, 0)

        sizer.Add(button_sizer, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(sizer)

        # Bind events
        close_btn.Bind(wx.EVT_BUTTON, self.on_close)

        # Auto-save on field changes
        self.name_input.Bind(wx.EVT_KILL_FOCUS, self.on_field_change)
        self.host_input.Bind(wx.EVT_KILL_FOCUS, self.on_field_change)
        self.port_input.Bind(wx.EVT_KILL_FOCUS, self.on_field_change)
        self.notes_input.Bind(wx.EVT_KILL_FOCUS, self.on_field_change)

        # Set focus - first account if editing existing server, otherwise name input
        if self.server_id and self.accounts_list.GetCount() > 0:
            self.accounts_list.SetSelection(0)
            self.accounts_list.SetFocus()
        else:
            self.name_input.SetFocus()

    def _refresh_accounts_list(self):
        """Refresh the accounts list."""
        if not hasattr(self, "accounts_list"):
            return

        self.accounts_list.Clear()
        self._account_ids = []

        if not self.server_id:
            return

        accounts = self.config_manager.get_server_accounts(self.server_id)

        for account_id, account in accounts.items():
            self.accounts_list.Append(account.get("username", "Unknown"))
            self._account_ids.append(account_id)

    def _refresh_certificate_status(self):
        """Update trusted certificate status text and button."""
        if not hasattr(self, "cert_status"):
            return
        if not self.server_id:
            self.cert_status.SetLabel("No server saved yet.")
            self.forget_cert_btn.Enable(False)
            return
        cert = self.config_manager.get_trusted_certificate(self.server_id)
        if cert:
            host = cert.get("host") or "unknown host"
            self.cert_status.SetLabel(f"Pinned certificate for {host}")
            self.forget_cert_btn.Enable(True)
        else:
            self.cert_status.SetLabel("No trusted certificate stored.")
            self.forget_cert_btn.Enable(False)

    def _get_selected_account_id(self) -> str:
        """Get the currently selected account ID."""
        selection = self.accounts_list.GetSelection()
        if selection == wx.NOT_FOUND:
            return None
        return self._account_ids[selection]

    def on_forget_certificate(self, event):
        """Remove stored trusted certificate for this server."""
        if not self.server_id:
            return
        confirm = wx.MessageBox(
            "Remove the trusted certificate for this server?",
            "Forget Certificate",
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING,
        )
        if confirm == wx.YES:
            self.config_manager.clear_trusted_certificate(self.server_id)
            self._refresh_certificate_status()

    def on_key(self, event):
        """Handle key events."""
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self._save_if_needed()
            self.EndModal(wx.ID_OK)
        else:
            event.Skip()

    def on_field_change(self, event):
        """Handle field change - auto-save."""
        self._save_if_needed()
        event.Skip()

    def _save_if_needed(self):
        """Save server data if there are changes."""
        name = self.name_input.GetValue().strip()
        host = self.host_input.GetValue().strip()
        port = self.port_input.GetValue().strip()
        notes = self.notes_input.GetValue().strip()

        if not name:
            return  # Don't save without a name

        if self.server_id:
            # Update existing server
            self.config_manager.update_server(
                self.server_id,
                name=name,
                host=host,
                port=port,
                notes=notes,
            )
        else:
            # Create new server
            self.server_id = self.config_manager.add_server(
                name=name,
                host=host,
                port=port,
                notes=notes,
            )
            # Reload server data
            self.server_data = self.config_manager.get_server_by_id(self.server_id)
            self._refresh_certificate_status()

    def on_edit_account(self, event):
        """Handle edit account button click."""
        if not self.server_id:
            wx.MessageBox(
                "Please save the server first", "Server Not Saved", wx.OK | wx.ICON_WARNING
            )
            return

        account_id = self._get_selected_account_id()
        if not account_id:
            wx.MessageBox(
                "Please select an account to edit", "No Selection", wx.OK | wx.ICON_WARNING
            )
            return

        dlg = AccountEditorDialog(self, self.config_manager, self.server_id, account_id)
        dlg.ShowModal()
        dlg.Destroy()
        self._refresh_accounts_list()

    def on_delete_account(self, event):
        """Handle delete account button click."""
        if not self.server_id:
            wx.MessageBox(
                "Please save the server first", "Server Not Saved", wx.OK | wx.ICON_WARNING
            )
            return

        account_id = self._get_selected_account_id()
        if not account_id:
            wx.MessageBox(
                "Please select an account to delete",
                "No Selection",
                wx.OK | wx.ICON_WARNING,
            )
            return

        account = self.config_manager.get_account_by_id(self.server_id, account_id)
        username = account.get("username", "Unknown") if account else "Unknown"

        result = wx.MessageBox(
            f"Are you sure you want to delete the account '{username}'?",
            "Confirm Delete",
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING,
        )

        if result == wx.YES:
            self.config_manager.delete_account(self.server_id, account_id)
            self._refresh_accounts_list()

    def on_add_account(self, event):
        """Handle add account button click."""
        # Save server first if needed
        if not self.server_id:
            self._save_if_needed()
            if not self.server_id:
                wx.MessageBox(
                    "Please enter a server name first", "Server Name Required", wx.OK | wx.ICON_WARNING
                )
                self.name_input.SetFocus()
                return

        dlg = AccountEditorDialog(self, self.config_manager, self.server_id)
        dlg.ShowModal()
        dlg.Destroy()
        self._refresh_accounts_list()

    def on_close(self, event):
        """Handle close button click."""
        self._save_if_needed()
        self.EndModal(wx.ID_OK)

    def get_server_id(self) -> str:
        """Get the server ID (for newly created servers)."""
        return self.server_id


class ServerManagerDialog(wx.Dialog):
    """Dialog for managing the list of servers."""

    def __init__(self, parent, config_manager: ConfigManager, initial_server_id: str = None):
        """Initialize the server manager dialog.

        Args:
            parent: Parent window
            config_manager: ConfigManager instance
            initial_server_id: Server ID to select initially
        """
        super().__init__(parent, title="Server Manager", size=(400, 350))

        self.config_manager = config_manager
        self._server_ids = []  # Track server IDs by index
        self._initial_server_id = initial_server_id

        self._create_ui()
        self.CenterOnParent()

        # Bind escape key to close
        self.Bind(wx.EVT_CHAR_HOOK, self.on_key)

    def _create_ui(self):
        """Create the UI components."""
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Servers label
        servers_label = wx.StaticText(panel, label="&Servers:")
        sizer.Add(servers_label, 0, wx.LEFT | wx.TOP, 10)

        # Servers list
        self.servers_list = wx.ListBox(panel, style=wx.LB_SINGLE, size=(-1, 180))
        sizer.Add(self.servers_list, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Server buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.edit_btn = wx.Button(panel, label="&Edit Server")
        button_sizer.Add(self.edit_btn, 0, wx.RIGHT, 5)

        self.delete_btn = wx.Button(panel, label="&Delete Server")
        button_sizer.Add(self.delete_btn, 0, wx.RIGHT, 5)

        self.add_btn = wx.Button(panel, label="&Add Server")
        button_sizer.Add(self.add_btn, 0)

        sizer.Add(button_sizer, 0, wx.ALL | wx.CENTER, 10)

        # Close button
        close_sizer = wx.BoxSizer(wx.HORIZONTAL)
        close_btn = wx.Button(panel, wx.ID_CANCEL, "&Close")
        close_sizer.Add(close_btn, 0)
        sizer.Add(close_sizer, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(sizer)

        # Bind events
        self.edit_btn.Bind(wx.EVT_BUTTON, self.on_edit_server)
        self.delete_btn.Bind(wx.EVT_BUTTON, self.on_delete_server)
        self.add_btn.Bind(wx.EVT_BUTTON, self.on_add_server)
        close_btn.Bind(wx.EVT_BUTTON, self.on_close)
        self.servers_list.Bind(wx.EVT_LISTBOX_DCLICK, self.on_edit_server)

        # Populate servers list
        self._refresh_servers_list()

    def _refresh_servers_list(self):
        """Refresh the servers list."""
        self.servers_list.Clear()
        servers = self.config_manager.get_all_servers()
        self._server_ids = []

        for server_id, server in servers.items():
            display_name = server.get("name", "Unknown Server")
            self.servers_list.Append(display_name)
            self._server_ids.append(server_id)

        # Select initial server if specified
        if self._initial_server_id and self._initial_server_id in self._server_ids:
            idx = self._server_ids.index(self._initial_server_id)
            self.servers_list.SetSelection(idx)

    def _get_selected_server_id(self) -> str:
        """Get the currently selected server ID."""
        selection = self.servers_list.GetSelection()
        if selection == wx.NOT_FOUND:
            return None
        return self._server_ids[selection]

    def on_key(self, event):
        """Handle key events."""
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_OK)
        else:
            event.Skip()

    def on_edit_server(self, event):
        """Handle edit server button click."""
        server_id = self._get_selected_server_id()
        if not server_id:
            wx.MessageBox(
                "Please select a server to edit", "No Selection", wx.OK | wx.ICON_WARNING
            )
            return

        dlg = ServerEditorDialog(self, self.config_manager, server_id)
        dlg.ShowModal()
        dlg.Destroy()
        self._refresh_servers_list()

    def on_delete_server(self, event):
        """Handle delete server button click."""
        server_id = self._get_selected_server_id()
        if not server_id:
            wx.MessageBox(
                "Please select a server to delete",
                "No Selection",
                wx.OK | wx.ICON_WARNING,
            )
            return

        server = self.config_manager.get_server_by_id(server_id)
        server_name = server.get("name", "Unknown Server") if server else "Unknown Server"

        result = wx.MessageBox(
            f"Are you sure you want to delete the server '{server_name}' and all its accounts?",
            "Confirm Delete",
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING,
        )

        if result == wx.YES:
            self.config_manager.delete_server(server_id)
            self._refresh_servers_list()

    def on_add_server(self, event):
        """Handle add server button click."""
        dlg = ServerEditorDialog(self, self.config_manager)
        dlg.ShowModal()
        dlg.Destroy()
        self._refresh_servers_list()

    def on_close(self, event):
        """Handle close button click."""
        self.EndModal(wx.ID_OK)
