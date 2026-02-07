# Yahtzee game messages

# Game info
game-name-yahtzee = ยาห์ซี

# Actions - Rolling
yahtzee-roll = ทอยใหม่ (เหลือ { $count } ครั้ง)
yahtzee-roll-all = ทอยลูกเต้า

# Upper section scoring categories
yahtzee-score-ones = เลข 1 ได้ { $points } คะแนน
yahtzee-score-twos = เลข 2 ได้ { $points } คะแนน
yahtzee-score-threes = เลข 3 ได้ { $points } คะแนน
yahtzee-score-fours = เลข 4 ได้ { $points } คะแนน
yahtzee-score-fives = เลข 5 ได้ { $points } คะแนน
yahtzee-score-sixes = เลข 6 ได้ { $points } คะแนน

# Lower section scoring categories
yahtzee-score-three-kind = สามเหมือนได้ { $points } คะแนน
yahtzee-score-four-kind = สี่เหมือนได้ { $points } คะแนน
yahtzee-score-full-house = ฟูลเฮาส์ได้ { $points } คะแนน
yahtzee-score-small-straight = สเตรทเล็กได้ { $points } คะแนน
yahtzee-score-large-straight = สเตรทใหญ่ได้ { $points } คะแนน
yahtzee-score-yahtzee = ยาห์ซีได้ { $points } คะแนน
yahtzee-score-chance = โอกาสได้ { $points } คะแนน

# Game events
yahtzee-you-rolled = คุณทอยได้: { $dice } เหลือ: { $remaining } ครั้ง
yahtzee-player-rolled = { $player } ทอยได้: { $dice } เหลือ: { $remaining } ครั้ง

# Scoring announcements
yahtzee-you-scored = คุณได้ { $points } คะแนนใน { $category }
yahtzee-player-scored = { $player } ได้ { $points } คะแนนใน { $category }

# Yahtzee bonus
yahtzee-you-bonus = โบนัสยาห์ซี! +100 คะแนน
yahtzee-player-bonus = { $player } ได้โบนัสยาห์ซี! +100 คะแนน

# Upper section bonus
yahtzee-you-upper-bonus = โบนัสส่วนบน! +35 คะแนน (รวม { $total } ในส่วนบน)
yahtzee-player-upper-bonus = { $player } ได้โบนัสส่วนบน! +35 คะแนน
yahtzee-you-upper-bonus-missed = คุณพลาดโบนัสส่วนบน (ได้ { $total } ในส่วนบน ต้องการ 63)
yahtzee-player-upper-bonus-missed = { $player } พลาดโบนัสส่วนบน

# Scoring mode
yahtzee-choose-category = เลือกหมวดที่จะให้คะแนน
yahtzee-continuing = ดำเนินการต่อ

# Status checks
yahtzee-check-scoresheet = ตรวจสอบบัตรคะแนน
yahtzee-view-dice = ตรวจสอบมือ
yahtzee-your-dice = ลูกเต้าของคุณ: { $dice }
yahtzee-your-dice-kept = ลูกเต้าของคุณ: { $dice } เก็บไว้: { $kept }
yahtzee-not-rolled = คุณยังไม่ได้ทอย

# Scoresheet display
yahtzee-scoresheet-header = === บัตรคะแนนของ { $player } ===
yahtzee-scoresheet-upper = ส่วนบน:
yahtzee-scoresheet-lower = ส่วนล่าง:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = รวมส่วนบน: { $total } (โบนัส: +35)
yahtzee-scoresheet-upper-total-needed = รวมส่วนบน: { $total } (ต้องการอีก { $needed } สำหรับโบนัส)
yahtzee-scoresheet-yahtzee-bonus = โบนัสยาห์ซี: { $count } x 100 = { $total }
yahtzee-scoresheet-grand-total = คะแนนรวม: { $total }

# Category names (for announcements)
yahtzee-category-ones = เลข 1
yahtzee-category-twos = เลข 2
yahtzee-category-threes = เลข 3
yahtzee-category-fours = เลข 4
yahtzee-category-fives = เลข 5
yahtzee-category-sixes = เลข 6
yahtzee-category-three-kind = สามเหมือน
yahtzee-category-four-kind = สี่เหมือน
yahtzee-category-full-house = ฟูลเฮาส์
yahtzee-category-small-straight = สเตรทเล็ก
yahtzee-category-large-straight = สเตรทใหญ่
yahtzee-category-yahtzee = ยาห์ซี
yahtzee-category-chance = โอกาส

# Game end
yahtzee-winner = { $player } ชนะด้วย { $score } คะแนน!
yahtzee-winners-tie = เสมอกัน! { $players } ได้ { $score } คะแนนเท่ากัน!

# Options
yahtzee-set-rounds = จำนวนเกม: { $rounds }
yahtzee-enter-rounds = ป้อนจำนวนเกม (1-10):
yahtzee-option-changed-rounds = ตั้งจำนวนเกมเป็น { $rounds }

# Disabled action reasons
yahtzee-no-rolls-left = คุณไม่มีการทอยเหลืออยู่
yahtzee-roll-first = คุณต้องทอยก่อน
yahtzee-category-filled = หมวดนั้นถูกใช้ไปแล้ว
