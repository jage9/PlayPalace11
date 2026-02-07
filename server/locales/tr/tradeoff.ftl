# Tradeoff oyun mesajları

# Oyun bilgisi
game-name-tradeoff = Tradeoff

# Raund ve iterasyon akışı
tradeoff-round-start = Raund { $round }.
tradeoff-iteration = 3'ten { $iteration } numaralı el.

# Faz 1: Takas
tradeoff-you-rolled = Attığın: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = takas ediliyor
tradeoff-trade-status-keeping = tutulacak
tradeoff-confirm-trades = Takasları onayla ({ $count } zar)
tradeoff-keeping = { $value } tutulacak.
tradeoff-trading = { $value } takas edilecek.
tradeoff-player-traded = { $player } takas etti: { $dice }.
tradeoff-player-traded-none = { $player } tüm zarları tuttu.

# Faz 2: Havuzdan alma
tradeoff-your-turn-take = Havuzdan bir zar alma sırası sende.
tradeoff-take-die = { $value } al ({ $remaining } kaldı)
tradeoff-you-take = { $value } alıyorsun.
tradeoff-player-takes = { $player } { $value } alıyor.

# Faz 3: Skorlama
tradeoff-player-scored = { $player } ({ $points } puan): { $sets }.
tradeoff-no-sets = { $player }: set yok.

# Set açıklamaları (özet)
tradeoff-set-triple = { $value } üçlüsü
tradeoff-set-group = { $value } grubu
tradeoff-set-mini-straight = mini sıra { $low }-{ $high }
tradeoff-set-double-triple = çift üçlü ({ $v1 } ve { $v2 })
tradeoff-set-straight = sıra { $low }-{ $high }
tradeoff-set-double-group = çift grup ({ $v1 } ve { $v2 })
tradeoff-set-all-groups = tüm gruplar
tradeoff-set-all-triplets = tüm üçlüler

# Raund sonu
tradeoff-round-scores = Raund { $round } skorları:
tradeoff-score-line = { $player }: +{ $round_points } (toplam: { $total })
tradeoff-leader = { $player } { $score } ile önde.

# Oyun sonu
tradeoff-winner = { $player } { $score } puan ile kazandı!
tradeoff-winners-tie = Berabere! { $players } { $score } puan ile berabere kaldı!

# Durum kontrolleri
tradeoff-view-hand = Elini görüntüle
tradeoff-view-pool = Havuzu görüntüle
tradeoff-view-players = Oyuncuları görüntüle
tradeoff-hand-display = Elin ({ $count } zar): { $dice }
tradeoff-pool-display = Havuz ({ $count } zar): { $dice }
tradeoff-player-info = { $player }: { $hand }. Takas edilen: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. Hiçbir şey takas etmedi.

# Hata mesajları
tradeoff-not-trading-phase = Takas aşamasında değil.
tradeoff-not-taking-phase = Alma aşamasında değil.
tradeoff-already-confirmed = Zaten onaylandı.
tradeoff-no-die = Değiştirilecek zar yok.
tradeoff-no-more-takes = Daha fazla alma yok.
tradeoff-not-in-pool = Bu zar havuzda değil.

# Seçenekler
tradeoff-set-target = Hedef skor: { $score }
tradeoff-enter-target = Hedef skoru girin:
tradeoff-option-changed-target = Hedef skor { $score } olarak ayarlandı.
