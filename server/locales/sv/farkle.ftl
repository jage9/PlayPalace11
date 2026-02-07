# Farkle game messages

# Game info
game-name-farkle = Farkle

# Actions - Roll and Bank
farkle-roll = Kasta { $count } { $count ->
    [one] tärning
   *[other] tärningar
}
farkle-bank = Spara { $points } poäng

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = Singel 1:a för { $points } poäng
farkle-take-single-five = Singel 5:a för { $points } poäng
farkle-take-three-kind = Tre { $number }or för { $points } poäng
farkle-take-four-kind = Fyra { $number }or för { $points } poäng
farkle-take-five-kind = Fem { $number }or för { $points } poäng
farkle-take-six-kind = Sex { $number }or för { $points } poäng
farkle-take-small-straight = Liten stege för { $points } poäng
farkle-take-large-straight = Stor stege för { $points } poäng
farkle-take-three-pairs = Tre par för { $points } poäng
farkle-take-double-triplets = Dubbla tretal för { $points } poäng
farkle-take-full-house = Kåk för { $points } poäng

# Game events (matching v10 exactly)
farkle-rolls = { $player } kastar { $count } { $count ->
    [one] tärning
   *[other] tärningar
}...
farkle-you-roll = Du kastar { $count } { $count ->
    [one] tärning
   *[other] tärningar
}...
farkle-roll-result = { $dice }
farkle-farkle = FARKLE! { $player } förlorar { $points } poäng
farkle-you-farkle = FARKLE! Du förlorar { $points } poäng
farkle-takes-combo = { $player } tar { $combo } för { $points } poäng
farkle-you-take-combo = Du tar { $combo } för { $points } poäng
farkle-hot-dice = Heta tärningar!
farkle-banks = { $player } sparar { $points } poäng för totalt { $total }
farkle-you-bank = Du sparar { $points } poäng för totalt { $total }
farkle-winner = { $player } vinner med { $score } poäng!
farkle-you-win = Du vinner med { $score } poäng!
farkle-winners-tie = Vi har oavgjort! Vinnare: { $players }

# Check turn score action
farkle-turn-score = { $player } har { $points } poäng detta drag.
farkle-no-turn = Ingen gör just nu ett drag.

# Farkle-specific options
farkle-set-target-score = Målpoäng: { $score }
farkle-enter-target-score = Ange målpoäng (500-5000):
farkle-option-changed-target = Målpoäng inställt på { $score }.

# Disabled action reasons
farkle-must-take-combo = Du måste först ta en poänggivande kombination.
farkle-cannot-bank = Du kan inte spara just nu.
