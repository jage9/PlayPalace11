# Monopoly Manual-Core Dual-Lane Throughput Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Promote all remaining Monopoly special boards from `near_full` to `manual_core` under the approved hybrid dual-lane policy, while keeping extraction traceability, rule compatibility, and regression safety.

**Architecture:** Treat board status promotion as a gated conformance change. First enforce runtime parity status (`board_parity`) with a failing test, then align catalog source-of-truth (`special_board_anchor_index`) with a second failing test. Keep historical manual limitations explicit (for example unresolved literal cards on low-text boards) but valid under hybrid policy. Finish by syncing rollout docs and running full Monopoly regression.

**Tech Stack:** Python 3.11, pytest, JSON catalog artifacts, Monopoly manual-rule payloads (`server/games/monopoly/manual_rules/data/*.json`)

---

### Task 1: Enforce Manual-Core Fidelity in Runtime Parity Map

**Files:**
- Modify: `server/tests/test_monopoly_special_board_manual_core_conformance.py`
- Modify: `server/games/monopoly/board_parity.py`
- Test: `server/tests/test_monopoly_special_board_manual_core_conformance.py`

**Step 1: Write the failing test**

```python
@pytest.mark.parametrize("board_id", ALL_SPECIAL_BOARD_IDS)
def test_special_board_reaches_manual_core(board_id: str):
    profile = get_board_parity_profile(board_id)
    assert profile is not None
    assert profile.fidelity_status == "manual_core"
```

**Step 2: Run test to verify it fails**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_special_board_manual_core_conformance.py -q`  
Expected: FAIL for all boards still marked `near_full`.

**Step 3: Write minimal implementation**

Update `_FIDELITY_OVERRIDES` in `server/games/monopoly/board_parity.py` so every special board id maps to `"manual_core"` (preserve existing keys/order).

```python
_FIDELITY_OVERRIDES = {
    "mario_kart": "manual_core",
    # ...
    "transformers_beast_wars": "manual_core",
}
```

**Step 4: Run test to verify it passes**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_special_board_manual_core_conformance.py -q`  
Expected: PASS.

**Step 5: Commit**

```bash
git add server/tests/test_monopoly_special_board_manual_core_conformance.py server/games/monopoly/board_parity.py
git commit -m "Promote parity fidelity map to manual_core for special boards"
```

### Task 2: Align Anchor Index Fidelity Status with Manual-Core Promotion

**Files:**
- Modify: `server/tests/test_monopoly_special_board_anchor_index.py`
- Modify: `server/games/monopoly/catalog/special_board_anchor_index.json`
- Test: `server/tests/test_monopoly_special_board_anchor_index.py`

**Step 1: Write the failing test**

```python
def test_anchor_index_marks_all_special_boards_manual_core():
    data = json.loads(_index_path().read_text(encoding="utf-8"))
    assert all(row["fidelity_status"] == "manual_core" for row in data)
```

**Step 2: Run test to verify it fails**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_special_board_anchor_index.py -q`  
Expected: FAIL for rows still marked `near_full`.

**Step 3: Write minimal implementation**

Set `"fidelity_status": "manual_core"` for every row in `server/games/monopoly/catalog/special_board_anchor_index.json`.

```json
{
  "board_id": "animal_crossing",
  "fidelity_status": "manual_core"
}
```

**Step 4: Run test to verify it passes**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_special_board_anchor_index.py -q`  
Expected: PASS.

**Step 5: Commit**

```bash
git add server/tests/test_monopoly_special_board_anchor_index.py server/games/monopoly/catalog/special_board_anchor_index.json
git commit -m "Mark anchor index special boards as manual_core"
```

### Task 3: Add Cross-Artifact Fidelity Consistency Gate

**Files:**
- Create: `server/tests/test_monopoly_manual_core_fidelity_alignment.py`
- Test: `server/tests/test_monopoly_manual_core_fidelity_alignment.py`

**Step 1: Write the failing test**

```python
def test_board_parity_and_anchor_index_fidelity_match():
    # load anchor index rows keyed by board_id
    # load board parity profiles keyed by board_id
    # assert same board id set
    # assert both sides are manual_core for each board
```

Concrete check body:

```python
assert set(anchor_by_id) == set(get_parity_board_ids())
for board_id in anchor_by_id:
    assert anchor_by_id[board_id]["fidelity_status"] == "manual_core"
    assert get_board_parity_profile(board_id).fidelity_status == "manual_core"
```

**Step 2: Run test to verify it fails**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_manual_core_fidelity_alignment.py -q`  
Expected: FAIL before both artifacts are fully aligned.

**Step 3: Write minimal implementation**

If task 1 and task 2 are complete, no product code change is needed; keep this as a permanent guard test.

**Step 4: Run test to verify it passes**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_manual_core_fidelity_alignment.py -q`  
Expected: PASS.

**Step 5: Commit**

