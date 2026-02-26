# Monopoly City Design (2026-02-26)

## Goal

Implement a full-fidelity `city` preset with complete winner-loop behavior using strict `anchor-first` rules from `monopoly-1790`.

## Confirmed Decisions

1. Next preset target: `city`.
2. Fidelity target: full.
3. Source policy: strict `anchor-first`.
4. Winner loop: complete in first implementation pass.
5. Priority: rules correctness first, UX polish second.
6. Chosen architecture: keep `MonopolyGame` and add City-specific modules.
7. First implementation phase starts with manual extraction and anchor notes.

## Anchor Context

- Preset id: `city`
- Anchor edition id: `monopoly-1790`
- Policy: `anchor-first`
- Manual source set: curated Monopoly catalog variants for `monopoly-1790` (`en-us` and equivalent locale mirrors)

## Architecture

### High-Level Split

- Add `city_profile.py` for anchor-driven City config.
- Add `city_engine.py` for deterministic City mechanics and win checks.
- Add City board/rules constants module (for City-only spaces/mechanics).
- Keep `MonopolyGame` as the orchestrator and route City-only flows by preset guard.

### Preset Routing

- `city`:
  - initializes City profile + engine + City state
  - routes turn/payment/endgame boundaries through City engine hooks
- all other presets:
  - no City engine initialized
  - no behavior changes

## Components And Data Flow

### Startup

- `on_start` resolves City profile (`monopoly-1790`) and initializes City engine + City runtime state.
- Existing Monopoly player lifecycle, turn ordering, bot scheduling, and score syncing are reused.

### Turn Flow

- canonical sequence:
  - `roll -> move -> resolve City space/effects -> settle payments/rewards -> evaluate winner -> end turn`
- City engine is called only at deterministic mutation boundaries.

### Payment And Economy

- Reuse shared helpers already used by Monopoly (`_credit_player`, `_debit_player_to_bank`, `_transfer_between_players`, liquidation, bankruptcy).
- City-specific modifiers remain centralized in City engine outcomes/profile data.

### Winner Loop

- Winner checks run after each City-relevant state mutation.
- If win condition is met, game transitions immediately to finished state and announces winner.
- No deferred winner pass in a second milestone.

## Error Handling And Determinism

- Fail-safe default for unknown/incomplete City context: no mutation (`allow`) rather than inferred behavior.
- City outcomes are applied atomically with existing economy helpers.
- Engine behavior must be deterministic: same state + same event sequence => same result.
- City rules never leak to non-City presets.

## Testing Strategy

### Unit Tests

- `city_profile` anchor resolution (`monopoly-1790`, `anchor-first`).
- `city_engine` outcome matrix and deterministic winner checks.
- Rule-specific edge cases from anchor manual.

### Integration Tests

- City startup initializes profile/engine/state.
- City turn-flow mechanics and payment effects.
- Full City winner-loop completion in first pass.
- Negative tests proving non-City presets are unaffected.

### Regression

- Run focused City tests.
- Run full Monopoly regression (`pytest -k monopoly -v`).
- Run game registry integration smoke tests.

## Acceptance Criteria

1. `city` preset resolves to anchor edition `monopoly-1790` with strict `anchor-first` policy.
2. City mechanics are implemented from anchor notes and are deterministic.
3. Full winner-loop behavior is available in first pass.
4. Core economy safety (liquidation/bankruptcy/accounting) remains correct.
5. Non-City presets retain existing behavior and tests remain green.

## Out Of Scope

- Non-anchor speculative City mechanics.
- Cross-preset refactor to generic variant-strategy architecture.
- Spin-off card-game families (`bid_card_game`, `deal_card_game`) and `knockout` work in this phase.
