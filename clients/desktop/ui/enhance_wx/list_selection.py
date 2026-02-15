"""
Selection management for wxPython list controls.

Provides mixins and ready-to-use controls that automatically manage selection
state for list controls:
- Auto-focus first item when control gains focus with no selection
- Maintain valid selection after item deletion (configurable: previous/next)
- Optionally auto-focus newly added items

Includes:
- ListBoxSelectionManagerMixin: For wx.ListBox-style controls
- ListCtrlSelectionManagerMixin: For wx.ListCtrl/wx.ListView-style controls
- ManagedListBox: Ready-to-use non-checkable single-column list
- ManagedListCtrl: Ready-to-use non-checkable multi-column list

Requires: wxPython
"""

from __future__ import annotations

from enum import Enum
from typing import Any

import wx


# =============================================================================
# CONFIGURATION ENUMS
# =============================================================================

class FocusAfterDelete(Enum):
    """Where to move focus after deleting an item."""
    PREVIOUS = "previous"  # Focus the item before the deleted one (default)
    NEXT = "next"          # Focus the item after the deleted one


class FocusAfterAdd(Enum):
    """Where to move focus after adding an item."""
    NEW_ITEM = "new"       # Focus the newly added item (default)
    STAY = "stay"          # Keep focus on current item


class ColumnWidth(Enum):
    """Column width modes for list controls."""
    AUTO_CONTENT = "auto_content"  # Auto-size to fit content (wx.LIST_AUTOSIZE)
    AUTO_HEADER = "auto_header"    # Auto-size to fit header text (wx.LIST_AUTOSIZE_USEHEADER)
    FILL = "fill"                  # Fill remaining space in the control


# =============================================================================
# MIXINS
# =============================================================================

