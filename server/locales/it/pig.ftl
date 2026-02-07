# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = Pig
pig-category = Giochi di dadi

# Actions
pig-roll = Tira il dado
pig-bank = Conserva { $points } punti

# Game events (Pig-specific)
pig-rolls = { $player } tira il dado...
pig-roll-result = Un { $roll }, per un totale di { $total }
pig-bust = Oh no, un 1! { $player } perde { $points } punti.
pig-bank-action = { $player } decide di conservare { $points }, per un totale di { $total }
pig-winner = Abbiamo un vincitore, ed è { $player }!

# Pig-specific options
pig-set-min-bank = Conservazione minima: { $points }
pig-set-dice-sides = Facce del dado: { $sides }
pig-enter-min-bank = Inserisci i punti minimi da conservare:
pig-enter-dice-sides = Inserisci il numero di facce del dado:
pig-option-changed-min-bank = Punti minimi di conservazione cambiati a { $points }
pig-option-changed-dice = Il dado ora ha { $sides } facce

# Disabled reasons
pig-need-more-points = Hai bisogno di più punti per conservare.

# Validation errors
pig-error-min-bank-too-high = I punti minimi di conservazione devono essere inferiori al punteggio obiettivo.
