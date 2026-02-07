# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = Алдагдсан тэнгисийн далайн дээрэмчид

# Game start and setup
pirates-welcome = Алдагдсан тэнгисийн далайн дээрэмчид тоглоомд тавтай морил! Далайгаар аялж, эрдэнийн чулуу цуглуулж, бусад далайн дээрэмчидтэй тулал!
pirates-oceans = Таны аялал: { $oceans }
pirates-gems-placed = { $total } эрдэнийн чулуу тэнгист тархсан. Бүгдийг нь ол!
pirates-golden-moon = Алтан сар мандав! Бүх туршлага гурав дахин өсөх болно!

# Turn announcements
pirates-turn = { $player }-ийн ээлж. Байрлал { $position }

# Movement actions
pirates-move-left = Зүүн тийш дарвуулах
pirates-move-right = Баруун тийш дарвуулах
pirates-move-2-left = 2 нүд зүүн тийш дарвуулах
pirates-move-2-right = 2 нүд баруун тийш дарвуулах
pirates-move-3-left = 3 нүд зүүн тийш дарвуулах
pirates-move-3-right = 3 нүд баруун тийш дарвуулах

# Movement messages
pirates-move-you = Та { $direction } тийш { $position } байрлал руу дарвуулав.
pirates-move-you-tiles = Та { $tiles } нүд { $direction } тийш { $position } байрлал руу дарвуулав.
pirates-move = { $player } { $direction } тийш { $position } байрлал руу дарвуулав.
pirates-map-edge = Цааш дарвуулж чадахгүй. Та { $position } байрлалд байна.

# Position and status
pirates-check-status = Төлөв шалгах
pirates-check-position = Байрлал шалгах
pirates-check-moon = Сарны гэрэлтэлт шалгах
pirates-your-position = Таны байрлал: { $ocean }-д { $position }
pirates-moon-brightness = Алтан сар { $brightness }% гэрэлтэж байна. ({ $total }-с { $collected } эрдэнийн чулуу цуглуулсан).
pirates-no-golden-moon = Алтан сар одоо тэнгэрт харагдахгүй байна.

# Gem collection
pirates-gem-found-you = Та { $gem } оллоо! { $value } оноо өгнө.
pirates-gem-found = { $player } { $gem } оллоо! { $value } оноо өгнө.
pirates-all-gems-collected = Бүх эрдэнийн чулуу цуглуулагдлаа!

# Winner
pirates-winner = { $player } { $score } оноогоор ялав!

# Skills menu
pirates-use-skill = Ур чадвар хэрэглэх
pirates-select-skill = Хэрэглэх ур чадвар сонгох

# Combat - Attack initiation
pirates-cannonball = Их буу харвах
pirates-no-targets = { $range } нүдийн зайд бай байхгүй.
pirates-attack-you-fire = Та { $target } руу их буу харвав!
pirates-attack-incoming = { $attacker } танд их буу харвалаа!
pirates-attack-fired = { $attacker } { $defender } руу их буу харвав!

# Combat - Rolls
pirates-attack-roll = Довтолгооны шоо: { $roll }
pirates-attack-bonus = Довтолгооны нэмэлт: +{ $bonus }
pirates-defense-roll = Хамгаалалтын шоо: { $roll }
pirates-defense-roll-others = { $player } хамгаалалтад { $roll } буулгав.
pirates-defense-bonus = Хамгаалалтын нэмэлт: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = Шууд тусав! Та { $target }-г онолоо!
pirates-attack-hit-them = { $attacker } танд тусав!
pirates-attack-hit = { $attacker } { $defender }-д тусав!

# Combat - Miss results
pirates-attack-miss-you = Таны их буу { $target }-г алдлаа.
pirates-attack-miss-them = Их буу танд тусаагүй!
pirates-attack-miss = { $attacker }-ийн их буу { $defender }-г алдав.

