# Messages for Left Right Center (isiZulu)

# Game name
game-name-leftrightcenter = Left Right Center

# Actions
lrc-roll = Phonsa { $count } { $count ->
    [one] idayisi
   *[other] amadayisi
}

# Dice faces
lrc-face-left = Kwesokunxele
lrc-face-right = Kwesokudla
lrc-face-center = Maphakathi
lrc-face-dot = Ichashazi

# Game events
lrc-roll-results = U-{ $player } uphonsa { $results }.
lrc-pass-left = U-{ $player } udlulisa { $count } { $count ->
    [one] i-chip
   *[other] ama-chips
} ku-{ $target }.
lrc-pass-right = U-{ $player } udlulisa { $count } { $count ->
    [one] i-chip
   *[other] ama-chips
} ku-{ $target }.
lrc-pass-center = U-{ $player } ubeka { $count } { $count ->
    [one] i-chip
   *[other] ama-chips
} maphakathi.
lrc-no-chips = U-{ $player } awanayo ama-chips okuphonsa.
lrc-center-pot = { $count } { $count ->
    [one] i-chip
   *[other] ama-chips
} maphakathi.
lrc-player-chips = U-{ $player } manje unama-chips angu-{ $count } { $count ->
    [one] i-chip
   *[other] ama-chips
}.
lrc-winner = U-{ $player } uyawina ngama-chips angu-{ $count } { $count ->
    [one] i-chip
   *[other] ama-chips
}!

# Options
lrc-set-starting-chips = Ama-chips okuqala: { $count }
lrc-enter-starting-chips = Faka ama-chips okuqala:
lrc-option-changed-starting-chips = Ama-chips okuqala asetelwe ku-{ $count }.
