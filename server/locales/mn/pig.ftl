# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = Гахай
pig-category = Шооны тоглоомууд

# Actions
pig-roll = Шоо шидэх
pig-bank = { $points } оноо хадгалах

# Game events (Pig-specific)
pig-rolls = { $player } шоо шидэж байна...
pig-roll-result = { $roll } гарлаа, нийт { $total } болов
pig-bust = Өө, 1 гарлаа! { $player } { $points } оноо алдлаа.
pig-bank-action = { $player } { $points } оноо хадгалахаар шийдсэн, нийт { $total } болов
pig-winner = Ялагч тодорлоо, тэр бол { $player }!

# Pig-specific options
pig-set-min-bank = Хамгийн бага хадгалалт: { $points }
pig-set-dice-sides = Шооны талууд: { $sides }
pig-enter-min-bank = Хадгалах хамгийн бага оноо оруулна уу:
pig-enter-dice-sides = Шооны талуудын тоо оруулна уу:
pig-option-changed-min-bank = Хамгийн бага хадгалах оноо { $points } болов
pig-option-changed-dice = Шоо одоо { $sides } талтай болов

# Disabled reasons
pig-need-more-points = Хадгалахын тулд илүү их оноо хэрэгтэй.

# Validation errors
pig-error-min-bank-too-high = Хамгийн бага хадгалах оноо зорилтот оноогоос бага байх ёстой.
