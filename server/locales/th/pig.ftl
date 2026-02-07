# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = หมู
pig-category = เกมลูกเต้า

# Actions
pig-roll = ทอยลูกเต้า
pig-bank = ฝาก { $points } คะแนน

# Game events (Pig-specific)
pig-rolls = { $player } ทอยลูกเต้า...
pig-roll-result = { $roll }, รวมเป็น { $total }
pig-bust = โอ้ไม่, 1! { $player } เสียคะแนน { $points }
pig-bank-action = { $player } ตัดสินใจฝาก { $points }, รวมเป็น { $total }
pig-winner = เรามีผู้ชนะแล้ว นั่นคือ { $player }!

# Pig-specific options
pig-set-min-bank = ขั้นต่ำการฝาก: { $points }
pig-set-dice-sides = ด้านลูกเต้า: { $sides }
pig-enter-min-bank = ใส่คะแนนขั้นต่ำในการฝาก:
pig-enter-dice-sides = ใส่จำนวนด้านของลูกเต้า:
pig-option-changed-min-bank = คะแนนขั้นต่ำการฝากเปลี่ยนเป็น { $points }
pig-option-changed-dice = ลูกเต้าตอนนี้มี { $sides } ด้าน

# Disabled reasons
pig-need-more-points = คุณต้องมีคะแนนมากกว่านี้เพื่อฝาก

# Validation errors
pig-error-min-bank-too-high = คะแนนขั้นต่ำการฝากต้องน้อยกว่าคะแนนเป้าหมาย
