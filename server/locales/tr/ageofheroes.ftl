# Age of Heroes oyun mesajları
# 2-6 oyuncu için bir medeniyet kurma kart oyunu

# Oyun adı
game-name-ageofheroes = Age of Heroes

# Kabileler
ageofheroes-tribe-egyptians = Mısırlılar
ageofheroes-tribe-romans = Romalılar
ageofheroes-tribe-greeks = Yunanlılar
ageofheroes-tribe-babylonians = Babilliler
ageofheroes-tribe-celts = Keltler
ageofheroes-tribe-chinese = Çinliler

# Özel Kaynaklar (anıtlar için)
ageofheroes-special-limestone = Kireçtaşı
ageofheroes-special-concrete = Beton
ageofheroes-special-marble = Mermer
ageofheroes-special-bricks = Tuğla
ageofheroes-special-sandstone = Kumtaşı
ageofheroes-special-granite = Granit

# Standart Kaynaklar
ageofheroes-resource-iron = Demir
ageofheroes-resource-wood = Odun
ageofheroes-resource-grain = Tahıl
ageofheroes-resource-stone = Taş
ageofheroes-resource-gold = Altın

# Olaylar
ageofheroes-event-population-growth = Nüfus Artışı
ageofheroes-event-earthquake = Deprem
ageofheroes-event-eruption = Patlama
ageofheroes-event-hunger = Açlık
ageofheroes-event-barbarians = Barbarlar
ageofheroes-event-olympics = Olimpiyat Oyunları
ageofheroes-event-hero = Kahraman
ageofheroes-event-fortune = Şans

# Binalar
ageofheroes-building-army = Ordu
ageofheroes-building-fortress = Kale
ageofheroes-building-general = General
ageofheroes-building-road = Yol
ageofheroes-building-city = Şehir

# Eylemler
ageofheroes-action-tax-collection = Vergi Toplama
ageofheroes-action-construction = İnşaat
ageofheroes-action-war = Savaş
ageofheroes-action-do-nothing = Hiçbir Şey Yapma
ageofheroes-play = Oyna

# Savaş hedefleri
ageofheroes-war-conquest = Fetih
ageofheroes-war-plunder = Yağma
ageofheroes-war-destruction = Yıkım

# Oyun seçenekleri
ageofheroes-set-victory-cities = Zafer şehirleri: { $cities }
ageofheroes-enter-victory-cities = Kazanmak için şehir sayısını girin (3-7)
ageofheroes-set-victory-monument = Anıt tamamlama: { $progress }%
ageofheroes-toggle-neighbor-roads = Sadece komşulara yol: { $enabled }
ageofheroes-set-max-hand = Maksimum el boyutu: { $cards } kart

# Seçenek değişikliği duyuruları
ageofheroes-option-changed-victory-cities = Zafer için { $cities } şehir gerekli.
ageofheroes-option-changed-victory-monument = Anıt tamamlama eşiği { $progress }% olarak ayarlandı.
ageofheroes-option-changed-neighbor-roads = Sadece komşulara yol { $enabled }.
ageofheroes-option-changed-max-hand = Maksimum el boyutu { $cards } kart olarak ayarlandı.

# Kurulum aşaması
ageofheroes-setup-start = Sen { $tribe } kabilesinin lidersin. Özel anıt kaynağın { $special }. Tur sırasını belirlemek için zarları at.
ageofheroes-setup-viewer = Oyuncular tur sırasını belirlemek için zar atıyor.
ageofheroes-roll-dice = Zarları at
ageofheroes-war-roll-dice = Zarları at
ageofheroes-dice-result = { $total } attın ({ $die1 } + { $die2 }).
ageofheroes-dice-result-other = { $player } { $total } attı.
ageofheroes-dice-tie = Birden fazla oyuncu { $total } ile berabere kaldı. Tekrar atılıyor...
ageofheroes-first-player = { $player } { $total } ile en yüksek attı ve ilk başlıyor.
ageofheroes-first-player-you = { $total } puan ile ilk sen başlıyorsun.

# Hazırlık aşaması
ageofheroes-prepare-start = Oyuncular olay kartlarını oynamalı ve felaketleri atmalı.
ageofheroes-prepare-your-turn = Oynamak veya atmak için { $count } { $count ->
    [one] kartın
    *[other] kartın
} var.
ageofheroes-prepare-done = Hazırlık aşaması tamamlandı.

