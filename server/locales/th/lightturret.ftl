# Light Turret game messages

# Game name
game-name-lightturret = หอคอยแสง

# Intro
lightturret-intro = เกมหอคอยแสงเริ่มแล้ว! ผู้เล่นแต่ละคนมีหอคอยที่มีพลัง { $power } ยิงหอคอยเพื่อรับแสงและเหรียญ แต่ถ้าแสงของคุณเกินพลัง คุณจะถูกคัดออก! ซื้ออัปเกรดด้วยเหรียญเพื่อเพิ่มพลัง ผู้เล่นที่มีแสงมากที่สุดตอนจบชนะ!

# Actions
lightturret-shoot = ยิงหอคอย
lightturret-upgrade = ซื้ออัปเกรด (10 เหรียญ)
lightturret-check-stats = ตรวจสอบสถิติ

# Action results
lightturret-shoot-result = { $player } ยิงหอคอยและได้แสง { $gain }! ตอนนี้หอคอยมีแสง { $light }
lightturret-coins-gained = { $player } ได้รับ { $coins } เหรียญ! { $player } มี { $total } เหรียญแล้ว
lightturret-buys-upgrade = { $player } ซื้ออัปเกรดพลัง!
lightturret-power-gained = { $player } ได้พลัง { $gain }! { $player } มีพลัง { $power } แล้ว
lightturret-upgrade-accident = อัปเกรดถูกรวมเข้ากับหอคอยโดยไม่ตั้งใจ! ทำให้มันมีแสง { $light }
lightturret-not-enough-coins = คุณมีเหรียญไม่พอ! ต้องการ { $need } เหรียญ แต่มีแค่ { $have }

# Elimination
lightturret-eliminated = แสงมากเกินไปสำหรับวิญญาณของ { $player }! { $player } ถูกคัดออก!

# Stats
lightturret-stats-alive = { $player }: พลัง { $power } แสง { $light } เหรียญ { $coins }
lightturret-stats-eliminated = { $player }: ถูกคัดออกด้วยแสง { $light }

# Game end
lightturret-game-over = จบเกม!
lightturret-final-alive = { $player } จบด้วยแสง { $light }
lightturret-final-eliminated = { $player } ถูกคัดออกด้วยแสง { $light }
lightturret-winner = { $player } ชนะด้วยแสง { $light }!
lightturret-tie = เสมอกันที่แสง { $light }!

# Options
lightturret-set-starting-power = พลังเริ่มต้น: { $power }
lightturret-enter-starting-power = ป้อนพลังเริ่มต้น:
lightturret-option-changed-power = ตั้งพลังเริ่มต้นเป็น { $power }
lightturret-set-max-rounds = รอบสูงสุด: { $rounds }
lightturret-enter-max-rounds = ป้อนรอบสูงสุด:
lightturret-option-changed-rounds = ตั้งรอบสูงสุดเป็น { $rounds }

# Disabled action reasons
lightturret-you-are-eliminated = คุณถูกคัดออกแล้ว
