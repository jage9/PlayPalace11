# Farkle game messages

# Game info
game-name-farkle = Farkle

# Actions - Roll and Bank
farkle-roll = Baci { $count } { $count ->
    [one] kockicu
   *[other] kockica
}
farkle-bank = Spremi { $points } bodova

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = Jedan 1 za { $points } bodova
farkle-take-single-five = Jedan 5 za { $points } bodova
farkle-take-three-kind = Tri { $number } za { $points } bodova
farkle-take-four-kind = Četiri { $number } za { $points } bodova
farkle-take-five-kind = Pet { $number } za { $points } bodova
farkle-take-six-kind = Šest { $number } za { $points } bodova
farkle-take-small-straight = Mali niz za { $points } bodova
farkle-take-large-straight = Veliki niz za { $points } bodova
farkle-take-three-pairs = Tri para za { $points } bodova
farkle-take-double-triplets = Dupli trojci za { $points } bodova
farkle-take-full-house = Puna kuća za { $points } bodova

# Game events (matching v10 exactly)
farkle-rolls = { $player } baca { $count } { $count ->
    [one] kockicu
   *[other] kockica
}...
farkle-you-roll = Bacate { $count } { $count ->
    [one] kockicu
   *[other] kockica
}...
farkle-roll-result = { $dice }
farkle-farkle = FARKLE! { $player } gubi { $points } bodova
farkle-you-farkle = FARKLE! Gubite { $points } bodova
farkle-takes-combo = { $player } uzima { $combo } za { $points } bodova
farkle-you-take-combo = Uzimate { $combo } za { $points } bodova
farkle-hot-dice = Vruće kockice!
farkle-banks = { $player } sprema { $points } bodova za ukupno { $total }
farkle-you-bank = Spremate { $points } bodova za ukupno { $total }
farkle-winner = { $player } pobjeđuje s { $score } bodova!
farkle-you-win = Pobjeđujete s { $score } bodova!
farkle-winners-tie = Imamo neriješeno! Pobjednici: { $players }

# Check turn score action
farkle-turn-score = { $player } ima { $points } bodova ovog poteza.
farkle-no-turn = Nitko trenutno nije na potezu.

# Farkle-specific options
farkle-set-target-score = Ciljani rezultat: { $score }
farkle-enter-target-score = Unesite ciljani rezultat (500-5000):
farkle-option-changed-target = Ciljani rezultat postavljen na { $score }.

# Disabled action reasons
farkle-must-take-combo = Morate prvo uzeti kombinaciju za bodovanje.
farkle-cannot-bank = Trenutno ne možete spremiti.

# Additional Farkle options
farkle-set-initial-bank-score = Početni bankovni rezultat: { $score }
farkle-enter-initial-bank-score = Unesite početni bankovni rezultat (0-1000):
farkle-option-changed-initial-bank-score = Početni bankovni rezultat postavljen na { $score }.
farkle-toggle-hot-dice-multiplier = Množitelj hot dice: { $enabled }
farkle-option-changed-hot-dice-multiplier = Množitelj hot dice postavljen na { $enabled }.

# Action feedback
farkle-minimum-initial-bank-score = Minimalni početni bankovni rezultat je { $score }.
