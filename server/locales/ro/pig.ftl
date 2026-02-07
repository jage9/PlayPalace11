# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = Porcul
pig-category = Jocuri cu zaruri

# Actions
pig-roll = Aruncă zarul
pig-bank = Salvează { $points } puncte

# Game events (Pig-specific)
pig-rolls = { $player } aruncă zarul...
pig-roll-result = Un { $roll }, pentru un total de { $total }
pig-bust = Oh nu, un 1! { $player } pierde { $points } puncte.
pig-bank-action = { $player } decide să salveze { $points }, pentru un total de { $total }
pig-winner = Avem un câștigător, și acesta este { $player }!

# Pig-specific options
pig-set-min-bank = Salvare minimă: { $points }
pig-set-dice-sides = Fețe zar: { $sides }
pig-enter-min-bank = Introduceți punctele minime de salvat:
pig-enter-dice-sides = Introduceți numărul de fețe ale zarului:
pig-option-changed-min-bank = Punctele minime de salvare au fost schimbate la { $points }
pig-option-changed-dice = Zarul are acum { $sides } fețe

# Disabled reasons
pig-need-more-points = Ai nevoie de mai multe puncte pentru a salva.

# Validation errors
pig-error-min-bank-too-high = Punctele minime de salvare trebuie să fie mai mici decât scorul țintă.
