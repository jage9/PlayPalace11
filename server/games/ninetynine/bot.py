"""
Bot AI for Ninety Nine game.

Direct port of the v10 Lua bot (bot_ai.lua) to Python.
"""

from typing import TYPE_CHECKING

from ...game_utils.cards import (
    Card,
    RS_RANK_PLUS_10,
    RS_RANK_MINUS_10,
    RS_RANK_PASS,
    RS_RANK_REVERSE,
    RS_RANK_SKIP,
    RS_RANK_NINETY_NINE,
)

if TYPE_CHECKING:
    from .game import NinetyNineGame, NinetyNinePlayer

# Game constants
MAX_COUNT = 99
TWO_DIVIDE_THRESHOLD = 49


def bot_think(game: "NinetyNineGame", player: "NinetyNinePlayer") -> str | None:
    """
    Bot AI decision making.

    Args:
        game: The Ninety Nine game instance.
        player: The bot player making a decision.

    Returns:
        Action ID to execute, or None if no action available.
    """
    if game.current_player != player:
        return None

    return _bot_choose_card(game, player)


def _bot_choose_card(game: "NinetyNineGame", player: "NinetyNinePlayer") -> str | None:
    """Bot chooses which card to play."""
    if not player.hand:
        return None

    best_slot = 0
    best_score = -99999
    best_rank = 0

    # Evaluate each card
    for i, card in enumerate(player.hand):
        score = _bot_evaluate_card(game, player, card)

        # Choose card with best score, or highest rank if tied
        if score > best_score or (score == best_score and card.rank > best_rank):
            best_score = score
            best_slot = i
            best_rank = card.rank

    return f"card_slot_{best_slot + 1}"


def _bot_evaluate_card(
    game: "NinetyNineGame", player: "NinetyNinePlayer", card: Card
) -> int:
    """Evaluate a card's value for playing."""
    current_count = game.count
    rank = card.rank
    is_rs_games = not game.is_quentin_c

    # RS Games variant
    if is_rs_games:
        if rank == 1:
            # Ace: Always +1 in RS Games
            return _bot_evaluate_count(game, player, current_count + 1, rank)
        elif rank == 2:
            # 2: Always +2 in RS Games
            return _bot_evaluate_count(game, player, current_count + 2, rank)
        elif 3 <= rank <= 9:
            # Number cards 3-9
            return _bot_evaluate_count(game, player, current_count + rank, rank)
        elif rank == RS_RANK_PLUS_10:
            # 10 card (always +10)
            return _bot_evaluate_count(game, player, current_count + 10, rank)
        elif rank == RS_RANK_MINUS_10:
            # -10 card
            return _bot_evaluate_count(game, player, current_count - 10, rank)
        elif rank == RS_RANK_PASS:
            # Pass (no change to count)
            return _bot_evaluate_count(game, player, current_count, rank)
        elif rank == RS_RANK_REVERSE:
            # Reverse (no change to count)
            return _bot_evaluate_count(game, player, current_count, rank)
        elif rank == RS_RANK_SKIP:
            # Skip (no change to count)
            return _bot_evaluate_count(game, player, current_count, rank)
        elif rank == RS_RANK_NINETY_NINE:
            # Ninety Nine (sets count to 99)
            return _bot_evaluate_count(game, player, 99, rank)

    # Quentin C variant
    else:
        if rank == 1:
            # Ace: Try both +1 and +11
            score_plus_11 = _bot_evaluate_count(game, player, current_count + 11, rank)
            score_plus_1 = _bot_evaluate_count(game, player, current_count + 1, rank)
            return max(score_plus_11, score_plus_1)

        elif rank == 10 and current_count < 90:
            # 10: Try both +10 and -10
            score_plus = _bot_evaluate_count(game, player, current_count + 10, rank)
            score_minus = _bot_evaluate_count(game, player, current_count - 10, rank)
            return max(score_plus, score_minus)

        elif rank == 2:
            # 2: Calculate multiply/divide effect
            new_count = _calculate_two_effect(current_count)
            return _bot_evaluate_count(game, player, new_count, rank)

        elif rank == 9:
            # 9: No change to count
            return _bot_evaluate_count(game, player, current_count, rank)

        elif rank == 11 and len(game.alive_players) == 2:
            # Jack in 2-player: evaluate the chain (skip = play again)
            # Only worth doing lookahead if we have Jacks
            jack_count = sum(1 for c in player.hand if c.rank == 11)
            if jack_count >= 1:
                new_count = current_count + 10
                if new_count > 99:
                    return -99999
                # Check for milestone pass-through on this first Jack
                if current_count < 33 < new_count:
                    return -8000  # Passing through 33
                if current_count < 66 < new_count:
                    return -8000  # Passing through 66
                remaining_hand = [c for c in player.hand if c is not card]
                return _evaluate_jack_chain(game, current_count + 10, remaining_hand)
            else:
                # No Jacks, shouldn't happen but fallback
                return _bot_evaluate_count(game, player, current_count + 10, rank)

        else:
            # Regular cards: Add face value
            value = _get_card_value(rank)
            return _bot_evaluate_count(game, player, current_count + value, rank)

    return 0