# Oynanan/atılan olaylar
ageofheroes-population-growth = { $player } Nüfus Artışı oynar ve yeni bir şehir kurar.
ageofheroes-population-growth-you = Nüfus Artışı oynuyorsun ve yeni bir şehir kuruyorsun.
ageofheroes-discard-card = { $player } { $card } atıyor.
ageofheroes-discard-card-you = { $card } atıyorsun.
ageofheroes-earthquake = { $player }'ın kabilesini deprem vuruyor; orduları toparlanıyor.
ageofheroes-earthquake-you = Kabileni deprem vuruyor; orduların toparlanıyor.
ageofheroes-eruption = Patlama { $player }'ın şehirlerinden birini yok ediyor.
ageofheroes-eruption-you = Patlama şehirlerinden birini yok ediyor.

# Felaket etkileri
ageofheroes-hunger-strikes = Açlık vuruyor.
ageofheroes-lose-card-hunger = { $card } kaybediyorsun.
ageofheroes-barbarians-pillage = Barbarlar { $player }'ın kaynaklarına saldırıyor.
ageofheroes-barbarians-attack = Barbarlar { $player }'ın kaynaklarına saldırıyor.
ageofheroes-barbarians-attack-you = Barbarlar kaynaklarına saldırıyor.
ageofheroes-lose-card-barbarians = { $card } kaybediyorsun.
ageofheroes-block-with-card = { $player } felaketi { $card } kullanarak engelliyor.
ageofheroes-block-with-card-you = Felaketi { $card } kullanarak engelliyorsun.

# Hedefli felaket kartları (Deprem/Patlama)
ageofheroes-select-disaster-target = { $card } için bir hedef seç.
ageofheroes-no-targets = Uygun hedef yok.
ageofheroes-earthquake-strikes-you = { $attacker } sana karşı Deprem oynuyor. Orduların devre dışı kalıyor.
ageofheroes-earthquake-strikes = { $attacker } { $player }'a karşı Deprem oynuyor.
ageofheroes-armies-disabled = { $count } { $count ->
    [one] ordu
    *[other] ordu
} bir tur için devre dışı kalıyor.
ageofheroes-eruption-strikes-you = { $attacker } sana karşı Patlama oynuyor. Şehirlerinden biri yok ediliyor.
ageofheroes-eruption-strikes = { $attacker } { $player }'a karşı Patlama oynuyor.
ageofheroes-city-destroyed = Patlama tarafından bir şehir yok ediliyor.

# Pazar aşaması
ageofheroes-fair-start = Pazarda gün doğuyor.
ageofheroes-fair-draw-base = { $count } { $count ->
    [one] kart
    *[other] kart
} çekiyorsun.
ageofheroes-fair-draw-roads = Yol ağın sayesinde { $count } ek { $count ->
    [one] kart
    *[other] kart
} çekiyorsun.
ageofheroes-fair-draw-other = { $player } { $count } { $count ->
    [one] kart
    *[other] kart
} çekiyor.

# Ticaret/Müzayede
ageofheroes-auction-start = Müzayede başlıyor.
ageofheroes-offer-trade = Takas teklifi yap
ageofheroes-offer-made = { $player } { $wanted } için { $card } teklif ediyor.
ageofheroes-offer-made-you = { $wanted } için { $card } teklif ediyorsun.
ageofheroes-trade-accepted = { $player } { $other }'ın teklifini kabul ediyor ve { $receive } için { $give }'i takas ediyor.
ageofheroes-trade-accepted-you = { $other }'ın teklifini kabul ediyorsun ve { $receive } alıyorsun.
ageofheroes-trade-cancelled = { $player } { $card } için teklifini geri çekiyor.
ageofheroes-trade-cancelled-you = { $card } için teklifini geri çekiyorsun.
ageofheroes-stop-trading = Ticareti Durdur
ageofheroes-select-request = { $card } teklif ediyorsun. Karşılığında ne istiyorsun?
ageofheroes-cancel = İptal
ageofheroes-left-auction = { $player } ayrılıyor.
ageofheroes-left-auction-you = Pazardan ayrılıyorsun.
ageofheroes-any-card = Herhangi bir kart
ageofheroes-cannot-trade-own-special = Kendi özel anıt kaynağını takas edemezsin.
ageofheroes-resource-not-in-game = Bu özel kaynak bu oyunda kullanılmıyor.

