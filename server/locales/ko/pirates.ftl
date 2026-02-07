# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = 잃어버린 바다의 해적들

# Game start and setup
pirates-welcome = 잃어버린 바다의 해적들에 오신 것을 환영합니다! 바다를 항해하고, 보석을 모으고, 다른 해적들과 전투하세요!
pirates-oceans = 당신의 항해는 다음을 거칩니다: { $oceans }
pirates-gems-placed = { $total }개의 보석이 바다 곳곳에 흩어져 있습니다. 모두 찾으세요!
pirates-golden-moon = 황금 달이 떠올랐습니다! 모든 XP 획득이 이번 라운드에 3배가 됩니다!

# Turn announcements
pirates-turn = { $player }의 차례. 위치 { $position }

# Movement actions
pirates-move-left = 왼쪽으로 항해
pirates-move-right = 오른쪽으로 항해
pirates-move-2-left = 왼쪽으로 2칸 항해
pirates-move-2-right = 오른쪽으로 2칸 항해
pirates-move-3-left = 왼쪽으로 3칸 항해
pirates-move-3-right = 오른쪽으로 3칸 항해

# Movement messages
pirates-move-you = 당신은 { $direction }(으)로 항해하여 위치 { $position }에 도착했습니다.
pirates-move-you-tiles = 당신은 { $tiles }칸 { $direction }(으)로 항해하여 위치 { $position }에 도착했습니다.
pirates-move = { $player }이(가) { $direction }(으)로 항해하여 위치 { $position }에 도착했습니다.
pirates-map-edge = 더 이상 항해할 수 없습니다. 당신은 위치 { $position }에 있습니다.

# Position and status
pirates-check-status = 상태 확인
pirates-check-position = 위치 확인
pirates-check-moon = 달 밝기 확인
pirates-your-position = 당신의 위치: { $ocean }의 { $position }
pirates-moon-brightness = 황금 달이 { $brightness }% 밝습니다. ({ $total }개 중 { $collected }개의 보석이 수집되었습니다).
pirates-no-golden-moon = 황금 달은 현재 하늘에 보이지 않습니다.

# Gem collection
pirates-gem-found-you = 당신은 { $gem }을(를) 발견했습니다! { $value }점의 가치가 있습니다.
pirates-gem-found = { $player }이(가) { $gem }을(를) 발견했습니다! { $value }점의 가치가 있습니다.
pirates-all-gems-collected = 모든 보석이 수집되었습니다!

# Winner
pirates-winner = { $player }이(가) { $score }점으로 승리했습니다!

# Skills menu
pirates-use-skill = 스킬 사용
pirates-select-skill = 사용할 스킬을 선택하세요

# Combat - Attack initiation
pirates-cannonball = 대포알 발사
pirates-no-targets = { $range }칸 내에 목표가 없습니다.
pirates-attack-you-fire = 당신은 { $target }에게 대포알을 발사했습니다!
pirates-attack-incoming = { $attacker }이(가) 당신에게 대포알을 발사했습니다!
pirates-attack-fired = { $attacker }이(가) { $defender }에게 대포알을 발사했습니다!

# Combat - Rolls
pirates-attack-roll = 공격 굴림: { $roll }
pirates-attack-bonus = 공격 보너스: +{ $bonus }
pirates-defense-roll = 방어 굴림: { $roll }
pirates-defense-roll-others = { $player }이(가) 방어를 위해 { $roll }을(를) 굴렸습니다.
pirates-defense-bonus = 방어 보너스: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = 직격탄! 당신은 { $target }을(를) 명중시켰습니다!
pirates-attack-hit-them = 당신은 { $attacker }에게 맞았습니다!
pirates-attack-hit = { $attacker }이(가) { $defender }을(를) 명중시켰습니다!

# Combat - Miss results
pirates-attack-miss-you = 당신의 대포알은 { $target }을(를) 빗나갔습니다.
pirates-attack-miss-them = 대포알이 당신을 빗나갔습니다!
pirates-attack-miss = { $attacker }의 대포알이 { $defender }을(를) 빗나갔습니다.

