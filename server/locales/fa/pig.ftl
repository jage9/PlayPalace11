# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = خوک
pig-category = بازی‌های تاس

# Actions
pig-roll = پرتاب تاس
pig-bank = ذخیره { $points } امتیاز

# Game events (Pig-specific)
pig-rolls = { $player } تاس می‌اندازد...
pig-roll-result = یک { $roll }، جمعاً { $total }
pig-bust = اوه نه، یک ۱! { $player } امتیاز { $points } را از دست می‌دهد.
pig-bank-action = { $player } تصمیم می‌گیرد { $points } را ذخیره کند، جمعاً { $total }
pig-winner = برنده داریم و آن { $player } است!

# Pig-specific options
pig-set-min-bank = حداقل ذخیره: { $points }
pig-set-dice-sides = اضلاع تاس: { $sides }
pig-enter-min-bank = حداقل امتیاز برای ذخیره را وارد کنید:
pig-enter-dice-sides = تعداد اضلاع تاس را وارد کنید:
pig-option-changed-min-bank = حداقل امتیاز ذخیره به { $points } تغییر یافت
pig-option-changed-dice = تاس اکنون { $sides } ضلع دارد

# Disabled reasons
pig-need-more-points = برای ذخیره نیاز به امتیاز بیشتری دارید.

# Validation errors
pig-error-min-bank-too-high = حداقل امتیاز ذخیره باید کمتر از امتیاز هدف باشد.
