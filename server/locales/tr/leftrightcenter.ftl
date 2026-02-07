# Left Right Center için mesajlar (Türkçe)

# Oyun adı
game-name-leftrightcenter = Left Right Center

# Eylemler
lrc-roll = { $count } { $count ->
    [one] zar
   *[other] zar
} at

# Zar yüzleri
lrc-face-left = Sol
lrc-face-right = Sağ
lrc-face-center = Merkez
lrc-face-dot = Nokta

# Oyun olayları
lrc-roll-results = { $player } { $results } atıyor.
lrc-pass-left = { $player } { $target }'a { $count } { $count ->
    [one] jeton
   *[other] jeton
} veriyor.
lrc-pass-right = { $player } { $target }'a { $count } { $count ->
    [one] jeton
   *[other] jeton
} veriyor.
lrc-pass-center = { $player } merkeze { $count } { $count ->
    [one] jeton
   *[other] jeton
} koyuyor.
lrc-no-chips = { $player }'ın atmak için jetonu yok.
lrc-center-pot = Merkezde { $count } { $count ->
    [one] jeton
   *[other] jeton
}.
lrc-player-chips = { $player } şimdi { $count } { $count ->
    [one] jetona
   *[other] jetona
} sahip.
lrc-winner = { $player } { $count } { $count ->
    [one] jeton
   *[other] jeton
} ile kazandı!

# Seçenekler
lrc-set-starting-chips = Başlangıç jetonları: { $count }
lrc-enter-starting-chips = Başlangıç jetonlarını girin:
lrc-option-changed-starting-chips = Başlangıç jetonları { $count } olarak ayarlandı.
