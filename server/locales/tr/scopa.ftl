# Scopa oyun mesajları
# Not: Raund başlangıcı, tur başlangıcı, hedef skor, takım modu gibi ortak mesajlar games.ftl'de

# Oyun adı
game-name-scopa = Scopa

# Oyun olayları
scopa-initial-table = Masa kartları: { $cards }
scopa-no-initial-table = Başlangıçta masada kart yok.
scopa-you-collect = { $card } ile { $cards } topluyorsun
scopa-player-collects = { $player } { $card } ile { $cards } topluyor
scopa-you-put-down = { $card } koyuyorsun.
scopa-player-puts-down = { $player } { $card } koyuyor.
scopa-scopa-suffix =  - SCOPA!
scopa-clear-table-suffix = , masayı temizliyor.
scopa-remaining-cards = { $player } kalan masa kartlarını alıyor.
scopa-scoring-round = Skorlama raund...
scopa-most-cards = { $player } en çok kart için 1 puan kazanıyor ({ $count } kart).
scopa-most-cards-tie = En çok kart berabere - puan verilmedi.
scopa-most-diamonds = { $player } en çok karo için 1 puan kazanıyor ({ $count } karo).
scopa-most-diamonds-tie = En çok karo berabere - puan verilmedi.
scopa-seven-diamonds = { $player } karo 7 için 1 puan kazanıyor.
scopa-seven-diamonds-multi = { $player } en çok karo 7 için 1 puan kazanıyor ({ $count } × karo 7).
scopa-seven-diamonds-tie = Karo 7 berabere - puan verilmedi.
scopa-most-sevens = { $player } en çok 7 için 1 puan kazanıyor ({ $count } yedi).
scopa-most-sevens-tie = En çok 7 berabere - puan verilmedi.
scopa-round-scores = Raund skorları:
scopa-round-score-line = { $player }: +{ $round_score } (toplam: { $total_score })
scopa-table-empty = Masada kart yok.
scopa-no-such-card = O pozisyonda kart yok.
scopa-captured-count = { $count } kart topladın

# Görüntüleme eylemleri
scopa-view-table = Masayı görüntüle
scopa-view-captured = Toplananları görüntüle

# Scopa'ya özel seçenekler
scopa-enter-target-score = Hedef skoru girin (1-121)
scopa-set-cards-per-deal = Dağıtım başına kart: { $cards }
scopa-enter-cards-per-deal = Dağıtım başına kart girin (1-10)
scopa-set-decks = Deste sayısı: { $decks }
scopa-enter-decks = Deste sayısını girin (1-6)
scopa-toggle-escoba = Escoba (15'e topla): { $enabled }
scopa-toggle-hints = Toplama ipuçlarını göster: { $enabled }
scopa-set-mechanic = Scopa mekaniği: { $mechanic }
scopa-select-mechanic = Scopa mekaniğini seç
scopa-toggle-instant-win = Scopa ile anında kazanma: { $enabled }
scopa-toggle-team-scoring = Takım kartlarını skorlama için birleştir: { $enabled }
scopa-toggle-inverse = Ters mod (hedefe ulaşma = eleme): { $enabled }

# Seçenek değişikliği duyuruları
scopa-option-changed-cards = Dağıtım başına kart { $cards } olarak ayarlandı.
scopa-option-changed-decks = Deste sayısı { $decks } olarak ayarlandı.
scopa-option-changed-escoba = Escoba { $enabled }.
scopa-option-changed-hints = Toplama ipuçları { $enabled }.
scopa-option-changed-mechanic = Scopa mekaniği { $mechanic } olarak ayarlandı.
scopa-option-changed-instant = Scopa ile anında kazanma { $enabled }.
scopa-option-changed-team-scoring = Takım kartı skorlaması { $enabled }.
scopa-option-changed-inverse = Ters mod { $enabled }.

# Scopa mekaniği seçenekleri
scopa-mechanic-normal = Normal
scopa-mechanic-no_scopas = Scopa Yok
scopa-mechanic-only_scopas = Sadece Scopalar

# Devre dışı eylem nedenleri
scopa-timer-not-active = Raund zamanlayıcısı aktif değil.

# Doğrulama hataları
scopa-error-not-enough-cards = { $decks } { $decks ->
    [one] destede
    *[other] destede
} { $players } { $players ->
    [one] oyuncu
    *[other] oyuncu
} için her birinin { $cards_per_deal } kartıyla yeterli kart yok. ({ $cards_per_deal } × { $players } = { $cards_needed } kart gerekli, ama sadece { $total_cards } var.)
