# Messages for Left Right Center (English)

# Game name
game-name-leftrightcenter = Влево, вправо, в центр

# Actions
lrc-roll = Бросить { $count } { $count ->
    [one] кубик
    [few] кубика
   *[other] кубиков
}

# Dice faces
lrc-face-left = Влево
lrc-face-right = Вправо
lrc-face-center = Центр
lrc-face-dot = Точка

# Game events
lrc-roll-results = { $player } выбрасывает: { $results }.
lrc-pass-left = { $player } передаёт { $count } { $count ->
    [one] фишку
    [few] фишки
   *[other] фишек
} игроку { $target }.
lrc-pass-right = { $player } передаёт { $count } { $count ->
    [one] фишку
    [few] фишки
   *[other] фишек
} игроку { $target }.
lrc-pass-center = { $player } кладёт { $count } { $count ->
    [one] фишку
    [few] фишки
   *[other] фишек
} в центр.
lrc-no-chips = У игрока { $player } нет фишек для броска.
lrc-center-pot = В центре { $count } { $count ->
    [one] фишка
    [few] фишки
   *[other] фишек
}.
lrc-player-chips = У игрока { $player } теперь { $count } { $count ->
    [one] фишка
    [few] фишки
   *[other] фишек
}.
lrc-winner = { $player } побеждает, сохранив { $count } { $count ->
    [one] фишку
    [few] фишки
   *[other] фишек
}!

# Options
lrc-set-starting-chips = Стартовые фишки: { $count }
lrc-enter-starting-chips = Введите количество стартовых фишек:
lrc-option-changed-starting-chips = Стартовое количество фишек установлено на { $count }.