```bash
git add server/tests/test_monopoly_manual_core_fidelity_alignment.py
git commit -m "Add manual_core fidelity alignment guard test"
```

### Task 4: Validate Hybrid Lane Exception Contract on Known Low-Text Boards

**Files:**
- Create: `server/tests/test_monopoly_hybrid_lane_exception_contract.py`
- Test: `server/tests/test_monopoly_hybrid_lane_exception_contract.py`

**Step 1: Write the failing test**

```python
@pytest.mark.parametrize("board_id", ("marvel_avengers_legacy", "marvel_flip"))
def test_hybrid_lane_not_observed_cards_have_evidence_notes(board_id: str):
    rule_set = load_manual_rule_set(board_id)
    unresolved = [
        card
        for deck in ("chance", "community_chest")
        for card in rule_set.cards.get(deck, [])
        if card.get("text_status") == "not_observed_in_available_manual_sources"
    ]
    assert unresolved
    assert all(card.get("text_note") for card in unresolved)
```

**Step 2: Run test to verify it fails**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_hybrid_lane_exception_contract.py -q`  
Expected: FAIL if unresolved cards are missing evidence notes.

**Step 3: Write minimal implementation**

If needed, update the two board payload files:
- `server/games/monopoly/manual_rules/data/marvel_avengers_legacy.json`
- `server/games/monopoly/manual_rules/data/marvel_flip.json`

Ensure each `text_status == not_observed_in_available_manual_sources` card has explicit `text_note`.

**Step 4: Run test to verify it passes**

Run: `cd server && ../.venv/bin/pytest tests/test_monopoly_hybrid_lane_exception_contract.py -q`  
Expected: PASS.

**Step 5: Commit**

```bash
git add server/tests/test_monopoly_hybrid_lane_exception_contract.py server/games/monopoly/manual_rules/data/marvel_avengers_legacy.json server/games/monopoly/manual_rules/data/marvel_flip.json
git commit -m "Gate hybrid lane unresolved card exceptions with evidence notes"
```

### Task 5: Refresh Plan/Status Docs for Complete Manual-Core Promotion

**Files:**
- Modify: `docs/plans/2026-02-26-monopoly-special-boards-final-part-status.md`
- Modify: `docs/plans/2026-02-27-monopoly-manual-core-overnight-checklist.md`
- Modify: `docs/plans/2026-02-26-monopoly-special-boards-parity-matrix.md`

**Step 1: Write the failing documentation expectation**

Add/update verifiable claims:
- `manual_core: 55`
- `near_full: 0`
- Hybrid-lane exception note retained for unresolved literal cards on `marvel_avengers_legacy` and `marvel_flip`.

**Step 2: Run lightweight verification**

Run:
`rg -n "manual_core|near_full|marvel_avengers_legacy|marvel_flip" docs/plans/2026-02-26-monopoly-special-boards-final-part-status.md docs/plans/2026-02-27-monopoly-manual-core-overnight-checklist.md docs/plans/2026-02-26-monopoly-special-boards-parity-matrix.md`

Expected: Updated counts and completion state present.

**Step 3: Write minimal implementation**

Update the three docs to reflect completion and current hybrid exception boundaries.

**Step 4: Re-run verification**

Run the same `rg` command and manually inspect for consistency.

**Step 5: Commit**

```bash
git add docs/plans/2026-02-26-monopoly-special-boards-final-part-status.md docs/plans/2026-02-27-monopoly-manual-core-overnight-checklist.md docs/plans/2026-02-26-monopoly-special-boards-parity-matrix.md
git commit -m "Update monopoly plans for full manual_core promotion state"
```

### Task 6: Full Regression and Final Integration Commit

**Files:**
- Modify: (none expected; verification-only task)
- Test: `server/tests/test_monopoly_special_board_manual_core_conformance.py`
- Test: `server/tests/test_monopoly_special_board_anchor_index.py`
- Test: `server/tests/test_monopoly_manual_core_fidelity_alignment.py`
- Test: `server/tests/test_monopoly_hybrid_lane_exception_contract.py`
- Test: Monopoly suite subset (`-k monopoly`)

**Step 1: Run targeted promotion-gate tests**

Run:
`cd server && ../.venv/bin/pytest tests/test_monopoly_special_board_manual_core_conformance.py tests/test_monopoly_special_board_anchor_index.py tests/test_monopoly_manual_core_fidelity_alignment.py tests/test_monopoly_hybrid_lane_exception_contract.py -q`

Expected: PASS.

**Step 2: Run full Monopoly regression**

Run:
`cd server && ../.venv/bin/pytest -k monopoly -q`

Expected: PASS with no new failures.

**Step 3: Commit final integration checkpoint**

```bash
git add -A
git commit -m "Finalize manual_core rollout for remaining Monopoly special boards"
```

**Step 4: Optional push**

```bash
git push
```

