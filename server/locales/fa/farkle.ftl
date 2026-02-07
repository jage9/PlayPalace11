# Farkle game messages

# Game info
game-name-farkle = فارکل

# Actions - Roll and Bank
farkle-roll = پرتاب { $count } { $count ->
    [one] تاس
   *[other] تاس
}
farkle-bank = ذخیره { $points } امتیاز

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = یک ۱ برای { $points } امتیاز
farkle-take-single-five = یک ۵ برای { $points } امتیاز
farkle-take-three-kind = سه { $number } برای { $points } امتیاز
farkle-take-four-kind = چهار { $number } برای { $points } امتیاز
farkle-take-five-kind = پنج { $number } برای { $points } امتیاز
farkle-take-six-kind = شش { $number } برای { $points } امتیاز
farkle-take-small-straight = دنباله کوچک برای { $points } امتیاز
farkle-take-large-straight = دنباله بزرگ برای { $points } امتیاز
farkle-take-three-pairs = سه جفت برای { $points } امتیاز
farkle-take-double-triplets = دو سه‌تایی برای { $points } امتیاز
farkle-take-full-house = خانه کامل برای { $points } امتیاز

# Game events (matching v10 exactly)
farkle-rolls = { $player } پرتاب می‌کند { $count } { $count ->
    [one] تاس
   *[other] تاس
}...
farkle-you-roll = شما پرتاب می‌کنید { $count } { $count ->
    [one] تاس
   *[other] تاس
}...
farkle-roll-result = { $dice }
farkle-farkle = فارکل! { $player } از دست می‌دهد { $points } امتیاز
farkle-you-farkle = فارکل! شما از دست می‌دهید { $points } امتیاز
farkle-takes-combo = { $player } می‌گیرد { $combo } برای { $points } امتیاز
farkle-you-take-combo = شما می‌گیرید { $combo } برای { $points } امتیاز
farkle-hot-dice = تاس‌های داغ!
farkle-banks = { $player } ذخیره می‌کند { $points } امتیاز برای مجموع { $total }
farkle-you-bank = شما ذخیره می‌کنید { $points } امتیاز برای مجموع { $total }
farkle-winner = { $player } برنده می‌شود با { $score } امتیاز!
farkle-you-win = شما برنده شدید با { $score } امتیاز!
farkle-winners-tie = مساوی! برندگان: { $players }

# Check turn score action
farkle-turn-score = { $player } دارد { $points } امتیاز در این نوبت.
farkle-no-turn = هیچ کس در حال حاضر نوبت ندارد.

# Farkle-specific options
farkle-set-target-score = امتیاز هدف: { $score }
farkle-enter-target-score = امتیاز هدف را وارد کنید (۵۰۰-۵۰۰۰):
farkle-option-changed-target = امتیاز هدف به { $score } تنظیم شد.

# Disabled action reasons
farkle-must-take-combo = ابتدا باید یک ترکیب امتیازی را بردارید.
farkle-cannot-bank = اکنون نمی‌توانید ذخیره کنید.
