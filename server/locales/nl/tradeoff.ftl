# Tradeoff game messages

# Game info
game-name-tradeoff = Tradeoff

# Round and iteration flow
tradeoff-round-start = Ronde { $round }.
tradeoff-iteration = Hand { $iteration } van 3.

# Phase 1: Trading
tradeoff-you-rolled = Je gooide: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = ruilen
tradeoff-trade-status-keeping = bewaren
tradeoff-confirm-trades = Bevestig ruilingen ({ $count } dobbelstenen)
tradeoff-keeping = { $value } bewaren.
tradeoff-trading = { $value } ruilen.
tradeoff-player-traded = { $player } ruilde: { $dice }.
tradeoff-player-traded-none = { $player } bewaarde alle dobbelstenen.

# Phase 2: Taking from pool
tradeoff-your-turn-take = Jouw beurt om een dobbelsteen uit de pool te pakken.
tradeoff-take-die = Pak een { $value } ({ $remaining } over)
tradeoff-you-take = Je pakt een { $value }.
tradeoff-player-takes = { $player } pakt een { $value }.

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points } ptn): { $sets }.
tradeoff-no-sets = { $player }: geen sets.

# Set descriptions (concise)
tradeoff-set-triple = triplet van { $value }en
tradeoff-set-group = groep van { $value }en
tradeoff-set-mini-straight = mini straat { $low }-{ $high }
tradeoff-set-double-triple = dubbele triplet ({ $v1 }en en { $v2 }en)
tradeoff-set-straight = straat { $low }-{ $high }
tradeoff-set-double-group = dubbele groep ({ $v1 }en en { $v2 }en)
tradeoff-set-all-groups = alle groepen
tradeoff-set-all-triplets = alle triplets

# Round end
tradeoff-round-scores = Ronde { $round } scores:
tradeoff-score-line = { $player }: +{ $round_points } (totaal: { $total })
tradeoff-leader = { $player } leidt met { $score }.

# Game end
tradeoff-winner = { $player } wint met { $score } punten!
tradeoff-winners-tie = Het is gelijk! { $players } eindigden gelijk met { $score } punten!

# Status checks
tradeoff-view-hand = Bekijk je hand
tradeoff-view-pool = Bekijk de pool
tradeoff-view-players = Bekijk spelers
tradeoff-hand-display = Jouw hand ({ $count } dobbelstenen): { $dice }
tradeoff-pool-display = Pool ({ $count } dobbelstenen): { $dice }
tradeoff-player-info = { $player }: { $hand }. Geruild: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. Niets geruild.

# Error messages
tradeoff-not-trading-phase = Niet in de ruilfase.
tradeoff-not-taking-phase = Niet in de pakfase.
tradeoff-already-confirmed = Reeds bevestigd.
tradeoff-no-die = Geen dobbelsteen om te wisselen.
tradeoff-no-more-takes = Geen pakbeurten meer beschikbaar.
tradeoff-not-in-pool = Die dobbelsteen zit niet in de pool.

# Options
tradeoff-set-target = Doelscore: { $score }
tradeoff-enter-target = Voer doelscore in:
tradeoff-option-changed-target = Doelscore ingesteld op { $score }.
