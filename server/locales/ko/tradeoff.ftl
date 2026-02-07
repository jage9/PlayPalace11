# Tradeoff game messages

# Game info
game-name-tradeoff = 트레이드오프

# Round and iteration flow
tradeoff-round-start = 라운드 { $round }.
tradeoff-iteration = 핸드 { $iteration } / 3.

# Phase 1: Trading
tradeoff-you-rolled = 주사위 굴림: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = 교환 중
tradeoff-trade-status-keeping = 보관 중
tradeoff-confirm-trades = 교환 확인 ({ $count }개 주사위)
tradeoff-keeping = { $value }을(를) 보관합니다.
tradeoff-trading = { $value }을(를) 교환합니다.
tradeoff-player-traded = { $player }님이 교환: { $dice }.
tradeoff-player-traded-none = { $player }님이 모든 주사위를 보관했습니다.

# Phase 2: Taking from pool
tradeoff-your-turn-take = 풀에서 주사위를 가져갈 차례입니다.
tradeoff-take-die = { $value } 가져가기 ({ $remaining }개 남음)
tradeoff-you-take = { $value }을(를) 가져갑니다.
tradeoff-player-takes = { $player }님이 { $value }을(를) 가져갑니다.

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points }점): { $sets }.
tradeoff-no-sets = { $player }: 세트 없음.

# Set descriptions (concise)
tradeoff-set-triple = { $value } 트리플
tradeoff-set-group = { $value } 그룹
tradeoff-set-mini-straight = 미니 스트레이트 { $low }-{ $high }
tradeoff-set-double-triple = 더블 트리플 ({ $v1 }와 { $v2 })
tradeoff-set-straight = 스트레이트 { $low }-{ $high }
tradeoff-set-double-group = 더블 그룹 ({ $v1 }와 { $v2 })
tradeoff-set-all-groups = 모든 그룹
tradeoff-set-all-triplets = 모든 트리플

# Round end
tradeoff-round-scores = 라운드 { $round } 점수:
tradeoff-score-line = { $player }: +{ $round_points } (총점: { $total })
tradeoff-leader = { $player }님이 { $score }점으로 선두입니다.

# Game end
tradeoff-winner = { $player }님이 { $score }점으로 승리했습니다!
tradeoff-winners-tie = 무승부! { $players }님이 { $score }점으로 동점입니다!

# Status checks
tradeoff-view-hand = 내 핸드 보기
tradeoff-view-pool = 풀 보기
tradeoff-view-players = 플레이어 보기
tradeoff-hand-display = 내 핸드 ({ $count }개 주사위): { $dice }
tradeoff-pool-display = 풀 ({ $count }개 주사위): { $dice }
tradeoff-player-info = { $player }: { $hand }. 교환: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. 교환 없음.

# Error messages
tradeoff-not-trading-phase = 교환 단계가 아닙니다.
tradeoff-not-taking-phase = 가져가기 단계가 아닙니다.
tradeoff-already-confirmed = 이미 확인했습니다.
tradeoff-no-die = 전환할 주사위가 없습니다.
tradeoff-no-more-takes = 더 이상 가져갈 수 없습니다.
tradeoff-not-in-pool = 해당 주사위가 풀에 없습니다.

# Options
tradeoff-set-target = 목표 점수: { $score }
tradeoff-enter-target = 목표 점수 입력:
tradeoff-option-changed-target = 목표 점수가 { $score }점으로 설정되었습니다.
