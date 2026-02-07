# Ninety Nine - English Localization

# Game info
ninetynine-name = تسعة وتسعون
ninetynine-description = لعبة ورق حيث يحاول اللاعبون تجنب دفع المجموع الجاري فوق 99. آخر لاعب واقف يفوز!

# Round
ninetynine-round = الجولة { $round }.

# Turn
ninetynine-player-turn = دور { $player }.

# Playing cards
ninetynine-you-play = أنت تلعب { $card }. العدد الآن { $count }.
ninetynine-player-plays = { $player } يلعب { $card }. العدد الآن { $count }.

# Direction reverse
ninetynine-direction-reverses = اتجاه اللعب ينعكس!

# Skip
ninetynine-player-skipped = تم تخطي { $player }.

# Token loss
ninetynine-you-lose-tokens = تخسر { $amount } { $amount ->
    [zero] رمز
    [one] رمزاً
    [two] رمزين
    [few] رموز
    [many] رمزاً
   *[other] رمز
}.
ninetynine-player-loses-tokens = { $player } يخسر { $amount } { $amount ->
    [zero] رمز
    [one] رمزاً
    [two] رمزين
    [few] رموز
    [many] رمزاً
   *[other] رمز
}.

# Elimination
ninetynine-player-eliminated = تم إقصاء { $player }!

# Game end
ninetynine-player-wins = { $player } يفوز باللعبة!

# Dealing
ninetynine-you-deal = أنت توزع الأوراق.
ninetynine-player-deals = { $player } يوزع الأوراق.

# Drawing cards
ninetynine-you-draw = أنت تسحب { $card }.
ninetynine-player-draws = { $player } يسحب ورقة.

# No valid cards
ninetynine-no-valid-cards = { $player } ليس لديه أوراق لن تتجاوز 99!

# Status - for C key
ninetynine-current-count = العدد هو { $count }.

# Hand check - for H key
ninetynine-hand-cards = أوراقك: { $cards }.
ninetynine-hand-empty = ليس لديك أوراق.

# Ace choice
ninetynine-ace-choice = العب الآس كـ +1 أو +11?
ninetynine-ace-add-eleven = أضف 11
ninetynine-ace-add-one = أضف 1

# Ten choice
ninetynine-ten-choice = العب 10 كـ +10 أو -10?
ninetynine-ten-add = أضف 10
ninetynine-ten-subtract = اطرح 10

# Manual draw
ninetynine-draw-card = اسحب ورقة
ninetynine-draw-prompt = اضغط Space أو D لسحب ورقة.

# Options
ninetynine-set-tokens = رموز البداية: { $tokens }
ninetynine-enter-tokens = أدخل عدد رموز البداية:
ninetynine-option-changed-tokens = تم تعيين رموز البداية إلى { $tokens }.
ninetynine-set-rules = متغير القواعد: { $rules }
ninetynine-select-rules = اختر متغير القواعد
ninetynine-option-changed-rules = تم تعيين متغير القواعد إلى { $rules }.
ninetynine-set-hand-size = حجم اليد: { $size }
ninetynine-enter-hand-size = أدخل حجم اليد:
ninetynine-option-changed-hand-size = تم تعيين حجم اليد إلى { $size }.
ninetynine-set-autodraw = السحب التلقائي: { $enabled }
ninetynine-option-changed-autodraw = تم تعيين السحب التلقائي إلى { $enabled }.

# Rules variant announcements (shown at game start)
ninetynine-rules-quentin = قواعد كوينتن سي.
ninetynine-rules-rsgames = قواعد آر إس جيمز.

# Rules variant choices (for menu display)
ninetynine-rules-variant-quentin_c = كوينتن سي
ninetynine-rules-variant-rs_games = آر إس جيمز

# Disabled action reasons
ninetynine-choose-first = تحتاج إلى اتخاذ اختيار أولاً.
ninetynine-draw-first = تحتاج إلى سحب ورقة أولاً.
