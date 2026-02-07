# Messages for Left Right Center (Arabic)

# Game name
game-name-leftrightcenter = يسار يمين وسط

# Actions
lrc-roll = ارمِ { $count } { $count ->
    [zero] زهر
    [one] زهراً
    [two] زهرين
    [few] أزهر
    [many] زهراً
   *[other] زهر
}

# Dice faces
lrc-face-left = يسار
lrc-face-right = يمين
lrc-face-center = وسط
lrc-face-dot = نقطة

# Game events
lrc-roll-results = { $player } رمى { $results }.
lrc-pass-left = { $player } يمرر { $count } { $count ->
    [zero] رقاقة
    [one] رقاقة
    [two] رقاقتين
    [few] رقائق
    [many] رقاقة
   *[other] رقاقة
} إلى { $target }.
lrc-pass-right = { $player } يمرر { $count } { $count ->
    [zero] رقاقة
    [one] رقاقة
    [two] رقاقتين
    [few] رقائق
    [many] رقاقة
   *[other] رقاقة
} إلى { $target }.
lrc-pass-center = { $player } يضع { $count } { $count ->
    [zero] رقاقة
    [one] رقاقة
    [two] رقاقتين
    [few] رقائق
    [many] رقاقة
   *[other] رقاقة
} في الوسط.
lrc-no-chips = { $player } ليس لديه رقائق للرمي.
lrc-center-pot = { $count } { $count ->
    [zero] رقاقة
    [one] رقاقة
    [two] رقاقتان
    [few] رقائق
    [many] رقاقة
   *[other] رقاقة
} في الوسط.
lrc-player-chips = { $player } لديه الآن { $count } { $count ->
    [zero] رقاقة
    [one] رقاقة
    [two] رقاقتان
    [few] رقائق
    [many] رقاقة
   *[other] رقاقة
}.
lrc-winner = { $player } يفوز بـ { $count } { $count ->
    [zero] رقاقة
    [one] رقاقة
    [two] رقاقتين
    [few] رقائق
    [many] رقاقة
   *[other] رقاقة
}!

# Options
lrc-set-starting-chips = رقائق البداية: { $count }
lrc-enter-starting-chips = أدخل رقائق البداية:
lrc-option-changed-starting-chips = تم تعيين رقائق البداية إلى { $count }.
