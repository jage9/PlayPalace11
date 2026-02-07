# 1-4-24 (Midnight) game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-midnight = 1-4-24
midnight-category = पासा खेल

# Actions
midnight-roll = पासे फेंकें
midnight-keep-die = { $value } रखें
midnight-bank = जमा करें

# Game events
midnight-turn-start = { $player } की बारी।
midnight-you-rolled = आपने फेंका: { $dice }।
midnight-player-rolled = { $player } ने फेंका: { $dice }।

# Keeping dice
midnight-you-keep = आप { $die } रखते हैं।
midnight-player-keeps = { $player } { $die } रखता है।
midnight-you-unkeep = आप { $die } हटाते हैं।
midnight-player-unkeeps = { $player } { $die } हटाता है।

# Turn status
midnight-you-have-kept = रखे हुए पासे: { $kept }। शेष फेंक: { $remaining }।
midnight-player-has-kept = { $player } ने रखा है: { $kept }। { $remaining } पासे शेष।

# Scoring
midnight-you-scored = आपने { $score } अंक स्कोर किए।
midnight-scored = { $player } ने { $score } अंक स्कोर किए।
midnight-you-disqualified = आपके पास 1 और 4 दोनों नहीं हैं। अयोग्य!
midnight-player-disqualified = { $player } के पास 1 और 4 दोनों नहीं हैं। अयोग्य!

# Round results
midnight-round-winner = { $player } राउंड जीतता है!
midnight-round-tie = { $players } के बीच राउंड बराबरी।
midnight-all-disqualified = सभी खिलाड़ी अयोग्य! इस राउंड में कोई विजेता नहीं।

# Game winner
midnight-game-winner = { $player } { $wins } राउंड जीत के साथ खेल जीतता है!
midnight-game-tie = यह बराबरी है! { $players } ने प्रत्येक { $wins } राउंड जीते।

# Options
midnight-set-rounds = खेलने के लिए राउंड: { $rounds }
midnight-enter-rounds = खेलने के लिए राउंड की संख्या दर्ज करें:
midnight-option-changed-rounds = खेलने के लिए राउंड { $rounds } में बदले गए

# Disabled reasons
midnight-need-to-roll = आपको पहले पासे फेंकने होंगे।
midnight-no-dice-to-keep = रखने के लिए कोई पासा उपलब्ध नहीं है।
midnight-must-keep-one = आपको प्रति फेंक कम से कम एक पासा रखना होगा।
midnight-must-roll-first = आपको पहले पासे फेंकने होंगे।
midnight-keep-all-first = जमा करने से पहले आपको सभी पासे रखने होंगे।
