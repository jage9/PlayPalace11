# Tradeoff game messages

# Game info
game-name-tradeoff = Трейдофф

# Round and iteration flow
tradeoff-round-start = Раунд { $round }.
tradeoff-iteration = Раздача { $iteration } из 3.

# Phase 1: Trading
tradeoff-you-rolled = Вы выбросили: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = обмен
tradeoff-trade-status-keeping = оставить
tradeoff-confirm-trades = Подтвердить обмен ({ $count } { $count ->
    [one] кубика
    [few] кубиков
   *[other] кубиков
})
tradeoff-keeping = Оставляем { $value }.
tradeoff-trading = Меняем { $value }.
tradeoff-player-traded = { $player } обменивает кубики: { $dice }.
tradeoff-player-traded-none = { $player } оставляет все кубики.

# Phase 2: Taking from pool
tradeoff-your-turn-take = Ваш ход: возьмите кубик из пула.
tradeoff-take-die = Взять { $value } (осталось: { $remaining })
tradeoff-you-take = Вы берёте { $value }.
tradeoff-player-takes = { $player } берёт { $value }.

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points } { $points ->
    [one] очко
    [few] очка
   *[other] очков
}): { $sets }.
tradeoff-no-sets = { $player }: нет комбинаций.

# Set descriptions (concise)
tradeoff-set-triple = тройка из { $value }
tradeoff-set-group = группа из { $value }
tradeoff-set-mini-straight = малый стрит { $low }–{ $high }
tradeoff-set-double-triple = двойная тройка ({ $v1 } и { $v2 })
tradeoff-set-straight = стрит { $low }–{ $high }
tradeoff-set-double-group = двойная группа ({ $v1 } и { $v2 })
tradeoff-set-all-groups = все группы
tradeoff-set-all-triplets = все тройки

# Round end
tradeoff-round-scores = Результаты за раунд { $round }:
tradeoff-score-line = { $player }: +{ $round_points } (всего: { $total })
tradeoff-leader = { $player } лидирует со счётом { $score }.

# Game end
tradeoff-winner = { $player } побеждает, набрав { $score } { $score ->
    [one] очко
    [few] очка
   *[other] очков
}!
tradeoff-winners-tie = Ничья! { $players } набрали по { $score } { $score ->
    [one] очку
    [few] очка
   *[other] очков
}!

# Status checks
tradeoff-view-hand = Посмотреть свои кубики
tradeoff-view-pool = Посмотреть пул
tradeoff-view-players = Посмотреть игроков
tradeoff-hand-display = Ваши кубики ({ $count } { $count ->
    [one] кубик
    [few] кубика
   *[other] кубиков
}): { $dice }
tradeoff-pool-display = Пул ({ $count } { $count ->
    [one] кубик
    [few] кубика
   *[other] кубиков
}): { $dice }
tradeoff-player-info = { $player }: { $hand }. Обменял: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. Ничего не менял.

# Error messages
tradeoff-not-trading-phase = Сейчас не фаза обмена.
tradeoff-not-taking-phase = Сейчас не фаза выбора из пула.
tradeoff-already-confirmed = Действие уже подтверждено.
tradeoff-no-die = Нет кубика для переключения.
tradeoff-no-more-takes = Больше нельзя ничего взять.
tradeoff-not-in-pool = Этого кубика нет в пуле.

# Options
tradeoff-set-target = Конечный счёт: { $score }
tradeoff-enter-target = Введите конечный счёт:
tradeoff-option-changed-target = Конечный счёт установлен на { $score }.
