"""
Example demonstrating enhance_wx package usage.

Run this file to see a demo window with accessible checkable list controls.
Test with a screen reader (NVDA, JAWS, Narrator, VoiceOver, Orca) to verify accessibility.

Usage:
    python test_example.py
"""

import wx

from list_selection import (
    FocusAfterDelete,
    FocusAfterAdd,
    ColumnWidth,
    ManagedListBox,
    ManagedListCtrl,
)
from accessible_lists import (
    AccessibleCheckListBox,
    AccessibleCheckListCtrl,
)


# -----------------------------------------------------------------------------
# Example 1: Plain ManagedListBox (non-checkable)
# -----------------------------------------------------------------------------

class ManagedListBoxExample(wx.Panel):
    """
    Using ManagedListBox for a plain list with selection management.
    """

    def __init__(self, parent: wx.Window) -> None:
        super().__init__(parent)
        self._item_counter = 5

        sizer = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(self, label="Example 1: ManagedListBox (non-checkable)")
        font = label.GetFont()
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        label.SetFont(font)
        sizer.Add(label, flag=wx.ALL, border=5)

        description = wx.StaticText(
            self,
            label="Plain wx.ListBox with automatic selection management.",
        )
        sizer.Add(description, flag=wx.LEFT | wx.BOTTOM, border=5)

        # Create the managed list box
        self.listbox = ManagedListBox(
            self,
            choices=[
                "Apple",
                "Banana",
                "Cherry",
                "Date",
                "Elderberry",
            ],
        )

        sizer.Add(self.listbox, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        # Focus behavior options
        options_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Delete focus option
        delete_box = wx.StaticBox(self, label="After Delete")
        delete_sizer = wx.StaticBoxSizer(delete_box, wx.HORIZONTAL)
        self.delete_prev = wx.RadioButton(self, label="Previous", style=wx.RB_GROUP)
        self.delete_next = wx.RadioButton(self, label="Next")
        self.delete_prev.SetValue(True)
        self.delete_prev.Bind(wx.EVT_RADIOBUTTON, self._on_delete_option_changed)
        self.delete_next.Bind(wx.EVT_RADIOBUTTON, self._on_delete_option_changed)
        delete_sizer.Add(self.delete_prev, flag=wx.RIGHT, border=5)
        delete_sizer.Add(self.delete_next)
        options_sizer.Add(delete_sizer, flag=wx.RIGHT, border=10)

        # Add focus option
        add_box = wx.StaticBox(self, label="After Add")
        add_sizer = wx.StaticBoxSizer(add_box, wx.HORIZONTAL)
        self.add_new = wx.RadioButton(self, label="New Item", style=wx.RB_GROUP)
        self.add_stay = wx.RadioButton(self, label="Stay")
        self.add_new.SetValue(True)
        self.add_new.Bind(wx.EVT_RADIOBUTTON, self._on_add_option_changed)
        self.add_stay.Bind(wx.EVT_RADIOBUTTON, self._on_add_option_changed)
        add_sizer.Add(self.add_new, flag=wx.RIGHT, border=5)
        add_sizer.Add(self.add_stay)
        options_sizer.Add(add_sizer)

        sizer.Add(options_sizer, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM, border=5)

        # Buttons row
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        btn_add = wx.Button(self, label="Add Item")
        btn_add.Bind(wx.EVT_BUTTON, self._on_add_item)
        btn_sizer.Add(btn_add, flag=wx.RIGHT, border=5)

        btn_delete = wx.Button(self, label="Delete Selected")
        btn_delete.Bind(wx.EVT_BUTTON, self._on_delete_selected)
        btn_sizer.Add(btn_delete, flag=wx.RIGHT, border=5)

        btn_clear = wx.Button(self, label="Clear All")
        btn_clear.Bind(wx.EVT_BUTTON, self._on_clear_all)
        btn_sizer.Add(btn_clear)

        sizer.Add(btn_sizer, flag=wx.ALL, border=5)

        self.SetSizer(sizer)

    def _on_delete_option_changed(self, evt: wx.CommandEvent) -> None:
        if self.delete_prev.GetValue():
            self.listbox.focus_after_delete = FocusAfterDelete.PREVIOUS
        else:
            self.listbox.focus_after_delete = FocusAfterDelete.NEXT

    def _on_add_option_changed(self, evt: wx.CommandEvent) -> None:
        if self.add_new.GetValue():
            self.listbox.focus_after_add = FocusAfterAdd.NEW_ITEM
        else:
            self.listbox.focus_after_add = FocusAfterAdd.STAY

    def _on_add_item(self, evt: wx.CommandEvent) -> None:
        self._item_counter += 1
        self.listbox.Append(f"Fruit {self._item_counter}")

    def _on_delete_selected(self, evt: wx.CommandEvent) -> None:
        selection = self.listbox.GetSelection()
        if selection != wx.NOT_FOUND:
            self.listbox.Delete(selection)

    def _on_clear_all(self, evt: wx.CommandEvent) -> None:
        self.listbox.Clear()


# -----------------------------------------------------------------------------
# Example 2: Accessible CheckListBox (checkable)
# -----------------------------------------------------------------------------

class CheckListBoxExample(wx.Panel):
    """
    Using AccessibleCheckListBox - a checkable list with accessibility fixes.
    """

    def __init__(self, parent: wx.Window) -> None:
        super().__init__(parent)
        self._item_counter = 4

        sizer = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(self, label="Example 2: AccessibleCheckListBox")
        font = label.GetFont()
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        label.SetFont(font)
        sizer.Add(label, flag=wx.ALL, border=5)

        description = wx.StaticText(
            self,
            label="Checkable list with screen reader support and selection management.",
        )
        sizer.Add(description, flag=wx.LEFT | wx.BOTTOM, border=5)

        # Create the accessible check list box
        self.checklist = AccessibleCheckListBox(
            self,
            choices=[
                "Enable notifications",
                "Start on login",
                "Check for updates",
                "Send statistics",
            ],
        )

        self.checklist.Check(0, True)
        self.checklist.Check(2, True)

        sizer.Add(self.checklist, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        # Focus behavior options
        options_sizer = wx.BoxSizer(wx.HORIZONTAL)

        delete_box = wx.StaticBox(self, label="After Delete")
        delete_sizer = wx.StaticBoxSizer(delete_box, wx.HORIZONTAL)
        self.delete_prev = wx.RadioButton(self, label="Previous", style=wx.RB_GROUP)
        self.delete_next = wx.RadioButton(self, label="Next")
        self.delete_prev.SetValue(True)
        self.delete_prev.Bind(wx.EVT_RADIOBUTTON, self._on_delete_option_changed)
        self.delete_next.Bind(wx.EVT_RADIOBUTTON, self._on_delete_option_changed)
        delete_sizer.Add(self.delete_prev, flag=wx.RIGHT, border=5)
        delete_sizer.Add(self.delete_next)
        options_sizer.Add(delete_sizer, flag=wx.RIGHT, border=10)

        add_box = wx.StaticBox(self, label="After Add")
        add_sizer = wx.StaticBoxSizer(add_box, wx.HORIZONTAL)
        self.add_new = wx.RadioButton(self, label="New Item", style=wx.RB_GROUP)
        self.add_stay = wx.RadioButton(self, label="Stay")
        self.add_new.SetValue(True)
        self.add_new.Bind(wx.EVT_RADIOBUTTON, self._on_add_option_changed)
        self.add_stay.Bind(wx.EVT_RADIOBUTTON, self._on_add_option_changed)
        add_sizer.Add(self.add_new, flag=wx.RIGHT, border=5)
        add_sizer.Add(self.add_stay)
        options_sizer.Add(add_sizer)

        sizer.Add(options_sizer, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM, border=5)

        # Buttons row
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        btn_show = wx.Button(self, label="Show Checked")
        btn_show.Bind(wx.EVT_BUTTON, self._on_show_checked)
        btn_sizer.Add(btn_show, flag=wx.RIGHT, border=5)

        btn_add = wx.Button(self, label="Add Item")
        btn_add.Bind(wx.EVT_BUTTON, self._on_add_item)
        btn_sizer.Add(btn_add, flag=wx.RIGHT, border=5)

        btn_delete = wx.Button(self, label="Delete Selected")
        btn_delete.Bind(wx.EVT_BUTTON, self._on_delete_selected)
        btn_sizer.Add(btn_delete, flag=wx.RIGHT, border=5)

        btn_clear = wx.Button(self, label="Clear All")
        btn_clear.Bind(wx.EVT_BUTTON, self._on_clear_all)
        btn_sizer.Add(btn_clear)

        sizer.Add(btn_sizer, flag=wx.ALL, border=5)

        self.SetSizer(sizer)

    def _on_delete_option_changed(self, evt: wx.CommandEvent) -> None:
        if self.delete_prev.GetValue():
            self.checklist.focus_after_delete = FocusAfterDelete.PREVIOUS
        else:
            self.checklist.focus_after_delete = FocusAfterDelete.NEXT

    def _on_add_option_changed(self, evt: wx.CommandEvent) -> None:
        if self.add_new.GetValue():
            self.checklist.focus_after_add = FocusAfterAdd.NEW_ITEM
        else:
            self.checklist.focus_after_add = FocusAfterAdd.STAY

    def _on_show_checked(self, evt: wx.CommandEvent) -> None:
        checked = [
            self.checklist.GetString(i)
            for i in range(self.checklist.GetCount())
            if self.checklist.IsChecked(i)
        ]
        if checked:
            msg = "Checked items:\n" + "\n".join(f"  - {item}" for item in checked)
        else:
            msg = "No items checked."
        wx.MessageBox(msg, "Checked Items")

    def _on_add_item(self, evt: wx.CommandEvent) -> None:
        self._item_counter += 1
        self.checklist.Append(f"Option {self._item_counter}")

    def _on_delete_selected(self, evt: wx.CommandEvent) -> None:
        selection = self.checklist.GetSelection()
        if selection != wx.NOT_FOUND:
            self.checklist.Delete(selection)

    def _on_clear_all(self, evt: wx.CommandEvent) -> None:
        self.checklist.Clear()


# -----------------------------------------------------------------------------
# Example 3: Multi-Column Checkable List (wx.ListCtrl)
# -----------------------------------------------------------------------------

class MultiColumnExample(wx.Panel):
    """
    Using AccessibleCheckListCtrl for multi-column checkable lists.

    This control automatically uses wx.ListView on Windows and
    wx.DataViewListCtrl on macOS/Linux for cross-platform accessibility.
    """

    def __init__(self, parent: wx.Window) -> None:
        super().__init__(parent)
        self._item_counter = 5

        sizer = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(self, label="Example 3: Multi-Column CheckListCtrl")
        font = label.GetFont()
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        label.SetFont(font)
        sizer.Add(label, flag=wx.ALL, border=5)

        description = wx.StaticText(
            self,
            label="Multi-column list with checkboxes (cross-platform accessible).",
        )
        sizer.Add(description, flag=wx.LEFT | wx.BOTTOM, border=5)

        # Create multi-column checkable list (cross-platform)
        self.listctrl = AccessibleCheckListCtrl(self, multi_column=True)

        # Add columns using ColumnWidth enum for auto-sizing
        self.listctrl.AppendColumn("Package", ColumnWidth.AUTO_CONTENT)
        self.listctrl.AppendColumn("Version", width=80)  # Fixed width also works
        self.listctrl.AppendColumn("Status", ColumnWidth.FILL)  # Fill remaining space

        # Add items
        packages = [
            ("numpy", "1.24.0", "Installed"),
            ("pandas", "2.0.0", "Installed"),
            ("requests", "2.28.0", "Update available"),
            ("flask", "2.2.0", "Installed"),
            ("django", "4.1.0", "Not installed"),
        ]

        for name, version, status in packages:
            self.listctrl.AppendItem([name, version, status])

        # Pre-check some items
        self.listctrl.CheckItem(0, True)
        self.listctrl.CheckItem(1, True)

        # Auto-size columns after adding items
        self.listctrl.AutoSizeColumns()

        sizer.Add(self.listctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        # Non-checkable multi-column list
        label2 = wx.StaticText(self, label="Non-checkable variant (ManagedListCtrl):")
        sizer.Add(label2, flag=wx.LEFT | wx.TOP, border=5)

        self.file_list = ManagedListCtrl(self, name="File list")
        self.file_list.AppendColumn("Name", ColumnWidth.AUTO_CONTENT)
        self.file_list.AppendColumn("Size", width=80)
        self.file_list.AppendColumn("Modified", ColumnWidth.FILL)

        files = [
            ("document.txt", "4 KB", "2024-01-15"),
            ("photo.jpg", "2.3 MB", "2024-01-10"),
            ("notes.md", "512 B", "2024-01-20"),
        ]

        for name, size, modified in files:
            idx = self.file_list.InsertItem(self.file_list.GetItemCount(), name)
            self.file_list.SetItem(idx, 1, size)
            self.file_list.SetItem(idx, 2, modified)

        self.file_list.AutoSizeColumns()

        sizer.Add(self.file_list, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        # Focus behavior options
        options_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Delete focus option
        delete_box = wx.StaticBox(self, label="After Delete")
        delete_sizer = wx.StaticBoxSizer(delete_box, wx.HORIZONTAL)
        self.delete_prev = wx.RadioButton(self, label="Previous", style=wx.RB_GROUP)
        self.delete_next = wx.RadioButton(self, label="Next")
        self.delete_prev.SetValue(True)
        self.delete_prev.Bind(wx.EVT_RADIOBUTTON, self._on_delete_option_changed)
        self.delete_next.Bind(wx.EVT_RADIOBUTTON, self._on_delete_option_changed)
        delete_sizer.Add(self.delete_prev, flag=wx.RIGHT, border=5)
        delete_sizer.Add(self.delete_next)
        options_sizer.Add(delete_sizer, flag=wx.RIGHT, border=10)

        # Add focus option
        add_box = wx.StaticBox(self, label="After Add")
        add_sizer = wx.StaticBoxSizer(add_box, wx.HORIZONTAL)
        self.add_new = wx.RadioButton(self, label="New Item", style=wx.RB_GROUP)
        self.add_stay = wx.RadioButton(self, label="Stay")
        self.add_new.SetValue(True)
        self.add_new.Bind(wx.EVT_RADIOBUTTON, self._on_add_option_changed)
        self.add_stay.Bind(wx.EVT_RADIOBUTTON, self._on_add_option_changed)
        add_sizer.Add(self.add_new, flag=wx.RIGHT, border=5)
        add_sizer.Add(self.add_stay)
        options_sizer.Add(add_sizer)

        sizer.Add(options_sizer, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM, border=5)

        # Buttons row
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        btn_show = wx.Button(self, label="Show Checked")
        btn_show.Bind(wx.EVT_BUTTON, self._on_show_checked)
        btn_sizer.Add(btn_show, flag=wx.RIGHT, border=5)

        btn_add = wx.Button(self, label="Add Item")
        btn_add.Bind(wx.EVT_BUTTON, self._on_add_item)
        btn_sizer.Add(btn_add, flag=wx.RIGHT, border=5)

        btn_delete = wx.Button(self, label="Delete Selected")
        btn_delete.Bind(wx.EVT_BUTTON, self._on_delete_selected)
        btn_sizer.Add(btn_delete, flag=wx.RIGHT, border=5)

        btn_clear = wx.Button(self, label="Clear All")
        btn_clear.Bind(wx.EVT_BUTTON, self._on_clear_all)
        btn_sizer.Add(btn_clear)

        sizer.Add(btn_sizer, flag=wx.ALL, border=5)

        self.SetSizer(sizer)

    def _on_delete_option_changed(self, evt: wx.CommandEvent) -> None:
        if self.delete_prev.GetValue():
            self.listctrl.focus_after_delete = FocusAfterDelete.PREVIOUS
        else:
            self.listctrl.focus_after_delete = FocusAfterDelete.NEXT

    def _on_add_option_changed(self, evt: wx.CommandEvent) -> None:
        if self.add_new.GetValue():
            self.listctrl.focus_after_add = FocusAfterAdd.NEW_ITEM
        else:
            self.listctrl.focus_after_add = FocusAfterAdd.STAY

    def _on_show_checked(self, evt: wx.CommandEvent) -> None:
        checked = [
            self.listctrl.GetItemText(i, 0)
            for i in range(self.listctrl.GetItemCount())
            if self.listctrl.IsChecked(i)
        ]
        if checked:
            msg = "Checked packages:\n" + "\n".join(f"  - {pkg}" for pkg in checked)
        else:
            msg = "No packages checked."
        wx.MessageBox(msg, "Checked Packages")

    def _on_add_item(self, evt: wx.CommandEvent) -> None:
        self._item_counter += 1
        self.listctrl.AppendItem([f"package{self._item_counter}", "0.0.1", "New"])

    def _on_delete_selected(self, evt: wx.CommandEvent) -> None:
        selection = self.listctrl.GetSelection()
        if selection != -1:
            self.listctrl.DeleteItem(selection)

    def _on_clear_all(self, evt: wx.CommandEvent) -> None:
        self.listctrl.DeleteAllItems()


# -----------------------------------------------------------------------------
# Example 4: Single-Column List (no header) - Accessible alternative to CheckListBox
# -----------------------------------------------------------------------------

class SingleColumnExample(wx.Panel):
    """
    Using AccessibleCheckListCtrl with show_header=False for simple lists.

    This demonstrates using ListView/DataViewCtrl as an accessible alternative
    to CheckListBox - better screen reader support with minimal visual overhead.
    """

    def __init__(self, parent: wx.Window) -> None:
        super().__init__(parent)
        self._item_counter = 5

        sizer = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(self, label="Example 4: Single-Column (No Header)")
        font = label.GetFont()
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        label.SetFont(font)
        sizer.Add(label, flag=wx.ALL, border=5)

        description = wx.StaticText(
            self,
            label="Accessible alternative to CheckListBox - no column header, clean look.",
        )
        sizer.Add(description, flag=wx.LEFT | wx.BOTTOM, border=5)

        # Create single-column checkable list with NO header
        self.listctrl = AccessibleCheckListCtrl(
            self,
            show_header=False,  # Hide the column header for cleaner appearance
            name="Settings list",
        )

        # Single column that fills available width
        self.listctrl.AppendColumn("Setting", ColumnWidth.FILL)

        # Add items
        settings = [
            "Enable dark mode",
            "Show notifications",
            "Auto-save documents",
            "Check for updates",
            "Send usage statistics",
        ]

        for setting in settings:
            self.listctrl.AppendItem([setting])

        # Pre-check some items
        self.listctrl.CheckItem(0, True)
        self.listctrl.CheckItem(2, True)

        # Set height to show exactly 5 rows
        self.listctrl.SetVisibleRowCount(5)

        sizer.Add(self.listctrl, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

        # Also show a ManagedListCtrl (non-checkable) with no header
        label2 = wx.StaticText(self, label="Non-checkable variant:")
        sizer.Add(label2, flag=wx.LEFT | wx.TOP, border=5)

        self.simple_list = ManagedListCtrl(
            self,
            show_header=False,
            style=wx.LC_REPORT | wx.LC_SINGLE_SEL,
        )
        self.simple_list.AppendColumn("Items", ColumnWidth.FILL)

        for fruit in ["Apple", "Banana", "Cherry", "Date", "Elderberry"]:
            idx = self.simple_list.InsertItem(self.simple_list.GetItemCount(), fruit)

        self.simple_list.SetVisibleRowCount(4)

        sizer.Add(self.simple_list, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

        # Buttons row
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        btn_show = wx.Button(self, label="Show Checked")
        btn_show.Bind(wx.EVT_BUTTON, self._on_show_checked)
        btn_sizer.Add(btn_show, flag=wx.RIGHT, border=5)

        btn_add = wx.Button(self, label="Add Item")
        btn_add.Bind(wx.EVT_BUTTON, self._on_add_item)
        btn_sizer.Add(btn_add, flag=wx.RIGHT, border=5)

        btn_delete = wx.Button(self, label="Delete Selected")
        btn_delete.Bind(wx.EVT_BUTTON, self._on_delete_selected)
        btn_sizer.Add(btn_delete)

        sizer.Add(btn_sizer, flag=wx.ALL, border=5)

        self.SetSizer(sizer)

    def _on_show_checked(self, evt: wx.CommandEvent) -> None:
        checked = [
            self.listctrl.GetItemText(i, 0)
            for i in range(self.listctrl.GetItemCount())
            if self.listctrl.IsChecked(i)
        ]
        if checked:
            msg = "Checked settings:\n" + "\n".join(f"  - {s}" for s in checked)
        else:
            msg = "No settings checked."
        wx.MessageBox(msg, "Checked Settings")

    def _on_add_item(self, evt: wx.CommandEvent) -> None:
        self._item_counter += 1
        self.listctrl.AppendItem([f"New setting {self._item_counter}"])

    def _on_delete_selected(self, evt: wx.CommandEvent) -> None:
        selection = self.listctrl.GetSelection()
        if selection != -1:
            self.listctrl.DeleteItem(selection)


# -----------------------------------------------------------------------------
# Main Application
# -----------------------------------------------------------------------------

class DemoFrame(wx.Frame):
    """Main demo window with all examples in a notebook."""

    def __init__(self) -> None:
        super().__init__(
            None,
            title="Accessible Controls Demo",
            size=(620, 550),
        )

        # Create a notebook to hold all examples
        notebook = wx.Notebook(self)

        # Add each example as a tab
        notebook.AddPage(ManagedListBoxExample(notebook), "ListBox")
        notebook.AddPage(CheckListBoxExample(notebook), "CheckListBox")
        notebook.AddPage(MultiColumnExample(notebook), "Multi-Col")
        notebook.AddPage(SingleColumnExample(notebook), "Single-Col")

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, proportion=1, flag=wx.EXPAND)
        self.SetSizer(sizer)

        # Status bar for instructions
        self.CreateStatusBar()
        self.SetStatusText("Use a screen reader to test accessibility features")

        self.Centre()


def main() -> None:
    app = wx.App()
    frame = DemoFrame()
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
