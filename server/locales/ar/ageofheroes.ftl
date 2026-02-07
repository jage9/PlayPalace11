# Age of Heroes game messages
# A civilization-building card game for 2-6 players

# Game name
game-name-ageofheroes = عصر الأبطال

# Tribes
ageofheroes-tribe-egyptians = المصريون
ageofheroes-tribe-romans = الرومان
ageofheroes-tribe-greeks = اليونانيون
ageofheroes-tribe-babylonians = البابليون
ageofheroes-tribe-celts = الكلت
ageofheroes-tribe-chinese = الصينيون

# Special Resources (for monuments)
ageofheroes-special-limestone = الحجر الجيري
ageofheroes-special-concrete = الخرسانة
ageofheroes-special-marble = الرخام
ageofheroes-special-bricks = الطوب
ageofheroes-special-sandstone = الحجر الرملي
ageofheroes-special-granite = الجرانيت

# Standard Resources
ageofheroes-resource-iron = الحديد
ageofheroes-resource-wood = الخشب
ageofheroes-resource-grain = الحبوب
ageofheroes-resource-stone = الحجر
ageofheroes-resource-gold = الذهب

# Events
ageofheroes-event-population-growth = نمو السكان
ageofheroes-event-earthquake = زلزال
ageofheroes-event-eruption = ثوران بركاني
ageofheroes-event-hunger = جوع
ageofheroes-event-barbarians = البرابرة
ageofheroes-event-olympics = الألعاب الأولمبية
ageofheroes-event-hero = بطل
ageofheroes-event-fortune = حظ

# Buildings
ageofheroes-building-army = جيش
ageofheroes-building-fortress = حصن
ageofheroes-building-general = قائد
ageofheroes-building-road = طريق
ageofheroes-building-city = مدينة

# Actions
ageofheroes-action-tax-collection = جمع الضرائب
ageofheroes-action-construction = البناء
ageofheroes-action-war = حرب
ageofheroes-action-do-nothing = لا تفعل شيئاً
ageofheroes-play = العب

# War goals
ageofheroes-war-conquest = الغزو
ageofheroes-war-plunder = النهب
ageofheroes-war-destruction = الدمار

# Game options
ageofheroes-set-victory-cities = مدن النصر: { $cities }
ageofheroes-enter-victory-cities = أدخل عدد المدن للفوز (3-7)
ageofheroes-set-victory-monument = إكمال النصب التذكاري: { $progress }%
ageofheroes-toggle-neighbor-roads = الطرق للجيران فقط: { $enabled }
ageofheroes-set-max-hand = الحد الأقصى لحجم اليد: { $cards } أوراق

# Option change announcements
ageofheroes-option-changed-victory-cities = النصر يتطلب { $cities } { $cities ->
    [zero] مدن
    [one] مدينة
    [two] مدينتين
    [few] مدن
    [many] مدينة
    *[other] مدينة
}.
ageofheroes-option-changed-victory-monument = تم تعيين حد إكمال النصب التذكاري إلى { $progress }%.
ageofheroes-option-changed-neighbor-roads = الطرق للجيران فقط { $enabled }.
ageofheroes-option-changed-max-hand = تم تعيين الحد الأقصى لحجم اليد إلى { $cards } { $cards ->
    [zero] أوراق
    [one] ورقة
    [two] ورقتين
    [few] أوراق
    [many] ورقة
    *[other] ورقة
}.

# Setup phase
ageofheroes-setup-start = أنت قائد قبيلة { $tribe }. مادة النصب التذكاري الخاصة بك هي { $special }. ارمِ النرد لتحديد ترتيب الدور.
ageofheroes-setup-viewer = اللاعبون يرمون النرد لتحديد ترتيب الدور.
ageofheroes-roll-dice = ارمِ النرد
ageofheroes-war-roll-dice = ارمِ النرد
ageofheroes-dice-result = رميت { $total } ({ $die1 } + { $die2 }).
ageofheroes-dice-result-other = { $player } رمى { $total }.
ageofheroes-dice-tie = تعادل عدة لاعبين بـ { $total }. إعادة الرمي...
ageofheroes-first-player = { $player } رمى الأعلى بـ { $total } ويلعب أولاً.
ageofheroes-first-player-you = بـ { $total } نقطة، أنت تلعب أولاً.

