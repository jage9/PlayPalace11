# Farkle game messages (isiZulu)

# Game info
game-name-farkle = Farkle

# Actions - Roll and Bank
farkle-roll = Phonsa { $count } { $count ->
    [one] idayisi
   *[other] amadayisi
}
farkle-bank = Gcina amaphuzu angu-{ $points }

# Scoring combination actions
farkle-take-single-one = U-1 owodwa ngamaphuzu angu-{ $points }
farkle-take-single-five = U-5 owodwa ngamaphuzu angu-{ $points }
farkle-take-three-kind = Ama-{ $number } amathathu ngamaphuzu angu-{ $points }
farkle-take-four-kind = Ama-{ $number } amane ngamaphuzu angu-{ $points }
farkle-take-five-kind = Ama-{ $number } amahlanu ngamaphuzu angu-{ $points }
farkle-take-six-kind = Ama-{ $number } ayisithupha ngamaphuzu angu-{ $points }
farkle-take-small-straight = Ukulandelana Okuncane ngamaphuzu angu-{ $points }
farkle-take-large-straight = Ukulandelana Okukhulu ngamaphuzu angu-{ $points }
farkle-take-three-pairs = Amapheya amathathu ngamaphuzu angu-{ $points }
farkle-take-double-triplets = Amatriplet amabili ngamaphuzu angu-{ $points }
farkle-take-full-house = Indlu egcwele ngamaphuzu angu-{ $points }

# Game events
farkle-rolls = U-{ $player } uphonsa { $count } { $count ->
    [one] idayisi
   *[other] amadayisi
}...
farkle-you-roll = Wena uphonsa { $count } { $count ->
    [one] idayisi
   *[other] amadayisi
}...
farkle-roll-result = { $dice }
farkle-farkle = I-FARKLE! U-{ $player } ulahlekelwa amaphuzu angu-{ $points }
farkle-you-farkle = I-FARKLE! Wena ulahlekelwa amaphuzu angu-{ $points }
farkle-takes-combo = U-{ $player } uthatha { $combo } ngamaphuzu angu-{ $points }
farkle-you-take-combo = Wena uthatha { $combo } ngamaphuzu angu-{ $points }
farkle-hot-dice = Amadayisi ashisayo!
farkle-banks = U-{ $player } ugcina amaphuzu angu-{ $points } esambeni esingu-{ $total }
farkle-you-bank = Wena ugcina amaphuzu angu-{ $points } esambeni esingu-{ $total }
farkle-winner = U-{ $player } uyawina ngamaphuzu angu-{ $score }!
farkle-you-win = Wena uyawina ngamaphuzu angu-{ $score }!
farkle-winners-tie = Siyalinganiswa! Abawini: { $players }

# Check turn score action
farkle-turn-score = U-{ $player } unamaphuzu angu-{ $points } kule shintshi.
farkle-no-turn = Akekho ophatha ishintshi njengamanje.

# Farkle-specific options
farkle-set-target-score = Amaphuzu ahlosiwe: { $score }
farkle-enter-target-score = Faka amaphuzu ahlosiwe (500-5000):
farkle-option-changed-target = Amaphuzu ahlosiwe asetelwe ku-{ $score }.

# Disabled action reasons
farkle-must-take-combo = Kufanele uthathe isihlanganiso samaphuzu kuqala.
farkle-cannot-bank = Awukwazi ukugcina manje.

# Additional Farkle options
farkle-set-initial-bank-score = Amaphuzu okuqala okubanka: { $score }
farkle-enter-initial-bank-score = Faka amaphuzu okuqala okubanka (0-1000):
farkle-option-changed-initial-bank-score = Amaphuzu okuqala okubanka asethwe ku-{ $score }.
farkle-toggle-hot-dice-multiplier = I-multiplier ye-hot dice: { $enabled }
farkle-option-changed-hot-dice-multiplier = I-multiplier ye-hot dice isethwe ku-{ $enabled }.

# Action feedback
farkle-minimum-initial-bank-score = Amaphuzu amancane okuqala okubanka ngu-{ $score }.
