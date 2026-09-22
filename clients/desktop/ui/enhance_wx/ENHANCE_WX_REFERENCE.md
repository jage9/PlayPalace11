# Enhanced Wx Reference

Quick reference for the `enhance_wx` package.

## Modules

- `tree_selection` — Tree controls with predictable focus behavior.
- `list_selection` — The `FocusAfterDelete` option used by tree controls.
- `audio_events` — Audio feedback helpers for UI events.

## Tree selection

`ManagedTreeCtrl` selects the first visible item when it receives focus without
an existing selection. After removing an item, call `select_after_delete()` to
choose a previous sibling, next sibling, or parent according to the configured
`FocusAfterDelete` value. On macOS, the control uses a DataView-backed
implementation while preserving the tree control API.

```python
from ui.enhance_wx.list_selection import FocusAfterDelete
from ui.enhance_wx.tree_selection import ManagedTreeCtrl

tree = ManagedTreeCtrl(
    parent,
    name="Items",
    focus_after_delete=FocusAfterDelete.PREVIOUS,
)
root = tree.AddRoot("Items")
previous = tree.AppendItem(root, "Previous")
current = tree.AppendItem(root, "Current")
next_item = tree.AppendItem(root, "Next")

# Delete current, then restore a useful selection.
tree.Delete(current)
tree.select_after_delete(root, previous, next_item)
```

`FocusAfterDelete.PREVIOUS` prefers the previous sibling and
`FocusAfterDelete.NEXT` prefers the next sibling. If the preferred sibling is
missing, the other sibling is used; otherwise the parent is selected when it is
not the invisible root.

## Audio events

`play_sound(name)` loads `name + ".wav"` and plays it asynchronously by
default. `SoundBindingsMixin` adds sound bindings for supported child controls.

```python
import wx

from ui.enhance_wx.audio_events import SoundBindingsMixin


class SettingsPanel(SoundBindingsMixin, wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        # Add child controls first, then bind their sound events.
        self.bind_sounds(enable_focus=True, recursion=None)
```

Use `audio_settings(sounds_path="sounds", block=False)` to configure the
default sound directory and playback mode before calling `bind_sounds()`.
