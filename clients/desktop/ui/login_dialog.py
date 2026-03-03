"""Login dialog for Play Palace client."""

import ssl
import threading
import urllib.request
import json
import wx
import sys
from pathlib import Path

# Add parent directory to path to import config_manager
sys.path.insert(0, str(Path(__file__).parent.parent))
from config_manager import ConfigManager


def _ws_url_to_http_url(ws_url: str) -> str | None:
    """Convert a WebSocket URL to an HTTP URL for the user count endpoint.

    Args:
        ws_url: WebSocket URL (e.g. ws://host:port or wss://host:port)

    Returns:
        HTTP URL string, or None if the URL cannot be parsed.
    """
    if not ws_url:
        return None
    lower = ws_url.lower()
    if lower.startswith("wss://"):
        return "https://" + ws_url[6:] + "/api/user_count"
    if lower.startswith("ws://"):
        return "http://" + ws_url[5:] + "/api/user_count"
    return None


def _fetch_user_count_sync(
    http_url: str, timeout: float = 3.0, trusted_cert_pem: str | None = None
) -> int | None:
    """Fetch the user count from the server over HTTP.

    For HTTPS URLs the request is first attempted with system certificate
    verification.  When that fails (e.g. a self-signed certificate), a second
    attempt is made using the PEM certificate explicitly stored as trusted for
    this server, if one is available.

    Args:
        http_url: Full HTTP URL to the user count endpoint.
        timeout: Request timeout in seconds.
        trusted_cert_pem: PEM-encoded certificate to trust, or None to use the
            system store only.

    Returns:
        Integer user count, or None if the request fails or the server is
        unreachable.
    """
    def _try_fetch(ctx) -> int | None:
        try:
            with urllib.request.urlopen(http_url, timeout=timeout, context=ctx) as resp:  # nosec B310
                data = json.loads(resp.read())
                count = data.get("user_count")
                if isinstance(count, int) and count >= 0:
                    return count
        except Exception:  # noqa: BLE001
            pass
        return None

    # First attempt: use the default SSL context (system-trusted certificates).
    default_ctx = ssl.create_default_context() if http_url.startswith("https://") else None
    result = _try_fetch(default_ctx)
    if result is not None:
        return result

    # Second attempt for HTTPS: try the explicitly trusted server certificate.
    if http_url.startswith("https://") and trusted_cert_pem:
        try:
            import tempfile
            import os
            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".pem", delete=False
            ) as f:
                f.write(trusted_cert_pem)
                tmp_path = f.name
            try:
                ctx = ssl.create_default_context(cafile=tmp_path)
                ctx.check_hostname = False
                result = _try_fetch(ctx)
            finally:
                os.unlink(tmp_path)
        except Exception:  # noqa: BLE001
            pass

    return result