# Combat - Push
pirates-push-you = 당신은 { $target }을(를) { $direction }(으)로 밀어 위치 { $position }(으)로 보냈습니다!
pirates-push-them = { $attacker }이(가) 당신을 { $direction }(으)로 밀어 위치 { $position }(으)로 보냈습니다!
pirates-push = { $attacker }이(가) { $defender }을(를) { $direction }(으)로 { $old_pos }에서 { $new_pos }(으)로 밀었습니다.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker }이(가) 보석을 훔치려고 시도합니다!
pirates-steal-rolls = 훔치기 굴림: { $steal } vs 방어: { $defend }
pirates-steal-success-you = 당신은 { $target }로부터 { $gem }을(를) 훔쳤습니다!
pirates-steal-success-them = { $attacker}이(가) 당신의 { $gem }을(를) 훔쳤습니다!
pirates-steal-success = { $attacker }이(가) { $defender }로부터 { $gem }을(를) 훔쳤습니다!
pirates-steal-failed = 훔치기 시도가 실패했습니다!

# XP and Leveling
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player }이(가) 레벨 { $level }에 도달했습니다!
pirates-level-up-you = 당신은 레벨 { $level }에 도달했습니다!
pirates-level-up-multiple = { $player }이(가) { $levels }레벨을 획득했습니다! 현재 레벨 { $level }!
pirates-level-up-multiple-you = 당신은 { $levels }레벨을 획득했습니다! 현재 레벨 { $level }!
pirates-skills-unlocked = { $player }이(가) 새로운 스킬을 잠금 해제했습니다: { $skills }.
pirates-skills-unlocked-you = 당신은 새로운 스킬을 잠금 해제했습니다: { $skills }.

# Skill activation
pirates-skill-activated = { $player }이(가) { $skill }을(를) 활성화했습니다!
pirates-buff-expired = { $player }의 { $skill } 버프가 사라졌습니다.

# Sword Fighter skill
pirates-sword-fighter-activated = 검투사 활성화! { $turns }턴 동안 +4 공격 보너스.

# Push skill (defense buff)
pirates-push-activated = 밀기 활성화! { $turns }턴 동안 +3 방어 보너스.

# Skilled Captain skill
pirates-skilled-captain-activated = 숙련된 선장 활성화! { $turns}턴 동안 +2 공격 및 +2 방어.

# Double Devastation skill
pirates-double-devastation-activated = 이중 파괴 활성화! { $turns }턴 동안 공격 범위가 10칸으로 증가합니다.

# Battleship skill
pirates-battleship-activated = 전함 활성화! 이번 턴에 두 번 사격할 수 있습니다!
pirates-battleship-no-targets = 사격 { $shot }에 대한 목표가 없습니다.
pirates-battleship-shot = 사격 { $shot } 발사 중...

# Portal skill
pirates-portal-no-ships = 포털로 이동할 다른 배가 보이지 않습니다.
pirates-portal-fizzle = { $player }의 포털이 목적지 없이 사라졌습니다.
pirates-portal-success = { $player }이(가) { $ocean }의 위치 { $position }(으)로 포털을 이동했습니다!

# Gem Seeker skill
pirates-gem-seeker-reveal = 바다가 위치 { $position }에 { $gem }이(가) 있다고 속삭입니다. (남은 사용 횟수 { $uses })

# Level requirements
pirates-requires-level-15 = 레벨 15 필요
pirates-requires-level-150 = 레벨 150 필요

# XP Multiplier options
pirates-set-combat-xp-multiplier = 전투 xp 배율: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = 전투 경험치
pirates-set-find-gem-xp-multiplier = 보석 발견 xp 배율: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = 보석 발견 경험치

# Gem stealing options
pirates-set-gem-stealing = 보석 훔치기: { $mode }
pirates-select-gem-stealing = 보석 훔치기 모드를 선택하세요
pirates-option-changed-stealing = 보석 훔치기가 { $mode }(으)로 설정되었습니다.

# Gem stealing mode choices
pirates-stealing-with-bonus = 굴림 보너스 포함
pirates-stealing-no-bonus = 굴림 보너스 없음
pirates-stealing-disabled = 비활성화
