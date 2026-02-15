"""
Cross-platform accessible checkable list controls for wxPython.

Provides:
- AccessibleCheckListCtrl: Recommended factory for all checkable lists
- AccessibleCheckListBox: Legacy wrapper for wx.CheckListBox
- Platform-specific implementations with full screen reader support

Uses selection management from list_selection module.

Requires: wxPython

See ENHANCED_ELEMENTS_REFERENCE.md for a quick reference guide.


================================================================================
USAGE GUIDE - Which Control to Use
================================================================================

This guide is for both human developers and AI coding assistants. Follow these
rules when selecting list controls for accessible wxPython applications.


1. NON-CHECKABLE LISTS
----------------------
Use: ManagedListBox (from list_selection module)

For any list where users select items but don't need checkboxes, always use
ManagedListBox. It provides:
- Automatic selection of first item when focused with no selection
- Smart focus management after item deletion (configurable: previous/next)
- Optional auto-focus on newly added items

Example:
    from list_selection import ManagedListBox, FocusAfterDelete

    listbox = ManagedListBox(
        parent,
        choices=["Apple", "Banana", "Cherry"],
        focus_after_delete=FocusAfterDelete.PREVIOUS,
    )

Do NOT use ManagedListCtrl for simple single-column non-checkable lists.
ManagedListCtrl is only appropriate for multi-column non-checkable lists
(e.g., file browsers with Name/Size/Date columns).


2. CHECKABLE LISTS (Including Single-Column)
--------------------------------------------
Use: AccessibleCheckListCtrl (function)

For ANY list with checkboxes - whether single-column or multi-column - always
use the AccessibleCheckListCtrl() factory function. It automatically returns
the correct platform-specific implementation with full accessibility support.

Single-column checkable list (use show_header=False for clean appearance):
    checklist = AccessibleCheckListCtrl(
        parent,
        show_header=False,  # Hides column header for simple lists
        name="Settings list",  # Accessible name for screen readers
    )
    checklist.AppendColumn("Setting", ColumnWidth.FILL)
    checklist.AppendItem(["Enable dark mode"])
    checklist.AppendItem(["Show notifications"])
    checklist.CheckItem(0, True)  # Check first item

Multi-column checkable list:
    checklist = AccessibleCheckListCtrl(parent, multi_column=True, name="Package list")
    checklist.AppendColumn("Package", ColumnWidth.AUTO_CONTENT)
    checklist.AppendColumn("Version", width=80)
    checklist.AppendColumn("Status", ColumnWidth.FILL)
    checklist.AppendItem(["numpy", "1.24.0", "Installed"])
    checklist.AutoSizeColumns()

Key features:
- Cross-platform: Uses ListView on Windows, DataViewListCtrl on macOS/Linux
- Full screen reader support (NVDA, JAWS, Narrator, VoiceOver, Orca)
- Checkbox state changes are announced to assistive technology
- Selection management (same as ManagedListBox)
- SetVisibleRowCount(n) to size control to show exactly n rows


3. LEGACY/LAST RESORT: AccessibleCheckListBox
---------------------------------------------
Use: AccessibleCheckListBox (ONLY for legacy projects)

AccessibleCheckListBox wraps wx.CheckListBox with accessibility fixes, but
wx.CheckListBox has fundamental accessibility limitations on some platforms:
- Screen readers may not announce checkbox state reliably
- Toggle actions may not be properly reported
- Limited cross-platform consistency

ONLY use AccessibleCheckListBox when:
- Migrating an existing project that already uses wx.CheckListBox
- The project structure cannot accommodate the different API of AccessibleCheckListCtrl
- You need exact wx.CheckListBox API compatibility

For all new development, use AccessibleCheckListCtrl instead - even for
single-column lists. The show_header=False option provides a clean appearance
equivalent to CheckListBox while maintaining full accessibility.


4. SUMMARY TABLE
----------------
+---------------------------+--------------------------------+------------------+
| Use Case                  | Recommended Control            | Avoid            |
+---------------------------+--------------------------------+------------------+
| Simple list (no checkbox) | ManagedListBox                 | ManagedListCtrl  |
| Multi-col (no checkbox)   | ManagedListCtrl                | -                |
| Checkable (single-col)    | AccessibleCheckListCtrl        | CheckListBox     |
|                           |   with show_header=False       |                  |
| Checkable (multi-col)     | AccessibleCheckListCtrl        | -                |
| Legacy checkbox list      | AccessibleCheckListBox         | -                |
+---------------------------+--------------------------------+------------------+


5. COMMON PATTERNS
------------------

Setting accessible names (important for screen readers):
    # For ManagedListBox, use standard wx name parameter
    listbox = ManagedListBox(parent, name="Fruit selection")

    # For AccessibleCheckListCtrl, use name parameter
    checklist = AccessibleCheckListCtrl(parent, name="Package list")

Configuring focus behavior:
    # Focus previous item after deletion (default)
    control.focus_after_delete = FocusAfterDelete.PREVIOUS

    # Focus next item after deletion
    control.focus_after_delete = FocusAfterDelete.NEXT

    # Auto-focus newly added items (default)
    control.focus_after_add = FocusAfterAdd.NEW_ITEM

    # Keep focus on current item when adding
    control.focus_after_add = FocusAfterAdd.STAY

================================================================================
"""

