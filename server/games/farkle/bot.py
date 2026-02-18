"""Heuristic bot logic for Farkle."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ComboEval:
    """Parsed scoring action metadata for heuristic ranking."""

    action_id: str
    combo_type: str
    number: int
    base_points: int
    used_dice: int

    @property
    def points_per_die(self) -> float:
        return self.base_points / self.used_dice if self.used_dice > 0 else 0.0


def bot_think(game, player) -> str | None:
    """Choose a Farkle bot action using lightweight EV-inspired heuristics."""
    turn_set = game.get_action_set(player, "turn")
    if not turn_set:
        return None

    resolved = turn_set.resolve_actions(game, player)
    roll_enabled = game._is_roll_enabled(player) is None
    bank_enabled = game._is_bank_enabled(player) is None

    # Rank and choose among legal scoring actions first.
    scoring_actions = [
        ra.action.id
        for ra in resolved
        if ra.enabled and ra.action.id.startswith("score_")
    ]
    if scoring_actions:
        if _should_skip_lone_five(game, player, scoring_actions, roll_enabled):
            # With a completed keep already taken this roll, we may skip a low-value
            # lone 5 to preserve more dice for the next roll.
            return "roll"
        return _choose_best_scoring_action(game, player, scoring_actions)

    if roll_enabled:
        dice_remaining = _next_roll_dice_count(player)
        if _should_bank_now(game, player, dice_remaining, bank_enabled):
            return "bank"
        return "roll"

    if bank_enabled:
        return "bank"

    return None


def _choose_best_scoring_action(game, player, action_ids: list[str]) -> str:
    evals = [_parse_combo_action(action_id) for action_id in action_ids]
    evals = [ev for ev in evals if ev is not None]
    if not evals:
        return action_ids[0]

    current_multiplier = max(1, getattr(player, "hot_dice_multiplier", 1))
    hot_mode = bool(getattr(game.options, "hot_dice_multiplier", False))

    def rank(ev: ComboEval) -> tuple:
        used = ev.used_dice
        remaining_now = max(0, len(player.current_roll) - used)
        will_hot_dice = remaining_now == 0 and (len(player.banked_dice) + used == 6)
        structure_bonus = _combo_structure_bonus(ev.combo_type)
        multi_bias = 0
        if hot_mode and current_multiplier >= 2 and used >= 5:
            # In multiplier mode, large multi-dice keeps are usually better.
            multi_bias = 2
        # Prefer points/die, then keeps that leave more dice, then raw points.
        return (
            1 if will_hot_dice else 0,
            multi_bias,
            structure_bonus,
            ev.points_per_die,
            remaining_now,
            ev.base_points,
        )

    best = max(evals, key=rank)
    return best.action_id


def _should_bank_now(game, player, dice_remaining: int, bank_enabled: bool) -> bool:
    if not bank_enabled:
        return False

    turn_points = player.turn_score
    total_if_bank = player.score + turn_points
    target = game.options.target_score
    initial_bank = getattr(game.options, "initial_bank_score", 0)

    # Avoid a blocked bank attempt on first successful bank.
    if player.score == 0 and initial_bank > 0 and turn_points < initial_bank:
        return False

    if total_if_bank >= target:
        return True

    # If another player is already at/over target, keep rolling unless banking beats them.
    best_finished = max((p.score for p in game.players if p is not player), default=0)
    if best_finished >= target and total_if_bank <= best_finished:
        return False

    base_thresholds = {6: 150, 5: 120, 4: 90, 3: 70, 2: 50, 1: 30}
    threshold = float(base_thresholds.get(dice_remaining, 90))

    # Race adjustments.
    if total_if_bank >= (target - 60):
        threshold *= 0.85
    if player.score + 100 < best_finished:
        threshold *= 1.15
    if player.score > best_finished + 100:
        threshold *= 0.90

    # Multiplier mode: more aggressive banking with 1-2 dice, slightly greedier with 4-6 dice.
    if getattr(game.options, "hot_dice_multiplier", False):
        mult = max(1, getattr(player, "hot_dice_multiplier", 1))
        if mult >= 2:
            if dice_remaining <= 2:
                threshold *= 0.70
            elif dice_remaining >= 4:
                threshold *= 1.15

    return turn_points >= int(round(threshold))


def _should_skip_lone_five(game, player, action_ids: list[str], roll_enabled: bool) -> bool:
    """Return True when skipping a lone 5 is a better upside play than taking it."""
    if not roll_enabled or not getattr(player, "has_taken_combo", False):
        return False
    if len(action_ids) != 1 or action_ids[0] != "score_single_5_5":
        return False

    # Must be able to roll these dice immediately after skipping.
    dice_to_roll = len(player.current_roll)
    if dice_to_roll <= 0:
        return False

    turn_points = player.turn_score
    score = player.score
    target = game.options.target_score
    initial_bank = getattr(game.options, "initial_bank_score", 0)
    best_other = max((p.score for p in game.players if p is not player), default=0)
    hdm_on = bool(getattr(game.options, "hot_dice_multiplier", False))
    mult = max(1, getattr(player, "hot_dice_multiplier", 1))

    # If +5 reaches key breakpoints, take it.
    if score + turn_points + 5 >= target:
        return False
    if score == 0 and initial_bank > 0 and (turn_points + 5) >= initial_bank:
        return False

    near_goal = (score + turn_points) >= (target - 40)
    behind = score + 60 < best_other

    if dice_to_roll >= 4:
        if near_goal:
            return False
        # In HDM mode, preserve big dice pools to chase chained hot-dice value.
        if hdm_on and mult >= 2:
            return True
        return True

    if dice_to_roll == 3:
        if near_goal:
            return False
        # 3-dice case: skip only when upside is needed.
        if score == 0 and initial_bank > 0 and turn_points < initial_bank:
            return True
        if behind and turn_points < 70:
            return True
        if hdm_on and mult >= 2 and turn_points < 90:
            return True
        return False

    # With 1-2 dice, lock points more often.
    return False


def _next_roll_dice_count(player) -> int:
    dice_remaining = 6 - len(player.banked_dice)
    return 6 if dice_remaining == 0 else dice_remaining


def _combo_structure_bonus(combo_type: str) -> int:
    if combo_type in {
        "three_of_kind",
        "four_of_kind",
        "five_of_kind",
        "six_of_kind",
        "small_straight",
        "large_straight",
        "three_pairs",
        "double_triplets",
        "full_house",
    }:
        return 2
    if combo_type in {"single_1", "single_5"}:
        return 0
    return 1


def _parse_combo_action(action_id: str) -> ComboEval | None:
    if not action_id.startswith("score_"):
        return None
    body = action_id.removeprefix("score_")

    if body == "single_1_1":
        return ComboEval(action_id, "single_1", 1, 10, 1)
    if body == "single_5_5":
        return ComboEval(action_id, "single_5", 5, 5, 1)

    if body.startswith("three_of_kind_"):
        n = int(body.split("_")[-1])
        pts = 100 if n == 1 else n * 10
        return ComboEval(action_id, "three_of_kind", n, pts, 3)
    if body.startswith("four_of_kind_"):
        n = int(body.split("_")[-1])
        pts = 200 if n == 1 else n * 20
        return ComboEval(action_id, "four_of_kind", n, pts, 4)
    if body.startswith("five_of_kind_"):
        n = int(body.split("_")[-1])
        pts = 400 if n == 1 else n * 40
        return ComboEval(action_id, "five_of_kind", n, pts, 5)
    if body.startswith("six_of_kind_"):
        n = int(body.split("_")[-1])
        pts = 800 if n == 1 else n * 80
        return ComboEval(action_id, "six_of_kind", n, pts, 6)

    fixed = {
        "small_straight_0": ("small_straight", 100, 5),
        "large_straight_0": ("large_straight", 200, 6),
        "three_pairs_0": ("three_pairs", 150, 6),
        "double_triplets_0": ("double_triplets", 250, 6),
        "full_house_0": ("full_house", 150, 6),
    }
    if body in fixed:
        combo, pts, used = fixed[body]
        return ComboEval(action_id, combo, 0, pts, used)
    return None