# Preparation phase
ageofheroes-prepare-start = يجب على اللاعبين لعب أوراق الأحداث والتخلص من الكوارث.
ageofheroes-prepare-your-turn = لديك { $count } { $count ->
    [zero] أوراق
    [one] ورقة
    [two] ورقتين
    [few] أوراق
    [many] ورقة
    *[other] ورقة
} للعب أو التخلص منها.
ageofheroes-prepare-done = اكتملت مرحلة التحضير.

# Events played/discarded
ageofheroes-population-growth = { $player } يلعب نمو السكان ويبني مدينة جديدة.
ageofheroes-population-growth-you = تلعب نمو السكان وتبني مدينة جديدة.
ageofheroes-discard-card = { $player } يتخلص من { $card }.
ageofheroes-discard-card-you = تتخلص من { $card }.
ageofheroes-earthquake = زلزال يضرب قبيلة { $player }؛ جيوشهم تدخل مرحلة التعافي.
ageofheroes-earthquake-you = زلزال يضرب قبيلتك؛ جيوشك تدخل مرحلة التعافي.
ageofheroes-eruption = ثوران بركاني يدمر إحدى مدن { $player }.
ageofheroes-eruption-you = ثوران بركاني يدمر إحدى مدنك.

# Disaster effects
ageofheroes-hunger-strikes = يضرب الجوع.
ageofheroes-lose-card-hunger = تخسر { $card }.
ageofheroes-barbarians-pillage = البرابرة يهاجمون موارد { $player }.
ageofheroes-barbarians-attack = البرابرة يهاجمون موارد { $player }.
ageofheroes-barbarians-attack-you = البرابرة يهاجمون مواردك.
ageofheroes-lose-card-barbarians = تخسر { $card }.
ageofheroes-block-with-card = { $player } يصد الكارثة باستخدام { $card }.
ageofheroes-block-with-card-you = تصد الكارثة باستخدام { $card }.

# Targeted disaster cards (Earthquake/Eruption)
ageofheroes-select-disaster-target = اختر هدفاً لـ { $card }.
ageofheroes-no-targets = لا توجد أهداف صالحة متاحة.
ageofheroes-earthquake-strikes-you = { $attacker } يلعب زلزال ضدك. جيوشك معطلة.
ageofheroes-earthquake-strikes = { $attacker } يلعب زلزال ضد { $player }.
ageofheroes-armies-disabled = { $count } { $count ->
    [zero] جيوش
    [one] جيش واحد
    [two] جيشان
    [few] جيوش
    [many] جيشاً
    *[other] جيش
} معطل لدورة واحدة.
ageofheroes-eruption-strikes-you = { $attacker } يلعب ثوران بركاني ضدك. إحدى مدنك مدمرة.
ageofheroes-eruption-strikes = { $attacker } يلعب ثوران بركاني ضد { $player }.
ageofheroes-city-destroyed = مدينة دمرت بسبب الثوران البركاني.

# Fair phase
ageofheroes-fair-start = يبزغ فجر السوق.
ageofheroes-fair-draw-base = تسحب { $count } { $count ->
    [zero] أوراق
    [one] ورقة
    [two] ورقتين
    [few] أوراق
    [many] ورقة
    *[other] ورقة
}.
ageofheroes-fair-draw-roads = تسحب { $count } { $count ->
    [zero] أوراق
    [one] ورقة
    [two] ورقتين
    [few] أوراق
    [many] ورقة
    *[other] ورقة
} إضافية بفضل شبكة طرقك.
ageofheroes-fair-draw-other = { $player } يسحب { $count } { $count ->
    [zero] أوراق
    [one] ورقة
    [two] ورقتين
    [few] أوراق
    [many] ورقة
    *[other] ورقة
}.

