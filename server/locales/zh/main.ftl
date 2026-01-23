# PlayPalace 主界面消息 (简体中文)

# 游戏分类
category-card-games = 纸牌游戏
category-dice-games = 骰子游戏
category-rb-play-center = RB Play Center
category-poker = 扑克
category-uncategorized = 未分类

# 菜单标题
main-menu-title = 主菜单
play-menu-title = 开始游戏
categories-menu-title = 游戏分类
tables-menu-title = 可用桌台

# 菜单项目
play = 开始游戏
saved-tables = 保存的桌台
whos-online = 谁在线
leaderboards = 排行榜
my-stats = 我的统计
options = 设置
logout = 退出登录
back = 返回
create-table = 创建新桌台
join-as-player = 作为玩家加入
join-as-spectator = 作为观众加入
leave-table = 离开桌台
start-game = 开始游戏
add-bot = 添加机器人
remove-bot = 移除机器人
actions-menu = 操作菜单
save-table = 保存桌台
whose-turn = 轮到谁
check-scores = 查看分数
check-scores-detailed = 详细分数

# 桌台消息
table-created = { $host } 创建了一个新的 { $game } 桌台。
table-joined = { $player } 加入了桌台。
table-left = { $player } 离开了桌台。
new-host = { $player } 现在是主持人。
waiting-for-players = 等待玩家中。当前 { $current }/{ $min } 最少，{ $max } 最多。
game-starting = 游戏开始！
table-listing = { $host } 的桌台 ({ $count } 位玩家)
table-not-exists = 桌台已不存在。
table-full = 桌台已满。
player-replaced-by-bot = { $player } 离开，已由机器人替代。
player-took-over = { $player } 接管了机器人。
spectator-joined = 已作为观众加入 { $host } 的桌台。

# 观众模式
spectate = 观战
now-playing = { $player } 现在参与游戏。
now-spectating = { $player } 现在观战。

# 通用
welcome = 欢迎来到 PlayPalace！
goodbye = 再见！

# 用户在线状态公告
user-online = { $player } 上线了。
user-offline = { $player } 下线了。

# 设置
language = 语言
language-english = English
language-option = 语言：{ $language }
language-changed = 语言已设置为 { $language }。

# 布尔选项状态
option-on = 开启
option-off = 关闭

# 声音选项
turn-sound-option = 回合提示音：{ $status }

# 骰子选项
clear-kept-option = 掷骰时清除保留的骰子：{ $status }
dice-keeping-style-option = 骰子保留风格：{ $style }
dice-keeping-style-changed = 骰子保留风格已设置为 { $style }。

# 机器人名称
cancel = 取消
no-bot-names-available = 没有可用的机器人名称。
select-bot-name = 选择机器人名称
enter-bot-name = 输入机器人名称
no-options-available = 没有可用选项。
no-scores-available = 没有可用分数。

# 保存/恢复
saved-tables = 已保存的桌台
no-saved-tables = 您没有已保存的桌台。
no-players-online = 目前没有玩家在线。
restore-table = 恢复
delete-saved-table = 删除
saved-table-deleted = 已删除保存的桌台。
missing-players = 无法恢复：以下玩家不在线：{ $players }
table-restored = 桌台已恢复！所有玩家已转移。
table-saved-destroying = 桌台已保存！返回主菜单。
game-type-not-found = 游戏类型不存在。

# 排行榜
leaderboards = 排行榜
leaderboards-menu-title = 排行榜
leaderboards-select-game = 选择游戏查看排行榜
leaderboard-no-data = 此游戏暂无排行榜数据。

# 排行榜类型
leaderboard-type-wins = 胜利排行
leaderboard-type-rating = 技能评分
leaderboard-type-total-score = 总分排行
leaderboard-type-high-score = 最高分排行
leaderboard-type-games-played = 游戏场次排行
leaderboard-type-avg-points-per-turn = 平均每回合得分
leaderboard-type-best-single-turn = 单回合最高分
leaderboard-type-score-per-round = 每轮得分

# 排行榜标题
leaderboard-wins-header = { $game } - 胜利排行
leaderboard-total-score-header = { $game } - 总分排行
leaderboard-high-score-header = { $game } - 最高分排行
leaderboard-games-played-header = { $game } - 游戏场次排行
leaderboard-rating-header = { $game } - 技能评分
leaderboard-avg-points-header = { $game } - 平均每回合得分
leaderboard-best-turn-header = { $game } - 单回合最高分
leaderboard-score-per-round-header = { $game } - 每轮得分

# 排行榜条目
leaderboard-wins-entry = { $rank }：{ $player }，{ $wins }胜 { $losses }负，{ $percentage }%胜率
leaderboard-score-entry = { $rank }. { $player }：{ $value }
leaderboard-avg-entry = { $rank }. { $player }：{ $value } 平均
leaderboard-games-entry = { $rank }. { $player }：{ $value } 场

# 玩家统计
leaderboard-player-stats = 您的统计：{ $wins } 胜，{ $losses } 负（{ $percentage }% 胜率）
leaderboard-no-player-stats = 您还没有玩过这个游戏。

# 技能评分排行榜
leaderboard-no-ratings = 此游戏暂无评分数据。
leaderboard-rating-entry = { $rank }. { $player }：{ $rating } 评分（{ $mu } ± { $sigma }）
leaderboard-player-rating = 您的评分：{ $rating }（{ $mu } ± { $sigma }）
leaderboard-no-player-rating = 您还没有这个游戏的评分。

# 我的统计菜单
my-stats = 我的统计
my-stats-select-game = 选择游戏查看您的统计
my-stats-no-data = 您还没有玩过这个游戏。
my-stats-no-games = 您还没有玩过任何游戏。
my-stats-header = { $game } - 您的统计
my-stats-wins = 胜利：{ $value }
my-stats-losses = 失败：{ $value }
my-stats-winrate = 胜率：{ $value }%
my-stats-games-played = 游戏场次：{ $value }
my-stats-total-score = 总分：{ $value }
my-stats-high-score = 最高分：{ $value }
my-stats-rating = 技能评分：{ $value }（{ $mu } ± { $sigma }）
my-stats-no-rating = 暂无技能评分
my-stats-avg-per-turn = 平均每回合得分：{ $value }
my-stats-best-turn = 单回合最高分：{ $value }

# 预测系统
predict-outcomes = 预测结果
predict-header = 预测结果（按技能评分）
predict-entry = { $rank }. { $player }（评分：{ $rating }）
predict-entry-2p = { $rank }. { $player }（评分：{ $rating }，{ $probability }% 获胜概率）
predict-unavailable = 评分预测不可用。
predict-need-players = 需要至少2名人类玩家才能进行预测。
action-need-more-humans = 需要更多人类玩家。
confirm-leave-game = 确定要离开桌子吗？
confirm-yes = 是
confirm-no = 否
