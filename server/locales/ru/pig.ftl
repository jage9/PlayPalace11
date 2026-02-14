# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = Свинья
pig-category = Игры в кости

# Actions
pig-roll = Бросить кубик
pig-bank = Банковать { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}

# Game events (Pig-specific)
pig-rolls = { $player } бросает кубик...
pig-roll-result = Выпало { $roll }, итого: { $total }
pig-bust = О нет, единица! { $player } теряет { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}.
pig-bank-action = { $player } решает забрать { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
} в банк, итого: { $total }
pig-winner = У нас есть победитель, и это { $player }!

# Pig-specific options
pig-set-min-bank = Минимальный банк: { $points }
pig-set-dice-sides = Граней у кубика: { $sides }
pig-enter-min-bank = Введите минимальное количество очков для банка:
pig-enter-dice-sides = Введите количество граней кубика:
pig-option-changed-min-bank = Минимальный порог очков для банка изменён на { $points }.
pig-option-changed-dice = Теперь у кубика { $sides } { $sides ->
    [one] грань
    [few] грани
   *[other] граней
}.

# Disabled reasons
pig-need-more-points = Вам нужно больше очков, чтобы забрать их в банк.

# Validation errors
pig-error-min-bank-too-high = Минимальный порог банка должен быть меньше, чем конечный счёт.
