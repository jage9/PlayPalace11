# Yahtzee game messages

# Game info
game-name-yahtzee = یاتزی

# Actions - Rolling
yahtzee-roll = پرتاب مجدد ({ $count } باقی‌مانده)
yahtzee-roll-all = پرتاب تاس‌ها

# Upper section scoring categories
yahtzee-score-ones = یک‌ها برای { $points } امتیاز
yahtzee-score-twos = دوها برای { $points } امتیاز
yahtzee-score-threes = سه‌ها برای { $points } امتیاز
yahtzee-score-fours = چهارها برای { $points } امتیاز
yahtzee-score-fives = پنج‌ها برای { $points } امتیاز
yahtzee-score-sixes = شش‌ها برای { $points } امتیاز

# Lower section scoring categories
yahtzee-score-three-kind = سه تا یکسان برای { $points } امتیاز
yahtzee-score-four-kind = چهار تا یکسان برای { $points } امتیاز
yahtzee-score-full-house = خانه کامل برای { $points } امتیاز
yahtzee-score-small-straight = دنباله کوچک برای { $points } امتیاز
yahtzee-score-large-straight = دنباله بزرگ برای { $points } امتیاز
yahtzee-score-yahtzee = یاتزی برای { $points } امتیاز
yahtzee-score-chance = شانس برای { $points } امتیاز

# Game events
yahtzee-you-rolled = شما پرتاب کردید: { $dice }. پرتاب‌های باقی‌مانده: { $remaining }
yahtzee-player-rolled = { $player } پرتاب کرد: { $dice }. پرتاب‌های باقی‌مانده: { $remaining }

# Scoring announcements
yahtzee-you-scored = شما کسب کردید { $points } امتیاز در { $category }.
yahtzee-player-scored = { $player } کسب کرد { $points } در { $category }.

# Yahtzee bonus
yahtzee-you-bonus = جایزه یاتزی! +۱۰۰ امتیاز
yahtzee-player-bonus = { $player } جایزه یاتزی گرفت! +۱۰۰ امتیاز

# Upper section bonus
yahtzee-you-upper-bonus = جایزه بخش بالا! +۳۵ امتیاز ({ $total } در بخش بالا)
yahtzee-player-upper-bonus = { $player } جایزه بخش بالا را گرفت! +۳۵ امتیاز
yahtzee-you-upper-bonus-missed = شما جایزه بخش بالا را از دست دادید ({ $total } در بخش بالا، نیاز به ۶۳).
yahtzee-player-upper-bonus-missed = { $player } جایزه بخش بالا را از دست داد.

# Scoring mode
yahtzee-choose-category = یک دسته برای امتیاز انتخاب کنید.
yahtzee-continuing = ادامه نوبت.

# Status checks
yahtzee-check-scoresheet = بررسی کارت امتیاز
yahtzee-view-dice = بررسی دست
yahtzee-your-dice = تاس‌های شما: { $dice }.
yahtzee-your-dice-kept = تاس‌های شما: { $dice }. نگه‌داشته: { $kept }
yahtzee-not-rolled = شما هنوز پرتاب نکرده‌اید.

# Scoresheet display
yahtzee-scoresheet-header = === کارت امتیاز { $player } ===
yahtzee-scoresheet-upper = بخش بالا:
yahtzee-scoresheet-lower = بخش پایین:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = مجموع بالا: { $total } (جایزه: +۳۵)
yahtzee-scoresheet-upper-total-needed = مجموع بالا: { $total } ({ $needed } بیشتر برای جایزه)
yahtzee-scoresheet-yahtzee-bonus = جوایز یاتزی: { $count } x ۱۰۰ = { $total }
yahtzee-scoresheet-grand-total = مجموع امتیاز: { $total }

# Category names (for announcements)
yahtzee-category-ones = یک‌ها
yahtzee-category-twos = دوها
yahtzee-category-threes = سه‌ها
yahtzee-category-fours = چهارها
yahtzee-category-fives = پنج‌ها
yahtzee-category-sixes = شش‌ها
yahtzee-category-three-kind = سه تا یکسان
yahtzee-category-four-kind = چهار تا یکسان
yahtzee-category-full-house = خانه کامل
yahtzee-category-small-straight = دنباله کوچک
yahtzee-category-large-straight = دنباله بزرگ
yahtzee-category-yahtzee = یاتزی
yahtzee-category-chance = شانس

# Game end
yahtzee-winner = { $player } برنده می‌شود با { $score } امتیاز!
yahtzee-winners-tie = مساوی! { $players } همگی { $score } امتیاز گرفتند!

# Options
yahtzee-set-rounds = تعداد بازی‌ها: { $rounds }
yahtzee-enter-rounds = تعداد بازی‌ها را وارد کنید (۱-۱۰):
yahtzee-option-changed-rounds = تعداد بازی‌ها به { $rounds } تنظیم شد.

# Disabled action reasons
yahtzee-no-rolls-left = هیچ پرتابی باقی نمانده است.
yahtzee-roll-first = ابتدا باید پرتاب کنید.
yahtzee-category-filled = آن دسته قبلاً پر شده است.
