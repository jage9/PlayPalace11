# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = Malac
pig-category = Kockajátékok

# Actions
pig-roll = Dobás a kockával
pig-bank = { $points } pont mentése

# Game events (Pig-specific)
pig-rolls = { $player } dobja a kockát...
pig-roll-result = Egy { $roll }, összesen { $total }
pig-bust = Ó ne, egy 1-es! { $player } elveszít { $points } pontot.
pig-bank-action = { $player } úgy dönt, hogy ment { $points } pontot, összesen { $total }
pig-winner = Van győztesünk, és az { $player }!

# Pig-specific options
pig-set-min-bank = Minimum mentés: { $points }
pig-set-dice-sides = Kocka oldalak: { $sides }
pig-enter-min-bank = Add meg a minimum mentendő pontokat:
pig-enter-dice-sides = Add meg a kocka oldalak számát:
pig-option-changed-min-bank = Minimum mentés pontok { $points }-ra változtak
pig-option-changed-dice = A kocka most { $sides } oldallal rendelkezik

# Disabled reasons
pig-need-more-points = Több pontra van szükséged a mentéshez.

# Validation errors
pig-error-min-bank-too-high = A minimum mentés pontoknak kisebbnek kell lenniük, mint a célpontszám.
