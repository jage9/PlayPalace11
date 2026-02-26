# Monopoly Voice Banking Design (2026-02-26)

## Goal

Implement a maximum-fidelity `voice_banking` preset using the existing deterministic banking simulator plus a deterministic voice-style command layer, with anchor-first policy.

## Confirmed Decisions

1. Next preset target: `voice_banking`.
2. Fidelity target: full.
3. Voice layer approach: simulated in-game command/prompt flow (no external STT/TTS services).
4. Source policy: `anchor-first`.
5. Interaction model: voice-style layer and normal actions both available.
6. Command prefix contract: strict exact prefix `voice:` only (case-sensitive).

## Anchor Context

- Preset id: `voice_banking`
- Catalog anchor edition id: `monopoly-e4816`
- Family: `voice_banking`

## Architecture

### High-Level Split

- Reuse banking simulator (`banking_sim.py`) for all economy state changes.
- Add `voice_banking_profile.py` for anchor-driven preset configuration.
- Add `voice_commands.py` for deterministic command parsing and intent mapping.
- Integrate in `MonopolyGame` with strict preset gating.

### Preset Routing

- `voice_banking`:
  - simulator-backed economy
  - voice-style command entry via `voice:` prefix
  - normal Monopoly actions still available
- all other presets:
  - no voice command parsing path changes
  - unchanged gameplay behavior

## Components and Data Flow

### VoiceBankingProfile

Dataclass fields:

- `preset_id`
- `anchor_edition_id`
- `source_policy`
- `starting_balance`
- `pass_go_credit`
- `command_mode`
- `confirmation_required_for_transfers`
- provenance notes

Resolver:

- `resolve_voice_banking_profile("voice_banking")` returns anchor-first defaults for `monopoly-e4816`.

### Voice Commands Module

Primary entry:

- `parse_voice_command(text, current_player, game_state) -> VoiceIntent | VoiceParseError`

Supported phase-1 intents:

- `check_balance`
- `transfer_amount_to_player`
- `show_recent_ledger`
- `repeat_last_bank_result`

Parser behavior:

- command is parsed only if input starts with exact `voice:`
- payload is text after `voice:`
- deterministic token patterns only (no fuzzy matching)

### Runtime Flow

1. Player enters message.
2. If no exact `voice:` prefix, treat as normal non-command text.
3. If prefixed, parse to intent.
4. Validate intent arguments and command phase (including optional transfer confirmation).
5. Route to simulator operation/query.
6. Sync mirrored `player.cash`, scores, and emit localized assistant-style response.

## Rules and UX Behavior

### Economy

- Money movement in `voice_banking` is simulator-backed.
- Existing liquid-balance helpers remain the source for decisions and checks.

### Dual Interface

- Keep normal actions available for accessibility and regression safety.
- Add voice-style command action path in parallel.

### Transfer Confirmation

- Profile controls confirmation requirement (default enabled for fidelity).
- Flow:
  - command stages transfer request
  - confirm command executes request
- staged transfer is player-bound and expires deterministically.

### Response Scope

- Private responses for personal financial details.
- Broadcast responses for successful inter-player transfer events.

## Command Contract

Strict contract:

- Only exact prefix `voice:` is accepted.
- Case-sensitive, no aliases (`Voice:`, `VOICE:` not accepted).
- Example valid command: `voice: transfer 200 to Guest`.

## Error Handling

- Prefix missing: no command execution.
- Empty payload after prefix: localized “missing command” response.
- Unknown command: localized “not recognized” + short usage hint.
- Validation failures:
  - invalid target
  - invalid amount
  - insufficient funds
  - inactive account
  - confirmation mismatch/expired staged transfer
- Failed operations do not partially mutate balances.

## Determinism and Safety

- Deterministic parser, intent resolution, and simulator transaction ordering.
- Confirmation token/state bound to player + turn + staged transfer details.
- No network/service dependencies in command processing.

## Testing Strategy

### Unit

- `voice_commands` parser tests:
  - strict `voice:` prefix requirement
  - supported intent parsing
  - invalid/unknown command handling

### Integration

- `voice_banking` startup profile/state initialization.
- `voice: check balance` response path.
- transfer stage + confirm flow.
- insufficient funds transfer failure with unchanged balances.
- non-prefixed input does not execute commands.
- normal board actions still operate in this preset.

### Regression

- Existing Monopoly suites (`classic`, `electronic_banking`, `junior_*`, `speed`, etc.) remain unchanged and green.

## Acceptance Criteria

1. `voice_banking` preset is playable with simulator-backed economy.
2. Voice-style commands work only with exact `voice:` prefix.
3. Transfer confirmation flow behaves deterministically and safely.
4. Localized assistant-style responses cover success/failure paths.
5. Existing Monopoly regression tests remain green.

## Out Of Scope

- Real STT/TTS integration.
- Fuzzy natural-language parsing.
- Cross-preset command processing changes.
