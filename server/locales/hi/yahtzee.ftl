# Yahtzee game messages

# Game info
game-name-yahtzee = याट्ज़ी

# Actions - Rolling
yahtzee-roll = फिर से फेंकें ({ $count } बचे)
yahtzee-roll-all = पासे फेंकें

# Upper section scoring categories
yahtzee-score-ones = { $points } अंकों के लिए इक्के
yahtzee-score-twos = { $points } अंकों के लिए दुक्के
yahtzee-score-threes = { $points } अंकों के लिए तिक्के
yahtzee-score-fours = { $points } अंकों के लिए चौके
yahtzee-score-fives = { $points } अंकों के लिए पंचके
yahtzee-score-sixes = { $points } अंकों के लिए छक्के

# Lower section scoring categories
yahtzee-score-three-kind = { $points } अंकों के लिए तीन एक जैसे
yahtzee-score-four-kind = { $points } अंकों के लिए चार एक जैसे
yahtzee-score-full-house = { $points } अंकों के लिए फुल हाउस
yahtzee-score-small-straight = { $points } अंकों के लिए छोटी स्ट्रेट
yahtzee-score-large-straight = { $points } अंकों के लिए बड़ी स्ट्रेट
yahtzee-score-yahtzee = { $points } अंकों के लिए याट्ज़ी
yahtzee-score-chance = { $points } अंकों के लिए चांस

# Game events
yahtzee-you-rolled = आपने फेंका: { $dice }। शेष फेंक: { $remaining }
yahtzee-player-rolled = { $player } ने फेंका: { $dice }। शेष फेंक: { $remaining }

# Scoring announcements
yahtzee-you-scored = आपने { $category } में { $points } अंक स्कोर किए।
yahtzee-player-scored = { $player } ने { $category } में { $points } स्कोर किए।

# Yahtzee bonus
yahtzee-you-bonus = याट्ज़ी बोनस! +100 अंक
yahtzee-player-bonus = { $player } को याट्ज़ी बोनस मिला! +100 अंक

# Upper section bonus
yahtzee-you-upper-bonus = ऊपरी खंड बोनस! +35 अंक (ऊपरी खंड में { $total })
yahtzee-player-upper-bonus = { $player } ने ऊपरी खंड बोनस अर्जित किया! +35 अंक
yahtzee-you-upper-bonus-missed = आप ऊपरी खंड बोनस से चूक गए (ऊपरी खंड में { $total }, 63 की आवश्यकता थी)।
yahtzee-player-upper-bonus-missed = { $player } ऊपरी खंड बोनस से चूक गया।

# Scoring mode
yahtzee-choose-category = स्कोर करने के लिए एक श्रेणी चुनें।
yahtzee-continuing = बारी जारी है।

# Status checks
yahtzee-check-scoresheet = स्कोरकार्ड जांचें
yahtzee-view-dice = हाथ जांचें
yahtzee-your-dice = आपके पासे: { $dice }।
yahtzee-your-dice-kept = आपके पासे: { $dice }। रखे हुए: { $kept }
yahtzee-not-rolled = आपने अभी तक नहीं फेंका है।

# Scoresheet display
yahtzee-scoresheet-header = === { $player } का स्कोरकार्ड ===
yahtzee-scoresheet-upper = ऊपरी खंड:
yahtzee-scoresheet-lower = निचला खंड:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = ऊपरी कुल: { $total } (बोनस: +35)
yahtzee-scoresheet-upper-total-needed = ऊपरी कुल: { $total } (बोनस के लिए { $needed } और चाहिए)
yahtzee-scoresheet-yahtzee-bonus = याट्ज़ी बोनस: { $count } x 100 = { $total }
yahtzee-scoresheet-grand-total = कुल स्कोर: { $total }

# Category names (for announcements)
yahtzee-category-ones = इक्के
yahtzee-category-twos = दुक्के
yahtzee-category-threes = तिक्के
yahtzee-category-fours = चौके
yahtzee-category-fives = पंचके
yahtzee-category-sixes = छक्के
yahtzee-category-three-kind = तीन एक जैसे
yahtzee-category-four-kind = चार एक जैसे
yahtzee-category-full-house = फुल हाउस
yahtzee-category-small-straight = छोटी स्ट्रेट
yahtzee-category-large-straight = बड़ी स्ट्रेट
yahtzee-category-yahtzee = याट्ज़ी
yahtzee-category-chance = चांस

# Game end
yahtzee-winner = { $player } { $score } अंकों के साथ जीतता है!
yahtzee-winners-tie = यह बराबरी है! { $players } सभी ने { $score } अंक स्कोर किए!

# Options
yahtzee-set-rounds = खेलों की संख्या: { $rounds }
yahtzee-enter-rounds = खेलों की संख्या दर्ज करें (1-10):
yahtzee-option-changed-rounds = खेलों की संख्या { $rounds } पर सेट की गई।

# Disabled action reasons
yahtzee-no-rolls-left = आपके पास कोई फेंक नहीं बची।
yahtzee-roll-first = आपको पहले फेंकना होगा।
yahtzee-category-filled = वह श्रेणी पहले से भरी हुई है।
