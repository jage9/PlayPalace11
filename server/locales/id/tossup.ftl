# Toss Up game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-tossup = Toss Up
tossup-category = Permainan Dadu

# Actions
tossup-roll-first = Lempar { $count } dadu
tossup-roll-remaining = Lempar { $count } dadu tersisa
tossup-bank = Simpan { $points } poin

# Game events
tossup-turn-start = Giliran { $player }. Skor: { $score }
tossup-you-roll = Anda melempar: { $results }.
tossup-player-rolls = { $player } melempar: { $results }.

# Turn status
tossup-you-have-points = Poin giliran: { $turn_points }. Dadu tersisa: { $dice_count }.
tossup-player-has-points = { $player } memiliki { $turn_points } poin giliran. { $dice_count } dadu tersisa.

# Fresh dice
tossup-you-get-fresh = Tidak ada dadu tersisa! Mendapat { $count } dadu baru.
tossup-player-gets-fresh = { $player } mendapat { $count } dadu baru.

# Bust
tossup-you-bust = Bust! Anda kehilangan { $points } poin untuk giliran ini.
tossup-player-busts = { $player } bust dan kehilangan { $points } poin!

# Bank
tossup-you-bank = Anda menyimpan { $points } poin. Total skor: { $total }.
tossup-player-banks = { $player } menyimpan { $points } poin. Total skor: { $total }.

# Winner
tossup-winner = { $player } menang dengan { $score } poin!
tossup-tie-tiebreaker = Seri antara { $players }! Ronde tiebreaker!

# Options
tossup-set-rules-variant = Varian aturan: { $variant }
tossup-select-rules-variant = Pilih varian aturan:
tossup-option-changed-rules = Varian aturan diubah menjadi { $variant }

tossup-set-starting-dice = Dadu awal: { $count }
tossup-enter-starting-dice = Masukkan jumlah dadu awal:
tossup-option-changed-dice = Dadu awal diubah menjadi { $count }

# Rules variants
tossup-rules-standard = Standard
tossup-rules-playpalace = PlayPalace

# Rules explanations
tossup-rules-standard-desc = 3 hijau, 2 kuning, 1 merah per dadu. Bust jika tidak ada hijau dan setidaknya satu merah.
tossup-rules-playpalace-desc = Distribusi sama. Bust jika semua dadu merah.

# Disabled reasons
tossup-need-points = Anda butuh poin untuk menyimpan.
