# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = دزدان دریایی دریاهای گمشده

# Game start and setup
pirates-welcome = به دزدان دریایی دریاهای گمشده خوش آمدید! دریاها را کشتی‌رانی کنید، جواهرات جمع کنید و با دزدان دریایی دیگر نبرد کنید!
pirates-oceans = سفر شما از این اقیانوس‌ها می‌گذرد: { $oceans }
pirates-gems-placed = { $total } جواهر در سراسر دریاها پراکنده شده‌اند. همه را پیدا کنید!
pirates-golden-moon = ماه طلایی طلوع می‌کند! تمام افزایش تجربه این دور سه برابر می‌شود!

# Turn announcements
pirates-turn = نوبت { $player }. موقعیت { $position }

# Movement actions
pirates-move-left = کشتی‌رانی به چپ
pirates-move-right = کشتی‌رانی به راست
pirates-move-2-left = کشتی‌رانی ۲ خانه به چپ
pirates-move-2-right = کشتی‌رانی ۲ خانه به راست
pirates-move-3-left = کشتی‌رانی ۳ خانه به چپ
pirates-move-3-right = کشتی‌رانی ۳ خانه به راست

# Movement messages
pirates-move-you = شما به { $direction } به موقعیت { $position } کشتی‌رانی می‌کنید.
pirates-move-you-tiles = شما { $tiles } خانه به { $direction } به موقعیت { $position } کشتی‌رانی می‌کنید.
pirates-move = { $player } به { $direction } به موقعیت { $position } کشتی‌رانی می‌کند.
pirates-map-edge = شما نمی‌توانید بیشتر کشتی‌رانی کنید. شما در موقعیت { $position } هستید.

# Position and status
pirates-check-status = بررسی وضعیت
pirates-check-position = بررسی موقعیت
pirates-check-moon = بررسی روشنایی ماه
pirates-your-position = موقعیت شما: { $position } در { $ocean }
pirates-moon-brightness = ماه طلایی { $brightness }٪ روشن است. ({ $collected } از { $total } جواهر جمع‌آوری شده است).
pirates-no-golden-moon = ماه طلایی در حال حاضر در آسمان دیده نمی‌شود.

# Gem collection
pirates-gem-found-you = شما یک { $gem } پیدا کردید! ارزش { $value } امتیاز.
pirates-gem-found = { $player } یک { $gem } پیدا کرد! ارزش { $value } امتیاز.
pirates-all-gems-collected = تمام جواهرات جمع‌آوری شدند!

# Winner
pirates-winner = { $player } با { $score } امتیاز برنده می‌شود!

# Skills menu
pirates-use-skill = استفاده از مهارت
pirates-select-skill = مهارتی برای استفاده انتخاب کنید

# Combat - Attack initiation
pirates-cannonball = شلیک گلوله توپ
pirates-no-targets = هدفی در { $range } خانه نیست.
pirates-attack-you-fire = شما گلوله توپی به { $target } شلیک می‌کنید!
pirates-attack-incoming = { $attacker } گلوله توپی به شما شلیک می‌کند!
pirates-attack-fired = { $attacker } گلوله توپی به { $defender } شلیک می‌کند!

# Combat - Rolls
pirates-attack-roll = تاس حمله: { $roll }
pirates-attack-bonus = پاداش حمله: +{ $bonus }
pirates-defense-roll = تاس دفاع: { $roll }
pirates-defense-roll-others = { $player } برای دفاع { $roll } می‌اندازد.
pirates-defense-bonus = پاداش دفاع: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = اصابت مستقیم! شما { $target } را زدید!
pirates-attack-hit-them = شما توسط { $attacker } زده شدید!
pirates-attack-hit = { $attacker } به { $defender } اصابت می‌کند!

# Combat - Miss results
pirates-attack-miss-you = گلوله توپ شما به { $target } نخورد.
pirates-attack-miss-them = گلوله توپ به شما نخورد!
pirates-attack-miss = گلوله توپ { $attacker } به { $defender } نمی‌خورد.

