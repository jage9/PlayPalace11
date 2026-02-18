# Farkle game messages

# Game info
game-name-farkle = Farkle

# Actions - Roll and Bank
farkle-roll = Dobj { $count } { $count ->
    [one] kockát
   *[other] kockát
}
farkle-bank = { $points } pont berakása

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = Egyetlen 1-es { $points } pontért
farkle-take-single-five = Egyetlen 5-ös { $points } pontért
farkle-take-three-kind = Három { $number }-es { $points } pontért
farkle-take-four-kind = Négy { $number }-es { $points } pontért
farkle-take-five-kind = Öt { $number }-es { $points } pontért
farkle-take-six-kind = Hat { $number }-es { $points } pontért
farkle-take-small-straight = Kis sor { $points } pontért
farkle-take-large-straight = Nagy sor { $points } pontért
farkle-take-three-pairs = Három pár { $points } pontért
farkle-take-double-triplets = Dupla hármasok { $points } pontért
farkle-take-full-house = Full { $points } pontért

# Game events (matching v10 exactly)
farkle-rolls = { $player } dob { $count } { $count ->
    [one] kockát
   *[other] kockát
}...
farkle-you-roll = Dobsz { $count } { $count ->
    [one] kockát
   *[other] kockát
}...
farkle-roll-result = { $dice }
farkle-farkle = FARKLE! { $player } elveszít { $points } pontot
farkle-you-farkle = FARKLE! Elveszítesz { $points } pontot
farkle-takes-combo = { $player } választja: { $combo } { $points } pontért
farkle-you-take-combo = Választod: { $combo } { $points } pontért
farkle-hot-dice = Forró kockák!
farkle-banks = { $player } berak { $points } pontot, összesen { $total }
farkle-you-bank = Beraksz { $points } pontot, összesen { $total }
farkle-winner = { $player } nyer { $score } ponttal!
farkle-you-win = Nyersz { $score } ponttal!
farkle-winners-tie = Döntetlen! Győztesek: { $players }

# Check turn score action
farkle-turn-score = { $player }nak { $points } pontja van ebben a körben.
farkle-no-turn = Jelenleg senki sem van körön.

# Farkle-specific options
farkle-set-target-score = Célpontszám: { $score }
farkle-enter-target-score = Adja meg a célpontszámot (500-5000):
farkle-option-changed-target = Célpontszám beállítva { $score }-ra.

# Disabled action reasons
farkle-must-take-combo = Először egy pontozó kombinációt kell választanod.
farkle-cannot-bank = Most nem rakhatsz be pontokat.

# Additional Farkle options
farkle-set-initial-bank-score = Kezdő bankolási pontszám: { $score }
farkle-enter-initial-bank-score = Add meg a kezdő bankolási pontszámot (0-1000):
farkle-option-changed-initial-bank-score = A kezdő bankolási pontszám { $score } értékre állítva.
farkle-toggle-hot-dice-multiplier = Hot dice szorzó: { $enabled }
farkle-option-changed-hot-dice-multiplier = A hot dice szorzó { $enabled } értékre állítva.

# Action feedback
farkle-minimum-initial-bank-score = A minimális kezdő bankolási pontszám { $score }.