# Trading/Auction
ageofheroes-auction-start = تبدأ المزاد.
ageofheroes-offer-trade = عرض للتجارة
ageofheroes-offer-made = { $player } يعرض { $card } مقابل { $wanted }.
ageofheroes-offer-made-you = تعرض { $card } مقابل { $wanted }.
ageofheroes-trade-accepted = { $player } يقبل عرض { $other } ويتاجر { $give } مقابل { $receive }.
ageofheroes-trade-accepted-you = تقبل عرض { $other } وتستلم { $receive }.
ageofheroes-trade-cancelled = { $player } يسحب عرضه لـ { $card }.
ageofheroes-trade-cancelled-you = تسحب عرضك لـ { $card }.
ageofheroes-stop-trading = إيقاف التجارة
ageofheroes-select-request = أنت تعرض { $card }. ماذا تريد في المقابل؟
ageofheroes-cancel = إلغاء
ageofheroes-left-auction = { $player } يغادر.
ageofheroes-left-auction-you = تغادر من السوق.
ageofheroes-any-card = أي ورقة
ageofheroes-cannot-trade-own-special = لا يمكنك تداول مادة النصب التذكاري الخاصة بك.
ageofheroes-resource-not-in-game = هذه المادة الخاصة غير مستخدمة في هذه اللعبة.

# Main play phase
ageofheroes-play-start = مرحلة اللعب.
ageofheroes-day = اليوم { $day }
ageofheroes-draw-card = { $player } يسحب ورقة من المجموعة.
ageofheroes-draw-card-you = تسحب { $card } من المجموعة.
ageofheroes-your-action = ماذا تريد أن تفعل؟

# Tax Collection
ageofheroes-tax-collection = { $player } يختار جمع الضرائب: { $cities } { $cities ->
    [zero] مدن
    [one] مدينة
    [two] مدينتان
    [few] مدن
    [many] مدينة
    *[other] مدينة
} تجمع { $cards } { $cards ->
    [zero] أوراق
    [one] ورقة
    [two] ورقتين
    [few] أوراق
    [many] ورقة
    *[other] ورقة
}.
ageofheroes-tax-collection-you = تختار جمع الضرائب: { $cities } { $cities ->
    [zero] مدن
    [one] مدينة
    [two] مدينتان
    [few] مدن
    [many] مدينة
    *[other] مدينة
} تجمع { $cards } { $cards ->
    [zero] أوراق
    [one] ورقة
    [two] ورقتين
    [few] أوراق
    [many] ورقة
    *[other] ورقة
}.
ageofheroes-tax-no-city = جمع الضرائب: ليس لديك مدن باقية. تخلص من ورقة لسحب واحدة جديدة.
ageofheroes-tax-no-city-done = { $player } يختار جمع الضرائب لكن ليس لديه مدن، لذا يتبادل ورقة.
ageofheroes-tax-no-city-done-you = جمع الضرائب: استبدلت { $card } بورقة جديدة.

# Construction
ageofheroes-construction-menu = ماذا تريد أن تبني؟
ageofheroes-construction-done = { $player } بنى { $article } { $building }.
ageofheroes-construction-done-you = بنيت { $article } { $building }.
ageofheroes-construction-stop = إيقاف البناء
ageofheroes-construction-stopped = قررت إيقاف البناء.
ageofheroes-road-select-neighbor = اختر الجار الذي تريد بناء طريق إليه.
ageofheroes-direction-left = إلى يسارك
ageofheroes-direction-right = إلى يمينك
ageofheroes-road-request-sent = تم إرسال طلب الطريق. في انتظار موافقة الجار.
ageofheroes-road-request-received = { $requester } يطلب إذناً لبناء طريق إلى قبيلتك.
ageofheroes-road-request-denied-you = رفضت طلب الطريق.
ageofheroes-road-request-denied = { $denier } رفض طلب الطريق الخاص بك.
ageofheroes-road-built = { $tribe1 } و { $tribe2 } متصلان الآن بطريق.
ageofheroes-road-no-target = لا توجد قبائل مجاورة متاحة لبناء الطريق.
ageofheroes-approve = موافقة
ageofheroes-deny = رفض
ageofheroes-supply-exhausted = لا يوجد المزيد من { $building } متاح للبناء.

