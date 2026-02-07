# Farkle game messages

# Game info
game-name-farkle = فاركل

# Actions - Roll and Bank
farkle-roll = ارمِ { $count } { $count ->
    [zero] زهر
    [one] زهراً
    [two] زهرين
    [few] أزهر
    [many] زهراً
   *[other] زهر
}
farkle-bank = ادخر { $points } نقطة

# Scoring combination actions
farkle-take-single-one = 1 واحد بـ { $points } نقطة
farkle-take-single-five = 5 واحد بـ { $points } نقطة
farkle-take-three-kind = ثلاثة { $number }s بـ { $points } نقطة
farkle-take-four-kind = أربعة { $number }s بـ { $points } نقطة
farkle-take-five-kind = خمسة { $number }s بـ { $points } نقطة
farkle-take-six-kind = ستة { $number }s بـ { $points } نقطة
farkle-take-small-straight = سلسلة صغيرة بـ { $points } نقطة
farkle-take-large-straight = سلسلة كبيرة بـ { $points } نقطة
farkle-take-three-pairs = ثلاثة أزواج بـ { $points } نقطة
farkle-take-double-triplets = ثلاثيات مزدوجة بـ { $points } نقطة
farkle-take-full-house = فل هاوس بـ { $points } نقطة

# Game events
farkle-rolls = { $player } يرمي { $count } { $count ->
    [zero] زهر
    [one] زهراً
    [two] زهرين
    [few] أزهر
    [many] زهراً
   *[other] زهر
}...
farkle-you-roll = أنت ترمي { $count } { $count ->
    [zero] زهر
    [one] زهراً
    [two] زهرين
    [few] أزهر
    [many] زهراً
   *[other] زهر
}...
farkle-roll-result = { $dice }
farkle-farkle = فاركل! { $player } يخسر { $points } نقطة
farkle-you-farkle = فاركل! أنت تخسر { $points } نقطة
farkle-takes-combo = { $player } يأخذ { $combo } بـ { $points } نقطة
farkle-you-take-combo = أنت تأخذ { $combo } بـ { $points } نقطة
farkle-hot-dice = نرد ساخن!
farkle-banks = { $player } يدخر { $points } نقطة بمجموع { $total }
farkle-you-bank = أنت تدخر { $points } نقطة بمجموع { $total }
farkle-winner = { $player } يفوز بـ { $score } نقطة!
farkle-you-win = أنت تفوز بـ { $score } نقطة!
farkle-winners-tie = لدينا تعادل! الفائزون: { $players }

# Check turn score action
farkle-turn-score = { $player } لديه { $points } نقطة هذا الدور.
farkle-no-turn = لا أحد يأخذ دوراً حالياً.

# Farkle-specific options
farkle-set-target-score = النتيجة المستهدفة: { $score }
farkle-enter-target-score = أدخل النتيجة المستهدفة (500-5000):
farkle-option-changed-target = تم تعيين النتيجة المستهدفة إلى { $score }.

# Disabled action reasons
farkle-must-take-combo = يجب أن تأخذ مجموعة تسجيل أولاً.
farkle-cannot-bank = لا يمكنك الادخار الآن.
