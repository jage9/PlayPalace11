# Farkle game messages

# Game info
game-name-farkle = ฟาร์เคิล

# Actions - Roll and Bank
farkle-roll = ทอยลูกเต้า { $count } ลูก
farkle-bank = เก็บ { $points } คะแนน

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = เลข 1 หนึ่งลูกได้ { $points } คะแนน
farkle-take-single-five = เลข 5 หนึ่งลูกได้ { $points } คะแนน
farkle-take-three-kind = เลข { $number } สามลูกได้ { $points } คะแนน
farkle-take-four-kind = เลข { $number } สี่ลูกได้ { $points } คะแนน
farkle-take-five-kind = เลข { $number } ห้าลูกได้ { $points } คะแนน
farkle-take-six-kind = เลข { $number } หกลูกได้ { $points } คะแนน
farkle-take-small-straight = สเตรทเล็กได้ { $points } คะแนน
farkle-take-large-straight = สเตรทใหญ่ได้ { $points } คะแนน
farkle-take-three-pairs = สามคู่ได้ { $points } คะแนน
farkle-take-double-triplets = สองชุดสามเหมือนได้ { $points } คะแนน
farkle-take-full-house = ฟูลเฮาส์ได้ { $points } คะแนน

# Game events (matching v10 exactly)
farkle-rolls = { $player } ทอยลูกเต้า { $count } ลูก...
farkle-you-roll = คุณทอยลูกเต้า { $count } ลูก...
farkle-roll-result = { $dice }
farkle-farkle = ฟาร์เคิล! { $player } เสีย { $points } คะแนน
farkle-you-farkle = ฟาร์เคิล! คุณเสีย { $points } คะแนน
farkle-takes-combo = { $player } เลือก { $combo } ได้ { $points } คะแนน
farkle-you-take-combo = คุณเลือก { $combo } ได้ { $points } คะแนน
farkle-hot-dice = ลูกเต้าร้อนแรง!
farkle-banks = { $player } เก็บ { $points } คะแนน รวมเป็น { $total }
farkle-you-bank = คุณเก็บ { $points } คะแนน รวมเป็น { $total }
farkle-winner = { $player } ชนะด้วย { $score } คะแนน!
farkle-you-win = คุณชนะด้วย { $score } คะแนน!
farkle-winners-tie = เสมอกัน! ผู้ชนะ: { $players }

# Check turn score action
farkle-turn-score = { $player } มี { $points } คะแนนในรอบนี้
farkle-no-turn = ไม่มีใครกำลังเล่นอยู่

# Farkle-specific options
farkle-set-target-score = คะแนนเป้าหมาย: { $score }
farkle-enter-target-score = ป้อนคะแนนเป้าหมาย (500-5000):
farkle-option-changed-target = ตั้งคะแนนเป้าหมายเป็น { $score }

# Disabled action reasons
farkle-must-take-combo = คุณต้องเลือกคอมโบคะแนนก่อน
farkle-cannot-bank = คุณไม่สามารถเก็บคะแนนได้ตอนนี้

# Additional Farkle options
farkle-set-initial-bank-score = คะแนนฝากครั้งแรก: { $score }
farkle-enter-initial-bank-score = กรอกคะแนนฝากครั้งแรก (0-1000):
farkle-option-changed-initial-bank-score = ตั้งค่าคะแนนฝากครั้งแรกเป็น { $score } แล้ว
farkle-toggle-hot-dice-multiplier = ตัวคูณฮอตไดซ์: { $enabled }
farkle-option-changed-hot-dice-multiplier = ตั้งค่าตัวคูณฮอตไดซ์เป็น { $enabled } แล้ว

# Action feedback
farkle-minimum-initial-bank-score = คะแนนฝากครั้งแรกขั้นต่ำคือ { $score }
