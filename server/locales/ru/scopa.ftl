# Scopa game messages
# Note: Common messages like round-start, turn-start, target-score, team-mode are in games.ftl

# Game name
game-name-scopa = Скопа

# Game events
scopa-initial-table = Карты на столе: { $cards }
scopa-no-initial-table = На столе нет карт для начала игры.
scopa-you-collect = Вы забираете { $cards } картой { $card }
scopa-player-collects = { $player } забирает { $cards } картой { $card }
scopa-you-put-down = Вы выкладываете карту: { $card }.
scopa-player-puts-down = { $player } выкладывает карту: { $card }.
scopa-scopa-suffix =  — СКОПА!
scopa-clear-table-suffix = , очищая стол.
scopa-remaining-cards = { $player } забирает оставшиеся на столе карты.
scopa-scoring-round = Подсчёт очков...
scopa-most-cards = { $player } получает 1 очко за наибольшее количество карт ({ $count }).
scopa-most-cards-tie = По количеству карт ничья — очко не присуждается.
scopa-most-diamonds = { $player } получает 1 очко за наибольшее количество бубен ({ $count }).
scopa-most-diamonds-tie = По количеству бубен ничья — очко не присуждается.
scopa-seven-diamonds = { $player } получает 1 очко за семёрку бубен.
scopa-seven-diamonds-multi = { $player } получает 1 очко за наибольшее количество семёрок бубен ({ $count } × 7 бубен).
scopa-seven-diamonds-tie = По количеству семёрок бубен ничья — очко не присуждается.
scopa-most-sevens = { $player } получает 1 очко за наибольшее количество семёрок ({ $count }).
scopa-most-sevens-tie = По количеству семёрок ничья — очко не присуждается.
scopa-round-scores = Очки за раунд:
scopa-round-score-line = { $player }: +{ $round_score } (всего: { $total_score })
scopa-table-empty = На столе нет карт.
scopa-no-such-card = На этой позиции нет карты.
scopa-captured-count = Вы забрали { $count } { $count ->
    [one] карту
    [few] карты
   *[other] карт
}

# View actions
scopa-view-table = Посмотреть на стол
scopa-view-captured = Посмотреть забранные карты

# Scopa-specific options
scopa-enter-target-score = Введите конечный счёт (1–121)
scopa-set-cards-per-deal = Карт при раздаче: { $cards }
scopa-enter-cards-per-deal = Введите количество карт при раздаче (1–10)
scopa-set-decks = Количество колод: { $decks }
scopa-enter-decks = Введите количество колод (1–6)
scopa-toggle-escoba = Эскоба (сумма до 15): { $enabled }
scopa-toggle-hints = Подсказки для взятия: { $enabled }
scopa-set-mechanic = Механика «Скопы»: { $mechanic }
scopa-select-mechanic = Выберите механику игры
scopa-toggle-instant-win = Мгновенная победа при «Скопе»: { $enabled }
scopa-toggle-team-scoring = Общие карты команды при подсчёте: { $enabled }
scopa-toggle-inverse = Инверсивный режим (цель = выбывание): { $enabled }

# Option change announcements
scopa-option-changed-cards = Количество карт при раздаче установлено на { $cards }.
scopa-option-changed-decks = Количество колод установлено на { $decks }.
scopa-option-changed-escoba = Режим «Эскоба»: { $enabled }.
scopa-option-changed-hints = Подсказки для взятия: { $enabled }.
scopa-option-changed-mechanic = Механика игры установлена на: { $mechanic }.
scopa-option-changed-instant = Мгновенная победа при «Скопе»: { $enabled }.
scopa-option-changed-team-scoring = Командный подсчёт карт: { $enabled }.
scopa-option-changed-inverse = Инверсивный режим: { $enabled }.

# Scopa mechanic choices
scopa-mechanic-normal = Обычная
scopa-mechanic-no_scopas = Без «Скоп»
scopa-mechanic-only_scopas = Только «Скопы»

# Disabled action reasons
scopa-timer-not-active = Таймер раунда не активен.

# Validation errors
scopa-error-not-enough-cards = Недостаточно карт в { $decks } { $decks ->
    [one] колоде
    [few] колодах
   *[other] колодах
} для { $players } { $players ->
    [one] игрока
    [few] игроков
   *[other] игроков
} при раздаче по { $cards_per_deal } { $cards_per_deal ->
    [one] карте
    [few] карты
   *[other] карт
}. (Нужно { $cards_needed }, но в наличии только { $total_cards }.)
