# Toss Up game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-tossup = Тосс-ап
tossup-category = Игры в кости

# Actions
tossup-roll-first = Бросить { $count } { $count ->
    [one] кубик
    [few] кубика
   *[other] кубиков
}
tossup-roll-remaining = Бросить оставшиеся { $count } { $count ->
    [one] кубик
    [few] кубика
   *[other] кубиков
}
tossup-bank = Банковать { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}

# Game events
tossup-turn-start = Ход игрока { $player }. Счёт: { $score }.
tossup-you-roll = Вы выбросили: { $results }.
tossup-player-rolls = { $player } выбрасывает: { $results }.

# Turn status
tossup-you-have-points = Очки за ход: { $turn_points }. Осталось кубиков: { $dice_count }.
tossup-player-has-points = У игрока { $player } { $turn_points } { $turn_points ->
    [one] очко
    [few] очка
   *[other] очков
} за этот ход. Осталось кубиков: { $dice_count }.

# Fresh dice
tossup-you-get-fresh = Кубиков не осталось! Берём { $count } { $count ->
    [one] новый кубик
    [few] новых кубика
   *[other] новых кубиков
}.
tossup-player-gets-fresh = У игрока { $player } закончились кубики, он берёт { $count } { $count ->
    [one] новый
    [few] новых
   *[other] новых
}.

# Bust
tossup-you-bust = Сгорели! Вы теряете { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}, набранных за этот ход.
tossup-player-busts = { $player } сгорает и теряет { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}!

# Bank
tossup-you-bank = Вы банкуете { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}. Общий счёт: { $total }.
tossup-player-banks = { $player } банкует { $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}. Общий счёт: { $total }.

# Winner
tossup-winner = { $player } побеждает, набрав { $score } { $score ->
    [one] очко
    [few] очка
   *[other] очков
}!
tossup-tie-tiebreaker = Ничья между игроками: { $players }! Раунд для определения победителя!

# Options
tossup-set-rules-variant = Вариант правил: { $variant }
tossup-select-rules-variant = Выберите вариант правил:
tossup-option-changed-rules = Вариант правил изменён на: { $variant }.

tossup-set-starting-dice = Количество кубиков: { $count }
tossup-enter-starting-dice = Введите количество кубиков для начала игры:
tossup-option-changed-dice = Количество кубиков изменено на { $count }.

# Rules variants
tossup-rules-standard = Стандартный
tossup-rules-playpalace = PlayPalace

# Rules explanations
tossup-rules-standard-desc = На каждом кубике: 3 зелёных, 2 жёлтых и 1 красная грань. Ход сгорает, если нет зелёных и выпала хотя бы одна красная.
tossup-rules-playpalace-desc = Равномерное распределение цветов. Ход сгорает только в том случае, если на всех кубиках выпал красный.

# Disabled reasons
tossup-need-points = Вам нужно набрать очки, прежде чем забирать их в банк.
