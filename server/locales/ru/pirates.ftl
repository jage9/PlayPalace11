# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = Пираты затерянных морей

# Game start and setup
pirates-welcome = Добро пожаловать в игру «Пираты затерянных морей»! Бороздите океаны, собирайте самоцветы и сражайтесь с другими пиратами!
pirates-oceans = Ваше странствие пройдёт через: { $oceans }.
pirates-gems-placed = По всем морям было рассеяно { $total } { $total ->
    [one] самоцвет
    [few] самоцвета
   *[other] самоцветов
}. Найдите их все!
pirates-golden-moon = Всходит Золотая луна! Весь получаемый опыт в этом раунде утроен!

# Turn announcements
pirates-turn = Ход игрока { $player }. Позиция: { $position }.

# Movement actions
pirates-move-left = Плыть влево
pirates-move-right = Плыть вправо
pirates-move-2-left = Проплыть 2 клетки влево
pirates-move-2-right = Проплыть 2 клетки вправо
pirates-move-3-left = Проплыть 3 клетки влево
pirates-move-3-right = Проплыть 3 клетки вправо

# Movement messages
pirates-move-you = Вы плывёте { $direction } на позицию { $position }.
pirates-move-you-tiles = Вы проплываете { $tiles } { $tiles ->
    [one] клетку
    [few] клетки
   *[other] клеток
} { $direction } на позицию { $position }.
pirates-move = { $player } плывёт { $direction } на позицию { $position }.
pirates-map-edge = Вы не можете плыть дальше. Ваша позиция: { $position }.

# Position and status
pirates-check-status = Проверить статус
pirates-check-status-detailed = Подробный статус
pirates-check-position = Проверить позицию
pirates-check-moon = Проверить яркость луны
pirates-your-position = Ваша позиция: { $position } (океан: { $ocean })
pirates-moon-brightness = Яркость Золотой луны: { $brightness }%. (Собрано { $collected } из { $total } самоцветов).
pirates-no-golden-moon = Золотой луны сейчас не видно на небосводе.

# Gem collection
pirates-gem-found-you = Вы нашли самоцвет ({ $gem })! Стоимость: { $value } { $value ->
    [one] очко
    [few] очка
   *[other] очков
}.
pirates-gem-found = { $player } находит самоцвет ({ $gem })! Стоимость: { $value } { $value ->
    [one] очко
    [few] очка
   *[other] очков
}.
pirates-all-gems-collected = Все самоцветы собраны!

# Winner
pirates-winner = { $player } побеждает со счётом { $score }!

# Skills menu
pirates-use-skill = Использовать навык
pirates-select-skill = Выберите навык для использования

# Combat - Attack initiation
pirates-cannonball = Выстрелить из пушки
pirates-no-targets = Нет целей в радиусе { $range } { $range ->
    [one] клетки
    [few] клеток
   *[other] клеток
}.
pirates-attack-you-fire = Вы стреляете пушечным ядром в игрока { $target }!
pirates-attack-incoming = { $attacker } стреляет в вас пушечным ядром!
pirates-attack-fired = { $attacker } стреляет пушечным ядром в игрока { $defender }!

# Combat - Rolls
pirates-attack-roll = Бросок атаки: { $roll }
pirates-attack-bonus = Бонус к атаке: +{ $bonus }
pirates-defense-roll = Бросок защиты: { $roll }
pirates-defense-roll-others = { $player } выбрасывает { $roll } для защиты.
pirates-defense-bonus = Бонус к защите: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = Прямое попадание! Вы поразили цель ({ $target })!
pirates-attack-hit-them = В вас попал { $attacker }!
pirates-attack-hit = { $attacker } попадает в игрока { $defender }!

# Combat - Miss results
pirates-attack-miss-you = Ваше ядро прошло мимо игрока { $target }.
pirates-attack-miss-them = Пушечное ядро пролетело мимо вас!
pirates-attack-miss = { $attacker } промахивается по игроку { $defender }.

# Combat - Push
pirates-push-you = Вы отталкиваете { $target } { $direction } на позицию { $position }!
pirates-push-them = { $attacker } отталкивает вас { $direction } на позицию { $position }!
pirates-push = { $attacker } отталкивает { $defender } { $direction } с позиции { $old_pos } на { $new_pos }.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } пытается украсть самоцвет!
pirates-steal-rolls = Бросок кражи: { $steal } против защиты: { $defend }
pirates-steal-success-you = Вы украли самоцвет ({ $gem }) у игрока { $target }!
pirates-steal-success-them = { $attacker } крадёт ваш самоцвет ({ $gem })!
pirates-steal-success = { $attacker } крадёт самоцвет ({ $gem }) у игрока { $defender }!
pirates-steal-failed = Попытка кражи провалилась!

