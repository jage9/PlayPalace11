# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = Svinja
pig-category = Igre s kockicama

# Actions
pig-roll = Baci kockicu
pig-bank = Spremi { $points } bodova

# Game events (Pig-specific)
pig-rolls = { $player } baca kockicu...
pig-roll-result = { $roll }, ukupno { $total }
pig-bust = O ne, jedinica! { $player } gubi { $points } bodova.
pig-bank-action = { $player } odlučuje spremiti { $points }, ukupno { $total }
pig-winner = Imamo pobjednika, i to je { $player }!

# Pig-specific options
pig-set-min-bank = Minimalno spremanje: { $points }
pig-set-dice-sides = Strane kockice: { $sides }
pig-enter-min-bank = Unesite minimalne bodove za spremanje:
pig-enter-dice-sides = Unesite broj strana kockice:
pig-option-changed-min-bank = Minimalni bodovi za spremanje promijenjeni na { $points }
pig-option-changed-dice = Kockica sada ima { $sides } strana

# Disabled reasons
pig-need-more-points = Trebate više bodova za spremanje.

# Validation errors
pig-error-min-bank-too-high = Minimalni bodovi za spremanje moraju biti manji od ciljnog rezultata.