# Do Nothing
ageofheroes-do-nothing = { $player } يمرر.
ageofheroes-do-nothing-you = تمرر...

# War
ageofheroes-war-declare = { $attacker } يعلن الحرب على { $defender }. الهدف: { $goal }.
ageofheroes-war-prepare = اختر جيوشك لـ { $action }.
ageofheroes-war-no-army = ليس لديك جيوش أو أوراق أبطال متاحة.
ageofheroes-war-no-targets = لا توجد أهداف صالحة للحرب.
ageofheroes-war-no-valid-goal = لا توجد أهداف حرب صالحة ضد هذا الهدف.
ageofheroes-war-select-target = اختر اللاعب الذي تريد مهاجمته.
ageofheroes-war-select-goal = اختر هدف الحرب الخاص بك.
ageofheroes-war-prepare-attack = اختر قواتك المهاجمة.
ageofheroes-war-prepare-defense = { $attacker } يهاجمك؛ اختر قواتك المدافعة.
ageofheroes-war-select-armies = اختر الجيوش: { $count }
ageofheroes-war-select-generals = اختر القادة: { $count }
ageofheroes-war-select-heroes = اختر الأبطال: { $count }
ageofheroes-war-attack = هجوم...
ageofheroes-war-defend = دفاع...
ageofheroes-war-prepared = قواتك: { $armies } { $armies ->
    [zero] جيوش
    [one] جيش
    [two] جيشان
    [few] جيوش
    [many] جيشاً
    *[other] جيش
}{ $generals ->
    [0] {""}
    [1] {" و 1 قائد"}
    [2] {" و قائدان"}
    *[other] {" و { $generals } قادة"}
}{ $heroes ->
    [0] {""}
    [1] {" و 1 بطل"}
    [2] {" و بطلان"}
    *[other] {" و { $heroes } أبطال"}
}.
ageofheroes-war-roll-you = ترمي { $roll }.
ageofheroes-war-roll-other = { $player } يرمي { $roll }.
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [1] {"+1 من الحصن = { $total } إجمالي"}
            *[other] {"+{ $fortress } من الحصون = { $total } إجمالي"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"+{ $general } من القائد = { $total } إجمالي"}
            [1] {"+{ $general } من القائد، +1 من الحصن = { $total } إجمالي"}
            *[other] {"+{ $general } من القائد، +{ $fortress } من الحصون = { $total } إجمالي"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [1] {"{ $player }: +1 من الحصن = { $total } إجمالي"}
            *[other] {"{ $player }: +{ $fortress } من الحصون = { $total } إجمالي"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } من القائد = { $total } إجمالي"}
            [1] {"{ $player }: +{ $general } من القائد، +1 من الحصن = { $total } إجمالي"}
            *[other] {"{ $player }: +{ $general } من القائد، +{ $fortress } من الحصون = { $total } إجمالي"}
        }
    }
}

