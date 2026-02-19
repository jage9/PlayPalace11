"""Bot strategy for Yahtzee."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

from ...game_utils.dice import count_dice

if TYPE_CHECKING:
    from .game import YahtzeeGame, YahtzeePlayer


def bot_think(
    game: "YahtzeeGame",
    player: "YahtzeePlayer",
    *,
    calculate_score: Callable[[list[int], str], int],
    all_categories: list[str],
    upper_categories: list[str],
) -> str | None:
    """Return the bot's next action."""
    if game.current_player != player:
        return None

    if not player.dice.has_rolled:
        return "roll"

    open_categories = player.get_open_categories()
    if not open_categories:
        return None

    if player.rolls_left > 0:
        target = _pick_target_category(player.dice.values, open_categories, player.rolls_left)
        desired_keeps = _desired_keep_indices(player.dice.values, target)
        current_keeps = {i for i in range(5) if player.dice.is_kept(i)}

        if desired_keeps != current_keeps:
            for i in range(5):
                if (i in desired_keeps) != (i in current_keeps):
                    return f"toggle_die_{i}"

        if player.rolls_left > 0 and len(desired_keeps) < 5:
            return "roll"

    return _pick_best_category_action(
        player, calculate_score=calculate_score, all_categories=all_categories, upper_categories=upper_categories
    )


def _pick_target_category(values: list[int], open_categories: list[str], rolls_left: int) -> str:
    """Choose category to pursue while rolling."""
    best_cat = open_categories[0]
    best_value = -1.0
    for cat in open_categories:
        value = _category_potential(values, cat, rolls_left)
        if value > best_value:
            best_value = value
            best_cat = cat
    return best_cat


def _category_potential(values: list[int], category: str, rolls_left: int) -> float:
    """Heuristic value for pursuing a category with remaining rolls."""
    counts = count_dice(values)
    best_value, best_count = max(counts.items(), key=lambda item: (item[1], item[0]))
    unique_values = sorted(set(values))
    run_len = _longest_consecutive_run(unique_values)

    if category in ("ones", "twos", "threes", "fours", "fives", "sixes"):
        target = _upper_target_value(category)
        matched = counts[target]
        return matched * target + (5 - matched) * target * 0.35 * rolls_left

    if category == "three_kind":
        need = max(0, 3 - best_count)
        return (best_count * best_value) + (need * best_value * 1.9 * rolls_left)

    if category == "four_kind":
        need = max(0, 4 - best_count)
        return (best_count * best_value) + (need * best_value * 2.0 * rolls_left)

    if category == "yahtzee":
        if best_count == 5:
            return 60.0
        return best_count * 10 + (5 - best_count) * 5 * rolls_left

    if category == "full_house":
        shape = sorted((c for c in counts.values() if c > 0), reverse=True)
        if len(shape) >= 2 and shape[0] >= 3 and shape[1] >= 2:
            return 45.0
        if len(shape) >= 2 and shape[0] >= 3:
            return 28.0 + rolls_left * 4.0
        if len(shape) >= 2 and shape[0] >= 2 and shape[1] >= 2:
            return 24.0 + rolls_left * 3.0
        return 10.0 + rolls_left * 2.0

    if category == "small_straight":
        if run_len >= 4:
            return 35.0
        return run_len * 7.0 + rolls_left * 4.0

    if category == "large_straight":
        if run_len >= 5:
            return 48.0
        return run_len * 6.0 + rolls_left * 3.0

    if category == "chance":
        return float(sum(v for v in values if v >= 4))

    return 0.0


def _desired_keep_indices(values: list[int], category: str) -> set[int]:
    """Select which dice to keep while pursuing a category."""
    counts = count_dice(values)

    if category in ("ones", "twos", "threes", "fours", "fives", "sixes"):
        target = _upper_target_value(category)
        keep = {i for i, value in enumerate(values) if value == target}
        return keep if keep else {max(range(5), key=lambda i: values[i])}

    if category in ("three_kind", "four_kind", "yahtzee"):
        best_value, _ = max(counts.items(), key=lambda item: (item[1], item[0]))
        keep = {i for i, value in enumerate(values) if value == best_value}
        return keep if keep else {max(range(5), key=lambda i: values[i])}

    if category == "full_house":
        top_values = sorted(
            (value for value, count in counts.items() if count > 0),
            key=lambda value: (counts[value], value),
            reverse=True,
        )[:2]
        keep = {i for i, value in enumerate(values) if value in top_values}
        return keep if keep else {max(range(5), key=lambda i: values[i])}

    if category in ("small_straight", "large_straight"):
        run = _best_straight_run(sorted(set(values)))
        keep: set[int] = set()
        used_values: set[int] = set()
        for i, value in enumerate(values):
            if value in run and value not in used_values:
                keep.add(i)
                used_values.add(value)
        return keep if keep else {max(range(5), key=lambda i: values[i])}

    if category == "chance":
        keep = {i for i, value in enumerate(values) if value >= 5}
        return keep if keep else {max(range(5), key=lambda i: values[i])}

    return {max(range(5), key=lambda i: values[i])}


def _pick_best_category_action(
    player: "YahtzeePlayer",
    *,
    calculate_score: Callable[[list[int], str], int],
    all_categories: list[str],
    upper_categories: list[str],
) -> str:
    """Choose the best category to score now."""
    open_categories = player.get_open_categories()
    scores = {cat: calculate_score(player.dice.values, cat) for cat in open_categories}

    best_cat = None
    best_utility = -1.0
    upper_total_before = player.get_upper_total()
    for cat in open_categories:
        score = scores[cat]
        utility = float(score)
        if cat in upper_categories:
            before_gap = max(0, 63 - upper_total_before)
            after_gap = max(0, 63 - (upper_total_before + score))
            if before_gap > 0:
                utility += (before_gap - after_gap) * 0.2
            if before_gap > 0 and after_gap == 0:
                utility += 35.0
        if utility > best_utility:
            best_utility = utility
            best_cat = cat

    if best_cat is not None and scores[best_cat] > 0:
        return f"score_{best_cat}"

    waste_order = [
        "yahtzee",
        "large_straight",
        "small_straight",
        "full_house",
        "four_kind",
        "three_kind",
        "chance",
        "ones",
        "twos",
        "threes",
        "fours",
        "fives",
        "sixes",
    ]
    for cat in waste_order:
        if cat in open_categories:
            return f"score_{cat}"

    return f"score_{all_categories[0]}"


def _upper_target_value(category: str) -> int:
    return {
        "ones": 1,
        "twos": 2,
        "threes": 3,
        "fours": 4,
        "fives": 5,
        "sixes": 6,
    }[category]


def _longest_consecutive_run(values: list[int]) -> int:
    """Return longest consecutive run length."""
    if not values:
        return 0
    best = 1
    current = 1
    for i in range(1, len(values)):
        if values[i] == values[i - 1] + 1:
            current += 1
            best = max(best, current)
        else:
            current = 1
    return best


def _best_straight_run(unique_values: list[int]) -> set[int]:
    """Return the longest consecutive run values."""
    if not unique_values:
        return set()
    best_start = unique_values[0]
    best_len = 1
    start = unique_values[0]
    length = 1
    for i in range(1, len(unique_values)):
        if unique_values[i] == unique_values[i - 1] + 1:
            length += 1
        else:
            if length > best_len:
                best_len = length
                best_start = start
            start = unique_values[i]
            length = 1
    if length > best_len:
        best_len = length
        best_start = start
    return set(range(best_start, best_start + best_len))
