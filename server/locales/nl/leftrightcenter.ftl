# Messages for Left Right Center (Dutch)

# Game name
game-name-leftrightcenter = Left Right Center

# Actions
lrc-roll = Gooi { $count } { $count ->
    [one] dobbelsteen
   *[other] dobbelstenen
}

# Dice faces
lrc-face-left = Links
lrc-face-right = Rechts
lrc-face-center = Midden
lrc-face-dot = Stip

# Game events
lrc-roll-results = { $player } gooit { $results }.
lrc-pass-left = { $player } geeft { $count } { $count ->
    [one] fiche
   *[other] fiches
} naar { $target }.
lrc-pass-right = { $player } geeft { $count } { $count ->
    [one] fiche
   *[other] fiches
} naar { $target }.
lrc-pass-center = { $player } legt { $count } { $count ->
    [one] fiche
   *[other] fiches
} in het midden.
lrc-no-chips = { $player } heeft geen fiches om te gooien.
lrc-center-pot = { $count } { $count ->
    [one] fiche
   *[other] fiches
} in het midden.
lrc-player-chips = { $player } heeft nu { $count } { $count ->
    [one] fiche
   *[other] fiches
}.
lrc-winner = { $player } wint met { $count } { $count ->
    [one] fiche
   *[other] fiches
}!

# Options
lrc-set-starting-chips = Startfiches: { $count }
lrc-enter-starting-chips = Voer startfiches in:
lrc-option-changed-starting-chips = Startfiches ingesteld op { $count }.
