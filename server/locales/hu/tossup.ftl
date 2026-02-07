# Toss Up game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-tossup = Feldobás
tossup-category = Kockajátékok

# Actions
tossup-roll-first = Dobj { $count } kockát
tossup-roll-remaining = Dobj a maradék { $count } kockát
tossup-bank = Ments { $points } pontot

# Game events
tossup-turn-start = { $player } köre. Pontszám: { $score }
tossup-you-roll = Dobtál: { $results }.
tossup-player-rolls = { $player } dobott: { $results }.

# Turn status
tossup-you-have-points = Kör pontok: { $turn_points }. Hátralévő kockák: { $dice_count }.
tossup-player-has-points = { $player }-nak/nek { $turn_points } kör pontja van. { $dice_count } kocka maradt.

# Fresh dice
tossup-you-get-fresh = Nincs több kocka! Kapsz { $count } új kockát.
tossup-player-gets-fresh = { $player } kap { $count } új kockát.

# Bust
tossup-you-bust = Csőd! Veszítesz { $points } pontot ebben a körben.
tossup-player-busts = { $player } csődbe ment és veszít { $points } pontot!

# Bank
tossup-you-bank = Mentesz { $points } pontot. Összpontszám: { $total }.
tossup-player-banks = { $player } ment { $points } pontot. Összpontszám: { $total }.

# Winner
tossup-winner = { $player } győz { $score } ponttal!
tossup-tie-tiebreaker = Döntetlen { $players } között! Döntő kör!

# Options
tossup-set-rules-variant = Szabályvariáns: { $variant }
tossup-select-rules-variant = Válassz szabályvariánst:
tossup-option-changed-rules = Szabályvariáns megváltoztatva: { $variant }

tossup-set-starting-dice = Kezdő kockák: { $count }
tossup-enter-starting-dice = Add meg a kezdő kockák számát:
tossup-option-changed-dice = Kezdő kockák megváltoztatva: { $count }

# Rules variants
tossup-rules-standard = Standard
tossup-rules-playpalace = PlayPalace

# Rules explanations
tossup-rules-standard-desc = 3 zöld, 2 sárga, 1 piros kockánként. Csőd ha nincs zöld és legalább egy piros van.
tossup-rules-playpalace-desc = Egyenletes eloszlás. Csőd ha minden kocka piros.

# Disabled reasons
tossup-need-points = Pontokra van szükséged a mentéshez.
