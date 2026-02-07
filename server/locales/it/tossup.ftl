# Toss Up game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-tossup = Toss Up
tossup-category = Giochi di dadi

# Actions
tossup-roll-first = Tira { $count } dadi
tossup-roll-remaining = Tira i { $count } dadi rimanenti
tossup-bank = Conserva { $points } punti

# Game events
tossup-turn-start = Turno di { $player }. Punteggio: { $score }
tossup-you-roll = Hai tirato: { $results }.
tossup-player-rolls = { $player } ha tirato: { $results }.

# Turn status
tossup-you-have-points = Punti turno: { $turn_points }. Dadi rimanenti: { $dice_count }.
tossup-player-has-points = { $player } ha { $turn_points } punti turno. { $dice_count } dadi rimanenti.

# Fresh dice
tossup-you-get-fresh = Nessun dado rimasto! Ottieni { $count } dadi nuovi.
tossup-player-gets-fresh = { $player } ottiene { $count } dadi nuovi.

# Bust
tossup-you-bust = Sballato! Perdi { $points } punti per questo turno.
tossup-player-busts = { $player } sballa e perde { $points } punti!

# Bank
tossup-you-bank = Conservi { $points } punti. Punteggio totale: { $total }.
tossup-player-banks = { $player } conserva { $points } punti. Punteggio totale: { $total }.

# Winner
tossup-winner = { $player } vince con { $score } punti!
tossup-tie-tiebreaker = È un pareggio tra { $players }! Round di spareggio!

# Options
tossup-set-rules-variant = Variante regole: { $variant }
tossup-select-rules-variant = Seleziona variante regole:
tossup-option-changed-rules = Variante regole cambiata in { $variant }

tossup-set-starting-dice = Dadi iniziali: { $count }
tossup-enter-starting-dice = Inserisci il numero di dadi iniziali:
tossup-option-changed-dice = Dadi iniziali cambiati in { $count }

# Rules variants
tossup-rules-standard = Standard
tossup-rules-playpalace = PlayPalace

# Rules explanations
tossup-rules-standard-desc = 3 verdi, 2 gialli, 1 rosso per dado. Sballato se nessun verde e almeno un rosso.
tossup-rules-playpalace-desc = Distribuzione uguale. Sballato se tutti i dadi sono rossi.

# Disabled reasons
tossup-need-points = Hai bisogno di punti per conservare.
