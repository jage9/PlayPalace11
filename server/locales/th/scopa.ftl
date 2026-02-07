# Scopa game messages
# Note: Common messages like round-start, turn-start, target-score, team-mode are in games.ftl

# Game name
game-name-scopa = สโกปา

# Game events
scopa-initial-table = ไพ่บนโต๊ะ: { $cards }
scopa-no-initial-table = ไม่มีไพ่บนโต๊ะตอนเริ่มเกม
scopa-you-collect = คุณเก็บ { $cards } ด้วย { $card }
scopa-player-collects = { $player } เก็บ { $cards } ด้วย { $card }
scopa-you-put-down = คุณวาง { $card }
scopa-player-puts-down = { $player } วาง { $card }
scopa-scopa-suffix =  - สโกปา!
scopa-clear-table-suffix = , เก็บโต๊ะหมด
scopa-remaining-cards = { $player } ได้รับไพ่ที่เหลือบนโต๊ะ
scopa-scoring-round = คำนวณคะแนน...
scopa-most-cards = { $player } ได้ 1 คะแนนสำหรับไพ่มากที่สุด ({ $count } ใบ)
scopa-most-cards-tie = ไพ่มากที่สุดเสมอกัน - ไม่มีคะแนน
scopa-most-diamonds = { $player } ได้ 1 คะแนนสำหรับข้าวหลามตัดมากที่สุด ({ $count } ใบ)
scopa-most-diamonds-tie = ข้าวหลามตัดมากที่สุดเสมอกัน - ไม่มีคะแนน
scopa-seven-diamonds = { $player } ได้ 1 คะแนนสำหรับเจ็ดข้าวหลามตัด
scopa-seven-diamonds-multi = { $player } ได้ 1 คะแนนสำหรับเจ็ดข้าวหลามตัดมากที่สุด ({ $count } ใบ)
scopa-seven-diamonds-tie = เจ็ดข้าวหลามตัดเสมอกัน - ไม่มีคะแนน
scopa-most-sevens = { $player } ได้ 1 คะแนนสำหรับเจ็ดมากที่สุด ({ $count } ใบ)
scopa-most-sevens-tie = เจ็ดมากที่สุดเสมอกัน - ไม่มีคะแนน
scopa-round-scores = คะแนนรอบนี้:
scopa-round-score-line = { $player }: +{ $round_score } (รวม: { $total_score })
scopa-table-empty = ไม่มีไพ่บนโต๊ะ
scopa-no-such-card = ไม่มีไพ่ที่ตำแหน่งนั้น
scopa-captured-count = คุณจับได้ { $count } ใบ

# View actions
scopa-view-table = ดูโต๊ะ
scopa-view-captured = ดูไพ่ที่จับได้

# Scopa-specific options
scopa-enter-target-score = ใส่คะแนนเป้าหมาย (1-121)
scopa-set-cards-per-deal = ไพ่แต่ละรอบ: { $cards }
scopa-enter-cards-per-deal = ใส่จำนวนไพ่แต่ละรอบ (1-10)
scopa-set-decks = จำนวนสำรับ: { $decks }
scopa-enter-decks = ใส่จำนวนสำรับ (1-6)
scopa-toggle-escoba = เอสโกบา (รวมได้ 15): { $enabled }
scopa-toggle-hints = แสดงคำใบ้การจับ: { $enabled }
scopa-set-mechanic = กลไกสโกปา: { $mechanic }
scopa-select-mechanic = เลือกกลไกสโกปา
scopa-toggle-instant-win = ชนะทันทีเมื่อได้สโกปา: { $enabled }
scopa-toggle-team-scoring = รวมไพ่ทีมสำหรับคะแนน: { $enabled }
scopa-toggle-inverse = โหมดกลับด้าน (ถึงเป้าหมาย = ตกรอบ): { $enabled }

# Option change announcements
scopa-option-changed-cards = ตั้งไพ่แต่ละรอบเป็น { $cards }
scopa-option-changed-decks = ตั้งจำนวนสำรับเป็น { $decks }
scopa-option-changed-escoba = เอสโกบา { $enabled }
scopa-option-changed-hints = คำใบ้การจับ { $enabled }
scopa-option-changed-mechanic = ตั้งกลไกสโกปาเป็น { $mechanic }
scopa-option-changed-instant = ชนะทันทีเมื่อได้สโกปา { $enabled }
scopa-option-changed-team-scoring = การคะแนนไพ่ทีม { $enabled }
scopa-option-changed-inverse = โหมดกลับด้าน { $enabled }

# Scopa mechanic choices
scopa-mechanic-normal = ปกติ
scopa-mechanic-no_scopas = ไม่มีสโกปา
scopa-mechanic-only_scopas = สโกปาเท่านั้น

# Disabled action reasons
scopa-timer-not-active = ตัวจับเวลารอบไม่ทำงาน

# Validation errors
scopa-error-not-enough-cards = ไพ่ไม่พอใน { $decks } สำรับสำหรับ { $players } คนด้วย { $cards_per_deal } ใบต่อคน (ต้องการ { $cards_per_deal } × { $players } = { $cards_needed } ใบ แต่มีเพียง { $total_cards } ใบ)
