# Yahtzee game messages

# Game info
game-name-yahtzee = Yahtzee

# Actions - Rolling
yahtzee-roll = Ponovno vrzite ({ $count } preostalo)
yahtzee-roll-all = Vrzite kocke

# Upper section scoring categories
yahtzee-score-ones = Enke za { $points } točk
yahtzee-score-twos = Dvojke za { $points } točk
yahtzee-score-threes = Trojke za { $points } točk
yahtzee-score-fours = Četvorke za { $points } točk
yahtzee-score-fives = Petke za { $points } točk
yahtzee-score-sixes = Šestke za { $points } točk

# Lower section scoring categories
yahtzee-score-three-kind = Tri enake za { $points } točk
yahtzee-score-four-kind = Štiri enake za { $points } točk
yahtzee-score-full-house = Full house za { $points } točk
yahtzee-score-small-straight = Mala lestvica za { $points } točk
yahtzee-score-large-straight = Velika lestvica za { $points } točk
yahtzee-score-yahtzee = Yahtzee za { $points } točk
yahtzee-score-chance = Priložnost za { $points } točk

# Game events
yahtzee-you-rolled = Vrgli ste: { $dice }. Preostali meti: { $remaining }
yahtzee-player-rolled = { $player } je vrgel: { $dice }. Preostali meti: { $remaining }

# Scoring announcements
yahtzee-you-scored = Dosegli ste { $points } točk v { $category }.
yahtzee-player-scored = { $player } je dosegel { $points } v { $category }.

# Yahtzee bonus
yahtzee-you-bonus = Yahtzee bonus! +100 točk
yahtzee-player-bonus = { $player } je dobil Yahtzee bonus! +100 točk

# Upper section bonus
yahtzee-you-upper-bonus = Bonus zgornjega dela! +35 točk ({ $total } v zgornjem delu)
yahtzee-player-upper-bonus = { $player } je zaslužil bonus zgornjega dela! +35 točk
yahtzee-you-upper-bonus-missed = Zamudili ste bonus zgornjega dela ({ $total } v zgornjem delu, potrebovali 63).
yahtzee-player-upper-bonus-missed = { $player } je zamudil bonus zgornjega dela.

# Scoring mode
yahtzee-choose-category = Izberite kategorijo za točkovanje.
yahtzee-continuing = Nadaljevanje poteze.

# Status checks
yahtzee-check-scoresheet = Preverite točkovni list
yahtzee-view-dice = Preverite roko
yahtzee-your-dice = Vaše kocke: { $dice }.
yahtzee-your-dice-kept = Vaše kocke: { $dice }. Obdržane: { $kept }
yahtzee-not-rolled = Še niste vrgli.

# Scoresheet display
yahtzee-scoresheet-header = === Točkovni list igralca { $player } ===
yahtzee-scoresheet-upper = Zgornji del:
yahtzee-scoresheet-lower = Spodnji del:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = Zgornji skupaj: { $total } (BONUS: +35)
yahtzee-scoresheet-upper-total-needed = Zgornji skupaj: { $total } (še { $needed } za bonus)
yahtzee-scoresheet-yahtzee-bonus = Yahtzee bonusi: { $count } x 100 = { $total }
yahtzee-scoresheet-grand-total = SKUPNI REZULTAT: { $total }

# Category names (for announcements)
yahtzee-category-ones = Enke
yahtzee-category-twos = Dvojke
yahtzee-category-threes = Trojke
yahtzee-category-fours = Četvorke
yahtzee-category-fives = Petke
yahtzee-category-sixes = Šestke
yahtzee-category-three-kind = Tri enake
yahtzee-category-four-kind = Štiri enake
yahtzee-category-full-house = Full house
yahtzee-category-small-straight = Mala lestvica
yahtzee-category-large-straight = Velika lestvica
yahtzee-category-yahtzee = Yahtzee
yahtzee-category-chance = Priložnost

# Game end
yahtzee-winner = { $player } zmaga s { $score } točkami!
yahtzee-winners-tie = Neodločeno! { $players } so vsi dosegli { $score } točk!

# Options
yahtzee-set-rounds = Število iger: { $rounds }
yahtzee-enter-rounds = Vnesite število iger (1-10):
yahtzee-option-changed-rounds = Število iger nastavljeno na { $rounds }.

# Disabled action reasons
yahtzee-no-rolls-left = Nimate več metov.
yahtzee-roll-first = Najprej morate vreči.
yahtzee-category-filled = Ta kategorija je že zapolnjena.
