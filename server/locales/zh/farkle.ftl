# Farkle 游戏消息 (简体中文)

# 游戏信息
game-name-farkle = 法克尔

# 操作 - 掷骰和存分
farkle-roll = 掷 { $count } 个骰子
farkle-bank = 存入 { $points } 分

# 得分组合操作（与v10完全匹配）
farkle-take-single-one = 单个1得 { $points } 分
farkle-take-single-five = 单个5得 { $points } 分
farkle-take-three-kind = 三个 { $number } 得 { $points } 分
farkle-take-four-kind = 四个 { $number } 得 { $points } 分
farkle-take-five-kind = 五个 { $number } 得 { $points } 分
farkle-take-six-kind = 六个 { $number } 得 { $points } 分
farkle-take-small-straight = 小顺子得 { $points } 分
farkle-take-large-straight = 大顺子得 { $points } 分
farkle-take-three-pairs = 三对得 { $points } 分
farkle-take-double-triplets = 双三条得 { $points } 分
farkle-take-full-house = 葫芦得 { $points } 分

# 游戏事件（与v10完全匹配）
farkle-rolls = { $player } 掷 { $count } 个骰子...
farkle-you-roll = 你掷 { $count } 个骰子...
farkle-roll-result = { $dice }
farkle-farkle = 法克尔！{ $player } 失去 { $points } 分
farkle-you-farkle = 法克尔！你失去 { $points } 分
farkle-takes-combo = { $player } 拿走 { $combo } 得 { $points } 分
farkle-you-take-combo = 你拿走 { $combo } 得 { $points } 分
farkle-hot-dice = 热骰子！
farkle-banks = { $player } 存入 { $points } 分，总计 { $total }
farkle-you-bank = 你存入 { $points } 分，总计 { $total }
farkle-winner = { $player } 以 { $score } 分获胜！
farkle-you-win = 你以 { $score } 分获胜！
farkle-winners-tie = 平局！获胜者：{ $players }

# 检查回合得分操作
farkle-turn-score = { $player } 本回合有 { $points } 分。
farkle-no-turn = 当前没有人在进行回合。

# Farkle特定选项
farkle-set-target-score = 目标分数：{ $score }
farkle-enter-target-score = 输入目标分数（500-5000）：
farkle-option-changed-target = 目标分数设置为 { $score }。

# 操作禁用原因
farkle-must-take-combo = 你必须先拿走一个得分组合。
farkle-cannot-bank = 你现在不能存分。

# Additional Farkle options
farkle-set-initial-bank-score = 首次存分门槛: { $score }
farkle-enter-initial-bank-score = 输入首次存分门槛 (0-1000):
farkle-option-changed-initial-bank-score = 首次存分门槛已设置为 { $score }。
farkle-toggle-hot-dice-multiplier = 热骰倍率: { $enabled }
farkle-option-changed-hot-dice-multiplier = 热骰倍率已设置为 { $enabled }。

# Action feedback
farkle-minimum-initial-bank-score = 首次存分的最低门槛是 { $score }。
