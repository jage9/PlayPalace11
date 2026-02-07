# Ninety Nine - Türkçe Yerelleştirme
# Mesajlar v10 ile tam eşleşiyor

# Oyun bilgisi
ninetynine-name = Ninety Nine
ninetynine-description = Oyuncuların devam eden toplamı 99'un üzerine çıkarmaktan kaçınmaya çalıştığı bir kart oyunu. Ayakta kalan son oyuncu kazanır!

# Raund
ninetynine-round = Raund { $round }.

# Tur
ninetynine-player-turn = { $player }'ın turu.

# Kart oynama - v10 ile tam eşleşiyor
ninetynine-you-play = { $card } oynuyorsun. Sayaç şimdi { $count }.
ninetynine-player-plays = { $player } { $card } oynuyor. Sayaç şimdi { $count }.

# Yön tersine çevirme
ninetynine-direction-reverses = Oyun yönü tersine çevriliyor!

# Atlama
ninetynine-player-skipped = { $player } atlanıyor.

# Jeton kaybı - v10 ile tam eşleşiyor
ninetynine-you-lose-tokens = { $amount } { $amount ->
    [one] jeton
    *[other] jeton
} kaybediyorsun.
ninetynine-player-loses-tokens = { $player } { $amount } { $amount ->
    [one] jeton
    *[other] jeton
} kaybediyor.

# Eleme
ninetynine-player-eliminated = { $player } elendi!

# Oyun sonu
ninetynine-player-wins = { $player } oyunu kazandı!

# Dağıtım
ninetynine-you-deal = Kartları dağıtıyorsun.
ninetynine-player-deals = { $player } kartları dağıtıyor.

# Kart çekme
ninetynine-you-draw = { $card } çekiyorsun.
ninetynine-player-draws = { $player } bir kart çekiyor.

# Geçerli kart yok
ninetynine-no-valid-cards = { $player }'ın 99'u aşmayacak kartı yok!

# Durum - C tuşu için
ninetynine-current-count = Sayaç { $count }.

# El kontrolü - H tuşu için
ninetynine-hand-cards = Kartların: { $cards }.
ninetynine-hand-empty = Kartın yok.

# As seçimi
ninetynine-ace-choice = As'ı +1 veya +11 olarak oyna?
ninetynine-ace-add-eleven = 11 ekle
ninetynine-ace-add-one = 1 ekle

# On seçimi
ninetynine-ten-choice = 10'u +10 veya -10 olarak oyna?
ninetynine-ten-add = 10 ekle
ninetynine-ten-subtract = 10 çıkar

# Manuel çekme
ninetynine-draw-card = Kart çek
ninetynine-draw-prompt = Kart çekmek için Boşluk veya D'ye basın.

# Seçenekler
ninetynine-set-tokens = Başlangıç jetonları: { $tokens }
ninetynine-enter-tokens = Başlangıç jeton sayısını girin:
ninetynine-option-changed-tokens = Başlangıç jetonları { $tokens } olarak ayarlandı.
ninetynine-set-rules = Kural varyantı: { $rules }
ninetynine-select-rules = Kural varyantını seç
ninetynine-option-changed-rules = Kural varyantı { $rules } olarak ayarlandı.
ninetynine-set-hand-size = El boyutu: { $size }
ninetynine-enter-hand-size = El boyutunu girin:
ninetynine-option-changed-hand-size = El boyutu { $size } olarak ayarlandı.
ninetynine-set-autodraw = Otomatik çekme: { $enabled }
ninetynine-option-changed-autodraw = Otomatik çekme { $enabled } olarak ayarlandı.

# Kural varyantı duyuruları (oyun başlangıcında gösterilen)
ninetynine-rules-quentin = Quentin C kuralları.
ninetynine-rules-rsgames = RS Games kuralları.

# Kural varyantı seçenekleri (menü gösterimi için)
ninetynine-rules-variant-quentin_c = Quentin C
ninetynine-rules-variant-rs_games = RS Games

# Devre dışı eylem nedenleri
ninetynine-choose-first = Önce bir seçim yapmalısın.
ninetynine-draw-first = Önce bir kart çekmelisin.
