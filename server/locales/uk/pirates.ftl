# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = Пірати загублених морів

# Game start and setup
pirates-welcome = Ласкаво просимо до Піратів загублених морів! Плавайте морями, збирайте самоцвіти та бийтеся з іншими піратами!
pirates-oceans = Ваша подорож проведе вас через: { $oceans }
pirates-gems-placed = { $total } самоцвітів розкидано по морям. Знайдіть їх усі!
pirates-golden-moon = Золотий місяць піднімається! Всі здобуття досвіду потроюються цього раунду!

# Turn announcements
pirates-turn = Хід { $player }. Позиція { $position }

# Movement actions
pirates-move-left = Плисти ліворуч
pirates-move-right = Плисти праворуч
pirates-move-2-left = Плисти на 2 плитки ліворуч
pirates-move-2-right = Плисти на 2 плитки праворуч
pirates-move-3-left = Плисти на 3 плитки ліворуч
pirates-move-3-right = Плисти на 3 плитки праворуч

# Movement messages
pirates-move-you = Ви пливете { $direction } до позиції { $position }.
pirates-move-you-tiles = Ви пливете на { $tiles } плиток { $direction } до позиції { $position }.
pirates-move = { $player } пливе { $direction } до позиції { $position }.
pirates-map-edge = Ви не можете плисти далі. Ви на позиції { $position }.

# Position and status
pirates-check-status = Перевірити статус
pirates-check-position = Перевірити позицію
pirates-check-moon = Перевірити яскравість місяця
pirates-your-position = Ваша позиція: { $position } в { $ocean }
pirates-moon-brightness = Золотий місяць { $brightness }% яскравий. ({ $collected } з { $total } самоцвітів зібрано).
pirates-no-golden-moon = Золотий місяць зараз не видно на небі.

# Gem collection
pirates-gem-found-you = Ви знайшли { $gem }! Вартість { $value } очок.
pirates-gem-found = { $player } знайшов { $gem }! Вартість { $value } очок.
pirates-all-gems-collected = Всі самоцвіти зібрано!

# Winner
pirates-winner = { $player } виграє з { $score } очками!

# Skills menu
pirates-use-skill = Використати навичку
pirates-select-skill = Виберіть навичку для використання

# Combat - Attack initiation
pirates-cannonball = Вистрілити ядром
pirates-no-targets = Немає цілей в межах { $range } плиток.
pirates-attack-you-fire = Ви стріляєте ядром по { $target }!
pirates-attack-incoming = { $attacker } стріляє ядром по вас!
pirates-attack-fired = { $attacker } стріляє ядром по { $defender }!

# Combat - Rolls
pirates-attack-roll = Кидок атаки: { $roll }
pirates-attack-bonus = Бонус атаки: +{ $bonus }
pirates-defense-roll = Кидок захисту: { $roll }
pirates-defense-roll-others = { $player } кидає { $roll } для захисту.
pirates-defense-bonus = Бонус захисту: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = Пряме влучання! Ви вдарили { $target }!
pirates-attack-hit-them = Вас вдарив { $attacker }!
pirates-attack-hit = { $attacker } влучає в { $defender }!

# Combat - Miss results
pirates-attack-miss-you = Ваше ядро не влучило в { $target }.
pirates-attack-miss-them = Ядро не влучило у вас!
pirates-attack-miss = Ядро { $attacker } не влучає в { $defender }.

# Combat - Push
pirates-push-you = Ви штовхаєте { $target } { $direction } до позиції { $position }!
pirates-push-them = { $attacker } штовхає вас { $direction } до позиції { $position }!
pirates-push = { $attacker } штовхає { $defender } { $direction } з { $old_pos } до { $new_pos }.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } намагається вкрасти самоцвіт!
pirates-steal-rolls = Кидок крадіжки: { $steal } проти захисту: { $defend }
pirates-steal-success-you = Ви вкрали { $gem } у { $target }!
pirates-steal-success-them = { $attacker } вкрав ваш { $gem }!
pirates-steal-success = { $attacker } краде { $gem } у { $defender }!
pirates-steal-failed = Спроба крадіжки провалилась!

# XP and Leveling
pirates-xp-gained = +{ $xp } досвіду
pirates-level-up = { $player } досяг рівня { $level }!
pirates-level-up-you = Ви досягли рівня { $level }!
pirates-level-up-multiple = { $player } отримав { $levels } рівнів! Тепер рівень { $level }!
pirates-level-up-multiple-you = Ви отримали { $levels } рівнів! Тепер рівень { $level }!
pirates-skills-unlocked = { $player } відкрив нові навички: { $skills }.
pirates-skills-unlocked-you = Ви відкрили нові навички: { $skills }.

# Skill activation
pirates-skill-activated = { $player } активує { $skill }!
pirates-buff-expired = Бонус { $skill } { $player } закінчився.

# Sword Fighter skill
pirates-sword-fighter-activated = Мечник активовано! +4 бонус атаки на { $turns } ходів.

# Push skill (defense buff)
pirates-push-activated = Поштовх активовано! +3 бонус захисту на { $turns } ходів.

# Skilled Captain skill
pirates-skilled-captain-activated = Досвідчений капітан активовано! +2 атаки та +2 захисту на { $turns } ходів.

# Double Devastation skill
pirates-double-devastation-activated = Подвійне спустошення активовано! Дальність атаки збільшена до 10 плиток на { $turns } ходів.

# Battleship skill
pirates-battleship-activated = Лінкор активовано! Ви можете зробити два постріли цього ходу!
pirates-battleship-no-targets = Немає цілей для пострілу { $shot }.
pirates-battleship-shot = Здійснюємо постріл { $shot }...

# Portal skill
pirates-portal-no-ships = Немає інших кораблів у полі зору для порталу.
pirates-portal-fizzle = Портал { $player } згасає без призначення.
pirates-portal-success = { $player } телепортується до { $ocean } на позицію { $position }!

# Gem Seeker skill
pirates-gem-seeker-reveal = Моря шепочуть про { $gem } на позиції { $position }. ({ $uses } використань залишилось)

# Level requirements
pirates-requires-level-15 = Вимагає рівень 15
pirates-requires-level-150 = Вимагає рівень 150

# XP Multiplier options
pirates-set-combat-xp-multiplier = множник досвіду за бій: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = досвід за бій
pirates-set-find-gem-xp-multiplier = множник досвіду за знахідку самоцвіту: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = досвід за знахідку самоцвіту

# Gem stealing options
pirates-set-gem-stealing = Крадіжка самоцвітів: { $mode }
pirates-select-gem-stealing = Виберіть режим крадіжки самоцвітів
pirates-option-changed-stealing = Крадіжку самоцвітів встановлено на { $mode }.

# Gem stealing mode choices
pirates-stealing-with-bonus = З бонусом кидка
pirates-stealing-no-bonus = Без бонусу кидка
pirates-stealing-disabled = Вимкнено
