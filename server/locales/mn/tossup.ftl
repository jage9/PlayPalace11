# Toss Up game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-tossup = Шидэлт
tossup-category = Шооны тоглоомууд

# Actions
tossup-roll-first = { $count } шоо шидэх
tossup-roll-remaining = Үлдсэн { $count } шоо шидэх
tossup-bank = { $points } оноо хадгалах

# Game events
tossup-turn-start = { $player }-ийн ээлж. Оноо: { $score }
tossup-you-roll = Та { $results } гаргалаа.
tossup-player-rolls = { $player } { $results } гаргалаа.

# Turn status
tossup-you-have-points = Ээлжийн оноо: { $turn_points }. Үлдсэн шоо: { $dice_count }.
tossup-player-has-points = { $player } { $turn_points } ээлжийн оноотой. { $dice_count } шоо үлдсэн.

# Fresh dice
tossup-you-get-fresh = Шоо дууслаа! { $count } шинэ шоо авч байна.
tossup-player-gets-fresh = { $player } { $count } шинэ шоо авлаа.

# Bust
tossup-you-bust = Унасан! Та энэ ээлжинд { $points } оноо алдлаа.
tossup-player-busts = { $player } унаад { $points } оноо алдлаа!

# Bank
tossup-you-bank = Та { $points } оноо хадгаллаа. Нийт оноо: { $total }.
tossup-player-banks = { $player } { $points } оноо хадгаллаа. Нийт оноо: { $total }.

# Winner
tossup-winner = { $player } { $score } оноогоор ялалт байгууллаа!
tossup-tie-tiebreaker = { $players } хооронд тэнцлээ! Тэнцэл шийдэх тойрог!

# Options
tossup-set-rules-variant = Дүрмийн хувилбар: { $variant }
tossup-select-rules-variant = Дүрмийн хувилбар сонгоно уу:
tossup-option-changed-rules = Дүрмийн хувилбар { $variant } болов

tossup-set-starting-dice = Эхлэх шоо: { $count }
tossup-enter-starting-dice = Эхлэх шооны тоо оруулна уу:
tossup-option-changed-dice = Эхлэх шоо { $count } болов

# Rules variants
tossup-rules-standard = Стандарт
tossup-rules-playpalace = PlayPalace

# Rules explanations
tossup-rules-standard-desc = Шоо тус бүрт 3 ногоон, 2 шар, 1 улаан. Ногоон байхгүй бөгөөд хамгийн багадаа нэг улаан бол унана.
tossup-rules-playpalace-desc = Тэнцүү хуваарилалт. Бүх шоо улаан бол унана.

# Disabled reasons
tossup-need-points = Хадгалахын тулд оноо хэрэгтэй.
