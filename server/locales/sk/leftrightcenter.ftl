# Messages for Left Right Center (Slovak)

# Game name
game-name-leftrightcenter = Vľavo Vpravo Stred

# Actions
lrc-roll = Hodiť { $count } { $count ->
    [one] kockou
    [few] kockami
    [many] kockami
   *[other] kockami
}

# Dice faces
lrc-face-left = Vľavo
lrc-face-right = Vpravo
lrc-face-center = Stred
lrc-face-dot = Bodka

# Game events
lrc-roll-results = { $player } hodil { $results }.
lrc-pass-left = { $player } predáva { $count } { $count ->
    [one] žetón
    [few] žetóny
    [many] žetónov
   *[other] žetónov
} hráčovi { $target }.
lrc-pass-right = { $player } predáva { $count } { $count ->
    [one] žetón
    [few] žetóny
    [many] žetónov
   *[other] žetónov
} hráčovi { $target }.
lrc-pass-center = { $player } vkladá { $count } { $count ->
    [one] žetón
    [few] žetóny
    [many] žetónov
   *[other] žetónov
} do stredu.
lrc-no-chips = { $player } nemá žetóny na hodenie.
lrc-center-pot = { $count } { $count ->
    [one] žetón
    [few] žetóny
    [many] žetónov
   *[other] žetónov
} v strede.
lrc-player-chips = { $player } má teraz { $count } { $count ->
    [one] žetón
    [few] žetóny
    [many] žetónov
   *[other] žetónov
}.
lrc-winner = { $player } vyhráva s { $count } { $count ->
    [one] žetónom
    [few] žetónmi
    [many] žetónmi
   *[other] žetónmi
}!

# Options
lrc-set-starting-chips = Počiatočné žetóny: { $count }
lrc-enter-starting-chips = Zadajte počiatočné žetóny:
lrc-option-changed-starting-chips = Počiatočné žetóny nastavené na { $count }.
