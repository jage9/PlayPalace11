# User Interface:
This will cover everything that is sent to the user's client for controlling navigation. Play palace v 10 used wxpython, and this will continue for v11.

# Menus:
Menus will be presented inside of a listbox element, for easier accessibility and simplicity. Wrapper functions will be provided for managing the listbox and contents inside.

## grids:
Allow for rotating the grid 90 and 180 degrees, or inverting directions aka ascending or decending order for one or all rows / columns.

## Keybinds:
Keybinds act as hotkey or shortcuts to trigger an action that can typically be accessed from a menu. As such, these should hold a high priority, but nevertheless be secondary to menu access.
A keybind can also contain a scope in which it can be preformed.
*global: can be accessed anywhere in the client.
*table: can be accessed only if the user is present at a table.

Keybinds should be a class with the following attributes:
*name [string]: the name of the keybind's function. For example, select dice.
*default key [string/int]: the default keycode to use. A user can override this.
*actions list [list of ints]: the list of action menu id(s) this keybind applies to.
*requires focus [bool]: whether the user must be focused on one of the valid actions for this keybind to trigger.
*current state [enum]: use this for controlling when this keybind should be enabled or not.

Default keybind state enum:
Each state should be able to determine whether the keybind is active or not. This can be done with a hash map of (string, bool) or (string, callable) for state callbacks.
Default enum values:
*never: this keybind is completely unavailable.
*idle: can be accessed if an activity is not in progress.
Most common usage is when a game at the table is not active. These may also be different depending on the game being played. For example, duck race would have a keybind to check which challenges are enabled, even without the game needing to be active.
*active: can be accessed while an activity is in progress
Most common usage is when a game at the table is active. This works best for a specific game type only. For example, uno and farkle would have different keybinds.
*always: this keybind is available.

If a keybind scope is table, add these additional attributes:
*players [list of players]: the list of players this keybind applies to. If empty, applies to all players.
*include spectators [bool]: whether  spectators can use this keybind, applies only to game specific keybinds.
