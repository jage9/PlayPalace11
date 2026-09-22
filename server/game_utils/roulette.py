"""Persistent session state for rounds played across different games."""

from dataclasses import dataclass, field, replace

from mashumaro.mixins.json import DataClassJSONMixin

from .game_result import GameResult, PlayerResult


@dataclass
class RouletteSession(DataClassJSONMixin):
    included_games: list[str]
    finish_mode: str = "rounds"
    total_rounds: int = 7
    target_score: int = 2000
    jokers: int = 1
    jokers_remaining: dict[str, int] = field(default_factory=dict)
    round_number: int = 0
    previous_game: str = ""
    scores: dict[str, int | float] = field(default_factory=dict)
    participants: list[PlayerResult] = field(default_factory=list)
    duration_ticks: int = 0

    @property
    def finished(self) -> bool:
        if self.finish_mode == "score":
            return max(self.scores.values(), default=0) >= self.target_score
        return self.round_number >= self.total_rounds

    def record_round(
        self, result: GameResult, *, score_points: dict[str, int | float] | None = None,
    ) -> None:
        """Record session awards without changing the game's native scores."""
        self.duration_ticks += result.duration_ticks
        for player in result.player_results:
            if player.player_id not in self.scores:
                self.participants.append(player)
                self.scores[player.player_id] = 0
        winners = set(result.get_winner_ids())
        scores = (
            {p.player_id: p.score for p in result.player_results}
            if score_points is None else score_points
        )
        has_points = any(scores.get(p.player_id) is not None for p in result.player_results)
        for player in result.player_results:
            if self.finish_mode == "rounds":
                earned = int(player.player_id in winners)
            elif has_points:
                earned = max(0, scores.get(player.player_id) or 0)
            else:
                earned = 100 if player.player_id in winners else 0
            player.session_points = earned
            self.scores[player.player_id] += earned

    def build_result(self, last_round: GameResult) -> GameResult:
        """Use the common result format for the completed roulette session."""
        best = max(self.scores.values(), default=0)
        winners = [pid for pid, score in self.scores.items() if score == best] if best else []
        return GameResult(
            game_type="roulette",
            timestamp=last_round.timestamp,
            duration_ticks=self.duration_ticks,
            player_results=[replace(p, score=self.scores[p.player_id], team_id=None, session_points=None)
                            for p in self.participants],
            winner_ids=winners,
            custom_data={"rounds": self.round_number, "finish_mode": self.finish_mode},
        )
