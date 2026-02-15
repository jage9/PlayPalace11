# 1-4-24 (Midnight) game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-midnight = 1-4-24
midnight-category = Игры в кости

# Actions
midnight-roll = Бросить кубики
midnight-keep-die = Оставить { $value }
midnight-bank = Банковать

# Game events
midnight-turn-start = Ход игрока { $player }.
midnight-you-rolled = Вы выбросили: { $dice }.
midnight-player-rolled = { $player } выбрасывает: { $dice }.

# Keeping dice
midnight-you-keep = Вы оставляете { $die }.
midnight-player-keeps = { $player } оставляет { $die }.
midnight-you-unkeep = Вы отменяете выбор { $die }.
midnight-player-unkeeps = { $player } отменяет выбор { $die }.

# Turn status
midnight-you-have-kept = Оставленные кубики: { $kept }. Осталось бросков: { $remaining }.
midnight-player-has-kept = { $player } оставил: { $kept }. Осталось кубиков: { $remaining }.

# Scoring
midnight-you-scored = Вы набрали { $score } { $score ->
    [one] очко
    [few] очка
   *[other] очков
}.
midnight-scored = { $player } набирает { $score } { $score ->
    [one] очко
    [few] очка
   *[other] очков
}.
midnight-you-disqualified = У вас нет единицы и четвёрки одновременно. Вы дисквалифицированы!
midnight-player-disqualified = У игрока { $player } нет единицы и четвёрки. Он дисквалифицирован!

# Round results
midnight-round-winner = { $player } побеждает в раунде!
midnight-round-tie = В раунде ничья между игроками: { $players }.
midnight-all-disqualified = Все игроки дисквалифицированы! В этом раунде нет победителя.

# Game winner
midnight-game-winner = { $player } побеждает в игре с результатом { $wins } { $wins ->
    [one] победа
    [few] победы
   *[other] побед
} в раундах!
midnight-game-tie = Ничья! { $players } одержали по { $wins } { $wins ->
    [one] победе
    [few] победы
   *[other] побед
}.

# Options
midnight-set-rounds = Количество раундов: { $rounds }
midnight-enter-rounds = Введите количество раундов:
midnight-option-changed-rounds = Количество раундов изменено на { $rounds }.

# Disabled reasons
midnight-need-to-roll = Сначала нужно бросить кубики.
midnight-no-dice-to-keep = Нет доступных кубиков, чтобы их оставить.
midnight-must-keep-one = Вы должны оставлять как минимум один кубик за бросок.
midnight-must-roll-first = Сначала нужно бросить кубики.
midnight-keep-all-first = Нужно выбрать все кубики перед тем, как зафиксировать счёт.