# XP and Leveling
pirates-xp-gained = +{ $xp } ед. опыта
pirates-level-up = { $player } достигает { $level } уровня!
pirates-level-up-you = Вы достигли { $level } уровня!
pirates-level-up-multiple = { $player } получает сразу несколько уровней ({ $levels })! Теперь уровень: { $level }.
pirates-level-up-multiple-you = Вы получили сразу несколько уровней ({ $levels })! Теперь уровень: { $level }.
pirates-skills-unlocked = { $player } открывает новые навыки: { $skills }.
pirates-skills-unlocked-you = Вы открыли новые навыки: { $skills }.

# Skill activation
pirates-skill-activated = { $player } активирует навык «{ $skill }»!
pirates-buff-expired = Эффект навыка «{ $skill }» у игрока { $player } истёк.

# Sword Fighter skill
pirates-sword-fighter-activated = «Мастер меча» активирован! +4 к бонусу атаки на { $turns } { $turns ->
    [one] ход
    [few] хода
   *[other] ходов
}.

# Push skill (defense buff)
pirates-push-activated = «Толкание» активировано! +3 к бонусу защиты на { $turns } { $turns ->
    [one] ход
    [few] хода
   *[other] ходов
}.

# Skilled Captain skill
pirates-skilled-captain-activated = «Опытный капитан» активирован! +2 к атаке и +2 к защите на { $turns } { $turns ->
    [one] ход
    [few] хода
   *[other] ходов
}.

# Double Devastation skill
pirates-double-devastation-activated = «Двойное опустошение» активировано! Дальность атаки увеличена до 10 клеток на { $turns } { $turns ->
    [one] ход
    [few] хода
   *[other] ходов
}.

# Battleship skill
pirates-battleship-activated = «Линкор» активирован! Вы можете сделать два выстрела в этот ход!
pirates-battleship-no-targets = Нет целей для выстрела №{ $shot }.
pirates-battleship-shot = Производится выстрел №{ $shot }...

# Portal skill
pirates-portal-no-ships = В поле зрения нет других кораблей для создания портала.
pirates-portal-fizzle = Портал игрока { $player } закрывается, так и не найдя цели.
pirates-portal-success = { $player } перемещается через портал в { $ocean } на позицию { $position }!

# Gem Seeker skill
pirates-gem-seeker-reveal = Морские волны шепчут, что на позиции { $position } есть самоцвет ({ $gem }). (Осталось использований: { $uses })

# Level requirements
pirates-requires-level-15 = Требуется уровень 15
pirates-requires-level-150 = Требуется уровень 150

# XP Multiplier options
pirates-set-combat-xp-multiplier = Множитель опыта за бой: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = Введите множитель опыта за бой
pirates-set-find-gem-xp-multiplier = Множитель опыта за находку самоцвета: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = Введите множитель опыта за нахождение самоцвета

# Gem stealing options
pirates-set-gem-stealing = Кража самоцветов: { $mode }
pirates-select-gem-stealing = Выберите режим кражи самоцветов
pirates-option-changed-stealing = Режим кражи самоцветов изменён на: { $mode }.

# Gem stealing mode choices
pirates-stealing-with-bonus = С бонусом к броску
pirates-stealing-no-bonus = Без бонуса к броску
pirates-stealing-disabled = Отключена
# Skill/status messages use the English locale fallback until translated.
pirates-skill-name-cannonball = Cannonball Shot
pirates-skill-name-instinct = Sailor's Instinct
pirates-skill-name-portal = Portal
pirates-skill-name-gem-seeker = Gem Seeker
pirates-skill-name-sword-fighter = Sword Fighter
pirates-skill-name-push = Push
pirates-skill-name-skilled-captain = Skilled Captain
pirates-skill-name-battleship = Battleship
pirates-skill-name-double-devastation = Double Devastation
pirates-skill-requires-level = Requires level { $level }
pirates-skill-already-active = { $skill } is already active ({ $turns } turns remaining)
pirates-skill-on-cooldown = { $skill } is on cooldown ({ $turns } turns)
pirates-skill-active = { $skill } (active: { $turns } turns)
pirates-skill-cooldown = { $skill } (cooldown: { $turns } turns)
pirates-skill-activate = { $skill } (activate)
pirates-skill-no-uses = { $skill } (no uses remaining)
pirates-skill-uses-left = { $skill } ({ $uses } uses left)
pirates-portal-menu = { $skill } (teleport to occupied ocean)
pirates-battleship-menu = { $skill } (fire extra shot)
pirates-not-your-turn = Not your turn
pirates-no-uses-remaining = No uses remaining
pirates-cannot-battleship-double = Cannot use Battleship while Double Devastation is active
pirates-no-targets-in-range = No targets in range
pirates-unknown = Unknown
pirates-map-sectors = Map Sectors:
pirates-charted-full = Fully charted
pirates-charted-partial = Partially charted ({ $count }/5)
pirates-charted-none = Uncharted
pirates-sector = Sector { $sector } ({ $start }-{ $end }): { $status }
pirates-status-player = { $player }: Level { $level }, { $xp } XP, { $score } points, { $gems }
