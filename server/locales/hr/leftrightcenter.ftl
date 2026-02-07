# Messages for Left Right Center (Croatian)

# Game name
game-name-leftrightcenter = Lijevo Desno Centar

# Actions
lrc-roll = Baci { $count } { $count ->
    [one] kockicu
   *[other] kockice
}

# Dice faces
lrc-face-left = Lijevo
lrc-face-right = Desno
lrc-face-center = Centar
lrc-face-dot = Točka

# Game events
lrc-roll-results = { $player } je bacio { $results }.
lrc-pass-left = { $player } predaje { $count } { $count ->
    [one] žeton
   *[other] žetona
} igraču { $target }.
lrc-pass-right = { $player } predaje { $count } { $count ->
    [one] žeton
   *[other] žetona
} igraču { $target }.
lrc-pass-center = { $player } stavlja { $count } { $count ->
    [one] žeton
   *[other] žetona
} u centar.
lrc-no-chips = { $player } nema žetona za bacanje.
lrc-center-pot = { $count } { $count ->
    [one] žeton
   *[other] žetona
} u centru.
lrc-player-chips = { $player } sada ima { $count } { $count ->
    [one] žeton
   *[other] žetona
}.
lrc-winner = { $player } pobjeđuje s { $count } { $count ->
    [one] žetonom
   *[other] žetona
}!

# Options
lrc-set-starting-chips = Početni žetoni: { $count }
lrc-enter-starting-chips = Unesite početne žetone:
lrc-option-changed-starting-chips = Početni žetoni postavljeni na { $count }.
