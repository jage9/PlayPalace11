# Shared game messages for PlayPalace
# These messages are common across multiple games

# Game names
game-name-ninetynine = Девяносто девять

# Round and turn flow
game-round-start = Раунд { $round }.
game-round-end = Раунд { $round } завершён.
game-turn-start = Ход игрока { $player }.
game-no-turn = Сейчас никто не ходит.

# Score display
game-scores-header = Текущий счёт:
game-score-line = { $player }: { $score } { $score ->
    [one] очко
    [few] очка
   *[other] очков
}
game-final-scores-header = Итоговый счёт:

# Win/loss
game-winner = { $player } побеждает!
game-winner-score = { $player } побеждает, набрав { $score } { $score ->
    [one] очко
    [few] очка
   *[other] очков
}!
game-tiebreaker = Ничья! Раунд для определения победителя!
game-tiebreaker-players = Ничья между игроками: { $players }! Раунд для определения победителя!
game-eliminated = Игрок { $player } выбывает из игры с результатом { $score } { $score ->
    [one] очко
    [few] очка
   *[other] очков
}.

# Common options
game-set-target-score = Конечный счёт: { $score }
game-enter-target-score = Введите конечный счёт:
game-option-changed-target = Конечный счёт установлен на { $score }.

game-set-team-mode = Командный режим: { $mode }
game-select-team-mode = Выберите командный режим
game-option-changed-team = Командный режим изменён на: { $mode }.
game-team-mode-individual = Индивидуальный
game-team-mode-x-teams-of-y = { $num_teams } { $num_teams ->
    [one] команда
    [few] команды
   *[other] команд
} по { $team_size } { $team_size ->
    [one] игроку
    [few] игрока
   *[other] игроков
}

# Boolean option values
option-on = вкл.
option-off = выкл.

# Status box
status-box-closed = Информационное окно закрыто.

# Game end
game-leave = Покинуть игру

# Round timer
round-timer-paused = Игрок { $player } поставил игру на паузу (нажмите «p», чтобы начать следующий раунд).
round-timer-resumed = Таймер раунда возобновлён.
round-timer-countdown = Следующий раунд через { $seconds }...

# Dice games - keeping/releasing dice
dice-keeping = Оставляем: { $value }.
dice-rerolling = Перебрасываем: { $value }.
dice-locked = Этот кубик заблокирован, его нельзя изменить.

# Dealing (card games)
game-deal-counter = Раздача { $current }/{ $total }.
game-you-deal = Вы раздаёте карты.
game-player-deals = { $player } раздаёт карты.

# Card names
card-name = { $rank } { $suit }
no-cards = Нет карт

# Suit names (in genitive plural for phrases like "Ace of clubs" -> "Туз треф")
suit-diamonds = бубен
suit-clubs = треф
suit-hearts = червей
suit-spades = пик

# Rank names
rank-ace = Туз
rank-ace-plural = Тузы
rank-two = Двойка
rank-two-plural = Двойки
rank-three = Тройка
rank-three-plural = Тройки
rank-four = Четвёрка
rank-four-plural = Четвёрки
rank-five = Пятёрка
rank-five-plural = Пятёрки
rank-six = Шестёрка
rank-six-plural = Шестёрки
rank-seven = Семёрка
rank-seven-plural = Семёрки
rank-eight = Восьмёрка
rank-eight-plural = Восьмёрки
rank-nine = Девятка
rank-nine-plural = Девятки
rank-ten = Десятка
rank-ten-plural = Десятки
rank-jack = Валет
rank-jack-plural = Валеты
rank-queen = Дама
rank-queen-plural = Дамы
rank-king = Король
rank-king-plural = Короли

# Poker hand descriptions
poker-high-card-with = Старшая карта { $high }, кикер { $rest }
poker-high-card = Старшая карта { $high }
poker-pair-with = Пара { $pair }, кикер { $rest }
poker-pair = Пара { $pair }
poker-two-pair-with = Две пары: { $high } и { $low }, кикер { $kicker }
poker-two-pair = Две пары: { $high } и { $low }
poker-trips-with = Сет: { $trips }, кикер { $rest }
poker-trips = Сет: { $trips }
poker-straight-high = Стрит до { $high }
poker-flush-high-with = Флеш до { $high }, кикер { $rest }
poker-full-house = Фулл-хаус: { $trips } и { $pair }
poker-quads-with = Каре: { $quads }, кикер { $kicker }
poker-quads = Каре: { $quads }
poker-straight-flush-high = Стрит-флеш до { $high }
poker-unknown-hand = Неизвестная комбинация

# Validation errors (common across games)
game-error-invalid-team-mode = Выбранный командный режим недопустим для текущего количества игроков.
