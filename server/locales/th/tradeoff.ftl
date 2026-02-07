# Tradeoff game messages

# Game info
game-name-tradeoff = เทรดออฟ

# Round and iteration flow
tradeoff-round-start = รอบที่ { $round }
tradeoff-iteration = มือที่ { $iteration } จาก 3

# Phase 1: Trading
tradeoff-you-rolled = คุณทอยได้: { $dice }
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = กำลังแลก
tradeoff-trade-status-keeping = กำลังเก็บ
tradeoff-confirm-trades = ยืนยันการแลก ({ $count } ลูกเต้า)
tradeoff-keeping = เก็บ { $value }
tradeoff-trading = แลก { $value }
tradeoff-player-traded = { $player } แลก: { $dice }
tradeoff-player-traded-none = { $player } เก็บลูกเต้าทั้งหมด

# Phase 2: Taking from pool
tradeoff-your-turn-take = ตาคุณเอาลูกเต้าจากพูล
tradeoff-take-die = เอา { $value } (เหลือ { $remaining })
tradeoff-you-take = คุณเอา { $value }
tradeoff-player-takes = { $player } เอา { $value }

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points } คะแนน): { $sets }
tradeoff-no-sets = { $player }: ไม่มีชุด

# Set descriptions
tradeoff-set-triple = สามใบของ { $value }
tradeoff-set-group = กลุ่มของ { $value }
tradeoff-set-mini-straight = สเตรทเล็ก { $low }-{ $high }
tradeoff-set-double-triple = สามใบคู่ ({ $v1 } และ { $v2 })
tradeoff-set-straight = สเตรท { $low }-{ $high }
tradeoff-set-double-group = กลุ่มคู่ ({ $v1 } และ { $v2 })
tradeoff-set-all-groups = ทุกกลุ่ม
tradeoff-set-all-triplets = ทุกสามใบ

# Round end
tradeoff-round-scores = คะแนนรอบที่ { $round }:
tradeoff-score-line = { $player }: +{ $round_points } (รวม: { $total })
tradeoff-leader = { $player } นำด้วย { $score }

# Game end
tradeoff-winner = { $player } ชนะด้วย { $score } คะแนน!
tradeoff-winners-tie = เสมอ! { $players } เสมอด้วย { $score } คะแนน!

# Status checks
tradeoff-view-hand = ดูมือของคุณ
tradeoff-view-pool = ดูพูล
tradeoff-view-players = ดูผู้เล่น
tradeoff-hand-display = มือของคุณ ({ $count } ลูกเต้า): { $dice }
tradeoff-pool-display = พูล ({ $count } ลูกเต้า): { $dice }
tradeoff-player-info = { $player }: { $hand } แลก: { $traded }
tradeoff-player-info-no-trade = { $player }: { $hand } ไม่ได้แลก

# Error messages
tradeoff-not-trading-phase = ไม่อยู่ในช่วงแลก
tradeoff-not-taking-phase = ไม่อยู่ในช่วงเอา
tradeoff-already-confirmed = ยืนยันแล้ว
tradeoff-no-die = ไม่มีลูกเต้าให้สลับ
tradeoff-no-more-takes = ไม่มีการเอาเพิ่ม
tradeoff-not-in-pool = ลูกเต้านั้นไม่อยู่ในพูล

# Options
tradeoff-set-target = คะแนนเป้าหมาย: { $score }
tradeoff-enter-target = ป้อนคะแนนเป้าหมาย:
tradeoff-option-changed-target = ตั้งคะแนนเป้าหมายเป็น { $score } แล้ว
