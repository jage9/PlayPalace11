# Toss Up game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-tossup = 토스업
tossup-category = 주사위 게임

# Actions
tossup-roll-first = 주사위 { $count }개 굴리기
tossup-roll-remaining = 남은 주사위 { $count }개 굴리기
tossup-bank = { $points }점 저축하기

# Game events
tossup-turn-start = { $player }의 턴. 점수: { $score }
tossup-you-roll = 굴린 결과: { $results }.
tossup-player-rolls = { $player }가 굴린 결과: { $results }.

# Turn status
tossup-you-have-points = 턴 점수: { $turn_points }. 남은 주사위: { $dice_count }개.
tossup-player-has-points = { $player }의 턴 점수는 { $turn_points }점입니다. 남은 주사위 { $dice_count }개.

# Fresh dice
tossup-you-get-fresh = 주사위가 없습니다! 새 주사위 { $count }개를 받습니다.
tossup-player-gets-fresh = { $player }가 새 주사위 { $count }개를 받습니다.

# Bust
tossup-you-bust = 버스트! 이번 턴에서 { $points }점을 잃었습니다.
tossup-player-busts = { $player }가 버스트하여 { $points }점을 잃었습니다!

# Bank
tossup-you-bank = { $points }점을 저축합니다. 총 점수: { $total }.
tossup-player-banks = { $player }가 { $points }점을 저축합니다. 총 점수: { $total }.

# Winner
tossup-winner = { $player }가 { $score }점으로 승리했습니다!
tossup-tie-tiebreaker = { $players } 사이에 무승부입니다! 타이브레이커 라운드!

# Options
tossup-set-rules-variant = 규칙 변형: { $variant }
tossup-select-rules-variant = 규칙 변형을 선택하세요:
tossup-option-changed-rules = 규칙 변형이 { $variant }(으)로 변경되었습니다

tossup-set-starting-dice = 시작 주사위: { $count }개
tossup-enter-starting-dice = 시작 주사위 수를 입력하세요:
tossup-option-changed-dice = 시작 주사위가 { $count }개로 변경되었습니다

# Rules variants
tossup-rules-standard = 표준
tossup-rules-playpalace = 플레이팰리스

# Rules explanations
tossup-rules-standard-desc = 주사위당 녹색 3개, 노란색 2개, 빨간색 1개. 녹색이 없고 빨간색이 하나 이상이면 버스트.
tossup-rules-playpalace-desc = 균등 분배. 모든 주사위가 빨간색이면 버스트.

# Disabled reasons
tossup-need-points = 저축하려면 점수가 필요합니다.
