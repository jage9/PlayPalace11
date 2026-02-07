# 1-4-24 (Midnight) game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-midnight = 1-4-24
midnight-category = Giochi di Dadi

# Actions
midnight-roll = Tira i dadi
midnight-keep-die = Tieni { $value }
midnight-bank = Conferma

# Game events
midnight-turn-start = Turno di { $player }.
midnight-you-rolled = Hai tirato: { $dice }.
midnight-player-rolled = { $player } ha tirato: { $dice }.

# Keeping dice
midnight-you-keep = Tieni { $die }.
midnight-player-keeps = { $player } tiene { $die }.
midnight-you-unkeep = Rilasci { $die }.
midnight-player-unkeeps = { $player } rilascia { $die }.

# Turn status
midnight-you-have-kept = Dadi tenuti: { $kept }. Tiri rimanenti: { $remaining }.
midnight-player-has-kept = { $player } ha tenuto: { $kept }. { $remaining } dadi rimanenti.

# Scoring
midnight-you-scored = Hai segnato { $score } punti.
midnight-scored = { $player } ha segnato { $score } punti.
midnight-you-disqualified = Non hai sia 1 che 4. Squalificato!
midnight-player-disqualified = { $player } non ha sia 1 che 4. Squalificato!

# Round results
midnight-round-winner = { $player } vince il round!
midnight-round-tie = Round in parità tra { $players }.
midnight-all-disqualified = Tutti i giocatori squalificati! Nessun vincitore in questo round.

# Game winner
midnight-game-winner = { $player } vince il gioco con { $wins } vittorie di round!
midnight-game-tie = È un pareggio! { $players } hanno vinto { $wins } round ciascuno.

# Options
midnight-set-rounds = Round da giocare: { $rounds }
midnight-enter-rounds = Inserisci il numero di round da giocare:
midnight-option-changed-rounds = Round da giocare cambiati a { $rounds }

# Disabled reasons
midnight-need-to-roll = Devi prima tirare i dadi.
midnight-no-dice-to-keep = Nessun dado disponibile da tenere.
midnight-must-keep-one = Devi tenere almeno un dado per tiro.
midnight-must-roll-first = Devi prima tirare i dadi.
midnight-keep-all-first = Devi tenere tutti i dadi prima di confermare.
