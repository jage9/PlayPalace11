# Scopa game messages
# Note: Common messages like round-start, turn-start, target-score, team-mode are in games.ftl

# Game name
game-name-scopa = 스코파

# Game events
scopa-initial-table = 테이블 카드: { $cards }
scopa-no-initial-table = 시작할 테이블에 카드가 없습니다.
scopa-you-collect = 당신은 { $card }(으)로 { $cards }을(를) 수집합니다
scopa-player-collects = { $player }이(가) { $card }(으)로 { $cards }을(를) 수집합니다
scopa-you-put-down = 당신은 { $card }을(를) 내려놓습니다.
scopa-player-puts-down = { $player }이(가) { $card }을(를) 내려놓습니다.
scopa-scopa-suffix =  - 스코파!
scopa-clear-table-suffix = , 테이블을 비웁니다.
scopa-remaining-cards = { $player }이(가) 남은 테이블 카드를 가져갑니다.
scopa-scoring-round = 점수 계산 라운드...
scopa-most-cards = { $player }이(가) 가장 많은 카드로 1점을 획득합니다 ({ $count }장).
scopa-most-cards-tie = 가장 많은 카드가 동점입니다 - 점수 없음.
scopa-most-diamonds = { $player }이(가) 가장 많은 다이아몬드로 1점을 획득합니다 ({ $count }개).
scopa-most-diamonds-tie = 가장 많은 다이아몬드가 동점입니다 - 점수 없음.
scopa-seven-diamonds = { $player }이(가) 다이아몬드 7로 1점을 획득합니다.
scopa-seven-diamonds-multi = { $player }이(가) 가장 많은 다이아몬드 7로 1점을 획득합니다 ({ $count }개).
scopa-seven-diamonds-tie = 다이아몬드 7이 동점입니다 - 점수 없음.
scopa-most-sevens = { $player }이(가) 가장 많은 7로 1점을 획득합니다 ({ $count }개).
scopa-most-sevens-tie = 가장 많은 7이 동점입니다 - 점수 없음.
scopa-round-scores = 라운드 점수:
scopa-round-score-line = { $player }: +{ $round_score } (총합: { $total_score })
scopa-table-empty = 테이블에 카드가 없습니다.
scopa-no-such-card = 해당 위치에 카드가 없습니다.
scopa-captured-count = 당신은 { $count }장을 수집했습니다

# View actions
scopa-view-table = 테이블 보기
scopa-view-captured = 수집한 카드 보기

# Scopa-specific options
scopa-enter-target-score = 목표 점수를 입력하세요 (1-121)
scopa-set-cards-per-deal = 배분당 카드: { $cards }
scopa-enter-cards-per-deal = 배분당 카드를 입력하세요 (1-10)
scopa-set-decks = 덱 개수: { $decks }
scopa-enter-decks = 덱 개수를 입력하세요 (1-6)
scopa-toggle-escoba = 에스코바 (합계 15): { $enabled }
scopa-toggle-hints = 수집 힌트 표시: { $enabled }
scopa-set-mechanic = 스코파 메커니즘: { $mechanic }
scopa-select-mechanic = 스코파 메커니즘을 선택하세요
scopa-toggle-instant-win = 스코파 시 즉시 승리: { $enabled }
scopa-toggle-team-scoring = 팀 카드 점수 통합: { $enabled }
scopa-toggle-inverse = 역방향 모드 (목표 도달 = 탈락): { $enabled }

# Option change announcements
scopa-option-changed-cards = 배분당 카드가 { $cards }(으)로 설정되었습니다.
scopa-option-changed-decks = 덱 개수가 { $decks }(으)로 설정되었습니다.
scopa-option-changed-escoba = 에스코바 { $enabled }.
scopa-option-changed-hints = 수집 힌트 { $enabled }.
scopa-option-changed-mechanic = 스코파 메커니즘이 { $mechanic }(으)로 설정되었습니다.
scopa-option-changed-instant = 스코파 시 즉시 승리 { $enabled }.
scopa-option-changed-team-scoring = 팀 카드 점수 통합 { $enabled }.
scopa-option-changed-inverse = 역방향 모드 { $enabled }.

# Scopa mechanic choices
scopa-mechanic-normal = 일반
scopa-mechanic-no_scopas = 스코파 없음
scopa-mechanic-only_scopas = 스코파만

# Disabled action reasons
scopa-timer-not-active = 라운드 타이머가 활성화되어 있지 않습니다.

# Validation errors
scopa-error-not-enough-cards = { $decks }개 덱에 { $players }명의 플레이어가 각각 { $cards_per_deal }장씩 받기에는 카드가 부족합니다. ({ $cards_per_deal } × { $players } = { $cards_needed }장 필요하지만 { $total_cards }장만 있습니다.)