# Combat - Push
pirates-push-you = Та { $target }-г { $direction } тийш { $position } байрлал руу түлхэв!
pirates-push-them = { $attacker } таныг { $direction } тийш { $position } байрлал руу түлхэв!
pirates-push = { $attacker } { $defender }-г { $old_pos }-с { $new_pos } руу { $direction } тийш түлхэв.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } эрдэнийн чулуу хулгайлах гэж байна!
pirates-steal-rolls = Хулгайлах шоо: { $steal } vs хамгаалалт: { $defend }
pirates-steal-success-you = Та { $target }-с { $gem } хулгайллаа!
pirates-steal-success-them = { $attacker } таны { $gem }-г хулгайллаа!
pirates-steal-success = { $attacker } { $defender }-с { $gem } хулгайллаа!
pirates-steal-failed = Хулгайлалт амжилтгүй боллоо!

# XP and Leveling
pirates-xp-gained = +{ $xp } туршлага
pirates-level-up = { $player } { $level } түвшинд хүрлээ!
pirates-level-up-you = Та { $level } түвшинд хүрлээ!
pirates-level-up-multiple = { $player } { $levels } түвшин ахив! Одоо { $level } түвшин!
pirates-level-up-multiple-you = Та { $levels } түвшин ахив! Одоо { $level } түвшин!
pirates-skills-unlocked = { $player } шинэ ур чадвар нээлээ: { $skills }.
pirates-skills-unlocked-you = Та шинэ ур чадвар нээлээ: { $skills }.

# Skill activation
pirates-skill-activated = { $player } { $skill } идэвхжүүллээ!
pirates-buff-expired = { $player }-ийн { $skill } нэмэлт дууслаа.

# Sword Fighter skill
pirates-sword-fighter-activated = Сэлэмчин идэвхжлээ! { $turns } ээлжид +4 довтолгооны нэмэлт.

# Push skill (defense buff)
pirates-push-activated = Түлхэлт идэвхжлээ! { $turns } ээлжид +3 хамгаалалтын нэмэлт.

# Skilled Captain skill
pirates-skilled-captain-activated = Чадварлаг ахмад идэвхжлээ! { $turns } ээлжид +2 довтолгоо ба +2 хамгаалалт.

# Double Devastation skill
pirates-double-devastation-activated = Давхар сүйрэл идэвхжлээ! { $turns } ээлжид довтолгооны зай 10 нүд болсон.

# Battleship skill
pirates-battleship-activated = Байлдааны хөлөг идэвхжлээ! Энэ ээлжид хоёр удаа харвах боломжтой!
pirates-battleship-no-targets = { $shot } дахь харвалтад бай байхгүй.
pirates-battleship-shot = { $shot } дахь харвалт хийж байна...

# Portal skill
pirates-portal-no-ships = Портал нээх хөлөг байхгүй байна.
pirates-portal-fizzle = { $player }-ийн портал очих газаргүйгээс аль хэдийн алга болов.
pirates-portal-success = { $player } { $ocean }-д { $position } байрлал руу портал нээв!

# Gem Seeker skill
pirates-gem-seeker-reveal = Тэнгис { $position } байрлалд { $gem } байгааг шивнэв. ({ $uses } ашиглалт үлдсэн)

# Level requirements
pirates-requires-level-15 = 15 түвшин шаардлагатай
pirates-requires-level-150 = 150 түвшин шаардлагатай

# XP Multiplier options
pirates-set-combat-xp-multiplier = тулааны туршлага үржүүлэгч: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = тулааны туршлага
pirates-set-find-gem-xp-multiplier = эрдэнийн чулуу олсон туршлага үржүүлэгч: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = эрдэнийн чулуу олсон туршлага

# Gem stealing options
pirates-set-gem-stealing = Эрдэнийн чулуу хулгайлах: { $mode }
pirates-select-gem-stealing = Эрдэнийн чулуу хулгайлах горим сонгох
pirates-option-changed-stealing = Эрдэнийн чулуу хулгайлах { $mode }-д тохируулагдлаа.

# Gem stealing mode choices
pirates-stealing-with-bonus = Шооны нэмэлттэй
pirates-stealing-no-bonus = Шооны нэмэлтгүй
pirates-stealing-disabled = Идэвхгүй
