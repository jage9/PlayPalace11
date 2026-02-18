# Farkle game messages

# Game info
game-name-farkle = फार्कल

# Actions - Roll and Bank
farkle-roll = { $count } { $count ->
    [one] पासा
   *[other] पासे
} फेंकें
farkle-bank = { $points } अंक जमा करें

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = { $points } अंकों के लिए एकल 1
farkle-take-single-five = { $points } अंकों के लिए एकल 5
farkle-take-three-kind = { $points } अंकों के लिए तीन { $number }
farkle-take-four-kind = { $points } अंकों के लिए चार { $number }
farkle-take-five-kind = { $points } अंकों के लिए पांच { $number }
farkle-take-six-kind = { $points } अंकों के लिए छह { $number }
farkle-take-small-straight = { $points } अंकों के लिए छोटी स्ट्रेट
farkle-take-large-straight = { $points } अंकों के लिए बड़ी स्ट्रेट
farkle-take-three-pairs = { $points } अंकों के लिए तीन जोड़े
farkle-take-double-triplets = { $points } अंकों के लिए दोहरी तिकड़ी
farkle-take-full-house = { $points } अंकों के लिए फुल हाउस

# Game events (matching v10 exactly)
farkle-rolls = { $player } { $count } { $count ->
    [one] पासा
   *[other] पासे
} फेंकता है...
farkle-you-roll = आप { $count } { $count ->
    [one] पासा
   *[other] पासे
} फेंकते हैं...
farkle-roll-result = { $dice }
farkle-farkle = फार्कल! { $player } { $points } अंक खो देता है
farkle-you-farkle = फार्कल! आप { $points } अंक खो देते हैं
farkle-takes-combo = { $player } { $points } अंकों के लिए { $combo } लेता है
farkle-you-take-combo = आप { $points } अंकों के लिए { $combo } लेते हैं
farkle-hot-dice = हॉट डाइस!
farkle-banks = { $player } कुल { $total } के लिए { $points } अंक जमा करता है
farkle-you-bank = आप कुल { $total } के लिए { $points } अंक जमा करते हैं
farkle-winner = { $player } { $score } अंकों के साथ जीतता है!
farkle-you-win = आप { $score } अंकों के साथ जीतते हैं!
farkle-winners-tie = यह बराबरी है! विजेता: { $players }

# Check turn score action
farkle-turn-score = { $player } के पास इस बारी में { $points } अंक हैं।
farkle-no-turn = अभी कोई बारी नहीं ले रहा है।

# Farkle-specific options
farkle-set-target-score = लक्ष्य अंक: { $score }
farkle-enter-target-score = लक्ष्य अंक दर्ज करें (500-5000):
farkle-option-changed-target = लक्ष्य अंक { $score } पर सेट किया गया।

# Disabled action reasons
farkle-must-take-combo = आपको पहले एक स्कोरिंग संयोजन लेना होगा।
farkle-cannot-bank = आप अभी जमा नहीं कर सकते।

# Additional Farkle options
farkle-set-initial-bank-score = प्रारंभिक बैंक स्कोर: { $score }
farkle-enter-initial-bank-score = प्रारंभिक बैंक स्कोर दर्ज करें (0-1000):
farkle-option-changed-initial-bank-score = प्रारंभिक बैंक स्कोर { $score } पर सेट किया गया।
farkle-toggle-hot-dice-multiplier = हॉट डाइस गुणक: { $enabled }
farkle-option-changed-hot-dice-multiplier = हॉट डाइस गुणक { $enabled } पर सेट किया गया।

# Action feedback
farkle-minimum-initial-bank-score = न्यूनतम प्रारंभिक बैंक स्कोर { $score } है।
