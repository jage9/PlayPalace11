# Pirates of the Lost Seas oyun mesajları
# Not: Raund başlangıcı, tur başlangıcı gibi ortak mesajlar games.ftl'de

# Oyun adı
game-name-pirates = Pirates of the Lost Seas

# Oyun başlangıcı ve kurulumu
pirates-welcome = Pirates of the Lost Seas'a hoş geldiniz! Denizlerde yolculuk edin, mücevher toplayın ve diğer korsanlarla savaşın!
pirates-oceans = Yolculuğunuz sizi buralardan geçirecek: { $oceans }
pirates-gems-placed = { $total } mücevher denizlere saçıldı. Hepsini bulun!
pirates-golden-moon = Altın Ay yükseliyor! Tüm XP kazançları bu raundda üç katına çıktı!

# Tur duyuruları
pirates-turn = { $player }'ın turu. Pozisyon { $position }

# Hareket eylemleri
pirates-move-left = Sola yelken aç
pirates-move-right = Sağa yelken aç
pirates-move-2-left = 2 kare sola yelken aç
pirates-move-2-right = 2 kare sağa yelken aç
pirates-move-3-left = 3 kare sola yelken aç
pirates-move-3-right = 3 kare sağa yelken aç

# Hareket mesajları
pirates-move-you = { $direction } { $position } pozisyonuna yelken açıyorsun.
pirates-move-you-tiles = { $tiles } kare { $direction } { $position } pozisyonuna yelken açıyorsun.
pirates-move = { $player } { $direction } { $position } pozisyonuna yelken açıyor.
pirates-map-edge = Daha fazla yelken açamazsın. { $position } pozisyonundasın.

# Pozisyon ve durum
pirates-check-status = Durumu kontrol et
pirates-check-position = Pozisyonu kontrol et
pirates-check-moon = Ay parlaklığını kontrol et
pirates-your-position = Pozisyonun: { $ocean }'da { $position }
pirates-moon-brightness = Altın Ay %{ $brightness } parlak. ({ $total } mücevherin { $collected }'i toplandı).
pirates-no-golden-moon = Altın Ay şu anda gökyüzünde görülemiyor.

# Mücevher toplama
pirates-gem-found-you = Bir { $gem } buldun! { $value } puan değerinde.
pirates-gem-found = { $player } bir { $gem } buldu! { $value } puan değerinde.
pirates-all-gems-collected = Tüm mücevherler toplandı!

# Kazanan
pirates-winner = { $player } { $score } puan ile kazandı!

# Yetenekler menüsü
pirates-use-skill = Yetenek kullan
pirates-select-skill = Kullanmak için bir yetenek seç

# Savaş - Saldırı başlatma
pirates-cannonball = Top ateşle
pirates-no-targets = { $range } kare içinde hedef yok.
pirates-attack-you-fire = { $target }'a top ateşliyorsun!
pirates-attack-incoming = { $attacker } sana top ateşliyor!
pirates-attack-fired = { $attacker } { $defender }'a top ateşliyor!

# Savaş - Atışlar
pirates-attack-roll = Saldırı atışı: { $roll }
pirates-attack-bonus = Saldırı bonusu: +{ $bonus }
pirates-defense-roll = Savunma atışı: { $roll }
pirates-defense-roll-others = { $player } savunma için { $roll } atıyor.
pirates-defense-bonus = Savunma bonusu: +{ $bonus }

# Savaş - İsabet sonuçları
pirates-attack-hit-you = Tam isabet! { $target }'ı vurdun!
pirates-attack-hit-them = { $attacker } tarafından vuruldun!
pirates-attack-hit = { $attacker } { $defender }'ı vuruyor!

# Savaş - Kaçırma sonuçları
pirates-attack-miss-you = Topun { $target }'ı ıskaladı.
pirates-attack-miss-them = Top seni ıskaladı!
pirates-attack-miss = { $attacker }'ın topu { $defender }'ı ıskalıyor.

# Savaş - İtme
pirates-push-you = { $target }'ı { $direction } { $position } pozisyonuna itiyorsun!
pirates-push-them = { $attacker } seni { $direction } { $position } pozisyonuna itiyor!
pirates-push = { $attacker } { $defender }'ı { $direction } { $old_pos }'den { $new_pos }'e itiyor.

# Savaş - Mücevher çalma
pirates-steal-attempt = { $attacker } mücevher çalmaya çalışıyor!
pirates-steal-rolls = Çalma atışı: { $steal } savunmaya karşı: { $defend }
pirates-steal-success-you = { $target }'dan bir { $gem } çaldın!
pirates-steal-success-them = { $attacker } { $gem }'ini çaldı!
pirates-steal-success = { $attacker } { $defender }'dan bir { $gem } çalıyor!
pirates-steal-failed = Çalma denemesi başarısız oldu!

# XP ve Seviye Atlama
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player } seviye { $level }'e ulaştı!
pirates-level-up-you = Seviye { $level }'e ulaştın!
pirates-level-up-multiple = { $player } { $levels } seviye atladı! Artık seviye { $level }!
pirates-level-up-multiple-you = { $levels } seviye atladın! Artık seviye { $level }!
pirates-skills-unlocked = { $player } yeni yetenekler açtı: { $skills }.
pirates-skills-unlocked-you = Yeni yetenekler açtın: { $skills }.

