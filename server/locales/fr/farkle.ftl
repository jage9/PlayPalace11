# Messages du jeu Farkle

# Informations sur le jeu
game-name-farkle = Farkle

# Actions - Lancer et Banquer
farkle-roll = Lancer { $count } { $count ->
    [0] dé
    [1] dé
   *[other] dés
}
farkle-bank = Banquer { $points } points

# Actions de combinaisons de score (correspondant exactement à v10)
farkle-take-single-one = Un 1 seul pour { $points } points
farkle-take-single-five = Un 5 seul pour { $points } points
farkle-take-three-kind = Trois { $number } pour { $points } points
farkle-take-four-kind = Quatre { $number } pour { $points } points
farkle-take-five-kind = Cinq { $number } pour { $points } points
farkle-take-six-kind = Six { $number } pour { $points } points
farkle-take-small-straight = Petite suite pour { $points } points
farkle-take-large-straight = Grande suite pour { $points } points
farkle-take-three-pairs = Trois paires pour { $points } points
farkle-take-double-triplets = Double triplets pour { $points } points
farkle-take-full-house = Full house pour { $points } points

# Événements de jeu (correspondant exactement à v10)
farkle-rolls = { $player } lance { $count } { $count ->
    [0] dé
    [1] dé
   *[other] dés
}...
farkle-you-roll = Vous lancez { $count } { $count ->
    [0] dé
    [1] dé
   *[other] dés
}...
farkle-roll-result = { $dice }
farkle-farkle = FARKLE ! { $player } perd { $points } points
farkle-you-farkle = FARKLE ! Vous perdez { $points } points
farkle-takes-combo = { $player } prend { $combo } pour { $points } points
farkle-you-take-combo = Vous prenez { $combo } pour { $points } points
farkle-hot-dice = Dés chauds !
farkle-banks = { $player } banque { $points } points pour un total de { $total }
farkle-you-bank = Vous banquez { $points } points pour un total de { $total }
farkle-winner = { $player } gagne avec { $score } points !
farkle-you-win = Vous gagnez avec { $score } points !
farkle-winners-tie = Nous avons une égalité ! Gagnants : { $players }

# Action de vérification du score du tour
farkle-turn-score = { $player } a { $points } points ce tour.
farkle-no-turn = Personne ne joue actuellement.

# Options spécifiques à Farkle
farkle-set-target-score = Score cible : { $score }
farkle-enter-target-score = Entrez le score cible (500-5000) :
farkle-option-changed-target = Score cible défini sur { $score }.

# Raisons d'action désactivée
farkle-must-take-combo = Vous devez d'abord prendre une combinaison de score.
farkle-cannot-bank = Vous ne pouvez pas banquer maintenant.

# Additional Farkle options
farkle-set-initial-bank-score = Score initial à banquer : { $score }
farkle-enter-initial-bank-score = Entrez le score initial à banquer (0-1000) :
farkle-option-changed-initial-bank-score = Le score initial à banquer est défini sur { $score }.
farkle-toggle-hot-dice-multiplier = Multiplicateur hot dice : { $enabled }
farkle-option-changed-hot-dice-multiplier = Le multiplicateur hot dice est défini sur { $enabled }.

# Action feedback
farkle-minimum-initial-bank-score = Le score initial minimum à banquer est { $score }.
