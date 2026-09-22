# Farkle game messages

# Game info
game-name-farkle = Farkl

# Actions - Roll and Bank
farkle-roll = Baci { $count } { $count ->
    [one] kockicu
    [few] kockice
   *[other] kockica
}
farkle-bank = Sačuvaj { $points } poena

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = Jedna jedinica za { $points } poena
farkle-take-single-five = Jedna petica za { $points } poena
farkle-take-three-kind = Tri puta { $number } za { $points } poena
farkle-take-four-kind = Četiri puta { $number } za { $points } poena
farkle-take-five-kind = Pet puta { $number } za { $points } poena
farkle-take-six-kind = Šest puta { $number } za { $points } poena
farkle-take-small-straight = Mala kenta za { $points } poena
farkle-take-large-straight = Velika kenta za { $points } poena
farkle-take-three-pairs = Tri para za { $points } poena
farkle-take-double-triplets = Dupli triplet za { $points } poena
farkle-take-full-house = Ful haus za { $points } poena

# Game events (matching v10 exactly)
farkle-rolls = { $player } baca { $count } { $count ->
    [one] kockicu
    [few] kockice
   *[other] kockica
}...
farkle-you-roll = Bacate { $count } { $count ->
    [one] kockicu
    [few] kockice
   *[other] kockica
}...
farkle-roll-result = { $dice }
farkle-farkle = Farkl! { $player } gubi { $points } poena
farkle-you-farkle = Farkl! Gubite { $points } poena
farkle-takes-combo = { $player } uzima { $combo }
farkle-you-take-combo = Uzimate { $combo }
farkle-hot-dice = Vruće kockice!
farkle-banks = { $player } čuva { $points } poena što je ukupno { $total }
farkle-you-bank = Čuvate { $points } poena što je ukupno { $total }
farkle-winner = { $player } pobeđuje sa { $score } poena!
farkle-you-win = Pobeđujete sa { $score } poena!
farkle-winners-tie = Izjednačeno! Pobednici: { $players }

# Check turn score action
farkle-turn-score = { $player } ima { $points } poena u ovom potezu.
farkle-no-turn = Niko trenutno nije na potezu.

# Farkle-specific options
farkle-set-target-score = Krajnji rezultat: { $score }
farkle-enter-target-score = Upišite krajnji rezultat (500-5000):
farkle-option-changed-target = Krajnji rezultat podešen na { $score }.

# Disabled action reasons
farkle-must-take-combo = Prvo morate da uzmete neku kombinaciju.
farkle-cannot-bank = Ne možete sada da sačuvate.

# Additional Farkle options
farkle-set-initial-bank-score = Rezultat za prvo čuvanje: { $score }
farkle-enter-initial-bank-score = Upišite rezultat neophodan za prvo čuvanje (0-1000):
farkle-option-changed-initial-bank-score = Rezultat za prvo čuvanje podešen na { $score }.
farkle-toggle-hot-dice-multiplier = Množilac vrućih kockica: { $enabled }
farkle-option-changed-hot-dice-multiplier = Množilac za vruće kockice { $enabled }.

# Action feedback
farkle-minimum-initial-bank-score = Najmanji rezultat za prvo čuvanje { $score }.
