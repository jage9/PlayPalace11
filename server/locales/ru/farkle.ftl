# Farkle game messages

# Game info
game-name-farkle = Фаркл

# Actions - Roll and Bank
farkle-roll = Бросить { $count } { $count ->
    [one] кубик
    [few] кубика
   *[other] кубиков
}
farkle-bank = Банковать { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = Одна единица за { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}
farkle-take-single-five = Одна пятёрка за { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}
farkle-take-three-kind = Три «{ $number }» за { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}
farkle-take-four-kind = Четыре «{ $number }» за { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}
farkle-take-five-kind = Пять «{ $number }» за { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}
farkle-take-six-kind = Шесть «{ $number }» за { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}
farkle-take-small-straight = Малый стрит за { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}
farkle-take-large-straight = Большой стрит за { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}
farkle-take-three-pairs = Три пары за { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}
farkle-take-double-triplets = Два триплета за { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}
farkle-take-full-house = Фулл-хаус за { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}

# Game events (matching v10 exactly)
farkle-rolls = { $player } бросает { $count } { $count ->
    [one] кубик
    [few] кубика
   *[other] кубиков
}...
farkle-roll-result = { $dice }
farkle-farkle = ФАРКЛ! { $player } теряет { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}
farkle-takes-combo = { $player } берёт комбинацию «{ $combo }» за { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}
farkle-you-take-combo = Вы берёте комбинацию «{ $combo }» за { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}
farkle-hot-dice = Горячие кубики!
farkle-banks = { $player } банкует { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
} (всего { $total })
farkle-winner = { $player } побеждает, набрав { $score } { $score ->
    [one] очко
    [few] очка
   *[other] очков
}!
farkle-winners-tie = Ничья! Победители: { $players }

# Check turn score action
farkle-turn-score = У игрока { $player } { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
} за этот ход.
farkle-no-turn = Сейчас никто не ходит.

# Farkle-specific options
farkle-set-target-score = Конечный счёт: { $score }
farkle-enter-target-score = Введите конечный счёт (500–5000):
farkle-option-changed-target = Конечный счёт установлен на { $score }.

# Disabled action reasons
farkle-must-take-combo = Сначала нужно выбрать выигрышную комбинацию.
farkle-cannot-bank = Сейчас нельзя забрать очки в банк.
