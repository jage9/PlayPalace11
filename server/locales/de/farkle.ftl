# Farkle-Spielnachrichten

# Spielinformationen
game-name-farkle = Farkle

# Aktionen - Würfeln und Sichern
farkle-roll = { $count } { $count ->
    [one] Würfel
   *[other] Würfel
} würfeln
farkle-bank = { $points } Punkte sichern

# Bewertungskombinationsaktionen (stimmt genau mit v10 überein)
farkle-take-single-one = Einzelne 1 für { $points } Punkte
farkle-take-single-five = Einzelne 5 für { $points } Punkte
farkle-take-three-kind = Drei { $number }en für { $points } Punkte
farkle-take-four-kind = Vier { $number }en für { $points } Punkte
farkle-take-five-kind = Fünf { $number }en für { $points } Punkte
farkle-take-six-kind = Sechs { $number }en für { $points } Punkte
farkle-take-small-straight = Kleine Straße für { $points } Punkte
farkle-take-large-straight = Große Straße für { $points } Punkte
farkle-take-three-pairs = Drei Paare für { $points } Punkte
farkle-take-double-triplets = Doppelter Drilling für { $points } Punkte
farkle-take-full-house = Full House für { $points } Punkte

# Spielereignisse (stimmt genau mit v10 überein)
farkle-rolls = { $player } würfelt { $count } { $count ->
    [one] Würfel
   *[other] Würfel
}...
farkle-you-roll = Sie würfeln { $count } { $count ->
    [one] Würfel
   *[other] Würfel
}...
farkle-roll-result = { $dice }
farkle-farkle = FARKLE! { $player } verliert { $points } Punkte
farkle-you-farkle = FARKLE! Sie verlieren { $points } Punkte
farkle-takes-combo = { $player } nimmt { $combo } für { $points } Punkte
farkle-you-take-combo = Sie nehmen { $combo } für { $points } Punkte
farkle-hot-dice = Heiße Würfel!
farkle-banks = { $player } sichert { $points } Punkte für insgesamt { $total }
farkle-you-bank = Sie sichern { $points } Punkte für insgesamt { $total }
farkle-winner = { $player } gewinnt mit { $score } Punkten!
farkle-you-win = Sie gewinnen mit { $score } Punkten!
farkle-winners-tie = Wir haben ein Unentschieden! Gewinner: { $players }

# Zugpunktzahl prüfen-Aktion
farkle-turn-score = { $player } hat { $points } Punkte in diesem Zug.
farkle-no-turn = Momentan ist niemand am Zug.

# Farkle-spezifische Optionen
farkle-set-target-score = Zielpunktzahl: { $score }
farkle-enter-target-score = Zielpunktzahl eingeben (500-5000):
farkle-option-changed-target = Zielpunktzahl auf { $score } gesetzt.

# Gründe für deaktivierte Aktionen
farkle-must-take-combo = Sie müssen zuerst eine Bewertungskombination nehmen.
farkle-cannot-bank = Sie können jetzt nicht sichern.

# Additional Farkle options
farkle-set-initial-bank-score = Anfangs-Bankpunktzahl: { $score }
farkle-enter-initial-bank-score = Anfangs-Bankpunktzahl eingeben (0-1000):
farkle-option-changed-initial-bank-score = Anfangs-Bankpunktzahl auf { $score } gesetzt.
farkle-toggle-hot-dice-multiplier = Hot-Dice-Multiplikator: { $enabled }
farkle-option-changed-hot-dice-multiplier = Hot-Dice-Multiplikator auf { $enabled } gesetzt.

# Action feedback
farkle-minimum-initial-bank-score = Mindestwert für die Anfangs-Bankpunktzahl ist { $score }.
