# Pirates of the Lost Seas game messages

# Game name
game-name-pirates = قراصنة البحار المفقودة

# Game start and setup
pirates-welcome = مرحباً بك في قراصنة البحار المفقودة! أبحر في البحار، اجمع الأحجار الكريمة، وقاتل القراصنة الآخرين!
pirates-oceans = رحلتك ستأخذك عبر: { $oceans }
pirates-gems-placed = { $total } أحجار كريمة متناثرة عبر البحار. اعثر عليها جميعاً!
pirates-golden-moon = القمر الذهبي يطلع! جميع مكاسب الخبرة مضاعفة ثلاث مرات هذه الجولة!

# Turn announcements
pirates-turn = دور { $player }. الموضع { $position }

# Movement actions
pirates-move-left = أبحر يساراً
pirates-move-right = أبحر يميناً
pirates-move-2-left = أبحر مربعين يساراً
pirates-move-2-right = أبحر مربعين يميناً
pirates-move-3-left = أبحر 3 مربعات يساراً
pirates-move-3-right = أبحر 3 مربعات يميناً

# Movement messages
pirates-move-you = أنت تبحر { $direction } إلى الموضع { $position }.
pirates-move-you-tiles = أنت تبحر { $tiles } مربع { $direction } إلى الموضع { $position }.
pirates-move = { $player } يبحر { $direction } إلى الموضع { $position }.
pirates-map-edge = لا يمكنك الإبحار أكثر. أنت في الموضع { $position }.

# Position and status
pirates-check-status = تحقق من الحالة
pirates-check-position = تحقق من الموضع
pirates-check-moon = تحقق من سطوع القمر
pirates-your-position = موضعك: { $position } في { $ocean }
pirates-moon-brightness = القمر الذهبي ساطع بنسبة { $brightness }%. ({ $collected } من { $total } أحجار كريمة تم جمعها).
pirates-no-golden-moon = لا يمكن رؤية القمر الذهبي في السماء الآن.

# Gem collection
pirates-gem-found-you = وجدت { $gem }! تساوي { $value } نقطة.
pirates-gem-found = { $player } وجد { $gem }! تساوي { $value } نقطة.
pirates-all-gems-collected = تم جمع جميع الأحجار الكريمة!

# Winner
pirates-winner = { $player } يفوز بـ { $score } نقطة!

# Skills menu
pirates-use-skill = استخدم مهارة
pirates-select-skill = اختر مهارة للاستخدام

# Combat - Attack initiation
pirates-cannonball = أطلق كرة مدفع
pirates-no-targets = لا توجد أهداف ضمن { $range } مربع.
pirates-attack-you-fire = أنت تطلق كرة مدفع على { $target }!
pirates-attack-incoming = { $attacker } يطلق كرة مدفع عليك!
pirates-attack-fired = { $attacker } يطلق كرة مدفع على { $defender }!

# Combat - Rolls
pirates-attack-roll = رمية الهجوم: { $roll }
pirates-attack-bonus = مكافأة الهجوم: +{ $bonus }
pirates-defense-roll = رمية الدفاع: { $roll }
pirates-defense-roll-others = { $player } يرمي { $roll } للدفاع.
pirates-defense-bonus = مكافأة الدفاع: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = إصابة مباشرة! لقد ضربت { $target }!
pirates-attack-hit-them = لقد أصابك { $attacker }!
pirates-attack-hit = { $attacker } يصيب { $defender }!

# Combat - Miss results
pirates-attack-miss-you = كرة مدفعك أخطأت { $target }.
pirates-attack-miss-them = كرة المدفع أخطأتك!
pirates-attack-miss = كرة مدفع { $attacker } تخطئ { $defender }.

# Combat - Push
pirates-push-you = أنت تدفع { $target } { $direction } إلى الموضع { $position }!
pirates-push-them = { $attacker } يدفعك { $direction } إلى الموضع { $position }!
pirates-push = { $attacker } يدفع { $defender } { $direction } من { $old_pos } إلى { $new_pos }.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } يحاول سرقة حجر كريم!
pirates-steal-rolls = رمية السرقة: { $steal } ضد الدفاع: { $defend }
pirates-steal-success-you = سرقت { $gem } من { $target }!
pirates-steal-success-them = { $attacker } سرق { $gem } منك!
pirates-steal-success = { $attacker } يسرق { $gem } من { $defender }!
pirates-steal-failed = فشلت محاولة السرقة!

# XP and Leveling
pirates-xp-gained = +{ $xp } خبرة
pirates-level-up = { $player } وصل إلى المستوى { $level }!
pirates-level-up-you = وصلت إلى المستوى { $level }!
pirates-level-up-multiple = { $player } كسب { $levels } مستويات! الآن المستوى { $level }!
pirates-level-up-multiple-you = كسبت { $levels } مستويات! الآن المستوى { $level }!
pirates-skills-unlocked = { $player } فتح مهارات جديدة: { $skills }.
pirates-skills-unlocked-you = فتحت مهارات جديدة: { $skills }.

# Skill activation
pirates-skill-activated = { $player } ينشط { $skill }!
pirates-buff-expired = تأثير { $skill } لـ { $player } انتهى.

# Sword Fighter skill
pirates-sword-fighter-activated = مقاتل السيف مفعل! +4 مكافأة هجوم لـ { $turns } دور.

# Push skill (defense buff)
pirates-push-activated = الدفع مفعل! +3 مكافأة دفاع لـ { $turns } دور.

# Skilled Captain skill
pirates-skilled-captain-activated = القبطان الماهر مفعل! +2 هجوم و +2 دفاع لـ { $turns } دور.

# Double Devastation skill
pirates-double-devastation-activated = الدمار المزدوج مفعل! نطاق الهجوم زاد إلى 10 مربعات لـ { $turns } دور.

# Battleship skill
pirates-battleship-activated = سفينة حربية مفعلة! يمكنك إطلاق طلقتين هذا الدور!
pirates-battleship-no-targets = لا توجد أهداف للطلقة { $shot }.
pirates-battleship-shot = إطلاق الطلقة { $shot }...

# Portal skill
pirates-portal-no-ships = لا توجد سفن أخرى في الأفق للانتقال إليها.
pirates-portal-fizzle = بوابة { $player } تتلاشى بدون وجهة.
pirates-portal-success = { $player } ينتقل إلى { $ocean } في الموضع { $position }!

# Gem Seeker skill
pirates-gem-seeker-reveal = البحار تهمس عن { $gem } في الموضع { $position }. ({ $uses } استخدامات متبقية)

# Level requirements
pirates-requires-level-15 = يتطلب المستوى 15
pirates-requires-level-150 = يتطلب المستوى 150

# XP Multiplier options
pirates-set-combat-xp-multiplier = مضاعف خبرة القتال: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = الخبرة للقتال
pirates-set-find-gem-xp-multiplier = مضاعف خبرة إيجاد الأحجار: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = الخبرة لإيجاد حجر كريم

# Gem stealing options
pirates-set-gem-stealing = سرقة الأحجار: { $mode }
pirates-select-gem-stealing = اختر وضع سرقة الأحجار
pirates-option-changed-stealing = تم تعيين سرقة الأحجار إلى { $mode }.

# Gem stealing mode choices
pirates-stealing-with-bonus = مع مكافأة الرمية
pirates-stealing-no-bonus = بدون مكافأة الرمية
pirates-stealing-disabled = معطل