def _bot_evaluate_count(
    game: "NinetyNineGame", player: "NinetyNinePlayer", new_count: int, rank: int
) -> int:
    """Evaluate a potential new count."""
    score = 0
    current_count = game.count
    is_rs_games = not game.is_quentin_c

    # Priority 1: NEVER go over 99 (instant loss!)
    if new_count > 99:
        return -99999

    # Milestone logic (Quentin C only)
    if not is_rs_games:
        # Priority 2: Hit milestones (33, 66, 99) - highest priority!
        # But only if we're ADDING to reach the milestone (positive value cards)
        # Dividing/subtracting to a milestone doesn't trigger the bonus
        if new_count in (33, 66, 99) and new_count > current_count:
            return 10000

        # Priority 1b: NEVER pass through a milestone (loses a token!)
        # Check if we cross 33 or 66 without landing on them
        if current_count < 33 < new_count:
            return -8000  # Passing through 33
        if current_count < 66 < new_count:
            return -8000  # Passing through 66

    # Check if this is a Skip card in a 2-player game (self-trap detection)
    alive_count = len(game.alive_players)
    is_two_player = alive_count == 2
    is_skip_card = (rank == 11 and not is_rs_games) or (rank == RS_RANK_SKIP and is_rs_games)

    if not is_rs_games:
        # Quentin C variant: milestone-based trap logic
        if is_two_player and is_skip_card:
            # In 2-player games, Skip skips opponent, so bot plays again immediately
            # Check if the count after Skip would be dangerous for bot's next turn

            # Danger zones where bot would struggle to play safely:
            # - Near milestones: 28-32, 61-65, 88-98 (hard to avoid passing/hitting)
            # - Trap setups: 23, 56, 89 (opponents can hit milestones)
            is_danger_zone = (
                (28 <= new_count <= 32)
                or (61 <= new_count <= 65)
                or (88 <= new_count <= 98)
                or new_count in (23, 56, 89)
            )

            if is_danger_zone:
                # Heavily penalize setting trap for ourselves!
                return -5000

        # Priority 2a: PERFECT TRAPS in 2-player (31, 97) - opponent is doomed!
        # 31: Requires 9, Ace+1, or 10-10 to avoid passing through 33
        # 97: Requires 9, Ace+1, or 10-10 to avoid going over 99
        if is_two_player and new_count in (31, 97):
            return 7000

        # Priority 2b: 64 is weaker in 2-player (opponent can use 2 to divide to 32)
        if is_two_player and new_count == 64:
            return 3000

        # Priority 2c: Setup zones - put opponents in bad positions
        if (29 <= new_count <= 32) or (62 <= new_count <= 65) or (95 <= new_count <= 98):
            return 5000

    else:
        # RS Games variant: simpler strategy (no milestones)
        if is_two_player and is_skip_card:
            # In 2-player, Skip makes us play again immediately
            # Avoid setting up dangerous counts for ourselves (close to 99)
            if 88 <= new_count <= 98:
                return -5000

        # In RS Games, prefer lower counts (safer)
        # But still strategic - set up 97 as a trap (hard to avoid going over 99)
        if is_two_player and new_count == 97:
            return 7000

    # Quentin C only: Avoid trap setups (23, 56, 89) if holding lots of +10 cards
    if not is_rs_games and new_count in (23, 56, 89):
        # Count how many +10 cards bot has
        plus_ten_count = sum(
            1 for c in player.hand if c.rank in (10, 11, 12, 13)
        )

        # If we have 2+ cards that can add +10, avoid setting up 23/56/89
        if plus_ten_count >= 2:
            return -3000

    # Card management: HOARD special cards - only use in danger!
    if is_rs_games:
        # RS Games: Danger zone is when count is high (close to 99)
        in_danger_zone = current_count >= 85

        if not in_danger_zone:
            # Hoard these cards! Heavy penalty for using them when not needed
            # Order: Pass/Skip (most) > -10 > Reverse > Ninety Nine (least)
            if rank == RS_RANK_PASS:
                # Pass: most valuable (keeps count same, very safe)
                score = score - 400
            elif rank == RS_RANK_SKIP:
                # Skip: also very valuable (skips opponent without changing count)
                score = score - 400
            elif rank == RS_RANK_MINUS_10:
                # -10: valuable for reducing high counts
                score = score - 300
            elif rank == RS_RANK_REVERSE:
                # Reverse: useful but less critical
                score = score - 200
            elif rank == RS_RANK_NINETY_NINE:
                # Ninety Nine: situational (sets to exactly 99)
                score = score - 250
        else:
            # In danger zone! Using special cards is smart
            if rank in (RS_RANK_PASS, RS_RANK_SKIP):
                # Pass/Skip are great in danger (keep count safe)
                score = score + 150
            elif rank == RS_RANK_MINUS_10:
                # -10 is excellent when count is high
                score = score + 200

    else:
        # Quentin C: Danger zones are near milestones
        in_danger_zone = (
            (28 <= current_count <= 32)
            or (61 <= current_count <= 65)
            or current_count >= 88
        )

        if not in_danger_zone:
            # Hoard these cards! Heavy penalty for using them when not needed
            # Order: Aces (most) > 9s > 10s > 2s (least)
            if rank == 1:
                # Aces are the most valuable (flexible +1/+11)
                score = score - 350
            elif rank == 9:
                # 9s are second-most valuable (can pass through danger)
                score = score - 300
            elif rank == 10:
                # 10s are third-most valuable (can +10 or -10)
                score = score - 200
            elif rank == 2:
                # 2s are fourth-most valuable (multiply/divide is powerful but situational)
                score = score - 150
        else:
            # In danger zone! Using special cards is smart, but prioritize usage
            if rank == 1:
                # Prefer using Aces first in danger (most flexible)
                score = score + 100
            elif rank == 9:
                # Use 9s second (good for staying put)
                score = score + 50
            elif rank == 10:
                # Use 10s last (save for worst emergencies)
                score = score + 0

    if is_rs_games:
        # RS Games: Prefer keeping count low (simpler strategy)
        # Penalize high counts heavily
        if 70 <= new_count <= 96:
            # Penalize based on how close to 99 we are
            danger_penalty = (new_count - 70) * -8
            score = score + danger_penalty

        # Bonus for safe low-to-mid range (20-60)
        if 20 <= new_count <= 60:
            score = score + 150

        # Small bonus for very low counts (safer)
        if 0 <= new_count <= 30:
            score = score + 50

    else:
        # Quentin C: Penalize high counts that aren't strategic (70-94 range)
        # Too close to 99, but not in setup zone (95-98)
        if 70 <= new_count <= 94:
            # Penalize based on how close to 99 we are
            danger_penalty = (new_count - 70) * -5
            score = score + danger_penalty

        # Fallback: Small bonus for safe middle range (40-60)
        if 40 <= new_count <= 60:
            score = score + 100

    return score


