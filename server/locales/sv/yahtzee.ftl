# Yahtzee game messages

# Game info
game-name-yahtzee = Yahtzee

# Actions - Rolling
yahtzee-roll = Kasta om ({ $count } kvar)
yahtzee-roll-all = Kasta tärningarna

# Upper section scoring categories
yahtzee-score-ones = Ettor för { $points } poäng
yahtzee-score-twos = Tvåor för { $points } poäng
yahtzee-score-threes = Treor för { $points } poäng
yahtzee-score-fours = Fyror för { $points } poäng
yahtzee-score-fives = Femmor för { $points } poäng
yahtzee-score-sixes = Sexor för { $points } poäng

# Lower section scoring categories
yahtzee-score-three-kind = Triss för { $points } poäng
yahtzee-score-four-kind = Fyrtal för { $points } poäng
yahtzee-score-full-house = Kåk för { $points } poäng
yahtzee-score-small-straight = Liten stege för { $points } poäng
yahtzee-score-large-straight = Stor stege för { $points } poäng
yahtzee-score-yahtzee = Yahtzee för { $points } poäng
yahtzee-score-chance = Chans för { $points } poäng

# Game events
yahtzee-you-rolled = Du kastade: { $dice }. Kast kvar: { $remaining }
yahtzee-player-rolled = { $player } kastade: { $dice }. Kast kvar: { $remaining }

# Scoring announcements
yahtzee-you-scored = Du fick { $points } poäng i { $category }.
yahtzee-player-scored = { $player } fick { $points } i { $category }.

# Yahtzee bonus
yahtzee-you-bonus = Yahtzee-bonus! +100 poäng
yahtzee-player-bonus = { $player } fick en Yahtzee-bonus! +100 poäng

# Upper section bonus
yahtzee-you-upper-bonus = Övre sektionsbonus! +35 poäng ({ $total } i övre sektionen)
yahtzee-player-upper-bonus = { $player } fick den övre sektionsbonusen! +35 poäng
yahtzee-you-upper-bonus-missed = Du missade den övre sektionsbonusen ({ $total } i övre sektionen, behövde 63).
yahtzee-player-upper-bonus-missed = { $player } missade den övre sektionsbonusen.

# Scoring mode
yahtzee-choose-category = Välj en kategori att poängsätta i.
yahtzee-continuing = Fortsätter tur.

# Status checks
yahtzee-check-scoresheet = Kontrollera poängkort
yahtzee-view-dice = Kontrollera hand
yahtzee-your-dice = Dina tärningar: { $dice }.
yahtzee-your-dice-kept = Dina tärningar: { $dice }. Behåller: { $kept }
yahtzee-not-rolled = Du har inte kastat än.

# Scoresheet display
yahtzee-scoresheet-header = === { $player }s poängkort ===
yahtzee-scoresheet-upper = Övre sektion:
yahtzee-scoresheet-lower = Undre sektion:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = Övre totalt: { $total } (BONUS: +35)
yahtzee-scoresheet-upper-total-needed = Övre totalt: { $total } ({ $needed } till för bonus)
yahtzee-scoresheet-yahtzee-bonus = Yahtzee-bonusar: { $count } x 100 = { $total }
yahtzee-scoresheet-grand-total = TOTALT POÄNG: { $total }

# Category names (for announcements)
yahtzee-category-ones = Ettor
yahtzee-category-twos = Tvåor
yahtzee-category-threes = Treor
yahtzee-category-fours = Fyror
yahtzee-category-fives = Femmor
yahtzee-category-sixes = Sexor
yahtzee-category-three-kind = Triss
yahtzee-category-four-kind = Fyrtal
yahtzee-category-full-house = Kåk
yahtzee-category-small-straight = Liten stege
yahtzee-category-large-straight = Stor stege
yahtzee-category-yahtzee = Yahtzee
yahtzee-category-chance = Chans

# Game end
yahtzee-winner = { $player } vinner med { $score } poäng!
yahtzee-winners-tie = Det är oavgjort! { $players } fick alla { $score } poäng!

# Options
yahtzee-set-rounds = Antal spel: { $rounds }
yahtzee-enter-rounds = Ange antal spel (1-10):
yahtzee-option-changed-rounds = Antal spel inställt på { $rounds }.

# Disabled action reasons
yahtzee-no-rolls-left = Du har inga kast kvar.
yahtzee-roll-first = Du måste kasta först.
yahtzee-category-filled = Den kategorin är redan fylld.
