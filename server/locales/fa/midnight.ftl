# 1-4-24 (Midnight) game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-midnight = ۱-۴-۲۴
midnight-category = بازی‌های تاس

# Actions
midnight-roll = پرتاب تاس‌ها
midnight-keep-die = نگه‌داشتن { $value }
midnight-bank = ذخیره

# Game events
midnight-turn-start = نوبت { $player }.
midnight-you-rolled = شما پرتاب کردید: { $dice }.
midnight-player-rolled = { $player } پرتاب کرد: { $dice }.

# Keeping dice
midnight-you-keep = شما نگه می‌دارید { $die }.
midnight-player-keeps = { $player } نگه می‌دارد { $die }.
midnight-you-unkeep = شما رها می‌کنید { $die }.
midnight-player-unkeeps = { $player } رها می‌کند { $die }.

# Turn status
midnight-you-have-kept = تاس‌های نگه‌داشته: { $kept }. پرتاب‌های باقی‌مانده: { $remaining }.
midnight-player-has-kept = { $player } نگه‌داشته: { $kept }. { $remaining } تاس باقی‌مانده.

# Scoring
midnight-you-scored = شما امتیاز گرفتید { $score } امتیاز.
midnight-scored = { $player } امتیاز گرفت { $score } امتیاز.
midnight-you-disqualified = شما هر دو ۱ و ۴ ندارید. رد صلاحیت شدید!
midnight-player-disqualified = { $player } هر دو ۱ و ۴ ندارد. رد صلاحیت شد!

# Round results
midnight-round-winner = { $player } برنده دور می‌شود!
midnight-round-tie = دور بین { $players } مساوی شد.
midnight-all-disqualified = همه بازیکنان رد صلاحیت شدند! این دور برنده‌ای نیست.

# Game winner
midnight-game-winner = { $player } برنده بازی می‌شود با { $wins } برد در دور!
midnight-game-tie = مساوی! { $players } هر کدام { $wins } دور بردند.

# Options
midnight-set-rounds = دورهای بازی: { $rounds }
midnight-enter-rounds = تعداد دورها را وارد کنید:
midnight-option-changed-rounds = دورهای بازی به { $rounds } تغییر یافت

# Disabled reasons
midnight-need-to-roll = ابتدا باید تاس‌ها را پرتاب کنید.
midnight-no-dice-to-keep = هیچ تاسی برای نگه‌داشتن موجود نیست.
midnight-must-keep-one = باید حداقل یک تاس در هر پرتاب نگه دارید.
midnight-must-roll-first = ابتدا باید تاس‌ها را پرتاب کنید.
midnight-keep-all-first = باید قبل از ذخیره همه تاس‌ها را نگه دارید.
