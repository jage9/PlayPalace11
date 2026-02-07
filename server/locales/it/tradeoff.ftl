# Tradeoff game messages

# Game info
game-name-tradeoff = Scambio

# Round and iteration flow
tradeoff-round-start = Round { $round }.
tradeoff-iteration = Mano { $iteration } di 3.

# Phase 1: Trading
tradeoff-you-rolled = Hai tirato: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = scambiando
tradeoff-trade-status-keeping = tenendo
tradeoff-confirm-trades = Conferma scambi ({ $count } dadi)
tradeoff-keeping = Tieni { $value }.
tradeoff-trading = Scambia { $value }.
tradeoff-player-traded = { $player } ha scambiato: { $dice }.
tradeoff-player-traded-none = { $player } ha tenuto tutti i dadi.

# Phase 2: Taking from pool
tradeoff-your-turn-take = È il tuo turno di prendere un dado dalla riserva.
tradeoff-take-die = Prendi un { $value } ({ $remaining } rimasti)
tradeoff-you-take = Prendi un { $value }.
tradeoff-player-takes = { $player } prende un { $value }.

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points } pt): { $sets }.
tradeoff-no-sets = { $player }: nessun set.

# Set descriptions (concise)
tradeoff-set-triple = tris di { $value }
tradeoff-set-group = gruppo di { $value }
tradeoff-set-mini-straight = mini scala { $low }-{ $high }
tradeoff-set-double-triple = doppio tris ({ $v1 } e { $v2 })
tradeoff-set-straight = scala { $low }-{ $high }
tradeoff-set-double-group = doppio gruppo ({ $v1 } e { $v2 })
tradeoff-set-all-groups = tutti i gruppi
tradeoff-set-all-triplets = tutti i tris

# Round end
tradeoff-round-scores = Punteggi round { $round }:
tradeoff-score-line = { $player }: +{ $round_points } (totale: { $total })
tradeoff-leader = { $player } è in testa con { $score }.

# Game end
tradeoff-winner = { $player } vince con { $score } punti!
tradeoff-winners-tie = È un pareggio! { $players } pari con { $score } punti!

# Status checks
tradeoff-view-hand = Visualizza la tua mano
tradeoff-view-pool = Visualizza la riserva
tradeoff-view-players = Visualizza i giocatori
tradeoff-hand-display = La tua mano ({ $count } dadi): { $dice }
tradeoff-pool-display = Riserva ({ $count } dadi): { $dice }
tradeoff-player-info = { $player }: { $hand }. Scambiato: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. Nulla scambiato.

# Error messages
tradeoff-not-trading-phase = Non è la fase di scambio.
tradeoff-not-taking-phase = Non è la fase di presa.
tradeoff-already-confirmed = Già confermato.
tradeoff-no-die = Nessun dado da cambiare.
tradeoff-no-more-takes = Nessuna presa disponibile.
tradeoff-not-in-pool = Quel dado non è nella riserva.

# Options
tradeoff-set-target = Punteggio obiettivo: { $score }
tradeoff-enter-target = Inserisci punteggio obiettivo:
tradeoff-option-changed-target = Punteggio obiettivo impostato a { $score }.
