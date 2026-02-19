"""Mixin providing menu management functionality for games."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..games.base import Player
    from server.core.users.base import User
    from .actions import ResolvedAction

from server.core.users.base import MenuItem, EscapeBehavior


class MenuManagementMixin:
    """Build and update turn menus and status boxes.

    Expected Game attributes:
        _destroyed: bool.
        status: str.
        players: list[Player].
        _status_box_open: set[str].
        get_user(player) -> User | None.
        get_all_visible_actions(player) -> list[ResolvedAction].
    """

    def rebuild_player_menu(
        self, player: "Player", *, position: int | None = None
    ) -> None:
        """Rebuild the turn menu for a player.

        Args:
            player: The player whose menu to rebuild.
            position: Optional 1-based position to focus on. Use position=1
                to reset focus to the first item. When None, the client
                preserves focus on the previously selected item by ID. This
                causes a stuck-cursor bug when an always-visible action (like
                "view pipe") shifts position as turn actions appear/disappear.
                Pass position=1 in _start_turn for the current player to avoid
                this.
        """
        if self._destroyed:
            return  # Don't rebuild menus after game is destroyed
        if self.status == "finished":
            return  # Don't rebuild turn menu after game has ended
        user = self.get_user(player)
        if not user:
            return

        items: list[MenuItem] = []
        for resolved in self.get_all_visible_actions(player):
            items.append(MenuItem(text=resolved.label, id=resolved.action.id, sound=resolved.sound))

        user.show_menu(
            "turn_menu",
            items,
            multiletter=False,
            escape_behavior=EscapeBehavior.KEYBIND,
            position=position,
        )

    def rebuild_all_menus(self) -> None:
        """Rebuild menus for all players."""
        if self._destroyed:
            return  # Don't rebuild menus after game is destroyed
        for player in self.players:
            self.rebuild_player_menu(player)

    def update_player_menu(
        self, player: "Player", selection_id: str | None = None
    ) -> None:
        """Update the turn menu for a player, preserving focus position."""
        if self._destroyed:
            return
        if self.status == "finished":
            return
        user = self.get_user(player)
        if not user:
            return

        items: list[MenuItem] = []
        for resolved in self.get_all_visible_actions(player):
            items.append(MenuItem(text=resolved.label, id=resolved.action.id, sound=resolved.sound))

        user.update_menu("turn_menu", items, selection_id=selection_id)

    def update_all_menus(self) -> None:
        """Update menus for all players, preserving focus position."""
        if self._destroyed:
            return
        for player in self.players:
            self.update_player_menu(player)

    def status_box(self, player: "Player", lines: list[str]) -> None:
        """Show a status box (menu with text items) to a player.

        Press Enter on any item to close. No header or close button needed
        since screen readers speak list items and Enter always closes.
        """
        user = self.get_user(player)
        if user:
            items = [MenuItem(text=line, id="status_line") for line in lines]
            user.show_menu(
                "status_box",
                items,
                multiletter=False,
                escape_behavior=EscapeBehavior.SELECT_LAST,
            )
            self._status_box_open.add(player.id)
