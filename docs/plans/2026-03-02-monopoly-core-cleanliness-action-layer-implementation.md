# Monopoly Core Cleanliness Action-Layer Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Split Monopoly action-layer internals into focused modules while preserving gameplay behavior, save/load shape, action ids, handler names, and existing tests.

**Architecture:** Keep `MonopolyGame` as the public facade in `server/games/monopoly/game.py` and delegate internals to `server/games/monopoly/actions/*.py`. Modules remain stateless and operate on `MonopolyGame` instance state, so no state ownership moves. Apply extraction in verified slices with targeted tests and frequent commits.

**Tech Stack:** Python 3.13+, dataclasses, PlayPalace game action framework, pytest/pytest-asyncio, uv

---

### Task 1: Create action module scaffold and wiring

**Files:**
- Create: `server/games/monopoly/actions/__init__.py`
- Create: `server/games/monopoly/actions/handlers.py`
- Create: `server/games/monopoly/actions/guards.py`
- Create: `server/games/monopoly/actions/options.py`
- Create: `server/games/monopoly/actions/labels.py`
- Modify: `server/games/monopoly/game.py`
- Test: `server/tests/test_monopoly.py`

**Step 1: Write the failing test**

```python
def test_monopoly_imports_clean_after_action_module_split() -> None:
    from server.games.monopoly.game import MonopolyGame
    game = MonopolyGame()
    assert game.get_type() == "monopoly"
```

Add this small import/regression test to `server/tests/test_monopoly.py` if equivalent coverage does not already exist.

**Step 2: Run test to verify it fails**

Run: `cd server && uv run pytest -v server/tests/test_monopoly.py::test_monopoly_imports_clean_after_action_module_split`
Expected: FAIL due to missing new action module imports/wiring.

**Step 3: Write minimal implementation**

Create module skeletons and import them in `game.py`.

```python
# server/games/monopoly/actions/handlers.py
from __future__ import annotations

def action_roll_dice(game, player, action_id: str) -> None:
    raise NotImplementedError
```

```python
# server/games/monopoly/actions/__init__.py
from . import guards, handlers, labels, options

__all__ = ["guards", "handlers", "labels", "options"]
```

In `game.py`, add:

```python
from .actions import guards as action_guards
from .actions import handlers as action_handlers
from .actions import options as action_options
```

**Step 4: Run test to verify it passes**

Run: `cd server && uv run pytest -v server/tests/test_monopoly.py::test_monopoly_imports_clean_after_action_module_split`
Expected: PASS.

**Step 5: Commit**

```bash
git add server/games/monopoly/actions/__init__.py \
  server/games/monopoly/actions/handlers.py \
  server/games/monopoly/actions/guards.py \
  server/games/monopoly/actions/options.py \
  server/games/monopoly/actions/labels.py \
  server/games/monopoly/game.py \
  server/tests/test_monopoly.py
git commit -m "Scaffold Monopoly action modules for facade delegation"
```

### Task 2: Extract banking and voice action family

**Files:**
- Modify: `server/games/monopoly/game.py`
- Modify: `server/games/monopoly/actions/handlers.py`
- Modify: `server/games/monopoly/actions/guards.py`
- Modify: `server/games/monopoly/actions/options.py`
- Test: `server/tests/test_monopoly_electronic_banking.py`
- Test: `server/tests/test_monopoly_voice_banking.py`
- Test: `server/tests/test_monopoly_voice_commands.py`

**Step 1: Write the failing test**

Add focused regression assertions to one Monopoly test file to lock delegate compatibility:

```python
def test_banking_and_voice_actions_still_available_in_facade() -> None:
    game = _start_two_player_game(MonopolyOptions(preset_id="voice_banking"))
    host = game.get_active_players()[0]
    assert game._is_banking_balance_hidden(host) != Visibility.HIDDEN
    assert game._is_voice_command_hidden(host) != Visibility.HIDDEN
```

**Step 2: Run test to verify it fails**

Run: `cd server && uv run pytest -v server/tests/test_monopoly_voice_banking.py::test_banking_and_voice_actions_still_available_in_facade`
Expected: FAIL before delegate wiring is complete.

**Step 3: Write minimal implementation**

Move logic bodies of:
- `_is_banking_balance_enabled`, `_is_banking_balance_hidden`
- `_options_for_banking_transfer`
- `_is_banking_transfer_enabled`, `_is_banking_transfer_hidden`
- `_is_banking_ledger_enabled`, `_is_banking_ledger_hidden`
- `_is_voice_command_enabled`, `_is_voice_command_hidden`
- `_action_banking_balance`, `_action_banking_transfer`, `_action_banking_ledger`, `_action_voice_command`

Use facade wrappers in `game.py`:

```python
def _action_banking_balance(self, player: Player, action_id: str) -> None:
    return action_handlers.action_banking_balance(self, player, action_id)
```

**Step 4: Run test to verify it passes**

