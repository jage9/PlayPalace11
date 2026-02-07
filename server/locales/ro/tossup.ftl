# Toss Up game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-tossup = Aruncare sus
tossup-category = Jocuri cu zaruri

# Actions
tossup-roll-first = Aruncă { $count } zaruri
tossup-roll-remaining = Aruncă { $count } zaruri rămase
tossup-bank = Salvează { $points } puncte

# Game events
tossup-turn-start = Tura lui { $player }. Scor: { $score }
tossup-you-roll = Ai aruncat: { $results }.
tossup-player-rolls = { $player } a aruncat: { $results }.

# Turn status
tossup-you-have-points = Puncte tură: { $turn_points }. Zaruri rămase: { $dice_count }.
tossup-player-has-points = { $player } are { $turn_points } puncte tură. { $dice_count } zaruri rămase.

# Fresh dice
tossup-you-get-fresh = Niciun zar rămas! Primești { $count } zaruri noi.
tossup-player-gets-fresh = { $player } primește { $count } zaruri noi.

# Bust
tossup-you-bust = Explozie! Pierzi { $points } puncte pentru această tură.
tossup-player-busts = { $player } explodează și pierde { $points } puncte!

# Bank
tossup-you-bank = Salvezi { $points } puncte. Scor total: { $total }.
tossup-player-banks = { $player } salvează { $points } puncte. Scor total: { $total }.

# Winner
tossup-winner = { $player } câștigă cu { $score } puncte!
tossup-tie-tiebreaker = Este egalitate între { $players }! Rundă decisivă!

# Options
tossup-set-rules-variant = Variantă reguli: { $variant }
tossup-select-rules-variant = Selectați varianta regulilor:
tossup-option-changed-rules = Variantă reguli schimbată la { $variant }

tossup-set-starting-dice = Zaruri inițiale: { $count }
tossup-enter-starting-dice = Introduceți numărul de zaruri inițiale:
tossup-option-changed-dice = Zaruri inițiale schimbate la { $count }

# Rules variants
tossup-rules-standard = Standard
tossup-rules-playpalace = PlayPalace

# Rules explanations
tossup-rules-standard-desc = 3 verzi, 2 galbene, 1 roșu per zar. Explozie dacă niciun verde și cel puțin un roșu.
tossup-rules-playpalace-desc = Distribuție egală. Explozie dacă toate zarurile sunt roșii.

# Disabled reasons
tossup-need-points = Ai nevoie de puncte pentru a salva.
