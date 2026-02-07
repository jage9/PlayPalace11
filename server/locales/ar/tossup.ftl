# Toss Up game messages

# Game info
game-name-tossup = رمية
tossup-category = ألعاب النرد

# Actions
tossup-roll-first = ارمِ { $count } { $count ->
    [zero] زهر
    [one] زهراً
    [two] زهرين
    [few] أزهر
    [many] زهراً
   *[other] زهر
}
tossup-roll-remaining = ارمِ { $count } { $count ->
    [zero] زهر متبقي
    [one] زهراً متبقياً
    [two] زهرين متبقيين
    [few] أزهر متبقية
    [many] زهراً متبقياً
   *[other] زهر متبقي
}
tossup-bank = ادخر { $points } نقطة

# Game events
tossup-turn-start = دور { $player }. النتيجة: { $score }
tossup-you-roll = رميت: { $results }.
tossup-player-rolls = { $player } رمى: { $results }.

# Turn status
tossup-you-have-points = نقاط الدور: { $turn_points }. نرد متبقي: { $dice_count }.
tossup-player-has-points = { $player } لديه { $turn_points } نقطة دور. { $dice_count } نرد متبقي.

# Fresh dice
tossup-you-get-fresh = لا يوجد نرد متبقي! الحصول على { $count } نرد جديد.
tossup-player-gets-fresh = { $player } يحصل على { $count } نرد جديد.

# Bust
tossup-you-bust = إفلاس! تخسر { $points } نقطة لهذا الدور.
tossup-player-busts = { $player } أفلس ويخسر { $points } نقطة!

# Bank
tossup-you-bank = تدخر { $points } نقطة. المجموع الكلي: { $total }.
tossup-player-banks = { $player } يدخر { $points } نقطة. المجموع الكلي: { $total }.

# Winner
tossup-winner = { $player } يفوز بـ { $score } نقطة!
tossup-tie-tiebreaker = إنه تعادل بين { $players }! جولة حاسمة!

# Options
tossup-set-rules-variant = متغير القواعد: { $variant }
tossup-select-rules-variant = اختر متغير القواعد:
tossup-option-changed-rules = تم تغيير متغير القواعد إلى { $variant }

tossup-set-starting-dice = نرد البداية: { $count }
tossup-enter-starting-dice = أدخل عدد نرد البداية:
tossup-option-changed-dice = تم تغيير نرد البداية إلى { $count }

# Rules variants
tossup-rules-standard = قياسي
tossup-rules-playpalace = بلاي بالاس

# Rules explanations
tossup-rules-standard-desc = 3 أخضر، 2 أصفر، 1 أحمر لكل زهر. إفلاس إذا لم يكن هناك أخضر وعلى الأقل أحمر واحد.
tossup-rules-playpalace-desc = توزيع متساوٍ. إفلاس إذا كان كل النرد أحمر.

# Disabled reasons
tossup-need-points = تحتاج إلى نقاط للادخار.
