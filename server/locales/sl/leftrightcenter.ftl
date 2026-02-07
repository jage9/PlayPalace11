# Messages for Left Right Center (Slovenian)

# Game name
game-name-leftrightcenter = Levo Desno Center

# Actions
lrc-roll = Vrzi { $count } { $count ->
    [one] kocko
   *[other] kock
}

# Dice faces
lrc-face-left = Levo
lrc-face-right = Desno
lrc-face-center = Center
lrc-face-dot = Pika

# Game events
lrc-roll-results = { $player } je vrgel { $results }.
lrc-pass-left = { $player } preda { $count } { $count ->
    [one] žeton
   *[other] žetonov
} igralcu { $target }.
lrc-pass-right = { $player } preda { $count } { $count ->
    [one] žeton
   *[other] žetonov
} igralcu { $target }.
lrc-pass-center = { $player } da { $count } { $count ->
    [one] žeton
   *[other] žetonov
} v center.
lrc-no-chips = { $player } nima žetonov za met.
lrc-center-pot = { $count } { $count ->
    [one] žeton
   *[other] žetonov
} v centru.
lrc-player-chips = { $player } ima zdaj { $count } { $count ->
    [one] žeton
   *[other] žetonov
}.
lrc-winner = { $player } zmaga z { $count } { $count ->
    [one] žetonom
   *[other] žetoni
}!

# Options
lrc-set-starting-chips = Začetni žetoni: { $count }
lrc-enter-starting-chips = Vnesite začetne žetone:
lrc-option-changed-starting-chips = Začetni žetoni nastavljeni na { $count }.
