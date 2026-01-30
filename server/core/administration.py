"""Administration functionality for the PlayPalace server."""

import functools
from typing import TYPE_CHECKING

from ..users.network_user import NetworkUser
from ..users.base import MenuItem, EscapeBehavior, TrustLevel
from ..messages.localization import Localization

if TYPE_CHECKING:
    from ..persistence.database import Database


def require_admin(func):
    """Decorator that checks if the user is still an admin before executing an admin action."""
    @functools.wraps(func)
    async def wrapper(self, admin, *args, **kwargs):
        if admin.trust_level.value < TrustLevel.ADMIN.value:
            admin.speak_l("not-admin-anymore")
            self._show_main_menu(admin)
            return
        return await func(self, admin, *args, **kwargs)
    return wrapper


def require_server_owner(func):
    """Decorator that checks if the user is the server owner before executing a server owner action."""
    @functools.wraps(func)
    async def wrapper(self, owner, *args, **kwargs):
        if owner.trust_level.value < TrustLevel.SERVER_OWNER.value:
            owner.speak_l("not-server-owner")
            self._show_main_menu(owner)
            return
        return await func(self, owner, *args, **kwargs)
    return wrapper


class AdministrationMixin:
    """
    Mixin class providing administration functionality.

    This mixin expects the following attributes on the class it's mixed into:
    - _db: Database instance
    - _users: dict[str, NetworkUser] of online users
    - _user_states: dict[str, dict] of user menu states
    - _show_main_menu(user): method to show main menu
    """

    _db: "Database"
    _users: dict[str, NetworkUser]
    _user_states: dict[str, dict]

    def _show_main_menu(self, user: NetworkUser) -> None:
        """Show main menu - to be implemented by the main class."""
        raise NotImplementedError

    def _notify_admins(
        self, message_id: str, sound: str, exclude_username: str | None = None
    ) -> None:
        """Notify all online admins with a message and sound, optionally excluding one admin."""
        for username, user in self._users.items():
            if user.trust_level.value < TrustLevel.ADMIN.value:
                continue  # Not an admin
            if exclude_username and username == exclude_username:
                continue  # Skip the excluded admin
            user.speak_l(message_id)
            user.play_sound(sound)

    # ==================== Menu Display Functions ====================

    def _show_admin_menu(self, user: NetworkUser) -> None:
        """Show administration menu."""
        items = [
            MenuItem(
                text=Localization.get(user.locale, "account-approval"),
                id="account_approval",
            ),
        ]
        # Only server owners can promote/demote admins, transfer ownership, and manage virtual bots
        if user.trust_level.value >= TrustLevel.SERVER_OWNER.value:
            items.append(
                MenuItem(
                    text=Localization.get(user.locale, "promote-admin"),
                    id="promote_admin",
                )
            )
            items.append(
                MenuItem(
                    text=Localization.get(user.locale, "demote-admin"),
                    id="demote_admin",
                )
            )
            items.append(
                MenuItem(
                    text=Localization.get(user.locale, "transfer-ownership"),
                    id="transfer_ownership",
                )
            )
            items.append(
                MenuItem(
                    text=Localization.get(user.locale, "virtual-bots"),
                    id="virtual_bots",
                )
            )
        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))
        user.show_menu(
            "admin_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {"menu": "admin_menu"}

    def _show_account_approval_menu(self, user: NetworkUser) -> None:
        """Show account approval menu with pending users."""
        pending = self._db.get_pending_users()

        if not pending:
            user.speak_l("no-pending-accounts")
            self._show_admin_menu(user)
            return

        items = []
        for pending_user in pending:
            items.append(MenuItem(text=pending_user.username, id=f"pending_{pending_user.username}"))
        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "account_approval_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {"menu": "account_approval_menu"}

    def _show_pending_user_actions_menu(self, user: NetworkUser, pending_username: str) -> None:
        """Show actions for a pending user (approve, decline)."""
        items = [
            MenuItem(text=Localization.get(user.locale, "approve-account"), id="approve"),
            MenuItem(text=Localization.get(user.locale, "decline-account"), id="decline"),
            MenuItem(text=Localization.get(user.locale, "back"), id="back"),
        ]
        user.show_menu(
            "pending_user_actions_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {
            "menu": "pending_user_actions_menu",
            "pending_username": pending_username,
        }

    def _show_promote_admin_menu(self, user: NetworkUser) -> None:
        """Show promote admin menu with list of non-admin users."""
        non_admins = self._db.get_non_admin_users()

        if not non_admins:
            user.speak_l("no-users-to-promote")
            self._show_admin_menu(user)
            return

        items = []
        for non_admin in non_admins:
            items.append(MenuItem(text=non_admin.username, id=f"promote_{non_admin.username}"))
        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "promote_admin_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {"menu": "promote_admin_menu"}

    def _show_demote_admin_menu(self, user: NetworkUser) -> None:
        """Show demote admin menu with list of admin users."""
        # Exclude server owner from demotion list
        admins = self._db.get_admin_users(include_server_owner=False)

        # Filter out the current user (can't demote yourself)
        admins = [a for a in admins if a.username != user.username]

        if not admins:
            user.speak_l("no-admins-to-demote")
            self._show_admin_menu(user)
            return

        items = []
        for admin in admins:
            items.append(MenuItem(text=admin.username, id=f"demote_{admin.username}"))
        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "demote_admin_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {"menu": "demote_admin_menu"}

    def _show_promote_confirm_menu(self, user: NetworkUser, target_username: str) -> None:
        """Show confirmation menu for promoting a user to admin."""
        user.speak_l("confirm-promote", player=target_username)
        items = [
            MenuItem(text=Localization.get(user.locale, "confirm-yes"), id="yes"),
            MenuItem(text=Localization.get(user.locale, "confirm-no"), id="no"),
        ]
        user.show_menu(
            "promote_confirm_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {
            "menu": "promote_confirm_menu",
            "target_username": target_username,
        }

    def _show_demote_confirm_menu(self, user: NetworkUser, target_username: str) -> None:
        """Show confirmation menu for demoting an admin."""
        user.speak_l("confirm-demote", player=target_username)
        items = [
            MenuItem(text=Localization.get(user.locale, "confirm-yes"), id="yes"),
            MenuItem(text=Localization.get(user.locale, "confirm-no"), id="no"),
        ]
        user.show_menu(
            "demote_confirm_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {
            "menu": "demote_confirm_menu",
            "target_username": target_username,
        }

    def _show_broadcast_choice_menu(self, user: NetworkUser, action: str, target_username: str) -> None:
        """Show menu to choose broadcast audience (all users, admins only, or nobody/silent)."""
        items = [
            MenuItem(text=Localization.get(user.locale, "broadcast-to-all"), id="all"),
            MenuItem(text=Localization.get(user.locale, "broadcast-to-admins"), id="admins"),
            MenuItem(text=Localization.get(user.locale, "broadcast-to-nobody"), id="nobody"),
        ]
        user.show_menu(
            "broadcast_choice_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {
            "menu": "broadcast_choice_menu",
            "action": action,  # "promote" or "demote"
            "target_username": target_username,
        }

    def _show_transfer_ownership_menu(self, user: NetworkUser) -> None:
        """Show transfer ownership menu with list of admin users."""
        # Only admins can receive ownership (exclude server owner)
        admins = self._db.get_admin_users(include_server_owner=False)

        if not admins:
            user.speak_l("no-admins-for-transfer")
            self._show_admin_menu(user)
            return

        items = []
        for admin in admins:
            items.append(MenuItem(text=admin.username, id=f"transfer_{admin.username}"))
        items.append(MenuItem(text=Localization.get(user.locale, "back"), id="back"))

        user.show_menu(
            "transfer_ownership_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {"menu": "transfer_ownership_menu"}

    def _show_transfer_ownership_confirm_menu(self, user: NetworkUser, target_username: str) -> None:
        """Show confirmation menu for transferring ownership."""
        user.speak_l("confirm-transfer-ownership", player=target_username)
        items = [
            MenuItem(text=Localization.get(user.locale, "confirm-yes"), id="yes"),
            MenuItem(text=Localization.get(user.locale, "confirm-no"), id="no"),
        ]
        user.show_menu(
            "transfer_ownership_confirm_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {
            "menu": "transfer_ownership_confirm_menu",
            "target_username": target_username,
        }

    def _show_transfer_broadcast_choice_menu(self, user: NetworkUser, target_username: str) -> None:
        """Show menu to choose broadcast audience for ownership transfer."""
        items = [
            MenuItem(text=Localization.get(user.locale, "broadcast-to-all"), id="all"),
            MenuItem(text=Localization.get(user.locale, "broadcast-to-admins"), id="admins"),
            MenuItem(text=Localization.get(user.locale, "broadcast-to-nobody"), id="nobody"),
        ]
        user.show_menu(
            "transfer_broadcast_choice_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {
            "menu": "transfer_broadcast_choice_menu",
            "target_username": target_username,
        }

    def _show_virtual_bots_menu(self, user: NetworkUser) -> None:
        """Show virtual bots management menu."""
        # Get current status if manager exists
        status_text = ""
        if hasattr(self, "_virtual_bots") and self._virtual_bots:
            status = self._virtual_bots.get_status()
            status_text = f" ({status['online']}/{status['total']})"

        items = [
            MenuItem(
                text=Localization.get(user.locale, "virtual-bots-fill") + status_text,
                id="fill",
            ),
            MenuItem(
                text=Localization.get(user.locale, "virtual-bots-clear"),
                id="clear",
            ),
            MenuItem(
                text=Localization.get(user.locale, "virtual-bots-status"),
                id="status",
            ),
            MenuItem(text=Localization.get(user.locale, "back"), id="back"),
        ]
        user.show_menu(
            "virtual_bots_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {"menu": "virtual_bots_menu"}

    def _show_virtual_bots_clear_confirm_menu(self, user: NetworkUser) -> None:
        """Show confirmation menu for clearing all virtual bots."""
        user.speak_l("virtual-bots-clear-confirm")
        items = [
            MenuItem(text=Localization.get(user.locale, "confirm-yes"), id="yes"),
            MenuItem(text=Localization.get(user.locale, "confirm-no"), id="no"),
        ]
        user.show_menu(
            "virtual_bots_clear_confirm_menu",
            items,
            multiletter=True,
            escape_behavior=EscapeBehavior.SELECT_LAST,
        )
        self._user_states[user.username] = {"menu": "virtual_bots_clear_confirm_menu"}

    # ==================== Menu Selection Handlers ====================

    async def _handle_admin_menu_selection(
        self, user: NetworkUser, selection_id: str
    ) -> None:
        """Handle admin menu selection."""
        if selection_id == "account_approval":
            self._show_account_approval_menu(user)
        elif selection_id == "promote_admin":
            self._show_promote_admin_menu(user)
        elif selection_id == "demote_admin":
            self._show_demote_admin_menu(user)
        elif selection_id == "transfer_ownership":
            self._show_transfer_ownership_menu(user)
        elif selection_id == "virtual_bots":
            self._show_virtual_bots_menu(user)
        elif selection_id == "back":
            self._show_main_menu(user)

    async def _handle_account_approval_selection(
        self, user: NetworkUser, selection_id: str
    ) -> None:
        """Handle account approval menu selection."""
        if selection_id == "back":
            self._show_admin_menu(user)
        elif selection_id.startswith("pending_"):
            pending_username = selection_id[8:]  # Remove "pending_" prefix
            self._show_pending_user_actions_menu(user, pending_username)

    async def _handle_pending_user_actions_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle pending user actions menu selection."""
        pending_username = state.get("pending_username")
        if not pending_username:
            self._show_account_approval_menu(user)
            return

        if selection_id == "approve":
            await self._approve_user(user, pending_username)
        elif selection_id == "decline":
            self._show_decline_reason_editbox(user, pending_username)
        elif selection_id == "back":
            self._show_account_approval_menu(user)

    def _show_decline_reason_editbox(self, user: NetworkUser, pending_username: str) -> None:
        """Show editbox for entering decline reason."""
        prompt = Localization.get(user.locale, "decline-reason-prompt")
        user.show_editbox(
            "decline_reason",
            prompt,
            default_value="",
            multiline=False,
            read_only=False,
        )
        self._user_states[user.username] = {
            "menu": "decline_reason_editbox",
            "pending_username": pending_username,
        }

    async def _handle_decline_reason_editbox(
        self, admin: NetworkUser, text: str, state: dict
    ) -> None:
        """Handle decline reason editbox submission."""
        pending_username = state.get("pending_username")
        if not pending_username:
            self._show_account_approval_menu(admin)
            return

        # Proceed with decline, passing the reason (empty text uses fallback)
        await self._decline_user(admin, pending_username, reason=text)

    async def _handle_promote_admin_selection(
        self, user: NetworkUser, selection_id: str
    ) -> None:
        """Handle promote admin menu selection."""
        if selection_id == "back":
            self._show_admin_menu(user)
        elif selection_id.startswith("promote_"):
            target_username = selection_id[8:]  # Remove "promote_" prefix
            self._show_promote_confirm_menu(user, target_username)

    async def _handle_demote_admin_selection(
        self, user: NetworkUser, selection_id: str
    ) -> None:
        """Handle demote admin menu selection."""
        if selection_id == "back":
            self._show_admin_menu(user)
        elif selection_id.startswith("demote_"):
            target_username = selection_id[7:]  # Remove "demote_" prefix
            self._show_demote_confirm_menu(user, target_username)

    async def _handle_promote_confirm_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle promote confirmation menu selection."""
        target_username = state.get("target_username")
        if not target_username:
            self._show_promote_admin_menu(user)
            return

        if selection_id == "yes":
            # Show broadcast choice menu
            self._show_broadcast_choice_menu(user, "promote", target_username)
        else:
            # No or back - return to promote admin menu
            self._show_promote_admin_menu(user)

    async def _handle_demote_confirm_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle demote confirmation menu selection."""
        target_username = state.get("target_username")
        if not target_username:
            self._show_demote_admin_menu(user)
            return

        if selection_id == "yes":
            # Show broadcast choice menu
            self._show_broadcast_choice_menu(user, "demote", target_username)
        else:
            # No or back - return to demote admin menu
            self._show_demote_admin_menu(user)

    async def _handle_broadcast_choice_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle broadcast choice menu selection."""
        action = state.get("action")
        target_username = state.get("target_username")

        if not action or not target_username:
            self._show_admin_menu(user)
            return

        # Determine broadcast scope: "all", "admins", or "nobody"
        broadcast_scope = selection_id  # "all", "admins", or "nobody"

        if action == "promote":
            await self._promote_to_admin(user, target_username, broadcast_scope)
        elif action == "demote":
            await self._demote_from_admin(user, target_username, broadcast_scope)

    async def _handle_transfer_ownership_selection(
        self, user: NetworkUser, selection_id: str
    ) -> None:
        """Handle transfer ownership menu selection."""
        if selection_id == "back":
            self._show_admin_menu(user)
        elif selection_id.startswith("transfer_"):
            target_username = selection_id[9:]  # Remove "transfer_" prefix
            self._show_transfer_ownership_confirm_menu(user, target_username)

    async def _handle_transfer_ownership_confirm_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle transfer ownership confirmation menu selection."""
        target_username = state.get("target_username")
        if not target_username:
            self._show_transfer_ownership_menu(user)
            return

        if selection_id == "yes":
            # Show broadcast choice menu
            self._show_transfer_broadcast_choice_menu(user, target_username)
        else:
            # No or back - return to transfer ownership menu
            self._show_transfer_ownership_menu(user)

    async def _handle_transfer_broadcast_choice_selection(
        self, user: NetworkUser, selection_id: str, state: dict
    ) -> None:
        """Handle transfer broadcast choice menu selection."""
        target_username = state.get("target_username")

        if not target_username:
            self._show_admin_menu(user)
            return

        # Determine broadcast scope: "all", "admins", or "nobody"
        broadcast_scope = selection_id

        await self._transfer_ownership(user, target_username, broadcast_scope)

    async def _handle_virtual_bots_selection(
        self, user: NetworkUser, selection_id: str
    ) -> None:
        """Handle virtual bots menu selection."""
        if selection_id == "fill":
            await self._fill_virtual_bots(user)
        elif selection_id == "clear":
            self._show_virtual_bots_clear_confirm_menu(user)
        elif selection_id == "status":
            await self._show_virtual_bots_status(user)
        elif selection_id == "back":
            self._show_admin_menu(user)

    async def _handle_virtual_bots_clear_confirm_selection(
        self, user: NetworkUser, selection_id: str
    ) -> None:
        """Handle virtual bots clear confirmation menu selection."""
        if selection_id == "yes":
            await self._clear_virtual_bots(user)
        else:
            self._show_virtual_bots_menu(user)

    # ==================== Admin Actions ====================

    @require_admin
    async def _approve_user(self, admin: NetworkUser, username: str) -> None:
        """Approve a pending user account."""
        if self._db.approve_user(username):
            admin.speak_l("account-approved", player=username)

            # Notify other admins of the account action
            self._notify_admins(
                "account-action", "accountactionnotify.ogg", exclude_username=admin.username
            )

            # Check if the user is online and waiting for approval
            waiting_user = self._users.get(username)
            if waiting_user:
                # Update the user's approved status so they can now interact
                waiting_user.set_approved(True)

                waiting_state = self._user_states.get(username, {})
                if waiting_state.get("menu") == "waiting_for_approval":
                    # User is online and waiting - welcome them and show main menu
                    waiting_user.speak_l("account-approved-welcome")
                    waiting_user.play_sound("accountapprove.ogg")
                    self._show_main_menu(waiting_user)

        self._show_account_approval_menu(admin)

    @require_admin
    async def _decline_user(self, admin: NetworkUser, username: str, reason: str = "") -> None:
        """Decline and delete a pending user account."""
        # Check if the user is online first
        waiting_user = self._users.get(username)

        if self._db.delete_user(username):
            admin.speak_l("account-declined", player=username)

            # Notify other admins of the account action
            self._notify_admins(
                "account-action", "accountactionnotify.ogg", exclude_username=admin.username
            )

            # If user is online, disconnect them with the reason
            if waiting_user:
                # Build the full decline message with reason
                decline_message = Localization.get(
                    waiting_user.locale, "account-declined-goodbye"
                )
                display_reason = reason.strip() if reason else ""
                if not display_reason:
                    display_reason = Localization.get(
                        waiting_user.locale, "approval-reject-no-reason"
                    )
                # Combine into single message for the dialog
                full_message = f"{decline_message}\n{display_reason}"
                waiting_user.speak(full_message)
                # Flush queued messages before disconnect so client receives them
                for msg in waiting_user.get_queued_messages():
                    await waiting_user.connection.send(msg)
                await waiting_user.connection.send({
                    "type": "disconnect",
                    "reconnect": False,
                    "show_message": True,
                })

        self._show_account_approval_menu(admin)

    @require_server_owner
    async def _promote_to_admin(
        self, owner: NetworkUser, username: str, broadcast_scope: str
    ) -> None:
        """Promote a user to admin. Only server owner can do this."""
        # Update trust level in database
        self._db.update_user_trust_level(username, TrustLevel.ADMIN)

        # Update the user's trust level if they are online
        target_user = self._users.get(username)
        if target_user:
            target_user.set_trust_level(TrustLevel.ADMIN)

        # Always notify the target user with personalized message
        if target_user:
            target_user.speak_l("promote-announcement-you")
            target_user.play_sound("accountpromoteadmin.ogg")

        # Broadcast the announcement to others based on scope
        if broadcast_scope == "nobody":
            # Silent mode - only notify the server owner who performed the action
            owner.speak_l("promote-announcement", player=username)
            owner.play_sound("accountpromoteadmin.ogg")
        else:
            # Broadcast to all or admins (excluding the target user who already got personalized message)
            self._broadcast_admin_change(
                "promote-announcement",
                "accountpromoteadmin.ogg",
                username,
                broadcast_scope,
                exclude_username=username,
            )

        self._show_admin_menu(owner)

    @require_server_owner
    async def _demote_from_admin(
        self, owner: NetworkUser, username: str, broadcast_scope: str
    ) -> None:
        """Demote an admin to regular user. Only server owner can do this."""
        # Update trust level in database
        self._db.update_user_trust_level(username, TrustLevel.USER)

        # Update the user's trust level if they are online
        target_user = self._users.get(username)
        if target_user:
            target_user.set_trust_level(TrustLevel.USER)

        # Always notify the target user with personalized message
        if target_user:
            target_user.speak_l("demote-announcement-you")
            target_user.play_sound("accountdemoteadmin.ogg")

        # Broadcast the announcement to others based on scope
        if broadcast_scope == "nobody":
            # Silent mode - only notify the server owner who performed the action
            owner.speak_l("demote-announcement", player=username)
            owner.play_sound("accountdemoteadmin.ogg")
        else:
            # Broadcast to all or admins (excluding the target user who already got personalized message)
            self._broadcast_admin_change(
                "demote-announcement",
                "accountdemoteadmin.ogg",
                username,
                broadcast_scope,
                exclude_username=username,
            )

        self._show_admin_menu(owner)

    def _broadcast_admin_change(
        self,
        message_id: str,
        sound: str,
        player_name: str,
        broadcast_scope: str,
        exclude_username: str | None = None,
    ) -> None:
        """Broadcast an admin promotion/demotion announcement."""
        for username, user in self._users.items():
            if not user.approved:
                continue  # Don't send broadcasts to unapproved users
            if exclude_username and username == exclude_username:
                continue  # Skip the excluded user
            if broadcast_scope == "admins" and user.trust_level.value < TrustLevel.ADMIN.value:
                continue  # Only admins if broadcasting to admins only
            user.speak_l(message_id, player=player_name)
            user.play_sound(sound)

    @require_server_owner
    async def _transfer_ownership(
        self, owner: NetworkUser, username: str, broadcast_scope: str
    ) -> None:
        """Transfer server ownership to another admin. Only server owner can do this."""
        # Update new owner to SERVER_OWNER
        self._db.update_user_trust_level(username, TrustLevel.SERVER_OWNER)

        # Demote current owner to ADMIN
        self._db.update_user_trust_level(owner.username, TrustLevel.ADMIN)

        # Update the new owner's trust level if they are online
        target_user = self._users.get(username)
        if target_user:
            target_user.set_trust_level(TrustLevel.SERVER_OWNER)

        # Update current owner's trust level
        owner.set_trust_level(TrustLevel.ADMIN)

        # Always notify the target user with personalized message
        if target_user:
            target_user.speak_l("transfer-ownership-announcement-you")
            target_user.play_sound("accounttransferownership.ogg")

        # Broadcast the announcement to others based on scope
        if broadcast_scope == "nobody":
            # Silent mode - only notify the former owner who performed the action
            owner.speak_l("transfer-ownership-announcement", player=username)
            owner.play_sound("accounttransferownership.ogg")
        else:
            # Broadcast to all or admins (excluding the target user who already got personalized message)
            self._broadcast_admin_change(
                "transfer-ownership-announcement",
                "accounttransferownership.ogg",
                username,
                broadcast_scope,
                exclude_username=username,
            )

        self._show_admin_menu(owner)

    # ==================== Virtual Bot Actions ====================

    @require_server_owner
    async def _fill_virtual_bots(self, owner: NetworkUser) -> None:
        """Fill the server with virtual bots from config."""
        if not hasattr(self, "_virtual_bots") or not self._virtual_bots:
            owner.speak_l("virtual-bots-not-available")
            self._show_virtual_bots_menu(owner)
            return

        added, online = self._virtual_bots.fill_server()
        if added > 0:
            owner.speak_l("virtual-bots-filled", added=added, online=online)
            # Save state after filling
            self._virtual_bots.save_state()
        else:
            owner.speak_l("virtual-bots-already-filled")

        self._show_virtual_bots_menu(owner)

    @require_server_owner
    async def _clear_virtual_bots(self, owner: NetworkUser) -> None:
        """Clear all virtual bots from the server."""
        if not hasattr(self, "_virtual_bots") or not self._virtual_bots:
            owner.speak_l("virtual-bots-not-available")
            self._show_virtual_bots_menu(owner)
            return

        bots_cleared, tables_killed = self._virtual_bots.clear_bots()
        if bots_cleared > 0:
            owner.speak_l(
                "virtual-bots-cleared",
                bots=bots_cleared,
                tables=tables_killed,
            )
        else:
            owner.speak_l("virtual-bots-none-to-clear")

        self._show_virtual_bots_menu(owner)

    @require_server_owner
    async def _show_virtual_bots_status(self, owner: NetworkUser) -> None:
        """Show virtual bots status."""
        if not hasattr(self, "_virtual_bots") or not self._virtual_bots:
            owner.speak_l("virtual-bots-not-available")
            self._show_virtual_bots_menu(owner)
            return

        status = self._virtual_bots.get_status()
        owner.speak_l(
            "virtual-bots-status-report",
            total=status["total"],
            online=status["online"],
            offline=status["offline"],
            in_game=status["in_game"],
        )
        self._show_virtual_bots_menu(owner)
