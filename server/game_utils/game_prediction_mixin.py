"""Mixin providing win probability prediction for games."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..games.base import Player
    from ..users.base import User

from .stats_helpers import RatingHelper
from ..messages.localization import Localization


class GamePredictionMixin:
    """Provide win probability predictions based on ratings.

    Expected Game attributes:
        _table: Table or server reference with DB access.
        players: list[Player].
        get_user(player) -> User | None.
        get_type() -> str.
        status_box(player, lines).
    """

    def _action_predict_outcomes(self, player: "Player", action_id: str) -> None:
        """Show predicted outcomes based on player ratings."""
        user = self.get_user(player)
        if not user:
            return

        rating_helper = self._get_prediction_helper(user)
        if not rating_helper:
            return

        human_players = self._get_predictable_players()
        if len(human_players) < 2:
            user.speak_l("predict-need-players")
            return

        player_ratings = self._collect_player_ratings(rating_helper, human_players)
        lines = self._build_prediction_lines(user, rating_helper, player_ratings)
        self.status_box(player, lines)

    def _get_prediction_helper(self, user: "User") -> RatingHelper | None:
        """Build the rating helper if DB is available."""
        if not self._table or not self._table._db:
            user.speak_l("predict-unavailable")
            return None
        return RatingHelper(self._table._db, self.get_type())

    def _get_predictable_players(self) -> list["Player"]:
        """Return human, non-spectator players."""
        return [p for p in self.players if not p.is_bot and not p.is_spectator]

    def _collect_player_ratings(
        self, rating_helper: RatingHelper, players: list["Player"]
    ) -> list[tuple["Player", Any]]:
        """Collect and sort ratings for the provided players."""
        player_ratings = [(p, rating_helper.get_rating(p.id)) for p in players]
        player_ratings.sort(key=lambda x: x[1].ordinal, reverse=True)
        return player_ratings

    def _build_prediction_lines(
        self,
        user: "User",
        rating_helper: RatingHelper,
        player_ratings: list[tuple["Player", Any]],
    ) -> list[str]:
        """Format prediction lines for display."""
        lines = [Localization.get(user.locale, "predict-header")]
        for rank, (player, rating) in enumerate(player_ratings, 1):
            lines.append(
                self._format_prediction_entry(
                    user, rating_helper, player_ratings, rank, player, rating
                )
            )
        return lines

    def _format_prediction_entry(
        self,
        user: "User",
        rating_helper: RatingHelper,
        player_ratings: list[tuple["Player", Any]],
        rank: int,
        player: "Player",
        rating: Any,
    ) -> str:
        """Format a single prediction entry."""
        if len(player_ratings) == 2:
            other = player_ratings[1] if rank == 1 else player_ratings[0]
            win_prob = rating_helper.predict_win_probability(player.id, other[0].id)
            return Localization.get(
                user.locale,
                "predict-entry-2p",
                rank=rank,
                player=player.name,
                rating=round(rating.ordinal),
                probability=round(win_prob * 100),
            )
        return Localization.get(
            user.locale,
            "predict-entry",
            rank=rank,
            player=player.name,
            rating=round(rating.ordinal),
        )