Run:
- `cd server && uv run pytest -v server/tests/test_monopoly_electronic_banking.py`
- `cd server && uv run pytest -v server/tests/test_monopoly_voice_banking.py`
- `cd server && uv run pytest -v server/tests/test_monopoly_voice_commands.py`
Expected: PASS.

**Step 5: Commit**

```bash
git add server/games/monopoly/game.py \
  server/games/monopoly/actions/handlers.py \
  server/games/monopoly/actions/guards.py \
  server/games/monopoly/actions/options.py \
  server/tests/test_monopoly_voice_banking.py
git commit -m "Extract Monopoly banking and voice action delegates"
```

### Task 3: Extract auction action family

**Files:**
- Modify: `server/games/monopoly/game.py`
- Modify: `server/games/monopoly/actions/handlers.py`
- Modify: `server/games/monopoly/actions/guards.py`
- Modify: `server/games/monopoly/actions/options.py`
- Test: `server/tests/test_monopoly.py`

**Step 1: Write the failing test**

Add or tighten auction-path assertions:

```python
def test_auction_actions_still_route_correctly_after_delegation() -> None:
    game = _start_two_player_game(MonopolyOptions())
    host = game.get_active_players()[0]
    assert game._is_auction_property_enabled(host) in (None, "monopoly-no-property-to-auction")
```

**Step 2: Run test to verify it fails**

Run: `cd server && uv run pytest -v server/tests/test_monopoly.py::test_auction_actions_still_route_correctly_after_delegation`
Expected: FAIL before extraction is complete.

**Step 3: Write minimal implementation**

Extract:
- `_options_for_auction_bid`, `_bot_select_auction_bid`
- `_is_auction_property_enabled`, `_is_auction_property_hidden`
- `_is_auction_bid_enabled`, `_is_auction_bid_hidden`
- `_is_auction_pass_enabled`, `_is_auction_pass_hidden`
- `_action_auction_property`, `_action_auction_bid`, `_action_auction_pass`

Keep wrapper signatures unchanged in `game.py`.

**Step 4: Run test to verify it passes**

Run: `cd server && uv run pytest -v server/tests/test_monopoly.py -k "auction or monopoly"`
Expected: PASS.

**Step 5: Commit**

```bash
git add server/games/monopoly/game.py \
  server/games/monopoly/actions/handlers.py \
  server/games/monopoly/actions/guards.py \
  server/games/monopoly/actions/options.py \
  server/tests/test_monopoly.py
git commit -m "Extract Monopoly auction action delegates"
```

### Task 4: Extract property-management action family

**Files:**
- Modify: `server/games/monopoly/game.py`
- Modify: `server/games/monopoly/actions/handlers.py`
- Modify: `server/games/monopoly/actions/guards.py`
- Modify: `server/games/monopoly/actions/options.py`
- Test: `server/tests/test_monopoly.py`
- Test: `server/tests/test_monopoly_junior.py`

**Step 1: Write the failing test**

Add regression checks for visibility and options:

```python
def test_property_management_actions_preserve_visibility_contracts() -> None:
    game = _start_two_player_game(MonopolyOptions(preset_id="junior"))
    host = game.get_active_players()[0]
    assert game._is_build_house_hidden(host) == Visibility.HIDDEN
    assert game._is_mortgage_property_hidden(host) == Visibility.HIDDEN
```

**Step 2: Run test to verify it fails**

Run: `cd server && uv run pytest -v server/tests/test_monopoly_junior.py::test_property_management_actions_preserve_visibility_contracts`
Expected: FAIL before complete extraction.

**Step 3: Write minimal implementation**

Extract:
- `_options_for_mortgage_property`, `_options_for_unmortgage_property`
- `_options_for_build_house`, `_options_for_sell_house`
- `_bot_select_mortgage_property`, `_bot_select_unmortgage_property`, `_bot_select_build_house`
- `_is_mortgage_property_*`, `_is_unmortgage_property_*`
- `_is_build_house_*`, `_is_sell_house_*`
- `_action_mortgage_property`, `_action_unmortgage_property`, `_action_build_house`, `_action_sell_house`

**Step 4: Run test to verify it passes**

Run:
- `cd server && uv run pytest -v server/tests/test_monopoly_junior.py`
- `cd server && uv run pytest -v server/tests/test_monopoly.py -k "mortgage or house"`
Expected: PASS.

**Step 5: Commit**

```bash
git add server/games/monopoly/game.py \
  server/games/monopoly/actions/handlers.py \
  server/games/monopoly/actions/guards.py \
  server/games/monopoly/actions/options.py \
  server/tests/test_monopoly_junior.py
git commit -m "Extract Monopoly property management action delegates"
```

### Task 5: Extract trade, jail, and turn-end action family

**Files:**
- Modify: `server/games/monopoly/game.py`
- Modify: `server/games/monopoly/actions/handlers.py`
- Modify: `server/games/monopoly/actions/guards.py`
- Modify: `server/games/monopoly/actions/options.py`
- Test: `server/tests/test_monopoly_cheaters.py`
- Test: `server/tests/test_monopoly_city.py`

**Step 1: Write the failing test**

Add regression for turn-end and jail action contracts:

