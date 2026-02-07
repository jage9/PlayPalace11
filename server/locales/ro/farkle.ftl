# Farkle game messages

# Game info
game-name-farkle = Farkle

# Actions - Roll and Bank
farkle-roll = Aruncă { $count } { $count ->
    [one] zar
    [few] zaruri
   *[other] de zaruri
}
farkle-bank = Depune { $points } puncte

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = Un singur 1 pentru { $points } puncte
farkle-take-single-five = Un singur 5 pentru { $points } puncte
farkle-take-three-kind = Trei { $number } pentru { $points } puncte
farkle-take-four-kind = Patru { $number } pentru { $points } puncte
farkle-take-five-kind = Cinci { $number } pentru { $points } puncte
farkle-take-six-kind = Șase { $number } pentru { $points } puncte
farkle-take-small-straight = Scară mică pentru { $points } puncte
farkle-take-large-straight = Scară mare pentru { $points } puncte
farkle-take-three-pairs = Trei perechi pentru { $points } puncte
farkle-take-double-triplets = Triplete duble pentru { $points } puncte
farkle-take-full-house = Full house pentru { $points } puncte

# Game events (matching v10 exactly)
farkle-rolls = { $player } aruncă { $count } { $count ->
    [one] zar
    [few] zaruri
   *[other] de zaruri
}...
farkle-you-roll = Arunci { $count } { $count ->
    [one] zar
    [few] zaruri
   *[other] de zaruri
}...
farkle-roll-result = { $dice }
farkle-farkle = FARKLE! { $player } pierde { $points } puncte
farkle-you-farkle = FARKLE! Pierzi { $points } puncte
farkle-takes-combo = { $player } ia { $combo } pentru { $points } puncte
farkle-you-take-combo = Iei { $combo } pentru { $points } puncte
farkle-hot-dice = Zaruri fierbinți!
farkle-banks = { $player } depune { $points } puncte pentru un total de { $total }
farkle-you-bank = Depui { $points } puncte pentru un total de { $total }
farkle-winner = { $player } câștigă cu { $score } puncte!
farkle-you-win = Câștigi cu { $score } puncte!
farkle-winners-tie = Avem egalitate! Câștigători: { $players }

# Check turn score action
farkle-turn-score = { $player } are { $points } puncte în această tură.
farkle-no-turn = Nimeni nu este la tură în prezent.

# Farkle-specific options
farkle-set-target-score = Scor țintă: { $score }
farkle-enter-target-score = Introduceți scorul țintă (500-5000):
farkle-option-changed-target = Scor țintă setat la { $score }.

# Disabled action reasons
farkle-must-take-combo = Trebuie să iei mai întâi o combinație de punctaj.
farkle-cannot-bank = Nu poți depune acum.
