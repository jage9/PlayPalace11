"""Mixin providing game result handling and persistence."""

from typing import TYPE_CHECKING, Any
from datetime import datetime

from .game_status import GameStatus

if TYPE_CHECKING:
    from ..games.base import Player

from .game_result import GameResult, PlayerResult
from .stats_helpers import RatingHelper
from ..messages.localization import Localization
from server.core.users.base import MenuItem, EscapeBehavior


class GameResultMixin:
    """Build, persist, and display game results.

    Expected Game attributes:
        game_active: bool.
        status: str.
        players: list[Player].
        sound_scheduler_tick: int.
        _table: Table or server reference.
        _is_transient_display_open(player) -> bool.
        _close_transient_display(player, rebuild_menu=False).
        get_user(player) -> User | None.
        get_type() -> str.
        get_active_players() -> list[Player].
        destroy().
    """

    def finish_game(self, show_end_screen: bool = True, *, result: GameResult | None = None) -> None:
        """Mark the game as finished, persist result, and optionally show end screen.

        Call this instead of setting status directly to ensure proper cleanup.
        If no humans remain, the table is automatically destroyed.

        Args:
            show_end_screen: Whether to show the end screen (default True).
                             Set to False if you want to show it manually.
            result: A completed round result when ending a roulette round early.
        """
        if self._last_game_result is not None:
            return
        self.clear_game_ui()
        self.game_active = False
        self.status = GameStatus.FINISHED
        self._sync_table_status()

        # Build and persist the game result
        result = result or self.build_game_result()
        self._last_game_result = result
        if self.roulette:
            self.event_queue.clear()
            self.roulette.record_round(result)
            if self.roulette.finished:
                self._persist_result(self.roulette.build_result(result))
        else:
            self._persist_result(result)

        # Show end screen
        if show_end_screen:
            self._show_end_screen(result)

        # Auto-destroy if no humans remain (bot-only games, but not virtual bot games)
        has_humans = any(not p.is_bot or getattr(p, "is_virtual_bot", False) for p in self.players)
        if not has_humans:
            self.destroy()

    def finish_round(
        self,
        winner_ids: list[str] | None = None,
        scores: dict[str, int | float] | None = None,
    ) -> bool:
        """Stop at a completed hand/round only when this is a roulette session.

        Games call this after scoring and before resetting for their next round.
        Explicit scores are earned points by player ID; an empty mapping denotes
        a game without points, which receives roulette's win award instead.
        """
        if self.roulette is None:
            return False
        if self._last_game_result is not None:
            return True
        result = self.build_game_result()
        if scores is not None:
            for player in result.player_results:
                player.score = scores.get(player.player_id)
        if winner_ids is not None:
            result.winner_ids = winner_ids
        else:
            scored_players = [p for p in result.player_results if p.score is not None]
            if scored_players:
                best = max(p.score for p in scored_players)
                result.winner_ids = [p.player_id for p in scored_players if p.score == best]
        self.finish_game(result=result)
        return True

    def build_game_result(self) -> GameResult:
        """Build the game result. Override in subclasses for custom data.

        Returns:
            A GameResult with game-specific data in custom_data.
        """
        return self.make_game_result(custom_data={})

    def get_result_players(self) -> list["Player"]:
        """Include eliminated participants, while excluding people who only watched."""
        return [p for p in self.players if not p.is_spectator or p.eliminated]

    def eliminate_player(self, player: "Player") -> None:
        """Remove a player from turn order without losing their participation."""
        player.eliminated = True
        player.is_spectator = True

    def make_game_result(self, *, custom_data: dict[str, Any]) -> GameResult:
        """Build common result data; games retain their own scoring and win rules."""
        players = self.get_result_players()
        scores = custom_data.get("final_scores", custom_data.get("final_light", {}))
        manager = self.team_manager
        player_results = []
        for player in players:
            team = manager.get_team(player.name)
            score_name = manager.get_team_name(team) if team else player.name
            player_results.append(PlayerResult(
                player_id=player.id,
                player_name=player.name,
                is_bot=player.is_bot and not player.replaced_human,
                is_virtual_bot=player.is_virtual_bot,
                score=scores.get(player.name, scores.get(score_name)),
                team_id=str(team.index) if team and len(team.members) > 1 else None,
            ))
        result = GameResult(
            game_type=self.get_type(),
            timestamp=datetime.now().isoformat(),
            duration_ticks=self.sound_scheduler_tick,
            player_results=player_results,
            custom_data=custom_data,
        )
        result.winner_ids = result.get_winner_ids()
        # Team games historically stored the team's display name as the winner.
        names = custom_data.get("winner_names", [custom_data.get("winner_name")])
        if not result.winner_ids:
            winner_names = {
                name for team in manager.teams
                if manager.get_team_name(team) in names
                for name in team.members
            }
            result.winner_ids = [p.id for p in players if p.name in winner_names]
        return result

    def format_end_screen(self, result: GameResult, locale: str) -> list[str]:
        """Format the end screen lines from a game result. Override for custom display.

        Args:
            result: The game result to format
            locale: The locale to use for localization

        Returns:
            List of lines to display on the end screen
        """
        # Default implementation - just show "Game Over" and player names
        lines = [Localization.get(locale, "game-over")]
        for p in result.player_results:
            lines.append(p.player_name)
        return lines

    def _persist_result(self, result: GameResult) -> None:
        """Persist the game result to the database and update ratings."""
        # Only persist if there are human players
        if not result.has_human_players():
            return

        if self._table:
            self._table.save_game_result(result)
            # Update player ratings
            self._update_ratings(result)

    def _update_ratings(self, result: GameResult) -> None:
        """Update player ratings based on game result."""
        if not self._table or not self._table._db:
            return

        RatingHelper(self._table._db, result.game_type).update_from_result(result)

    def get_rankings_for_rating(self, result: GameResult) -> list[list[str]]:
        """Get player placement groups from the shared result contract.

        Returns a list of player ID groups ordered by placement.
        First group = 1st place, second = 2nd place, etc.
        Players in same group = tie for that position.

        Default: Winner first, everyone else tied for second.
        """
        return result.get_rankings()

    def _end_screen_items(self, result: GameResult, player: "Player", locale: str) -> list[MenuItem]:
        """Build result lines and the actions available to this table member."""
        items = [MenuItem(text=line, id="score_line")
                 for line in self.format_end_screen(result, locale)]
        if self.roulette:
            session = self.roulette
            items.append(MenuItem(text=Localization.get(locale, "roulette-standings"), id="score_line"))
            for participant in sorted(session.participants,
                                      key=lambda p: session.scores[p.player_id], reverse=True):
                items.append(MenuItem(text=Localization.get(
                    locale, "roulette-score", player=participant.player_name,
                    score=session.scores[participant.player_id]), id="score_line"))
            if session.finished:
                items.append(MenuItem(text=Localization.get(locale, "roulette-finished"), id="score_line"))
            elif self._table and player.name == self.host:
                items.append(MenuItem(text=Localization.get(locale, "roulette-next-round"), id="roulette_next"))
        if getattr(self, "_table", None) and player.name == self.host:
            if not self.roulette or self.roulette.finished:
                items.append(MenuItem(text=Localization.get(locale, "game-play-again"), id="play_again"))
            items.append(MenuItem(text=Localization.get(locale, "game-change-game"), id="change_game"))
        items.append(MenuItem(text=Localization.get(locale, "game-leave"), id="leave_game"))
        return items

    def _show_end_screen(self, result: GameResult, recipient: "Player | None" = None) -> None:
        """Show the end screen to all players using structured result."""
        for player in ([recipient] if recipient is not None else self.players):
            if self._is_transient_display_open(player):
                self._close_transient_display(player, rebuild_menu=False)
            user = self.get_user(player)
            if user:
                items = self._end_screen_items(result, player, user.locale)
                user.show_menu("game_over", items, multiletter=False)

    def _handle_game_over_selection(self, player: "Player", event: dict) -> None:
        """Handle only known end-screen actions; selecting a score does nothing."""
        selection = event.get("selection_id", "")
        if not selection and self._last_game_result:
            user = self.get_user(player)
            if user:
                items = self._end_screen_items(self._last_game_result, player, user.locale)
                index = event.get("selection", 0) - 1
                if 0 <= index < len(items):
                    selection = items[index].id
        if selection == "leave_game":
            self.execute_action(player, "leave_game")
        elif self.status == GameStatus.FINISHED and self._table and player.name == self.host:
            if selection == "play_again":
                self._table.prepare_next_game(player.name, "roulette" if self.roulette else None)
            elif selection == "change_game":
                self._show_change_game_menu(player)
            elif selection == "roulette_next" and self.roulette and not self.roulette.finished:
                self._table.start_roulette_round()
