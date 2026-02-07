# Tradeoff game messages

# Game info
game-name-tradeoff = Обмін

# Round and iteration flow
tradeoff-round-start = Раунд { $round }.
tradeoff-iteration = Роздача { $iteration } з 3.

# Phase 1: Trading
tradeoff-you-rolled = Ви кинули: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = обмінюється
tradeoff-trade-status-keeping = зберігається
tradeoff-confirm-trades = Підтвердити обміни ({ $count } кубиків)
tradeoff-keeping = Зберігаємо { $value }.
tradeoff-trading = Обмінюємо { $value }.
tradeoff-player-traded = { $player } обміняв: { $dice }.
tradeoff-player-traded-none = { $player } зберіг усі кубики.

# Phase 2: Taking from pool
tradeoff-your-turn-take = Ваш хід взяти кубик з пулу.
tradeoff-take-die = Взяти { $value } ({ $remaining } залишилось)
tradeoff-you-take = Ви берете { $value }.
tradeoff-player-takes = { $player } бере { $value }.

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points } оч): { $sets }.
tradeoff-no-sets = { $player }: немає сетів.

# Set descriptions (concise)
tradeoff-set-triple = трійка { $value }
tradeoff-set-group = група { $value }
tradeoff-set-mini-straight = міні стріт { $low }-{ $high }
tradeoff-set-double-triple = подвійна трійка ({ $v1 } та { $v2 })
tradeoff-set-straight = стріт { $low }-{ $high }
tradeoff-set-double-group = подвійна група ({ $v1 } та { $v2 })
tradeoff-set-all-groups = всі групи
tradeoff-set-all-triplets = всі трійки

# Round end
tradeoff-round-scores = Очки раунду { $round }:
tradeoff-score-line = { $player }: +{ $round_points } (всього: { $total })
tradeoff-leader = { $player } лідирує з { $score }.

# Game end
tradeoff-winner = { $player } виграє з { $score } очками!
tradeoff-winners-tie = Нічия! { $players } зрівнялись з { $score } очками!

# Status checks
tradeoff-view-hand = Переглянути свою руку
tradeoff-view-pool = Переглянути пул
tradeoff-view-players = Переглянути гравців
tradeoff-hand-display = Ваша рука ({ $count } кубиків): { $dice }
tradeoff-pool-display = Пул ({ $count } кубиків): { $dice }
tradeoff-player-info = { $player }: { $hand }. Обміняв: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. Нічого не обміняв.

# Error messages
tradeoff-not-trading-phase = Не в фазі обміну.
tradeoff-not-taking-phase = Не в фазі взяття.
tradeoff-already-confirmed = Вже підтверджено.
tradeoff-no-die = Немає кубика для перемикання.
tradeoff-no-more-takes = Більше немає можливості взяти.
tradeoff-not-in-pool = Цього кубика немає в пулі.

# Options
tradeoff-set-target = Цільовий рахунок: { $score }
tradeoff-enter-target = Введіть цільовий рахунок:
tradeoff-option-changed-target = Цільовий рахунок встановлено на { $score }.
