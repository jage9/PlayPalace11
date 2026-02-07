# 1-4-24 (Midnight) game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-midnight = 1-4-24
midnight-category = Шооны тоглоомууд

# Actions
midnight-roll = Шоог шидэх
midnight-keep-die = { $value }-г хадгалах
midnight-bank = Хадгалах

# Game events
midnight-turn-start = { $player }-ын ээлж.
midnight-you-rolled = Та шидсэн: { $dice }.
midnight-player-rolled = { $player } шидсэн: { $dice }.

# Keeping dice
midnight-you-keep = Та { $die }-г хадгаллаа.
midnight-player-keeps = { $player } { $die }-г хадгаллаа.
midnight-you-unkeep = Та { $die }-г буцаалаа.
midnight-player-unkeeps = { $player } { $die }-г буцаалаа.

# Turn status
midnight-you-have-kept = Хадгалсан шоо: { $kept }. Үлдсэн шидэлт: { $remaining }.
midnight-player-has-kept = { $player } хадгалсан: { $kept }. { $remaining } шоо үлдсэн.

# Scoring
midnight-you-scored = Та { $score } оноо авлаа.
midnight-scored = { $player } { $score } оноо авлаа.
midnight-you-disqualified = Танд 1 болон 4 аль аль нь байхгүй байна. Хасагдлаа!
midnight-player-disqualified = { $player }-д 1 болон 4 аль аль нь байхгүй байна. Хасагдлаа!

# Round results
midnight-round-winner = { $player } тойрогт ялав!
midnight-round-tie = { $players } хооронд тэнцсэн.
midnight-all-disqualified = Бүх тоглогчид хасагдлаа! Энэ тойрогт ялагч байхгүй.

# Game winner
midnight-game-winner = { $player } { $wins } тойрог ялж тоглолтод түрүүллээ!
midnight-game-tie = Тэнцсэн! { $players } тус бүр { $wins } тойрог яллаа.

# Options
midnight-set-rounds = Тоглох тойрог: { $rounds }
midnight-enter-rounds = Тоглох тойргийн тоог оруулна уу:
midnight-option-changed-rounds = Тоглох тойрог { $rounds } болж өөрчлөгдлөө

# Disabled reasons
midnight-need-to-roll = Та эхлээд шоо шидэх хэрэгтэй.
midnight-no-dice-to-keep = Хадгалах боломжтой шоо байхгүй байна.
midnight-must-keep-one = Та шидэлт бүрт наад зах нь нэг шоог хадгалах ёстой.
midnight-must-roll-first = Та эхлээд шоо шидэх ёстой.
midnight-keep-all-first = Та хадгалахын өмнө бүх шоог хадгалах ёстой.
