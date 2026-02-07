# Scopa game messages

# Game name
game-name-scopa = سكوبا

# Game events
scopa-initial-table = أوراق الطاولة: { $cards }
scopa-no-initial-table = لا توجد أوراق على الطاولة للبدء.
scopa-you-collect = أنت تجمع { $cards } بـ { $card }
scopa-player-collects = { $player } يجمع { $cards } بـ { $card }
scopa-you-put-down = أنت تضع { $card }.
scopa-player-puts-down = { $player } يضع { $card }.
scopa-scopa-suffix =  - سكوبا!
scopa-clear-table-suffix = ، مسح الطاولة.
scopa-remaining-cards = { $player } يحصل على الأوراق المتبقية على الطاولة.
scopa-scoring-round = جولة التسجيل...
scopa-most-cards = { $player } يسجل 1 نقطة لأكثر الأوراق ({ $count } ورقة).
scopa-most-cards-tie = أكثر الأوراق تعادل - لم تُمنح نقطة.
scopa-most-diamonds = { $player } يسجل 1 نقطة لأكثر الماسات ({ $count } ماسة).
scopa-most-diamonds-tie = أكثر الماسات تعادل - لم تُمنح نقطة.
scopa-seven-diamonds = { $player } يسجل 1 نقطة لـ 7 الماس.
scopa-seven-diamonds-multi = { $player } يسجل 1 نقطة لأكثر 7 الماسات ({ $count } × 7 الماس).
scopa-seven-diamonds-tie = 7 الماس تعادل - لم تُمنح نقطة.
scopa-most-sevens = { $player } يسجل 1 نقطة لأكثر السبعات ({ $count } سبعة).
scopa-most-sevens-tie = أكثر السبعات تعادل - لم تُمنح نقطة.
scopa-round-scores = نتائج الجولة:
scopa-round-score-line = { $player }: +{ $round_score } (المجموع: { $total_score })
scopa-table-empty = لا توجد أوراق على الطاولة.
scopa-no-such-card = لا توجد ورقة في هذا الموضع.
scopa-captured-count = لقد جمعت { $count } ورقة

# View actions
scopa-view-table = شاهد الطاولة
scopa-view-captured = شاهد المجموع

# Scopa-specific options
scopa-enter-target-score = أدخل النتيجة المستهدفة (1-121)
scopa-set-cards-per-deal = الأوراق لكل توزيع: { $cards }
scopa-enter-cards-per-deal = أدخل الأوراق لكل توزيع (1-10)
scopa-set-decks = عدد المجموعات: { $decks }
scopa-enter-decks = أدخل عدد المجموعات (1-6)
scopa-toggle-escoba = إسكوبا (المجموع إلى 15): { $enabled }
scopa-toggle-hints = إظهار تلميحات الجمع: { $enabled }
scopa-set-mechanic = آلية السكوبا: { $mechanic }
scopa-select-mechanic = اختر آلية السكوبا
scopa-toggle-instant-win = الفوز الفوري في السكوبا: { $enabled }
scopa-toggle-team-scoring = تجميع أوراق الفريق للتسجيل: { $enabled }
scopa-toggle-inverse = الوضع العكسي (الوصول للهدف = الإقصاء): { $enabled }

# Option change announcements
scopa-option-changed-cards = تم تعيين الأوراق لكل توزيع إلى { $cards }.
scopa-option-changed-decks = تم تعيين عدد المجموعات إلى { $decks }.
scopa-option-changed-escoba = إسكوبا { $enabled }.
scopa-option-changed-hints = تلميحات الجمع { $enabled }.
scopa-option-changed-mechanic = تم تعيين آلية السكوبا إلى { $mechanic }.
scopa-option-changed-instant = الفوز الفوري في السكوبا { $enabled }.
scopa-option-changed-team-scoring = تسجيل أوراق الفريق { $enabled }.
scopa-option-changed-inverse = الوضع العكسي { $enabled }.

# Scopa mechanic choices
scopa-mechanic-normal = عادي
scopa-mechanic-no_scopas = بدون سكوباس
scopa-mechanic-only_scopas = سكوباس فقط

# Disabled action reasons
scopa-timer-not-active = مؤقت الجولة غير نشط.

# Validation errors
scopa-error-not-enough-cards = لا توجد أوراق كافية في { $decks } { $decks ->
    [zero] مجموعة
    [one] مجموعة
    [two] مجموعتين
    [few] مجموعات
    [many] مجموعة
   *[other] مجموعة
} لـ { $players } { $players ->
    [zero] لاعب
    [one] لاعب
    [two] لاعبين
    [few] لاعبين
    [many] لاعباً
   *[other] لاعب
} مع { $cards_per_deal } ورقة لكل منهم. (بحاجة إلى { $cards_per_deal } × { $players } = { $cards_needed } ورقة، لكن لديك فقط { $total_cards }.)