# Battle
ageofheroes-battle-start = تبدأ المعركة. { $attacker } بـ { $att_armies } { $att_armies ->
    [zero] جيوش
    [one] جيش
    [two] جيشان
    [few] جيوش
    [many] جيشاً
    *[other] جيش
} ضد { $defender } بـ { $def_armies } { $def_armies ->
    [zero] جيوش
    [one] جيش
    [two] جيشان
    [few] جيوش
    [many] جيشاً
    *[other] جيش
}.
ageofheroes-dice-roll-detailed = { $name } يرمي { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } من القائد" }
}{ $fortress ->
    [0] {""}
    [1] { " + 1 من الحصن" }
    *[other] { " + { $fortress } من الحصون" }
} = { $total }.
ageofheroes-dice-roll-detailed-you = ترمي { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } من القائد" }
}{ $fortress ->
    [0] {""}
    [1] { " + 1 من الحصن" }
    *[other] { " + { $fortress } من الحصون" }
} = { $total }.
ageofheroes-round-attacker-wins = { $attacker } يفوز بالجولة ({ $att_total } مقابل { $def_total }). { $defender } يخسر جيشاً.
ageofheroes-round-defender-wins = { $defender } يدافع بنجاح ({ $def_total } مقابل { $att_total }). { $attacker } يخسر جيشاً.
ageofheroes-round-draw = كلا الجانبين يتعادلان عند { $total }. لا جيوش مفقودة.
ageofheroes-battle-victory-attacker = { $attacker } يهزم { $defender }.
ageofheroes-battle-victory-defender = { $defender } يدافع بنجاح ضد { $attacker }.
ageofheroes-battle-mutual-defeat = كلا من { $attacker } و { $defender } يخسران جميع الجيوش.
ageofheroes-general-bonus = +{ $count } من { $count ->
    [zero] القادة
    [one] القائد
    [two] القائدين
    [few] القادة
    [many] قائداً
    *[other] قائد
}
ageofheroes-fortress-bonus = +{ $count } من دفاع الحصن
ageofheroes-battle-winner = { $winner } يفوز بالمعركة.
ageofheroes-battle-draw = المعركة تنتهي بالتعادل...
ageofheroes-battle-continue = استمر في المعركة.
ageofheroes-battle-end = المعركة انتهت.

# War outcomes
ageofheroes-conquest-success = { $attacker } يغزو { $count } { $count ->
    [zero] مدن
    [one] مدينة
    [two] مدينتين
    [few] مدن
    [many] مدينة
    *[other] مدينة
} من { $defender }.
ageofheroes-plunder-success = { $attacker } ينهب { $count } { $count ->
    [zero] أوراق
    [one] ورقة
    [two] ورقتين
    [few] أوراق
    [many] ورقة
    *[other] ورقة
} من { $defender }.
ageofheroes-destruction-success = { $attacker } يدمر { $count } من { $count ->
    [zero] موارد
    [one] مورد
    [two] موردين
    [few] موارد
    [many] مورداً
    *[other] مورد
} نصب { $defender } التذكاري.
ageofheroes-army-losses = { $player } يخسر { $count } { $count ->
    [zero] جيوش
    [one] جيش
    [two] جيشان
    [few] جيوش
    [many] جيشاً
    *[other] جيش
}.
ageofheroes-army-losses-you = تخسر { $count } { $count ->
    [zero] جيوش
    [one] جيش
    [two] جيشان
    [few] جيوش
    [many] جيشاً
    *[other] جيش
}.

# Army return
ageofheroes-army-return-road = قواتك تعود فوراً عبر الطريق.
ageofheroes-army-return-delayed = { $count } { $count ->
    [zero] وحدات
    [one] وحدة
    [two] وحدتان
    [few] وحدات
    [many] وحدة
    *[other] وحدة
} تعود في نهاية دورك القادم.
ageofheroes-army-returned = قوات { $player } عادت من الحرب.
ageofheroes-army-returned-you = قواتك عادت من الحرب.
ageofheroes-army-recover = جيوش { $player } تتعافى من الزلزال.
ageofheroes-army-recover-you = جيوشك تتعافى من الزلزال.

# Olympics
ageofheroes-olympics-cancel = { $player } يلعب الألعاب الأولمبية. الحرب ملغاة.
ageofheroes-olympics-prompt = { $attacker } أعلن الحرب. لديك الألعاب الأولمبية - استخدمها للإلغاء؟
ageofheroes-yes = نعم
ageofheroes-no = لا

# Monument progress
ageofheroes-monument-progress = نصب { $player } التذكاري { $count }/5 مكتمل.
ageofheroes-monument-progress-you = نصبك التذكاري { $count }/5 مكتمل.

# Hand management
ageofheroes-discard-excess = لديك أكثر من { $max } أوراق. تخلص من { $count } { $count ->
    [zero] أوراق
    [one] ورقة
    [two] ورقتين
    [few] أوراق
    [many] ورقة
    *[other] ورقة
}.
ageofheroes-discard-excess-other = { $player } يجب أن يتخلص من الأوراق الزائدة.
ageofheroes-discard-more = تخلص من { $count } { $count ->
    [zero] أوراق
    [one] ورقة أخرى
    [two] ورقتين أخريين
    [few] أوراق أخرى
    [many] ورقة أخرى
    *[other] ورقة أخرى
}.