def _calculate_two_effect(current_count: int) -> int:
    """Calculate the new count after playing a 2 (Quentin C)."""
    if current_count % 2 == 0 and current_count > TWO_DIVIDE_THRESHOLD:
        return current_count // 2
    else:
        return current_count * 2


def _get_card_value(rank: int) -> int:
    """Get simple card value for Quentin C."""
    if 3 <= rank <= 8:
        return rank
    elif rank == 9:
        return 0
    elif rank in (11, 12, 13):  # J, Q, K
        return 10
    return 0


# =============================================================================
# Jack Chain Evaluation (2-player only)
# =============================================================================

def _evaluate_jack_chain(
    game: "NinetyNineGame", count_after_jack: int, remaining_hand: list["Card"]
) -> int:
    """
    Evaluate the best outcome achievable after playing a Jack in 2-player.

    In 2-player, Jacks skip the opponent, so the bot plays again immediately.
    This allows chaining multiple Jacks and planning the final position.

    Args:
        game: The game instance
        count_after_jack: Count after playing the Jack (+10)
        remaining_hand: Cards remaining in hand after playing the Jack

    Returns:
        Best score achievable through the chain
    """
    if count_after_jack > 99:
        return -99999  # Busted

    # Check if we hit a milestone with this Jack
    if count_after_jack == 99:
        return 15000  # Hit 99, round ends, huge bonus

    if count_after_jack in (33, 66):
        # We hit a milestone! And we get to play again (Jack skips opponent).
        # Find best continuation from remaining hand
        if remaining_hand:
            continuation_score = _find_best_chain_continuation(
                game, count_after_jack, remaining_hand
            )
            # Milestone bonus + continuation (continuation could be negative if bad)
            return 12000 + max(0, continuation_score // 10)
        else:
            return 12000  # Just the milestone

    # Check for milestone pass-through (bad!)
    # We need the original count to check this, but we only have count_after_jack
    # The caller should have already checked this, so we just evaluate the position

    if not remaining_hand:
        # No more cards, evaluate opponent's position
        return _score_opponent_position(count_after_jack)

    # Find best play from remaining hand
    return _find_best_chain_continuation(game, count_after_jack, remaining_hand)


def _find_best_chain_continuation(
    game: "NinetyNineGame", current_count: int, hand: list["Card"]
) -> int:
    """
    Find the best score achievable from current position with given hand.

    Args:
        game: The game instance
        current_count: Current count
        hand: Cards available to play

    Returns:
        Best score achievable
    """
    best_score = -99999

    for i, card in enumerate(hand):
        remaining = hand[:i] + hand[i + 1 :]

        if card.rank == 11:  # Another Jack
            new_count = current_count + 10
            if new_count <= 99:
                # Check for milestone pass-through
                if current_count < 33 < new_count:
                    score = -8000  # Would pass through 33
                elif current_count < 66 < new_count:
                    score = -8000  # Would pass through 66
                else:
                    score = _evaluate_jack_chain(game, new_count, remaining)
                best_score = max(best_score, score)
        else:
            # Non-Jack - evaluate all possible final positions
            for final_count in _get_card_final_counts(card, current_count):
                if final_count > 99:
                    continue
                # Check for milestone pass-through
                if current_count < 33 < final_count:
                    score = -8000
                elif current_count < 66 < final_count:
                    score = -8000
                elif final_count in (33, 66, 99):
                    score = 10000  # Milestone hit!
                else:
                    score = _score_opponent_position(final_count)
                best_score = max(best_score, score)

    return best_score


def _get_card_final_counts(card: "Card", current_count: int) -> list[int]:
    """
    Get possible final counts for playing a card.

    For cards with choices (Ace, 10), returns both options.
    """
    rank = card.rank
    if rank == 1:  # Ace: +1 or +11
        return [current_count + 1, current_count + 11]
    elif rank == 10:  # Ten: +10 or -10
        return [current_count + 10, current_count - 10]
    elif rank == 2:  # Two: multiply/divide
        return [_calculate_two_effect(current_count)]
    elif rank == 9:  # Nine: pass
        return [current_count]
    elif rank in (12, 13):  # Q, K: +10
        return [current_count + 10]
    elif 3 <= rank <= 8:  # Number cards
        return [current_count + rank]
    return [current_count]


def _score_opponent_position(count: int) -> int:
    """
    Score a position based on how bad it is for the opponent.

    Higher score = worse for opponent = better for us.
    """
    if count > 99:
        return -99999  # We busted (shouldn't happen)

    # Perfect traps - opponent is almost guaranteed to lose tokens
    # 31: Almost every card passes through 33 (only escape: 9, Ace+1, or 10-10)
    # 97: Almost every card goes over 99 (only escape: 9, Ace+1, or 10-10)
    if count in (31, 97):
        return 9000

    # Weaker trap (opponent can escape with 2 to divide)
    if count == 64:
        return 6000

    # Setup zones - opponent is in danger of passing through milestones
    if 29 <= count <= 30:  # Will likely pass through 33
        return 7000
    if count == 32:  # Very dangerous, only 9/Ace+1 avoids passing 33
        return 7500
    if 62 <= count <= 63:  # Will likely pass through 66
        return 7000
    if count == 65:  # Very dangerous
        return 7500
    if 95 <= count <= 96:  # Will likely go over 99
        return 7000
    if count == 98:  # Very dangerous
        return 7500

    # Bad positions for US to leave (opponent can hit milestones easily)
    if count in (23, 56, 89):
        return -3000  # Opponent can hit 33, 66, 99 with +10

    if count in (22, 55, 88):
        return -2000  # Opponent can hit milestones with +11

    # Neutral-ish positions
    if 40 <= count <= 60:
        return 100  # Safe middle range, slight bonus

    # High counts are generally worse for opponent
    if 70 <= count <= 94:
        return (count - 70) * 50  # More dangerous as count increases

    return 0


# Export for use in game.py (bot choice selection)
evaluate_count = _bot_evaluate_count
