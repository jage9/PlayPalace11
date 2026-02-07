# Yahtzee game messages

# Game info
game-name-yahtzee = Yahtzee

# Actions - Rolling
yahtzee-roll = Lempar ulang ({ $count } tersisa)
yahtzee-roll-all = Lempar dadu

# Upper section scoring categories
yahtzee-score-ones = Satu untuk { $points } poin
yahtzee-score-twos = Dua untuk { $points } poin
yahtzee-score-threes = Tiga untuk { $points } poin
yahtzee-score-fours = Empat untuk { $points } poin
yahtzee-score-fives = Lima untuk { $points } poin
yahtzee-score-sixes = Enam untuk { $points } poin

# Lower section scoring categories
yahtzee-score-three-kind = Three of a Kind untuk { $points } poin
yahtzee-score-four-kind = Four of a Kind untuk { $points } poin
yahtzee-score-full-house = Full House untuk { $points } poin
yahtzee-score-small-straight = Small Straight untuk { $points } poin
yahtzee-score-large-straight = Large Straight untuk { $points } poin
yahtzee-score-yahtzee = Yahtzee untuk { $points } poin
yahtzee-score-chance = Chance untuk { $points } poin

# Game events
yahtzee-you-rolled = Anda melempar: { $dice }. Lemparan tersisa: { $remaining }
yahtzee-player-rolled = { $player } melempar: { $dice }. Lemparan tersisa: { $remaining }

# Scoring announcements
yahtzee-you-scored = Anda mencetak { $points } poin di { $category }.
yahtzee-player-scored = { $player } mencetak { $points } di { $category }.

# Yahtzee bonus
yahtzee-you-bonus = Bonus Yahtzee! +100 poin
yahtzee-player-bonus = { $player } mendapat bonus Yahtzee! +100 poin

# Upper section bonus
yahtzee-you-upper-bonus = Bonus bagian atas! +35 poin ({ $total } di bagian atas)
yahtzee-player-upper-bonus = { $player } mendapat bonus bagian atas! +35 poin
yahtzee-you-upper-bonus-missed = Anda melewatkan bonus bagian atas ({ $total } di bagian atas, butuh 63).
yahtzee-player-upper-bonus-missed = { $player } melewatkan bonus bagian atas.

# Scoring mode
yahtzee-choose-category = Pilih kategori untuk mencetak.
yahtzee-continuing = Melanjutkan giliran.

# Status checks
yahtzee-check-scoresheet = Periksa kartu skor
yahtzee-view-dice = Periksa tangan
yahtzee-your-dice = Dadu Anda: { $dice }.
yahtzee-your-dice-kept = Dadu Anda: { $dice }. Menyimpan: { $kept }
yahtzee-not-rolled = Anda belum melempar.

# Scoresheet display
yahtzee-scoresheet-header = === Kartu Skor { $player } ===
yahtzee-scoresheet-upper = Bagian Atas:
yahtzee-scoresheet-lower = Bagian Bawah:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = Total Atas: { $total } (BONUS: +35)
yahtzee-scoresheet-upper-total-needed = Total Atas: { $total } ({ $needed } lagi untuk bonus)
yahtzee-scoresheet-yahtzee-bonus = Bonus Yahtzee: { $count } x 100 = { $total }
yahtzee-scoresheet-grand-total = TOTAL SKOR: { $total }

# Category names (for announcements)
yahtzee-category-ones = Satu
yahtzee-category-twos = Dua
yahtzee-category-threes = Tiga
yahtzee-category-fours = Empat
yahtzee-category-fives = Lima
yahtzee-category-sixes = Enam
yahtzee-category-three-kind = Three of a Kind
yahtzee-category-four-kind = Four of a Kind
yahtzee-category-full-house = Full House
yahtzee-category-small-straight = Small Straight
yahtzee-category-large-straight = Large Straight
yahtzee-category-yahtzee = Yahtzee
yahtzee-category-chance = Chance

# Game end
yahtzee-winner = { $player } menang dengan { $score } poin!
yahtzee-winners-tie = Seri! { $players } semua mencetak { $score } poin!

# Options
yahtzee-set-rounds = Jumlah permainan: { $rounds }
yahtzee-enter-rounds = Masukkan jumlah permainan (1-10):
yahtzee-option-changed-rounds = Jumlah permainan diatur ke { $rounds }.

# Disabled action reasons
yahtzee-no-rolls-left = Anda tidak memiliki lemparan tersisa.
yahtzee-roll-first = Anda perlu melempar terlebih dahulu.
yahtzee-category-filled = Kategori itu sudah terisi.
