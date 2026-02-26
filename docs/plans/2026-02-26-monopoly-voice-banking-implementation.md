# Monopoly Voice Banking Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement a full-fidelity `voice_banking` preset with a deterministic `voice:` command layer on top of simulator-backed banking.

**Architecture:** Reuse existing `banking_sim.py` and economy helpers in `MonopolyGame`. Add a preset-specific profile resolver and deterministic command parser module, then bridge voice intents into existing banking operations under strict `voice:` prefix gating. Keep normal Monopoly actions available and unchanged.

**Tech Stack:** Python 3.13, dataclasses, pytest, existing Monopoly engine (`server/games/monopoly/game.py`), Fluent localization files.

---

### Task 1: Add Voice Banking Profile Resolver

**Files:**
- Create: `server/games/monopoly/voice_banking_profile.py`
- Test: `server/tests/test_monopoly_voice_banking_profile.py`

**Step 1: Write the failing test**

```python
from server.games.monopoly.voice_banking_profile import (
    resolve_voice_banking_profile,
    DEFAULT_VOICE_BANKING_PROFILE,
)


def test_resolve_voice_profile_uses_anchor_defaults():
    profile = resolve_voice_banking_profile("voice_banking")
    assert profile.preset_id == "voice_banking"
    assert profile.anchor_edition_id == "monopoly-e4816"
    assert profile.source_policy == "anchor-first"
    assert profile.confirmation_required_for_transfers is True


def test_resolve_voice_profile_falls_back_to_default():
    profile = resolve_voice_banking_profile("unknown")
    assert profile == DEFAULT_VOICE_BANKING_PROFILE
```

**Step 2: Run test to verify it fails**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_voice_banking_profile.py -v`
Expected: FAIL because module does not exist.

**Step 3: Write minimal implementation**

```python
@dataclass(frozen=True)
class VoiceBankingProfile:
    preset_id: str
    anchor_edition_id: str
    source_policy: str = "anchor-first"
    starting_balance: int = 1500
    pass_go_credit: int = 200
    command_prefix: str = "voice:"
    confirmation_required_for_transfers: bool = True
    provenance_notes: tuple[str, ...] = ()
```

Define `DEFAULT_VOICE_BANKING_PROFILE` anchored to `monopoly-e4816`, and `resolve_voice_banking_profile(...)`.

**Step 4: Run test to verify it passes**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_voice_banking_profile.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add server/games/monopoly/voice_banking_profile.py server/tests/test_monopoly_voice_banking_profile.py
git commit -m "Add voice banking profile resolver"
```

### Task 2: Add Deterministic Voice Command Parser

**Files:**
- Create: `server/games/monopoly/voice_commands.py`
- Test: `server/tests/test_monopoly_voice_commands.py`

**Step 1: Write the failing test**

```python
from server.games.monopoly.voice_commands import parse_voice_command


def test_requires_exact_voice_prefix():
    assert parse_voice_command("voice: balance").intent == "check_balance"
    assert parse_voice_command("Voice: balance").error == "missing_prefix"
    assert parse_voice_command("balance").error == "missing_prefix"


def test_parses_transfer_and_ledger_commands():
    transfer = parse_voice_command("voice: transfer 200 to Guest")
    assert transfer.intent == "transfer_amount_to_player"
    assert transfer.amount == 200
    assert transfer.target_name == "Guest"

    ledger = parse_voice_command("voice: ledger")
    assert ledger.intent == "show_recent_ledger"
```

**Step 2: Run test to verify it fails**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_voice_commands.py -v`
Expected: FAIL.

**Step 3: Write minimal implementation**

Implement dataclasses:

- `VoiceIntent`
- `VoiceParseResult`

Implement parser with strict case-sensitive `voice:` requirement and deterministic grammar for:

- `balance`
- `ledger`
- `repeat`
- `transfer <amount> to <target>`
- `confirm transfer`

**Step 4: Run test to verify it passes**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_voice_commands.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add server/games/monopoly/voice_commands.py server/tests/test_monopoly_voice_commands.py
git commit -m "Add deterministic voice command parser"
```

### Task 3: Initialize Voice Banking Preset Runtime in MonopolyGame

**Files:**
- Modify: `server/games/monopoly/game.py`
- Modify: `server/tests/test_monopoly.py`
- Create: `server/tests/test_monopoly_voice_banking.py`

**Step 1: Write the failing test**

```python
def test_voice_banking_on_start_initializes_profile_and_accounts():
    game = _start_two_player_game(MonopolyOptions(preset_id="voice_banking"))
    assert game.voice_banking_profile is not None
    assert game.voice_banking_profile.anchor_edition_id == "monopoly-e4816"
    assert game.banking_state is not None
    assert game._bank_balance(game.players[0]) > 0
```

