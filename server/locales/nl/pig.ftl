# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = Pig
pig-category = Dobbelsteenspellen

# Actions
pig-roll = Gooi de dobbelsteen
pig-bank = Bank { $points } punten

# Game events (Pig-specific)
pig-rolls = { $player } gooit de dobbelsteen...
pig-roll-result = Een { $roll }, voor een totaal van { $total }
pig-bust = Oh nee, een 1! { $player } verliest { $points } punten.
pig-bank-action = { $player } besluit { $points } te banken, voor een totaal van { $total }
pig-winner = We hebben een winnaar, en dat is { $player }!

# Pig-specific options
pig-set-min-bank = Minimale bank: { $points }
pig-set-dice-sides = Zijden van dobbelsteen: { $sides }
pig-enter-min-bank = Voer de minimale punten om te banken in:
pig-enter-dice-sides = Voer het aantal zijden van de dobbelsteen in:
pig-option-changed-min-bank = Minimale bankpunten gewijzigd naar { $points }
pig-option-changed-dice = Dobbelsteen heeft nu { $sides } zijden

# Disabled reasons
pig-need-more-points = Je hebt meer punten nodig om te banken.

# Validation errors
pig-error-min-bank-too-high = Minimale bankpunten moeten lager zijn dan de doelscore.
