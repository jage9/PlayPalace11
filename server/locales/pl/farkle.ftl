# Farkle game messages

# Game info
game-name-farkle = Farkle

# Actions - Roll and Bank
farkle-roll = Rzuć { $count } { $count ->
    [one] kostką
   *[other] kostkami
}
farkle-bank = Bankuj { $points } punktów

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = Single 1 for { $points } points
farkle-take-single-five = Single 5 for { $points } points
farkle-take-three-kind = Three { $number }s for { $points } points
farkle-take-four-kind = Four { $number }s for { $points } points
farkle-take-five-kind = Five { $number }s for { $points } points
farkle-take-six-kind = Six { $number }s for { $points } points
farkle-take-small-straight = Small Straight for { $points } points
farkle-take-large-straight = Large Straight for { $points } points
farkle-take-three-pairs = Three pairs for { $points } points
farkle-take-double-triplets = Double triplets for { $points } points
farkle-take-full-house = Full house for { $points } points

# Game events (matching v10 exactly)
farkle-rolls = { $player } rzuca { $count } { $count ->
    [one] kostką
   *[other] kostkami
}...
farkle-you-roll = Rzucasz { $count } { $count ->
    [one] kostką
   *[other] kostkami
}...
farkle-roll-result = { $dice }
farkle-farkle = FARKLE! { $player } traci { $points } punktów
farkle-you-farkle = FARKLE! Tracisz { $points } punktów
farkle-takes-combo = { $player } bierze { $combo }
farkle-you-take-combo = Bierzesz { $combo }
farkle-hot-dice = Gorące kości!
farkle-banks = { $player } bankuje { $points } punktów, łącznie ma { $total }
farkle-you-bank = Bankujesz { $points } punktów, łącznie masz { $total }
farkle-winner = { $player } wygrywa z wynikiem { $score } punktów!
farkle-you-win = Wygrywasz z wynikiem { $score } punktów!
farkle-winners-tie = Mamy remis! Wygrywają: { $players }

# Check turn score action
farkle-turn-score = { $player } ma { $points } punktów w tej turze.
farkle-no-turn = Obecnie nikt nie ma tury.

# Farkle-specific options
farkle-set-target-score = Maksymalna liczba punktów: { $score }
farkle-enter-target-score = Podaj maksymalną liczbę punktów (między 500 a 5000):
farkle-option-changed-target = Maksymalna liczba punktów została ustawiona na { $score }.

# Disabled action reasons
farkle-must-take-combo = Najpierw musisz wybrać punktującą kombinację.
farkle-cannot-bank = Nie możesz teraz zabankować.

# Additional Farkle options
farkle-set-initial-bank-score = Początkowy próg bankowania: { $score }
farkle-enter-initial-bank-score = Wpisz początkowy próg bankowania (między 0 a 1000):
farkle-option-changed-initial-bank-score = Początkowy próg bankowania został ustawiony na { $score }.
farkle-toggle-hot-dice-multiplier = Mnożnik gorących kości: { $enabled }
farkle-option-changed-hot-dice-multiplier = Mnożnik gorących kości został ustawiony na { $enabled }.

# Action feedback
farkle-minimum-initial-bank-score = Minimalny początkowy próg bankowania wynosi { $score }.
