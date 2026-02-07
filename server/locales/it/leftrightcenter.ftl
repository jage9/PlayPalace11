# Messages for Left Right Center (Italian)

# Game name
game-name-leftrightcenter = Sinistra Destra Centro

# Actions
lrc-roll = Tira { $count } { $count ->
    [one] dado
   *[other] dadi
}

# Dice faces
lrc-face-left = Sinistra
lrc-face-right = Destra
lrc-face-center = Centro
lrc-face-dot = Punto

# Game events
lrc-roll-results = { $player } ha tirato { $results }.
lrc-pass-left = { $player } passa { $count } { $count ->
    [one] fiche
   *[other] fiches
} a { $target }.
lrc-pass-right = { $player } passa { $count } { $count ->
    [one] fiche
   *[other] fiches
} a { $target }.
lrc-pass-center = { $player } mette { $count } { $count ->
    [one] fiche
   *[other] fiches
} al centro.
lrc-no-chips = { $player } non ha fiches da tirare.
lrc-center-pot = { $count } { $count ->
    [one] fiche
   *[other] fiches
} al centro.
lrc-player-chips = { $player } ora ha { $count } { $count ->
    [one] fiche
   *[other] fiches
}.
lrc-winner = { $player } vince con { $count } { $count ->
    [one] fiche
   *[other] fiches
}!

# Options
lrc-set-starting-chips = Fiches iniziali: { $count }
lrc-enter-starting-chips = Inserisci fiches iniziali:
lrc-option-changed-starting-chips = Fiches iniziali impostate a { $count }.