# Ana oyun aşaması
ageofheroes-play-start = Oyun aşaması.
ageofheroes-day = Gün { $day }
ageofheroes-draw-card = { $player } desteden bir kart çekiyor.
ageofheroes-draw-card-you = Desteden { $card } çekiyorsun.
ageofheroes-your-action = Ne yapmak istiyorsun?

# Vergi Toplama
ageofheroes-tax-collection = { $player } Vergi Toplama seçiyor: { $cities } { $cities ->
    [one] şehir
    *[other] şehir
} { $cards } { $cards ->
    [one] kart
    *[other] kart
} topluyor.
ageofheroes-tax-collection-you = Vergi Toplama seçiyorsun: { $cities } { $cities ->
    [one] şehir
    *[other] şehir
} { $cards } { $cards ->
    [one] kart
    *[other] kart
} topluyor.
ageofheroes-tax-no-city = Vergi Toplama: Ayakta kalan şehrin yok. Yeni bir tane çekmek için bir kart at.
ageofheroes-tax-no-city-done = { $player } Vergi Toplama seçiyor ama şehri yok, bu yüzden bir kart değiştiriyor.
ageofheroes-tax-no-city-done-you = Vergi Toplama: { $card }'ı yeni bir kart için değiştirdin.

# İnşaat
ageofheroes-construction-menu = Ne inşa etmek istiyorsun?
ageofheroes-construction-done = { $player } { $article } { $building } inşa etti.
ageofheroes-construction-done-you = { $article } { $building } inşa ettin.
ageofheroes-construction-stop = İnşaatı durdur
ageofheroes-construction-stopped = İnşaatı durdurmaya karar verdin.
ageofheroes-road-select-neighbor = Yol inşa etmek için hangi komşuyu seçiyorsun.
ageofheroes-direction-left = Solundakine
ageofheroes-direction-right = Sağındakine
ageofheroes-road-request-sent = Yol isteği gönderildi. Komşunun onayı bekleniyor.
ageofheroes-road-request-received = { $requester } kabilene yol inşa etmek için izin istiyor.
ageofheroes-road-request-denied-you = Yol isteğini reddettiniz.
ageofheroes-road-request-denied = { $denier } yol isteğinizi reddetti.
ageofheroes-road-built = { $tribe1 } ve { $tribe2 } artık yolla bağlı.
ageofheroes-road-no-target = Yol inşaatı için komşu kabile yok.
ageofheroes-approve = Onayla
ageofheroes-deny = Reddet
ageofheroes-supply-exhausted = İnşa edilecek { $building } kalmadı.

# Hiçbir Şey Yapma
ageofheroes-do-nothing = { $player } pas geçiyor.
ageofheroes-do-nothing-you = Pas geçiyorsun...

# Savaş
ageofheroes-war-declare = { $attacker } { $defender }'a savaş ilan ediyor. Hedef: { $goal }.
ageofheroes-war-prepare = { $action } için ordularını seç.
ageofheroes-war-no-army = Kullanılabilir ordu veya kahraman kartın yok.
ageofheroes-war-no-targets = Savaş için uygun hedef yok.
ageofheroes-war-no-valid-goal = Bu hedefe karşı uygun savaş hedefi yok.
ageofheroes-war-select-target = Hangi oyuncuya saldıracağını seç.
ageofheroes-war-select-goal = Savaş hedefini seç.
ageofheroes-war-prepare-attack = Saldırı kuvvetlerini seç.
ageofheroes-war-prepare-defense = { $attacker } sana saldırıyor; Savunma kuvvetlerini seç.
ageofheroes-war-select-armies = Ordu seç: { $count }
ageofheroes-war-select-generals = General seç: { $count }
ageofheroes-war-select-heroes = Kahraman seç: { $count }
ageofheroes-war-attack = Saldır...
ageofheroes-war-defend = Savun...
ageofheroes-war-prepared = Kuvvetlerin: { $armies } { $armies ->
    [one] ordu
    *[other] ordu
}{ $generals ->
    [0] {""}
    [one] {" ve 1 general"}
    *[other] {" ve { $generals } general"}
}{ $heroes ->
    [0] {""}
    [one] {" ve 1 kahraman"}
    *[other] {" ve { $heroes } kahraman"}
}.
ageofheroes-war-roll-you = { $roll } atıyorsun.
ageofheroes-war-roll-other = { $player } { $roll } atıyor.
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"+1 kaleden = { $total } toplam"}
            *[other] {"+{ $fortress } kalelerden = { $total } toplam"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"+{ $general } generalden = { $total } toplam"}
            [one] {"+{ $general } generalden, +1 kaleden = { $total } toplam"}
            *[other] {"+{ $general } generalden, +{ $fortress } kalelerden = { $total } toplam"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"{ $player }: +1 kaleden = { $total } toplam"}
            *[other] {"{ $player }: +{ $fortress } kalelerden = { $total } toplam"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } generalden = { $total } toplam"}
            [one] {"{ $player }: +{ $general } generalden, +1 kaleden = { $total } toplam"}
            *[other] {"{ $player }: +{ $general } generalden, +{ $fortress } kalelerden = { $total } toplam"}
        }
    }
}

