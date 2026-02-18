# Farkle game messages

# Game info
game-name-farkle = Фаркл

# Actions - Roll and Bank
farkle-roll = Кинути { $count } { $count ->
    [one] кубик
   *[other] кубиків
}
farkle-bank = Зберегти { $points } очок

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = Одна 1 за { $points } очок
farkle-take-single-five = Одна 5 за { $points } очок
farkle-take-three-kind = Три { $number } за { $points } очок
farkle-take-four-kind = Чотири { $number } за { $points } очок
farkle-take-five-kind = П'ять { $number } за { $points } очок
farkle-take-six-kind = Шість { $number } за { $points } очок
farkle-take-small-straight = Малий стріт за { $points } очок
farkle-take-large-straight = Великий стріт за { $points } очок
farkle-take-three-pairs = Три пари за { $points } очок
farkle-take-double-triplets = Подвійні трійки за { $points } очок
farkle-take-full-house = Фул-хаус за { $points } очок

# Game events (matching v10 exactly)
farkle-rolls = { $player } кидає { $count } { $count ->
    [one] кубик
   *[other] кубиків
}...
farkle-you-roll = Ви кидаєте { $count } { $count ->
    [one] кубик
   *[other] кубиків
}...
farkle-roll-result = { $dice }
farkle-farkle = ФАРКЛ! { $player } втрачає { $points } очок
farkle-you-farkle = ФАРКЛ! Ви втрачаєте { $points } очок
farkle-takes-combo = { $player } бере { $combo } за { $points } очок
farkle-you-take-combo = Ви берете { $combo } за { $points } очок
farkle-hot-dice = Гарячі кубики!
farkle-banks = { $player } зберігає { $points } очок, всього { $total }
farkle-you-bank = Ви зберігаєте { $points } очок, всього { $total }
farkle-winner = { $player } перемагає з { $score } очками!
farkle-you-win = Ви перемагаєте з { $score } очками!
farkle-winners-tie = У нас нічия! Переможці: { $players }

# Check turn score action
farkle-turn-score = { $player } має { $points } очок цього ходу.
farkle-no-turn = Наразі ніхто не робить хід.

# Farkle-specific options
farkle-set-target-score = Цільовий рахунок: { $score }
farkle-enter-target-score = Введіть цільовий рахунок (500-5000):
farkle-option-changed-target = Цільовий рахунок встановлено на { $score }.

# Disabled action reasons
farkle-must-take-combo = Спочатку ви повинні взяти рахункову комбінацію.
farkle-cannot-bank = Ви не можете зберегти зараз.

# Additional Farkle options
farkle-set-initial-bank-score = Початковий поріг банку: { $score }
farkle-enter-initial-bank-score = Введіть початковий поріг банку (0-1000):
farkle-option-changed-initial-bank-score = Початковий поріг банку встановлено на { $score }.
farkle-toggle-hot-dice-multiplier = Множник hot dice: { $enabled }
farkle-option-changed-hot-dice-multiplier = Множник hot dice встановлено на { $enabled }.

# Action feedback
farkle-minimum-initial-bank-score = Мінімальний початковий поріг банку: { $score }.
