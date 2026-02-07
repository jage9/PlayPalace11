# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = पिग
pig-category = पासा खेल

# Actions
pig-roll = पासा रोल करें
pig-bank = { $points } अंक बैंक करें

# Game events (Pig-specific)
pig-rolls = { $player } पासा रोल कर रहा है...
pig-roll-result = एक { $roll }, कुल { $total } के लिए
pig-bust = अरे नहीं, एक 1! { $player } { $points } अंक खो देता है।
pig-bank-action = { $player } { $points } बैंक करने का फैसला करता है, कुल { $total } के लिए
pig-winner = हमारे पास एक विजेता है, और वह { $player } है!

# Pig-specific options
pig-set-min-bank = न्यूनतम बैंक: { $points }
pig-set-dice-sides = पासा भुजाएं: { $sides }
pig-enter-min-bank = बैंक करने के लिए न्यूनतम अंक दर्ज करें:
pig-enter-dice-sides = पासा भुजाओं की संख्या दर्ज करें:
pig-option-changed-min-bank = न्यूनतम बैंक अंक { $points } में बदल गए
pig-option-changed-dice = पासा में अब { $sides } भुजाएं हैं

# Disabled reasons
pig-need-more-points = आपको बैंक करने के लिए अधिक अंकों की आवश्यकता है।

# Validation errors
pig-error-min-bank-too-high = न्यूनतम बैंक अंक लक्ष्य स्कोर से कम होना चाहिए।
