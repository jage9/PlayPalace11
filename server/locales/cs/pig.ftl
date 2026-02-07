# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = Prase
pig-category = Karetní hry

# Actions
pig-roll = Hodit kostkou
pig-bank = Uložit { $points } bodů

# Game events (Pig-specific)
pig-rolls = { $player } hází kostkou...
pig-roll-result = { $roll }, celkem { $total }
pig-bust = Ale ne, jednička! { $player } ztrácí { $points } bodů.
pig-bank-action = { $player } se rozhodl uložit { $points }, celkem { $total }
pig-winner = Máme vítěze a je to { $player }!

# Pig-specific options
pig-set-min-bank = Minimální uložení: { $points }
pig-set-dice-sides = Stran kostky: { $sides }
pig-enter-min-bank = Zadejte minimální body k uložení:
pig-enter-dice-sides = Zadejte počet stran kostky:
pig-option-changed-min-bank = Minimální uložení bodů změněno na { $points }
pig-option-changed-dice = Kostka má nyní { $sides } stran

# Disabled reasons
pig-need-more-points = Potřebujete více bodů k uložení.

# Validation errors
pig-error-min-bank-too-high = Minimální body k uložení musí být nižší než cílové skóre.
