# Monopoly Mario Board Anchor Notes

## Wave 1 Boards
- `mario_collectors` -> `monopoly-c4382` (Monopoly: Super Mario Bros. Collector's Edition)
- `mario_kart` -> `monopoly-e1870` (Monopoly Gamer Mario Kart)
- `mario_celebration` -> `monopoly-e9517` (Monopoly Super Mario Celebration)
- `mario_movie` -> `monopoly-f6818` (Monopoly The Super Mario Bros. Movie Edition)
- `junior_super_mario` -> `monopoly-f4817` (Monopoly Junior Super Mario Edition)

## Source Policy
- Rule resolution policy: `anchor-first`
- Conflict fallback: anchor family evidence -> deterministic safe default

## Manual Sources (en-us)
- `monopoly-c4382`
  - instruction: `https://instructions.hasbro.com/en-us/instruction/monopoly-super-mario-bros-collector-s-edition-board-game-ages-8-and-up`
  - pdf: `https://assets-us-01.kc-usercontent.com:443/500e0a65-283d-00ef-33b2-7f1f20488fe2/0855c1af-ad39-4304-8895-92f61228f71f/Monopoly%20Super%20Mario%20Bros.%20Collector%27s%20Edition%20%281%29.pdf`
- `monopoly-e1870`
  - instruction: `https://instructions.hasbro.com/en-us/instruction/Monopoly-Gamer-Mario-Kart`
  - pdf: `https://assets-us-01.kc-usercontent.com:443/500e0a65-283d-00ef-33b2-7f1f20488fe2/6fa72e6d-38e2-4036-8cc4-e65aa8e81abc/E18700000_MN_Gamer_Kart_INST.pdf`
- `monopoly-e9517`
  - instruction: `https://instructions.hasbro.com/en-us/instruction/monopoly-super-mario-celebration-edition-board-game-instructions`
  - pdf: `https://assets-us-01.kc-usercontent.com:443/500e0a65-283d-00ef-33b2-7f1f20488fe2/6583f8cd-113c-461f-9f7f-92ac10c3a579/E95170000_INST_MN_SuperMario_F20_P1_FFR.pdf`
- `monopoly-f6818`
  - instruction: `https://instructions.hasbro.com/en-us/instruction/monopoly-the-super-mario-bros-movie-edition-kids-board-game-includes-bowser-token-family-games-ages-8`
  - pdf: `https://assets-us-01.kc-usercontent.com:443/500e0a65-283d-00ef-33b2-7f1f20488fe2/6d0c863f-5c00-4c9d-8b5b-edcfd9136558/F68180000_INST_MONOPOLY_SUPER_MARIO_MOVIE_S23.pdf`
- `monopoly-f4817`
  - instruction: `https://instructions.hasbro.com/en-us/instruction/monopoly-junior-super-mario-edition-board-game-ages-5-explore-the-mushroom-kingdom-as-mario-peach-yoshi-or-luigi`
  - pdf: `https://assets-us-01.kc-usercontent.com:443/500e0a65-283d-00ef-33b2-7f1f20488fe2/5b7fac09-cdf9-4f63-9efe-9483c26b33a1/F48170000_INST_MN_Jr_SuperMario_I.pdf`

## Normalized Rule Table
| board_id | anchor_edition_id | compatible_presets | rule_pack_id | rule_pack_status | pass_go_credit | notes |
|---|---|---|---|---|---:|---|
| `classic_default` | `monopoly-00009` | `classic_standard` | _(none)_ | `none` | 200 | Base classic/themed standard fallback board profile. |
| `mario_collectors` | `monopoly-c4382` | `classic_standard` | `mario_collectors` | `partial` | 200 | Wave 1 Mario board; unimplemented mechanics fall back to classic behavior. |
| `mario_kart` | `monopoly-e1870` | `classic_standard` | `mario_kart` | `partial` | 200 | Wave 1 Mario board; unimplemented mechanics fall back to classic behavior. |
| `mario_celebration` | `monopoly-e9517` | `classic_standard` | `mario_celebration` | `partial` | 200 | Wave 1 Mario board; unimplemented mechanics fall back to classic behavior. |
| `mario_movie` | `monopoly-f6818` | `classic_standard` | `mario_movie` | `partial` | 200 | Wave 1 Mario board; unimplemented mechanics fall back to classic behavior. |
| `junior_super_mario` | `monopoly-f4817` | `junior`, `junior_modern`, `junior_legacy` | `junior_super_mario` | `partial` | 2 | Junior path board profile; incompatible presets auto-fix to `junior`. |

## Wave 4 Promotions
- `mario_kart`: added `card_id_remap` behavior (partial_rules+).
- `mario_movie`: added `card_cash_override` behavior (partial_rules+).

## Next Mario Targets
1. Promote `mario_collectors` with one card capability.
2. Promote `mario_celebration` with one card capability.
3. Define Junior-safe mechanic plan for `junior_super_mario`.
