# Yahtzee game messages (isiZulu)

# Game info
game-name-yahtzee = Yahtzee

# Actions - Rolling
yahtzee-roll = Phonsa kabusha (kusele { $count })
yahtzee-roll-all = Phonsa amadayisi

# Upper section scoring categories
yahtzee-score-ones = Ama-Ones ngamaphuzu angu-{ $points }
yahtzee-score-twos = Ama-Twos ngamaphuzu angu-{ $points }
yahtzee-score-threes = Ama-Threes ngamaphuzu angu-{ $points }
yahtzee-score-fours = Ama-Fours ngamaphuzu angu-{ $points }
yahtzee-score-fives = Ama-Fives ngamaphuzu angu-{ $points }
yahtzee-score-sixes = Ama-Sixes ngamaphuzu angu-{ $points }

# Lower section scoring categories
yahtzee-score-three-kind = Amathathu Ohlobo Olulodwa ngamaphuzu angu-{ $points }
yahtzee-score-four-kind = Amane Ohlobo Olulodwa ngamaphuzu angu-{ $points }
yahtzee-score-full-house = Indlu Egcwele ngamaphuzu angu-{ $points }
yahtzee-score-small-straight = Ukulandelana Okuncane ngamaphuzu angu-{ $points }
yahtzee-score-large-straight = Ukulandelana Okukhulu ngamaphuzu angu-{ $points }
yahtzee-score-yahtzee = I-Yahtzee ngamaphuzu angu-{ $points }
yahtzee-score-chance = Ithuba ngamaphuzu angu-{ $points }

# Game events
yahtzee-you-rolled = Wena uphonse: { $dice }. Ukuphonsa okusele: { $remaining }
yahtzee-player-rolled = U-{ $player } uphonse: { $dice }. Ukuphonsa okusele: { $remaining }

# Scoring announcements
yahtzee-you-scored = Wena uphumelele amaphuzu angu-{ $points } ku-{ $category }.
yahtzee-player-scored = U-{ $player } uphumelele amaphuzu angu-{ $points } ku-{ $category }.

# Yahtzee bonus
yahtzee-you-bonus = Inzuzo ye-Yahtzee! +100 amaphuzu
yahtzee-player-bonus = U-{ $player } uthole inzuzo ye-Yahtzee! +100 amaphuzu

# Upper section bonus
yahtzee-you-upper-bonus = Inzuzo yesigaba esiphezulu! +35 amaphuzu ({ $total } esigabeni esiphezulu)
yahtzee-player-upper-bonus = U-{ $player } uphumelele inzuzo yesigaba esiphezulu! +35 amaphuzu
yahtzee-you-upper-bonus-missed = Ulahlekelwe inzuzo yesigaba esiphezulu ({ $total } esigabeni esiphezulu, udinga 63).
yahtzee-player-upper-bonus-missed = U-{ $player } ulahlekelwe inzuzo yesigaba esiphezulu.

# Scoring mode
yahtzee-choose-category = Khetha isigaba sokubala amaphuzu.
yahtzee-continuing = Iqhubeka ishintshi.

# Status checks
yahtzee-check-scoresheet = Bheka ikhadi lamaphuzu
yahtzee-view-dice = Bheka isandla
yahtzee-your-dice = Amadayisi akho: { $dice }.
yahtzee-your-dice-kept = Amadayisi akho: { $dice }. Kugcinwa: { $kept }
yahtzee-not-rolled = Awukaphonsi.

# Scoresheet display
yahtzee-scoresheet-header = === Ikhadi Lamaphuzu Lika-{ $player } ===
yahtzee-scoresheet-upper = Isigaba Esiphezulu:
yahtzee-scoresheet-lower = Isigaba Esiphansi:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = Isamba Esiphezulu: { $total } (INZUZO: +35)
yahtzee-scoresheet-upper-total-needed = Isamba Esiphezulu: { $total } (kudinga { $needed } okwengeziwe kwengeziwe)
yahtzee-scoresheet-yahtzee-bonus = Izinzuzo Ze-Yahtzee: { $count } x 100 = { $total }
yahtzee-scoresheet-grand-total = ISAMBA SAMAPHUZU: { $total }

# Category names (for announcements)
yahtzee-category-ones = Ama-Ones
yahtzee-category-twos = Ama-Twos
yahtzee-category-threes = Ama-Threes
yahtzee-category-fours = Ama-Fours
yahtzee-category-fives = Ama-Fives
yahtzee-category-sixes = Ama-Sixes
yahtzee-category-three-kind = Amathathu Ohlobo Olulodwa
yahtzee-category-four-kind = Amane Ohlobo Olulodwa
yahtzee-category-full-house = Indlu Egcwele
yahtzee-category-small-straight = Ukulandelana Okuncane
yahtzee-category-large-straight = Ukulandelana Okukhulu
yahtzee-category-yahtzee = I-Yahtzee
yahtzee-category-chance = Ithuba

# Game end
yahtzee-winner = U-{ $player } uyawina ngamaphuzu angu-{ $score }!
yahtzee-winners-tie = Kuyalinganiswa! { $players } bonke baphumelele amaphuzu angu-{ $score }!

# Options
yahtzee-set-rounds = Inani lemidlalo: { $rounds }
yahtzee-enter-rounds = Faka inani lemidlalo (1-10):
yahtzee-option-changed-rounds = Inani lemidlalo lisetelwe ku-{ $rounds }.

# Disabled action reasons
yahtzee-no-rolls-left = Awunayo ukuphonsa okusele.
yahtzee-roll-first = Udinga ukuphonsa kuqala.
yahtzee-category-filled = Leso sigaba sesigcwele.