# Savaş
ageofheroes-battle-start = Savaş başlıyor. { $attacker }'ın { $att_armies } { $att_armies ->
    [one] ordusu
    *[other] ordusu
} { $defender }'ın { $def_armies } { $def_armies ->
    [one] ordusuna
    *[other] ordusuna
} karşı.
ageofheroes-dice-roll-detailed = { $name } { $dice } atıyor{ $general ->
    [0] {""}
    *[other] { " + { $general } generalden" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 kaleden" }
    *[other] { " + { $fortress } kalelerden" }
} = { $total }.
ageofheroes-dice-roll-detailed-you = { $dice } atıyorsun{ $general ->
    [0] {""}
    *[other] { " + { $general } generalden" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 kaleden" }
    *[other] { " + { $fortress } kalelerden" }
} = { $total }.
ageofheroes-round-attacker-wins = { $attacker } raund kazanıyor ({ $att_total }'e karşı { $def_total }). { $defender } bir ordu kaybediyor.
ageofheroes-round-defender-wins = { $defender } başarıyla savunuyor ({ $def_total }'e karşı { $att_total }). { $attacker } bir ordu kaybediyor.
ageofheroes-round-draw = Her iki taraf { $total } ile berabere. Ordu kaybedilmedi.
ageofheroes-battle-victory-attacker = { $attacker } { $defender }'ı yeniyor.
ageofheroes-battle-victory-defender = { $defender } { $attacker }'a karşı başarıyla savunuyor.
ageofheroes-battle-mutual-defeat = Hem { $attacker } hem { $defender } tüm ordularını kaybediyor.
ageofheroes-general-bonus = +{ $count } { $count ->
    [one] generalden
    *[other] generalden
}
ageofheroes-fortress-bonus = +{ $count } kale savunmasından
ageofheroes-battle-winner = { $winner } savaşı kazanıyor.
ageofheroes-battle-draw = Savaş beraberlikle bitiyor...
ageofheroes-battle-continue = Savaşa devam et.
ageofheroes-battle-end = Savaş bitti.

# Savaş sonuçları
ageofheroes-conquest-success = { $attacker } { $defender }'dan { $count } { $count ->
    [one] şehir
    *[other] şehir
} fethediyor.
ageofheroes-plunder-success = { $attacker } { $defender }'dan { $count } { $count ->
    [one] kart
    *[other] kart
} yağmalıyor.
ageofheroes-destruction-success = { $attacker } { $defender }'ın anıt { $count ->
    [one] kaynağını
    *[other] kaynağını
} yok ediyor.
ageofheroes-army-losses = { $player } { $count } { $count ->
    [one] ordu
    *[other] ordu
} kaybediyor.
ageofheroes-army-losses-you = { $count } { $count ->
    [one] ordu
    *[other] ordu
} kaybediyorsun.

# Ordu dönüşü
ageofheroes-army-return-road = Birlikleriniz yolla hemen geri dönüyor.
ageofheroes-army-return-delayed = { $count } { $count ->
    [one] birim
    *[other] birim
} bir sonraki turunun sonunda dönüyor.
ageofheroes-army-returned = { $player }'ın birlikleri savaştan döndü.
ageofheroes-army-returned-you = Birliklerin savaştan döndü.
ageofheroes-army-recover = { $player }'ın orduları depremden toparlanıyor.
ageofheroes-army-recover-you = Orduların depremden toparlanıyor.

# Olimpiyatlar
ageofheroes-olympics-cancel = { $player } Olimpiyat Oyunları oynuyor. Savaş iptal edildi.
ageofheroes-olympics-prompt = { $attacker } savaş ilan etti. Olimpiyat Oyunların var - iptal etmek için kullanılsın mı?
ageofheroes-yes = Evet
ageofheroes-no = Hayır

# Anıt ilerlemesi
ageofheroes-monument-progress = { $player }'ın anıtı { $count }/5 tamamlandı.
ageofheroes-monument-progress-you = Anıtın { $count }/5 tamamlandı.

# El yönetimi
ageofheroes-discard-excess = { $max } karttan fazlan var. { $count } { $count ->
    [one] kart
    *[other] kart
} at.
ageofheroes-discard-excess-other = { $player } fazla kartları atmalı.
ageofheroes-discard-more = { $count } { $count ->
    [one] kart
    *[other] kart
} daha at.

# Zafer
ageofheroes-victory-cities = { $player } 5 şehir inşa etti! Beş Şehir İmparatorluğu.
ageofheroes-victory-cities-you = 5 şehir inşa ettin! Beş Şehir İmparatorluğu.
ageofheroes-victory-monument = { $player } anıtını tamamladı! Büyük Kültürün Taşıyıcıları.
ageofheroes-victory-monument-you = Anıtını tamamladın! Büyük Kültürün Taşıyıcıları.
ageofheroes-victory-last-standing = { $player } ayakta kalan son kabile! En Kararlı.
ageofheroes-victory-last-standing-you = Ayakta kalan son kabilesin! En Kararlı.
ageofheroes-game-over = Oyun Bitti.

# Eleme
ageofheroes-eliminated = { $player } elendi.
ageofheroes-eliminated-you = Elendin.

# El
ageofheroes-hand-empty = Kartın yok.
ageofheroes-hand-contents = Elin ({ $count } { $count ->
    [one] kart
    *[other] kart
}): { $cards }

# Durum
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [one] şehir
    *[other] şehir
}, { $armies } { $armies ->
    [one] ordu
    *[other] ordu
}, { $monument }/5 anıt
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = Şehirler: { $count }
ageofheroes-status-armies = Ordular: { $count }
ageofheroes-status-generals = Generaller: { $count }
ageofheroes-status-fortresses = Kaleler: { $count }
ageofheroes-status-monument = Anıt: { $count }/5
ageofheroes-status-roads = Yollar: { $left }{ $right }
ageofheroes-status-road-left = sol
ageofheroes-status-road-right = sağ
ageofheroes-status-none = yok
ageofheroes-status-earthquake-armies = Toparlanıyor ordular: { $count }
ageofheroes-status-returning-armies = Dönen ordular: { $count }
ageofheroes-status-returning-generals = Dönen generaller: { $count }

