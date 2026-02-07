# Yahtzee game messages

# Game info
game-name-yahtzee = يات زي

# Actions - Rolling
yahtzee-roll = إعادة رمي ({ $count } متبقي)
yahtzee-roll-all = ارمِ النرد

# Upper section scoring categories
yahtzee-score-ones = واحدات بـ { $points } نقطة
yahtzee-score-twos = اثنينات بـ { $points } نقطة
yahtzee-score-threes = ثلاثات بـ { $points } نقطة
yahtzee-score-fours = أربعات بـ { $points } نقطة
yahtzee-score-fives = خمسات بـ { $points } نقطة
yahtzee-score-sixes = ستات بـ { $points } نقطة

# Lower section scoring categories
yahtzee-score-three-kind = ثلاثة من نوع بـ { $points } نقطة
yahtzee-score-four-kind = أربعة من نوع بـ { $points } نقطة
yahtzee-score-full-house = فل هاوس بـ { $points } نقطة
yahtzee-score-small-straight = سلسلة صغيرة بـ { $points } نقطة
yahtzee-score-large-straight = سلسلة كبيرة بـ { $points } نقطة
yahtzee-score-yahtzee = يات زي بـ { $points } نقطة
yahtzee-score-chance = فرصة بـ { $points } نقطة

# Game events
yahtzee-you-rolled = رميت: { $dice }. رميات متبقية: { $remaining }
yahtzee-player-rolled = { $player } رمى: { $dice }. رميات متبقية: { $remaining }

# Scoring announcements
yahtzee-you-scored = سجلت { $points } نقطة في { $category }.
yahtzee-player-scored = { $player } سجل { $points } في { $category }.

# Yahtzee bonus
yahtzee-you-bonus = مكافأة يات زي! +100 نقطة
yahtzee-player-bonus = { $player } حصل على مكافأة يات زي! +100 نقطة

# Upper section bonus
yahtzee-you-upper-bonus = مكافأة القسم العلوي! +35 نقطة ({ $total } في القسم العلوي)
yahtzee-player-upper-bonus = { $player } حصل على مكافأة القسم العلوي! +35 نقطة
yahtzee-you-upper-bonus-missed = فاتتك مكافأة القسم العلوي ({ $total } في القسم العلوي، كنت بحاجة إلى 63).
yahtzee-player-upper-bonus-missed = { $player } فاتته مكافأة القسم العلوي.

# Scoring mode
yahtzee-choose-category = اختر فئة للتسجيل فيها.
yahtzee-continuing = متابعة الدور.

# Status checks
yahtzee-check-scoresheet = تحقق من بطاقة النتائج
yahtzee-view-dice = تحقق من اليد
yahtzee-your-dice = نردك: { $dice }.
yahtzee-your-dice-kept = نردك: { $dice }. الاحتفاظ بـ: { $kept }
yahtzee-not-rolled = لم ترمِ بعد.

# Scoresheet display
yahtzee-scoresheet-header = === بطاقة نتائج { $player } ===
yahtzee-scoresheet-upper = القسم العلوي:
yahtzee-scoresheet-lower = القسم السفلي:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = المجموع العلوي: { $total } (مكافأة: +35)
yahtzee-scoresheet-upper-total-needed = المجموع العلوي: { $total } ({ $needed } أخرى للمكافأة)
yahtzee-scoresheet-yahtzee-bonus = مكافآت يات زي: { $count } × 100 = { $total }
yahtzee-scoresheet-grand-total = المجموع الكلي: { $total }

# Category names (for announcements)
yahtzee-category-ones = واحدات
yahtzee-category-twos = اثنينات
yahtzee-category-threes = ثلاثات
yahtzee-category-fours = أربعات
yahtzee-category-fives = خمسات
yahtzee-category-sixes = ستات
yahtzee-category-three-kind = ثلاثة من نوع
yahtzee-category-four-kind = أربعة من نوع
yahtzee-category-full-house = فل هاوس
yahtzee-category-small-straight = سلسلة صغيرة
yahtzee-category-large-straight = سلسلة كبيرة
yahtzee-category-yahtzee = يات زي
yahtzee-category-chance = فرصة

# Game end
yahtzee-winner = { $player } يفوز بـ { $score } نقطة!
yahtzee-winners-tie = إنه تعادل! { $players } جميعهم سجلوا { $score } نقطة!

# Options
yahtzee-set-rounds = عدد الألعاب: { $rounds }
yahtzee-enter-rounds = أدخل عدد الألعاب (1-10):
yahtzee-option-changed-rounds = تم تعيين عدد الألعاب إلى { $rounds }.

# Disabled action reasons
yahtzee-no-rolls-left = لا توجد لديك رميات متبقية.
yahtzee-roll-first = تحتاج إلى الرمي أولاً.
yahtzee-category-filled = هذه الفئة ممتلئة بالفعل.