# Yetenek aktivasyonu
pirates-skill-activated = { $player } { $skill }'i etkinleştiriyor!
pirates-buff-expired = { $player }'ın { $skill } güçlendirmesi sona erdi.

# Kılıç Dövüşçüsü yeteneği
pirates-sword-fighter-activated = Kılıç Dövüşçüsü etkinleştirildi! { $turns } tur boyunca +4 saldırı bonusu.

# İtme yeteneği (savunma güçlendirmesi)
pirates-push-activated = İtme etkinleştirildi! { $turns } tur boyunca +3 savunma bonusu.

# Yetenekli Kaptan yeteneği
pirates-skilled-captain-activated = Yetenekli Kaptan etkinleştirildi! { $turns } tur boyunca +2 saldırı ve +2 savunma.

# Çifte Yıkım yeteneği
pirates-double-devastation-activated = Çifte Yıkım etkinleştirildi! { $turns } tur boyunca saldırı menzili 10 kareye çıktı.

# Savaş Gemisi yeteneği
pirates-battleship-activated = Savaş Gemisi etkinleştirildi! Bu turda iki atış yapabilirsin!
pirates-battleship-no-targets = { $shot } numaralı atış için hedef yok.
pirates-battleship-shot = { $shot } numaralı atış ateşleniyor...

# Portal yeteneği
pirates-portal-no-ships = Portal açmak için görünürde başka gemi yok.
pirates-portal-fizzle = { $player }'ın portalı hedef olmadan söndü.
pirates-portal-success = { $player } { $ocean }'da { $position } pozisyonuna portal açıyor!

# Mücevher Arayıcısı yeteneği
pirates-gem-seeker-reveal = Denizler { $position } pozisyonunda bir { $gem } fısıldıyor. ({ $uses } kullanım kaldı)

# Seviye gereksinimleri
pirates-requires-level-15 = Seviye 15 gerektirir
pirates-requires-level-150 = Seviye 150 gerektirir

# XP Çarpanı seçenekleri
pirates-set-combat-xp-multiplier = savaş xp çarpanı: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = savaş için deneyim
pirates-set-find-gem-xp-multiplier = mücevher bulma xp çarpanı: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = mücevher bulmak için deneyim

# Mücevher çalma seçenekleri
pirates-set-gem-stealing = Mücevher çalma: { $mode }
pirates-select-gem-stealing = Mücevher çalma modunu seç
pirates-option-changed-stealing = Mücevher çalma { $mode } olarak ayarlandı.

# Mücevher çalma modu seçenekleri
pirates-stealing-with-bonus = Atış bonusuyla
pirates-stealing-no-bonus = Atış bonusu yok
pirates-stealing-disabled = Devre dışı
