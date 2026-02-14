# Threes dice game messages

# Game info
game-name-threes = Тройки
threes-category = Игры в кости

# Actions
threes-roll = Бросить кубики
threes-bank = Зафиксировать счёт и закончить ход
threes-check-hand = Проверить кубики

# Rolling
threes-you-rolled = Вы выбросили: { $dice }
threes-player-rolled = { $player } выбрасывает: { $dice }
threes-must-keep = Вы должны оставить хотя бы один кубик перед следующим броском.

# Dice status (keeping messages now in games.ftl)
threes-no-dice-yet = Вы ещё не бросали кубики.
threes-your-dice = Ваши кубики: { $dice }

# Scoring
threes-you-scored = Вы набрали { $score } { $score ->
    [one] очко
    [few] очка
   *[other] очков
} за этот ход.
threes-scored = { $player } набрал { $score } { $score ->
    [one] очко
    [few] очка
   *[other] очков
} за этот ход.
threes-you-shot-moon = «Выстрел по луне»! Вы набрали -30 очков!
threes-shot-moon = «Выстрел по луне»! { $player } набрал -30 очков!

# Round flow
threes-round-start = Раунд { $round } из { $total }.
threes-round-scores = Результаты за раунд { $round }: { $scores }

# Game end
threes-winner = { $player } побеждает с результатом { $score } { $score ->
    [one] очко
    [few] очка
   *[other] очков
}!
threes-tie = Ничья ({ $players }) с результатом { $score } { $score ->
    [one] очко
    [few] очка
   *[other] очков
}!

# Options
threes-set-rounds = Раундов: { $rounds }
threes-enter-rounds = Введите количество раундов:
threes-option-changed-rounds = Количество раундов установлено на { $rounds }.

# Disabled reasons
threes-must-bank = Теперь вы должны зафиксировать счёт.
threes-roll-first = Сначала нужно бросить кубики.
threes-keep-all-first = Чтобы зафиксировать счёт, сначала нужно выбрать все кубики.
threes-last-die = Это ваш последний кубик.
