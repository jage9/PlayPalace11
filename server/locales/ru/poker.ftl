# Shared Poker Messages

poker-fold = Пас
poker-call = Колл
poker-check = Чек
poker-raise = Рейз
poker-all-in = Ва-банк
poker-enter-raise = Введите сумму рейза

poker-check-pot = Проверить банк
poker-check-bet = Сумма для колла
poker-check-min-raise = Минимальный рейз
poker-check-log = Журнал действий
poker-check-hand-players = Игроки в раздаче
poker-check-turn-timer = Таймер хода
poker-check-blind-timer = Таймер блайндов
poker-check-button = У кого баттон
poker-check-dealer = Кто дилер
poker-check-position = Ваша позиция

poker-read-hand = Посмотреть руку
poker-read-table = Посмотреть карты на столе
poker-hand-value = Комбинация
poker-read-card = Посмотреть карту №{ $index }
poker-dealt-cards = Вам сдали: { $cards }.
poker-flop = Флоп: { $cards }.
poker-turn = Тёрн: { $card }.
poker-river = Ривер: { $card }.

poker-pot-total = В банке { $amount } { $amount ->
    [one] фишка
    [few] фишки
   *[other] фишек
}.
poker-pot-main = Основной банк: { $amount } { $amount ->
    [one] фишка
    [few] фишки
   *[other] фишек
}.
poker-pot-side = Побочный банк { $index }: { $amount } { $amount ->
    [one] фишка
    [few] фишки
   *[other] фишек
}.
poker-to-call = Вам нужно { $amount } { $amount ->
    [one] фишка
    [few] фишки
   *[other] фишек
}, чтобы уравнять (колл).
poker-min-raise = Минимальный рейз: { $amount } { $amount ->
    [one] фишка
    [few] фишки
   *[other] фишек
}.

poker-player-folds = { $player } пасует.
poker-player-checks = { $player } говорит «чек».
poker-player-calls = { $player } коллирует { $amount } { $amount ->
    [one] фишку
    [few] фишки
   *[other] фишек
}.
poker-player-raises = { $player } делает рейз до { $amount } { $amount ->
    [one] фишки
    [few] фишки
   *[other] фишек
}.
poker-player-all-in = { $player } идёт ва-банк на { $amount } { $amount ->
    [one] фишку
    [few] фишки
   *[other] фишек
}.

poker-player-wins-pot = { $player } выигрывает банк: { $amount } { $amount ->
    [one] фишка
    [few] фишки
   *[other] фишек
}.
poker-player-wins-pot-hand = { $player } выигрывает { $amount } { $amount ->
    [one] фишку
    [few] фишки
   *[other] фишек
} (карты: { $cards }, комбинация: { $hand }).
poker-player-wins-side-pot-hand = { $player } выигрывает побочный банк { $index } ({ $amount } { $amount ->
    [one] фишка
    [few] фишки
   *[other] фишек
}), карты: { $cards }, комбинация: { $hand }.
poker-players-split-pot = { $players } делят банк ({ $amount } { $amount ->
    [one] фишка
    [few] фишки
   *[other] фишек
}), имея { $hand }.
poker-players-split-side-pot = { $players } делят побочный банк { $index } ({ $amount } { $amount ->
    [one] фишка
    [few] фишки
   *[other] фишек
}), имея { $hand }.
poker-player-wins-game = { $player } побеждает в игре.

poker-showdown = Вскрытие.

poker-timer-disabled = Таймер хода отключён.
poker-timer-remaining = Осталось { $seconds } { $seconds ->
    [one] секунда
    [few] секунды
   *[other] секунд
}.
poker-blind-timer-disabled = Таймер блайндов отключён.
poker-blind-timer-remaining = До повышения блайндов осталось { $seconds } { $seconds ->
    [one] секунда
    [few] секунды
   *[other] секунд
}.
poker-blind-timer-remaining-ms = До повышения блайндов осталось { $minutes } { $minutes ->
    [one] минута
    [few] минуты
   *[other] минут
} и { $seconds } { $seconds ->
    [one] секунда
    [few] секунды
   *[other] секунд
}.
poker-blinds-raise-next-hand = Блайнды повысятся в следующей раздаче.

poker-button-is = Баттон у игрока { $player }.
poker-dealer-is = Дилер: { $player }.
poker-position-seat = Вы на { $position }-м месте после баттона.
poker-position-seats = Вы на { $position }-м месте после баттона.
poker-position-button = Вы на баттоне.
poker-position-dealer = Вы дилер.
poker-position-dealer-seat = Вы на { $position }-м месте после дилера.
poker-position-dealer-seats = Вы на { $position }-м месте после дилера.
poker-show-hand = { $player } показывает карты { $cards } (комбинация: { $hand }).
poker-blinds-players = Малый блайнд: { $sb }. Большой блайнд: { $bb }.
poker-reveal-only-showdown = Открыть карты можно только в конце раздачи (на вскрытии).

poker-reveal-both = Открыть обе карманные карты
poker-reveal-first = Открыть первую карманную карту
poker-reveal-second = Открыть вторую карманную карту

poker-raise-cap-reached = В этом раунде достигнут лимит повышений (рейзов).
poker-raise-too-small = Минимальный рейз: { $amount } { $amount ->
    [one] фишка
    [few] фишки
   *[other] фишек
}.
poker-hand-players-none = В раздаче нет игроков.
poker-hand-players-one = { $count } игрок: { $names }.
poker-hand-players = { $count } { $count ->
    [one] игрок
    [few] игрока
   *[other] игроков
}: { $names }.
poker-raise-too-large = Вы не можете поставить больше фишек, чем у вас есть.

poker-log-empty = Действий пока не было.
poker-log-fold = { $player } — пас
poker-log-check = { $player } — чек
poker-log-call = { $player } — колл { $amount }
poker-log-raise = { $player } — рейз { $amount }
poker-log-all-in = { $player } — ва-банк { $amount }

poker-table-cards = Карты на столе: { $cards }.
poker-your-hand = Ваши карты: { $cards }.

# Timer choice labels
poker-timer-5 = 5 секунд
poker-timer-10 = 10 секунд
poker-timer-15 = 15 секунд
poker-timer-20 = 20 секунд
poker-timer-30 = 30 секунд
poker-timer-45 = 45 секунд
poker-timer-60 = 60 секунд
poker-timer-90 = 90 секунд
poker-timer-unlimited = Без ограничений

poker-blind-timer-unlimited = Без ограничений
poker-blind-timer-5 = 5 минут
poker-blind-timer-10 = 10 минут
poker-blind-timer-15 = 15 минут
poker-blind-timer-20 = 20 минут
poker-blind-timer-30 = 30 минут

poker-raise-no-limit = Без лимита
poker-raise-pot-limit = Пот-лимит
poker-raise-double-pot = Двойной пот-лимит
