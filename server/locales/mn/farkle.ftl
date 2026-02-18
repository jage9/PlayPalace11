# Farkle game messages

# Game info
game-name-farkle = Фаркл

# Actions - Roll and Bank
farkle-roll = { $count } { $count ->
    [one] шоо
   *[other] шоо
} шидэх
farkle-bank = { $points } оноо хадгалах

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = Нэг 1-ийн оноо { $points }
farkle-take-single-five = Нэг 5-ын оноо { $points }
farkle-take-three-kind = Гурван { $number }-ын оноо { $points }
farkle-take-four-kind = Дөрвөн { $number }-ын оноо { $points }
farkle-take-five-kind = Таван { $number }-ын оноо { $points }
farkle-take-six-kind = Зургаан { $number }-ын оноо { $points }
farkle-take-small-straight = Бага дараалал { $points } оноо
farkle-take-large-straight = Том дараалал { $points } оноо
farkle-take-three-pairs = Гурван хос { $points } оноо
farkle-take-double-triplets = Давхар гурвал { $points } оноо
farkle-take-full-house = Бүтэн байшин { $points } оноо

# Game events (matching v10 exactly)
farkle-rolls = { $player } { $count } { $count ->
    [one] шоо
   *[other] шоо
} шидэж байна...
farkle-you-roll = Та { $count } { $count ->
    [one] шоо
   *[other] шоо
} шидэж байна...
farkle-roll-result = { $dice }
farkle-farkle = ФАРКЛ! { $player } { $points } оноо алдлаа
farkle-you-farkle = ФАРКЛ! Та { $points } оноо алдлаа
farkle-takes-combo = { $player } { $combo } авч { $points } оноо олов
farkle-you-take-combo = Та { $combo } авч { $points } оноо оллоо
farkle-hot-dice = Халуун шоо!
farkle-banks = { $player } { $points } оноо хадгалж, нийт { $total } боллоо
farkle-you-bank = Та { $points } оноо хадгалж, нийт { $total } боллоо
farkle-winner = { $player } { $score } оноогоор ялав!
farkle-you-win = Та { $score } оноогоор яллаа!
farkle-winners-tie = Тэнцсэн! Ялагчид: { $players }

# Check turn score action
farkle-turn-score = { $player } энэ ээлжиндээ { $points } оноотой байна.
farkle-no-turn = Одоо хэн ч ээлж авахгүй байна.

# Farkle-specific options
farkle-set-target-score = Зорилтот оноо: { $score }
farkle-enter-target-score = Зорилтот оноо оруулна уу (500-5000):
farkle-option-changed-target = Зорилтот оноо { $score } болж өөрчлөгдлөө.

# Disabled action reasons
farkle-must-take-combo = Та эхлээд оноотой хослол авах ёстой.
farkle-cannot-bank = Та одоо хадгалж чадахгүй.

# Additional Farkle options
farkle-set-initial-bank-score = Эхний банк хийх оноо: { $score }
farkle-enter-initial-bank-score = Эхний банк хийх оноог оруулна уу (0-1000):
farkle-option-changed-initial-bank-score = Эхний банк хийх оноог { $score } болголоо.
farkle-toggle-hot-dice-multiplier = Халуун шооны үржүүлэгч: { $enabled }
farkle-option-changed-hot-dice-multiplier = Халуун шооны үржүүлэгчийг { $enabled } болголоо.

# Action feedback
farkle-minimum-initial-bank-score = Эхний банк хийх доод оноо { $score }.
