# Enhanced Wx Reference

Quick reference for the `enhance_wx` package.

Sub-modules:
- `general_accessibility` — Platform-specific accessibility notification utilities
- `list_selection` — Selection management mixins and managed list controls
- `accessible_lists` — Accessible checkable list controls

---

## Configuration Enums

Settings you pass to controls.

| Name | What it does |
|------|--------------|
| `FocusAfterDelete` | After deleting an item, focus the `PREVIOUS` or `NEXT` item |
| `FocusAfterAdd` | After adding an item, focus the `NEW_ITEM` or `STAY` on current |
| `ColumnWidth` | Column sizing: `AUTO_CONTENT`, `AUTO_HEADER`, or `FILL` remaining space |

---

## Mixins

Internal building blocks. You don't use these directly.

| Name | What it does |
|------|--------------|
| `ListBoxSelectionManagerMixin` | Adds auto-select-on-focus and smart deletion handling to `wx.ListBox` |
| `ListCtrlSelectionManagerMixin` | Same thing, but for `wx.ListCtrl`/`wx.ListView` (not DataView) |
| `AccessibleCheckableMixin` | Tells screen readers when checkboxes change state (for `wx.CheckListBox`) |

Note: `wx.DataViewListCtrl` has incompatible method names (e.g., `GetSelectedRow()` vs `GetFirstSelected()`), so `_DataViewCheckListCtrl` implements the same selection management features directly rather than using a mixin. All platforms have equal selection support.

---

## Low-level Accessibility Helpers

Internal. You don't use these directly.

| Name | What it does |
|------|--------------|
| `notify_state_change()` | Windows function that fires an accessibility event when a checkbox toggles |
| `CheckableListAccessible` | Tells Windows screen readers "these items are checkboxes" and their checked/unchecked state |

---

## Ready-to-Use Controls

What you actually instantiate.

| Name | Base control | Checkboxes? | Columns | When to use |
|------|--------------|-------------|---------|-------------|
| `ManagedListBox` | `wx.ListBox` | No | 1 | **Simple lists** - fruits, names, options |
| `ManagedListCtrl` | `wx.ListView` | No | Multiple | **Multi-column lists** - file browsers, data tables |
| `AccessibleCheckListBox` | `wx.CheckListBox` | Yes | 1 | **Legacy only** - old projects that can't migrate |
| `AccessibleCheckListCtrl()` | Platform-specific (see below) | Yes | 1 or more | **All checkable lists** - settings, package lists, todo items |

**AccessibleCheckListCtrl platform behavior:**
- **Windows**: Always uses `wx.ListView` (works for single and multi-column)
- **macOS single-column** (`multi_column=False`): Uses `wx.CheckListBox` for better VoiceOver support
- **macOS multi-column** (`multi_column=True`): Uses `wx.DataViewListCtrl`

---

## Internal Platform-Specific Classes

You never instantiate these directly. They are returned by `AccessibleCheckListCtrl()`.

| Name | What it does |
|------|--------------|
| `_WindowsCheckListCtrl` | Windows implementation (all cases) |
| `AccessibleCheckListBox` | macOS implementation for single-column lists (`multi_column=False`) |
| `_DataViewCheckListCtrl` | macOS/Linux implementation for multi-column lists (`multi_column=True`) |

---

## Quick Start: Just Remember These 3

For day-to-day use, you only need:

### 1. Simple list without checkboxes

```python
from list_selection import ManagedListBox

fruits = ManagedListBox(parent, choices=["Apple", "Banana", "Cherry"])
```

### 2. Multi-column list without checkboxes

```python
from list_selection import ManagedListCtrl, ColumnWidth

files = ManagedListCtrl(parent)
files.AppendColumn("Name", ColumnWidth.AUTO_CONTENT)
files.AppendColumn("Size", width=80)
files.AppendColumn("Modified", ColumnWidth.FILL)
files.InsertItem(0, "document.txt")
files.SetItem(0, 1, "4 KB")
files.SetItem(0, 2, "2024-01-15")
```

### 3. ANY list with checkboxes

```python
from accessible_lists import AccessibleCheckListCtrl
from list_selection import ColumnWidth

# Single-column (use show_header=False for clean look)
# On macOS, this uses wx.CheckListBox for better accessibility
settings = AccessibleCheckListCtrl(parent, show_header=False, name="Settings")
settings.AppendColumn("Option", ColumnWidth.FILL)
settings.AppendItem(["Enable dark mode"])
settings.AppendItem(["Show notifications"])
settings.CheckItem(0, True)  # Check first item

# Multi-column (must specify multi_column=True)
packages = AccessibleCheckListCtrl(parent, multi_column=True, name="Packages")
packages.AppendColumn("Name", ColumnWidth.AUTO_CONTENT)
packages.AppendColumn("Version", width=80)
packages.AppendItem(["numpy", "1.24.0"])
packages.AppendItem(["pandas", "2.0.0"], checked=True)
```

---

## Decision Flowchart

```
Do you need checkboxes?
    |
    +-- NO --> Is it single-column?
    |              |
    |              +-- YES --> ManagedListBox
    |              |
    |              +-- NO  --> ManagedListCtrl
    |
    +-- YES --> Is this a legacy project using wx.CheckListBox?
                   |
                   +-- YES --> AccessibleCheckListBox (last resort)
                   |
                   +-- NO  --> AccessibleCheckListCtrl (always use this)
```

---

## Common Operations

### Focus behavior after deletion

```python
from list_selection import FocusAfterDelete

# Focus the item before the deleted one (default)
control.focus_after_delete = FocusAfterDelete.PREVIOUS

# Focus the item after the deleted one
control.focus_after_delete = FocusAfterDelete.NEXT
```

### Focus behavior after adding

```python
from list_selection import FocusAfterAdd

# Auto-focus newly added items (default)
control.focus_after_add = FocusAfterAdd.NEW_ITEM

# Keep focus on current item
control.focus_after_add = FocusAfterAdd.STAY
```

### Set control height to show N rows

```python
# Only available on ManagedListCtrl and AccessibleCheckListCtrl
control.SetVisibleRowCount(5)
```

### Auto-size columns to fit content

```python
# Only available on ManagedListCtrl and AccessibleCheckListCtrl
control.AutoSizeColumns()
```
