# Messages for Left Right Center (Romanian)

# Game name
game-name-leftrightcenter = Stânga Dreapta Centru

# Actions
lrc-roll = Aruncă { $count } { $count ->
    [one] zar
    [few] zaruri
   *[other] de zaruri
}

# Dice faces
lrc-face-left = Stânga
lrc-face-right = Dreapta
lrc-face-center = Centru
lrc-face-dot = Punct

# Game events
lrc-roll-results = { $player } a aruncat { $results }.
lrc-pass-left = { $player } trece { $count } { $count ->
    [one] jeton
    [few] jetoane
   *[other] de jetoane
} lui { $target }.
lrc-pass-right = { $player } trece { $count } { $count ->
    [one] jeton
    [few] jetoane
   *[other] de jetoane
} lui { $target }.
lrc-pass-center = { $player } pune { $count } { $count ->
    [one] jeton
    [few] jetoane
   *[other] de jetoane
} în centru.
lrc-no-chips = { $player } nu are jetoane de aruncat.
lrc-center-pot = { $count } { $count ->
    [one] jeton
    [few] jetoane
   *[other] de jetoane
} în centru.
lrc-player-chips = { $player } are acum { $count } { $count ->
    [one] jeton
    [few] jetoane
   *[other] de jetoane
}.
lrc-winner = { $player } câștigă cu { $count } { $count ->
    [one] jeton
    [few] jetoane
   *[other] de jetoane
}!

# Options
lrc-set-starting-chips = Jetoane inițiale: { $count }
lrc-enter-starting-chips = Introduceți jetoanele inițiale:
lrc-option-changed-starting-chips = Jetoane inițiale setate la { $count }.
