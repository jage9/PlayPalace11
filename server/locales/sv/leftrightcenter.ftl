# Messages for Left Right Center (Swedish)

# Game name
game-name-leftrightcenter = Vänster Höger Mitten

# Actions
lrc-roll = Kasta { $count } { $count ->
    [one] tärning
   *[other] tärningar
}

# Dice faces
lrc-face-left = Vänster
lrc-face-right = Höger
lrc-face-center = Mitten
lrc-face-dot = Prick

# Game events
lrc-roll-results = { $player } kastade { $results }.
lrc-pass-left = { $player } ger { $count } { $count ->
    [one] mark
   *[other] marker
} till { $target }.
lrc-pass-right = { $player } ger { $count } { $count ->
    [one] mark
   *[other] marker
} till { $target }.
lrc-pass-center = { $player } lägger { $count } { $count ->
    [one] mark
   *[other] marker
} i mitten.
lrc-no-chips = { $player } har inga marker att kasta.
lrc-center-pot = { $count } { $count ->
    [one] mark
   *[other] marker
} i mitten.
lrc-player-chips = { $player } har nu { $count } { $count ->
    [one] mark
   *[other] marker
}.
lrc-winner = { $player } vinner med { $count } { $count ->
    [one] mark
   *[other] marker
}!

# Options
lrc-set-starting-chips = Startmarker: { $count }
lrc-enter-starting-chips = Ange startmarker:
lrc-option-changed-starting-chips = Startmarker inställda på { $count }.
