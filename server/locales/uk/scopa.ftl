# Scopa game messages
# Note: Common messages like round-start, turn-start, target-score, team-mode are in games.ftl

# Game name
game-name-scopa = Скопа

# Game events
scopa-initial-table = Карти столу: { $cards }
scopa-no-initial-table = Немає карт на столі для початку.
scopa-you-collect = Ви збираєте { $cards } з { $card }
scopa-player-collects = { $player } збирає { $cards } з { $card }
scopa-you-put-down = Ви кладете { $card }.
scopa-player-puts-down = { $player } кладе { $card }.
scopa-scopa-suffix =  - СКОПА!
scopa-clear-table-suffix = , очищаючи стіл.
scopa-remaining-cards = { $player } отримує залишкові карти столу.
scopa-scoring-round = Підрахунок очок...
scopa-most-cards = { $player } отримує 1 очко за найбільше карт ({ $count } карт).
scopa-most-cards-tie = Найбільше карт - нічия, очко не присуджується.
scopa-most-diamonds = { $player } отримує 1 очко за найбільше бубнів ({ $count } бубнів).
scopa-most-diamonds-tie = Найбільше бубнів - нічия, очко не присуджується.
scopa-seven-diamonds = { $player } отримує 1 очко за 7 бубен.
scopa-seven-diamonds-multi = { $player } отримує 1 очко за найбільше 7 бубен ({ $count } × 7 бубен).
scopa-seven-diamonds-tie = 7 бубен - нічия, очко не присуджується.
scopa-most-sevens = { $player } отримує 1 очко за найбільше сімок ({ $count } сімок).
scopa-most-sevens-tie = Найбільше сімок - нічия, очко не присуджується.
scopa-round-scores = Очки раунду:
scopa-round-score-line = { $player }: +{ $round_score } (всього: { $total_score })
scopa-table-empty = На столі немає карт.
scopa-no-such-card = Немає карти на цій позиції.
scopa-captured-count = Ви зібрали { $count } карт

# View actions
scopa-view-table = Переглянути стіл
scopa-view-captured = Переглянути зібране

# Scopa-specific options
scopa-enter-target-score = Введіть цільовий рахунок (1-121)
scopa-set-cards-per-deal = Карт на роздачу: { $cards }
scopa-enter-cards-per-deal = Введіть карт на роздачу (1-10)
scopa-set-decks = Кількість колод: { $decks }
scopa-enter-decks = Введіть кількість колод (1-6)
scopa-toggle-escoba = Ескоба (сума до 15): { $enabled }
scopa-toggle-hints = Показувати підказки збору: { $enabled }
scopa-set-mechanic = Механіка скопи: { $mechanic }
scopa-select-mechanic = Виберіть механіку скопи
scopa-toggle-instant-win = Миттєва перемога на скопі: { $enabled }
scopa-toggle-team-scoring = Об'єднувати командні карти для підрахунку: { $enabled }
scopa-toggle-inverse = Інверсний режим (досягнення мети = вибування): { $enabled }

# Option change announcements
scopa-option-changed-cards = Карт на роздачу встановлено на { $cards }.
scopa-option-changed-decks = Кількість колод встановлено на { $decks }.
scopa-option-changed-escoba = Ескоба { $enabled }.
scopa-option-changed-hints = Підказки збору { $enabled }.
scopa-option-changed-mechanic = Механіка скопи встановлена на { $mechanic }.
scopa-option-changed-instant = Миттєва перемога на скопі { $enabled }.
scopa-option-changed-team-scoring = Підрахунок командних карт { $enabled }.
scopa-option-changed-inverse = Інверсний режим { $enabled }.

# Scopa mechanic choices
scopa-mechanic-normal = Нормальна
scopa-mechanic-no_scopas = Без скоп
scopa-mechanic-only_scopas = Тільки скопи

# Disabled action reasons
scopa-timer-not-active = Таймер раунду не активний.

# Validation errors
scopa-error-not-enough-cards = Недостатньо карт у { $decks } { $decks ->
    [one] колоді
    *[other] колодах
} для { $players } { $players ->
    [one] гравця
    *[other] гравців
} з { $cards_per_deal } картами кожному. (Потрібно { $cards_per_deal } × { $players } = { $cards_needed } карт, але є лише { $total_cards }.)
