"""
Bot AI for Scopa game.

Handles bot decision making for card play.
"""

from typing import TYPE_CHECKING

from ...game_utils.cards import Card
from .capture import find_captures, select_best_capture

if TYPE_CHECKING:
    from .game import ScopaGame, ScopaPlayer


def bot_think(game: "ScopaGame", player: "ScopaPlayer") -> str | None:
    """
    Bot AI decision making.

    Args:
        game: The Scopa game instance.
        player: The bot player making a decision.

    Returns:
        Action ID to execute, or None if no action available.
    """
    if not player.hand:
        return None

    # Evaluate each card and pick the best
    best_card = None
    best_score = float("-inf")

    for card in player.hand:
        score = evaluate_card(game, card, player)
        if score > best_score:
            best_score = score
            best_card = card

    if best_card:
        return f"play_card_{best_card.id}"
    return None


def find_best_combo_chain(
    table: list[Card],
    remaining_hand: list[Card],
    escoba: bool,
    cards_played: list[Card],
    depth: int = 0,
    max_depth: int = 4,
) -> tuple[list[Card], list[Card], float]:
    """
    Recursively find the best combo chain starting from current state.

    Returns the sequence of cards to play and what gets captured at the end.

    Args:
        table: Current table cards (simulated).
        remaining_hand: Cards still in hand.
        escoba: Whether escoba rules apply.
        cards_played: Cards played so far in this combo chain.
        depth: Current recursion depth.
        max_depth: Maximum depth to search.

    Returns:
        Tuple of (cards_to_play, cards_captured, score).
    """
    if depth >= max_depth or not remaining_hand:
        return ([], [], 0.0)

    best_sequence: list[Card] = []
    best_captured: list[Card] = []
    best_score = 0.0

    for card in remaining_hand:
        captures = find_captures(table, card.rank, escoba)
        if captures:
            sequence, captured, score = _evaluate_combo_completion(
                captures, cards_played, card
            )
        else:
            sequence, captured, score = _explore_combo_chain(
                table,
                remaining_hand,
                escoba,
                cards_played,
                card,
                depth,
                max_depth,
            )

        if score > best_score:
            best_score = score
            best_sequence = sequence
            best_captured = captured

    return (best_sequence, best_captured, best_score)


def _evaluate_combo_completion(
    captures: list[list[Card]], cards_played: list[Card], card: Card
) -> tuple[list[Card], list[Card], float]:
    best_capture = select_best_capture(captures)
    played_set = {c.id for c in cards_played}
    captured_from_combo = [c for c in best_capture if c.id in played_set]
    if not captured_from_combo:
        return ([], [], 0.0)

    score = _score_combo_completion(best_capture, captured_from_combo, cards_played)
    return (cards_played + [card], best_capture, score)


def _score_combo_completion(
    best_capture: list[Card],
    captured_from_combo: list[Card],
    cards_played: list[Card],
) -> float:
    score = 15 + len(best_capture) * 5
    score += len(captured_from_combo) * 8
    score += len(cards_played) * 3
    score += _score_combo_captured_cards(best_capture)
    return score


def _score_combo_captured_cards(captured_cards: list[Card]) -> float:
    score = 0.0
    for card in captured_cards:
        if card.suit == 1:  # Diamond
            score += 2
        if card.rank == 7:
            score += 3
        if card.rank == 7 and card.suit == 1:
            score += 5
    return score


def _explore_combo_chain(
    table: list[Card],
    remaining_hand: list[Card],
    escoba: bool,
    cards_played: list[Card],
    card: Card,
    depth: int,
    max_depth: int,
) -> tuple[list[Card], list[Card], float]:
    new_table = table + [card]
    new_hand = [c for c in remaining_hand if c.id != card.id]
    new_played = cards_played + [card]
    return find_best_combo_chain(
        new_table, new_hand, escoba, new_played, depth + 1, max_depth
    )


