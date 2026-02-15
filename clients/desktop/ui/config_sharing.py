"""Config sharing dialog for importing and exporting server profiles.

Provides a single dialog that handles both import and export operations,
plus pure data helper functions for building export data, matching servers,
detecting account changes, and managing notes.
"""

import copy
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from config_schemas import ExportedIdentities, OptionsProfile, Server

# ========== Data Helpers ==========


def build_export_server(server_dict: dict, include_accounts: bool, include_options: bool) -> dict:
    """Build an export-ready copy of a server dict.

    Deep-copies the server, clears accounts/options if not included,
    and always clears trusted_certificate and last_account_id.
    Server IDs and account IDs are kept.
    """
    result = copy.deepcopy(server_dict)
    if not include_accounts:
        result["accounts"] = {}
    if not include_options:
        result["options_profile"] = OptionsProfile().model_dump()
    result["trusted_certificate"] = None
    result["last_account_id"] = None
    return result


def match_servers(imported_servers: list, existing_servers: dict) -> dict:
    """Map imported server index to existing server_id by matching host.

    Args:
        imported_servers: List of imported server dicts.
        existing_servers: Dict mapping server_id to server dict (from config manager).

    Returns:
        Dict mapping imported list index to existing server_id, or None if new.
    """
    # Build lookup: lowercase host -> server_id
    host_to_id = {}
    for server_id, server in existing_servers.items():
        host_lower = server.get("host", "").lower()
        if host_lower:
            host_to_id[host_lower] = server_id

    result = {}
    for i, imp_server in enumerate(imported_servers):
        imp_host = imp_server.get("host", "").lower()
        result[i] = host_to_id.get(imp_host)
    return result


def find_changed_accounts(
    imported_accounts: dict, existing_accounts: dict
) -> Tuple[List[dict], List[dict]]:
    """Find new and changed accounts by matching username.

    Notes are excluded from comparison. Returns changed field names.

    Args:
        imported_accounts: Dict mapping account_id to account dict (from import).
        existing_accounts: Dict mapping account_id to account dict (from config).

    Returns:
        Tuple of (new_accounts, changed_accounts) where:
        - new_accounts: list of imported account dicts with no username match
        - changed_accounts: list of dicts with keys: imported, existing, changed_fields
    """
    # Build existing username lookup (case-insensitive)
    existing_by_username = {}
    for acct_id, acct in existing_accounts.items():
        username_lower = acct.get("username", "").lower()
        if username_lower:
            existing_by_username[username_lower] = (acct_id, acct)

    new_accounts = []
    changed_accounts = []
    compare_fields = ("password", "email")

    for imp_id, imp_acct in imported_accounts.items():
        imp_username = imp_acct.get("username", "").lower()
        match = existing_by_username.get(imp_username)
        if match is None:
            new_accounts.append(imp_acct)
        else:
            existing_id, existing_acct = match
            changed_fields = []
            for field in compare_fields:
                if imp_acct.get(field, "") != existing_acct.get(field, ""):
                    changed_fields.append(field)
            if changed_fields:
                changed_accounts.append({
                    "imported": imp_acct,
                    "existing": existing_acct,
                    "existing_id": existing_id,
                    "changed_fields": changed_fields,
                })

    return new_accounts, changed_accounts


def has_meaningful_changes(imported_server: dict, existing_server: dict) -> bool:
    """Check if an imported server has anything meaningful to import for an existing server.

    True if there are new/changed accounts, non-default options, or name/port differs.
    """
    if server_info_differs(imported_server, existing_server):
        return True
    if has_options_profile_data(imported_server):
        return True
    # Check accounts
    new_accts, changed_accts = find_changed_accounts(
        imported_server.get("accounts", {}),
        existing_server.get("accounts", {}),
    )
    if new_accts or changed_accts:
        return True
    return False


def server_info_differs(imported: dict, existing: dict) -> bool:
    """Compare name and port only between imported and existing server."""
    if imported.get("name", "") != existing.get("name", ""):
        return True
    if imported.get("port", 8000) != existing.get("port", 8000):
        return True
    return False


def build_server_info_display(imported: dict, existing: dict) -> str:
    """Build multiline comparison text for server info differences."""
    lines = []
    imp_name = imported.get("name", "")
    ext_name = existing.get("name", "")
    if imp_name != ext_name:
        lines.append(f"Name: {ext_name} -> {imp_name}")
    imp_port = imported.get("port", 8000)
    ext_port = existing.get("port", 8000)
    if imp_port != ext_port:
        lines.append(f"Port: {ext_port} -> {imp_port}")
    return "\n".join(lines)


