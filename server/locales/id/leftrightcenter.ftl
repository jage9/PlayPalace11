# Messages for Left Right Center (English)

# Game name
game-name-leftrightcenter = Left Right Center

# Actions
lrc-roll = Lempar { $count } { $count ->
    [one] dadu
   *[other] dadu
}

# Dice faces
lrc-face-left = Kiri
lrc-face-right = Kanan
lrc-face-center = Tengah
lrc-face-dot = Titik

# Game events
lrc-roll-results = { $player } melempar { $results }.
lrc-pass-left = { $player } memberikan { $count } { $count ->
    [one] chip
   *[other] chip
} ke { $target }.
lrc-pass-right = { $player } memberikan { $count } { $count ->
    [one] chip
   *[other] chip
} ke { $target }.
lrc-pass-center = { $player } menaruh { $count } { $count ->
    [one] chip
   *[other] chip
} di tengah.
lrc-no-chips = { $player } tidak memiliki chip untuk dilempar.
lrc-center-pot = { $count } { $count ->
    [one] chip
   *[other] chip
} di tengah.
lrc-player-chips = { $player } sekarang memiliki { $count } { $count ->
    [one] chip
   *[other] chip
}.
lrc-winner = { $player } menang dengan { $count } { $count ->
    [one] chip
   *[other] chip
}!

# Options
lrc-set-starting-chips = Chip awal: { $count }
lrc-enter-starting-chips = Masukkan chip awal:
lrc-option-changed-starting-chips = Chip awal diatur ke { $count }.
