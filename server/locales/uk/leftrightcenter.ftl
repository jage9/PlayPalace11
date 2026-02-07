# Messages for Left Right Center (English)

# Game name
game-name-leftrightcenter = Ліво Право Центр

# Actions
lrc-roll = Кинути { $count } { $count ->
    [one] кубик
   *[other] кубиків
}

# Dice faces
lrc-face-left = Ліво
lrc-face-right = Право
lrc-face-center = Центр
lrc-face-dot = Крапка

# Game events
lrc-roll-results = { $player } кидає { $results }.
lrc-pass-left = { $player } передає { $count } { $count ->
    [one] фішку
   *[other] фішок
} гравцю { $target }.
lrc-pass-right = { $player } передає { $count } { $count ->
    [one] фішку
   *[other] фішок
} гравцю { $target }.
lrc-pass-center = { $player } кладе { $count } { $count ->
    [one] фішку
   *[other] фішок
} в центр.
lrc-no-chips = { $player } немає фішок для кидка.
lrc-center-pot = { $count } { $count ->
    [one] фішка
   *[other] фішок
} в центрі.
lrc-player-chips = { $player } тепер має { $count } { $count ->
    [one] фішку
   *[other] фішок
}.
lrc-winner = { $player } перемагає з { $count } { $count ->
    [one] фішкою
   *[other] фішками
}!

# Options
lrc-set-starting-chips = Початкові фішки: { $count }
lrc-enter-starting-chips = Введіть початкові фішки:
lrc-option-changed-starting-chips = Початкові фішки встановлено на { $count }.
