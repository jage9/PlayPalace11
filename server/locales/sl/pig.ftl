# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = Prašič
pig-category = Igre s kockami

# Actions
pig-roll = Vrzi kocko
pig-bank = Shrani { $points } točk

# Game events (Pig-specific)
pig-rolls = { $player } vrže kocko...
pig-roll-result = { $roll }, skupaj { $total }
pig-bust = O ne, enica! { $player } izgubi { $points } točk.
pig-bank-action = { $player } se odloči shraniti { $points }, skupaj { $total }
pig-winner = Imamo zmagovalca, in to je { $player }!

# Pig-specific options
pig-set-min-bank = Minimalno shranjevanje: { $points }
pig-set-dice-sides = Strani kocke: { $sides }
pig-enter-min-bank = Vnesite minimalne točke za shranjevanje:
pig-enter-dice-sides = Vnesite število strani kocke:
pig-option-changed-min-bank = Minimalne točke za shranjevanje spremenjene na { $points }
pig-option-changed-dice = Kocka ima zdaj { $sides } strani

# Disabled reasons
pig-need-more-points = Potrebujete več točk za shranjevanje.

# Validation errors
pig-error-min-bank-too-high = Minimalne točke za shranjevanje morajo biti nižje od ciljnega rezultata.
