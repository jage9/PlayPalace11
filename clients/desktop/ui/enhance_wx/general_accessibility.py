"""
General-purpose accessibility helpers for wxPython.

Provides platform-specific accessibility notification utilities that can be
used by any control, not just lists.

Requires: wxPython
"""

from __future__ import annotations

import sys
from typing import Tuple

import wx


# Type alias for wx.Accessible return values
AccResult = Tuple[int, int]


# =============================================================================
# Platform-specific accessibility notification
# =============================================================================

if sys.platform == "win32":
    import ctypes

    _user32 = ctypes.windll.user32

    # Windows accessibility constants
    # https://learn.microsoft.com/en-us/windows/win32/winauto/object-identifiers
    _CHILDID_SELF = 0
    _OBJID_CLIENT = -4
    _EVENT_OBJECT_STATECHANGE = 0x800A

    def notify_state_change(hwnd: int, child_index: int) -> None:
        """
        Notify Windows accessibility system of a state change.

        Args:
            hwnd: Window handle (use control.Handle)
            child_index: 0-based index of the child item that changed
        """
        # Accessibility child IDs are 1-based (0 means the object itself)
        child_id = child_index + 1
        _user32.NotifyWinEvent(
            _EVENT_OBJECT_STATECHANGE,
            hwnd,
            _OBJID_CLIENT,
            child_id,
        )

elif sys.platform == "darwin":
    _CHILDID_SELF = 0

    def notify_state_change(hwnd: int, child_index: int) -> None:
        """No-op on macOS (Windows-style notifications don't apply)."""
        pass

else:
    # Linux and other platforms
    _CHILDID_SELF = 0

    def notify_state_change(hwnd: int, child_index: int) -> None:
        """No-op on Linux platforms."""
        pass


__all__ = [
    "AccResult",
    "notify_state_change",
]