def check_combo_potential(
    game: "ScopaGame", card: Card, player: "ScopaPlayer"
) -> float:
    """
    Check if playing this card sets up a capture combo chain.

    Handles multi-card combos like:
    - Table: 2, Hand: 3, 5, 10
    - Play 3 → table: 2, 3
    - Play 5 → table: 2, 3, 5 (sum = 10)
    - Play 10 → captures 2, 3, 5!

    Args:
        game: The Scopa game instance.
        card: The card being considered for play.
        player: The bot player.

    Returns:
        Bonus score if combo potential exists.
    """
    escoba = game.options.escoba
    other_cards = [c for c in player.hand if c.id != card.id]

    if not other_cards:
        return 0.0

    # Simulate the table after playing this card
    simulated_table = game.table_cards + [card]

    # Find the best combo chain starting from this state
    sequence, captured, score = find_best_combo_chain(
        simulated_table,
        other_cards,
        escoba,
        cards_played=[card],
        depth=0,
        max_depth=min(len(other_cards), 4),  # Don't search too deep
    )

    # Discount score based on chain length (longer chains are riskier)
    # Opponent might capture before we complete the chain
    if sequence:
        chain_length = len(sequence)
        # Each extra step has ~50% chance of being interrupted in 2-player
        # More players = more risk
        num_players = len(game.get_active_players())
        risk_factor = 0.7 ** ((chain_length - 1) * (num_players - 1))
        score *= risk_factor

    return score


def evaluate_escoba_empty_table(card: Card, inverse: bool) -> float:
    """
    Evaluate card for playing on empty table in escoba mode.

    Cards with value <= 4 cannot be captured alone (15 - 4 = 11 > max rank 10),
    preventing opponent from both capturing AND sweeping.

    Args:
        card: The card being considered.
        inverse: If True, inverse scopa rules apply.

    Returns:
        Score bonus/penalty for this card on empty table.
    """
    if card.rank <= 4:
        # Safe card - can't be captured or swept
        # Prefer lower values (1 is safest, 4 is least safe)
        safety_bonus = 30 + (5 - card.rank) * 2
        return safety_bonus if not inverse else -safety_bonus
    else:
        # Risky card - can be captured
        # Penalize higher values more (10 is worst)
        risk_penalty = -20 - (card.rank - 4) * 3
        return risk_penalty if not inverse else -risk_penalty


def evaluate_card(game: "ScopaGame", card: Card, player: "ScopaPlayer") -> float:
    """
    Evaluate a card for bot play.

    Args:
        game: The Scopa game instance.
        card: The card to evaluate.
        player: The bot player.

    Returns:
        Score for this card (higher is better).
    """
    inverse = game.options.inverse_scopa
    escoba = game.options.escoba

    captures = find_captures(game.table_cards, card.rank, escoba)

    if not captures:
        return _score_non_capture(game, card, player, inverse, escoba)

    return _score_capture(game, card, captures, inverse)


def _score_non_capture(
    game: "ScopaGame", card: Card, player: "ScopaPlayer", inverse: bool, escoba: bool
) -> float:
    score = 10 - (card.rank * 0.5) if inverse else -5 + (card.rank * 0.5)
    score += check_combo_potential(game, card, player)
    if escoba and len(game.table_cards) == 0:
        score += evaluate_escoba_empty_table(card, inverse)
    return score


def _score_capture(
    game: "ScopaGame", card: Card, captures: list[list[Card]], inverse: bool
) -> float:
    best_capture = select_best_capture(captures)
    score = _score_capture_size(best_capture, inverse)
    score += _score_scopa(best_capture, game.table_cards, inverse)
    score += _score_capture_cards(best_capture, inverse)
    return score


def _score_capture_size(best_capture: list[Card], inverse: bool) -> float:
    num_captured = len(best_capture)
    return -num_captured * 10 if inverse else num_captured * 10


def _score_scopa(
    best_capture: list[Card], table_cards: list[Card], inverse: bool
) -> float:
    num_captured = len(best_capture)
    is_scopa = num_captured == len(table_cards) and len(table_cards) > 0
    if not is_scopa:
        return 0.0
    return -100 if inverse else 100


def _score_capture_cards(best_capture: list[Card], inverse: bool) -> float:
    score = 0.0
    for card in best_capture:
        if card.suit == 1:  # Diamond
            score += -5 if inverse else 5
        if card.rank == 7 and card.suit == 1:
            score += -20 if inverse else 20
        if card.rank == 7:
            score += -3 if inverse else 3
        if card.rank in (1, 6):
            score += -2 if inverse else 2
    return score
