# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = โจรสลัดแห่งทะเลสาบสูญ

# Game start and setup
pirates-welcome = ยินดีต้อนรับสู่โจรสลัดแห่งทะเลสาบสูญ! แล่นเรือ เก็บอัญมณี และต่อสู้กับโจรสลัดอื่น!
pirates-oceans = การเดินทางของคุณจะผ่าน: { $oceans }
pirates-gems-placed = อัญมณี { $total } อัน กระจายอยู่ทั่วทะเล ค้นหาทั้งหมด!
pirates-golden-moon = พระจันทร์ทองขึ้นมาแล้ว! XP ที่ได้รับจะเป็น 3 เท่าในรอบนี้!

# Turn announcements
pirates-turn = เทิร์นของ { $player } ตำแหน่ง { $position }

# Movement actions
pirates-move-left = แล่นซ้าย
pirates-move-right = แล่นขวา
pirates-move-2-left = แล่น 2 ช่องซ้าย
pirates-move-2-right = แล่น 2 ช่องขวา
pirates-move-3-left = แล่น 3 ช่องซ้าย
pirates-move-3-right = แล่น 3 ช่องขวา

# Movement messages
pirates-move-you = คุณแล่น{ $direction }ไปยังตำแหน่ง { $position }
pirates-move-you-tiles = คุณแล่น { $tiles } ช่อง{ $direction }ไปยังตำแหน่ง { $position }
pirates-move = { $player } แล่น{ $direction }ไปยังตำแหน่ง { $position }
pirates-map-edge = คุณไม่สามารถแล่นไปไกลกว่านี้ คุณอยู่ที่ตำแหน่ง { $position }

# Position and status
pirates-check-status = ตรวจสอบสถานะ
pirates-check-position = ตรวจสอบตำแหน่ง
pirates-check-moon = ตรวจสอบความสว่างพระจันทร์
pirates-your-position = ตำแหน่งของคุณ: { $position } ใน { $ocean }
pirates-moon-brightness = พระจันทร์ทองสว่าง { $brightness }% (เก็บอัญมณีแล้ว { $collected } จาก { $total } อัน)
pirates-no-golden-moon = ยังไม่เห็นพระจันทร์ทองบนท้องฟ้าตอนนี้

# Gem collection
pirates-gem-found-you = คุณพบ { $gem }! มูลค่า { $value } คะแนน
pirates-gem-found = { $player } พบ { $gem }! มูลค่า { $value } คะแนน
pirates-all-gems-collected = เก็บอัญมณีครบทั้งหมดแล้ว!

# Winner
pirates-winner = { $player } ชนะด้วย { $score } คะแนน!

# Skills menu
pirates-use-skill = ใช้ทักษะ
pirates-select-skill = เลือกทักษะที่จะใช้

# Combat - Attack initiation
pirates-cannonball = ยิงลูกปืนใหญ่
pirates-no-targets = ไม่มีเป้าหมายในระยะ { $range } ช่อง
pirates-attack-you-fire = คุณยิงลูกปืนใหญ่ที่ { $target }!
pirates-attack-incoming = { $attacker } ยิงลูกปืนใหญ่มาที่คุณ!
pirates-attack-fired = { $attacker } ยิงลูกปืนใหญ่ที่ { $defender }!

# Combat - Rolls
pirates-attack-roll = ทอยโจมตี: { $roll }
pirates-attack-bonus = โบนัสโจมตี: +{ $bonus }
pirates-defense-roll = ทอยป้องกัน: { $roll }
pirates-defense-roll-others = { $player } ทอยได้ { $roll } สำหรับป้องกัน
pirates-defense-bonus = โบนัสป้องกัน: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = โดนเป้า! คุณโจมตี { $target } สำเร็จ!
pirates-attack-hit-them = คุณถูกโจมตีโดย { $attacker }!
pirates-attack-hit = { $attacker } โจมตี { $defender } สำเร็จ!

# Combat - Miss results
pirates-attack-miss-you = ลูกปืนใหญ่ของคุณพลาด { $target }
pirates-attack-miss-them = ลูกปืนใหญ่พลาดคุณ!
pirates-attack-miss = ลูกปืนใหญ่ของ { $attacker } พลาด { $defender }

