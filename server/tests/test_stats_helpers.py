"""Tests for statistics helper utilities (leaderboards and ratings)."""

from datetime import datetime

from server.game_utils.game_result import GameResult, PlayerResult
from server.game_utils.stats_helpers import (
    LeaderboardHelper,
    LeaderboardEntry,
    RatingHelper,
)


def make_result(players, custom_data):
    return GameResult(
        game_type="test",
        timestamp=datetime.now().isoformat(),
        duration_ticks=100,
        player_results=[
            PlayerResult(
                player_id=pid,
                player_name=name,
                is_bot=is_bot,
                is_virtual_bot=is_virtual_bot,
            )
            for pid, name, is_bot, is_virtual_bot in players
        ],
        custom_data=custom_data,
    )


def test_leaderboard_helper_aggregations_and_bot_filtering():
    results = [
        make_result(
            [
                ("h1", "Alice", False, False),
                ("b1", "Bot", True, False),
                ("v1", "VBot", True, True),
            ],
            {"scores": {"h1": 10, "v1": 5}},
        ),
        make_result(
            [
                ("h1", "Alice", False, False),
                ("h2", "Bob", False, False),
            ],
            {"scores": {"h1": 4, "h2": 8}},
        ),
    ]

    def score_extractor(result, player_id):
        return result.custom_data["scores"].get(player_id)

    entries = LeaderboardHelper.build_from_results(results, score_extractor, aggregate="sum")
    assert [entry.player_id for entry in entries] == ["h1", "h2", "v1"]
    assert entries[0].value == 14

    avg_entries = LeaderboardHelper.build_from_results(results, score_extractor, aggregate="avg")
    avg_map = {entry.player_id: entry.value for entry in avg_entries}
    assert avg_map["h1"] == 7  # Alice: (10 + 4)/2
    assert avg_map["h2"] == 8

    count_entries = LeaderboardHelper.build_from_results(
        results, score_extractor, aggregate="count"
    )
    assert count_entries[0].value == 2  # Alice appeared twice


def test_leaderboard_helper_invalid_aggregate_and_wins():
    result = make_result(
        [("p1", "Alice", False, False), ("p2", "Bob", False, False)],
        {"winner_name": "Bob"},
    )

    try:
        LeaderboardHelper.build_from_results([result], lambda r, pid: 1, aggregate="median")
    except ValueError as exc:
        assert "Unknown aggregate mode" in str(exc)
    else:
        assert False, "ValueError expected for invalid aggregate"

    wins = LeaderboardHelper.build_wins_leaderboard([result])
    assert wins[0].player_id == "p2"
    assert wins[0].value == 1


class DummyDB:
    def __init__(self):
        self.store = {}

    def get_player_rating(self, player_id, game_type):
        return self.store.get((player_id, game_type))

    def set_player_rating(self, player_id, game_type, mu, sigma):
        self.store[(player_id, game_type)] = (mu, sigma)

    def get_rating_leaderboard(self, game_type, limit):
        rows = [
            (pid, mu, sigma) for (pid, gt), (mu, sigma) in self.store.items() if gt == game_type
        ]
        rows.sort(key=lambda row: row[1] - 3 * row[2], reverse=True)
        return rows[:limit]


def test_rating_helper_update_and_prediction_flow():
    db = DummyDB()
    helper = RatingHelper(db, game_type="test")

    updated = helper.update_ratings([["alice"], ["bob", "carol"]])
    assert set(updated.keys()) == {"alice", "bob", "carol"}
    assert db.get_player_rating("alice", "test") is not None

    result = make_result(
        [
            ("alice", "Alice", False, False),
            ("bob", "Bob", False, False),
            ("bot", "Bot", True, False),
            ("vbot", "VBot", True, True),
        ],
        {"winner_name": "Alice"},
    )
    helper.update_from_result(result)
    alice_rating = helper.get_rating("alice")
    vbot_rating = helper.get_rating("vbot")
    assert alice_rating.mu != helper.DEFAULT_MU  # updated
    assert vbot_rating.mu != helper.DEFAULT_MU  # virtual bot included

    leaderboard = helper.get_leaderboard(limit=5)
    assert leaderboard[0].ordinal >= leaderboard[-1].ordinal

    probability = helper.predict_win_probability("alice", "bob")
    assert 0 <= probability <= 1


def test_ratings_distinguish_tied_individuals_from_actual_teams():
    helper = RatingHelper(DummyDB(), "test")
    tied = helper.update_ratings([["alice", "bob"]])
    assert tied["alice"].mu == tied["bob"].mu
    result = make_result(
        [(name, name, False, False) for name in ("a", "b", "c", "d")], {}
    )
    result.winner_ids = ["a", "c"]
    for player in result.player_results:
        player.team_id = "winners" if player.player_id in result.winner_ids else "others"
    ratings = helper.update_from_result(result)
    assert ratings["a"].mu == ratings["c"].mu > helper.DEFAULT_MU
    assert ratings["b"].mu == ratings["d"].mu < helper.DEFAULT_MU
    wins = {entry.player_id: entry.value for entry in LeaderboardHelper.build_wins_leaderboard([result])}
    assert wins == {"a": 1, "c": 1, "b": 0, "d": 0}
