# Messages for Left Right Center (Czech)

# Game name
game-name-leftrightcenter = Vlevo Vpravo Střed

# Actions
lrc-roll = Hodit { $count } { $count ->
    [one] kostkou
    [few] kostkami
    [many] kostkami
   *[other] kostkami
}

# Dice faces
lrc-face-left = Vlevo
lrc-face-right = Vpravo
lrc-face-center = Střed
lrc-face-dot = Tečka

# Game events
lrc-roll-results = { $player } hodil { $results }.
lrc-pass-left = { $player } předává { $count } { $count ->
    [one] žeton
    [few] žetony
    [many] žetonů
   *[other] žetonů
} hráči { $target }.
lrc-pass-right = { $player } předává { $count } { $count ->
    [one] žeton
    [few] žetony
    [many] žetonů
   *[other] žetonů
} hráči { $target }.
lrc-pass-center = { $player } vkládá { $count } { $count ->
    [one] žeton
    [few] žetony
    [many] žetonů
   *[other] žetonů
} do středu.
lrc-no-chips = { $player } nemá žetony na hození.
lrc-center-pot = { $count } { $count ->
    [one] žeton
    [few] žetony
    [many] žetonů
   *[other] žetonů
} ve středu.
lrc-player-chips = { $player } má nyní { $count } { $count ->
    [one] žeton
    [few] žetony
    [many] žetonů
   *[other] žetonů
}.
lrc-winner = { $player } vyhrává s { $count } { $count ->
    [one] žetonem
    [few] žetony
    [many] žetony
   *[other] žetony
}!

# Options
lrc-set-starting-chips = Počáteční žetony: { $count }
lrc-enter-starting-chips = Zadejte počáteční žetony:
lrc-option-changed-starting-chips = Počáteční žetony nastaveny na { $count }.
