# パイレーツオブザロストシーズ

# ゲーム名
game-name-pirates = パイレーツオブザロストシーズ

# ゲーム開始とセットアップ
pirates-welcome = パイレーツオブザロストシーズへようこそ!海を航海し、宝石を集め、他の海賊と戦いましょう!
pirates-oceans = あなたの航海は次の海を通ります: { $oceans }
pirates-gems-placed = { $total }個の宝石が海に散らばっています。すべて見つけましょう!
pirates-golden-moon = ゴールデンムーンが昇りました!すべてのXP獲得がこのラウンドで3倍になります!

# ターン発表
pirates-turn = { $player }のターン。位置{ $position }

# 移動アクション
pirates-move-left = 左へ航海
pirates-move-right = 右へ航海
pirates-move-2-left = 左へ2タイル航海
pirates-move-2-right = 右へ2タイル航海
pirates-move-3-left = 左へ3タイル航海
pirates-move-3-right = 右へ3タイル航海

# 移動メッセージ
pirates-move-you = あなたは{ $direction }へ航海して位置{ $position }に移動しました。
pirates-move-you-tiles = あなたは{ $direction }へ{ $tiles }タイル航海して位置{ $position }に移動しました。
pirates-move = { $player }は{ $direction }へ航海して位置{ $position }に移動しました。
pirates-map-edge = これ以上航海できません。あなたは位置{ $position }にいます。

# 位置とステータス
pirates-check-status = ステータスを確認
pirates-check-status-detailed = 詳細ステータス
pirates-check-position = 位置を確認
pirates-check-moon = 月の明るさを確認
pirates-your-position = あなたの位置: { $ocean }の{ $position }
pirates-moon-brightness = ゴールデンムーンは{ $brightness }%の明るさです。({ $total }個中{ $collected }個の宝石が集められました)。
pirates-no-golden-moon = ゴールデンムーンは現在空に見えません。

# 宝石収集
pirates-gem-found-you = あなたは{ $gem }を見つけました!{ $value }点の価値があります。
pirates-gem-found = { $player }が{ $gem }を見つけました!{ $value }点の価値があります。
pirates-all-gems-collected = すべての宝石が集められました!

# 勝者
pirates-winner = { $player }が{ $score }点で勝利!

# スキルメニュー
pirates-use-skill = スキルを使用
pirates-select-skill = 使用するスキルを選択

# 戦闘 - 攻撃開始
pirates-cannonball = 大砲を発射
pirates-no-targets = { $range }タイル以内にターゲットがありません。
pirates-attack-you-fire = あなたは{ $target }に大砲を発射しました!
pirates-attack-incoming = { $attacker }があなたに大砲を発射しました!
pirates-attack-fired = { $attacker }が{ $defender }に大砲を発射しました!

# 戦闘 - ロール
pirates-attack-roll = 攻撃ロール: { $roll }
pirates-attack-bonus = 攻撃ボーナス: +{ $bonus }
pirates-defense-roll = 防御ロール: { $roll }
pirates-defense-roll-others = { $player }は防御で{ $roll }をロールしました。
pirates-defense-bonus = 防御ボーナス: +{ $bonus }

# 戦闘 - ヒット結果
pirates-attack-hit-you = 直撃!あなたは{ $target }に命中しました!
pirates-attack-hit-them = あなたは{ $attacker }に攻撃されました!
pirates-attack-hit = { $attacker }が{ $defender }に命中しました!

# 戦闘 - ミス結果
pirates-attack-miss-you = あなたの大砲は{ $target }を外れました。
pirates-attack-miss-them = 大砲はあなたを外れました!
pirates-attack-miss = { $attacker }の大砲は{ $defender }を外れました。

# 戦闘 - プッシュ
pirates-push-you = あなたは{ $target }を{ $direction }に押して位置{ $position }に移動させました!
pirates-push-them = { $attacker }があなたを{ $direction }に押して位置{ $position }に移動させました!
pirates-push = { $attacker }が{ $defender }を{ $direction }に{ $old_pos }から{ $new_pos }に押しました。

# 戦闘 - 宝石の盗み
pirates-steal-attempt = { $attacker }が宝石を盗もうとしています!
pirates-steal-rolls = 盗みロール: { $steal } 対 防御: { $defend }
pirates-steal-success-you = あなたは{ $target }から{ $gem }を盗みました!
pirates-steal-success-them = { $attacker }があなたの{ $gem }を盗みました!
pirates-steal-success = { $attacker }が{ $defender }から{ $gem }を盗みました!
pirates-steal-failed = 盗みの試みは失敗しました!

# XPとレベリング
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player }がレベル{ $level }に到達しました!
pirates-level-up-you = あなたはレベル{ $level }に到達しました!
pirates-level-up-multiple = { $player }が{ $levels }レベル上がりました!現在レベル{ $level }!
pirates-level-up-multiple-you = あなたは{ $levels }レベル上がりました!現在レベル{ $level }!
pirates-skills-unlocked = { $player }が新しいスキルをアンロックしました: { $skills }。
pirates-skills-unlocked-you = あなたは新しいスキルをアンロックしました: { $skills }。

# スキル発動
pirates-skill-activated = { $player }が{ $skill }を発動しました!
pirates-buff-expired = { $player }の{ $skill }バフが切れました。

# ソードファイタースキル
pirates-sword-fighter-activated = ソードファイター発動!{ $turns }ターンの間、攻撃ボーナス+4。

# プッシュスキル(防御バフ)
pirates-push-activated = プッシュ発動!{ $turns }ターンの間、防御ボーナス+3。

# スキルドキャプテンスキル
pirates-skilled-captain-activated = スキルドキャプテン発動!{ $turns }ターンの間、攻撃+2と防御+2。

# ダブルデバステーションスキル
pirates-double-devastation-activated = ダブルデバステーション発動!{ $turns }ターンの間、攻撃範囲が10タイルに増加。

# バトルシップスキル
pirates-battleship-activated = バトルシップ発動!このターンで2回射撃できます!
pirates-battleship-no-targets = ショット{ $shot }のターゲットがありません。
pirates-battleship-shot = ショット{ $shot }を発射中...

# ポータルスキル
pirates-portal-no-ships = ポータルする他の船が見えません。
pirates-portal-fizzle = { $player }のポータルは目的地がなく消えました。
pirates-portal-success = { $player }が{ $ocean }の位置{ $position }にポータルしました!

# ジェムシーカースキル
pirates-gem-seeker-reveal = 海が位置{ $position }に{ $gem }があることを囁いています。(残り{ $uses }回使用可能)

# レベル要件
pirates-requires-level-15 = レベル15が必要
pirates-requires-level-150 = レベル150が必要

# XP倍率オプション
pirates-set-combat-xp-multiplier = 戦闘XP倍率: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = 戦闘の経験値
pirates-set-find-gem-xp-multiplier = 宝石発見XP倍率: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = 宝石発見の経験値

# 宝石盗みオプション
pirates-set-gem-stealing = 宝石盗み: { $mode }
pirates-select-gem-stealing = 宝石盗みモードを選択
pirates-option-changed-stealing = 宝石盗みが{ $mode }に設定されました。

# 宝石盗みモード選択肢
pirates-stealing-with-bonus = ロールボーナスあり
pirates-stealing-no-bonus = ロールボーナスなし
pirates-stealing-disabled = 無効
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
