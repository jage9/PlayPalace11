# Yahtzee game messages

# Game info
game-name-yahtzee = Yahtzee

# Actions - Rolling
yahtzee-roll = Újradobás ({ $count } maradt)
yahtzee-roll-all = Dobd a kockákat

# Upper section scoring categories
yahtzee-score-ones = Egyesek { $points } pontra
yahtzee-score-twos = Kettesek { $points } pontra
yahtzee-score-threes = Hármasok { $points } pontra
yahtzee-score-fours = Négyesek { $points } pontra
yahtzee-score-fives = Ötösök { $points } pontra
yahtzee-score-sixes = Hatosok { $points } pontra

# Lower section scoring categories
yahtzee-score-three-kind = Háromfajta { $points } pontra
yahtzee-score-four-kind = Négyfajta { $points } pontra
yahtzee-score-full-house = Full { $points } pontra
yahtzee-score-small-straight = Kis sor { $points } pontra
yahtzee-score-large-straight = Nagy sor { $points } pontra
yahtzee-score-yahtzee = Yahtzee { $points } pontra
yahtzee-score-chance = Esély { $points } pontra

# Game events
yahtzee-you-rolled = Dobtál: { $dice }. Hátralévő dobások: { $remaining }
yahtzee-player-rolled = { $player } dobott: { $dice }. Hátralévő dobások: { $remaining }

# Scoring announcements
yahtzee-you-scored = { $points } pontot szereztél a { $category } kategóriában.
yahtzee-player-scored = { $player } { $points } pontot szerzett a { $category } kategóriában.

# Yahtzee bonus
yahtzee-you-bonus = Yahtzee bónusz! +100 pont
yahtzee-player-bonus = { $player } Yahtzee bónuszt kapott! +100 pont

# Upper section bonus
yahtzee-you-upper-bonus = Felső szekció bónusz! +35 pont ({ $total } a felső szekcióban)
yahtzee-player-upper-bonus = { $player } megkapta a felső szekció bónuszt! +35 pont
yahtzee-you-upper-bonus-missed = Lemaradtál a felső szekció bónuszról ({ $total } a felső szekcióban, 63 kellett).
yahtzee-player-upper-bonus-missed = { $player } lemaradt a felső szekció bónuszról.

# Scoring mode
yahtzee-choose-category = Válassz kategóriát a pontozáshoz.
yahtzee-continuing = Kör folytatása.

# Status checks
yahtzee-check-scoresheet = Ellenőrizd a pontlapot
yahtzee-view-dice = Ellenőrizd a kezed
yahtzee-your-dice = A kockáid: { $dice }.
yahtzee-your-dice-kept = A kockáid: { $dice }. Megtartva: { $kept }
yahtzee-not-rolled = Még nem dobtál.

# Scoresheet display
yahtzee-scoresheet-header = === { $player } pontlapja ===
yahtzee-scoresheet-upper = Felső szekció:
yahtzee-scoresheet-lower = Alsó szekció:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = Felső összesen: { $total } (BÓNUSZ: +35)
yahtzee-scoresheet-upper-total-needed = Felső összesen: { $total } (még { $needed } a bónuszhoz)
yahtzee-scoresheet-yahtzee-bonus = Yahtzee bónuszok: { $count } x 100 = { $total }
yahtzee-scoresheet-grand-total = TELJES PONTSZÁM: { $total }

# Category names (for announcements)
yahtzee-category-ones = Egyesek
yahtzee-category-twos = Kettesek
yahtzee-category-threes = Hármasok
yahtzee-category-fours = Négyesek
yahtzee-category-fives = Ötösök
yahtzee-category-sixes = Hatosok
yahtzee-category-three-kind = Háromfajta
yahtzee-category-four-kind = Négyfajta
yahtzee-category-full-house = Full
yahtzee-category-small-straight = Kis sor
yahtzee-category-large-straight = Nagy sor
yahtzee-category-yahtzee = Yahtzee
yahtzee-category-chance = Esély

# Game end
yahtzee-winner = { $player } nyer { $score } ponttal!
yahtzee-winners-tie = Döntetlen! { $players } mindannyian { $score } pontot szereztek!

# Options
yahtzee-set-rounds = Játékok száma: { $rounds }
yahtzee-enter-rounds = Add meg a játékok számát (1-10):
yahtzee-option-changed-rounds = Játékok száma beállítva: { $rounds }.

# Disabled action reasons
yahtzee-no-rolls-left = Nincs több dobásod.
yahtzee-roll-first = Először dobnod kell.
yahtzee-category-filled = Ez a kategória már ki van töltve.
