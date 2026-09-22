"""
Scoring logic for Scopa game.

Handles round scoring, winner detection, and game end.
"""

from typing import TYPE_CHECKING

from ...game_utils.cards import Card
from ...game_utils.teams import Team

if TYPE_CHECKING:
    from .game import ScopaGame, ScopaPlayer


def get_team_captured_cards(players: list["ScopaPlayer"], team: Team) -> list[Card]:
    """Get all cards captured by team members."""
    cards = []
    for player in players:
        if player.name in team.members:
            cards.extend(player.captured)
    return cards


def score_round(game: "ScopaGame") -> None:
    """
    Calculate and award round scores.

    Awards points for:
    - Most cards (1 point)
    - Most diamonds (1 point)
    - 7 of diamonds (1 point)
    - Most sevens (1 point)
    """
    game.broadcast_l("scopa-scoring-round")

    teams = game.team_manager.get_alive_teams()
    if not teams:
        teams = game.team_manager.teams

    # Build team card data
    team_data: list[tuple[Team, list[Card]]] = []
    for team in teams:
        if game.options.team_card_scoring:
            cards = get_team_captured_cards(game.players, team)
            team_data.append((team, cards))
        else:
            # Compare individual captures, then credit each award to the actual team.
            for player in game.players:
                if player.name in team.members:
                    scorer = Team(index=team.index, members=[player.name])
                    team_data.append((scorer, player.captured))

    _award_most_cards(game, team_data)
    _award_most_diamonds(game, team_data)
    _award_seven_of_diamonds(game, team_data)
    _award_most_sevens(game, team_data)

    # Announce round scores
    game.broadcast_l("scopa-round-scores")
    for team in teams:
        name = game.team_manager.get_team_name(team)
        game.broadcast_l(
            "scopa-round-score-line",
            player=name,
            round_score=team.round_score,
            total_score=team.total_score,
        )

    # Play round end sound
    game.play_sound("game_pig/win.ogg")


def _award_most_cards(game: "ScopaGame", team_data: list[tuple[Team, list[Card]]]) -> None:
    card_counts = [(team, len(cards)) for team, cards in team_data]
    max_cards = max(count for _, count in card_counts)
    winners = [team for team, count in card_counts if count == max_cards]
    if len(winners) == 1:
        _award_round_point(game, winners[0], "scopa-most-cards", count=max_cards)
    else:
        game.broadcast_l("scopa-most-cards-tie")


def _award_most_diamonds(game: "ScopaGame", team_data: list[tuple[Team, list[Card]]]) -> None:
    diamond_counts = [(team, sum(1 for c in cards if c.suit == 1)) for team, cards in team_data]
    max_diamonds = max(count for _, count in diamond_counts)
    if max_diamonds <= 0:
        return
    winners = [team for team, count in diamond_counts if count == max_diamonds]
    if len(winners) == 1:
        _award_round_point(game, winners[0], "scopa-most-diamonds", count=max_diamonds)
    else:
        game.broadcast_l("scopa-most-diamonds-tie")


def _award_seven_of_diamonds(game: "ScopaGame", team_data: list[tuple[Team, list[Card]]]) -> None:
    seven_diamond_counts = [
        (team, sum(1 for c in cards if c.rank == 7 and c.suit == 1)) for team, cards in team_data
    ]
    max_seven_diamonds = max(count for _, count in seven_diamond_counts)
    if max_seven_diamonds <= 0:
        return
    winners = [team for team, count in seven_diamond_counts if count == max_seven_diamonds]
    if len(winners) == 1:
        _award_round_point(
            game,
            winners[0],
            "scopa-seven-diamonds",
            count=max_seven_diamonds,
            plural_key="scopa-seven-diamonds-multi",
        )
    else:
        game.broadcast_l("scopa-seven-diamonds-tie")


def _award_most_sevens(game: "ScopaGame", team_data: list[tuple[Team, list[Card]]]) -> None:
    seven_counts = [(team, sum(1 for c in cards if c.rank == 7)) for team, cards in team_data]
    max_sevens = max(count for _, count in seven_counts)
    if max_sevens <= 0:
        return
    winners = [team for team, count in seven_counts if count == max_sevens]
    if len(winners) == 1:
        _award_round_point(game, winners[0], "scopa-most-sevens", count=max_sevens)
    else:
        game.broadcast_l("scopa-most-sevens-tie")


def _award_round_point(
    game: "ScopaGame",
    team: Team,
    message_key: str,
    *,
    count: int | None = None,
    plural_key: str | None = None,
) -> None:
    game.team_manager.add_to_team_round_score(team.members[0], 1)
    name = game.team_manager.get_team_name(team)
    if plural_key and count is not None and count > 1:
        game.broadcast_l(plural_key, player=name, count=count)
    elif count is not None:
        game.broadcast_l(message_key, player=name, count=count)
    else:
        game.broadcast_l(message_key, player=name)


def check_winner(game: "ScopaGame") -> Team | None:
    """
    Check for a winner.

    Args:
        game: The Scopa game instance.

    Returns:
        Winning team or None if no winner yet.
    """
    target = game.options.target_score

    if game.options.inverse_scopa:
        # Inverse: eliminate teams that reach target
        alive_teams = game.team_manager.get_alive_teams()
        for team in alive_teams:
            if team.total_score >= target:
                game.team_manager.eliminate_team(team)
                name = game.team_manager.get_team_name(team)
                game.broadcast_l("game-eliminated", player=name, score=team.total_score)

        # Check for last standing
        remaining = game.team_manager.get_alive_teams()
        if len(remaining) == 1:
            return remaining[0]
        elif len(remaining) == 0:
            # All eliminated - lowest score wins
            teams = game.team_manager.teams
            return min(teams, key=lambda t: t.total_score)
    else:
        # Normal: first to target wins
        teams_at_target = game.team_manager.get_teams_at_or_above_score(target)
        if teams_at_target:
            # Highest score wins
            return max(teams_at_target, key=lambda t: t.total_score)

    return None


def declare_winner(game: "ScopaGame", team: Team) -> None:
    """Declare a winner and end the game."""
    name = game.team_manager.get_team_name(team)
    game.broadcast_l("game-winner-score", player=name, score=team.total_score)

    game.play_sound("game_pig/win.ogg")

    # Mark game as finished (auto-destroys if no humans)
    # finish_game() now handles both persisting the result and showing the end screen
    game.finish_game()