**Step 2: Run test to verify it fails**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_voice_banking.py::test_voice_banking_on_start_initializes_profile_and_accounts -v`
Expected: FAIL.

**Step 3: Write minimal implementation**

Add fields:

- `voice_banking_profile: VoiceBankingProfile | None = None`
- `voice_last_response_by_player_id: dict[str, str]`
- `voice_pending_transfer_by_player_id: dict[str, tuple[str, int]]`

On `on_start`, initialize profile + `banking_state` for `voice_banking` similarly to electronic banking, and clear voice runtime dicts.

**Step 4: Run test to verify it passes**

Run: same as Step 2
Expected: PASS.

**Step 5: Commit**

```bash
git add server/games/monopoly/game.py server/tests/test_monopoly.py server/tests/test_monopoly_voice_banking.py
git commit -m "Initialize voice banking preset runtime state"
```

### Task 4: Add Voice Command Action and Prefix-Gated Parsing

**Files:**
- Modify: `server/games/monopoly/game.py`
- Modify: `server/locales/en/monopoly.ftl`
- Modify: `server/locales/pl/monopoly.ftl`
- Modify: `server/locales/pt/monopoly.ftl`
- Modify: `server/locales/ru/monopoly.ftl`
- Modify: `server/locales/vi/monopoly.ftl`
- Modify: `server/locales/zh/monopoly.ftl`
- Modify: `server/tests/test_monopoly_voice_banking.py`

**Step 1: Write the failing test**

```python
def test_voice_commands_require_exact_voice_prefix():
    game = _start_two_player_game(MonopolyOptions(preset_id="voice_banking"))
    host = game.current_player
    assert host is not None

    game.execute_action(host, "voice_command", input_value="Voice: balance")
    assert game.voice_last_response_by_player_id.get(host.id) == "missing_prefix"

    game.execute_action(host, "voice_command", input_value="voice: balance")
    assert game.voice_last_response_by_player_id.get(host.id) == "check_balance"
```

**Step 2: Run test to verify it fails**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_voice_banking.py::test_voice_commands_require_exact_voice_prefix -v`
Expected: FAIL.

**Step 3: Write minimal implementation**

Add turn action:

- `voice_command` with string input prompt

Implement handler:

- parse using `parse_voice_command(...)`
- enforce exact prefix behavior
- store deterministic response code in `voice_last_response_by_player_id`

Add localization keys for prompt and parse-error responses in all Monopoly locale files.

**Step 4: Run test to verify it passes**

Run: same as Step 2
Expected: PASS.

**Step 5: Commit**

```bash
git add server/games/monopoly/game.py server/locales/en/monopoly.ftl server/locales/pl/monopoly.ftl server/locales/pt/monopoly.ftl server/locales/ru/monopoly.ftl server/locales/vi/monopoly.ftl server/locales/zh/monopoly.ftl server/tests/test_monopoly_voice_banking.py
git commit -m "Add voice command action with strict voice prefix gating"
```

### Task 5: Implement Voice Intents (Balance, Ledger, Repeat)

**Files:**
- Modify: `server/games/monopoly/game.py`
- Modify: `server/tests/test_monopoly_voice_banking.py`

**Step 1: Write the failing test**

```python
def test_voice_balance_and_ledger_and_repeat_flow():
    game = _start_two_player_game(MonopolyOptions(preset_id="voice_banking"))
    host = game.current_player
    assert host is not None

    game.execute_action(host, "voice_command", input_value="voice: balance")
    assert game.voice_last_response_by_player_id[host.id] == "check_balance"

    game.execute_action(host, "voice_command", input_value="voice: ledger")
    assert game.voice_last_response_by_player_id[host.id] == "show_recent_ledger"

    game.execute_action(host, "voice_command", input_value="voice: repeat")
    assert game.voice_last_response_by_player_id[host.id] == "repeat_last_bank_result"
```

**Step 2: Run test to verify it fails**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_voice_banking.py::test_voice_balance_and_ledger_and_repeat_flow -v`
Expected: FAIL.

**Step 3: Write minimal implementation**

Add intent handlers:

- `_handle_voice_balance(...)`
- `_handle_voice_ledger(...)`
- `_handle_voice_repeat(...)`

Responses should be deterministic and localized.

**Step 4: Run test to verify it passes**

Run: same as Step 2
Expected: PASS.

**Step 5: Commit**

```bash
git add server/games/monopoly/game.py server/tests/test_monopoly_voice_banking.py
git commit -m "Implement voice balance ledger and repeat intents"
```

### Task 6: Implement Transfer + Confirm Voice Flow

**Files:**
- Modify: `server/games/monopoly/game.py`
- Modify: `server/tests/test_monopoly_voice_banking.py`

**Step 1: Write the failing test**

```python
def test_voice_transfer_requires_confirm_then_executes():
    game = _start_two_player_game(MonopolyOptions(preset_id="voice_banking"))
    host = game.current_player
    assert host is not None
    guest = game.players[1]

    game.execute_action(host, "voice_command", input_value=f"voice: transfer 200 to {guest.name}")
    assert host.id in game.voice_pending_transfer_by_player_id
    assert game._bank_balance(host) == 1500

    game.execute_action(host, "voice_command", input_value="voice: confirm transfer")
    assert host.id not in game.voice_pending_transfer_by_player_id
    assert game._bank_balance(host) == 1300
    assert game._bank_balance(guest) == 1700
