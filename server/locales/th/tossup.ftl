# Toss Up game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-tossup = โยนขึ้น
tossup-category = เกมลูกเต้า

# Actions
tossup-roll-first = ทอยลูกเต้า { $count } ลูก
tossup-roll-remaining = ทอยลูกเต้าที่เหลือ { $count } ลูก
tossup-bank = ฝาก { $points } คะแนน

# Game events
tossup-turn-start = ตา{ $player } คะแนน: { $score }
tossup-you-roll = คุณทอยได้: { $results }
tossup-player-rolls = { $player } ทอยได้: { $results }

# Turn status
tossup-you-have-points = คะแนนในตา: { $turn_points } ลูกเต้าที่เหลือ: { $dice_count }
tossup-player-has-points = { $player } มีคะแนนในตา { $turn_points } มีลูกเต้าเหลือ { $dice_count } ลูก

# Fresh dice
tossup-you-get-fresh = ไม่มีลูกเต้าเหลือ! ได้รับลูกเต้าใหม่ { $count } ลูก
tossup-player-gets-fresh = { $player } ได้รับลูกเต้าใหม่ { $count } ลูก

# Bust
tossup-you-bust = ล้ม! คุณเสียคะแนน { $points } คะแนนในตานี้
tossup-player-busts = { $player } ล้มและเสียคะแนน { $points } คะแนน!

# Bank
tossup-you-bank = คุณฝาก { $points } คะแนน คะแนนรวม: { $total }
tossup-player-banks = { $player } ฝาก { $points } คะแนน คะแนนรวม: { $total }

# Winner
tossup-winner = { $player } ชนะด้วย { $score } คะแนน!
tossup-tie-tiebreaker = เสมอกันระหว่าง { $players }! รอบตัดสิน!

# Options
tossup-set-rules-variant = กฎแบบ: { $variant }
tossup-select-rules-variant = เลือกกฎแบบ:
tossup-option-changed-rules = กฎแบบเปลี่ยนเป็น { $variant }

tossup-set-starting-dice = ลูกเต้าเริ่มต้น: { $count }
tossup-enter-starting-dice = ใส่จำนวนลูกเต้าเริ่มต้น:
tossup-option-changed-dice = ลูกเต้าเริ่มต้นเปลี่ยนเป็น { $count }

# Rules variants
tossup-rules-standard = มาตรฐาน
tossup-rules-playpalace = PlayPalace

# Rules explanations
tossup-rules-standard-desc = 3 เขียว, 2 เหลือง, 1 แดงต่อลูก ล้มถ้าไม่มีเขียวและมีแดงอย่างน้อยหนึ่ง
tossup-rules-playpalace-desc = การกระจายเท่ากัน ล้มถ้าลูกเต้าทั้งหมดเป็นสีแดง

# Disabled reasons
tossup-need-points = คุณต้องมีคะแนนเพื่อฝาก
