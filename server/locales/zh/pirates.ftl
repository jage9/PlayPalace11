# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = 失落海域的海盗

# Game start and setup
pirates-welcome = 欢迎来到失落海域的海盗！航行于海洋，收集宝石，与其他海盗战斗！
pirates-oceans = 你的航程将穿越：{ $oceans }
pirates-gems-placed = { $total }颗宝石已散落在海洋中。找到它们全部！
pirates-golden-moon = 金月升起！本回合所有XP获得三倍！

# Turn announcements
pirates-turn = { $player }的回合。位置{ $position }

# Movement actions
pirates-move-left = 向左航行
pirates-move-right = 向右航行
pirates-move-2-left = 向左航行2格
pirates-move-2-right = 向右航行2格
pirates-move-3-left = 向左航行3格
pirates-move-3-right = 向右航行3格

# Movement messages
pirates-move-you = 你向{ $direction }航行到位置{ $position }。
pirates-move-you-tiles = 你向{ $direction }航行{ $tiles }格到位置{ $position }。
pirates-move = { $player }向{ $direction }航行到位置{ $position }。
pirates-map-edge = 你不能再航行更远了。你在位置{ $position }。

# Position and status
pirates-check-status = 检查状态
pirates-check-status-detailed = 详细状态
pirates-check-position = 检查位置
pirates-check-moon = 检查月亮亮度
pirates-your-position = 你的位置：{ $ocean }的{ $position }
pirates-moon-brightness = 金月亮度为{ $brightness }%。（已收集{ $collected }/{ $total }颗宝石）。
pirates-no-golden-moon = 金月现在无法在天空中看到。

# Gem collection
pirates-gem-found-you = 你找到了{ $gem }！价值{ $value }点。
pirates-gem-found = { $player }找到了{ $gem }！价值{ $value }点。
pirates-all-gems-collected = 所有宝石都已被收集！

# Winner
pirates-winner = { $player }以{ $score }点获胜！

# Skills menu
pirates-use-skill = 使用技能
pirates-select-skill = 选择要使用的技能

# Combat - Attack initiation
pirates-cannonball = 发射炮弹
pirates-no-targets = { $range }格内没有目标。
pirates-attack-you-fire = 你向{ $target }发射炮弹！
pirates-attack-incoming = { $attacker }向你发射炮弹！
pirates-attack-fired = { $attacker }向{ $defender }发射炮弹！

# Combat - Rolls
pirates-attack-roll = 攻击掷骰：{ $roll }
pirates-attack-bonus = 攻击加成：+{ $bonus }
pirates-defense-roll = 防御掷骰：{ $roll }
pirates-defense-roll-others = { $player }掷出{ $roll }进行防御。
pirates-defense-bonus = 防御加成：+{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = 直接命中！你击中了{ $target }！
pirates-attack-hit-them = 你被{ $attacker }击中了！
pirates-attack-hit = { $attacker }击中{ $defender }！

# Combat - Miss results
pirates-attack-miss-you = 你的炮弹未击中{ $target }。
pirates-attack-miss-them = 炮弹未击中你！
pirates-attack-miss = { $attacker }的炮弹未击中{ $defender }。

# Combat - Push
pirates-push-you = 你将{ $target }推向{ $direction }到位置{ $position }！
pirates-push-them = { $attacker }将你推向{ $direction }到位置{ $position }！
pirates-push = { $attacker }将{ $defender }从{ $old_pos }推向{ $direction }到{ $new_pos }。

# Combat - Gem stealing
pirates-steal-attempt = { $attacker }试图偷取宝石！
pirates-steal-rolls = 偷窃掷骰：{ $steal } vs 防御：{ $defend }
pirates-steal-success-you = 你从{ $target }偷到了{ $gem }！
pirates-steal-success-them = { $attacker }偷走了你的{ $gem }！
pirates-steal-success = { $attacker }从{ $defender }偷到{ $gem }！
pirates-steal-failed = 偷窃失败！

# XP and Leveling
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player }达到等级{ $level }！
pirates-level-up-you = 你达到等级{ $level }！
pirates-level-up-multiple = { $player }升了{ $levels }级！现在是等级{ $level }！
pirates-level-up-multiple-you = 你升了{ $levels }级！现在是等级{ $level }！
pirates-skills-unlocked = { $player }解锁了新技能：{ $skills }。
pirates-skills-unlocked-you = 你解锁了新技能：{ $skills }。

# Skill activation
pirates-skill-activated = { $player }激活{ $skill }！
pirates-buff-expired = { $player }的{ $skill }增益效果已消失。

# Sword Fighter skill
pirates-sword-fighter-activated = 剑客激活！攻击加成+4，持续{ $turns }回合。

# Push skill (defense buff)
pirates-push-activated = 推击激活！防御加成+3，持续{ $turns }回合。

# Skilled Captain skill
pirates-skilled-captain-activated = 熟练船长激活！攻击+2和防御+2，持续{ $turns }回合。

# Double Devastation skill
pirates-double-devastation-activated = 双重毁灭激活！攻击范围增加到10格，持续{ $turns }回合。

# Battleship skill
pirates-battleship-activated = 战舰激活！本回合你可以发射两次炮弹！
pirates-battleship-no-targets = 第{ $shot }次射击没有目标。
pirates-battleship-shot = 发射第{ $shot }次射击...

# Portal skill
pirates-portal-no-ships = 没有其他船只可以传送。
pirates-portal-fizzle = { $player }的传送门消失了，没有目的地。
pirates-portal-success = { $player }传送到{ $ocean }的位置{ $position }！

# Gem Seeker skill
pirates-gem-seeker-reveal = 海洋低语着位置{ $position }有{ $gem }。（剩余{ $uses }次使用）

# Level requirements
pirates-requires-level-15 = 需要等级15
pirates-requires-level-150 = 需要等级150

# XP Multiplier options
pirates-set-combat-xp-multiplier = 战斗经验倍数：{ $combat_multiplier }
pirates-enter-combat-xp-multiplier = 战斗经验
pirates-set-find-gem-xp-multiplier = 找到宝石经验倍数：{ $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = 找到宝石的经验

# Gem stealing options
pirates-set-gem-stealing = 宝石偷窃：{ $mode }
pirates-select-gem-stealing = 选择宝石偷窃模式
pirates-option-changed-stealing = 宝石偷窃设置为{ $mode }。

# Gem stealing mode choices
pirates-stealing-with-bonus = 带掷骰加成
pirates-stealing-no-bonus = 无掷骰加成
pirates-stealing-disabled = 禁用
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