# Combat - Push
pirates-push-you = شما { $target } را به { $direction } به موقعیت { $position } هل می‌دهید!
pirates-push-them = { $attacker } شما را به { $direction } به موقعیت { $position } هل می‌دهد!
pirates-push = { $attacker } { $defender } را به { $direction } از { $old_pos } به { $new_pos } هل می‌دهد.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } سعی در سرقت جواهر می‌کند!
pirates-steal-rolls = تاس سرقت: { $steal } در مقابل دفاع: { $defend }
pirates-steal-success-you = شما یک { $gem } از { $target } دزدیدید!
pirates-steal-success-them = { $attacker } { $gem } شما را دزدید!
pirates-steal-success = { $attacker } یک { $gem } از { $defender } می‌دزدد!
pirates-steal-failed = تلاش برای سرقت شکست خورد!

# XP and Leveling
pirates-xp-gained = +{ $xp } تجربه
pirates-level-up = { $player } به سطح { $level } رسید!
pirates-level-up-you = شما به سطح { $level } رسیدید!
pirates-level-up-multiple = { $player } { $levels } سطح به دست آورد! حالا سطح { $level }!
pirates-level-up-multiple-you = شما { $levels } سطح به دست آوردید! حالا سطح { $level }!
pirates-skills-unlocked = { $player } مهارت‌های جدید باز کرد: { $skills }.
pirates-skills-unlocked-you = شما مهارت‌های جدید باز کردید: { $skills }.

# Skill activation
pirates-skill-activated = { $player } { $skill } را فعال می‌کند!
pirates-buff-expired = بافت { $skill } { $player } از بین رفت.

# Sword Fighter skill
pirates-sword-fighter-activated = جنگجوی شمشیر فعال شد! +۴ پاداش حمله برای { $turns } نوبت.

# Push skill (defense buff)
pirates-push-activated = هل دادن فعال شد! +۳ پاداش دفاع برای { $turns } نوبت.

# Skilled Captain skill
pirates-skilled-captain-activated = کاپیتان ماهر فعال شد! +۲ حمله و +۲ دفاع برای { $turns } نوبت.

# Double Devastation skill
pirates-double-devastation-activated = ویرانی دوگانه فعال شد! برد حمله به ۱۰ خانه برای { $turns } نوبت افزایش یافت.

# Battleship skill
pirates-battleship-activated = کشتی جنگی فعال شد! شما می‌توانید این نوبت دو شلیک انجام دهید!
pirates-battleship-no-targets = هدفی برای شلیک { $shot } نیست.
pirates-battleship-shot = شلیک { $shot }...

# Portal skill
pirates-portal-no-ships = کشتی دیگری در دیدرس برای پورتال نیست.
pirates-portal-fizzle = پورتال { $player } بدون مقصد محو می‌شود.
pirates-portal-success = { $player } به { $ocean } در موقعیت { $position } پورتال می‌شود!

# Gem Seeker skill
pirates-gem-seeker-reveal = دریاها از یک { $gem } در موقعیت { $position } نجوا می‌کنند. ({ $uses } استفاده باقی‌مانده)

# Level requirements
pirates-requires-level-15 = نیاز به سطح ۱۵
pirates-requires-level-150 = نیاز به سطح ۱۵۰

# XP Multiplier options
pirates-set-combat-xp-multiplier = ضریب تجربه نبرد: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = تجربه برای نبرد
pirates-set-find-gem-xp-multiplier = ضریب تجربه پیدا کردن جواهر: { $find_gem_xp_multiplier }
pirates-enter-find-gem-xp-multiplier = تجربه برای پیدا کردن جواهر

# Gem stealing options
pirates-set-gem-stealing = سرقت جواهر: { $mode }
pirates-select-gem-stealing = حالت سرقت جواهر را انتخاب کنید
pirates-option-changed-stealing = سرقت جواهر به { $mode } تنظیم شد.

# Gem stealing mode choices
pirates-stealing-with-bonus = با پاداش تاس
pirates-stealing-no-bonus = بدون پاداش تاس
pirates-stealing-disabled = غیرفعال
