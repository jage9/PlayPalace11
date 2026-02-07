# Farkle game messages

# Game info
game-name-farkle = Farkle

# Actions - Roll and Bank
farkle-roll = Gooi { $count } { $count ->
    [one] dobbelsteen
   *[other] dobbelstenen
}
farkle-bank = Bank { $points } punten

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = Enkele 1 voor { $points } punten
farkle-take-single-five = Enkele 5 voor { $points } punten
farkle-take-three-kind = Drie { $number }en voor { $points } punten
farkle-take-four-kind = Vier { $number }en voor { $points } punten
farkle-take-five-kind = Vijf { $number }en voor { $points } punten
farkle-take-six-kind = Zes { $number }en voor { $points } punten
farkle-take-small-straight = Kleine straat voor { $points } punten
farkle-take-large-straight = Grote straat voor { $points } punten
farkle-take-three-pairs = Drie paren voor { $points } punten
farkle-take-double-triplets = Dubbele triplets voor { $points } punten
farkle-take-full-house = Full house voor { $points } punten

# Game events (matching v10 exactly)
farkle-rolls = { $player } gooit { $count } { $count ->
    [one] dobbelsteen
   *[other] dobbelstenen
}...
farkle-you-roll = Je gooit { $count } { $count ->
    [one] dobbelsteen
   *[other] dobbelstenen
}...
farkle-roll-result = { $dice }
farkle-farkle = FARKLE! { $player } verliest { $points } punten
farkle-you-farkle = FARKLE! Je verliest { $points } punten
farkle-takes-combo = { $player } pakt { $combo } voor { $points } punten
farkle-you-take-combo = Je pakt { $combo } voor { $points } punten
farkle-hot-dice = Hete dobbelstenen!
farkle-banks = { $player } bankt { $points } punten voor een totaal van { $total }
farkle-you-bank = Je bankt { $points } punten voor een totaal van { $total }
farkle-winner = { $player } wint met { $score } punten!
farkle-you-win = Je wint met { $score } punten!
farkle-winners-tie = We hebben een gelijkspel! Winnaars: { $players }

# Check turn score action
farkle-turn-score = { $player } heeft { $points } punten deze beurt.
farkle-no-turn = Niemand is momenteel aan de beurt.

# Farkle-specific options
farkle-set-target-score = Doelscore: { $score }
farkle-enter-target-score = Voer doelscore in (500-5000):
farkle-option-changed-target = Doelscore ingesteld op { $score }.

# Disabled action reasons
farkle-must-take-combo = Je moet eerst een scorende combinatie pakken.
farkle-cannot-bank = Je kunt nu niet banken.
