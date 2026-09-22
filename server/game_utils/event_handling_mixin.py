"""Mixin providing event handling for games."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..games.base import Player, ActionContext

from .menu_management_mixin import TRANSIENT_DISPLAY_MENU_ID
from .actions import EditboxInput, MenuInput


class EventHandlingMixin:
    """Handle menu/editbox/keybind events for a game.

    Expected Game attributes:
        _destroyed: bool.
        _actions_menu_open: set[str].
        _pending_actions: dict[str, str].
        _keybinds: dict[str, list[Keybind]].
        get_user(player) -> User | None.
        find_action(player, action_id) -> Action | None.
        resolve_action(player, action) -> ResolvedAction.
        execute_action(player, action_id, input_value?, context?).
        get_all_visible_actions(player) -> list[ResolvedAction].
        rebuild_player_menu(player).
        rebuild_all_menus().
        _is_player_spectator(player) -> bool.
    """

    def handle_event(self, player: "Player", event: dict) -> None:
        """Handle an event from a player."""
        if self._destroyed:
            return
        event_type = event.get("type")

        if event_type == "menu":
            self._handle_menu_event(player, event)

        elif event_type == "editbox":
            self._handle_editbox_event(player, event)

        elif event_type == "keybind":
            self._handle_keybind_event(player, event)

    def _handle_menu_event(self, player: "Player", event: dict) -> None:
        """Handle a menu selection event."""
        menu_id = event.get("menu_id")
        selection_id = event.get("selection_id", "")

        if self._is_transient_display_open(player) and menu_id != TRANSIENT_DISPLAY_MENU_ID:
            return
        if player.id in self._pending_actions and menu_id in ("game_menu", "actions_menu"):
            return

        if menu_id == "game_menu":
            self._handle_game_menu_selection(player, event, selection_id)

        elif menu_id == "actions_menu":
            # Actions menu - use selection_id directly
            if selection_id:
                self._handle_actions_menu_selection(player, selection_id)

        elif menu_id == TRANSIENT_DISPLAY_MENU_ID:
            remember_position = getattr(self, "_remember_transient_display_position", None)
            if remember_position:
                remember_position(player, event)
            handler = getattr(self, "_handle_transient_display_selection", None)
            if handler:
                handler(player, selection_id)

        elif menu_id == "game_over":
            self._handle_game_over_selection(player, event)

        elif menu_id == "change_game":
            self._handle_change_game_selection(player, selection_id)

        elif menu_id == "action_input_menu":
            self._handle_action_input_menu(player, event, selection_id)
        elif menu_id == "leave_game_confirm":
            self._handle_leave_game_confirm(player, event, selection_id)

    def _handle_editbox_event(self, player: "Player", event: dict) -> None:
        """Handle an editbox submission event."""
        if self._is_transient_display_open(player):
            return

        input_id = event.get("input_id", "")
        text = event.get("text", "")

        if input_id == "action_input_editbox":
            # Handle action input editbox submission
            if player.id in self._pending_actions:
                action_id = self._pending_actions[player.id]
                action = self.find_action(player, action_id)
                if action and not isinstance(action.input_request, EditboxInput):
                    return
                self._pending_actions.pop(player.id)
                if text:  # Non-empty input
                    self.execute_action(player, action_id, text)
            self.rebuild_player_menu(player)

    def _handle_keybind_event(self, player: "Player", event: dict) -> None:
        """Handle a keybind press event."""
        if self._is_transient_display_open(player) or player.id in self._pending_actions:
            return

        key = self._normalize_keybind(event)
        menu_item_id = event.get("menu_item_id")
        menu_index = event.get("menu_index")

        # Space key speaks option descriptions when not playing
        if key == "space" and getattr(self, "status", "playing") != "playing" and menu_item_id:
            handler = getattr(self, "_speak_option_description", None)
            if handler and handler(player, menu_item_id):
                return

        keybinds = self._keybinds.get(key)
        if keybinds is None:
            return

        is_spectator = self._is_player_spectator(player)

        from ..games.base import ActionContext

        context = ActionContext(
            menu_item_id=menu_item_id,
            menu_index=menu_index,
            from_keybind=True,
        )

        executed_any = self._execute_keybinds(player, keybinds, is_spectator, menu_item_id, context)

        if self._should_rebuild_after_keybind(player, executed_any):
            self.rebuild_all_menus()

    def _handle_actions_menu_selection(self, player: "Player", action_id: str) -> None:
        """Handle selection from the actions menu."""
        # Actions menu is no longer open
        self._actions_menu_open.discard(player.id)
        # Handle "back" - just return to game menu
        if action_id == "go_back":
            self.rebuild_player_menu(player)
            return
        self.execute_action(player, action_id)
        # Don't rebuild if action opened another transient UI
        if (
            player.id not in self._pending_actions
            and not self._is_transient_display_open(player)
            and (
                player.id not in self._actions_menu_open
            )
        ):
            self.rebuild_player_menu(player)

    def _handle_game_menu_selection(self, player: "Player", event: dict, selection_id: str) -> None:
        self._actions_menu_open.discard(player.id)
        if selection_id:
            # A supplied ID is authoritative, even if the action has disappeared.
            accepted = self.execute_action(player, selection_id)
            if accepted and player.id not in self._pending_actions:
                self.rebuild_all_menus()
            return

        selection = event.get("selection", 1) - 1
        visible = self.get_all_visible_actions(player)
        if 0 <= selection < len(visible):
            resolved = visible[selection]
            accepted = self.execute_action(player, resolved.action.id)
            if accepted and player.id not in self._pending_actions:
                self.rebuild_all_menus()

    def _handle_action_input_menu(self, player: "Player", event: dict, selection_id: str) -> None:
        if player.id in self._pending_actions:
            action_id = self._pending_actions[player.id]
            resolved_selection_id = self._resolve_action_input_selection_id(
                player, action_id, event, selection_id
            )
            self._pending_actions.pop(player.id, None)
            if resolved_selection_id and resolved_selection_id != "_cancel":
                self.execute_action(player, action_id, resolved_selection_id)
        if (
            player.id not in self._pending_actions
            and not self._is_transient_display_open(player)
            and player.id not in self._actions_menu_open
        ):
            self.rebuild_player_menu(player)

    def _resolve_action_input_selection_id(
        self, player: "Player", action_id: str, event: dict, selection_id: str = ""
    ) -> str | None:
        action = self.find_action(player, action_id)
        if not action:
            return None
        input_request = action.input_request
        if not isinstance(input_request, MenuInput):
            return None

        options = self._get_menu_options_for_action(action, player)
        if selection_id:
            return selection_id if options and selection_id in options else None

        selection = event.get("selection")
        if not isinstance(selection, int):
            return None
        selection_index = selection - 1

        if options and 0 <= selection_index < len(options):
            return options[selection_index]

        include_cancel = getattr(input_request, "include_cancel", False)
        if include_cancel and options and selection_index == len(options):
            return "_cancel"
        return None

    def _handle_leave_game_confirm(self, player: "Player", event: dict, selection_id: str) -> None:
        user = self.get_user(player)
        if user:
            user.remove_menu("leave_game_confirm")
        if player.id in self._pending_actions:
            self._pending_actions.pop(player.id, None)
        choice = selection_id
        if not choice:
            selection = event.get("selection", 1) - 1
            choice = "yes" if selection == 0 else "no"
        if choice == "yes":
            handler = getattr(self, "_perform_leave_game", None)
            if handler:
                handler(player)
        elif self.status == "finished" and getattr(self, "_last_game_result", None):
            self._show_end_screen(self._last_game_result)
        else:
            self.rebuild_player_menu(player)

    @staticmethod
    def _normalize_keybind(event: dict) -> str:
        key = event.get("key", "").lower()
        if event.get("shift") and not key.startswith("shift+"):
            key = f"shift+{key}"
        if event.get("control") and not key.startswith("ctrl+"):
            key = f"ctrl+{key}"
        if event.get("alt") and not key.startswith("alt+"):
            key = f"alt+{key}"
        return key

    def _execute_keybinds(
        self,
        player: "Player",
        keybinds: list,
        is_spectator: bool,
        menu_item_id: str | None,
        context: "ActionContext",
    ) -> bool:
        executed_any = False
        for keybind in keybinds:
            if not keybind.can_player_use(self, player, is_spectator):
                continue
            if keybind.requires_focus and menu_item_id not in keybind.actions:
                continue
            for action_id in keybind.actions:
                if self.execute_action(player, action_id, context=context):
                    executed_any = True
        return executed_any

    def _should_rebuild_after_keybind(self, player: "Player", executed_any: bool) -> bool:
        return (
            executed_any
            and player.id not in self._pending_actions
            and not self._is_transient_display_open(player)
            and player.id not in self._actions_menu_open
        )
