# Yahtzee oyun mesajları

# Oyun bilgisi
game-name-yahtzee = Yahtzee

# Eylemler - Zar atma
yahtzee-roll = Tekrar at ({ $count } kaldı)
yahtzee-roll-all = Zarları at

# Üst bölüm skorlama kategorileri
yahtzee-score-ones = { $points } puan için Birler
yahtzee-score-twos = { $points } puan için İkiler
yahtzee-score-threes = { $points } puan için Üçler
yahtzee-score-fours = { $points } puan için Dörtler
yahtzee-score-fives = { $points } puan için Beşler
yahtzee-score-sixes = { $points } puan için Altılar

# Alt bölüm skorlama kategorileri
yahtzee-score-three-kind = { $points } puan için Üçlü
yahtzee-score-four-kind = { $points } puan için Dörtlü
yahtzee-score-full-house = { $points } puan için Full House
yahtzee-score-small-straight = { $points } puan için Küçük Sıra
yahtzee-score-large-straight = { $points } puan için Büyük Sıra
yahtzee-score-yahtzee = { $points } puan için Yahtzee
yahtzee-score-chance = { $points } puan için Şans

# Oyun olayları
yahtzee-you-rolled = Attığın: { $dice }. Kalan atış: { $remaining }
yahtzee-player-rolled = { $player } attı: { $dice }. Kalan atış: { $remaining }

# Skorlama duyuruları
yahtzee-you-scored = { $category }'de { $points } puan kazandın.
yahtzee-player-scored = { $player } { $category }'de { $points } kazandı.

# Yahtzee bonusu
yahtzee-you-bonus = Yahtzee bonusu! +100 puan
yahtzee-player-bonus = { $player } Yahtzee bonusu aldı! +100 puan

# Üst bölüm bonusu
yahtzee-you-upper-bonus = Üst bölüm bonusu! +35 puan (üst bölümde { $total })
yahtzee-player-upper-bonus = { $player } üst bölüm bonusu kazandı! +35 puan
yahtzee-you-upper-bonus-missed = Üst bölüm bonusunu kaçırdın (üst bölümde { $total }, 63 gerekiyordu).
yahtzee-player-upper-bonus-missed = { $player } üst bölüm bonusunu kaçırdı.

# Skorlama modu
yahtzee-choose-category = Skor almak için bir kategori seç.
yahtzee-continuing = Tura devam ediliyor.

# Durum kontrolleri
yahtzee-check-scoresheet = Skor kartını kontrol et
yahtzee-view-dice = Eli kontrol et
yahtzee-your-dice = Zarların: { $dice }.
yahtzee-your-dice-kept = Zarların: { $dice }. Tutulanlar: { $kept }
yahtzee-not-rolled = Henüz atmadın.

# Skor kartı gösterimi
yahtzee-scoresheet-header = === { $player }'ın Skor Kartı ===
yahtzee-scoresheet-upper = Üst Bölüm:
yahtzee-scoresheet-lower = Alt Bölüm:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = Üst Toplam: { $total } (BONUS: +35)
yahtzee-scoresheet-upper-total-needed = Üst Toplam: { $total } (bonus için { $needed } daha)
yahtzee-scoresheet-yahtzee-bonus = Yahtzee Bonusları: { $count } x 100 = { $total }
yahtzee-scoresheet-grand-total = TOPLAM SKOR: { $total }

# Kategori adları (duyurular için)
yahtzee-category-ones = Birler
yahtzee-category-twos = İkiler
yahtzee-category-threes = Üçler
yahtzee-category-fours = Dörtler
yahtzee-category-fives = Beşler
yahtzee-category-sixes = Altılar
yahtzee-category-three-kind = Üçlü
yahtzee-category-four-kind = Dörtlü
yahtzee-category-full-house = Full House
yahtzee-category-small-straight = Küçük Sıra
yahtzee-category-large-straight = Büyük Sıra
yahtzee-category-yahtzee = Yahtzee
yahtzee-category-chance = Şans

# Oyun sonu
yahtzee-winner = { $player } { $score } puan ile kazandı!
yahtzee-winners-tie = Berabere! { $players } hepsi { $score } puan kazandı!

# Seçenekler
yahtzee-set-rounds = Oyun sayısı: { $rounds }
yahtzee-enter-rounds = Oyun sayısını girin (1-10):
yahtzee-option-changed-rounds = Oyun sayısı { $rounds } olarak ayarlandı.

# Devre dışı eylem nedenleri
yahtzee-no-rolls-left = Atış hakkın kalmadı.
yahtzee-roll-first = Önce atmalısın.
yahtzee-category-filled = Bu kategori zaten dolu.
