# Tradeoff game messages

# Game info
game-name-tradeoff = مقايضة

# Round and iteration flow
tradeoff-round-start = الجولة { $round }.
tradeoff-iteration = اليد { $iteration } من 3.

# Phase 1: Trading
tradeoff-you-rolled = رميت: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = المقايضة
tradeoff-trade-status-keeping = الاحتفاظ
tradeoff-confirm-trades = تأكيد المقايضات ({ $count } نرد)
tradeoff-keeping = الاحتفاظ بـ { $value }.
tradeoff-trading = مقايضة { $value }.
tradeoff-player-traded = { $player } قايض: { $dice }.
tradeoff-player-traded-none = { $player } احتفظ بكل النرد.

# Phase 2: Taking from pool
tradeoff-your-turn-take = دورك لأخذ زهر من المجموعة.
tradeoff-take-die = خذ { $value } ({ $remaining } متبقي)
tradeoff-you-take = أنت تأخذ { $value }.
tradeoff-player-takes = { $player } يأخذ { $value }.

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points } نقطة): { $sets }.
tradeoff-no-sets = { $player }: لا توجد مجموعات.

# Set descriptions
tradeoff-set-triple = ثلاثي من { $value }s
tradeoff-set-group = مجموعة من { $value }s
tradeoff-set-mini-straight = سلسلة صغيرة { $low }-{ $high }
tradeoff-set-double-triple = ثلاثي مزدوج ({ $v1 }s و { $v2 }s)
tradeoff-set-straight = سلسلة { $low }-{ $high }
tradeoff-set-double-group = مجموعة مزدوجة ({ $v1 }s و { $v2 }s)
tradeoff-set-all-groups = كل المجموعات
tradeoff-set-all-triplets = كل الثلاثيات

# Round end
tradeoff-round-scores = نتائج الجولة { $round }:
tradeoff-score-line = { $player }: +{ $round_points } (المجموع: { $total })
tradeoff-leader = { $player } يتصدر بـ { $score }.

# Game end
tradeoff-winner = { $player } يفوز بـ { $score } نقطة!
tradeoff-winners-tie = إنه تعادل! { $players } تعادلوا بـ { $score } نقطة!

# Status checks
tradeoff-view-hand = شاهد يدك
tradeoff-view-pool = شاهد المجموعة
tradeoff-view-players = شاهد اللاعبين
tradeoff-hand-display = يدك ({ $count } نرد): { $dice }
tradeoff-pool-display = المجموعة ({ $count } نرد): { $dice }
tradeoff-player-info = { $player }: { $hand }. قايض: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. لم يقايض شيئاً.

# Error messages
tradeoff-not-trading-phase = ليس في مرحلة المقايضة.
tradeoff-not-taking-phase = ليس في مرحلة الأخذ.
tradeoff-already-confirmed = تم التأكيد بالفعل.
tradeoff-no-die = لا يوجد زهر للتبديل.
tradeoff-no-more-takes = لا مزيد من الأخذات المتاحة.
tradeoff-not-in-pool = هذا الزهر ليس في المجموعة.

# Options
tradeoff-set-target = النتيجة المستهدفة: { $score }
tradeoff-enter-target = أدخل النتيجة المستهدفة:
tradeoff-option-changed-target = تم تعيين النتيجة المستهدفة إلى { $score }.