def append_imported_notes(existing_notes: str, imported_notes: str, description: str, timestamp: int) -> str:
    """Append imported notes with a header.

    If imported_notes is empty, returns existing_notes unchanged.
    """
    if not imported_notes:
        return existing_notes
    date_str = format_export_timestamp(timestamp)
    header = f"Imported Notes From Export ({description}, {date_str}):"
    parts = []
    if existing_notes:
        parts.append(existing_notes)
    parts.append(f"{header}\n{imported_notes}")
    return "\n\n".join(parts)


def has_options_profile_data(server_dict: dict) -> bool:
    """True if the server's options_profile differs from defaults."""
    defaults = OptionsProfile().model_dump()
    current = server_dict.get("options_profile", defaults)
    return current != defaults


def try_load_export_file(path: str) -> Optional[dict]:
    """Load and validate an export JSON file.

    Returns:
        Parsed dict if valid, None if invalid.
    """
    try:
        with open(path, "r") as f:
            data = json.load(f)
        ExportedIdentities.model_validate(data)
        return data
    except Exception:
        return None


def format_export_timestamp(timestamp: int) -> str:
    """Format a unix timestamp as a human-readable date string."""
    try:
        dt = datetime.fromtimestamp(timestamp)
        return dt.strftime("%B %d, %Y at %I:%M %p")
    except (OSError, ValueError, OverflowError):
        return "Unknown date"


# ========== Dialogs ==========

import wx
from .enhance_wx import audio_events
from config_manager import ConfigManager


