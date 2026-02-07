# Yahtzee game messages

# Game info
game-name-yahtzee = Yahtzee

# Actions - Rolling
yahtzee-roll = Ritira ({ $count } rimasti)
yahtzee-roll-all = Tira i dadi

# Upper section scoring categories
yahtzee-score-ones = Uni per { $points } punti
yahtzee-score-twos = Due per { $points } punti
yahtzee-score-threes = Tre per { $points } punti
yahtzee-score-fours = Quattro per { $points } punti
yahtzee-score-fives = Cinque per { $points } punti
yahtzee-score-sixes = Sei per { $points } punti

# Lower section scoring categories
yahtzee-score-three-kind = Tris per { $points } punti
yahtzee-score-four-kind = Poker per { $points } punti
yahtzee-score-full-house = Full per { $points } punti
yahtzee-score-small-straight = Scala piccola per { $points } punti
yahtzee-score-large-straight = Scala grande per { $points } punti
yahtzee-score-yahtzee = Yahtzee per { $points } punti
yahtzee-score-chance = Fortuna per { $points } punti

# Game events
yahtzee-you-rolled = Hai tirato: { $dice }. Tiri rimanenti: { $remaining }
yahtzee-player-rolled = { $player } ha tirato: { $dice }. Tiri rimanenti: { $remaining }

# Scoring announcements
yahtzee-you-scored = Hai segnato { $points } punti in { $category }.
yahtzee-player-scored = { $player } ha segnato { $points } in { $category }.

# Yahtzee bonus
yahtzee-you-bonus = Bonus Yahtzee! +100 punti
yahtzee-player-bonus = { $player } ha ottenuto un bonus Yahtzee! +100 punti

# Upper section bonus
yahtzee-you-upper-bonus = Bonus sezione superiore! +35 punti ({ $total } nella sezione superiore)
yahtzee-player-upper-bonus = { $player } ha guadagnato il bonus della sezione superiore! +35 punti
yahtzee-you-upper-bonus-missed = Hai mancato il bonus della sezione superiore ({ $total } nella sezione superiore, servivano 63).
yahtzee-player-upper-bonus-missed = { $player } ha mancato il bonus della sezione superiore.

# Scoring mode
yahtzee-choose-category = Scegli una categoria per segnare.
yahtzee-continuing = Turno continua.

# Status checks
yahtzee-check-scoresheet = Controlla il punteggio
yahtzee-view-dice = Controlla la mano
yahtzee-your-dice = I tuoi dadi: { $dice }.
yahtzee-your-dice-kept = I tuoi dadi: { $dice }. Tenendo: { $kept }
yahtzee-not-rolled = Non hai ancora tirato.

# Scoresheet display
yahtzee-scoresheet-header = === Scheda di { $player } ===
yahtzee-scoresheet-upper = Sezione superiore:
yahtzee-scoresheet-lower = Sezione inferiore:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = Totale superiore: { $total } (BONUS: +35)
yahtzee-scoresheet-upper-total-needed = Totale superiore: { $total } ({ $needed } ancora per il bonus)
yahtzee-scoresheet-yahtzee-bonus = Bonus Yahtzee: { $count } x 100 = { $total }
yahtzee-scoresheet-grand-total = PUNTEGGIO TOTALE: { $total }

# Category names (for announcements)
yahtzee-category-ones = Uni
yahtzee-category-twos = Due
yahtzee-category-threes = Tre
yahtzee-category-fours = Quattro
yahtzee-category-fives = Cinque
yahtzee-category-sixes = Sei
yahtzee-category-three-kind = Tris
yahtzee-category-four-kind = Poker
yahtzee-category-full-house = Full
yahtzee-category-small-straight = Scala piccola
yahtzee-category-large-straight = Scala grande
yahtzee-category-yahtzee = Yahtzee
yahtzee-category-chance = Fortuna

# Game end
yahtzee-winner = { $player } vince con { $score } punti!
yahtzee-winners-tie = È un pareggio! { $players } hanno tutti segnato { $score } punti!

# Options
yahtzee-set-rounds = Numero di partite: { $rounds }
yahtzee-enter-rounds = Inserisci il numero di partite (1-10):
yahtzee-option-changed-rounds = Numero di partite impostato a { $rounds }.

# Disabled action reasons
yahtzee-no-rolls-left = Non hai più tiri.
yahtzee-roll-first = Devi prima tirare.
yahtzee-category-filled = Quella categoria è già piena.
