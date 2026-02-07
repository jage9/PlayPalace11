# Yahtzee game messages

# Game info
game-name-yahtzee = 야찌

# Actions - Rolling
yahtzee-roll = 다시 굴리기 (남은 횟수 { $count })
yahtzee-roll-all = 주사위 굴리기

# Upper section scoring categories
yahtzee-score-ones = 1로 { $points }점
yahtzee-score-twos = 2로 { $points }점
yahtzee-score-threes = 3으로 { $points }점
yahtzee-score-fours = 4로 { $points }점
yahtzee-score-fives = 5로 { $points }점
yahtzee-score-sixes = 6으로 { $points }점

# Lower section scoring categories
yahtzee-score-three-kind = 쓰리 오브 어 카인드로 { $points }점
yahtzee-score-four-kind = 포 오브 어 카인드로 { $points }점
yahtzee-score-full-house = 풀하우스로 { $points }점
yahtzee-score-small-straight = 작은 스트레이트로 { $points }점
yahtzee-score-large-straight = 큰 스트레이트로 { $points }점
yahtzee-score-yahtzee = 야찌로 { $points }점
yahtzee-score-chance = 찬스로 { $points }점

# Game events
yahtzee-you-rolled = { $dice }를 굴렸습니다. 남은 횟수: { $remaining }
yahtzee-player-rolled = { $player }님이 { $dice }를 굴렸습니다. 남은 횟수: { $remaining }

# Scoring announcements
yahtzee-you-scored = { $category }에 { $points }점을 기록했습니다.
yahtzee-player-scored = { $player }님이 { $category }에 { $points }점을 기록했습니다.

# Yahtzee bonus
yahtzee-you-bonus = 야찌 보너스! +100점
yahtzee-player-bonus = { $player }님이 야찌 보너스를 획득했습니다! +100점

# Upper section bonus
yahtzee-you-upper-bonus = 상단 섹션 보너스! +35점 (상단 섹션 총 { $total }점)
yahtzee-player-upper-bonus = { $player }님이 상단 섹션 보너스를 획득했습니다! +35점
yahtzee-you-upper-bonus-missed = 상단 섹션 보너스를 놓쳤습니다 (상단 섹션 { $total }점, 필요 점수 63점).
yahtzee-player-upper-bonus-missed = { $player }님이 상단 섹션 보너스를 놓쳤습니다.

# Scoring mode
yahtzee-choose-category = 점수를 기록할 카테고리를 선택하세요.
yahtzee-continuing = 턴을 계속합니다.

# Status checks
yahtzee-check-scoresheet = 점수판 확인
yahtzee-view-dice = 주사위 확인
yahtzee-your-dice = 주사위: { $dice }.
yahtzee-your-dice-kept = 주사위: { $dice }. 보관: { $kept }
yahtzee-not-rolled = 아직 주사위를 굴리지 않았습니다.

# Scoresheet display
yahtzee-scoresheet-header = === { $player }님의 점수판 ===
yahtzee-scoresheet-upper = 상단 섹션:
yahtzee-scoresheet-lower = 하단 섹션:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = 상단 총점: { $total } (보너스: +35)
yahtzee-scoresheet-upper-total-needed = 상단 총점: { $total } (보너스까지 { $needed }점 더 필요)
yahtzee-scoresheet-yahtzee-bonus = 야찌 보너스: { $count } x 100 = { $total }
yahtzee-scoresheet-grand-total = 최종 점수: { $total }

# Category names (for announcements)
yahtzee-category-ones = 1
yahtzee-category-twos = 2
yahtzee-category-threes = 3
yahtzee-category-fours = 4
yahtzee-category-fives = 5
yahtzee-category-sixes = 6
yahtzee-category-three-kind = 쓰리 오브 어 카인드
yahtzee-category-four-kind = 포 오브 어 카인드
yahtzee-category-full-house = 풀하우스
yahtzee-category-small-straight = 작은 스트레이트
yahtzee-category-large-straight = 큰 스트레이트
yahtzee-category-yahtzee = 야찌
yahtzee-category-chance = 찬스

# Game end
yahtzee-winner = { $player }님이 { $score }점으로 승리했습니다!
yahtzee-winners-tie = 무승부입니다! { $players } 모두 { $score }점을 기록했습니다!

# Options
yahtzee-set-rounds = 게임 횟수: { $rounds }
yahtzee-enter-rounds = 게임 횟수를 입력하세요 (1-10):
yahtzee-option-changed-rounds = 게임 횟수가 { $rounds }로 설정되었습니다.

# Disabled action reasons
yahtzee-no-rolls-left = 남은 굴리기 횟수가 없습니다.
yahtzee-roll-first = 먼저 주사위를 굴려야 합니다.
yahtzee-category-filled = 해당 카테고리는 이미 채워졌습니다.