# Combat - Push
pirates-push-you = คุณผลัก { $target } ไป{ $direction }ยังตำแหน่ง { $position }!
pirates-push-them = { $attacker } ผลักคุณ{ $direction }ไปยังตำแหน่ง { $position }!
pirates-push = { $attacker } ผลัก { $defender } { $direction }จาก { $old_pos } ไปยัง { $new_pos }

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } พยายามขโมยอัญมณี!
pirates-steal-rolls = ทอยขโมย: { $steal } vs ป้องกัน: { $defend }
pirates-steal-success-you = คุณขโมย { $gem } จาก { $target }!
pirates-steal-success-them = { $attacker } ขโมย { $gem } ของคุณ!
pirates-steal-success = { $attacker } ขโมย { $gem } จาก { $defender }!
pirates-steal-failed = ขโมยไม่สำเร็จ!

# XP and Leveling
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player } ขึ้นเลเวล { $level }!
pirates-level-up-you = คุณขึ้นเลเวล { $level }!
pirates-level-up-multiple = { $player } ขึ้น { $levels } เลเวล! ตอนนี้เลเวล { $level }!
pirates-level-up-multiple-you = คุณขึ้น { $levels } เลเวล! ตอนนี้เลเวล { $level }!
pirates-skills-unlocked = { $player } ปลดล็อกทักษะใหม่: { $skills }
pirates-skills-unlocked-you = คุณปลดล็อกทักษะใหม่: { $skills }

# Skill activation
pirates-skill-activated = { $player } เปิดใช้ { $skill }!
pirates-buff-expired = บัฟ { $skill } ของ { $player } หมดแล้ว

# Sword Fighter skill
pirates-sword-fighter-activated = เปิดใช้นักรบดาบ! โบนัสโจมตี +4 นาน { $turns } เทิร์น

# Push skill (defense buff)
pirates-push-activated = เปิดใช้การผลัก! โบนัสป้องกัน +3 นาน { $turns } เทิร์น

# Skilled Captain skill
pirates-skilled-captain-activated = เปิดใช้กัปตันผู้เชี่ยวชาญ! โจมตี +2 และป้องกัน +2 นาน { $turns } เทิร์น

# Double Devastation skill
pirates-double-devastation-activated = เปิดใช้การทำลายสองเท่า! เพิ่มระยะโจมตีเป็น 10 ช่องนาน { $turns } เทิร์น

# Battleship skill
pirates-battleship-activated = เปิดใช้เรือรบ! คุณสามารถยิง 2 นัดในเทิร์นนี้!
pirates-battleship-no-targets = ไม่มีเป้าหมายสำหรับการยิงที่ { $shot }
pirates-battleship-shot = ยิงนัดที่ { $shot }...

# Portal skill
pirates-portal-no-ships = ไม่มีเรือเห็นเพื่อเทเลพอร์ตไป
pirates-portal-fizzle = พอร์ทัลของ { $player } จางหายโดยไม่มีปลายทาง
pirates-portal-success = { $player } เทเลพอร์ตไปยัง { $ocean } ที่ตำแหน่ง { $position }!

# Gem Seeker skill
pirates-gem-seeker-reveal = ทะเลกระซิบเกี่ยวกับ { $gem } ที่ตำแหน่ง { $position } (เหลือใช้ได้ { $uses } ครั้ง)

# Level requirements
pirates-requires-level-15 = ต้องการเลเวล 15
pirates-requires-level-150 = ต้องการเลเวล 150

# XP Multiplier options
pirates-set-combat-xp-multiplier = ตัวคูณ XP การต่อสู้: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = ประสบการณ์จากการต่อสู้
pirates-set-find-gem-xp-multiplier = ตัวคูณ XP หาอัญมณี: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = ประสบการณ์จากการหาอัญมณี

# Gem stealing options
pirates-set-gem-stealing = ขโมยอัญมณี: { $mode }
pirates-select-gem-stealing = เลือกโหมดขโมยอัญมณี
pirates-option-changed-stealing = ตั้งขโมยอัญมณีเป็น { $mode }

# Gem stealing mode choices
pirates-stealing-with-bonus = มีโบนัสทอย
pirates-stealing-no-bonus = ไม่มีโบนัสทอย
pirates-stealing-disabled = ปิดใช้งาน
