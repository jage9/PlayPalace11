# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = Grisen
pig-category = Tärningsspel

# Actions
pig-roll = Kasta tärningen
pig-bank = Spara { $points } poäng

# Game events (Pig-specific)
pig-rolls = { $player } kastar tärningen...
pig-roll-result = En { $roll }, för totalt { $total }
pig-bust = Åh nej, en etta! { $player } förlorar { $points } poäng.
pig-bank-action = { $player } bestämmer sig för att spara { $points }, för totalt { $total }
pig-winner = Vi har en vinnare, och det är { $player }!

# Pig-specific options
pig-set-min-bank = Minsta sparande: { $points }
pig-set-dice-sides = Tärningssidor: { $sides }
pig-enter-min-bank = Ange minsta poäng att spara:
pig-enter-dice-sides = Ange antal tärningssidor:
pig-option-changed-min-bank = Minsta sparande poäng ändrades till { $points }
pig-option-changed-dice = Tärningen har nu { $sides } sidor

# Disabled reasons
pig-need-more-points = Du behöver fler poäng för att spara.

# Validation errors
pig-error-min-bank-too-high = Minsta sparande poäng måste vara lägre än målpoängen.
