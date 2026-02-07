# Five Card Draw

game-name-fivecarddraw = السحب بخمس أوراق

draw-set-starting-chips = رقائق البداية: { $count }
draw-enter-starting-chips = أدخل رقائق البداية
draw-option-changed-starting-chips = تم تعيين رقائق البداية إلى { $count }.

draw-set-ante = الرهان الأولي: { $count }
draw-enter-ante = أدخل مبلغ الرهان الأولي
draw-option-changed-ante = تم تعيين الرهان الأولي إلى { $count }.

draw-set-turn-timer = مؤقت الدور: { $mode }
draw-select-turn-timer = اختر مؤقت الدور
draw-option-changed-turn-timer = تم تعيين مؤقت الدور إلى { $mode }.

draw-set-raise-mode = وضع الرفع: { $mode }
draw-select-raise-mode = اختر وضع الرفع
draw-option-changed-raise-mode = تم تعيين وضع الرفع إلى { $mode }.

draw-set-max-raises = الرفعات القصوى: { $count }
draw-enter-max-raises = أدخل الرفعات القصوى (0 لغير محدود)
draw-option-changed-max-raises = تم تعيين الرفعات القصوى إلى { $count }.

draw-antes-posted = تم نشر الرهانات الأولية: { $amount }.
draw-betting-round-1 = جولة الرهان.
draw-betting-round-2 = جولة الرهان.
draw-begin-draw = مرحلة السحب.
draw-not-draw-phase = ليس وقت السحب.
draw-not-betting = لا يمكنك الرهان أثناء مرحلة السحب.

draw-toggle-discard = تبديل الإلقاء للورقة { $index }
draw-card-keep = { $card }، محتفظ به
draw-card-discard = { $card }، سيتم إلقاؤه
draw-card-kept = احتفظ بـ { $card }.
draw-card-discarded = ألقِ { $card }.
draw-draw-cards = اسحب أوراقاً
draw-draw-cards-count = اسحب { $count } { $count ->
    [zero] ورقة
    [one] ورقة
    [two] ورقتين
    [few] أوراق
    [many] ورقة
   *[other] ورقة
}
draw-dealt-cards = تم توزيع { $cards } عليك.
draw-you-drew-cards = أنت تسحب { $cards }.
draw-you-draw = أنت تسحب { $count } { $count ->
    [zero] ورقة
    [one] ورقة
    [two] ورقتين
    [few] أوراق
    [many] ورقة
   *[other] ورقة
}.
draw-player-draws = { $player } يسحب { $count } { $count ->
    [zero] ورقة
    [one] ورقة
    [two] ورقتين
    [few] أوراق
    [many] ورقة
   *[other] ورقة
}.
draw-you-stand-pat = أنت تقف على حالك.
draw-player-stands-pat = { $player } يقف على حاله.
draw-you-discard-limit = يمكنك إلقاء ما يصل إلى { $count } ورقة.
draw-player-discard-limit = { $player } يمكنه إلقاء ما يصل إلى { $count } ورقة.
