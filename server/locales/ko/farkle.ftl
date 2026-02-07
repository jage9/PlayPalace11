# Farkle game messages

# Game info
game-name-farkle = 파클

# Actions - Roll and Bank
farkle-roll = { $count }개 주사위 굴리기
farkle-bank = { $points }점 저금하기

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = 1 하나로 { $points }점
farkle-take-single-five = 5 하나로 { $points }점
farkle-take-three-kind = { $number } 세 개로 { $points }점
farkle-take-four-kind = { $number } 네 개로 { $points }점
farkle-take-five-kind = { $number } 다섯 개로 { $points }점
farkle-take-six-kind = { $number } 여섯 개로 { $points }점
farkle-take-small-straight = 작은 스트레이트로 { $points }점
farkle-take-large-straight = 큰 스트레이트로 { $points }점
farkle-take-three-pairs = 세 쌍으로 { $points }점
farkle-take-double-triplets = 더블 트리플렛으로 { $points }점
farkle-take-full-house = 풀하우스로 { $points }점

# Game events (matching v10 exactly)
farkle-rolls = { $player }님이 { $count }개 주사위를 굴립니다...
farkle-you-roll = { $count }개 주사위를 굴립니다...
farkle-roll-result = { $dice }
farkle-farkle = 파클! { $player }님이 { $points }점을 잃습니다
farkle-you-farkle = 파클! { $points }점을 잃었습니다
farkle-takes-combo = { $player }님이 { $combo }를 선택하여 { $points }점 획득
farkle-you-take-combo = { $combo }를 선택하여 { $points }점 획득
farkle-hot-dice = 핫 주사위!
farkle-banks = { $player }님이 { $points }점을 저금하여 총 { $total }점
farkle-you-bank = { $points }점을 저금하여 총 { $total }점
farkle-winner = { $player }님이 { $score }점으로 승리했습니다!
farkle-you-win = { $score }점으로 승리했습니다!
farkle-winners-tie = 무승부입니다! 승자: { $players }

# Check turn score action
farkle-turn-score = { $player }님이 이번 턴에 { $points }점을 가지고 있습니다.
farkle-no-turn = 현재 턴을 진행 중인 플레이어가 없습니다.

# Farkle-specific options
farkle-set-target-score = 목표 점수: { $score }
farkle-enter-target-score = 목표 점수를 입력하세요 (500-5000):
farkle-option-changed-target = 목표 점수가 { $score }점으로 설정되었습니다.

# Disabled action reasons
farkle-must-take-combo = 먼저 점수 조합을 선택해야 합니다.
farkle-cannot-bank = 지금은 저금할 수 없습니다.
