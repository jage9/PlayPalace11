# Tradeoff game messages

# Game info
game-name-tradeoff = Schimb

# Round and iteration flow
tradeoff-round-start = Runda { $round }.
tradeoff-iteration = Mână { $iteration } din 3.

# Phase 1: Trading
tradeoff-you-rolled = Ați aruncat: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = schimbă
tradeoff-trade-status-keeping = păstrează
tradeoff-confirm-trades = Confirmați schimburile ({ $count } zaruri)
tradeoff-keeping = Păstrați { $value }.
tradeoff-trading = Schimbați { $value }.
tradeoff-player-traded = { $player } a schimbat: { $dice }.
tradeoff-player-traded-none = { $player } a păstrat toate zarurile.

# Phase 2: Taking from pool
tradeoff-your-turn-take = Rândul dvs. să luați un zar din rezervă.
tradeoff-take-die = Luați un { $value } ({ $remaining } rămase)
tradeoff-you-take = Luați un { $value }.
tradeoff-player-takes = { $player } ia un { $value }.

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points } pct): { $sets }.
tradeoff-no-sets = { $player }: niciun set.

# Set descriptions (concise)
tradeoff-set-triple = triplu de { $value }
tradeoff-set-group = grup de { $value }
tradeoff-set-mini-straight = mini scară { $low }-{ $high }
tradeoff-set-double-triple = dublu triplu ({ $v1 } și { $v2 })
tradeoff-set-straight = scară { $low }-{ $high }
tradeoff-set-double-group = dublu grup ({ $v1 } și { $v2 })
tradeoff-set-all-groups = toate grupurile
tradeoff-set-all-triplets = toate triplele

# Round end
tradeoff-round-scores = Scoruri runda { $round }:
tradeoff-score-line = { $player }: +{ $round_points } (total: { $total })
tradeoff-leader = { $player } conduce cu { $score }.

# Game end
tradeoff-winner = { $player } câștigă cu { $score } puncte!
tradeoff-winners-tie = Egalitate! { $players } la egalitate cu { $score } puncte!

# Status checks
tradeoff-view-hand = Vizualizați mâna dvs.
tradeoff-view-pool = Vizualizați rezerva
tradeoff-view-players = Vizualizați jucătorii
tradeoff-hand-display = Mâna dvs. ({ $count } zaruri): { $dice }
tradeoff-pool-display = Rezervă ({ $count } zaruri): { $dice }
tradeoff-player-info = { $player }: { $hand }. Schimbat: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. Nu a schimbat nimic.

# Error messages
tradeoff-not-trading-phase = Nu este faza de schimb.
tradeoff-not-taking-phase = Nu este faza de luare.
tradeoff-already-confirmed = Deja confirmat.
tradeoff-no-die = Niciun zar de schimbat.
tradeoff-no-more-takes = Nu mai sunt luări disponibile.
tradeoff-not-in-pool = Acel zar nu este în rezervă.

# Options
tradeoff-set-target = Scor țintă: { $score }
tradeoff-enter-target = Introduceți scorul țintă:
tradeoff-option-changed-target = Scor țintă setat la { $score }.