from __future__ import annotations

import sys
from typing import Any, Protocol

import wx
import wx.dataview as dv

from .general_accessibility import AccResult, _CHILDID_SELF, notify_state_change
from .list_selection import (
    ColumnWidth,
    FocusAfterAdd,
    FocusAfterDelete,
    ListBoxSelectionManagerMixin,
    ListCtrlSelectionManagerMixin,
)


# =============================================================================
# ACCESSIBILITY HELPERS (Internal)
# =============================================================================

class CheckableWindowProtocol(Protocol):
    """Protocol for windows that support checking/selecting items."""

    def IsChecked(self, index: int) -> bool: ...
    def IsSelected(self, index: int) -> bool: ...
    def HasFocus(self) -> bool: ...
    def GetItemCount(self) -> int: ...


class CheckableListAccessible(wx.Accessible):
    """
    Accessibility implementation for checkable list controls.

    Fixes wx's incomplete accessibility support by properly reporting:
    - Role: Each item is a checkbox (ROLE_SYSTEM_CHECKBUTTON)
    - State: Checked, selected, and focused states

    Works with any window that implements IsChecked(), IsSelected(), and HasFocus().

    Note: Only works on Windows. On other platforms, SetAccessible raises NotImplementedError.
    """

    def __init__(self, window: CheckableWindowProtocol) -> None:
        super().__init__(window)

    @property
    def _window(self) -> CheckableWindowProtocol:
        """Type-safe access to the window."""
        return self.Window  # type: ignore[return-value]

    def GetRole(self, childId: int) -> AccResult:
        """Return the role of the object or child."""
        if childId == _CHILDID_SELF:
            return super().GetRole(childId)
        return (wx.ACC_OK, wx.ROLE_SYSTEM_CHECKBUTTON)

    def GetState(self, childId: int) -> AccResult:
        """Return the state of the object or child."""
        if childId == _CHILDID_SELF:
            return super().GetState(childId)

        # Convert 1-based childId to 0-based index
        index = childId - 1

        # Bounds check - accessibility system may query stale indices after deletion
        if index < 0 or index >= self._window.GetItemCount():
            return (wx.ACC_OK, wx.ACC_STATE_SYSTEM_INVISIBLE)

        # Build state flags
        states = wx.ACC_STATE_SYSTEM_SELECTABLE | wx.ACC_STATE_SYSTEM_FOCUSABLE

        if self._window.IsChecked(index):
            states |= wx.ACC_STATE_SYSTEM_CHECKED

        if self._window.IsSelected(index):
            states |= wx.ACC_STATE_SYSTEM_SELECTED
            # Assume selected item is focused when the list has focus
            # (wx doesn't expose per-item focus state)
            if self._window.HasFocus():
                states |= wx.ACC_STATE_SYSTEM_FOCUSED

        return (wx.ACC_OK, states)


