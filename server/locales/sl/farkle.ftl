# Farkle game messages

# Game info
game-name-farkle = Farkle

# Actions - Roll and Bank
farkle-roll = Vrzi { $count } { $count ->
    [one] kocko
   *[other] kock
}
farkle-bank = Shrani { $points } točk

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = Ena 1 za { $points } točk
farkle-take-single-five = Ena 5 za { $points } točk
farkle-take-three-kind = Tri { $number } za { $points } točk
farkle-take-four-kind = Štiri { $number } za { $points } točk
farkle-take-five-kind = Pet { $number } za { $points } točk
farkle-take-six-kind = Šest { $number } za { $points } točk
farkle-take-small-straight = Majhna lestvica za { $points } točk
farkle-take-large-straight = Velika lestvica za { $points } točk
farkle-take-three-pairs = Trije pari za { $points } točk
farkle-take-double-triplets = Dvojni trojčki za { $points } točk
farkle-take-full-house = Polna hiša za { $points } točk

# Game events (matching v10 exactly)
farkle-rolls = { $player } vrže { $count } { $count ->
    [one] kocko
   *[other] kock
}...
farkle-you-roll = Vržeš { $count } { $count ->
    [one] kocko
   *[other] kock
}...
farkle-roll-result = { $dice }
farkle-farkle = FARKLE! { $player } izgubi { $points } točk
farkle-you-farkle = FARKLE! Izgubiš { $points } točk
farkle-takes-combo = { $player } vzame { $combo } za { $points } točk
farkle-you-take-combo = Vzameš { $combo } za { $points } točk
farkle-hot-dice = Vroče kocke!
farkle-banks = { $player } shrani { $points } točk za skupno { $total }
farkle-you-bank = Shraniš { $points } točk za skupno { $total }
farkle-winner = { $player } zmaga s { $score } točkami!
farkle-you-win = Zmagaš s { $score } točkami!
farkle-winners-tie = Imamo neodločeno! Zmagovalci: { $players }

# Check turn score action
farkle-turn-score = { $player } ima { $points } točk v tej potezi.
farkle-no-turn = Trenutno nihče ni na potezi.

# Farkle-specific options
farkle-set-target-score = Cilj rezultat: { $score }
farkle-enter-target-score = Vnesite ciljni rezultat (500-5000):
farkle-option-changed-target = Ciljni rezultat nastavljen na { $score }.

# Disabled action reasons
farkle-must-take-combo = Najprej moraš vzeti kombinacijo za točkovanje.
farkle-cannot-bank = Zdaj ne moreš shraniti.

# Additional Farkle options
farkle-set-initial-bank-score = Začetni bančni rezultat: { $score }
farkle-enter-initial-bank-score = Vnesite začetni bančni rezultat (0-1000):
farkle-option-changed-initial-bank-score = Začetni bančni rezultat nastavljen na { $score }.
farkle-toggle-hot-dice-multiplier = Množilnik hot dice: { $enabled }
farkle-option-changed-hot-dice-multiplier = Množilnik hot dice nastavljen na { $enabled }.

# Action feedback
farkle-minimum-initial-bank-score = Najmanjši začetni bančni rezultat je { $score }.
