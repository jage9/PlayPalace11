# 1-4-24 (Midnight) game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-midnight = 1-4-24
midnight-category = Permainan Dadu

# Actions
midnight-roll = Lempar dadu
midnight-keep-die = Simpan { $value }
midnight-bank = Simpan

# Game events
midnight-turn-start = Giliran { $player }.
midnight-you-rolled = Anda melempar: { $dice }.
midnight-player-rolled = { $player } melempar: { $dice }.

# Keeping dice
midnight-you-keep = Anda menyimpan { $die }.
midnight-player-keeps = { $player } menyimpan { $die }.
midnight-you-unkeep = Anda tidak menyimpan { $die }.
midnight-player-unkeeps = { $player } tidak menyimpan { $die }.

# Turn status
midnight-you-have-kept = Dadu yang disimpan: { $kept }. Lemparan tersisa: { $remaining }.
midnight-player-has-kept = { $player } telah menyimpan: { $kept }. { $remaining } dadu tersisa.

# Scoring
midnight-you-scored = Anda mencetak { $score } poin.
midnight-scored = { $player } mencetak { $score } poin.
midnight-you-disqualified = Anda tidak memiliki 1 dan 4. Diskualifikasi!
midnight-player-disqualified = { $player } tidak memiliki 1 dan 4. Diskualifikasi!

# Round results
midnight-round-winner = { $player } memenangkan ronde!
midnight-round-tie = Ronde seri antara { $players }.
midnight-all-disqualified = Semua pemain diskualifikasi! Tidak ada pemenang ronde ini.

# Game winner
midnight-game-winner = { $player } memenangkan permainan dengan { $wins } kemenangan ronde!
midnight-game-tie = Seri! { $players } masing-masing memenangkan { $wins } ronde.

# Options
midnight-set-rounds = Ronde untuk dimainkan: { $rounds }
midnight-enter-rounds = Masukkan jumlah ronde untuk dimainkan:
midnight-option-changed-rounds = Ronde untuk dimainkan diubah menjadi { $rounds }

# Disabled reasons
midnight-need-to-roll = Anda harus melempar dadu terlebih dahulu.
midnight-no-dice-to-keep = Tidak ada dadu yang tersedia untuk disimpan.
midnight-must-keep-one = Anda harus menyimpan setidaknya satu dadu per lemparan.
midnight-must-roll-first = Anda harus melempar dadu terlebih dahulu.
midnight-keep-all-first = Anda harus menyimpan semua dadu sebelum menyimpan.
