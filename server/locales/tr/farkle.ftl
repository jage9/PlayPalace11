# Farkle oyun mesajları

# Oyun bilgisi
game-name-farkle = Farkle

# Eylemler - Atma ve Bankaya Yatırma
farkle-roll = { $count } { $count ->
    [one] zar
   *[other] zar
} at
farkle-bank = { $points } puan bankaya yatır

# Skor kombinasyonu eylemleri (v10 ile tam eşleşiyor)
farkle-take-single-one = { $points } puan için tek 1
farkle-take-single-five = { $points } puan için tek 5
farkle-take-three-kind = { $points } puan için üç { $number }
farkle-take-four-kind = { $points } puan için dört { $number }
farkle-take-five-kind = { $points } puan için beş { $number }
farkle-take-six-kind = { $points } puan için altı { $number }
farkle-take-small-straight = { $points } puan için Küçük Sıra
farkle-take-large-straight = { $points } puan için Büyük Sıra
farkle-take-three-pairs = { $points } puan için üç çift
farkle-take-double-triplets = { $points } puan için çift üçlü
farkle-take-full-house = { $points } puan için full

# Oyun olayları (v10 ile tam eşleşiyor)
farkle-rolls = { $player } { $count } { $count ->
    [one] zar
   *[other] zar
} atıyor...
farkle-you-roll = { $count } { $count ->
    [one] zar
   *[other] zar
} atıyorsun...
farkle-roll-result = { $dice }
farkle-farkle = FARKLE! { $player } { $points } puan kaybediyor
farkle-you-farkle = FARKLE! { $points } puan kaybediyorsun
farkle-takes-combo = { $player } { $points } puan için { $combo } alıyor
farkle-you-take-combo = { $points } puan için { $combo } alıyorsun
farkle-hot-dice = Sıcak zar!
farkle-banks = { $player } { $points } puan bankaya yatırıyor toplam { $total }
farkle-you-bank = { $points } puan bankaya yatırıyorsun toplam { $total }
farkle-winner = { $player } { $score } puan ile kazandı!
farkle-you-win = { $score } puan ile kazandın!
farkle-winners-tie = Berabere! Kazananlar: { $players }

# Tur skoru kontrolü eylemi
farkle-turn-score = { $player } bu turda { $points } puan var.
farkle-no-turn = Şu anda kimse tur atmıyor.

# Farkle'a özel seçenekler
farkle-set-target-score = Hedef skor: { $score }
farkle-enter-target-score = Hedef skoru girin (500-5000):
farkle-option-changed-target = Hedef skor { $score } olarak ayarlandı.

# Devre dışı eylem nedenleri
farkle-must-take-combo = Önce bir skor kombinasyonu almalısın.
farkle-cannot-bank = Şu anda bankaya yatıramazsın.