# Victory
ageofheroes-victory-cities = { $player } بنى 5 مدن! إمبراطورية المدن الخمس.
ageofheroes-victory-cities-you = بنيت 5 مدن! إمبراطورية المدن الخمس.
ageofheroes-victory-monument = { $player } أكمل نصبه التذكاري! حاملو الثقافة العظيمة.
ageofheroes-victory-monument-you = أكملت نصبك التذكاري! حاملو الثقافة العظيمة.
ageofheroes-victory-last-standing = { $player } هو القبيلة الأخيرة الباقية! الأكثر إصراراً.
ageofheroes-victory-last-standing-you = أنت القبيلة الأخيرة الباقية! الأكثر إصراراً.
ageofheroes-game-over = انتهت اللعبة.

# Elimination
ageofheroes-eliminated = { $player } تم القضاء عليه.
ageofheroes-eliminated-you = تم القضاء عليك.

# Hand
ageofheroes-hand-empty = ليس لديك أوراق.
ageofheroes-hand-contents = يدك ({ $count } { $count ->
    [zero] أوراق
    [one] ورقة
    [two] ورقتين
    [few] أوراق
    [many] ورقة
    *[other] ورقة
}): { $cards }

# Status
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [zero] مدن
    [one] مدينة
    [two] مدينتان
    [few] مدن
    [many] مدينة
    *[other] مدينة
}، { $armies } { $armies ->
    [zero] جيوش
    [one] جيش
    [two] جيشان
    [few] جيوش
    [many] جيشاً
    *[other] جيش
}، { $monument }/5 نصب تذكاري
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = المدن: { $count }
ageofheroes-status-armies = الجيوش: { $count }
ageofheroes-status-generals = القادة: { $count }
ageofheroes-status-fortresses = الحصون: { $count }
ageofheroes-status-monument = النصب التذكاري: { $count }/5
ageofheroes-status-roads = الطرق: { $left }{ $right }
ageofheroes-status-road-left = يسار
ageofheroes-status-road-right = يمين
ageofheroes-status-none = لا شيء
ageofheroes-status-earthquake-armies = الجيوش المتعافية: { $count }
ageofheroes-status-returning-armies = الجيوش العائدة: { $count }
ageofheroes-status-returning-generals = القادة العائدون: { $count }

# Deck info
ageofheroes-deck-empty = لا مزيد من أوراق { $card } في المجموعة.
ageofheroes-deck-count = الأوراق المتبقية: { $count }
ageofheroes-deck-reshuffled = تم إعادة خلط كومة التخلص في المجموعة.

# Give up
ageofheroes-give-up-confirm = هل أنت متأكد أنك تريد الاستسلام؟
ageofheroes-gave-up = { $player } استسلم!
ageofheroes-gave-up-you = استسلمت!

# Hero card
ageofheroes-hero-use = استخدام كجيش أو قائد؟
ageofheroes-hero-army = جيش
ageofheroes-hero-general = قائد

# Fortune card
ageofheroes-fortune-reroll = { $player } يستخدم الحظ لإعادة الرمي.
ageofheroes-fortune-prompt = خسرت الرمية. استخدم الحظ لإعادة الرمي؟

# Disabled action reasons
ageofheroes-not-your-turn = ليس دورك.
ageofheroes-game-not-started = اللعبة لم تبدأ بعد.
ageofheroes-wrong-phase = هذا الإجراء غير متاح في المرحلة الحالية.
ageofheroes-no-resources = ليس لديك الموارد المطلوبة.

# Building costs (for display)
ageofheroes-cost-army = 2 حبوب، حديد
ageofheroes-cost-fortress = حديد، خشب، حجر
ageofheroes-cost-general = حديد، ذهب
ageofheroes-cost-road = 2 حجر
ageofheroes-cost-city = 2 خشب، حجر
