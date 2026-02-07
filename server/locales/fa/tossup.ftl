# Toss Up game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-tossup = پرتاب
tossup-category = بازی‌های تاس

# Actions
tossup-roll-first = پرتاب { $count } تاس
tossup-roll-remaining = پرتاب { $count } تاس باقیمانده
tossup-bank = ذخیره { $points } امتیاز

# Game events
tossup-turn-start = نوبت { $player }. امتیاز: { $score }
tossup-you-roll = شما انداختید: { $results }.
tossup-player-rolls = { $player } انداخت: { $results }.

# Turn status
tossup-you-have-points = امتیاز نوبت: { $turn_points }. تاس‌های باقیمانده: { $dice_count }.
tossup-player-has-points = { $player } دارای { $turn_points } امتیاز نوبت است. { $dice_count } تاس باقیمانده.

# Fresh dice
tossup-you-get-fresh = تاسی باقی نماند! دریافت { $count } تاس تازه.
tossup-player-gets-fresh = { $player } { $count } تاس تازه می‌گیرد.

# Bust
tossup-you-bust = باخت! شما { $points } امتیاز این نوبت را از دست دادید.
tossup-player-busts = { $player } باخت و { $points } امتیاز را از دست داد!

# Bank
tossup-you-bank = شما { $points } امتیاز ذخیره کردید. مجموع امتیاز: { $total }.
tossup-player-banks = { $player } { $points } امتیاز ذخیره کرد. مجموع امتیاز: { $total }.

# Winner
tossup-winner = { $player } با { $score } امتیاز برنده شد!
tossup-tie-tiebreaker = بین { $players } مساوی شد! دور تعیین برنده!

# Options
tossup-set-rules-variant = نوع قوانین: { $variant }
tossup-select-rules-variant = نوع قوانین را انتخاب کنید:
tossup-option-changed-rules = نوع قوانین به { $variant } تغییر یافت

tossup-set-starting-dice = تاس‌های شروع: { $count }
tossup-enter-starting-dice = تعداد تاس‌های شروع را وارد کنید:
tossup-option-changed-dice = تاس‌های شروع به { $count } تغییر یافت

# Rules variants
tossup-rules-standard = استاندارد
tossup-rules-playpalace = پلی‌پلس

# Rules explanations
tossup-rules-standard-desc = ۳ سبز، ۲ زرد، ۱ قرمز در هر تاس. باخت اگر سبز نباشد و حداقل یک قرمز باشد.
tossup-rules-playpalace-desc = توزیع یکسان. باخت اگر همه تاس‌ها قرمز باشند.

# Disabled reasons
tossup-need-points = برای ذخیره نیاز به امتیاز دارید.
