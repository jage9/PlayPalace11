# Scopa game messages
# Note: Common messages like round-start, turn-start, target-score, team-mode are in games.ftl

# Game name
game-name-scopa = स्कोपा

# Game events
scopa-initial-table = टेबल कार्ड: { $cards }
scopa-no-initial-table = शुरू करने के लिए टेबल पर कोई कार्ड नहीं।
scopa-you-collect = आप { $card } के साथ { $cards } एकत्र करते हैं
scopa-player-collects = { $player } { $card } के साथ { $cards } एकत्र करता है
scopa-you-put-down = आप { $card } रखते हैं।
scopa-player-puts-down = { $player } { $card } रखता है।
scopa-scopa-suffix =  - स्कोपा!
scopa-clear-table-suffix = , टेबल को साफ करते हुए।
scopa-remaining-cards = { $player } को शेष टेबल कार्ड मिलते हैं।
scopa-scoring-round = स्कोरिंग राउंड...
scopa-most-cards = { $player } सबसे अधिक कार्ड के लिए 1 अंक स्कोर करता है ({ $count } कार्ड)।
scopa-most-cards-tie = सबसे अधिक कार्ड बराबरी है - कोई अंक नहीं दिया गया।
scopa-most-diamonds = { $player } सबसे अधिक डायमंड के लिए 1 अंक स्कोर करता है ({ $count } डायमंड)।
scopa-most-diamonds-tie = सबसे अधिक डायमंड बराबरी है - कोई अंक नहीं दिया गया।
scopa-seven-diamonds = { $player } डायमंड के 7 के लिए 1 अंक स्कोर करता है।
scopa-seven-diamonds-multi = { $player } सबसे अधिक डायमंड के 7 के लिए 1 अंक स्कोर करता है ({ $count } × डायमंड के 7)।
scopa-seven-diamonds-tie = डायमंड का 7 बराबरी है - कोई अंक नहीं दिया गया।
scopa-most-sevens = { $player } सबसे अधिक सात के लिए 1 अंक स्कोर करता है ({ $count } सात)।
scopa-most-sevens-tie = सबसे अधिक सात बराबरी है - कोई अंक नहीं दिया गया।
scopa-round-scores = राउंड स्कोर:
scopa-round-score-line = { $player }: +{ $round_score } (कुल: { $total_score })
scopa-table-empty = टेबल पर कोई कार्ड नहीं है।
scopa-no-such-card = उस स्थिति पर कोई कार्ड नहीं।
scopa-captured-count = आपने { $count } कार्ड कैप्चर किए हैं

# View actions
scopa-view-table = टेबल देखें
scopa-view-captured = कैप्चर किए गए देखें

# Scopa-specific options
scopa-enter-target-score = लक्ष्य स्कोर दर्ज करें (1-121)
scopa-set-cards-per-deal = प्रति डील कार्ड: { $cards }
scopa-enter-cards-per-deal = प्रति डील कार्ड दर्ज करें (1-10)
scopa-set-decks = डेक की संख्या: { $decks }
scopa-enter-decks = डेक की संख्या दर्ज करें (1-6)
scopa-toggle-escoba = एस्कोबा (15 का योग): { $enabled }
scopa-toggle-hints = कैप्चर संकेत दिखाएं: { $enabled }
scopa-set-mechanic = स्कोपा मैकेनिक: { $mechanic }
scopa-select-mechanic = स्कोपा मैकेनिक चुनें
scopa-toggle-instant-win = स्कोपा पर तुरंत जीत: { $enabled }
scopa-toggle-team-scoring = स्कोरिंग के लिए टीम कार्ड पूल करें: { $enabled }
scopa-toggle-inverse = इनवर्स मोड (लक्ष्य पहुंचना = उन्मूलन): { $enabled }

# Option change announcements
scopa-option-changed-cards = प्रति डील कार्ड { $cards } पर सेट किया गया।
scopa-option-changed-decks = डेक की संख्या { $decks } पर सेट की गई।
scopa-option-changed-escoba = एस्कोबा { $enabled }।
scopa-option-changed-hints = कैप्चर संकेत { $enabled }।
scopa-option-changed-mechanic = स्कोपा मैकेनिक { $mechanic } पर सेट किया गया।
scopa-option-changed-instant = स्कोपा पर तुरंत जीत { $enabled }।
scopa-option-changed-team-scoring = टीम कार्ड स्कोरिंग { $enabled }।
scopa-option-changed-inverse = इनवर्स मोड { $enabled }।

# Scopa mechanic choices
scopa-mechanic-normal = सामान्य
scopa-mechanic-no_scopas = कोई स्कोपा नहीं
scopa-mechanic-only_scopas = केवल स्कोपा

# Disabled action reasons
scopa-timer-not-active = राउंड टाइमर सक्रिय नहीं है।

# Validation errors
scopa-error-not-enough-cards = { $decks } { $decks ->
    [one] डेक
    *[other] डेक
} में { $players } { $players ->
    [one] खिलाड़ी
    *[other] खिलाड़ियों
} के लिए पर्याप्त कार्ड नहीं हैं, प्रत्येक के लिए { $cards_per_deal } कार्ड। ({ $cards_per_deal } × { $players } = { $cards_needed } कार्ड चाहिए, लेकिन केवल { $total_cards } हैं।)
