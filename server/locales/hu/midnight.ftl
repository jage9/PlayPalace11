# 1-4-24 (Midnight) game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-midnight = 1-4-24
midnight-category = Kockajátékok

# Actions
midnight-roll = Dobd a kockákat
midnight-keep-die = Tartsd meg: { $value }
midnight-bank = Befejezés

# Game events
midnight-turn-start = { $player } köre.
midnight-you-rolled = Dobtál: { $dice }.
midnight-player-rolled = { $player } dobott: { $dice }.

# Keeping dice
midnight-you-keep = Megtartod: { $die }.
midnight-player-keeps = { $player } megtartja: { $die }.
midnight-you-unkeep = Elengeded: { $die }.
midnight-player-unkeeps = { $player } elengedi: { $die }.

# Turn status
midnight-you-have-kept = Megtartott kockák: { $kept }. Hátralévő dobások: { $remaining }.
midnight-player-has-kept = { $player } megtartotta: { $kept }. { $remaining } kocka maradt.

# Scoring
midnight-you-scored = { $score } pontot szereztél.
midnight-scored = { $player } { $score } pontot szerzett.
midnight-you-disqualified = Nincs 1-esed és 4-esed is. Kizárva!
midnight-player-disqualified = { $player } nincs 1-ese és 4-ese is. Kizárva!

# Round results
midnight-round-winner = { $player } nyeri a kört!
midnight-round-tie = Döntetlen kör: { $players }.
midnight-all-disqualified = Minden játékos kizárva! Nincs győztes ebben a körben.

# Game winner
midnight-game-winner = { $player } nyeri a játékot { $wins } körgyőzelemmel!
midnight-game-tie = Döntetlen! { $players } mindegyike { $wins } kört nyert.

# Options
midnight-set-rounds = Körök száma: { $rounds }
midnight-enter-rounds = Add meg a körök számát:
midnight-option-changed-rounds = Körök száma módosítva: { $rounds }

# Disabled reasons
midnight-need-to-roll = Először dobnod kell a kockákkal.
midnight-no-dice-to-keep = Nincs elérhető kocka megtartásra.
midnight-must-keep-one = Dobásonként legalább egy kockát meg kell tartanod.
midnight-must-roll-first = Először dobnod kell a kockákkal.
midnight-keep-all-first = Minden kockát meg kell tartanod befejezés előtt.
