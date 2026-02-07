# Tradeoff game messages

# Game info
game-name-tradeoff = Byte

# Round and iteration flow
tradeoff-round-start = Runda { $round }.
tradeoff-iteration = Hand { $iteration } av 3.

# Phase 1: Trading
tradeoff-you-rolled = Du kastade: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = byter
tradeoff-trade-status-keeping = behåller
tradeoff-confirm-trades = Bekräfta byten ({ $count } tärningar)
tradeoff-keeping = Behåller { $value }.
tradeoff-trading = Byter { $value }.
tradeoff-player-traded = { $player } bytte: { $dice }.
tradeoff-player-traded-none = { $player } behöll alla tärningar.

# Phase 2: Taking from pool
tradeoff-your-turn-take = Din tur att ta en tärning från poolen.
tradeoff-take-die = Ta en { $value } ({ $remaining } kvar)
tradeoff-you-take = Du tar en { $value }.
tradeoff-player-takes = { $player } tar en { $value }.

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points } p): { $sets }.
tradeoff-no-sets = { $player }: inga set.

# Set descriptions (concise)
tradeoff-set-triple = triss av { $value }or
tradeoff-set-group = grupp av { $value }or
tradeoff-set-mini-straight = ministege { $low }-{ $high }
tradeoff-set-double-triple = dubbeltriss ({ $v1 }or och { $v2 }or)
tradeoff-set-straight = stege { $low }-{ $high }
tradeoff-set-double-group = dubbelgrupp ({ $v1 }or och { $v2 }or)
tradeoff-set-all-groups = alla grupper
tradeoff-set-all-triplets = alla trissar

# Round end
tradeoff-round-scores = Runda { $round } poäng:
tradeoff-score-line = { $player }: +{ $round_points } (totalt: { $total })
tradeoff-leader = { $player } leder med { $score }.

# Game end
tradeoff-winner = { $player } vinner med { $score } poäng!
tradeoff-winners-tie = Det är oavgjort! { $players } oavgjort med { $score } poäng!

# Status checks
tradeoff-view-hand = Visa din hand
tradeoff-view-pool = Visa poolen
tradeoff-view-players = Visa spelare
tradeoff-hand-display = Din hand ({ $count } tärningar): { $dice }
tradeoff-pool-display = Pool ({ $count } tärningar): { $dice }
tradeoff-player-info = { $player }: { $hand }. Bytte: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. Bytte inget.

# Error messages
tradeoff-not-trading-phase = Inte i bytesfasen.
tradeoff-not-taking-phase = Inte i tagfasen.
tradeoff-already-confirmed = Redan bekräftad.
tradeoff-no-die = Ingen tärning att växla.
tradeoff-no-more-takes = Inga fler tag tillgängliga.
tradeoff-not-in-pool = Den tärningen finns inte i poolen.

# Options
tradeoff-set-target = Målpoäng: { $score }
tradeoff-enter-target = Ange målpoäng:
tradeoff-option-changed-target = Målpoäng inställd på { $score }.
