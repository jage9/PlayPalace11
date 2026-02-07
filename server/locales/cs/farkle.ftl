# Farkle - České zprávy hry

# Informace o hře
game-name-farkle = Farkle

# Akce - Hod a Uložení
farkle-roll = Hodit { $count } { $count ->
    [one] kostkou
    [few] kostkami
    [many] kostkou
   *[other] kostkami
}
farkle-bank = Uložit { $points } bodů

# Akce skórových kombinací
farkle-take-single-one = Jednička za { $points } bodů
farkle-take-single-five = Pětka za { $points } bodů
farkle-take-three-kind = Tři { $number } za { $points } bodů
farkle-take-four-kind = Čtyři { $number } za { $points } bodů
farkle-take-five-kind = Pět { $number } za { $points } bodů
farkle-take-six-kind = Šest { $number } za { $points } bodů
farkle-take-small-straight = Malá postupka za { $points } bodů
farkle-take-large-straight = Velká postupka za { $points } bodů
farkle-take-three-pairs = Tři páry za { $points } bodů
farkle-take-double-triplets = Dvojité trojice za { $points } bodů
farkle-take-full-house = Full house za { $points } bodů

# Herní události
farkle-rolls = { $player } hází { $count } { $count ->
    [one] kostkou
    [few] kostkami
    [many] kostkou
   *[other] kostkami
}...
farkle-you-roll = Házíte { $count } { $count ->
    [one] kostkou
    [few] kostkami
    [many] kostkou
   *[other] kostkami
}...
farkle-roll-result = { $dice }
farkle-farkle = FARKLE! { $player } ztrácí { $points } bodů
farkle-you-farkle = FARKLE! Ztrácíte { $points } bodů
farkle-takes-combo = { $player } bere { $combo } za { $points } bodů
farkle-you-take-combo = Berete { $combo } za { $points } bodů
farkle-hot-dice = Horké kostky!
farkle-banks = { $player } ukládá { $points } bodů, celkem { $total }
farkle-you-bank = Ukládáte { $points } bodů, celkem { $total }
farkle-winner = { $player } vyhrává s { $score } body!
farkle-you-win = Vyhráváte s { $score } body!
farkle-winners-tie = Remíza! Vítězové: { $players }

# Kontrola skóre tahu
farkle-turn-score = { $player } má { $points } bodů v tomto tahu.
farkle-no-turn = Momentálně nikdo není na tahu.

# Možnosti pro Farkle
farkle-set-target-score = Cílové skóre: { $score }
farkle-enter-target-score = Zadejte cílové skóre (500-5000):
farkle-option-changed-target = Cílové skóre nastaveno na { $score }.

# Důvody zakázaných akcí
farkle-must-take-combo = Musíte nejprve vzít skórovací kombinaci.
farkle-cannot-bank = Právě teď nemůžete uložit body.
