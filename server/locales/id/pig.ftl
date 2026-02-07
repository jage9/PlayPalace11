# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = Pig
pig-category = Permainan Dadu

# Actions
pig-roll = Lempar dadu
pig-bank = Simpan { $points } poin

# Game events (Pig-specific)
pig-rolls = { $player } melempar dadu...
pig-roll-result = { $roll }, untuk total { $total }
pig-bust = Oh tidak, 1! { $player } kehilangan { $points } poin.
pig-bank-action = { $player } memutuskan untuk menyimpan { $points }, untuk total { $total }
pig-winner = Kita punya pemenang, dan itu adalah { $player }!

# Pig-specific options
pig-set-min-bank = Penyimpanan minimal: { $points }
pig-set-dice-sides = Sisi dadu: { $sides }
pig-enter-min-bank = Masukkan poin minimal untuk menyimpan:
pig-enter-dice-sides = Masukkan jumlah sisi dadu:
pig-option-changed-min-bank = Poin penyimpanan minimal diubah menjadi { $points }
pig-option-changed-dice = Dadu sekarang memiliki { $sides } sisi

# Disabled reasons
pig-need-more-points = Anda butuh lebih banyak poin untuk menyimpan.

# Validation errors
pig-error-min-bank-too-high = Poin penyimpanan minimal harus kurang dari skor target.
