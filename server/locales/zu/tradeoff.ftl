# Tradeoff game messages (isiZulu)

# Game info
game-name-tradeoff = Tradeoff

# Round and iteration flow
tradeoff-round-start = Umjikelezo { $round }.
tradeoff-iteration = Isandla { $iteration } ku-3.

# Phase 1: Trading
tradeoff-you-rolled = Wena uphonse: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = ukushintshanisa
tradeoff-trade-status-keeping = ukugcina
tradeoff-confirm-trades = Qinisekisa ukushintshanisa (amadayisi angu-{ $count })
tradeoff-keeping = Kugcinwa { $value }.
tradeoff-trading = Kushintshaniswa { $value }.
tradeoff-player-traded = U-{ $player } ushintshanise: { $dice }.
tradeoff-player-traded-none = U-{ $player } ugcine onke amadayisi.

# Phase 2: Taking from pool
tradeoff-your-turn-take = Ishintshi lakho lokuthatha idayisi esizindeni.
tradeoff-take-die = Thatha u-{ $value } (kusele u-{ $remaining })
tradeoff-you-take = Wena uthatha u-{ $value }.
tradeoff-player-takes = U-{ $player } uthatha u-{ $value }.

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points } pts): { $sets }.
tradeoff-no-sets = { $player }: awekho masethi.

# Set descriptions (concise)
tradeoff-set-triple = i-triple ye-{ $value }s
tradeoff-set-group = iqembu le-{ $value }s
tradeoff-set-mini-straight = ukuqonda okuncane { $low }-{ $high }
tradeoff-set-double-triple = i-triple ephindwe kabili ({ $v1 }s no-{ $v2 }s)
tradeoff-set-straight = ukuqonda { $low }-{ $high }
tradeoff-set-double-group = iqembu eliphindwe kabili ({ $v1 }s no-{ $v2 }s)
tradeoff-set-all-groups = wonke amaqembu
tradeoff-set-all-triplets = wonke ama-triplets

# Round end
tradeoff-round-scores = Amaphuzu omjikelezo { $round }:
tradeoff-score-line = { $player }: +{ $round_points } (isamba: { $total })
tradeoff-leader = U-{ $player } uhola ngo-{ $score }.

# Game end
tradeoff-winner = U-{ $player } uyawina ngamaphuzu angu-{ $score }!
tradeoff-winners-tie = Kuyalinganiswa! { $players } balinganiswe ngamaphuzu angu-{ $score }!

# Status checks
tradeoff-view-hand = Bheka isandla sakho
tradeoff-view-pool = Bheka isizinda
tradeoff-view-players = Bheka abadlali
tradeoff-hand-display = Isandla sakho (amadayisi angu-{ $count }): { $dice }
tradeoff-pool-display = Isizinda (amadayisi angu-{ $count }): { $dice }
tradeoff-player-info = { $player }: { $hand }. Kushintshanisiwe: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. Akushintshanisanga lutho.

# Error messages
tradeoff-not-trading-phase = Akukho esigabeni sokushintshanisa.
tradeoff-not-taking-phase = Akukho esigabeni sokuthatha.
tradeoff-already-confirmed = Sekuqinisekisiwe.
tradeoff-no-die = Alikho idayisi elishintshayo.
tradeoff-no-more-takes = Awusekho ukuthatha okutholakalayo.
tradeoff-not-in-pool = Lelo dayisi alikhona esizindeni.

# Options
tradeoff-set-target = Amaphuzu ahlosiwe: { $score }
tradeoff-enter-target = Faka amaphuzu ahlosiwe:
tradeoff-option-changed-target = Amaphuzu ahlosiwe asetelwe ku-{ $score }.