```

**Step 2: Run test to verify it fails**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_voice_banking.py::test_voice_transfer_requires_confirm_then_executes -v`
Expected: FAIL.

**Step 3: Write minimal implementation**

Implement transfer flow:

- stage transfer on `transfer_amount_to_player`
- execute on `confirm transfer` if staged entry exists and still valid
- clear staged entry after success or hard failure
- emit localized success/failure responses

**Step 4: Run test to verify it passes**

Run: same as Step 2
Expected: PASS.

**Step 5: Commit**

```bash
git add server/games/monopoly/game.py server/tests/test_monopoly_voice_banking.py
git commit -m "Implement voice transfer confirmation flow"
```

### Task 7: Handle Voice Transfer Failures Without State Mutation

**Files:**
- Modify: `server/games/monopoly/game.py`
- Modify: `server/tests/test_monopoly_voice_banking.py`

**Step 1: Write the failing test**

```python
def test_voice_transfer_insufficient_funds_keeps_balances_unchanged():
    game = _start_two_player_game(MonopolyOptions(preset_id="voice_banking"))
    host = game.current_player
    assert host is not None
    guest = game.players[1]
    assert game.banking_state is not None
    game.banking_state.accounts[host.id].balance = 100
    game._sync_player_cash_from_banking(host)

    game.execute_action(host, "voice_command", input_value=f"voice: transfer 200 to {guest.name}")
    game.execute_action(host, "voice_command", input_value="voice: confirm transfer")

    assert game._bank_balance(host) == 100
    assert game._bank_balance(guest) == 1500
```

**Step 2: Run test to verify it fails**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_voice_banking.py::test_voice_transfer_insufficient_funds_keeps_balances_unchanged -v`
Expected: FAIL.

**Step 3: Write minimal implementation**

Add validation/error branch for insufficient funds on confirmation path and preserve balances.

**Step 4: Run test to verify it passes**

Run: same as Step 2
Expected: PASS.

**Step 5: Commit**

```bash
git add server/games/monopoly/game.py server/tests/test_monopoly_voice_banking.py
git commit -m "Handle voice transfer insufficient funds deterministically"
```

### Task 8: Ensure Normal Monopoly Actions Coexist in Voice Preset

**Files:**
- Modify: `server/tests/test_monopoly_voice_banking.py`

**Step 1: Write the failing test**

```python
def test_voice_preset_keeps_normal_board_actions_available(monkeypatch):
    game = _start_two_player_game(MonopolyOptions(preset_id="voice_banking"))
    host = game.current_player
    assert host is not None

    rolls = iter([1, 2])
    monkeypatch.setattr("server.games.monopoly.game.random.randint", lambda a, b: next(rolls))
    game.execute_action(host, "roll_dice")
    assert game.turn_pending_purchase_space_id == "baltic_avenue"
```

**Step 2: Run test to verify it fails (or asserts unexpected behavior)**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_voice_banking.py::test_voice_preset_keeps_normal_board_actions_available -v`
Expected: Initially FAIL if integration accidentally gates actions.

**Step 3: Write minimal implementation**

Adjust preset gating logic to ensure `voice_banking` does not hide/disable core board actions.

**Step 4: Run test to verify it passes**

Run: same as Step 2
Expected: PASS.

**Step 5: Commit**

```bash
git add server/tests/test_monopoly_voice_banking.py server/games/monopoly/game.py
git commit -m "Keep normal board actions enabled in voice banking preset"
```

### Task 9: Final Verification

**Files:**
- Modify: tests only if regressions discovered

**Step 1: Run focused voice-banking tests**

Run:

```bash
cd server && ../.venv/bin/pytest tests/test_monopoly_voice_banking_profile.py tests/test_monopoly_voice_commands.py tests/test_monopoly_voice_banking.py -v
```

Expected: PASS.

**Step 2: Run Monopoly regression suite**

Run:

```bash
cd server && ../.venv/bin/pytest -k monopoly -v
```

Expected: PASS.

**Step 3: Run integration smoke checks**

Run:

```bash
cd server && ../.venv/bin/pytest tests/test_integration.py::TestGameRegistryIntegration::test_pig_game_registered tests/test_integration.py::TestGameRegistryIntegration::test_get_by_category -v
```

Expected: PASS.

**Step 4: Fix regressions minimally if any fail**

Apply targeted changes only; avoid broad refactors.

**Step 5: Commit**

```bash
git add server/games/monopoly/*.py server/tests/test_monopoly*.py server/locales/*/monopoly.ftl
git commit -m "Finalize voice banking preset implementation"
```

## Done Definition

1. `voice_banking` preset initializes anchor-driven voice profile and simulator-backed economy.
2. Voice commands only execute with exact `voice:` prefix.
3. Transfer confirmation flow is deterministic and safe.
4. Normal Monopoly actions remain available in `voice_banking`.
5. Full Monopoly regression suite remains green.
