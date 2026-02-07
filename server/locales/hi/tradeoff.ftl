# Tradeoff game messages

# Game info
game-name-tradeoff = ट्रेडऑफ

# Round and iteration flow
tradeoff-round-start = राउंड { $round }।
tradeoff-iteration = 3 में से हाथ { $iteration }।

# Phase 1: Trading
tradeoff-you-rolled = आपने रोल किया: { $dice }।
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = व्यापार कर रहे हैं
tradeoff-trade-status-keeping = रख रहे हैं
tradeoff-confirm-trades = व्यापार की पुष्टि करें ({ $count } पासे)
tradeoff-keeping = { $value } को रख रहे हैं।
tradeoff-trading = { $value } का व्यापार कर रहे हैं।
tradeoff-player-traded = { $player } ने व्यापार किया: { $dice }।
tradeoff-player-traded-none = { $player } ने सभी पासे रखे।

# Phase 2: Taking from pool
tradeoff-your-turn-take = पूल से पासा लेने की आपकी बारी।
tradeoff-take-die = एक { $value } लें ({ $remaining } बाकी)
tradeoff-you-take = आप एक { $value } लेते हैं।
tradeoff-player-takes = { $player } एक { $value } लेते हैं।

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points } अंक): { $sets }।
tradeoff-no-sets = { $player }: कोई सेट नहीं।

# Set descriptions (concise)
tradeoff-set-triple = { $value }s की तिकड़ी
tradeoff-set-group = { $value }s का समूह
tradeoff-set-mini-straight = मिनी स्ट्रेट { $low }-{ $high }
tradeoff-set-double-triple = दोहरी तिकड़ी ({ $v1 }s और { $v2 }s)
tradeoff-set-straight = स्ट्रेट { $low }-{ $high }
tradeoff-set-double-group = दोहरा समूह ({ $v1 }s और { $v2 }s)
tradeoff-set-all-groups = सभी समूह
tradeoff-set-all-triplets = सभी तिकड़ियाँ

# Round end
tradeoff-round-scores = राउंड { $round } स्कोर:
tradeoff-score-line = { $player }: +{ $round_points } (कुल: { $total })
tradeoff-leader = { $player } { $score } के साथ आगे हैं।

# Game end
tradeoff-winner = { $player } { $score } अंकों के साथ जीतते हैं!
tradeoff-winners-tie = बराबरी है! { $players } { $score } अंकों के साथ बराबर हैं!

# Status checks
tradeoff-view-hand = अपना हाथ देखें
tradeoff-view-pool = पूल देखें
tradeoff-view-players = खिलाड़ियों को देखें
tradeoff-hand-display = आपका हाथ ({ $count } पासे): { $dice }
tradeoff-pool-display = पूल ({ $count } पासे): { $dice }
tradeoff-player-info = { $player }: { $hand }। व्यापार किया: { $traded }।
tradeoff-player-info-no-trade = { $player }: { $hand }। कुछ भी व्यापार नहीं किया।

# Error messages
tradeoff-not-trading-phase = व्यापार चरण में नहीं।
tradeoff-not-taking-phase = लेने के चरण में नहीं।
tradeoff-already-confirmed = पहले से पुष्टि की गई।
tradeoff-no-die = टॉगल करने के लिए कोई पासा नहीं।
tradeoff-no-more-takes = अब और नहीं ले सकते।
tradeoff-not-in-pool = वह पासा पूल में नहीं है।

# Options
tradeoff-set-target = लक्ष्य स्कोर: { $score }
tradeoff-enter-target = लक्ष्य स्कोर दर्ज करें:
tradeoff-option-changed-target = लक्ष्य स्कोर { $score } पर सेट किया गया।
