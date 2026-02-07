# Pig oyun mesajları
# Not: Raund başlangıcı, tur başlangıcı, hedef skor gibi ortak mesajlar games.ftl'de

# Oyun bilgisi
game-name-pig = Pig
pig-category = Zar Oyunları

# Eylemler
pig-roll = Zar at
pig-bank = { $points } puan bankaya yatır

# Oyun olayları (Pig'e özel)
pig-rolls = { $player } zar atıyor...
pig-roll-result = { $roll }, toplam { $total }
pig-bust = Vay canına, 1! { $player } { $points } puan kaybediyor.
pig-bank-action = { $player } { $points } puan bankaya yatırmaya karar veriyor, toplam { $total }
pig-winner = Bir kazananımız var, o da { $player }!

# Pig'e özel seçenekler
pig-set-min-bank = Minimum bankaya yatırma: { $points }
pig-set-dice-sides = Zar yüzleri: { $sides }
pig-enter-min-bank = Minimum bankaya yatırma puanını girin:
pig-enter-dice-sides = Zar yüz sayısını girin:
pig-option-changed-min-bank = Minimum bankaya yatırma puanı { $points } olarak değiştirildi
pig-option-changed-dice = Zar artık { $sides } yüze sahip

# Devre dışı nedenler
pig-need-more-points = Bankaya yatırmak için daha fazla puana ihtiyacın var.

# Doğrulama hataları
pig-error-min-bank-too-high = Minimum bankaya yatırma puanı hedef skordan az olmalı.
