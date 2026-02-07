# Yahtzee game messages

# Game info
game-name-yahtzee = Yahtzee

# Actions - Rolling
yahtzee-roll = Znovu hoďte ({ $count } zostáva)
yahtzee-roll-all = Hoďte kockami

# Upper section scoring categories
yahtzee-score-ones = Jednotky za { $points } bodov
yahtzee-score-twos = Dvojky za { $points } bodov
yahtzee-score-threes = Trojky za { $points } bodov
yahtzee-score-fours = Štvorky za { $points } bodov
yahtzee-score-fives = Pätky za { $points } bodov
yahtzee-score-sixes = Šestky za { $points } bodov

# Lower section scoring categories
yahtzee-score-three-kind = Tri rovnaké za { $points } bodov
yahtzee-score-four-kind = Štyri rovnaké za { $points } bodov
yahtzee-score-full-house = Full house za { $points } bodov
yahtzee-score-small-straight = Malá postupnosť za { $points } bodov
yahtzee-score-large-straight = Veľká postupnosť za { $points } bodov
yahtzee-score-yahtzee = Yahtzee za { $points } bodov
yahtzee-score-chance = Šanca za { $points } bodov

# Game events
yahtzee-you-rolled = Hodili ste: { $dice }. Zostávajúce hody: { $remaining }
yahtzee-player-rolled = { $player } hodil: { $dice }. Zostávajúce hody: { $remaining }

# Scoring announcements
yahtzee-you-scored = Získali ste { $points } bodov v { $category }.
yahtzee-player-scored = { $player } získal { $points } v { $category }.

# Yahtzee bonus
yahtzee-you-bonus = Yahtzee bonus! +100 bodov
yahtzee-player-bonus = { $player } získal Yahtzee bonus! +100 bodov

# Upper section bonus
yahtzee-you-upper-bonus = Bonus hornej sekcie! +35 bodov ({ $total } v hornej sekcii)
yahtzee-player-upper-bonus = { $player } získal bonus hornej sekcie! +35 bodov
yahtzee-you-upper-bonus-missed = Premeškal si bonus hornej sekcie ({ $total } v hornej sekcii, potrebných 63).
yahtzee-player-upper-bonus-missed = { $player } premeškal bonus hornej sekcie.

# Scoring mode
yahtzee-choose-category = Vyberte kategóriu na bodovanie.
yahtzee-continuing = Pokračovanie ťahu.

# Status checks
yahtzee-check-scoresheet = Skontrolovať skórovací hárok
yahtzee-view-dice = Skontrolovať ruku
yahtzee-your-dice = Vaše kocky: { $dice }.
yahtzee-your-dice-kept = Vaše kocky: { $dice }. Podržané: { $kept }
yahtzee-not-rolled = Ešte ste nehodili.

# Scoresheet display
yahtzee-scoresheet-header = === Skórovací hárok hráča { $player } ===
yahtzee-scoresheet-upper = Horná sekcia:
yahtzee-scoresheet-lower = Dolná sekcia:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = Horný súčet: { $total } (BONUS: +35)
yahtzee-scoresheet-upper-total-needed = Horný súčet: { $total } (ešte { $needed } na bonus)
yahtzee-scoresheet-yahtzee-bonus = Yahtzee bonusy: { $count } x 100 = { $total }
yahtzee-scoresheet-grand-total = CELKOVÉ SKÓRE: { $total }

# Category names (for announcements)
yahtzee-category-ones = Jednotky
yahtzee-category-twos = Dvojky
yahtzee-category-threes = Trojky
yahtzee-category-fours = Štvorky
yahtzee-category-fives = Pätky
yahtzee-category-sixes = Šestky
yahtzee-category-three-kind = Tri rovnaké
yahtzee-category-four-kind = Štyri rovnaké
yahtzee-category-full-house = Full house
yahtzee-category-small-straight = Malá postupnosť
yahtzee-category-large-straight = Veľká postupnosť
yahtzee-category-yahtzee = Yahtzee
yahtzee-category-chance = Šanca

# Game end
yahtzee-winner = { $player } vyhráva s { $score } bodmi!
yahtzee-winners-tie = Remíza! { $players } všetci získali { $score } bodov!

# Options
yahtzee-set-rounds = Počet hier: { $rounds }
yahtzee-enter-rounds = Zadajte počet hier (1-10):
yahtzee-option-changed-rounds = Počet hier nastavený na { $rounds }.

# Disabled action reasons
yahtzee-no-rolls-left = Nemáte žiadne hody.
yahtzee-roll-first = Najprv musíte hodiť.
yahtzee-category-filled = Táto kategória je už vyplnená.
