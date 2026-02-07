# Chaos Bear game messages

# Game name
game-name-chaosbear = دب الفوضى

# Actions
chaosbear-roll-dice = ارمِ النرد
chaosbear-draw-card = اسحب ورقة
chaosbear-check-status = تحقق من الحالة

# Game intro (3 separate messages like v10)
chaosbear-intro-1 = بدأ دب الفوضى! جميع اللاعبين يبدأون 30 مربعاً أمام الدب.
chaosbear-intro-2 = ارمِ النرد للتحرك للأمام، واسحب الأوراق عند مضاعفات 5 للحصول على تأثيرات خاصة.
chaosbear-intro-3 = لا تدع الدب يمسك بك!

# Turn announcement
chaosbear-turn = دور { $player }؛ المربع { $position }.

# Rolling
chaosbear-roll = { $player } رمى { $roll }.
chaosbear-position = { $player } الآن في المربع { $position }.

# Drawing cards
chaosbear-draws-card = { $player } يسحب ورقة.
chaosbear-card-impulsion = دفع! { $player } يتحرك للأمام 3 مربعات إلى المربع { $position }!
chaosbear-card-super-impulsion = دفع فائق! { $player } يتحرك للأمام 5 مربعات إلى المربع { $position }!
chaosbear-card-tiredness = تعب! طاقة الدب ناقص 1. لديه الآن { $energy } طاقة.
chaosbear-card-hunger = جوع! طاقة الدب زائد 1. لديه الآن { $energy } طاقة.
chaosbear-card-backward = دفع للخلف! { $player } يعود إلى المربع { $position }.
chaosbear-card-random-gift = هدية عشوائية!
chaosbear-gift-back = { $player } عاد إلى المربع { $position }.
chaosbear-gift-forward = { $player } تقدم إلى المربع { $position }!

# Bear turn
chaosbear-bear-roll = الدب رمى { $roll } + طاقته { $energy } = { $total }.
chaosbear-bear-energy-up = الدب رمى 3 وكسب 1 طاقة!
chaosbear-bear-position = الدب الآن في المربع { $position }!
chaosbear-player-caught = الدب أمسك { $player }! تم هزيمة { $player }!
chaosbear-bear-feast = الدب يخسر 3 طاقة بعد التهام لحمهم!

# Status check
chaosbear-status-player-alive = { $player }: المربع { $position }.
chaosbear-status-player-caught = { $player }: تم الإمساك به في المربع { $position }.
chaosbear-status-bear = الدب في المربع { $position } بطاقة { $energy }.

# End game
chaosbear-winner = { $player } نجا وفاز! وصل إلى المربع { $position }!
chaosbear-tie = إنه تعادل في المربع { $position }!

# Disabled action reasons
chaosbear-you-are-caught = لقد أمسك بك الدب.
chaosbear-not-on-multiple = يمكنك فقط سحب الأوراق عند مضاعفات 5.