class ListBoxSelectionManagerMixin:
    """
    Mixin that manages selection for wx.ListBox-style controls.

    Features:
    - Auto-selects first item when focused with no selection
    - Maintains valid selection when items are deleted
    - Optionally focuses new items when added

    Works with: wx.ListBox and subclasses.

    Note: While this mixin works with wx.CheckListBox, that control has
    accessibility limitations. For checkable lists, use AccessibleCheckListCtrl()
    instead, which provides this same selection management with better accessibility.

    Args:
        focus_after_delete: Where to focus after deleting an item.
            FocusAfterDelete.PREVIOUS (default) or FocusAfterDelete.NEXT
        focus_after_add: Where to focus after adding an item.
            FocusAfterAdd.NEW_ITEM (default) or FocusAfterAdd.STAY
    """

    def __init__(
        self,
        *args: Any,
        focus_after_delete: FocusAfterDelete = FocusAfterDelete.PREVIOUS,
        focus_after_add: FocusAfterAdd = FocusAfterAdd.NEW_ITEM,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.focus_after_delete = focus_after_delete
        self.focus_after_add = focus_after_add
        self._suppress_auto_select = False
        self.Bind(wx.EVT_SET_FOCUS, self._on_focus_ensure_selection)

    def _on_focus_ensure_selection(self, evt: wx.FocusEvent) -> None:
        """Auto-select first item when control gains focus with no selection."""
        evt.Skip()
        if self._suppress_auto_select:
            return
        if self.GetCount() > 0 and self.GetSelection() == wx.NOT_FOUND:  # type: ignore[attr-defined]
            self.SetSelection(0)  # type: ignore[attr-defined]

    def Delete(self, n: int) -> None:
        """Delete item and maintain valid selection."""
        was_selected = self.GetSelection() == n  # type: ignore[attr-defined]
        self._suppress_auto_select = True
        try:
            super().Delete(n)  # type: ignore[misc]
            if was_selected:
                new_count = self.GetCount()  # type: ignore[attr-defined]
                if new_count > 0:
                    if self.focus_after_delete == FocusAfterDelete.PREVIOUS:
                        new_selection = max(0, n - 1)
                    else:  # FocusAfterDelete.NEXT
                        new_selection = min(n, new_count - 1)
                    self.SetSelection(new_selection)  # type: ignore[attr-defined]
        finally:
            self._suppress_auto_select = False

    def Clear(self) -> None:
        """Clear all items."""
        super().Clear()  # type: ignore[misc]

    def Append(self, item: str) -> int:
        """Append item and optionally select it."""
        was_empty = self.GetCount() == 0  # type: ignore[attr-defined]
        result = super().Append(item)  # type: ignore[misc]
        if was_empty or self.focus_after_add == FocusAfterAdd.NEW_ITEM:
            self.SetSelection(self.GetCount() - 1)  # type: ignore[attr-defined]
        return result

    def Insert(self, item: str, pos: int) -> int:
        """Insert item and optionally select it."""
        was_empty = self.GetCount() == 0  # type: ignore[attr-defined]
        result = super().Insert(item, pos)  # type: ignore[misc]
        if was_empty or self.focus_after_add == FocusAfterAdd.NEW_ITEM:
            self.SetSelection(pos)  # type: ignore[attr-defined]
        return result

    def Set(self, items: list[str]) -> None:
        """Replace all items and maintain selection if possible."""
        old_selection = self.GetSelection()  # type: ignore[attr-defined]
        super().Set(items)  # type: ignore[misc]
        if self.GetCount() > 0:  # type: ignore[attr-defined]
            if old_selection != wx.NOT_FOUND:
                new_selection = min(old_selection, self.GetCount() - 1)  # type: ignore[attr-defined]
            else:
                new_selection = 0
            self.SetSelection(new_selection)  # type: ignore[attr-defined]


class ListCtrlSelectionManagerMixin:
    """
    Mixin that manages selection for wx.ListCtrl/wx.ListView-style controls.

    Features:
    - Auto-selects first item when focused with no selection
    - Maintains valid selection when items are deleted
    - Optionally focuses new items when added

    Works with: wx.ListCtrl, wx.ListView, and subclasses.

    Args:
        focus_after_delete: Where to focus after deleting an item.
            FocusAfterDelete.PREVIOUS (default) or FocusAfterDelete.NEXT
        focus_after_add: Where to focus after adding an item.
            FocusAfterAdd.NEW_ITEM (default) or FocusAfterAdd.STAY
    """

    # These will be set by __init__ or by subclass
    focus_after_delete: FocusAfterDelete
    focus_after_add: FocusAfterAdd

    def _init_selection_manager(
        self,
        focus_after_delete: FocusAfterDelete = FocusAfterDelete.PREVIOUS,
        focus_after_add: FocusAfterAdd = FocusAfterAdd.NEW_ITEM,
    ) -> None:
        """Initialize selection manager. Call this from __init__."""
        self.focus_after_delete = focus_after_delete
        self.focus_after_add = focus_after_add
        self._suppress_auto_select = False
        self.Bind(wx.EVT_SET_FOCUS, self._on_focus_ensure_selection)  # type: ignore[attr-defined]

    def _on_focus_ensure_selection(self, evt: wx.FocusEvent) -> None:
        """Auto-select first item when control gains focus with no selection."""
        evt.Skip()
        if self._suppress_auto_select:
            return
        if self.GetItemCount() > 0 and self.GetFirstSelected() == -1:  # type: ignore[attr-defined]
            self.Select(0)  # type: ignore[attr-defined]
            self.Focus(0)  # type: ignore[attr-defined]

    def DeleteItem(self, item: int) -> bool:
        """Delete item and maintain valid selection."""
        was_selected = self.IsSelected(item)  # type: ignore[attr-defined]
        self._suppress_auto_select = True
        try:
            result = super().DeleteItem(item)  # type: ignore[misc]
            if result and was_selected:
                new_count = self.GetItemCount()  # type: ignore[attr-defined]
                if new_count > 0:
                    if self.focus_after_delete == FocusAfterDelete.PREVIOUS:
                        new_selection = max(0, item - 1)
                    else:  # FocusAfterDelete.NEXT
                        new_selection = min(item, new_count - 1)
                    self.Select(new_selection)  # type: ignore[attr-defined]
                    self.Focus(new_selection)  # type: ignore[attr-defined]
        finally:
            self._suppress_auto_select = False
        return result

    def DeleteAllItems(self) -> bool:
        """Delete all items."""
        return super().DeleteAllItems()  # type: ignore[misc]

    def InsertItem(self, *args: Any, **kwargs: Any) -> int:
        """Insert item and optionally select it."""
        was_empty = self.GetItemCount() == 0  # type: ignore[attr-defined]
        result = super().InsertItem(*args, **kwargs)  # type: ignore[misc]
        if result != -1:
            if was_empty or self.focus_after_add == FocusAfterAdd.NEW_ITEM:
                self.Select(result)  # type: ignore[attr-defined]
                self.Focus(result)  # type: ignore[attr-defined]
        return result


# =============================================================================
# READY-TO-USE CONTROLS
# =============================================================================

class ManagedListBox(ListBoxSelectionManagerMixin, wx.ListBox):
    """
    A wx.ListBox with automatic selection management.

    RECOMMENDED: Use this for all non-checkable single-column lists.
    =================================================================
    This is the preferred control for simple lists without checkboxes.
    It's lightweight, uses the native platform listbox, and is already
    fully accessible to screen readers.

    Do NOT use ManagedListCtrl for simple single-column lists - that control
    is only appropriate for multi-column non-checkable lists.

    Features:
    - Auto-selects first item when focused with no selection
    - Maintains valid selection when items are deleted
    - Optionally focuses new items when added
    - Native platform appearance and full accessibility

    Args:
        parent: Parent window
        choices: Initial list of items (optional)
        focus_after_delete: Where to focus after deleting an item.
            FocusAfterDelete.PREVIOUS (default) or FocusAfterDelete.NEXT
        focus_after_add: Where to focus after adding an item.
            FocusAfterAdd.NEW_ITEM (default) or FocusAfterAdd.STAY
        name: Accessible name for the control (recommended for screen readers)

    Usage:
        fruits = ManagedListBox(
            parent,
            choices=["Apple", "Banana", "Cherry"],
            name="Fruit selection",
        )
        fruits.Append("Date")  # Auto-focuses new item
        fruits.Delete(0)       # Auto-focuses appropriate neighbor
    """
    pass


class ManagedListCtrl(ListCtrlSelectionManagerMixin, wx.ListView):
    """
    A wx.ListView with automatic selection management for multi-column lists.

    USE CASE: Multi-column non-checkable lists only.
    =================================================
    This control is for lists that need multiple columns but no checkboxes
    (e.g., file browsers with Name/Size/Date columns).

    For single-column non-checkable lists, use ManagedListBox instead.
    For any checkable list (single or multi-column), use AccessibleCheckListCtrl.

    Features:
    - Auto-selects first item when focused with no selection
    - Maintains valid selection when items are deleted
    - Optionally focuses new items when added
    - Auto-sizing columns with ColumnWidth enum
    - Configurable visible row count with SetVisibleRowCount()

    Args:
        parent: Parent window
        focus_after_delete: Where to focus after deleting an item.
            FocusAfterDelete.PREVIOUS (default) or FocusAfterDelete.NEXT
        focus_after_add: Where to focus after adding an item.
            FocusAfterAdd.NEW_ITEM (default) or FocusAfterAdd.STAY
        show_header: Whether to show column headers.
        name: Accessible name for the control (recommended for screen readers)

    Usage:
        files = ManagedListCtrl(parent, name="File list")
        files.AppendColumn("Name", ColumnWidth.AUTO_CONTENT)
        files.AppendColumn("Size", width=80)
        files.AppendColumn("Modified", ColumnWidth.FILL)
        files.InsertItem(0, "document.txt")
        files.SetItem(0, 1, "4 KB")
        files.SetItem(0, 2, "2024-01-15")
        files.AutoSizeColumns()
    """

    def __init__(
        self,
        parent: wx.Window,
        id: int = wx.ID_ANY,
        pos: wx.Point = wx.DefaultPosition,
        size: wx.Size = wx.DefaultSize,
        style: int = wx.LC_REPORT,
        focus_after_delete: FocusAfterDelete = FocusAfterDelete.PREVIOUS,
        focus_after_add: FocusAfterAdd = FocusAfterAdd.NEW_ITEM,
        show_header: bool = True,
        **kwargs: Any,
    ) -> None:
        if not show_header:
            style |= wx.LC_NO_HEADER
        super().__init__(parent, id, pos, size, style, **kwargs)
        self._init_selection_manager(focus_after_delete, focus_after_add)
        self._column_count = 0
        self._column_widths: list[int | ColumnWidth] = []
        self._show_header = show_header

    def AppendColumn(self, heading: str, width: int | ColumnWidth = ColumnWidth.AUTO_CONTENT) -> None:
        """
        Add a column to the list.

        Args:
            heading: Column header text
            width: Column width - can be int or ColumnWidth enum
        """
        if isinstance(width, ColumnWidth):
            if width == ColumnWidth.AUTO_CONTENT:
                initial_width = wx.LIST_AUTOSIZE
            elif width == ColumnWidth.AUTO_HEADER:
                initial_width = wx.LIST_AUTOSIZE_USEHEADER
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
        if self._show_header:
            dc = wx.ClientDC(self)
            dc.SetFont(self.GetFont())
            header_height = dc.GetTextExtent("Tg")[1] + 8

        total_height = (rows * item_height) + header_height + 4

        current_size = self.GetSize()
        self.SetMinSize(wx.Size(current_size.width, total_height))
        self.SetSize(wx.Size(current_size.width, total_height))


__all__ = [
    # Configuration enums
    "FocusAfterDelete",
    "FocusAfterAdd",
    "ColumnWidth",

    # Mixins (for custom controls)
    "ListBoxSelectionManagerMixin",
    "ListCtrlSelectionManagerMixin",

    # Ready-to-use controls
    "ManagedListBox",
    "ManagedListCtrl",
]
