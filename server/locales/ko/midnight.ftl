# 1-4-24 (Midnight) game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-midnight = 1-4-24
midnight-category = 주사위 게임

# Actions
midnight-roll = 주사위 굴리기
midnight-keep-die = { $value } 보관하기
midnight-bank = 저금하기

# Game events
midnight-turn-start = { $player }님의 턴입니다.
midnight-you-rolled = { $dice }를 굴렸습니다.
midnight-player-rolled = { $player }님이 { $dice }를 굴렸습니다.

# Keeping dice
midnight-you-keep = { $die }를 보관합니다.
midnight-player-keeps = { $player }님이 { $die }를 보관합니다.
midnight-you-unkeep = { $die }의 보관을 취소합니다.
midnight-player-unkeeps = { $player }님이 { $die }의 보관을 취소합니다.

# Turn status
midnight-you-have-kept = 보관된 주사위: { $kept }. 남은 굴리기: { $remaining }.
midnight-player-has-kept = { $player }님이 보관: { $kept }. 남은 주사위 { $remaining }개.

# Scoring
midnight-you-scored = { $score }점을 획득했습니다.
midnight-scored = { $player }님이 { $score }점을 획득했습니다.
midnight-you-disqualified = 1과 4가 모두 없습니다. 실격!
midnight-player-disqualified = { $player }님이 1과 4가 모두 없습니다. 실격!

# Round results
midnight-round-winner = { $player }님이 라운드에서 승리했습니다!
midnight-round-tie = { $players } 간에 무승부입니다.
midnight-all-disqualified = 모든 플레이어가 실격했습니다! 이번 라운드는 승자가 없습니다.

# Game winner
midnight-game-winner = { $player }님이 { $wins }번의 라운드 승리로 게임에서 승리했습니다!
midnight-game-tie = 무승부입니다! { $players } 모두 { $wins }번의 라운드를 이겼습니다.

# Options
midnight-set-rounds = 플레이할 라운드: { $rounds }
midnight-enter-rounds = 플레이할 라운드 수를 입력하세요:
midnight-option-changed-rounds = 플레이할 라운드가 { $rounds }로 변경되었습니다

# Disabled reasons
midnight-need-to-roll = 먼저 주사위를 굴려야 합니다.
midnight-no-dice-to-keep = 보관할 수 있는 주사위가 없습니다.
midnight-must-keep-one = 매 굴리기마다 최소 하나의 주사위를 보관해야 합니다.
midnight-must-roll-first = 먼저 주사위를 굴려야 합니다.
midnight-keep-all-first = 저금하기 전에 모든 주사위를 보관해야 합니다.