# =============================================================================
# MIXINS (Internal Building Blocks)
# =============================================================================

class AccessibleCheckableMixin:
    """
    Mixin that adds accessibility support to wx.CheckListBox controls.

    LEGACY USE ONLY: This mixin is for wx.CheckListBox-based controls, which
    have inherent accessibility limitations. For new development, use
    AccessibleCheckListCtrl() instead.

    Automatically:
    - Registers a CheckableListAccessible (Windows only)
    - Notifies the accessibility system on state changes

    Usage (legacy projects only):
        class MyCheckList(AccessibleCheckableMixin, wx.CheckListBox):
            pass
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        # wx.Accessible is only implemented on Windows
        try:
            self.SetAccessible(CheckableListAccessible(self))  # type: ignore[arg-type]
        except NotImplementedError:
            pass  # Graceful fallback on non-Windows platforms
        self.Bind(wx.EVT_CHECKLISTBOX, self._on_check_changed)

    def _on_check_changed(self, evt: wx.CommandEvent) -> None:
        """Handle checkbox state change and notify accessibility system."""
        evt.Skip()
        index = evt.Selection
        notify_state_change(self.Handle, index)  # type: ignore[attr-defined]


# =============================================================================
# READY-TO-USE CONTROLS
# =============================================================================

# -----------------------------------------------------------------------------
# Checkable lists - Legacy (AccessibleCheckListBox)
# -----------------------------------------------------------------------------

class AccessibleCheckListBox(AccessibleCheckableMixin, ListBoxSelectionManagerMixin, wx.CheckListBox):
    """
    A wx.CheckListBox with proper accessibility and selection management.

    NOTE: On macOS, this class is used internally by AccessibleCheckListCtrl()
    for single-column lists because wx.CheckListBox has better VoiceOver support
    than wx.DataViewListCtrl for single-column scenarios.

    For Windows or legacy projects, consider using AccessibleCheckListCtrl()
    which provides a unified cross-platform API.

    Features:
    - Screen readers correctly announce each item as a checkbox
    - Checked/unchecked state is properly reported
    - State changes are announced when items are toggled
    - Auto-selects first item when focused with no selection
    - Maintains valid selection when items are added/removed
    - Unified API compatible with AccessibleCheckListCtrl (AppendItem, CheckItem, etc.)

    Args:
        focus_after_delete: Where to focus after deleting an item.
            FocusAfterDelete.PREVIOUS (default) or FocusAfterDelete.NEXT
        focus_after_add: Where to focus after adding an item.
            FocusAfterAdd.NEW_ITEM (default) or FocusAfterAdd.STAY
        name: Accessible name for the control (announced by screen readers)
    """

    def __init__(
        self,
        parent: wx.Window,
        id: int = wx.ID_ANY,
        pos: wx.Point = wx.DefaultPosition,
        size: wx.Size = wx.DefaultSize,
        choices: list[str] | None = None,
        style: int = 0,
        focus_after_delete: FocusAfterDelete = FocusAfterDelete.PREVIOUS,
        focus_after_add: FocusAfterAdd = FocusAfterAdd.NEW_ITEM,
        name: str = "",
        **kwargs: Any,
    ) -> None:
        if choices is None:
            choices = []
        super().__init__(
            parent, id, pos, size, choices, style,
            focus_after_delete=focus_after_delete,
            focus_after_add=focus_after_add,
            **kwargs
        )
        if name:
            self.SetName(name)

    # -------------------------------------------------------------------------
    # Unified API (compatible with AccessibleCheckListCtrl)
    # -------------------------------------------------------------------------

    def AppendColumn(self, heading: str, width: int | ColumnWidth = ColumnWidth.AUTO_CONTENT) -> None:
        """No-op for single-column CheckListBox (column is implicit)."""
        pass

    def AutoSizeColumns(self, use_header: bool = False) -> None:
        """No-op for CheckListBox (no columns to size)."""
        pass

    def SetVisibleRowCount(self, rows: int) -> None:
        """Set control height to show approximately this many rows."""
        rows = max(1, rows)
        dc = wx.ClientDC(self)
        dc.SetFont(self.GetFont())
        row_height = dc.GetTextExtent("Tg")[1] + 4
        total_height = (rows * row_height) + 4
        current_size = self.GetSize()
        self.SetMinSize(wx.Size(current_size.width, total_height))
        self.SetSize(wx.Size(current_size.width, total_height))

    def AppendItem(self, values: list[str], checked: bool = False) -> int:
        """Append an item to the list (unified API)."""
        text = values[0] if values else ""
        index = self.Append(text)
        if checked:
            self.Check(index, True)
        return index

    def GetItemCount(self) -> int:
        """Return the number of items in the list."""
        return self.GetCount()

    def GetItemText(self, row: int, col: int = 0) -> str:
        """Get the text value at the specified row."""
        return self.GetString(row)

    def SetItemText(self, row: int, col: int, value: str) -> None:
        """Set the text value at the specified row."""
        self.SetString(row, value)

    def DeleteItem(self, row: int) -> bool:
        """Delete an item from the list (unified API)."""
        self.Delete(row)
        return True

    def DeleteAllItems(self) -> bool:
        """Delete all items from the list (unified API)."""
        self.Clear()
        return True

    def CheckItem(self, row: int, check: bool = True) -> None:
        """Set the checkbox state for an item (unified API)."""
        self.Check(row, check)

    def GetSelection(self) -> int:
        """Return the index of the selected item, or -1 if none."""
        sel = super().GetSelection()
        return sel if sel != wx.NOT_FOUND else -1

    def SetSelection(self, row: int) -> None:
        """Select the item at the given row."""
        super().SetSelection(row)


# -----------------------------------------------------------------------------
# Checkable lists - Recommended (AccessibleCheckListCtrl)
# -----------------------------------------------------------------------------

def AccessibleCheckListCtrl(
    parent: wx.Window,
    id: int = wx.ID_ANY,
    pos: wx.Point = wx.DefaultPosition,
    size: wx.Size = wx.DefaultSize,
    focus_after_delete: FocusAfterDelete = FocusAfterDelete.PREVIOUS,
    focus_after_add: FocusAfterAdd = FocusAfterAdd.NEW_ITEM,
    name: str = "",
    show_header: bool = True,
    multi_column: bool = False,
    **kwargs: Any,
) -> _WindowsCheckListCtrl | _DataViewCheckListCtrl | AccessibleCheckListBox:
    """
    Create a cross-platform checkable list with full accessibility support.

    RECOMMENDED: Use this for ALL checkable lists, including single-column.
    ========================================================================
    This is the preferred control for any list with checkboxes. It provides
    superior accessibility compared to wx.CheckListBox/AccessibleCheckListBox.

    For single-column checkable lists, use show_header=False for a clean
    appearance similar to CheckListBox, but with full accessibility.

    Uses wx.ListView on Windows (better screen reader support) and
    wx.DataViewListCtrl on macOS/Linux (where ListView isn't accessible).

    Features:
    - Single or multiple columns with checkboxes
    - Cross-platform accessibility (works with NVDA, JAWS, Narrator, VoiceOver, Orca)
    - Checkbox state changes properly announced to screen readers
    - Auto-selects first item when focused with no selection
    - Maintains valid selection when items are added/removed
    - Auto-sizing columns with ColumnWidth enum
    - Configurable visible row count with SetVisibleRowCount()

    Args:
        parent: Parent window
        focus_after_delete: Where to focus after deleting an item.
            FocusAfterDelete.PREVIOUS (default) or FocusAfterDelete.NEXT
        focus_after_add: Where to focus after adding an item.
            FocusAfterAdd.NEW_ITEM (default) or FocusAfterAdd.STAY
        name: Accessible name for the control (announced by screen readers).
            Always provide a meaningful name for accessibility.
        show_header: Whether to show column headers. Set to False for simple
            single-column lists where a header would look out of place.
        multi_column: Set to True when using multiple columns. On macOS/Linux,
            single-column lists (multi_column=False) use wx.CheckListBox which
            has better accessibility for single-column scenarios. Multi-column
            lists use wx.DataViewListCtrl. Default is False.

    Methods:
        AppendColumn(heading, width): Add a column. Width can be int or ColumnWidth enum.
        AppendItem(values, checked): Add a row with optional initial checked state.
        CheckItem(row, check): Set checkbox state for a row.
        IsChecked(row): Get checkbox state for a row.
        AutoSizeColumns(use_header): Resize columns to fit content.
        SetVisibleRowCount(rows): Set height to show exactly N rows.
        GetSelection() / SetSelection(row): Get/set selected row.
        DeleteItem(row) / DeleteAllItems(): Remove items.

    Usage - Single-column checkable list (preferred over CheckListBox):
        settings = AccessibleCheckListCtrl(
            parent,
            show_header=False,  # Clean appearance, no column header
            name="Settings list",
        )
        settings.AppendColumn("Setting", ColumnWidth.FILL)
        settings.AppendItem(["Enable dark mode"])
        settings.AppendItem(["Show notifications"])
        settings.CheckItem(0, True)
        settings.SetVisibleRowCount(5)

    Usage - Multi-column checkable list:
        packages = AccessibleCheckListCtrl(parent, multi_column=True, name="Package list")
        packages.AppendColumn("Name", ColumnWidth.AUTO_CONTENT)
        packages.AppendColumn("Version", width=80)
        packages.AppendColumn("Status", ColumnWidth.FILL)
        packages.AppendItem(["numpy", "1.24.0", "Installed"])
        packages.AutoSizeColumns()
    """
    if sys.platform == "win32":
        return _WindowsCheckListCtrl(parent, id, pos, size, focus_after_delete, focus_after_add, name, show_header, **kwargs)
    elif sys.platform == "darwin" and not multi_column:
        # On macOS, single-column lists use CheckListBox for better VoiceOver support
        return AccessibleCheckListBox(parent, id, pos, size, focus_after_delete=focus_after_delete, focus_after_add=focus_after_add, name=name, **kwargs)
    else:
        return _DataViewCheckListCtrl(parent, id, pos, size, focus_after_delete, focus_after_add, name, show_header, **kwargs)


# =============================================================================
# INTERNAL PLATFORM-SPECIFIC CLASSES
# =============================================================================

class _WindowsCheckListCtrl(ListCtrlSelectionManagerMixin, wx.ListView):
    """
    Windows implementation of AccessibleCheckListCtrl.

    Uses wx.ListView with EnableCheckBoxes(True) for native checkbox support.
    Do not instantiate directly - use AccessibleCheckListCtrl() instead.
    """

    def __init__(
        self,
        parent: wx.Window,
        id: int = wx.ID_ANY,
        pos: wx.Point = wx.DefaultPosition,
        size: wx.Size = wx.DefaultSize,
        focus_after_delete: FocusAfterDelete = FocusAfterDelete.PREVIOUS,
        focus_after_add: FocusAfterAdd = FocusAfterAdd.NEW_ITEM,
        name: str = "",
        show_header: bool = True,
        **kwargs: Any,
    ) -> None:
        style = wx.LC_REPORT | wx.LC_SINGLE_SEL
        if not show_header:
            style |= wx.LC_NO_HEADER
        super().__init__(parent, id, pos, size, style=style, **kwargs)
        self.EnableCheckBoxes(True)
        self._init_selection_manager(focus_after_delete, focus_after_add)
        self._column_count = 0
        self._column_widths: list[int | ColumnWidth] = []

        if name:
            self.SetName(name)

        try:
            self.SetAccessible(CheckableListAccessible(self))
        except NotImplementedError:
            pass

        self.Bind(wx.EVT_LIST_ITEM_CHECKED, self._on_item_check_changed)
        self.Bind(wx.EVT_LIST_ITEM_UNCHECKED, self._on_item_check_changed)

    def _on_item_check_changed(self, evt: wx.ListEvent) -> None:
        """Notify accessibility system when checkbox state changes."""
        evt.Skip()
        notify_state_change(self.Handle, evt.GetIndex())

    def AppendColumn(self, heading: str, width: int | ColumnWidth = ColumnWidth.AUTO_CONTENT) -> None:
        """Add a column to the list."""
        if isinstance(width, ColumnWidth):
            if width == ColumnWidth.AUTO_CONTENT:
                initial_width = wx.LIST_AUTOSIZE
            elif width == ColumnWidth.AUTO_HEADER:
                initial_width = wx.LIST_AUTOSIZE_USEHEADER
            elif width == ColumnWidth.FILL:
                initial_width = -1
            else:
                initial_width = -1
        else:
            initial_width = width

        self.InsertColumn(self._column_count, heading, width=initial_width)
        self._column_widths.append(width)
        self._column_count += 1

    def AutoSizeColumns(self, use_header: bool = False) -> None:
        """Resize all columns to fit their content."""
        for col in range(self._column_count):
            original_width = self._column_widths[col] if col < len(self._column_widths) else ColumnWidth.AUTO_CONTENT

            if isinstance(original_width, ColumnWidth) and original_width == ColumnWidth.FILL:
                total_width = self.GetClientSize().width
                other_cols_width = sum(
                    self.GetColumnWidth(c) for c in range(self._column_count) if c != col
                )
                fill_width = max(50, total_width - other_cols_width)
                self.SetColumnWidth(col, fill_width)
            elif use_header:
                self.SetColumnWidth(col, wx.LIST_AUTOSIZE_USEHEADER)
            else:
                self.SetColumnWidth(col, wx.LIST_AUTOSIZE)

    def SetVisibleRowCount(self, rows: int) -> None:
        """Set control height to show approximately this many rows."""
        rows = max(1, rows)

        if self.GetItemCount() > 0:
            item_rect = self.GetItemRect(0)
            item_height = item_rect.height
        else:
            dc = wx.ClientDC(self)
            dc.SetFont(self.GetFont())
            item_height = dc.GetTextExtent("Tg")[1] + 4

        header_height = 0
        if not (self.GetWindowStyle() & wx.LC_NO_HEADER):
            dc = wx.ClientDC(self)
            dc.SetFont(self.GetFont())
            header_height = dc.GetTextExtent("Tg")[1] + 8

        total_height = (rows * item_height) + header_height + 4

        current_size = self.GetSize()
        self.SetMinSize(wx.Size(current_size.width, total_height))
        self.SetSize(wx.Size(current_size.width, total_height))

    def AppendItem(self, values: list[str], checked: bool = False) -> int:
        """Append an item to the list."""
        was_empty = self.GetItemCount() == 0
        index = self.GetItemCount()

        wx.ListView.InsertItem(self, index, values[0] if values else "")
        for col, value in enumerate(values[1:], start=1):
            self.SetItem(index, col, value)
        if checked:
            self.CheckItem(index, True)

        if was_empty or self.focus_after_add == FocusAfterAdd.NEW_ITEM:
            self.SetSelection(index)

        return index

    def GetItemText(self, row: int, col: int = 0) -> str:
        """Get the text value at the specified row and column."""
        return super().GetItemText(row, col)

    def SetItemText(self, row: int, col: int, value: str) -> None:
        """Set the text value at the specified row and column."""
        self.SetItem(row, col, value)

    def IsChecked(self, row: int) -> bool:
        """Return True if the item at row is checked."""
        return self.IsItemChecked(row)

    def CheckItem(self, row: int, check: bool = True) -> None:
        """Set the checkbox state for an item."""
        super().CheckItem(row, check)
        notify_state_change(self.Handle, row)

    def GetSelection(self) -> int:
        """Return the index of the selected item, or -1 if none."""
        return self.GetFirstSelected()

    def SetSelection(self, row: int) -> None:
        """Select the item at the given row."""
        sel = self.GetFirstSelected()
        while sel != -1:
            self.Select(sel, False)
            sel = self.GetNextSelected(sel)
        self.Select(row, True)
        self.Focus(row)


class _DataViewCheckListCtrl(dv.DataViewListCtrl):
    """
    macOS/Linux implementation of AccessibleCheckListCtrl.

    Uses wx.DataViewListCtrl which provides accessible checkboxes on these platforms.
    Do not instantiate directly - use AccessibleCheckListCtrl() instead.
    """

    def __init__(
        self,
        parent: wx.Window,
        id: int = wx.ID_ANY,
        pos: wx.Point = wx.DefaultPosition,
        size: wx.Size = wx.DefaultSize,
        focus_after_delete: FocusAfterDelete = FocusAfterDelete.PREVIOUS,
        focus_after_add: FocusAfterAdd = FocusAfterAdd.NEW_ITEM,
        name: str = "",
        show_header: bool = True,
        **kwargs: Any,
    ) -> None:
        style = dv.DV_SINGLE
        if not show_header:
            style |= dv.DV_NO_HEADER
        super().__init__(parent, id, pos, size, style=style, **kwargs)

        self.focus_after_delete = focus_after_delete
        self.focus_after_add = focus_after_add
        self._column_count = 0
        self._column_widths: list[int | ColumnWidth] = []
        self._show_header = show_header
        self._suppress_auto_select = False

        if name:
            self.SetName(name)

        self.Bind(wx.EVT_SET_FOCUS, self._on_focus_ensure_selection)

    def _on_focus_ensure_selection(self, evt: wx.FocusEvent) -> None:
        """Auto-select first item when control gains focus with no selection."""
        evt.Skip()
        if self._suppress_auto_select:
            return
        if self.GetItemCount() > 0 and self.GetSelection() == -1:
            self.SetSelection(0)

    def AppendColumn(self, heading: str, width: int | ColumnWidth = ColumnWidth.AUTO_CONTENT) -> None:
        """Add a column to the list."""
        if isinstance(width, ColumnWidth):
            if width in (ColumnWidth.AUTO_CONTENT, ColumnWidth.AUTO_HEADER):
                initial_width = wx.COL_WIDTH_AUTOSIZE
            elif width == ColumnWidth.FILL:
                initial_width = wx.COL_WIDTH_AUTOSIZE
            else:
                initial_width = wx.COL_WIDTH_DEFAULT
        else:
            initial_width = width

        if self._column_count == 0:
            checkbox_width = 50 if isinstance(width, ColumnWidth) else width
            self.AppendToggleColumn(heading, width=checkbox_width)
        else:
            self.AppendTextColumn(heading, width=initial_width)

        self._column_widths.append(width)
        self._column_count += 1

    def AutoSizeColumns(self, use_header: bool = False) -> None:
        """Resize all columns to fit their content."""
        for col_idx in range(self._column_count):
            column = self.GetColumn(col_idx)
            if column is None:
                continue

            original_width = self._column_widths[col_idx] if col_idx < len(self._column_widths) else ColumnWidth.AUTO_CONTENT

            if isinstance(original_width, ColumnWidth) and original_width == ColumnWidth.FILL:
                total_width = self.GetClientSize().width
                other_cols_width = sum(
                    self.GetColumn(c).GetWidth() for c in range(self._column_count)
                    if c != col_idx and self.GetColumn(c) is not None
                )
                fill_width = max(50, total_width - other_cols_width)
                column.SetWidth(fill_width)
            else:
                max_width = 50

                if use_header:
                    dc = wx.ClientDC(self)
                    dc.SetFont(self.GetFont())
                    header_width = dc.GetTextExtent(column.GetTitle())[0] + 20
                    max_width = max(max_width, header_width)

                dc = wx.ClientDC(self)
                dc.SetFont(self.GetFont())
                for row in range(min(self.GetItemCount(), 100)):
                    if col_idx == 0:
                        max_width = max(max_width, 50)
                    else:
                        text = self.GetTextValue(row, col_idx)
                        text_width = dc.GetTextExtent(text)[0] + 20
                        max_width = max(max_width, text_width)

                column.SetWidth(max_width)

    def SetVisibleRowCount(self, rows: int) -> None:
        """Set control height to show approximately this many rows."""
        rows = max(1, rows)

        dc = wx.ClientDC(self)
        dc.SetFont(self.GetFont())
        row_height = dc.GetTextExtent("Tg")[1] + 8

        header_height = 0
        if self._show_header:
            header_height = dc.GetTextExtent("Tg")[1] + 12

        total_height = (rows * row_height) + header_height + 4

        current_size = self.GetSize()
        self.SetMinSize(wx.Size(current_size.width, total_height))
        self.SetSize(wx.Size(current_size.width, total_height))

    def AppendItem(self, values: list[str], checked: bool = False) -> int:
        """Append an item to the list."""
        was_empty = self.GetItemCount() == 0
        index = self.GetItemCount()

        row_data: list[Any] = [checked] + list(values)
        super().AppendItem(row_data)

        if was_empty or self.focus_after_add == FocusAfterAdd.NEW_ITEM:
            self.SetSelection(index)

        return index

    def GetItemText(self, row: int, col: int = 0) -> str:
        """Get the text value at the specified row and column."""
        return self.GetTextValue(row, col + 1)

    def SetItemText(self, row: int, col: int, value: str) -> None:
        """Set the text value at the specified row and column."""
        self.SetTextValue(value, row, col + 1)

    def DeleteItem(self, row: int) -> bool:
        """Delete an item and maintain valid selection."""
        was_selected = self.GetSelection() == row

        self._suppress_auto_select = True
        try:
            super().DeleteItem(row)

            if was_selected:
                new_count = self.GetItemCount()
                if new_count > 0:
                    if self.focus_after_delete == FocusAfterDelete.PREVIOUS:
                        new_selection = max(0, row - 1)
                    else:
                        new_selection = min(row, new_count - 1)
                    self.SetSelection(new_selection)
        finally:
            self._suppress_auto_select = False

        return True

    def DeleteAllItems(self) -> bool:
        """Delete all items from the list."""
        super().DeleteAllItems()
        return True

    def IsChecked(self, row: int) -> bool:
        """Return True if the item at row is checked."""
        return self.GetToggleValue(row, 0)

    def CheckItem(self, row: int, check: bool = True) -> None:
        """Set the checkbox state for an item."""
        self.SetToggleValue(check, row, 0)

    def GetSelection(self) -> int:
        """Return the index of the selected item, or -1 if none."""
        return self.GetSelectedRow()

    def SetSelection(self, row: int) -> None:
        """Select the item at the given row."""
        self.SelectRow(row)

    def IsSelected(self, row: int) -> bool:
        """Return True if the item at row is selected."""
        return self.GetSelectedRow() == row


# =============================================================================
# PUBLIC API
# =============================================================================

__all__ = [
    # Accessibility helpers
    "CheckableListAccessible",
    "CheckableWindowProtocol",
    "AccessibleCheckableMixin",

    # Ready-to-use controls
    "AccessibleCheckListBox",
    "AccessibleCheckListCtrl",
]
