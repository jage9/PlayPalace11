# Yahtzee game messages

# Game info
game-name-yahtzee = Яцзи

# Actions - Rolling
yahtzee-roll = Дахин шидэх ({ $count } үлдсэн)
yahtzee-roll-all = Шоо шидэх

# Upper section scoring categories
yahtzee-score-ones = Нэгийнх { $points } оноо
yahtzee-score-twos = Хоёрынх { $points } оноо
yahtzee-score-threes = Гурвынх { $points } оноо
yahtzee-score-fours = Дөрвийнх { $points } оноо
yahtzee-score-fives = Тавынх { $points } оноо
yahtzee-score-sixes = Зургаанынх { $points } оноо

# Lower section scoring categories
yahtzee-score-three-kind = Гурвын төрөл { $points } оноо
yahtzee-score-four-kind = Дөрвийн төрөл { $points } оноо
yahtzee-score-full-house = Бүтэн байшин { $points } оноо
yahtzee-score-small-straight = Бага дараалал { $points } оноо
yahtzee-score-large-straight = Том дараалал { $points } оноо
yahtzee-score-yahtzee = Яцзи { $points } оноо
yahtzee-score-chance = Боломж { $points } оноо

# Game events
yahtzee-you-rolled = Та шидсэн: { $dice }. Үлдсэн шидэлт: { $remaining }
yahtzee-player-rolled = { $player } шидсэн: { $dice }. Үлдсэн шидэлт: { $remaining }

# Scoring announcements
yahtzee-you-scored = Та { $category }-д { $points } оноо авлаа.
yahtzee-player-scored = { $player } { $category }-д { $points } оноо авлаа.

# Yahtzee bonus
yahtzee-you-bonus = Яцзийн урамшуулал! +100 оноо
yahtzee-player-bonus = { $player } Яцзийн урамшуулал авлаа! +100 оноо

# Upper section bonus
yahtzee-you-upper-bonus = Дээд хэсгийн урамшуулал! +35 оноо (дээд хэсэгт { $total })
yahtzee-player-upper-bonus = { $player } дээд хэсгийн урамшуулал авлаа! +35 оноо
yahtzee-you-upper-bonus-missed = Та дээд хэсгийн урамшууллыг алдлаа (дээд хэсэгт { $total }, 63 хэрэгтэй байсан).
yahtzee-player-upper-bonus-missed = { $player } дээд хэсгийн урамшууллыг алдлаа.

# Scoring mode
yahtzee-choose-category = Оноо тооцох ангилал сонгоно уу.
yahtzee-continuing = Ээлжийг үргэлжлүүлж байна.

# Status checks
yahtzee-check-scoresheet = Оноо хүснэгт шалгах
yahtzee-view-dice = Гар шалгах
yahtzee-your-dice = Таны шоо: { $dice }.
yahtzee-your-dice-kept = Таны шоо: { $dice }. Хадгалсан: { $kept }
yahtzee-not-rolled = Та одоогоор шидээгүй байна.

# Scoresheet display
yahtzee-scoresheet-header = === { $player }-ын оноо хүснэгт ===
yahtzee-scoresheet-upper = Дээд хэсэг:
yahtzee-scoresheet-lower = Доод хэсэг:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = Дээд нийт: { $total } (УРАМШУУЛАЛ: +35)
yahtzee-scoresheet-upper-total-needed = Дээд нийт: { $total } (урамшууллын тулд { $needed } дутуу)
yahtzee-scoresheet-yahtzee-bonus = Яцзийн урамшуулал: { $count } x 100 = { $total }
yahtzee-scoresheet-grand-total = НИЙТ ОНОО: { $total }

# Category names (for announcements)
yahtzee-category-ones = Нэгийнх
yahtzee-category-twos = Хоёрынх
yahtzee-category-threes = Гурвынх
yahtzee-category-fours = Дөрвийнх
yahtzee-category-fives = Тавынх
yahtzee-category-sixes = Зургаанынх
yahtzee-category-three-kind = Гурвын төрөл
yahtzee-category-four-kind = Дөрвийн төрөл
yahtzee-category-full-house = Бүтэн байшин
yahtzee-category-small-straight = Бага дараалал
yahtzee-category-large-straight = Том дараалал
yahtzee-category-yahtzee = Яцзи
yahtzee-category-chance = Боломж

# Game end
yahtzee-winner = { $player } { $score } оноогоор ялав!
yahtzee-winners-tie = Тэнцсэн! { $players } бүгд { $score } оноо авлаа!

# Options
yahtzee-set-rounds = Тоглолтын тоо: { $rounds }
yahtzee-enter-rounds = Тоглолтын тоо оруулна уу (1-10):
yahtzee-option-changed-rounds = Тоглолтын тоо { $rounds } болж өөрчлөгдлөө.

# Disabled action reasons
yahtzee-no-rolls-left = Танд шидэлт үлдээгүй байна.
yahtzee-roll-first = Та эхлээд шидэх хэрэгтэй.
yahtzee-category-filled = Тэр ангилал аль хэдийн бөглөгдсөн байна.
