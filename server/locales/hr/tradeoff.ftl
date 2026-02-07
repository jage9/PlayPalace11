# Tradeoff game messages

# Game info
game-name-tradeoff = Razmjena

# Round and iteration flow
tradeoff-round-start = Runda { $round }.
tradeoff-iteration = Ruka { $iteration } od 3.

# Phase 1: Trading
tradeoff-you-rolled = Bacili ste: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = mijenja se
tradeoff-trade-status-keeping = zadržava se
tradeoff-confirm-trades = Potvrdite razmjene ({ $count } kockica)
tradeoff-keeping = Zadržavanje { $value }.
tradeoff-trading = Razmjena { $value }.
tradeoff-player-traded = { $player } je razmijenio: { $dice }.
tradeoff-player-traded-none = { $player } je zadržao sve kockice.

# Phase 2: Taking from pool
tradeoff-your-turn-take = Vaš red za uzimanje kockice iz fonda.
tradeoff-take-die = Uzmite { $value } (preostalo { $remaining })
tradeoff-you-take = Uzimate { $value }.
tradeoff-player-takes = { $player } uzima { $value }.

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points } bod.): { $sets }.
tradeoff-no-sets = { $player }: nema setova.

# Set descriptions (concise)
tradeoff-set-triple = trojka { $value }
tradeoff-set-group = grupa { $value }
tradeoff-set-mini-straight = mini niz { $low }-{ $high }
tradeoff-set-double-triple = dvostruka trojka ({ $v1 } i { $v2 })
tradeoff-set-straight = niz { $low }-{ $high }
tradeoff-set-double-group = dvostruka grupa ({ $v1 } i { $v2 })
tradeoff-set-all-groups = sve grupe
tradeoff-set-all-triplets = sve trojke

# Round end
tradeoff-round-scores = Rezultati runde { $round }:
tradeoff-score-line = { $player }: +{ $round_points } (ukupno: { $total })
tradeoff-leader = { $player } vodi sa { $score }.

# Game end
tradeoff-winner = { $player } pobjeđuje sa { $score } bodova!
tradeoff-winners-tie = Neriješeno! { $players } neriješeni sa { $score } bodova!

# Status checks
tradeoff-view-hand = Pogledajte svoju ruku
tradeoff-view-pool = Pogledajte fond
tradeoff-view-players = Pogledajte igrače
tradeoff-hand-display = Vaša ruka ({ $count } kockica): { $dice }
tradeoff-pool-display = Fond ({ $count } kockica): { $dice }
tradeoff-player-info = { $player }: { $hand }. Razmijenio: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. Ništa nije razmijenio.

# Error messages
tradeoff-not-trading-phase = Nije faza razmjene.
tradeoff-not-taking-phase = Nije faza uzimanja.
tradeoff-already-confirmed = Već potvrđeno.
tradeoff-no-die = Nema kockice za promjenu.
tradeoff-no-more-takes = Nema više dostupnih uzimanja.
tradeoff-not-in-pool = Ta kockica nije u fondu.

# Options
tradeoff-set-target = Ciljni rezultat: { $score }
tradeoff-enter-target = Unesite ciljni rezultat:
tradeoff-option-changed-target = Ciljni rezultat postavljen na { $score }.
