# Scopa game messages
# Note: Common messages like round-start, turn-start, target-score, team-mode are in games.ftl

# Game name
game-name-scopa = اسکوپا

# Game events
scopa-initial-table = کارت‌های روی میز: { $cards }
scopa-no-initial-table = کارتی برای شروع روی میز نیست.
scopa-you-collect = شما جمع می‌کنید { $cards } با { $card }
scopa-player-collects = { $player } جمع می‌کند { $cards } با { $card }
scopa-you-put-down = شما می‌گذارید { $card }.
scopa-player-puts-down = { $player } می‌گذارد { $card }.
scopa-scopa-suffix =  - اسکوپا!
scopa-clear-table-suffix = ، میز را خالی کرد.
scopa-remaining-cards = { $player } کارت‌های باقی‌مانده روی میز را می‌گیرد.
scopa-scoring-round = دور امتیازدهی...
scopa-most-cards = { $player } یک امتیاز برای بیشترین کارت‌ها می‌گیرد ({ $count } کارت).
scopa-most-cards-tie = بیشترین کارت‌ها مساوی است - امتیازی داده نمی‌شود.
scopa-most-diamonds = { $player } یک امتیاز برای بیشترین خشت‌ها می‌گیرد ({ $count } خشت).
scopa-most-diamonds-tie = بیشترین خشت‌ها مساوی است - امتیازی داده نمی‌شود.
scopa-seven-diamonds = { $player } یک امتیاز برای ۷ خشت می‌گیرد.
scopa-seven-diamonds-multi = { $player } یک امتیاز برای بیشترین ۷ خشت می‌گیرد ({ $count } × ۷ خشت).
scopa-seven-diamonds-tie = ۷ خشت مساوی است - امتیازی داده نمی‌شود.
scopa-most-sevens = { $player } یک امتیاز برای بیشترین هفت‌ها می‌گیرد ({ $count } هفت).
scopa-most-sevens-tie = بیشترین هفت‌ها مساوی است - امتیازی داده نمی‌شود.
scopa-round-scores = امتیازهای دور:
scopa-round-score-line = { $player }: +{ $round_score } (مجموع: { $total_score })
scopa-table-empty = کارتی روی میز نیست.
scopa-no-such-card = کارتی در آن موقعیت نیست.
scopa-captured-count = شما { $count } کارت گرفته‌اید

# View actions
scopa-view-table = مشاهده میز
scopa-view-captured = مشاهده گرفته‌شده‌ها

# Scopa-specific options
scopa-enter-target-score = امتیاز هدف را وارد کنید (۱-۱۲۱)
scopa-set-cards-per-deal = کارت در هر دست: { $cards }
scopa-enter-cards-per-deal = کارت در هر دست را وارد کنید (۱-۱۰)
scopa-set-decks = تعداد دسته‌ها: { $decks }
scopa-enter-decks = تعداد دسته‌ها را وارد کنید (۱-۶)
scopa-toggle-escoba = اسکوبا (جمع به ۱۵): { $enabled }
scopa-toggle-hints = نمایش راهنمای گرفتن: { $enabled }
scopa-set-mechanic = مکانیک اسکوپا: { $mechanic }
scopa-select-mechanic = مکانیک اسکوپا را انتخاب کنید
scopa-toggle-instant-win = برد فوری با اسکوپا: { $enabled }
scopa-toggle-team-scoring = جمع کارت‌های تیم برای امتیازدهی: { $enabled }
scopa-toggle-inverse = حالت معکوس (رسیدن به هدف = حذف): { $enabled }

# Option change announcements
scopa-option-changed-cards = کارت در هر دست به { $cards } تنظیم شد.
scopa-option-changed-decks = تعداد دسته‌ها به { $decks } تنظیم شد.
scopa-option-changed-escoba = اسکوبا { $enabled }.
scopa-option-changed-hints = راهنماهای گرفتن { $enabled }.
scopa-option-changed-mechanic = مکانیک اسکوپا به { $mechanic } تنظیم شد.
scopa-option-changed-instant = برد فوری با اسکوپا { $enabled }.
scopa-option-changed-team-scoring = امتیازدهی کارت تیم { $enabled }.
scopa-option-changed-inverse = حالت معکوس { $enabled }.

# Scopa mechanic choices
scopa-mechanic-normal = عادی
scopa-mechanic-no_scopas = بدون اسکوپا
scopa-mechanic-only_scopas = فقط اسکوپا

# Disabled action reasons
scopa-timer-not-active = تایمر دور فعال نیست.

# Validation errors
scopa-error-not-enough-cards = کارت کافی در { $decks } { $decks ->
    [one] دسته
    *[other] دسته
} برای { $players } { $players ->
    [one] بازیکن
    *[other] بازیکن
} با { $cards_per_deal } کارت برای هرکدام نیست. (نیاز به { $cards_per_deal } × { $players } = { $cards_needed } کارت، اما فقط { $total_cards } وجود دارد.)
