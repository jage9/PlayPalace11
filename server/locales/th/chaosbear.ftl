# Chaos Bear game messages

# Game name
game-name-chaosbear = หมีวุ่นวาย

# Actions
chaosbear-roll-dice = ทอยลูกเต้า
chaosbear-draw-card = จั่วไพ่
chaosbear-check-status = ตรวจสอบสถานะ

# Game intro (3 separate messages like v10)
chaosbear-intro-1 = เกมหมีวุ่นวายเริ่มแล้ว! ผู้เล่นทุกคนเริ่มต้นที่ช่องที่ 30 ห่างจากหมี
chaosbear-intro-2 = ทอยลูกเต้าเพื่อเดินไปข้างหน้า และจั่วไพ่ที่ช่องที่เป็นทวีคูณของ 5 เพื่อรับผลพิเศษ
chaosbear-intro-3 = อย่าให้หมีจับคุณได้!

# Turn announcement
chaosbear-turn = ตา{ $player }; ช่องที่ { $position }

# Rolling
chaosbear-roll = { $player } ทอยได้ { $roll }
chaosbear-position = { $player } อยู่ที่ช่องที่ { $position } แล้ว

# Drawing cards
chaosbear-draws-card = { $player } จั่วไพ่
chaosbear-card-impulsion = แรงผลัก! { $player } เดินไปข้างหน้า 3 ช่องไปที่ช่องที่ { $position }!
chaosbear-card-super-impulsion = แรงผลักสุดพิเศษ! { $player } เดินไปข้างหน้า 5 ช่องไปที่ช่องที่ { $position }!
chaosbear-card-tiredness = เหนื่อยล้า! พลังงานหมีลดลง 1 ตอนนี้หมีมีพลังงาน { $energy }
chaosbear-card-hunger = หิวโหย! พลังงานหมีเพิ่มขึ้น 1 ตอนนี้หมีมีพลังงาน { $energy }
chaosbear-card-backward = ผลักถอยหลัง! { $player } เดินถอยหลังไปที่ช่องที่ { $position }
chaosbear-card-random-gift = ของขวัญสุ่ม!
chaosbear-gift-back = { $player } ถอยหลังไปที่ช่องที่ { $position }
chaosbear-gift-forward = { $player } เดินไปข้างหน้าที่ช่องที่ { $position }!

# Bear turn
chaosbear-bear-roll = หมีทอยได้ { $roll } + พลังงาน { $energy } = { $total }
chaosbear-bear-energy-up = หมีทอยได้ 3 และได้รับพลังงานเพิ่ม 1!
chaosbear-bear-position = หมีอยู่ที่ช่องที่ { $position } แล้ว!
chaosbear-player-caught = หมีจับ{ $player } ได้! { $player } พ่ายแพ้แล้ว!
chaosbear-bear-feast = หมีสูญเสียพลังงาน 3 หลังจากกินเนื้อของพวกเขา!

# Status check
chaosbear-status-player-alive = { $player }: ช่องที่ { $position }
chaosbear-status-player-caught = { $player }: ถูกจับที่ช่องที่ { $position }
chaosbear-status-bear = หมีอยู่ที่ช่องที่ { $position } มีพลังงาน { $energy }

# End game
chaosbear-winner = { $player } รอดชีวิตและชนะ! พวกเขาไปถึงช่องที่ { $position }!
chaosbear-tie = เสมอกันที่ช่องที่ { $position }!

# Disabled action reasons
chaosbear-you-are-caught = คุณถูกหมีจับแล้ว
chaosbear-not-on-multiple = คุณสามารถจั่วไพ่ได้เฉพาะที่ช่องทวีคูณของ 5 เท่านั้น
