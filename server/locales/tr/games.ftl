# PlayPalace için paylaşılan oyun mesajları
# Bu mesajlar birden fazla oyunda ortak kullanılır

# Oyun adları
game-name-ninetynine = Ninety Nine

# Raund ve tur akışı
game-round-start = Raund { $round }.
game-round-end = Raund { $round } tamamlandı.
game-turn-start = { $player }'ın turu.
game-your-turn = Senin turun.
game-no-turn = Şu anda kimsenin turu değil.

# Skor gösterimi
game-scores-header = Güncel Skorlar:
game-score-line = { $player }: { $score } puan
game-final-scores-header = Final Skorları:

# Kazanma/kaybetme
game-winner = { $player } kazandı!
game-winner-score = { $player } { $score } puan ile kazandı!
game-tiebreaker = Berabere! Beraberlik turu!
game-tiebreaker-players = { $players } arasında berabere! Beraberlik turu!
game-eliminated = { $player } { $score } puan ile elendi.

# Ortak seçenekler
game-set-target-score = Hedef skor: { $score }
game-enter-target-score = Hedef skoru girin:
game-option-changed-target = Hedef skor { $score } olarak ayarlandı.

game-set-team-mode = Takım modu: { $mode }
game-select-team-mode = Takım modunu seç
game-option-changed-team = Takım modu { $mode } olarak ayarlandı.
game-team-mode-individual = Bireysel
game-team-mode-x-teams-of-y = { $team_size } kişilik { $num_teams } takım

# Boolean seçenek değerleri
option-on = açık
option-off = kapalı

# Durum kutusu
status-box-closed = Durum bilgisi kapatıldı.

# Oyun sonu
game-leave = Oyundan ayrıl

# Raund zamanlayıcısı
round-timer-paused = { $player } oyunu duraklattı (sonraki raunda başlamak için p'ye basın).
round-timer-resumed = Raund zamanlayıcısı devam etti.
round-timer-countdown = Sonraki raund { $seconds } içinde...

# Zar oyunları - zarları tutma/bırakma
dice-keeping = { $value } tutulyor.
dice-rerolling = { $value } tekrar atılıyor.
dice-locked = Bu zar kilitli ve değiştirilemez.

# Dağıtma (kart oyunları)
game-deal-counter = Dağıtım { $current }/{ $total }.
game-you-deal = Kartları dağıtıyorsun.
game-player-deals = { $player } kartları dağıtıyor.

# Kart adları
card-name = { $suit } { $rank }
no-cards = Kart yok

# Takım adları
suit-diamonds = karo
suit-clubs = sinek
suit-hearts = kupa
suit-spades = maça

# Değer adları
rank-ace = as
rank-ace-plural = aslar
rank-two = 2
rank-two-plural = 2'ler
rank-three = 3
rank-three-plural = 3'ler
rank-four = 4
rank-four-plural = 4'ler
rank-five = 5
rank-five-plural = 5'ler
rank-six = 6
rank-six-plural = 6'ler
rank-seven = 7
rank-seven-plural = 7'ler
rank-eight = 8
rank-eight-plural = 8'ler
rank-nine = 9
rank-nine-plural = 9'lar
rank-ten = 10
rank-ten-plural = 10'lar
rank-jack = vale
rank-jack-plural = valeler
rank-queen = kız
rank-queen-plural = kızlar
rank-king = papaz
rank-king-plural = papazlar

# Poker el açıklamaları
poker-high-card-with = { $high } yüksek, { $rest } ile
poker-high-card = { $high } yüksek
poker-pair-with = { $pair } çifti, { $rest } ile
poker-pair = { $pair } çifti
poker-two-pair-with = İki Çift, { $high } ve { $low }, { $kicker } ile
poker-two-pair = İki Çift, { $high } ve { $low }
poker-trips-with = Üçlü, { $trips }, { $rest } ile
poker-trips = Üçlü, { $trips }
poker-straight-high = { $high } yüksek Sıra
poker-flush-high-with = { $high } yüksek Renk, { $rest } ile
poker-full-house = Full House, { $trips } üzerinde { $pair }
poker-quads-with = Dörtlü, { $quads }, { $kicker } ile
poker-quads = Dörtlü, { $quads }
poker-straight-flush-high = { $high } yüksek Sıralı Renk
poker-unknown-hand = Bilinmeyen el

# Doğrulama hataları (oyunlar arası ortak)
game-error-invalid-team-mode = Seçilen takım modu mevcut oyuncu sayısı için geçerli değil.
