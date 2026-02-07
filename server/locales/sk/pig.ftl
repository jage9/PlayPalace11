# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = Prasa
pig-category = Kockové hry

# Actions
pig-roll = Hodiť kockou
pig-bank = Uložiť { $points } bodov

# Game events (Pig-specific)
pig-rolls = { $player } hádže kockou...
pig-roll-result = { $roll }, celkom { $total }
pig-bust = Ale nie, jednotka! { $player } stráca { $points } bodov.
pig-bank-action = { $player } sa rozhodol uložiť { $points }, celkom { $total }
pig-winner = Máme víťaza a je to { $player }!

# Pig-specific options
pig-set-min-bank = Minimálne uloženie: { $points }
pig-set-dice-sides = Strán kocky: { $sides }
pig-enter-min-bank = Zadajte minimálne body na uloženie:
pig-enter-dice-sides = Zadajte počet strán kocky:
pig-option-changed-min-bank = Minimálne uloženie bodov zmenené na { $points }
pig-option-changed-dice = Kocka má teraz { $sides } strán

# Disabled reasons
pig-need-more-points = Potrebujete viac bodov na uloženie.

# Validation errors
pig-error-min-bank-too-high = Minimálne body na uloženie musia byť nižšie ako cieľové skóre.
