# Tradeoff game messages

# Game info
game-name-tradeoff = Tradeoff

# Round and iteration flow
tradeoff-round-start = Ronde { $round }.
tradeoff-iteration = Tangan { $iteration } dari 3.

# Phase 1: Trading
tradeoff-you-rolled = Anda melempar: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = menukar
tradeoff-trade-status-keeping = menyimpan
tradeoff-confirm-trades = Konfirmasi tukar ({ $count } dadu)
tradeoff-keeping = Menyimpan { $value }.
tradeoff-trading = Menukar { $value }.
tradeoff-player-traded = { $player } menukar: { $dice }.
tradeoff-player-traded-none = { $player } menyimpan semua dadu.

# Phase 2: Taking from pool
tradeoff-your-turn-take = Giliran Anda untuk mengambil dadu dari pool.
tradeoff-take-die = Ambil { $value } ({ $remaining } tersisa)
tradeoff-you-take = Anda mengambil { $value }.
tradeoff-player-takes = { $player } mengambil { $value }.

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points } poin): { $sets }.
tradeoff-no-sets = { $player }: tidak ada set.

# Set descriptions (concise)
tradeoff-set-triple = triple { $value }
tradeoff-set-group = grup { $value }
tradeoff-set-mini-straight = mini straight { $low }-{ $high }
tradeoff-set-double-triple = triple ganda ({ $v1 } dan { $v2 })
tradeoff-set-straight = straight { $low }-{ $high }
tradeoff-set-double-group = grup ganda ({ $v1 } dan { $v2 })
tradeoff-set-all-groups = semua grup
tradeoff-set-all-triplets = semua triplet

# Round end
tradeoff-round-scores = Skor ronde { $round }:
tradeoff-score-line = { $player }: +{ $round_points } (total: { $total })
tradeoff-leader = { $player } memimpin dengan { $score }.

# Game end
tradeoff-winner = { $player } menang dengan { $score } poin!
tradeoff-winners-tie = Seri! { $players } seri dengan { $score } poin!

# Status checks
tradeoff-view-hand = Lihat tangan Anda
tradeoff-view-pool = Lihat pool
tradeoff-view-players = Lihat pemain
tradeoff-hand-display = Tangan Anda ({ $count } dadu): { $dice }
tradeoff-pool-display = Pool ({ $count } dadu): { $dice }
tradeoff-player-info = { $player }: { $hand }. Ditukar: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. Tidak menukar apa pun.

# Error messages
tradeoff-not-trading-phase = Tidak dalam fase tukar.
tradeoff-not-taking-phase = Tidak dalam fase ambil.
tradeoff-already-confirmed = Sudah dikonfirmasi.
tradeoff-no-die = Tidak ada dadu untuk toggle.
tradeoff-no-more-takes = Tidak ada lagi pengambilan yang tersedia.
tradeoff-not-in-pool = Dadu itu tidak ada di pool.

# Options
tradeoff-set-target = Skor target: { $score }
tradeoff-enter-target = Masukkan skor target:
tradeoff-option-changed-target = Skor target diatur ke { $score }.