class AccountConflictDialog(wx.Dialog):
    """Prompt for resolving an account conflict during import."""

    RESULT_UPDATE = "update"
    RESULT_SKIP = "skip"
    RESULT_UPDATE_ALL = "update_all"
    RESULT_SKIP_ALL = "skip_all"

    def __init__(self, parent, username: str, server_name: str, changed_fields: list):
        super().__init__(parent, title="Account Conflict", size=(400, 250))
        self.result = self.RESULT_SKIP

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        fields_str = ", ".join(changed_fields)
        msg = (
            f"The account '{username}' on server '{server_name}' "
            f"has different values for: {fields_str}.\n\n"
            f"What would you like to do?"
        )
        label = wx.StaticText(panel, label=msg)
        label.Wrap(370)
        sizer.Add(label, 0, wx.ALL, 10)

        update_btn = wx.Button(panel, label="&Update")
        update_btn.Bind(wx.EVT_BUTTON, lambda e: self._finish(self.RESULT_UPDATE))
        sizer.Add(update_btn, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        skip_btn = wx.Button(panel, label="&Skip")
        skip_btn.Bind(wx.EVT_BUTTON, lambda e: self._finish(self.RESULT_SKIP))
        sizer.Add(skip_btn, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        update_all_btn = wx.Button(panel, label=f'Update &all for server "{server_name}"')
        update_all_btn.Bind(wx.EVT_BUTTON, lambda e: self._finish(self.RESULT_UPDATE_ALL))
        sizer.Add(update_all_btn, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        skip_all_btn = wx.Button(panel, label=f'S&kip all for server "{server_name}"')
        skip_all_btn.Bind(wx.EVT_BUTTON, lambda e: self._finish(self.RESULT_SKIP_ALL))
        sizer.Add(skip_all_btn, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        panel.SetSizer(sizer)
        self.CenterOnParent()
        update_btn.SetFocus()

    def _finish(self, result: str):
        self.result = result
        self.EndModal(wx.ID_OK)

    def get_result(self) -> str:
        return self.result


class ConfigSharingDialog(wx.Dialog, audio_events.SoundBindingsMixin):
    """Dialog for importing or exporting server profiles."""

    MODE_EXPORT = "export"
    MODE_IMPORT = "import"

    # Included type identifiers
    TYPE_ACCOUNTS = "user_accounts"
    TYPE_OPTIONS = "option_profiles"
    TYPE_SERVER_INFO = "server_info_updates"

    def __init__(
        self,
        parent,
        config_manager: ConfigManager,
        mode: str,
        imported_data: Optional[dict] = None,
    ):
        title = "Export Server Profiles" if mode == self.MODE_EXPORT else "Import Server Profiles"
        super().__init__(parent, title=title, size=(500, 450))

        self.config_manager = config_manager
        self.mode = mode
        self.imported_data = imported_data
        self._user_interacted = False
        self._no_data = False

        # Build server data for the dialog
        self._server_data = []  # List of dicts with metadata per server
        self._per_server_state = {}  # index -> {accounts: bool, options: bool, update_info: bool}
        self._build_server_data()

        self._create_ui()
        self.CenterOnParent()
        self.Bind(wx.EVT_CHAR_HOOK, self._on_key)

    def _build_server_data(self):
        """Build the list of servers and their metadata for the dialog."""
        existing_servers = self.config_manager.get_all_servers()

        if self.mode == self.MODE_EXPORT:
            for server_id, server in existing_servers.items():
                accounts = server.get("accounts", {})
                self._server_data.append({
                    "server_id": server_id,
                    "server_dict": server,
                    "name": server.get("name", "Unknown"),
                    "account_count": len(accounts),
                    "has_options": has_options_profile_data(server),
                    "is_new": False,
                    "info_differs": False,
                    "existing_id": server_id,
                })
        else:
            # Import mode
            imported_servers = self.imported_data.get("servers", [])
            matches = match_servers(imported_servers, existing_servers)

            for i, imp_server in enumerate(imported_servers):
                existing_id = matches.get(i)
                is_new = existing_id is None
                accounts = imp_server.get("accounts", {})
                info_differs = False
                account_count = len(accounts)

                if not is_new:
                    existing_server = existing_servers[existing_id]
                    # Filter out existing servers with no meaningful changes
                    if not has_meaningful_changes(imp_server, existing_server):
                        continue
                    info_differs = server_info_differs(imp_server, existing_server)
                    new_accts, changed_accts = find_changed_accounts(
                        accounts, existing_server.get("accounts", {}),
                    )
                    account_count = len(new_accts) + len(changed_accts)

                self._server_data.append({
                    "index": i,
                    "server_dict": imp_server,
                    "name": imp_server.get("name", "Unknown"),
                    "account_count": account_count,
                    "has_options": has_options_profile_data(imp_server),
                    "is_new": is_new,
                    "info_differs": info_differs,
                    "existing_id": existing_id,
                })

            if not self._server_data:
                self._no_data = True

        # Initialize per-server state (all unchecked by default)
        for i in range(len(self._server_data)):
            state = {"accounts": False, "options": False}
            if self.mode == self.MODE_IMPORT:
                state["update_info"] = False
            self._per_server_state[i] = state

    def _create_ui(self):
        """Create all UI components."""
        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Import mode: server filter radio box
        if self.mode == self.MODE_IMPORT:
            filter_box = wx.StaticBox(panel, label="Filters")
            filter_sizer = wx.StaticBoxSizer(filter_box, wx.VERTICAL)

            self._server_filter = wx.RadioBox(
                panel,
                label="&Server filter",
                choices=["All", "Existing only", "New only"],
                majorDimension=1,
                style=wx.RA_SPECIFY_ROWS,
            )
            self._server_filter.Bind(wx.EVT_RADIOBOX, self._on_server_filter_changed)
            filter_sizer.Add(self._server_filter, 0, wx.EXPAND | wx.ALL, 5)
        else:
            filter_box = wx.StaticBox(panel, label="Filters")
            filter_sizer = wx.StaticBoxSizer(filter_box, wx.VERTICAL)

        # Included types checklistbox
        type_label = "E&xport types" if self.mode == self.MODE_EXPORT else "I&mport types"
        self._type_items = []
        self._type_keys = []
        # Dynamic items based on what data exists
        any_accounts = any(s["account_count"] > 0 for s in self._server_data)
        any_options = any(s["has_options"] for s in self._server_data)
        any_info_differs = any(s.get("info_differs", False) for s in self._server_data)

        if any_accounts:
            self._type_items.append("User accounts")
            self._type_keys.append(self.TYPE_ACCOUNTS)
        if any_options:
            self._type_items.append("Option profiles")
            self._type_keys.append(self.TYPE_OPTIONS)
        if self.mode == self.MODE_IMPORT and any_info_differs:
            self._type_items.append("Server info updates")
            self._type_keys.append(self.TYPE_SERVER_INFO)

        types_label = wx.StaticText(panel, label=type_label)
        filter_sizer.Add(types_label, 0, wx.LEFT | wx.TOP, 5)
        self._types_list = wx.CheckListBox(panel, choices=self._type_items)
        # All checked by default
        for i in range(len(self._type_items)):
            self._types_list.Check(i, True)
        self._types_list.Bind(wx.EVT_CHECKLISTBOX, self._on_type_toggled)
        if self._types_list.GetCount() > 0:
            self._types_list.SetSelection(0)
        filter_sizer.Add(self._types_list, 0, wx.EXPAND | wx.ALL, 5)

        main_sizer.Add(filter_sizer, 0, wx.EXPAND | wx.ALL, 5)

        # Details section
        details_box = wx.StaticBox(panel, label="Details")
        details_sizer = wx.StaticBoxSizer(details_box, wx.VERTICAL)

        # Available servers checklistbox
        servers_label = wx.StaticText(panel, label="&Available servers")
        details_sizer.Add(servers_label, 0, wx.LEFT | wx.TOP, 5)

        self._servers_list = wx.CheckListBox(panel, choices=[], size=(-1, 120))
        self._servers_list.Bind(wx.EVT_CHECKLISTBOX, self._on_server_checked)
        self._servers_list.Bind(wx.EVT_LISTBOX, self._on_server_selection_changed)
        details_sizer.Add(self._servers_list, 1, wx.EXPAND | wx.ALL, 5)

        # Empty list message (multiline so screen readers can focus it)
        self._empty_list_msg = wx.TextCtrl(
            panel,
            value="",
            style=wx.TE_MULTILINE | wx.TE_READONLY,
            size=(-1, 30),
        )
        self._empty_list_msg.Hide()
        details_sizer.Add(self._empty_list_msg, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        # Server panel
        self._server_panel = wx.Panel(panel)
        self._panel_sizer = wx.BoxSizer(wx.VERTICAL)

        # "Server not included" message (multiline so screen readers can focus it)
        self._not_included_label = wx.TextCtrl(
            self._server_panel,
            value="Server not included",
            style=wx.TE_MULTILINE | wx.TE_READONLY,
            size=(-1, 30),
        )
        self._not_included_label.SetName("Server not included")

        # Accounts checkbox
        self._accounts_cb = wx.CheckBox(self._server_panel, label="Add &user accounts")
        self._accounts_cb.Bind(wx.EVT_CHECKBOX, self._on_account_cb_changed)

        # Options checkbox
        self._options_cb = wx.CheckBox(self._server_panel, label="Add options &profile")
        self._options_cb.Bind(wx.EVT_CHECKBOX, self._on_options_cb_changed)

        # Import-only: server info display and update checkbox
        if self.mode == self.MODE_IMPORT:
            self._info_text = wx.TextCtrl(
                self._server_panel,
                style=wx.TE_MULTILINE | wx.TE_READONLY,
                size=(-1, 50),
            )
            self._info_text.SetName("Server info changes")
            self._update_info_cb = wx.CheckBox(self._server_panel, label="Update server &info")
            self._update_info_cb.Bind(wx.EVT_CHECKBOX, self._on_update_info_cb_changed)

        self._panel_sizer.Add(self._not_included_label, 0, wx.ALL, 5)
        self._panel_sizer.Add(self._accounts_cb, 0, wx.ALL, 5)
        self._panel_sizer.Add(self._options_cb, 0, wx.ALL, 5)
        if self.mode == self.MODE_IMPORT:
            self._panel_sizer.Add(self._info_text, 0, wx.EXPAND | wx.ALL, 5)
            self._panel_sizer.Add(self._update_info_cb, 0, wx.ALL, 5)

        self._server_panel.SetSizer(self._panel_sizer)
        details_sizer.Add(self._server_panel, 0, wx.EXPAND | wx.ALL, 5)

        main_sizer.Add(details_sizer, 1, wx.EXPAND | wx.ALL, 5)

        # Operation section
        op_box = wx.StaticBox(panel, label="Operation")
        op_sizer = wx.StaticBoxSizer(op_box, wx.HORIZONTAL)

        start_label = "Start &export" if self.mode == self.MODE_EXPORT else "Start &import"
        self._start_btn = wx.Button(panel, label=start_label)
        self._start_btn.Bind(wx.EVT_BUTTON, self._on_start)
        op_sizer.Add(self._start_btn, 0, wx.ALL, 5)

        self._cancel_btn = wx.Button(panel, wx.ID_CANCEL, "&Cancel")
        self._cancel_btn.Bind(wx.EVT_BUTTON, self._on_cancel)
        op_sizer.Add(self._cancel_btn, 0, wx.ALL, 5)

        main_sizer.Add(op_sizer, 0, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(main_sizer)

        # Populate the servers list
        self._populate_servers_list()
        # Show initial panel state
        self._refresh_server_panel()

        # Add sounds to the CheckListBox elements for accessibility
        self.bind_sounds(recursion=-1)  # don't need to bind sounds to every control
        self.bind_sfx_to_control(self._types_list, True)
        self.bind_sfx_to_control(self._servers_list, True)

        # Set initial focus
        if self.mode == self.MODE_IMPORT and hasattr(self, "_server_filter"):
            self._server_filter.SetFocus()
        elif self._type_items:
            self._types_list.SetFocus()
        else:
            self._servers_list.SetFocus()

    def _populate_servers_list(self):
        """Populate the available servers checklistbox based on current filter."""
        self._servers_list.Clear()
        self._visible_indices = []  # Maps list position -> server_data index

        filter_val = 0  # "All"
        if self.mode == self.MODE_IMPORT and hasattr(self, "_server_filter"):
            filter_val = self._server_filter.GetSelection()

        for i, sdata in enumerate(self._server_data):
            # Apply filter
            if self.mode == self.MODE_IMPORT:
                if filter_val == 1 and sdata["is_new"]:  # Existing only
                    continue
                if filter_val == 2 and not sdata["is_new"]:  # New only
                    continue

            label = sdata["name"]
            if self.mode == self.MODE_IMPORT and filter_val == 0:
                tag = "new" if sdata["is_new"] else "existing"
                label = f"{label} ({tag})"

            self._servers_list.Append(label)
            self._visible_indices.append(i)

        if self._servers_list.GetCount() == 0:
            if self.mode == self.MODE_IMPORT:
                if filter_val == 1:
                    msg = "No existing servers with changes"
                elif filter_val == 2:
                    msg = "No new servers found"
                else:
                    msg = "No servers available"
                self._empty_list_msg.SetValue(msg)
                self._empty_list_msg.SetName(msg)
                self._empty_list_msg.Show(True)
            self._servers_list.Hide()
            self._servers_list.GetParent().Layout()
            return

        self._servers_list.Show(True)
        self._empty_list_msg.Hide()
        self._servers_list.Enable(True)

        # Restore check states
        for list_pos, data_idx in enumerate(self._visible_indices):
            # A server is "checked" in the servers list if the user checked it
            # We track this via a flag in per_server_state
            checked = self._per_server_state[data_idx].get("server_checked", False)
            self._servers_list.Check(list_pos, checked)

        if self._servers_list.GetCount() > 0:
            self._servers_list.SetSelection(0)

    def _get_focused_data_index(self) -> Optional[int]:
        """Get the server_data index for the currently focused server."""
        sel = self._servers_list.GetSelection()
        if sel == wx.NOT_FOUND or sel >= len(self._visible_indices):
            return None
        return self._visible_indices[sel]

    def _show_panel_message(self, text):
        """Show a message in the server panel, hiding all other controls."""
        self._not_included_label.SetValue(text)
        self._not_included_label.SetName(text)
        self._not_included_label.Show(True)
        self._accounts_cb.Show(False)
        self._options_cb.Show(False)
        if self.mode == self.MODE_IMPORT:
            self._info_text.Show(False)
            self._update_info_cb.Show(False)
        self._server_panel.Layout()

    def _refresh_server_panel(self):
        """Refresh the server panel for the currently focused server."""
        # Hide panel entirely when no servers are visible
        if not self._visible_indices:
            self._server_panel.Show(False)
            self._server_panel.GetParent().Layout()
            return

        self._server_panel.Show(True)
        idx = self._get_focused_data_index()

        if idx is None:
            self._show_panel_message("Server not included")
            return

        sdata = self._server_data[idx]
        state = self._per_server_state[idx]
        is_checked = state.get("server_checked", False)

        if not is_checked:
            self._show_panel_message("Server not included")
            return

        # Determine which types are visible (from included types checklistbox)
        visible_types = self._get_visible_types()
        show_accounts = self.TYPE_ACCOUNTS in visible_types
        show_options = self.TYPE_OPTIONS in visible_types
        show_info = self.TYPE_SERVER_INFO in visible_types

        # Check if any control would actually be visible for this server
        any_visible = show_accounts or show_options or (
            self.mode == self.MODE_IMPORT and show_info and sdata.get("info_differs", False)
        )
        if not any_visible:
            self._show_panel_message("No included types for this server")
            return

        self._not_included_label.Show(False)

        # Accounts checkbox
        if show_accounts:
            count = sdata["account_count"]
            acct_label = f"Add &user accounts, {count} account{'s' if count != 1 else ''}"
            self._accounts_cb.SetLabel(acct_label)
            self._accounts_cb.SetValue(state["accounts"])
            self._accounts_cb.Enable(count > 0)
            self._accounts_cb.Show(True)
        else:
            self._accounts_cb.Show(False)

        # Options checkbox
        if show_options:
            if sdata["has_options"]:
                self._options_cb.SetLabel("Add options &profile")
                self._options_cb.Enable(True)
            else:
                self._options_cb.SetLabel("Add options &profile (will use defaults)")
                self._options_cb.Enable(False)
            self._options_cb.SetValue(state["options"])
            self._options_cb.Show(True)
        else:
            self._options_cb.Show(False)

        # Import-only: server info
        if self.mode == self.MODE_IMPORT:
            if show_info and sdata.get("info_differs", False):
                existing_servers = self.config_manager.get_all_servers()
                existing_server = existing_servers.get(sdata["existing_id"], {})
                display_text = build_server_info_display(sdata["server_dict"], existing_server)
                self._info_text.SetValue(display_text)
                self._info_text.Show(True)
                self._update_info_cb.SetValue(state.get("update_info", False))
                self._update_info_cb.Show(True)
            else:
                self._info_text.Show(False)
                self._update_info_cb.Show(False)

        self._server_panel.Layout()

    def _get_visible_types(self) -> list:
        """Get the list of currently visible type keys."""
        result = []
        for i in range(len(self._type_keys)):
            if self._types_list.IsChecked(i):
                result.append(self._type_keys[i])
        return result

    # ========== Event Handlers ==========

    def _on_key(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self._on_cancel(event)
        else:
            event.Skip()

    def _on_type_toggled(self, event):
        self._user_interacted = True
        self._refresh_server_panel()

    def _on_server_filter_changed(self, event):
        self._populate_servers_list()
        self._refresh_server_panel()

    def _on_server_checked(self, event):
        self._user_interacted = True
        list_pos = event.GetInt()
        if list_pos < len(self._visible_indices):
            data_idx = self._visible_indices[list_pos]
            self._per_server_state[data_idx]["server_checked"] = self._servers_list.IsChecked(list_pos)
        self._refresh_server_panel()

    def _on_server_selection_changed(self, event):
        self._refresh_server_panel()

    def _on_account_cb_changed(self, event):
        self._user_interacted = True
        idx = self._get_focused_data_index()
        if idx is not None:
            self._per_server_state[idx]["accounts"] = self._accounts_cb.GetValue()

    def _on_options_cb_changed(self, event):
        self._user_interacted = True
        idx = self._get_focused_data_index()
        if idx is not None:
            self._per_server_state[idx]["options"] = self._options_cb.GetValue()

    def _on_update_info_cb_changed(self, event):
        self._user_interacted = True
        idx = self._get_focused_data_index()
        if idx is not None:
            self._per_server_state[idx]["update_info"] = self._update_info_cb.GetValue()

    def _on_cancel(self, event):
        if self._user_interacted:
            result = wx.MessageBox(
                "Are you sure you want to cancel? Your selections will be lost.",
                "Confirm Cancel",
                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING,
                self,
            )
            if result != wx.YES:
                return
        self.EndModal(wx.ID_CANCEL)

    def _on_start(self, event):
        if self.mode == self.MODE_EXPORT:
            self._execute_export()
        else:
            self._execute_import()

    # ========== Export Flow ==========

    def _get_selected_servers(self) -> list:
        """Get list of (data_index, server_data) for all checked servers."""
        result = []
        for list_pos, data_idx in enumerate(self._visible_indices):
            if self._per_server_state[data_idx].get("server_checked", False):
                result.append((data_idx, self._server_data[data_idx]))
        return result

    def _execute_export(self):
        selected = self._get_selected_servers()
        if not selected:
            wx.MessageBox("No servers selected.", "Export", wx.OK | wx.ICON_INFORMATION, self)
            return

        # Check if any server includes accounts
        any_accounts = any(self._per_server_state[idx]["accounts"] for idx, _ in selected)
        if any_accounts:
            result = wx.MessageBox(
                "User accounts are included in this export. Are you sure you want to proceed?\n\n"
                "Some servers will ban the account owner and anyone else who attempts to access the same account.",
                "Export Warning",
                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING,
                self,
            )
            if result != wx.YES:
                return

        # Ask for description
        desc_dlg = wx.TextEntryDialog(self, "Enter a description for this export:", "Export Description")
        while True:
            if desc_dlg.ShowModal() != wx.ID_OK:
                desc_dlg.Destroy()
                return
            description = desc_dlg.GetValue().strip()
            if description:
                break
            wx.MessageBox("Description cannot be empty.", "Export", wx.OK | wx.ICON_WARNING, self)
        desc_dlg.Destroy()

        # Build export data
        timestamp = int(time.time())
        export_servers = []
        for idx, sdata in selected:
            state = self._per_server_state[idx]
            server_export = build_export_server(
                sdata["server_dict"],
                include_accounts=state["accounts"],
                include_options=state["options"],
            )
            export_servers.append(server_export)

        export_data = {
            "description": description,
            "timestamp": timestamp,
            "servers": export_servers,
        }

        # Validate with schema
        try:
            ExportedIdentities.model_validate(export_data)
        except Exception as e:
            wx.MessageBox(
                f"Export data validation failed: {e}",
                "Export Error",
                wx.OK | wx.ICON_ERROR,
                self,
            )
            return

        # Save file dialog
        file_dlg = wx.FileDialog(
            self,
            "Save Export File",
            defaultDir=str(Path.cwd()),
            defaultFile="identities-export.json",
            wildcard="JSON files (*.json)|*.json",
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
        )
        if file_dlg.ShowModal() != wx.ID_OK:
            file_dlg.Destroy()
            return
        save_path = file_dlg.GetPath()
        file_dlg.Destroy()

        # Write file
        try:
            with open(save_path, "w") as f:
                json.dump(export_data, f, indent=2)
        except Exception as e:
            wx.MessageBox(
                f"Failed to save export file: {e}",
                "Export Error",
                wx.OK | wx.ICON_ERROR,
                self,
            )
            return

        server_count = len(export_servers)
        wx.MessageBox(
            f"Successfully exported {server_count} server{'s' if server_count != 1 else ''}.",
            "Export Complete",
            wx.OK | wx.ICON_INFORMATION,
            self,
        )
        self.EndModal(wx.ID_OK)

    # ========== Import Flow ==========

    def _execute_import(self):
        selected = self._get_selected_servers()
        if not self._validate_import_selection(selected):
            return

        snapshot = copy.deepcopy(self.config_manager.identities)
        description = self.imported_data.get("description", "")
        timestamp = self.imported_data.get("timestamp", 0)
        stats = {"new_servers": 0, "updated_servers": 0, "new_accounts": 0, "updated_accounts": 0, "skipped_accounts": 0}

        try:
            self._run_import(selected, description, timestamp, stats)
            self.config_manager.save_identities()
        except Exception as e:
            self._rollback_import(snapshot, e)
            return

        self._show_import_summary(stats)
        self.EndModal(wx.ID_OK)

    def _validate_import_selection(self, selected) -> bool:
        if not selected:
            wx.MessageBox("No servers selected.", "Import", wx.OK | wx.ICON_INFORMATION, self)
            return False
        if self._has_selected_accounts(selected):
            result = wx.MessageBox(
                "User accounts are included in this import. Are you sure you want to proceed?\n\n"
                "Some servers will ban the account owner and anyone else who attempts to access the same account.",
                "Import Warning",
                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING,
                self,
            )
            if result != wx.YES:
                return False
        if self._has_selected_options(selected):
            result = wx.MessageBox(
                "Option profiles will overwrite your existing settings. Do you want to proceed?",
                "Import Warning",
                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING,
                self,
            )
            if result != wx.YES:
                return False
        return True

    def _has_selected_accounts(self, selected) -> bool:
        return any(self._per_server_state[idx]["accounts"] for idx, _ in selected)

    def _has_selected_options(self, selected) -> bool:
        return any(self._per_server_state[idx]["options"] for idx, _ in selected)

    def _run_import(self, selected, description: str, timestamp: int, stats: dict) -> None:
        for idx, sdata in selected:
            state = self._per_server_state[idx]
            imp_server = sdata["server_dict"]
            is_new = sdata["is_new"]

            if is_new:
                self._import_new_server(imp_server, state, description, timestamp, stats)
            else:
                self._import_existing_server(sdata, state, description, timestamp, stats)

    def _rollback_import(self, snapshot, error: Exception) -> None:
        self.config_manager.identities = snapshot
        self.config_manager.save_identities()
        wx.MessageBox(
            f"Import failed and changes were rolled back: {error}",
            "Import Error",
            wx.OK | wx.ICON_ERROR,
            self,
        )

    def _show_import_summary(self, stats: dict) -> None:
        parts = []
        if stats["new_servers"]:
            parts.append(f"{stats['new_servers']} new server{'s' if stats['new_servers'] != 1 else ''}")
        if stats["updated_servers"]:
            parts.append(f"{stats['updated_servers']} updated server{'s' if stats['updated_servers'] != 1 else ''}")
        if stats["new_accounts"]:
            parts.append(f"{stats['new_accounts']} new account{'s' if stats['new_accounts'] != 1 else ''}")
        if stats["updated_accounts"]:
            parts.append(f"{stats['updated_accounts']} updated account{'s' if stats['updated_accounts'] != 1 else ''}")
        if stats["skipped_accounts"]:
            parts.append(f"{stats['skipped_accounts']} skipped account{'s' if stats['skipped_accounts'] != 1 else ''}")

        summary = "Imported " + ", ".join(parts) + "." if parts else "No changes were made."
        wx.MessageBox(summary, "Import Complete", wx.OK | wx.ICON_INFORMATION, self)

    def _import_new_server(self, imp_server: dict, state: dict, description: str, timestamp: int, stats: dict):
        """Import a completely new server."""
        notes = imp_server.get("notes", "")
        server_id = self.config_manager.add_server(
            name=imp_server.get("name", ""),
            host=imp_server.get("host", ""),
            port=imp_server.get("port", 8000),
            notes=notes,
        )
        stats["new_servers"] += 1

        # Add accounts if included
        if state["accounts"]:
            for acct_id, acct in imp_server.get("accounts", {}).items():
                self.config_manager.add_account(
                    server_id,
                    username=acct.get("username", ""),
                    password=acct.get("password", ""),
                    email=acct.get("email", ""),
                    notes=acct.get("notes", ""),
                )
                stats["new_accounts"] += 1

        # Set options profile if included
        if state["options"] and has_options_profile_data(imp_server):
            server = self.config_manager.get_server_by_id(server_id)
            if server:
                server["options_profile"] = copy.deepcopy(imp_server.get("options_profile", {}))

    def _import_existing_server(self, sdata: dict, state: dict, description: str, timestamp: int, stats: dict):
        """Import data into an existing server."""
        imp_server = sdata["server_dict"]
        existing_id = sdata["existing_id"]
        existing_server = self.config_manager.get_server_by_id(existing_id)
        if not existing_server:
            return

        updated = False

        # Update server info if requested
        if state.get("update_info", False) and sdata.get("info_differs", False):
            new_name = imp_server.get("name")
            new_port = imp_server.get("port")
            new_notes = append_imported_notes(
                existing_server.get("notes", ""),
                imp_server.get("notes", ""),
                description,
                timestamp,
            )
            self.config_manager.update_server(
                existing_id,
                name=new_name,
                port=new_port,
                notes=new_notes,
            )
            updated = True

        # Process accounts if included
        if state["accounts"]:
            existing_accounts = self.config_manager.get_server_accounts(existing_id)
            new_accts, changed_accts = find_changed_accounts(
                imp_server.get("accounts", {}),
                existing_accounts,
            )

            # Add new accounts silently
            for acct in new_accts:
                self.config_manager.add_account(
                    existing_id,
                    username=acct.get("username", ""),
                    password=acct.get("password", ""),
                    email=acct.get("email", ""),
                    notes=acct.get("notes", ""),
                )
                stats["new_accounts"] += 1

            # Handle changed accounts with conflict prompt
            server_name = existing_server.get("name", "Unknown")
            update_all = False
            skip_all = False

            for change in changed_accts:
                if skip_all:
                    stats["skipped_accounts"] += 1
                    continue
                if update_all:
                    self._apply_account_update(
                        existing_id, change, description, timestamp
                    )
                    stats["updated_accounts"] += 1
                    continue

                # Show conflict dialog
                dlg = AccountConflictDialog(
                    self,
                    change["imported"].get("username", ""),
                    server_name,
                    change["changed_fields"],
                )
                dlg.ShowModal()
                result = dlg.get_result()
                dlg.Destroy()

                if result == AccountConflictDialog.RESULT_UPDATE:
                    self._apply_account_update(existing_id, change, description, timestamp)
                    stats["updated_accounts"] += 1
                elif result == AccountConflictDialog.RESULT_SKIP:
                    stats["skipped_accounts"] += 1
                elif result == AccountConflictDialog.RESULT_UPDATE_ALL:
                    update_all = True
                    self._apply_account_update(existing_id, change, description, timestamp)
                    stats["updated_accounts"] += 1
                elif result == AccountConflictDialog.RESULT_SKIP_ALL:
                    skip_all = True
                    stats["skipped_accounts"] += 1

            if new_accts or changed_accts:
                updated = True

        # Set options profile if included (full replacement)
        if state["options"] and has_options_profile_data(imp_server):
            existing_server["options_profile"] = copy.deepcopy(
                imp_server.get("options_profile", {})
            )
            updated = True

        if updated:
            stats["updated_servers"] += 1

    def _apply_account_update(self, server_id: str, change: dict, description: str, timestamp: int):
        """Apply an account update from import data."""
        existing_id = change["existing_id"]
        imp_acct = change["imported"]
        existing_acct = change["existing"]

        # Build update kwargs
        kwargs = {}
        for field in change["changed_fields"]:
            kwargs[field] = imp_acct.get(field, "")

        # Handle notes
        new_notes = append_imported_notes(
            existing_acct.get("notes", ""),
            imp_acct.get("notes", ""),
            description,
            timestamp,
        )
        kwargs["notes"] = new_notes

        self.config_manager.update_account(server_id, existing_id, **kwargs)
