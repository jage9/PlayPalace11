# Shared Poker Messages

poker-fold = หมอบ
poker-call = ตาม
poker-check = เช็ค
poker-raise = เรซ
poker-all-in = ออลอิน
poker-enter-raise = ป้อนจำนวนเรซ

poker-check-pot = เช็คพอท
poker-check-bet = จำนวนที่ต้องตาม
poker-check-min-raise = เรซขั้นต่ำ
poker-check-log = บันทึกการกระทำ
poker-check-hand-players = ผู้เล่นในมือ
poker-check-turn-timer = ตั้งเวลาเทิร์น
poker-check-blind-timer = ตั้งเวลาบลายด์
poker-check-button = ใครมีปุ่ม
poker-check-dealer = ใครเป็นดีลเลอร์
poker-check-position = ตำแหน่งของคุณ

poker-read-hand = อ่านมือ
poker-read-table = อ่านไพ่บนโต๊ะ
poker-hand-value = ค่ามือ
poker-read-card = อ่านไพ่ { $index }
poker-dealt-cards = คุณได้รับ { $cards }
poker-flop = ฟล็อป: { $cards }
poker-turn = เทิร์น: { $card }
poker-river = ริเวอร์: { $card }

poker-pot-total = { $amount } ชิปในพอท
poker-pot-main = พอทหลัก: { $amount } ชิป
poker-pot-side = พอทข้าง { $index }: { $amount } ชิป
poker-to-call = คุณต้องใช้ { $amount } ชิปเพื่อตาม
poker-min-raise = { $amount } ชิปเรซขั้นต่ำ

poker-player-folds = { $player } หมอบ
poker-player-checks = { $player } เช็ค
poker-player-calls = { $player } ตาม { $amount } ชิป
poker-player-raises = { $player } เรซ { $amount } ชิป
poker-player-all-in = { $player } ออลอิน { $amount } ชิป

poker-player-wins-pot = { $player } ชนะ { $amount } ชิป
poker-player-wins-pot-hand = { $player } ชนะ { $amount } ชิปด้วย { $cards } สำหรับ { $hand }
poker-player-wins-side-pot-hand = { $player } ชนะพอทข้าง { $index } จาก { $amount } ชิปด้วย { $cards } สำหรับ { $hand }
poker-players-split-pot = { $players } แบ่ง { $amount } ชิปด้วย { $hand }
poker-players-split-side-pot = { $players } แบ่งพอทข้าง { $index } จาก { $amount } ชิปด้วย { $hand }
poker-player-all-in = { $player } ออลอิน { $amount } ชิป
poker-player-wins-game = { $player } ชนะเกม

poker-showdown = โชว์ดาวน์

poker-timer-disabled = ตั้งเวลาเทิร์นปิดอยู่
poker-timer-remaining = เหลือ { $seconds } วินาที
poker-blind-timer-disabled = ตั้งเวลาบลายด์ปิดอยู่
poker-blind-timer-remaining = เหลือ { $seconds } วินาทีจนกว่าบลายด์จะเพิ่ม
poker-blind-timer-remaining-ms = เหลือ { $minutes } นาที { $seconds } วินาทีจนกว่าบลายด์จะเพิ่ม
poker-blinds-raise-next-hand = บลายด์จะเพิ่มมือถัดไป

poker-button-is = ปุ่มอยู่กับ { $player }
poker-dealer-is = ดีลเลอร์คือ { $player }
poker-position-seat = คุณอยู่ที่นั่ง { $position } หลังจากปุ่ม
poker-position-seats = คุณอยู่ { $position } ที่นั่งหลังจากปุ่ม
poker-position-button = คุณอยู่ที่ปุ่ม
poker-position-dealer = คุณเป็นดีลเลอร์
poker-position-dealer-seat = คุณอยู่ที่นั่ง { $position } หลังจากดีลเลอร์
poker-position-dealer-seats = คุณอยู่ { $position } ที่นั่งหลังจากดีลเลอร์
poker-show-hand = { $player } แสดง { $cards } สำหรับ { $hand }
poker-blinds-players = สมอลบลายด์: { $sb } บิ๊กบลายด์: { $bb }
poker-reveal-only-showdown = คุณสามารถเปิดไพ่ได้เฉพาะตอนจบมือเท่านั้น

poker-reveal-both = เปิดไพ่สองใบ
poker-reveal-first = เปิดไพ่ใบแรก
poker-reveal-second = เปิดไพ่ใบที่สอง

poker-raise-cap-reached = ถึงขีดจำกัดเรซสำหรับรอบนี้แล้ว
poker-raise-too-small = { $amount } ชิปเรซขั้นต่ำ
poker-hand-players-none = ไม่มีผู้เล่นในมือ
poker-hand-players-one = { $count } ผู้เล่น: { $names }
poker-hand-players = { $count } ผู้เล่น: { $names }
poker-raise-too-large = คุณไม่สามารถเรซมากกว่าชิปของคุณได้

poker-log-empty = ยังไม่มีการกระทำ
poker-log-fold = { $player } หมอบ
poker-log-check = { $player } เช็ค
poker-log-call = { $player } ตาม { $amount }
poker-log-raise = { $player } เรซ { $amount }
poker-log-all-in = { $player } ออลอิน { $amount }

poker-table-cards = ไพ่บนโต๊ะ: { $cards }
poker-your-hand = มือของคุณ: { $cards }

# Timer choice labels
poker-timer-5 = 5 วินาที
poker-timer-10 = 10 วินาที
poker-timer-15 = 15 วินาที
poker-timer-20 = 20 วินาที
poker-timer-30 = 30 วินาที
poker-timer-45 = 45 วินาที
poker-timer-60 = 60 วินาที
poker-timer-90 = 90 วินาที
poker-timer-unlimited = ไม่จำกัด

poker-blind-timer-unlimited = ไม่จำกัด
poker-blind-timer-5 = 5 นาที
poker-blind-timer-10 = 10 นาที
poker-blind-timer-15 = 15 นาที
poker-blind-timer-20 = 20 นาที
poker-blind-timer-30 = 30 นาที

poker-raise-no-limit = ไม่จำกัด
poker-raise-pot-limit = จำกัดพอท
poker-raise-double-pot = จำกัดพอทสองเท่า
