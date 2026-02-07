# Toss Up game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-tossup = टॉस अप
tossup-category = पासा खेल

# Actions
tossup-roll-first = { $count } पासे रोल करें
tossup-roll-remaining = { $count } शेष पासे रोल करें
tossup-bank = { $points } अंक बैंक करें

# Game events
tossup-turn-start = { $player } की बारी। स्कोर: { $score }
tossup-you-roll = आपने रोल किया: { $results }।
tossup-player-rolls = { $player } ने रोल किया: { $results }।

# Turn status
tossup-you-have-points = बारी के अंक: { $turn_points }। शेष पासे: { $dice_count }।
tossup-player-has-points = { $player } के पास { $turn_points } बारी के अंक हैं। { $dice_count } पासे शेष।

# Fresh dice
tossup-you-get-fresh = कोई पासा नहीं बचा! { $count } ताजे पासे मिल रहे हैं।
tossup-player-gets-fresh = { $player } को { $count } ताजे पासे मिलते हैं।

# Bust
tossup-you-bust = बस्ट! आप इस बारी के { $points } अंक खो देते हैं।
tossup-player-busts = { $player } बस्ट हो गया और { $points } अंक खो दिए!

# Bank
tossup-you-bank = आप { $points } अंक बैंक करते हैं। कुल स्कोर: { $total }।
tossup-player-banks = { $player } { $points } अंक बैंक करता है। कुल स्कोर: { $total }।

# Winner
tossup-winner = { $player } { $score } अंकों के साथ जीतता है!
tossup-tie-tiebreaker = { $players } के बीच बराबरी है! टाईब्रेकर राउंड!

# Options
tossup-set-rules-variant = नियम संस्करण: { $variant }
tossup-select-rules-variant = नियम संस्करण चुनें:
tossup-option-changed-rules = नियम संस्करण { $variant } में बदल गया

tossup-set-starting-dice = शुरुआती पासे: { $count }
tossup-enter-starting-dice = शुरुआती पासों की संख्या दर्ज करें:
tossup-option-changed-dice = शुरुआती पासे { $count } में बदल गए

# Rules variants
tossup-rules-standard = मानक
tossup-rules-playpalace = प्लेपैलेस

# Rules explanations
tossup-rules-standard-desc = प्रति पासा 3 हरे, 2 पीले, 1 लाल। यदि कोई हरा नहीं और कम से कम एक लाल हो तो बस्ट।
tossup-rules-playpalace-desc = समान वितरण। यदि सभी पासे लाल हों तो बस्ट।

# Disabled reasons
tossup-need-points = आपको बैंक करने के लिए अंकों की आवश्यकता है।
