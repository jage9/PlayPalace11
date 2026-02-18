# Farkle game messages

# Game info
game-name-farkle = Farkle

# Actions - Roll and Bank
farkle-roll = Tirar { $count } { $count ->
    [one] dado
   *[other] dados
}
farkle-bank = Guardar { $points } puntos

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = Un solo 1 por { $points } puntos
farkle-take-single-five = Un solo 5 por { $points } puntos
farkle-take-three-kind = Tres { $number }s por { $points } puntos
farkle-take-four-kind = Cuatro { $number }s por { $points } puntos
farkle-take-five-kind = Cinco { $number }s por { $points } puntos
farkle-take-six-kind = Seis { $number }s por { $points } puntos
farkle-take-small-straight = Escalera Pequeña por { $points } puntos
farkle-take-large-straight = Escalera Grande por { $points } puntos
farkle-take-three-pairs = Tres pares por { $points } puntos
farkle-take-double-triplets = Triples dobles por { $points } puntos
farkle-take-full-house = Full house por { $points } puntos

# Game events (matching v10 exactly)
farkle-rolls = { $player } tira { $count } { $count ->
    [one] dado
   *[other] dados
}...
farkle-you-roll = Tiras { $count } { $count ->
    [one] dado
   *[other] dados
}...
farkle-roll-result = { $dice }
farkle-farkle = ¡FARKLE! { $player } pierde { $points } puntos
farkle-you-farkle = ¡FARKLE! Pierdes { $points } puntos
farkle-takes-combo = { $player } toma { $combo } por { $points } puntos
farkle-you-take-combo = Tomas { $combo } por { $points } puntos
farkle-hot-dice = ¡Dados calientes!
farkle-banks = { $player } guarda { $points } puntos para un total de { $total }
farkle-you-bank = Guardas { $points } puntos para un total de { $total }
farkle-winner = ¡{ $player } gana con { $score } puntos!
farkle-you-win = ¡Ganas con { $score } puntos!
farkle-winners-tie = ¡Tenemos un empate! Ganadores: { $players }

# Check turn score action
farkle-turn-score = { $player } tiene { $points } puntos este turno.
farkle-no-turn = Nadie está tomando un turno actualmente.

# Farkle-specific options
farkle-set-target-score = Puntuación objetivo: { $score }
farkle-enter-target-score = Ingresa la puntuación objetivo (500-5000):
farkle-option-changed-target = Puntuación objetivo establecida en { $score }.

# Disabled action reasons
farkle-must-take-combo = Debes tomar una combinación de puntuación primero.
farkle-cannot-bank = No puedes guardar ahora mismo.

# Additional Farkle options
farkle-set-initial-bank-score = Puntuación inicial para guardar: { $score }
farkle-enter-initial-bank-score = Introduce la puntuación inicial para guardar (0-1000):
farkle-option-changed-initial-bank-score = La puntuación inicial para guardar se estableció en { $score }.
farkle-toggle-hot-dice-multiplier = Multiplicador de hot dice: { $enabled }
farkle-option-changed-hot-dice-multiplier = El multiplicador de hot dice se estableció en { $enabled }.

# Action feedback
farkle-minimum-initial-bank-score = La puntuación mínima inicial para guardar es { $score }.
