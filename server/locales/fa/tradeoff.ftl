# Tradeoff game messages

# Game info
game-name-tradeoff = معامله

# Round and iteration flow
tradeoff-round-start = دور { $round }.
tradeoff-iteration = دست { $iteration } از ۳.

# Phase 1: Trading
tradeoff-you-rolled = شما انداختید: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = معامله
tradeoff-trade-status-keeping = نگه‌داری
tradeoff-confirm-trades = تأیید معاملات ({ $count } تاس)
tradeoff-keeping = نگه‌داری { $value }.
tradeoff-trading = معامله { $value }.
tradeoff-player-traded = { $player } معامله کرد: { $dice }.
tradeoff-player-traded-none = { $player } همه تاس‌ها را نگه داشت.

# Phase 2: Taking from pool
tradeoff-your-turn-take = نوبت شماست که یک تاس از مخزن بردارید.
tradeoff-take-die = برداشتن یک { $value } ({ $remaining } باقی‌مانده)
tradeoff-you-take = شما یک { $value } برمی‌دارید.
tradeoff-player-takes = { $player } یک { $value } برمی‌دارد.

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points } امتیاز): { $sets }.
tradeoff-no-sets = { $player }: بدون ست.

# Set descriptions (concise)
tradeoff-set-triple = سه‌تایی { $value }
tradeoff-set-group = گروه { $value }
tradeoff-set-mini-straight = ترتیب کوچک { $low }-{ $high }
tradeoff-set-double-triple = سه‌تایی دوبل ({ $v1 } و { $v2 })
tradeoff-set-straight = ترتیب { $low }-{ $high }
tradeoff-set-double-group = گروه دوبل ({ $v1 } و { $v2 })
tradeoff-set-all-groups = همه گروه‌ها
tradeoff-set-all-triplets = همه سه‌تایی‌ها

# Round end
tradeoff-round-scores = امتیازات دور { $round }:
tradeoff-score-line = { $player }: +{ $round_points } (مجموع: { $total })
tradeoff-leader = { $player } با { $score } در صدر است.

# Game end
tradeoff-winner = { $player } با { $score } امتیاز برنده می‌شود!
tradeoff-winners-tie = مساوی! { $players } با { $score } امتیاز مساوی شدند!

# Status checks
tradeoff-view-hand = مشاهده دست شما
tradeoff-view-pool = مشاهده مخزن
tradeoff-view-players = مشاهده بازیکنان
tradeoff-hand-display = دست شما ({ $count } تاس): { $dice }
tradeoff-pool-display = مخزن ({ $count } تاس): { $dice }
tradeoff-player-info = { $player }: { $hand }. معامله شده: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. هیچ معامله‌ای نشد.

# Error messages
tradeoff-not-trading-phase = در مرحله معامله نیست.
tradeoff-not-taking-phase = در مرحله برداشت نیست.
tradeoff-already-confirmed = قبلاً تأیید شده است.
tradeoff-no-die = تاسی برای تغییر وجود ندارد.
tradeoff-no-more-takes = دیگر برداشتی ممکن نیست.
tradeoff-not-in-pool = آن تاس در مخزن نیست.

# Options
tradeoff-set-target = امتیاز هدف: { $score }
tradeoff-enter-target = امتیاز هدف را وارد کنید:
tradeoff-option-changed-target = امتیاز هدف به { $score } تنظیم شد.
