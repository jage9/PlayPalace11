# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = 피그
pig-category = 주사위 게임

# Actions
pig-roll = 주사위 굴리기
pig-bank = { $points }점 저축하기

# Game events (Pig-specific)
pig-rolls = { $player }가 주사위를 굴립니다...
pig-roll-result = { $roll }이(가) 나왔습니다, 총 { $total }점
pig-bust = 오 안돼, 1이 나왔습니다! { $player }가 { $points }점을 잃었습니다.
pig-bank-action = { $player }가 { $points }점을 저축하여, 총 { $total }점
pig-winner = 우리는 승자가 있습니다, 바로 { $player }입니다!

# Pig-specific options
pig-set-min-bank = 최소 저축 점수: { $points }
pig-set-dice-sides = 주사위 면 수: { $sides }
pig-enter-min-bank = 저축할 최소 점수를 입력하세요:
pig-enter-dice-sides = 주사위 면 수를 입력하세요:
pig-option-changed-min-bank = 최소 저축 점수가 { $points }점으로 변경되었습니다
pig-option-changed-dice = 주사위는 이제 { $sides }개의 면을 가집니다

# Disabled reasons
pig-need-more-points = 저축하려면 더 많은 점수가 필요합니다.

# Validation errors
pig-error-min-bank-too-high = 최소 저축 점수는 목표 점수보다 낮아야 합니다.
