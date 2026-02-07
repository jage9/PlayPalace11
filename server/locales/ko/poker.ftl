# Shared Poker Messages

poker-fold = 폴드
poker-call = 콜
poker-check = 체크
poker-raise = 레이즈
poker-all-in = 올인
poker-enter-raise = 레이즈 금액 입력

poker-check-pot = 팟 확인
poker-check-bet = 콜 금액
poker-check-min-raise = 최소 레이즈
poker-check-log = 액션 로그
poker-check-hand-players = 핸드에 참여한 플레이어
poker-check-turn-timer = 턴 타이머
poker-check-blind-timer = 블라인드 타이머
poker-check-button = 버튼을 가진 사람
poker-check-dealer = 딜러
poker-check-position = 내 포지션

poker-read-hand = 핸드 읽기
poker-read-table = 테이블 카드 읽기
poker-hand-value = 핸드 가치
poker-read-card = 카드 { $index } 읽기
poker-dealt-cards = { $cards }를 받았습니다.
poker-flop = 플랍: { $cards }.
poker-turn = 턴: { $card }.
poker-river = 리버: { $card }.

poker-pot-total = 팟에 { $amount }칩.
poker-pot-main = 메인 팟: { $amount }칩.
poker-pot-side = 사이드 팟 { $index }: { $amount }칩.
poker-to-call = 콜하려면 { $amount }칩이 필요합니다.
poker-min-raise = 최소 레이즈 { $amount }칩.

poker-player-folds = { $player }님이 폴드했습니다.
poker-player-checks = { $player }님이 체크했습니다.
poker-player-calls = { $player }님이 { $amount }칩을 콜했습니다.
poker-player-raises = { $player }님이 { $amount }칩을 레이즈했습니다.
poker-player-all-in = { $player }님이 { $amount }칩으로 올인했습니다.

poker-player-wins-pot = { $player }님이 { $amount }칩을 획득했습니다.
poker-player-wins-pot-hand = { $player }님이 { $cards }로 { $hand }을(를) 만들어 { $amount }칩을 획득했습니다.
poker-player-wins-side-pot-hand = { $player }님이 { $cards }로 { $hand }을(를) 만들어 사이드 팟 { $index }의 { $amount }칩을 획득했습니다.
poker-players-split-pot = { $players }님이 { $hand }로 { $amount }칩을 나눠 가집니다.
poker-players-split-side-pot = { $players }님이 { $hand }로 사이드 팟 { $index }의 { $amount }칩을 나눠 가집니다.
poker-player-all-in = { $player }님이 { $amount }칩으로 올인했습니다.
poker-player-wins-game = { $player }님이 게임에서 승리했습니다.

poker-showdown = 쇼다운.

poker-timer-disabled = 턴 타이머가 비활성화되었습니다.
poker-timer-remaining = { $seconds }초 남음.
poker-blind-timer-disabled = 블라인드 타이머가 비활성화되었습니다.
poker-blind-timer-remaining = 블라인드 증가까지 { $seconds }초.
poker-blind-timer-remaining-ms = 블라인드 증가까지 { $minutes }분 { $seconds }초.
poker-blinds-raise-next-hand = 다음 핸드에서 블라인드가 증가합니다.

poker-button-is = 버튼은 { $player }님이 가지고 있습니다.
poker-dealer-is = 딜러는 { $player }님입니다.
poker-position-seat = 버튼 다음 { $position }번째 자리입니다.
poker-position-seats = 버튼 다음 { $position }번째 자리입니다.
poker-position-button = 버튼입니다.
poker-position-dealer = 딜러입니다.
poker-position-dealer-seat = 딜러 다음 { $position }번째 자리입니다.
poker-position-dealer-seats = 딜러 다음 { $position }번째 자리입니다.
poker-show-hand = { $player }님이 { $cards }로 { $hand }을(를) 보여줍니다.
poker-blinds-players = 스몰 블라인드: { $sb }. 빅 블라인드: { $bb }.
poker-reveal-only-showdown = 핸드가 끝날 때만 카드를 공개할 수 있습니다.

poker-reveal-both = 홀카드 둘 다 공개
poker-reveal-first = 첫 번째 홀카드 공개
poker-reveal-second = 두 번째 홀카드 공개

poker-raise-cap-reached = 이 라운드의 레이즈 한도에 도달했습니다.
poker-raise-too-small = 최소 레이즈 { $amount }칩.
poker-hand-players-none = 핸드에 참여한 플레이어가 없습니다.
poker-hand-players-one = { $count }명의 플레이어: { $names }.
poker-hand-players = { $count }명의 플레이어: { $names }.
poker-raise-too-large = 칩 스택보다 많이 레이즈할 수 없습니다.

poker-log-empty = 아직 액션이 없습니다.
poker-log-fold = { $player }님이 폴드했습니다
poker-log-check = { $player }님이 체크했습니다
poker-log-call = { $player }님이 { $amount }칩을 콜했습니다
poker-log-raise = { $player }님이 { $amount }칩을 레이즈했습니다
poker-log-all-in = { $player }님이 { $amount }칩으로 올인했습니다

poker-table-cards = 테이블 카드: { $cards }.
poker-your-hand = 내 핸드: { $cards }.

# Timer choice labels
poker-timer-5 = 5초
poker-timer-10 = 10초
poker-timer-15 = 15초
poker-timer-20 = 20초
poker-timer-30 = 30초
poker-timer-45 = 45초
poker-timer-60 = 60초
poker-timer-90 = 90초
poker-timer-unlimited = 무제한

poker-blind-timer-unlimited = 무제한
poker-blind-timer-5 = 5분
poker-blind-timer-10 = 10분
poker-blind-timer-15 = 15분
poker-blind-timer-20 = 20분
poker-blind-timer-30 = 30분

poker-raise-no-limit = 노 리밋
poker-raise-pot-limit = 팟 리밋
poker-raise-double-pot = 더블 팟 리밋
