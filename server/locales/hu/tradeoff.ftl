# Tradeoff game messages

# Game info
game-name-tradeoff = Csere

# Round and iteration flow
tradeoff-round-start = { $round }. kör.
tradeoff-iteration = { $iteration }. kéz 3-ból.

# Phase 1: Trading
tradeoff-you-rolled = Dobtál: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = cserélés
tradeoff-trade-status-keeping = megtartás
tradeoff-confirm-trades = Cserék megerősítése ({ $count } kocka)
tradeoff-keeping = Megtartás: { $value }.
tradeoff-trading = Cserélés: { $value }.
tradeoff-player-traded = { $player } cserélt: { $dice }.
tradeoff-player-traded-none = { $player } minden kockát megtartott.

# Phase 2: Taking from pool
tradeoff-your-turn-take = A te köröd, hogy vegyél egy kockát a poolból.
tradeoff-take-die = Végy egy { $value }-t ({ $remaining } maradt)
tradeoff-you-take = Veszel egy { $value }-t.
tradeoff-player-takes = { $player } vesz egy { $value }-t.

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points } pont): { $sets }.
tradeoff-no-sets = { $player }: nincs szett.

# Set descriptions (concise)
tradeoff-set-triple = hármas { $value }
tradeoff-set-group = csoport { $value }
tradeoff-set-mini-straight = mini sor { $low }-{ $high }
tradeoff-set-double-triple = dupla hármas ({ $v1 } és { $v2 })
tradeoff-set-straight = sor { $low }-{ $high }
tradeoff-set-double-group = dupla csoport ({ $v1 } és { $v2 })
tradeoff-set-all-groups = minden csoport
tradeoff-set-all-triplets = minden hármas

# Round end
tradeoff-round-scores = { $round }. kör eredményei:
tradeoff-score-line = { $player }: +{ $round_points } (összesen: { $total })
tradeoff-leader = { $player } vezet { $score } ponttal.

# Game end
tradeoff-winner = { $player } nyer { $score } ponttal!
tradeoff-winners-tie = Döntetlen! { $players } döntetlenben { $score } ponttal!

# Status checks
tradeoff-view-hand = Nézd meg a kezedet
tradeoff-view-pool = Nézd meg a poolt
tradeoff-view-players = Nézd meg a játékosokat
tradeoff-hand-display = A kezed ({ $count } kocka): { $dice }
tradeoff-pool-display = Pool ({ $count } kocka): { $dice }
tradeoff-player-info = { $player }: { $hand }. Cserélt: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. Nem cserélt semmit.

# Error messages
tradeoff-not-trading-phase = Nem csere fázis.
tradeoff-not-taking-phase = Nem vétel fázis.
tradeoff-already-confirmed = Már megerősítve.
tradeoff-no-die = Nincs kocka váltáshoz.
tradeoff-no-more-takes = Nincs több vétel lehetőség.
tradeoff-not-in-pool = Ez a kocka nincs a poolban.

# Options
tradeoff-set-target = Célpontszám: { $score }
tradeoff-enter-target = Add meg a célpontszámot:
tradeoff-option-changed-target = Célpontszám beállítva: { $score }.
