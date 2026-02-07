# Chaos Bear game messages

# Game name
game-name-chaosbear = 카오스 베어

# Actions
chaosbear-roll-dice = 주사위 굴리기
chaosbear-draw-card = 카드 뽑기
chaosbear-check-status = 상태 확인

# Game intro (3 separate messages like v10)
chaosbear-intro-1 = 카오스 베어가 시작되었습니다! 모든 플레이어는 곰보다 30칸 앞에서 시작합니다.
chaosbear-intro-2 = 주사위를 굴려 앞으로 이동하고, 5의 배수에서 카드를 뽑아 특수 효과를 얻으세요.
chaosbear-intro-3 = 곰에게 잡히지 마세요!

# Turn announcement
chaosbear-turn = { $player }의 턴; { $position }번 칸.

# Rolling
chaosbear-roll = { $player }가 { $roll }을(를) 굴렸습니다.
chaosbear-position = { $player }는 이제 { $position }번 칸에 있습니다.

# Drawing cards
chaosbear-draws-card = { $player }가 카드를 뽑습니다.
chaosbear-card-impulsion = 충동! { $player }가 3칸 전진하여 { $position }번 칸으로 이동합니다!
chaosbear-card-super-impulsion = 슈퍼 충동! { $player }가 5칸 전진하여 { $position }번 칸으로 이동합니다!
chaosbear-card-tiredness = 피로! 곰의 에너지가 1 감소합니다. 이제 { $energy } 에너지를 가지고 있습니다.
chaosbear-card-hunger = 배고픔! 곰의 에너지가 1 증가합니다. 이제 { $energy } 에너지를 가지고 있습니다.
chaosbear-card-backward = 뒤로 밀림! { $player }가 { $position }번 칸으로 후퇴합니다.
chaosbear-card-random-gift = 랜덤 선물!
chaosbear-gift-back = { $player }가 { $position }번 칸으로 후퇴했습니다.
chaosbear-gift-forward = { $player }가 { $position }번 칸으로 전진했습니다!

# Bear turn
chaosbear-bear-roll = 곰이 { $roll } + { $energy } 에너지 = { $total }을(를) 굴렸습니다.
chaosbear-bear-energy-up = 곰이 3을 굴려 에너지 1을 얻었습니다!
chaosbear-bear-position = 곰은 이제 { $position }번 칸에 있습니다!
chaosbear-player-caught = 곰이 { $player }를 잡았습니다! { $player }는 패배했습니다!
chaosbear-bear-feast = 곰이 그들의 살을 먹은 후 에너지가 3 감소합니다!

# Status check
chaosbear-status-player-alive = { $player }: { $position }번 칸.
chaosbear-status-player-caught = { $player }: { $position }번 칸에서 잡힘.
chaosbear-status-bear = 곰은 { $energy } 에너지를 가지고 { $position }번 칸에 있습니다.

# End game
chaosbear-winner = { $player }가 생존하여 승리했습니다! { $position }번 칸에 도달했습니다!
chaosbear-tie = { $position }번 칸에서 무승부입니다!

# Disabled action reasons
chaosbear-you-are-caught = 당신은 곰에게 잡혔습니다.
chaosbear-not-on-multiple = 5의 배수에서만 카드를 뽑을 수 있습니다.
