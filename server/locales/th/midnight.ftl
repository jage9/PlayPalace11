# 1-4-24 (Midnight) game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-midnight = 1-4-24
midnight-category = เกมลูกเต้า

# Actions
midnight-roll = ทอยลูกเต้า
midnight-keep-die = เก็บ { $value }
midnight-bank = เก็บคะแนน

# Game events
midnight-turn-start = ตาของ { $player }
midnight-you-rolled = คุณทอยได้: { $dice }
midnight-player-rolled = { $player } ทอยได้: { $dice }

# Keeping dice
midnight-you-keep = คุณเก็บ { $die }
midnight-player-keeps = { $player } เก็บ { $die }
midnight-you-unkeep = คุณเลิกเก็บ { $die }
midnight-player-unkeeps = { $player } เลิกเก็บ { $die }

# Turn status
midnight-you-have-kept = ลูกเต้าที่เก็บไว้: { $kept } เหลือการทอย: { $remaining } ครั้ง
midnight-player-has-kept = { $player } เก็บไว้: { $kept } เหลือลูกเต้า { $remaining } ลูก

# Scoring
midnight-you-scored = คุณได้ { $score } คะแนน
midnight-scored = { $player } ได้ { $score } คะแนน
midnight-you-disqualified = คุณไม่มีทั้ง 1 และ 4 ตกรอบ!
midnight-player-disqualified = { $player } ไม่มีทั้ง 1 และ 4 ตกรอบ!

# Round results
midnight-round-winner = { $player } ชนะรอบนี้!
midnight-round-tie = รอบนี้เสมอกันระหว่าง { $players }
midnight-all-disqualified = ผู้เล่นทุกคนตกรอบ! ไม่มีผู้ชนะรอบนี้

# Game winner
midnight-game-winner = { $player } ชนะเกมด้วย { $wins } รอบ!
midnight-game-tie = เสมอกัน! { $players } ชนะคนละ { $wins } รอบ

# Options
midnight-set-rounds = จำนวนรอบ: { $rounds }
midnight-enter-rounds = ป้อนจำนวนรอบที่จะเล่น:
midnight-option-changed-rounds = เปลี่ยนจำนวนรอบเป็น { $rounds }

# Disabled reasons
midnight-need-to-roll = คุณต้องทอยลูกเต้าก่อน
midnight-no-dice-to-keep = ไม่มีลูกเต้าที่จะเก็บ
midnight-must-keep-one = คุณต้องเก็บอย่างน้อยหนึ่งลูกต่อการทอย
midnight-must-roll-first = คุณต้องทอยลูกเต้าก่อน
midnight-keep-all-first = คุณต้องเก็บลูกเต้าทั้งหมดก่อนเก็บคะแนน
