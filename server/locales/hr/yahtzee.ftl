# Yahtzee game messages

# Game info
game-name-yahtzee = Yahtzee

# Actions - Rolling
yahtzee-roll = Ponovno bacite ({ $count } preostalo)
yahtzee-roll-all = Bacite kockice

# Upper section scoring categories
yahtzee-score-ones = Jedinice za { $points } bodova
yahtzee-score-twos = Dvojke za { $points } bodova
yahtzee-score-threes = Trojke za { $points } bodova
yahtzee-score-fours = Četvorke za { $points } bodova
yahtzee-score-fives = Petice za { $points } bodova
yahtzee-score-sixes = Šestice za { $points } bodova

# Lower section scoring categories
yahtzee-score-three-kind = Tri jednaka za { $points } bodova
yahtzee-score-four-kind = Četiri jednaka za { $points } bodova
yahtzee-score-full-house = Puni kućica za { $points } bodova
yahtzee-score-small-straight = Mali niz za { $points } bodova
yahtzee-score-large-straight = Veliki niz za { $points } bodova
yahtzee-score-yahtzee = Yahtzee za { $points } bodova
yahtzee-score-chance = Šansa za { $points } bodova

# Game events
yahtzee-you-rolled = Bacili ste: { $dice }. Preostala bacanja: { $remaining }
yahtzee-player-rolled = { $player } je bacio: { $dice }. Preostala bacanja: { $remaining }

# Scoring announcements
yahtzee-you-scored = Osvojili ste { $points } bodova u { $category }.
yahtzee-player-scored = { $player } je osvojio { $points } u { $category }.

# Yahtzee bonus
yahtzee-you-bonus = Yahtzee bonus! +100 bodova
yahtzee-player-bonus = { $player } je dobio Yahtzee bonus! +100 bodova

# Upper section bonus
yahtzee-you-upper-bonus = Bonus gornje sekcije! +35 bodova ({ $total } u gornjoj sekciji)
yahtzee-player-upper-bonus = { $player } je zaradio bonus gornje sekcije! +35 bodova
yahtzee-you-upper-bonus-missed = Promašili ste bonus gornje sekcije ({ $total } u gornjoj sekciji, potrebno 63).
yahtzee-player-upper-bonus-missed = { $player } je promašio bonus gornje sekcije.

# Scoring mode
yahtzee-choose-category = Odaberite kategoriju za bodovanje.
yahtzee-continuing = Nastavljanje poteza.

# Status checks
yahtzee-check-scoresheet = Provjerite karticu rezultata
yahtzee-view-dice = Provjerite ruku
yahtzee-your-dice = Vaše kockice: { $dice }.
yahtzee-your-dice-kept = Vaše kockice: { $dice }. Zadržavate: { $kept }
yahtzee-not-rolled = Još niste bacili.

# Scoresheet display
yahtzee-scoresheet-header = === Kartica rezultata igrača { $player } ===
yahtzee-scoresheet-upper = Gornja sekcija:
yahtzee-scoresheet-lower = Donja sekcija:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = Ukupno gornje: { $total } (BONUS: +35)
yahtzee-scoresheet-upper-total-needed = Ukupno gornje: { $total } (još { $needed } za bonus)
yahtzee-scoresheet-yahtzee-bonus = Yahtzee bonusi: { $count } x 100 = { $total }
yahtzee-scoresheet-grand-total = UKUPNI REZULTAT: { $total }

# Category names (for announcements)
yahtzee-category-ones = Jedinice
yahtzee-category-twos = Dvojke
yahtzee-category-threes = Trojke
yahtzee-category-fours = Četvorke
yahtzee-category-fives = Petice
yahtzee-category-sixes = Šestice
yahtzee-category-three-kind = Tri jednaka
yahtzee-category-four-kind = Četiri jednaka
yahtzee-category-full-house = Puni kućica
yahtzee-category-small-straight = Mali niz
yahtzee-category-large-straight = Veliki niz
yahtzee-category-yahtzee = Yahtzee
yahtzee-category-chance = Šansa

# Game end
yahtzee-winner = { $player } pobjeđuje sa { $score } bodova!
yahtzee-winners-tie = Neriješeno! { $players } svi su osvojili { $score } bodova!

# Options
yahtzee-set-rounds = Broj igara: { $rounds }
yahtzee-enter-rounds = Unesite broj igara (1-10):
yahtzee-option-changed-rounds = Broj igara postavljen na { $rounds }.

# Disabled action reasons
yahtzee-no-rolls-left = Nemate više bacanja.
yahtzee-roll-first = Morate prvo baciti.
yahtzee-category-filled = Ta kategorija je već popunjena.
