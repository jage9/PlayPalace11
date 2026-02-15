"""Server manager dialogs for managing servers and user accounts."""

import re
import wx
import sys
from pathlib import Path

# Add parent directory to path to import config_manager
sys.path.insert(0, str(Path(__file__).parent.parent))
from config_manager import ConfigManager
from ui.config_sharing import (
    ConfigSharingDialog,
    try_load_export_file,
    format_export_timestamp,
)


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
        super().__init__(parent, title=title, size=(400, 330))

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

        password_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Placeholder for user-entered password.
        password_value = ""  # nosec B105
        if self.account_data:
            password_value = self.account_data.get("password", "")

        # Create both masked and plain text controls for password
        self.password_input = wx.TextCtrl(panel, value=password_value, style=wx.TE_PASSWORD)
        self.password_input.SetName("Password")
        self.password_plain = wx.TextCtrl(panel, value=password_value)
        self.password_plain.SetName("Password")
        self.password_plain.Hide()

        password_sizer.Add(self.password_input, 1, wx.RIGHT, 5)
        password_sizer.Add(self.password_plain, 1, wx.RIGHT, 5)

        self.show_password_btn = wx.Button(panel, label="&Show Password")
        password_sizer.Add(self.show_password_btn, 0)

        sizer.Add(password_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Email
        email_label = wx.StaticText(panel, label="&Email:")
        sizer.Add(email_label, 0, wx.LEFT | wx.TOP, 10)

        email_value = ""
        if self.account_data:
            email_value = self.account_data.get("email", "")
        self.email_input = wx.TextCtrl(panel, value=email_value)
        sizer.Add(self.email_input, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

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
        self.show_password_btn.Bind(wx.EVT_BUTTON, self.on_show_password)
        close_btn.Bind(wx.EVT_BUTTON, self.on_close)

        # Auto-save on field changes
        self.username_input.Bind(wx.EVT_KILL_FOCUS, self.on_field_change)
        self.password_input.Bind(wx.EVT_KILL_FOCUS, self.on_field_change)
        self.password_plain.Bind(wx.EVT_KILL_FOCUS, self.on_field_change)
        self.email_input.Bind(wx.EVT_KILL_FOCUS, self.on_field_change)
        self.notes_input.Bind(wx.EVT_KILL_FOCUS, self.on_field_change)

        # Set focus
        self.username_input.SetFocus()

    def on_key(self, event):
        """Handle key events."""
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            if not self._validate_for_close():
                return
            self._save_if_needed()
            self.EndModal(wx.ID_OK)
        else:
            event.Skip()

    def on_show_password(self, event):
        """Toggle password visibility."""
        if self.password_input.IsShown():
            # Switch to plain text (show password)
            current_value = self.password_input.GetValue()
            self.password_plain.SetValue(current_value)
            self.password_input.Hide()
            self.password_plain.Show()
            self.show_password_btn.SetLabel("&Hide Password")
            self.password_plain.SetFocus()
        else:
            # Switch to masked (hide password)
            current_value = self.password_plain.GetValue()
            self.password_input.SetValue(current_value)
            self.password_plain.Hide()
            self.password_input.Show()
            self.show_password_btn.SetLabel("&Show")
            self.password_input.SetFocus()

        self.password_input.GetParent().Layout()

    def on_field_change(self, event):
        """Handle field change - auto-save."""
        self._save_if_needed()
        event.Skip()

    def _get_password_value(self) -> str:
        """Get the current password value from whichever control is visible."""
        if self.password_input.IsShown():
            return self.password_input.GetValue()
        else:
            return self.password_plain.GetValue()

    def _validate_email(self, email: str) -> bool:
        """Validate email address format.

        Args:
            email: Email address to validate

        Returns:
            True if valid (empty or valid format), False otherwise
        """
        if not email:
            return True  # Empty is allowed
        # Lowercase and validate against pattern
        email_lower = email.lower()
        pattern = r'^[a-z0-9_.+-]+@[a-z0-9_.-]+$'
        return bool(re.match(pattern, email_lower))

    def _validate_for_close(self) -> bool:
        """Validate all fields before closing.

        Validates in display order: username, password, email.

        Returns:
            True if all fields are valid, False otherwise
        """
        username = self.username_input.GetValue().strip()
        password = self._get_password_value()
        email = self.email_input.GetValue().strip()

        # Validate username
        if not username:
            wx.MessageBox(
                "Username cannot be empty.",
                "Validation Error",
                wx.OK | wx.ICON_ERROR,
            )
            self.username_input.SetFocus()
            return False

        # Validate password
        if not password:
            wx.MessageBox(
                "Password cannot be empty.",
                "Validation Error",
                wx.OK | wx.ICON_ERROR,
            )
            # Focus the visible password field
            if self.password_input.IsShown():
                self.password_input.SetFocus()
            else:
                self.password_plain.SetFocus()
            return False

        # Validate email
        if not self._validate_email(email):
            wx.MessageBox(
                "Invalid email address format.",
                "Validation Error",
                wx.OK | wx.ICON_ERROR,
            )
            self.email_input.SetFocus()
            return False

        return True

    def _save_if_needed(self) -> bool:
        """Save account data if there are changes.

        Returns:
            True if saved successfully or no save needed, False if validation failed
        """
        username = self.username_input.GetValue().strip()
        password = self._get_password_value()
        email = self.email_input.GetValue().strip().lower()
        notes = self.notes_input.GetValue().strip()

        if not username:
            return True  # Don't save without a username, but not an error

        if not self._validate_email(email):
            return False  # Validation failed

        if self.account_id:
            # Update existing account
            self.config_manager.update_account(
                self.server_id,
                self.account_id,
                username=username,
                password=password,
                email=email,
                notes=notes,
            )
        else:
            # Create new account
            self.account_id = self.config_manager.add_account(
                self.server_id,
                username=username,
                password=password,
                email=email,
                notes=notes,
            )
        return True

    def on_close(self, event):
        """Handle close button click."""
        if not self._validate_for_close():
            return
        self._save_if_needed()
        self.EndModal(wx.ID_OK)

    def get_account_id(self) -> str:
        """Get the account ID (for newly created accounts)."""
        return self.account_id


class TrustedCertificateDialog(wx.Dialog):
    """Dialog for viewing and managing trusted certificates."""

    def __init__(
        self,
        parent,
        config_manager: ConfigManager,
        server_id: str,
    ):
        """Initialize the trusted certificate dialog.

        Args:
            parent: Parent window
            config_manager: ConfigManager instance
            server_id: Server ID to view certificate for
        """
        super().__init__(parent, title="Trusted Certificate", size=(450, 300))

        self.config_manager = config_manager
        self.server_id = server_id

        self._create_ui()
        self.CenterOnParent()

        # Bind escape key to close
        self.Bind(wx.EVT_CHAR_HOOK, self.on_key)

    def _create_ui(self):
        """Create the UI components."""
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Certificate details label
        details_label = wx.StaticText(panel, label="Certificate &Details:")
        sizer.Add(details_label, 0, wx.LEFT | wx.TOP, 10)

        # Certificate details text field
        self.details_text = wx.TextCtrl(
            panel,
            style=wx.TE_MULTILINE | wx.TE_READONLY,
            size=(-1, 150),
        )
        sizer.Add(self.details_text, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Populate certificate details
        self._refresh_certificate_details()

        # Buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.forget_btn = wx.Button(panel, label="&Forget Certificate")
        self.forget_btn.Bind(wx.EVT_BUTTON, self.on_forget_certificate)
        button_sizer.Add(self.forget_btn, 0, wx.RIGHT, 5)

        close_btn = wx.Button(panel, wx.ID_CANCEL, "&Close")
        close_btn.Bind(wx.EVT_BUTTON, self.on_close)
        button_sizer.Add(close_btn, 0)

        sizer.Add(button_sizer, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(sizer)

        # Update forget button state
        self._update_forget_button_state()

    def _refresh_certificate_details(self):
        """Refresh the certificate details text."""
        if not self.server_id:
            self.details_text.SetValue("No server saved yet.")
            return

        cert = self.config_manager.get_trusted_certificate(self.server_id)
        if not cert:
            self.details_text.SetValue("No trusted certificate stored.")
            return

        # Build certificate details text
        details = []
        if cert.get("host"):
            details.append(f"Host: {cert['host']}")
        if cert.get("common_name"):
            details.append(f"Common Name: {cert['common_name']}")
        if cert.get("fingerprint"):
            details.append(f"Fingerprint: {cert['fingerprint']}")
        if cert.get("pem"):
            details.append("")
            details.append("PEM Certificate:")
            details.append(cert["pem"])

        self.details_text.SetValue("\n".join(details) if details else "Certificate data unavailable.")

    def _update_forget_button_state(self):
        """Enable/disable forget button based on certificate existence."""
        if not self.server_id:
            self.forget_btn.Enable(False)
            return
        cert = self.config_manager.get_trusted_certificate(self.server_id)
        self.forget_btn.Enable(cert is not None)

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
            self._refresh_certificate_details()
            self._update_forget_button_state()

    def on_key(self, event):
        """Handle key events."""
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_OK)
        else:
            event.Skip()

    def on_close(self, event):
        """Handle close button click."""
        self.EndModal(wx.ID_OK)


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

        # Options Profile button
        self.options_profile_btn = wx.Button(panel, label="&Options Profile")
        self.options_profile_btn.Bind(wx.EVT_BUTTON, self.on_options_profile)
        sizer.Add(self.options_profile_btn, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)

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

        port_value = 8000
        if self.server_data:
            port_value = self.server_data.get("port", 8000)
        self.port_input = wx.TextCtrl(panel, value=str(port_value))
        sizer.Add(self.port_input, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Trusted certificate button
        self.cert_btn = wx.Button(panel, label="&Trusted Certificate")
        self.cert_btn.Bind(wx.EVT_BUTTON, self.on_trusted_certificate)
        sizer.Add(self.cert_btn, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)

        # Notes
        notes_label = wx.StaticText(panel, label="&Notes:")
        sizer.Add(notes_label, 0, wx.LEFT | wx.TOP, 10)

        notes_value = ""
        if self.server_data:
            notes_value = self.server_data.get("notes", "")
        self.notes_input = wx.TextCtrl(
            panel, value=notes_value, style=wx.TE_MULTILINE, size=(-1, 50)
        )
        sizer.Add(self.notes_input, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Close button
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

        # Set focus - options profile if editing existing server, otherwise name input
        if self.server_id:
            self.options_profile_btn.SetFocus()
            if self.accounts_list.GetCount() > 0:
                self.accounts_list.SetSelection(0)
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

        # Select first item if nothing is selected
        if self.accounts_list.GetSelection() == wx.NOT_FOUND and self.accounts_list.GetCount() > 0:
            self.accounts_list.SetSelection(0)

    def _get_selected_account_id(self) -> str:
        """Get the currently selected account ID."""
        selection = self.accounts_list.GetSelection()
        if selection == wx.NOT_FOUND:
            return None
        return self._account_ids[selection]

    def on_trusted_certificate(self, event):
        """Open the trusted certificate dialog."""
        if not self.server_id:
            # Save server first if needed
            self._save_if_needed()
            if not self.server_id:
                wx.MessageBox(
                    "Please enter a server name first.",
                    "Server Name Required",
                    wx.OK | wx.ICON_WARNING,
                )
                self.name_input.SetFocus()
                return

        dlg = TrustedCertificateDialog(self, self.config_manager, self.server_id)
        dlg.ShowModal()
        dlg.Destroy()

    def on_options_profile(self, event):
        """Handle options profile button click."""
        wx.MessageBox(
            "Not implemented yet.",
            "Options Profile",
            wx.OK | wx.ICON_INFORMATION,
        )

    def on_key(self, event):
        """Handle key events."""
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            if not self._validate_for_close():
                return
            self._save_if_needed()
            self.EndModal(wx.ID_OK)
        else:
            event.Skip()

    def on_field_change(self, event):
        """Handle field change - auto-save."""
        self._save_if_needed()
        event.Skip()

    def _validate_for_close(self) -> bool:
        """Validate all fields before closing.

        Validates in display order: name, host, port.
        Notes is optional.

        Returns:
            True if all fields are valid, False otherwise
        """
        name = self.name_input.GetValue().strip()
        host = self.host_input.GetValue().strip()
        port = self.port_input.GetValue().strip()

        # Validate server name
        if not name:
            wx.MessageBox(
                "Server name cannot be empty.",
                "Validation Error",
                wx.OK | wx.ICON_ERROR,
            )
            self.name_input.SetFocus()
            return False

        # Validate host address
        if not host:
            wx.MessageBox(
                "Host address cannot be empty.",
                "Validation Error",
                wx.OK | wx.ICON_ERROR,
            )
            self.host_input.SetFocus()
            return False

        # Validate port
        if not port:
            wx.MessageBox(
                "Port cannot be empty.",
                "Validation Error",
                wx.OK | wx.ICON_ERROR,
            )
            self.port_input.SetFocus()
            return False

        try:
            port_num = int(port)
            if port_num < 1000 or port_num > 65535:
                wx.MessageBox(
                    "Port must be between 1000 and 65535.",
                    "Validation Error",
                    wx.OK | wx.ICON_ERROR,
                )
                self.port_input.SetFocus()
                return False
        except ValueError:
            wx.MessageBox(
                "Port must be a valid number.",
                "Validation Error",
                wx.OK | wx.ICON_ERROR,
            )
            self.port_input.SetFocus()
            return False

        return True

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
                port=int(port),
                notes=notes,
            )
        else:
            # Create new server
            self.server_id = self.config_manager.add_server(
                name=name,
                host=host,
                port=int(port),
                notes=notes,
            )
            # Reload server data
            self.server_data = self.config_manager.get_server_by_id(self.server_id)

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
        if not self._validate_for_close():
            return
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

        # Default options profile button
        self.default_options_btn = wx.Button(panel, label="Default &Options Profile")
        self.default_options_btn.Bind(wx.EVT_BUTTON, self.on_default_options_profile)
        sizer.Add(self.default_options_btn, 0, wx.LEFT | wx.RIGHT, 10)

        # Import/Export buttons
        sharing_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.import_btn = wx.Button(panel, label="&Import Server Profiles")
        self.import_btn.Bind(wx.EVT_BUTTON, self._on_import_profiles)
        sharing_sizer.Add(self.import_btn, 0, wx.RIGHT, 5)

        self.export_btn = wx.Button(panel, label="E&xport Server Profiles")
        self.export_btn.Bind(wx.EVT_BUTTON, self._on_export_profiles)
        sharing_sizer.Add(self.export_btn, 0)
        sizer.Add(sharing_sizer, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)

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
        # Otherwise select first item if nothing is selected
        elif self.servers_list.GetSelection() == wx.NOT_FOUND and self.servers_list.GetCount() > 0:
            self.servers_list.SetSelection(0)

    def _get_selected_server_id(self) -> str:
        """Get the currently selected server ID."""
        selection = self.servers_list.GetSelection()
        if selection == wx.NOT_FOUND:
            return None
        return self._server_ids[selection]

    def on_default_options_profile(self, event):
        """Handle default options profile button click."""
        wx.MessageBox(
            "Not implemented yet.",
            "Default Options Profile",
            wx.OK | wx.ICON_INFORMATION,
        )

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

    def _on_export_profiles(self, event):
        """Handle export server profiles button click."""
        servers = self.config_manager.get_all_servers()
        if not servers:
            wx.MessageBox(
                "No servers to export.",
                "Export",
                wx.OK | wx.ICON_INFORMATION,
            )
            return

        dlg = ConfigSharingDialog(
            self, self.config_manager, ConfigSharingDialog.MODE_EXPORT
        )
        dlg.ShowModal()
        dlg.Destroy()

    def _on_import_profiles(self, event):
        """Handle import server profiles button click."""
        imported_data = self._load_import_file()
        if imported_data is None:
            return

        dlg = ConfigSharingDialog(
            self, self.config_manager, ConfigSharingDialog.MODE_IMPORT,
            imported_data=imported_data,
        )
        if dlg._no_data:
            dlg.Destroy()
            wx.MessageBox(
                "There is no data to import. All servers in this file either already "
                "exist with no changes, or the file contains no servers.",
                "Nothing to Import",
                wx.OK | wx.ICON_INFORMATION,
            )
            return

        result = dlg.ShowModal()
        dlg.Destroy()

        if result == wx.ID_OK:
            # Refresh servers list, preserving selection index
            prev_idx = self.servers_list.GetSelection()
            self._refresh_servers_list()
            if self.servers_list.GetCount() > 0:
                new_idx = min(prev_idx, self.servers_list.GetCount() - 1)
                if new_idx >= 0:
                    self.servers_list.SetSelection(new_idx)

    def _load_import_file(self):
        """Load an import file, with auto-detection and browser fallback.

        Returns:
            Parsed dict if a valid file was loaded, or None to abort.
        """
        auto_path = Path.cwd() / "identities-export.json"

        # Auto-detect file in cwd
        if auto_path.exists():
            data = try_load_export_file(str(auto_path))
            if data:
                desc = data.get("description", "")
                ts = format_export_timestamp(data.get("timestamp", 0))
                result = wx.MessageBox(
                    f"Found export file in current directory.\n\n"
                    f"Description: {desc}\n"
                    f"Date: {ts}\n\n"
                    f"Would you like to load this file?",
                    "Import Server Profiles",
                    wx.YES_NO | wx.ICON_QUESTION,
                )
                if result == wx.YES:
                    return data

        # File browser loop
        while True:
            file_dlg = wx.FileDialog(
                self,
                "Select Export File to Import",
                defaultDir=str(Path.cwd()),
                wildcard="JSON files (*.json)|*.json",
                style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
            )
            if file_dlg.ShowModal() != wx.ID_OK:
                file_dlg.Destroy()
                return None
            chosen_path = file_dlg.GetPath()
            file_dlg.Destroy()

            data = try_load_export_file(chosen_path)
            if data is None:
                wx.MessageBox(
                    "The selected file is not a valid export file.",
                    "Invalid File",
                    wx.OK | wx.ICON_ERROR,
                )
                continue

            # Confirm file details
            desc = data.get("description", "")
            ts = format_export_timestamp(data.get("timestamp", 0))
            result = wx.MessageBox(
                f"Description: {desc}\n"
                f"Date: {ts}\n\n"
                f"Would you like to import this file?",
                "Confirm Import File",
                wx.YES_NO | wx.ICON_QUESTION,
            )
            if result == wx.YES:
                return data
            # If No, return to file browser

    def on_close(self, event):
        """Handle close button click."""
        self.EndModal(wx.ID_OK)
