# Tradeoff game messages

# Game info
game-name-tradeoff = Výmena

# Round and iteration flow
tradeoff-round-start = Kolo { $round }.
tradeoff-iteration = Ruka { $iteration } z 3.

# Phase 1: Trading
tradeoff-you-rolled = Hodili ste: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = výmena
tradeoff-trade-status-keeping = podržanie
tradeoff-confirm-trades = Potvrďte výmeny ({ $count } kociek)
tradeoff-keeping = Podržanie { $value }.
tradeoff-trading = Výmena { $value }.
tradeoff-player-traded = { $player } vymenil: { $dice }.
tradeoff-player-traded-none = { $player } podržal všetky kocky.

# Phase 2: Taking from pool
tradeoff-your-turn-take = Váš ťah na vzatie kocky z fondu.
tradeoff-take-die = Vezmite { $value } (zostáva { $remaining })
tradeoff-you-take = Vezmete { $value }.
tradeoff-player-takes = { $player } vezme { $value }.

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points } b.): { $sets }.
tradeoff-no-sets = { $player }: žiadne sety.

# Set descriptions (concise)
tradeoff-set-triple = trojica { $value }
tradeoff-set-group = skupina { $value }
tradeoff-set-mini-straight = mini postupnosť { $low }-{ $high }
tradeoff-set-double-triple = dvojitá trojica ({ $v1 } a { $v2 })
tradeoff-set-straight = postupnosť { $low }-{ $high }
tradeoff-set-double-group = dvojitá skupina ({ $v1 } a { $v2 })
tradeoff-set-all-groups = všetky skupiny
tradeoff-set-all-triplets = všetky trojice

# Round end
tradeoff-round-scores = Skóre kola { $round }:
tradeoff-score-line = { $player }: +{ $round_points } (celkom: { $total })
tradeoff-leader = { $player } vedie s { $score }.

# Game end
tradeoff-winner = { $player } vyhrá s { $score } bodmi!
tradeoff-winners-tie = Remíza! { $players } remizovali s { $score } bodmi!

# Status checks
tradeoff-view-hand = Zobraziť vašu ruku
tradeoff-view-pool = Zobraziť fond
tradeoff-view-players = Zobraziť hráčov
tradeoff-hand-display = Vaša ruka ({ $count } kociek): { $dice }
tradeoff-pool-display = Fond ({ $count } kociek): { $dice }
tradeoff-player-info = { $player }: { $hand }. Vymenil: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. Nič nevymenil.

# Error messages
tradeoff-not-trading-phase = Nie je fáza výmeny.
tradeoff-not-taking-phase = Nie je fáza brania.
tradeoff-already-confirmed = Už potvrdené.
tradeoff-no-die = Žiadna kocka na prepnutie.
tradeoff-no-more-takes = Žiadne ďalšie brania k dispozícii.
tradeoff-not-in-pool = Táto kocka nie je vo fonde.

# Options
tradeoff-set-target = Cieľové skóre: { $score }
tradeoff-enter-target = Zadajte cieľové skóre:
tradeoff-option-changed-target = Cieľové skóre nastavené na { $score }.