# Deste bilgisi
ageofheroes-deck-empty = Destede { $card } kart kalmadı.
ageofheroes-deck-count = Kalan kartlar: { $count }
ageofheroes-deck-reshuffled = Atılan kartlar destede karıştırıldı.

# Pes et
ageofheroes-give-up-confirm = Pes etmek istediğinden emin misin?
ageofheroes-gave-up = { $player } pes etti!
ageofheroes-gave-up-you = Pes ettin!

# Kahraman kartı
ageofheroes-hero-use = Ordu veya general olarak kullan?
ageofheroes-hero-army = Ordu
ageofheroes-hero-general = General

# Şans kartı
ageofheroes-fortune-reroll = { $player } tekrar atmak için Şans kullanıyor.
ageofheroes-fortune-prompt = Atışı kaybettin. Tekrar atmak için Şans kullan?

# Devre dışı eylem nedenleri
ageofheroes-not-your-turn = Senin turun değil.
ageofheroes-game-not-started = Oyun henüz başlamadı.
ageofheroes-wrong-phase = Bu eylem mevcut aşamada kullanılamaz.
ageofheroes-no-resources = Gerekli kaynaklara sahip değilsin.

# İnşaat maliyetleri (görüntüleme için)
ageofheroes-cost-army = 2 Tahıl, Demir
ageofheroes-cost-fortress = Demir, Odun, Taş
ageofheroes-cost-general = Demir, Altın
ageofheroes-cost-road = 2 Taş
ageofheroes-cost-city = 2 Odun, Taş