class LoginDialog(wx.Dialog):
    """Login dialog with server selection and account list."""

    def __init__(self, parent=None):
        """Initialize the login dialog."""
        super().__init__(parent, title="Play Palace Login", size=(450, 380))

        # Initialize config manager
        self.config_manager = ConfigManager()

        self.username = ""
        # Placeholder for user-entered password.
        self.user_input_value = str()
        self.refresh_token = None
        self.refresh_expires_at = None
        self.server_id = None
        self.account_id = None
        self.server_url = None

        self._server_ids = []  # Track server IDs by index
        self._account_ids = []  # Track account IDs by index
        self._user_count_fetch_id = 0  # Cancels in-flight fetches on server change

        self._create_ui()
        self.CenterOnScreen()

    def _create_ui(self):
        """Create the UI components."""
        self.panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Title
        title = wx.StaticText(self.panel, label="PlayPalace 11.")
        title_font = title.GetFont()
        title_font.PointSize += 4
        title_font = title_font.Bold()
        title.SetFont(title_font)
        sizer.Add(title, 0, wx.ALL | wx.CENTER, 10)

        # Server Manager button
        self.server_manager_btn = wx.Button(self.panel, label="Server &Manager")
        sizer.Add(self.server_manager_btn, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Server selection
        server_label = wx.StaticText(self.panel, label="&Server:")
        sizer.Add(server_label, 0, wx.LEFT | wx.TOP, 10)

        self.server_combo = wx.ComboBox(
            self.panel,
            choices=[],
            style=wx.CB_READONLY | wx.CB_DROPDOWN,
        )
        sizer.Add(self.server_combo, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # User count label shown below the server combo
        self.user_count_label = wx.StaticText(self.panel, label="")
        sizer.Add(self.user_count_label, 0, wx.LEFT | wx.BOTTOM, 10)

        # User Accounts list
        accounts_label = wx.StaticText(self.panel, label="&User Account:")
        sizer.Add(accounts_label, 0, wx.LEFT | wx.TOP, 10)

        self.accounts_list = wx.ListBox(self.panel, style=wx.LB_SINGLE, size=(-1, 120))
        sizer.Add(self.accounts_list, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.login_btn = wx.Button(self.panel, wx.ID_OK, "&Login")
        self.login_btn.SetDefault()
        button_sizer.Add(self.login_btn, 0, wx.RIGHT, 5)

        self.create_account_btn = wx.Button(self.panel, label="Create &Account")
        self.create_account_btn.Hide()
        button_sizer.Add(self.create_account_btn, 0, wx.RIGHT, 5)

        cancel_btn = wx.Button(self.panel, wx.ID_CANCEL, "&Cancel")
        button_sizer.Add(cancel_btn, 0)

        sizer.Add(button_sizer, 0, wx.ALL | wx.CENTER, 10)

        # Set sizer
        self.panel.SetSizer(sizer)

        # Bind events
        self.server_manager_btn.Bind(wx.EVT_BUTTON, self.on_server_manager)
        self.server_combo.Bind(wx.EVT_COMBOBOX, self.on_server_change)
        self.login_btn.Bind(wx.EVT_BUTTON, self.on_login)
        self.create_account_btn.Bind(wx.EVT_BUTTON, self.on_create_account)
        cancel_btn.Bind(wx.EVT_BUTTON, self.on_cancel)
        self.accounts_list.Bind(wx.EVT_LISTBOX_DCLICK, self.on_login)

        # Populate servers
        self._refresh_servers_list()

        # Select last used server if available
        last_server_id = self.config_manager.get_last_server_id()
        if last_server_id and last_server_id in self._server_ids:
            idx = self._server_ids.index(last_server_id)
            self.server_combo.SetSelection(idx)
            self._refresh_accounts_list()
            self._refresh_user_count()

        # Set focus
        if self.accounts_list.GetCount() > 0:
            self.accounts_list.SetFocus()
        elif self.server_combo.GetCount() > 0:
            self.server_combo.SetFocus()
        else:
            self.server_manager_btn.SetFocus()

    def _refresh_servers_list(self):
        """Refresh the servers dropdown."""
        current_selection = self.server_combo.GetSelection()
        current_server_id = None
        if current_selection != wx.NOT_FOUND and current_selection < len(self._server_ids):
            current_server_id = self._server_ids[current_selection]

        self.server_combo.Clear()
        servers = self.config_manager.get_all_servers()
        self._server_ids = []

        for server_id, server in servers.items():
            display_name = server.get("name", "Unknown Server")
            self.server_combo.Append(display_name)
            self._server_ids.append(server_id)

        # Restore selection if possible
        if current_server_id and current_server_id in self._server_ids:
            idx = self._server_ids.index(current_server_id)
            self.server_combo.SetSelection(idx)
        elif self.server_combo.GetCount() > 0:
            self.server_combo.SetSelection(0)

        self._refresh_accounts_list()
        self._refresh_user_count()

    def _refresh_user_count(self):
        """Start a background fetch of the user count for the selected server."""
        server_id = self._get_selected_server_id()
        if not server_id:
            self.user_count_label.SetLabel("")
            return

        ws_url = self.config_manager.get_server_url(server_id)
        http_url = _ws_url_to_http_url(ws_url) if ws_url else None
        if not http_url:
            self.user_count_label.SetLabel("")
            return

        self.user_count_label.SetLabel("Fetching users...")

        # Retrieve the trusted certificate PEM (if stored) for HTTPS fallback.
        cert = self.config_manager.get_trusted_certificate(server_id)
        trusted_pem = cert.get("pem") if isinstance(cert, dict) else None

        # Increment the fetch ID so stale results from previous requests are ignored.
        self._user_count_fetch_id += 1
        fetch_id = self._user_count_fetch_id

        def _bg_fetch():
            count = _fetch_user_count_sync(http_url, trusted_cert_pem=trusted_pem)
            wx.CallAfter(self._on_user_count_result, fetch_id, count)

        threading.Thread(target=_bg_fetch, daemon=True).start()

    def _refresh_accounts_list(self):
        """Refresh the accounts list for the selected server."""
        self.accounts_list.Clear()
        self._account_ids = []

        server_id = self._get_selected_server_id()
        if not server_id:
            return

        accounts = self.config_manager.get_server_accounts(server_id)
        for account_id, account in accounts.items():
            self.accounts_list.Append(account.get("username", "Unknown"))
            self._account_ids.append(account_id)

        # Select last used account for this server, or first account if none
        last_account_id = self.config_manager.get_last_account_id(server_id)
        if last_account_id and last_account_id in self._account_ids:
            idx = self._account_ids.index(last_account_id)
            self.accounts_list.SetSelection(idx)
        elif self.accounts_list.GetCount() > 0:
            self.accounts_list.SetSelection(0)

    def _get_selected_server_id(self) -> str:
        """Get the currently selected server ID."""
        selection = self.server_combo.GetSelection()
        if selection == wx.NOT_FOUND or selection >= len(self._server_ids):
            return None
        return self._server_ids[selection]

    def _get_selected_account_id(self) -> str:
        """Get the currently selected account ID."""
        selection = self.accounts_list.GetSelection()
        if selection == wx.NOT_FOUND or selection >= len(self._account_ids):
            return None
        return self._account_ids[selection]

    def on_server_manager(self, event):
        """Handle server manager button click."""
        from .server_manager import ServerManagerDialog

        current_server_id = self._get_selected_server_id()
        dlg = ServerManagerDialog(self, self.config_manager, current_server_id)
        dlg.ShowModal()
        dlg.Destroy()
        self._refresh_servers_list()

    def on_server_change(self, event):
        """Handle server selection change."""
        self._refresh_accounts_list()
        self._refresh_user_count()

    def _on_user_count_result(self, fetch_id: int, count: int | None):
        """Update the user count label with the result of an async fetch.

        Args:
            fetch_id: ID of the fetch that produced this result (stale results are ignored).
            count: Number of logged-in users, or None if the server is unreachable.
        """
        if not self or not self.IsShown():
            return
        if fetch_id != self._user_count_fetch_id:
            return  # Stale result from a previous selection
        if count is None:
            self.user_count_label.SetLabel("unreachable")
        elif count == 1:
            self.user_count_label.SetLabel("1 user connected")
        else:
            self.user_count_label.SetLabel(f"{count} users connected")

    def on_login(self, event):
        """Handle login button click."""
        server_id = self._get_selected_server_id()
        if not server_id:
            wx.MessageBox("Please select a server", "Error", wx.OK | wx.ICON_ERROR)
            self.server_combo.SetFocus()
            return

        account_id = self._get_selected_account_id()
        if not account_id:
            wx.MessageBox("Please select an account", "Error", wx.OK | wx.ICON_ERROR)
            self.accounts_list.SetFocus()
            return

        # Get account credentials
        account = self.config_manager.get_account_by_id(server_id, account_id)
        if not account:
            wx.MessageBox("Account not found", "Error", wx.OK | wx.ICON_ERROR)
            return

        self.server_id = server_id
        self.account_id = account_id
        self.username = account.get("username", "")
        self.user_input_value = account.get("password", "")
        self.refresh_token = account.get("refresh_token")
        self.refresh_expires_at = account.get("refresh_expires_at")
        self.server_url = self.config_manager.get_server_url(server_id)

        # Save last used server and account
        self.config_manager.set_last_account(server_id, account_id)

        self.EndModal(wx.ID_OK)

    def on_create_account(self, event):
        """Handle create account button click."""
        server_id = self._get_selected_server_id()
        if not server_id:
            wx.MessageBox(
                "Please select a server first", "Error", wx.OK | wx.ICON_ERROR
            )
            self.server_combo.SetFocus()
            return

        server_url = self.config_manager.get_server_url(server_id)
        if not server_url:
            wx.MessageBox(
                "Could not determine server URL", "Error", wx.OK | wx.ICON_ERROR
            )
            return

        from .registration_dialog import RegistrationDialog

        dlg = RegistrationDialog(self, server_url, server_id=server_id)
        dlg.ShowModal()
        dlg.Destroy()

    def on_cancel(self, event):
        """Handle cancel button click."""
        self.EndModal(wx.ID_CANCEL)

    def get_credentials(self):
        """Get the login credentials."""
        return {
            "username": self.username,
            "password": self.user_input_value,
            "refresh_token": self.refresh_token,
            "refresh_expires_at": self.refresh_expires_at,
            "server_url": self.server_url,
            "server_id": self.server_id,
            "account_id": self.account_id,
            "config_manager": self.config_manager,
        }
