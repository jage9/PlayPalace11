# Farkle game messages

# Game info
game-name-farkle = Farkle

# Actions - Roll and Bank
farkle-roll = Lempar { $count } { $count ->
    [one] dadu
   *[other] dadu
}
farkle-bank = Simpan { $points } poin

# Scoring combination actions (matching v10 exactly)
farkle-take-single-one = Satu 1 untuk { $points } poin
farkle-take-single-five = Satu 5 untuk { $points } poin
farkle-take-three-kind = Tiga { $number } untuk { $points } poin
farkle-take-four-kind = Empat { $number } untuk { $points } poin
farkle-take-five-kind = Lima { $number } untuk { $points } poin
farkle-take-six-kind = Enam { $number } untuk { $points } poin
farkle-take-small-straight = Straight Kecil untuk { $points } poin
farkle-take-large-straight = Straight Besar untuk { $points } poin
farkle-take-three-pairs = Tiga pasang untuk { $points } poin
farkle-take-double-triplets = Triplet ganda untuk { $points } poin
farkle-take-full-house = Full house untuk { $points } poin

# Game events (matching v10 exactly)
farkle-rolls = { $player } melempar { $count } { $count ->
    [one] dadu
   *[other] dadu
}...
farkle-you-roll = Anda melempar { $count } { $count ->
    [one] dadu
   *[other] dadu
}...
farkle-roll-result = { $dice }
farkle-farkle = FARKLE! { $player } kehilangan { $points } poin
farkle-you-farkle = FARKLE! Anda kehilangan { $points } poin
farkle-takes-combo = { $player } mengambil { $combo } untuk { $points } poin
farkle-you-take-combo = Anda mengambil { $combo } untuk { $points } poin
farkle-hot-dice = Dadu panas!
farkle-banks = { $player } menyimpan { $points } poin untuk total { $total }
farkle-you-bank = Anda menyimpan { $points } poin untuk total { $total }
farkle-winner = { $player } menang dengan { $score } poin!
farkle-you-win = Anda menang dengan { $score } poin!
farkle-winners-tie = Kita seri! Pemenang: { $players }

# Check turn score action
farkle-turn-score = { $player } memiliki { $points } poin giliran ini.
farkle-no-turn = Tidak ada yang sedang mengambil giliran.

# Farkle-specific options
farkle-set-target-score = Skor target: { $score }
farkle-enter-target-score = Masukkan skor target (500-5000):
farkle-option-changed-target = Skor target diatur ke { $score }.

# Disabled action reasons
farkle-must-take-combo = Anda harus mengambil kombinasi skor terlebih dahulu.
farkle-cannot-bank = Anda tidak dapat menyimpan sekarang.
