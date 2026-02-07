# Messages for Left Right Center (Hungarian)

# Game name
game-name-leftrightcenter = Bal Jobb Közép

# Actions
lrc-roll = Dobj { $count } { $count ->
    [one] kockával
   *[other] kockával
}

# Dice faces
lrc-face-left = Bal
lrc-face-right = Jobb
lrc-face-center = Közép
lrc-face-dot = Pont

# Game events
lrc-roll-results = { $player } dobott { $results }.
lrc-pass-left = { $player } átad { $count } { $count ->
    [one] zsetont
   *[other] zsetont
} { $target } játékosnak.
lrc-pass-right = { $player } átad { $count } { $count ->
    [one] zsetont
   *[other] zsetont
} { $target } játékosnak.
lrc-pass-center = { $player } { $count } { $count ->
    [one] zsetont
   *[other] zsetont
} tesz a középre.
lrc-no-chips = { $player }-nak/nek nincsenek zsetonjai a dobáshoz.
lrc-center-pot = { $count } { $count ->
    [one] zseton
   *[other] zseton
} a középen.
lrc-player-chips = { $player }-nak/nek most { $count } { $count ->
    [one] zsetonja van
   *[other] zsetonja van
}.
lrc-winner = { $player } győz { $count } { $count ->
    [one] zsetonnal
   *[other] zsetonnal
}!

# Options
lrc-set-starting-chips = Kezdő zsetonok: { $count }
lrc-enter-starting-chips = Add meg a kezdő zsetonokat:
lrc-option-changed-starting-chips = Kezdő zsetonok { $count }-ra állítva.