```python
def test_turn_end_and_jail_actions_preserve_guard_contracts() -> None:
    game = _start_two_player_game(MonopolyOptions())
    host = game.get_active_players()[0]
    assert game._is_end_turn_enabled(host) == "monopoly-roll-first"
```

**Step 2: Run test to verify it fails**

Run: `cd server && uv run pytest -v server/tests/test_monopoly.py::test_turn_end_and_jail_actions_preserve_guard_contracts`
Expected: FAIL before extraction/wiring is complete.

**Step 3: Write minimal implementation**

Extract:
- `_options_for_offer_trade`
- `_is_offer_trade_*`, `_is_accept_trade_*`, `_is_decline_trade_*`
- `_is_pay_bail_*`, `_is_use_jail_card_*`
- `_is_end_turn_*`, `_is_claim_cheat_reward_*`
- `_action_offer_trade`, `_action_accept_trade`, `_action_decline_trade`
- `_action_pay_bail`, `_action_use_jail_card`, `_action_claim_cheat_reward`, `_action_end_turn`

**Step 4: Run test to verify it passes**

Run:
- `cd server && uv run pytest -v server/tests/test_monopoly_cheaters.py`
- `cd server && uv run pytest -v server/tests/test_monopoly_city.py`
- `cd server && uv run pytest -v server/tests/test_monopoly.py -k "trade or jail or end_turn"`
Expected: PASS.

**Step 5: Commit**

```bash
git add server/games/monopoly/game.py \
  server/games/monopoly/actions/handlers.py \
  server/games/monopoly/actions/guards.py \
  server/games/monopoly/actions/options.py \
  server/tests/test_monopoly.py
git commit -m "Extract Monopoly trade jail and turn-end delegates"
```

### Task 6: Extract roll/buy action family (highest complexity)

**Files:**
- Modify: `server/games/monopoly/game.py`
- Modify: `server/games/monopoly/actions/handlers.py`
- Modify: `server/games/monopoly/actions/guards.py`
- Test: `server/tests/test_monopoly.py`
- Test: `server/tests/test_monopoly_junior.py`
- Test: `server/tests/test_monopoly_junior_super_mario_manual.py`
- Test: `server/tests/test_monopoly_city.py`

**Step 1: Write the failing test**

Add a delegation regression marker test focused on roll path:

```python
def test_roll_and_buy_actions_preserve_contract_after_delegation(monkeypatch) -> None:
    game = _start_two_player_game(MonopolyOptions())
    host = game.get_active_players()[0]
    assert game._is_roll_dice_hidden(host) != Visibility.HIDDEN
```

**Step 2: Run test to verify it fails**

Run: `cd server && uv run pytest -v server/tests/test_monopoly.py::test_roll_and_buy_actions_preserve_contract_after_delegation`
Expected: FAIL before extraction/wiring is complete.

**Step 3: Write minimal implementation**

Extract:
- `_is_roll_dice_*`, `_is_buy_property_*`
- `_action_roll_dice`, `_action_buy_property`

Keep all branch behavior identical, including:
- junior/junior-super-mario behavior
- doubles/extra-roll behavior
- jail and bail logic
- pending purchase behavior
- menu rebuild/sync timing

**Step 4: Run test to verify it passes**

Run:
- `cd server && uv run pytest -v server/tests/test_monopoly.py`
- `cd server && uv run pytest -v server/tests/test_monopoly_junior.py`
- `cd server && uv run pytest -v server/tests/test_monopoly_junior_super_mario_manual.py`
- `cd server && uv run pytest -v server/tests/test_monopoly_city.py`
Expected: PASS.

**Step 5: Commit**

```bash
git add server/games/monopoly/game.py \
  server/games/monopoly/actions/handlers.py \
  server/games/monopoly/actions/guards.py \
  server/tests/test_monopoly.py
git commit -m "Extract Monopoly roll and buy action delegates"
```

### Task 7: Final regression sweep and cleanup

**Files:**
- Modify: `server/games/monopoly/game.py`
- Modify: `server/games/monopoly/actions/*.py`
- Test: `server/tests/test_monopoly*.py`
- Test: `server/tests/test_farkle.py`
- Test: `server/tests/test_tradeoff.py`

**Step 1: Write the failing test**

No new test in this task; use full existing regression suite for confidence.

**Step 2: Run test to verify it fails**

N/A (skip; previous tasks already provide failing-test checkpoints).

**Step 3: Write minimal implementation**

Perform final cleanup only:
- remove duplicated dead code left in `game.py`
- ensure all extracted wrappers delegate one-to-one
- keep imports ordered and module boundaries clear

**Step 4: Run test to verify it passes**

Run:
- `cd server && uv run pytest -v server/tests/test_monopoly*.py`
- `cd server && uv run pytest -v server/tests/test_farkle.py server/tests/test_tradeoff.py`
Expected: PASS.

**Step 5: Commit**

```bash
git add server/games/monopoly/game.py server/games/monopoly/actions/*.py
git commit -m "Finish Monopoly action-layer cleanup regression pass"
```
