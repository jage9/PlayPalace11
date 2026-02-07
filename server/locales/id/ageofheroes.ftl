# Age of Heroes game messages
# A civilization-building card game for 2-6 players

# Game name
game-name-ageofheroes = Age of Heroes

# Tribes
ageofheroes-tribe-egyptians = Mesir
ageofheroes-tribe-romans = Romawi
ageofheroes-tribe-greeks = Yunani
ageofheroes-tribe-babylonians = Babilonia
ageofheroes-tribe-celts = Kelt
ageofheroes-tribe-chinese = Tionghoa

# Special Resources (for monuments)
ageofheroes-special-limestone = Batu Kapur
ageofheroes-special-concrete = Beton
ageofheroes-special-marble = Marmer
ageofheroes-special-bricks = Bata
ageofheroes-special-sandstone = Batu Pasir
ageofheroes-special-granite = Granit

# Standard Resources
ageofheroes-resource-iron = Besi
ageofheroes-resource-wood = Kayu
ageofheroes-resource-grain = Gandum
ageofheroes-resource-stone = Batu
ageofheroes-resource-gold = Emas

# Events
ageofheroes-event-population-growth = Pertumbuhan Populasi
ageofheroes-event-earthquake = Gempa Bumi
ageofheroes-event-eruption = Letusan
ageofheroes-event-hunger = Kelaparan
ageofheroes-event-barbarians = Barbar
ageofheroes-event-olympics = Olimpiade
ageofheroes-event-hero = Pahlawan
ageofheroes-event-fortune = Keberuntungan

# Buildings
ageofheroes-building-army = Tentara
ageofheroes-building-fortress = Benteng
ageofheroes-building-general = Jenderal
ageofheroes-building-road = Jalan
ageofheroes-building-city = Kota

# Actions
ageofheroes-action-tax-collection = Pengumpulan Pajak
ageofheroes-action-construction = Konstruksi
ageofheroes-action-war = Perang
ageofheroes-action-do-nothing = Tidak Berbuat Apa-apa
ageofheroes-play = Main

# War goals
ageofheroes-war-conquest = Penaklukan
ageofheroes-war-plunder = Penjarahan
ageofheroes-war-destruction = Penghancuran

# Game options
ageofheroes-set-victory-cities = Kota kemenangan: { $cities }
ageofheroes-enter-victory-cities = Masukkan jumlah kota untuk menang (3-7)
ageofheroes-set-victory-monument = Penyelesaian monumen: { $progress }%
ageofheroes-toggle-neighbor-roads = Jalan hanya ke tetangga: { $enabled }
ageofheroes-set-max-hand = Maksimum kartu di tangan: { $cards } kartu

# Option change announcements
ageofheroes-option-changed-victory-cities = Kemenangan memerlukan { $cities } kota.
ageofheroes-option-changed-victory-monument = Ambang penyelesaian monumen diatur ke { $progress }%.
ageofheroes-option-changed-neighbor-roads = Jalan hanya ke tetangga { $enabled }.
ageofheroes-option-changed-max-hand = Maksimum kartu di tangan diatur ke { $cards } kartu.

# Setup phase
ageofheroes-setup-start = Anda adalah pemimpin suku { $tribe }. Sumber daya monumen khusus Anda adalah { $special }. Lempar dadu untuk menentukan urutan giliran.
ageofheroes-setup-viewer = Pemain melempar dadu untuk menentukan urutan giliran.
ageofheroes-roll-dice = Lempar dadu
ageofheroes-war-roll-dice = Lempar dadu
ageofheroes-dice-result = Anda melempar { $total } ({ $die1 } + { $die2 }).
ageofheroes-dice-result-other = { $player } melempar { $total }.
ageofheroes-dice-tie = Beberapa pemain seri dengan { $total }. Melempar lagi...
ageofheroes-first-player = { $player } melempar tertinggi dengan { $total } dan bermain pertama.
ageofheroes-first-player-you = Dengan { $total } poin, Anda bermain pertama.

# Preparation phase
ageofheroes-prepare-start = Pemain harus memainkan kartu peristiwa dan membuang bencana.
ageofheroes-prepare-your-turn = Anda memiliki { $count } { $count ->
    [one] kartu
    *[other] kartu
} untuk dimainkan atau dibuang.
ageofheroes-prepare-done = Fase persiapan selesai.

# Events played/discarded
ageofheroes-population-growth = { $player } memainkan Pertumbuhan Populasi dan membangun kota baru.
ageofheroes-population-growth-you = Anda memainkan Pertumbuhan Populasi dan membangun kota baru.
ageofheroes-discard-card = { $player } membuang { $card }.
ageofheroes-discard-card-you = Anda membuang { $card }.
ageofheroes-earthquake = Gempa bumi melanda suku { $player }; tentara mereka masuk pemulihan.
ageofheroes-earthquake-you = Gempa bumi melanda suku Anda; tentara Anda masuk pemulihan.
ageofheroes-eruption = Letusan menghancurkan salah satu kota { $player }.
ageofheroes-eruption-you = Letusan menghancurkan salah satu kota Anda.

# Disaster effects
ageofheroes-hunger-strikes = Kelaparan melanda.
ageofheroes-lose-card-hunger = Anda kehilangan { $card }.
ageofheroes-barbarians-pillage = Barbar menyerang sumber daya { $player }.
ageofheroes-barbarians-attack = Barbar menyerang sumber daya { $player }.
ageofheroes-barbarians-attack-you = Barbar menyerang sumber daya Anda.
ageofheroes-lose-card-barbarians = Anda kehilangan { $card }.
ageofheroes-block-with-card = { $player } memblokir bencana menggunakan { $card }.
ageofheroes-block-with-card-you = Anda memblokir bencana menggunakan { $card }.

# Targeted disaster cards (Earthquake/Eruption)
ageofheroes-select-disaster-target = Pilih target untuk { $card }.
ageofheroes-no-targets = Tidak ada target valid yang tersedia.
ageofheroes-earthquake-strikes-you = { $attacker } memainkan Gempa Bumi melawan Anda. Tentara Anda dinonaktifkan.
ageofheroes-earthquake-strikes = { $attacker } memainkan Gempa Bumi melawan { $player }.
ageofheroes-armies-disabled = { $count } { $count ->
    [one] tentara
    *[other] tentara
} dinonaktifkan selama satu giliran.
ageofheroes-eruption-strikes-you = { $attacker } memainkan Letusan melawan Anda. Salah satu kota Anda hancur.
ageofheroes-eruption-strikes = { $attacker } memainkan Letusan melawan { $player }.
ageofheroes-city-destroyed = Sebuah kota dihancurkan oleh letusan.

# Fair phase
ageofheroes-fair-start = Hari dimulai di pasar.
ageofheroes-fair-draw-base = Anda mengambil { $count } { $count ->
    [one] kartu
    *[other] kartu
}.
ageofheroes-fair-draw-roads = Anda mengambil { $count } { $count ->
    [one] kartu
    *[other] kartu
} tambahan berkat jaringan jalan Anda.
ageofheroes-fair-draw-other = { $player } mengambil { $count } { $count ->
    [one] kartu
    *[other] kartu
}.

# Trading/Auction
ageofheroes-auction-start = Lelang dimulai.
ageofheroes-offer-trade = Tawarkan untuk berdagang
ageofheroes-offer-made = { $player } menawarkan { $card } untuk { $wanted }.
ageofheroes-offer-made-you = Anda menawarkan { $card } untuk { $wanted }.
ageofheroes-trade-accepted = { $player } menerima tawaran { $other } dan menukar { $give } dengan { $receive }.
ageofheroes-trade-accepted-you = Anda menerima tawaran { $other } dan menerima { $receive }.
ageofheroes-trade-cancelled = { $player } menarik tawaran mereka untuk { $card }.
ageofheroes-trade-cancelled-you = Anda menarik tawaran Anda untuk { $card }.
ageofheroes-stop-trading = Berhenti Berdagang
ageofheroes-select-request = Anda menawarkan { $card }. Apa yang Anda inginkan sebagai balasannya?
ageofheroes-cancel = Batal
ageofheroes-left-auction = { $player } pergi.
ageofheroes-left-auction-you = Anda pergi dari pasar.
ageofheroes-any-card = Kartu apa saja
ageofheroes-cannot-trade-own-special = Anda tidak dapat memperdagangkan sumber daya monumen khusus Anda sendiri.
ageofheroes-resource-not-in-game = Sumber daya khusus ini tidak digunakan dalam permainan ini.

# Main play phase
ageofheroes-play-start = Fase bermain.
ageofheroes-day = Hari { $day }
ageofheroes-draw-card = { $player } mengambil kartu dari dek.
ageofheroes-draw-card-you = Anda mengambil { $card } dari dek.
ageofheroes-your-action = Apa yang ingin Anda lakukan?

# Tax Collection
ageofheroes-tax-collection = { $player } memilih Pengumpulan Pajak: { $cities } { $cities ->
    [one] kota
    *[other] kota
} mengumpulkan { $cards } { $cards ->
    [one] kartu
    *[other] kartu
}.
ageofheroes-tax-collection-you = Anda memilih Pengumpulan Pajak: { $cities } { $cities ->
    [one] kota
    *[other] kota
} mengumpulkan { $cards } { $cards ->
    [one] kartu
    *[other] kartu
}.
ageofheroes-tax-no-city = Pengumpulan Pajak: Anda tidak memiliki kota yang masih hidup. Buang kartu untuk mengambil yang baru.
ageofheroes-tax-no-city-done = { $player } memilih Pengumpulan Pajak tetapi tidak memiliki kota, jadi mereka menukar kartu.
ageofheroes-tax-no-city-done-you = Pengumpulan Pajak: Anda menukar { $card } dengan kartu baru.

# Construction
ageofheroes-construction-menu = Apa yang ingin Anda bangun?
ageofheroes-construction-done = { $player } membangun { $article } { $building }.
ageofheroes-construction-done-you = Anda membangun { $article } { $building }.
ageofheroes-construction-stop = Berhenti membangun
ageofheroes-construction-stopped = Anda memutuskan untuk berhenti membangun.
ageofheroes-road-select-neighbor = Pilih tetangga mana yang akan dibangun jalannya.
ageofheroes-direction-left = Ke kiri Anda
ageofheroes-direction-right = Ke kanan Anda
ageofheroes-road-request-sent = Permintaan jalan dikirim. Menunggu persetujuan tetangga.
ageofheroes-road-request-received = { $requester } meminta izin untuk membangun jalan ke suku Anda.
ageofheroes-road-request-denied-you = Anda menolak permintaan jalan.
ageofheroes-road-request-denied = { $denier } menolak permintaan jalan Anda.
ageofheroes-road-built = { $tribe1 } dan { $tribe2 } sekarang terhubung dengan jalan.
ageofheroes-road-no-target = Tidak ada suku tetangga yang tersedia untuk pembangunan jalan.
ageofheroes-approve = Setuju
ageofheroes-deny = Tolak
ageofheroes-supply-exhausted = Tidak ada { $building } lagi yang tersedia untuk dibangun.

# Do Nothing
ageofheroes-do-nothing = { $player } melewatkan.
ageofheroes-do-nothing-you = Anda melewatkan...

# War
ageofheroes-war-declare = { $attacker } menyatakan perang terhadap { $defender }. Tujuan: { $goal }.
ageofheroes-war-prepare = Pilih tentara Anda untuk { $action }.
ageofheroes-war-no-army = Anda tidak memiliki tentara atau kartu pahlawan yang tersedia.
ageofheroes-war-no-targets = Tidak ada target valid untuk perang.
ageofheroes-war-no-valid-goal = Tidak ada tujuan perang yang valid terhadap target ini.
ageofheroes-war-select-target = Pilih pemain mana yang akan diserang.
ageofheroes-war-select-goal = Pilih tujuan perang Anda.
ageofheroes-war-prepare-attack = Pilih pasukan penyerang Anda.
ageofheroes-war-prepare-defense = { $attacker } menyerang Anda; Pilih pasukan pertahanan Anda.
ageofheroes-war-select-armies = Pilih tentara: { $count }
ageofheroes-war-select-generals = Pilih jenderal: { $count }
ageofheroes-war-select-heroes = Pilih pahlawan: { $count }
ageofheroes-war-attack = Serang...
ageofheroes-war-defend = Bertahan...
ageofheroes-war-prepared = Pasukan Anda: { $armies } { $armies ->
    [one] tentara
    *[other] tentara
}{ $generals ->
    [0] {""}
    [one] {" dan 1 jenderal"}
    *[other] {" dan { $generals } jenderal"}
}{ $heroes ->
    [0] {""}
    [one] {" dan 1 pahlawan"}
    *[other] {" dan { $heroes } pahlawan"}
}.
ageofheroes-war-roll-you = Anda melempar { $roll }.
ageofheroes-war-roll-other = { $player } melempar { $roll }.
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [1] {"+1 dari benteng = { $total } total"}
            *[other] {"+{ $fortress } dari benteng = { $total } total"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"+{ $general } dari jenderal = { $total } total"}
            [1] {"+{ $general } dari jenderal, +1 dari benteng = { $total } total"}
            *[other] {"+{ $general } dari jenderal, +{ $fortress } dari benteng = { $total } total"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [1] {"{ $player }: +1 dari benteng = { $total } total"}
            *[other] {"{ $player }: +{ $fortress } dari benteng = { $total } total"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } dari jenderal = { $total } total"}
            [1] {"{ $player }: +{ $general } dari jenderal, +1 dari benteng = { $total } total"}
            *[other] {"{ $player }: +{ $general } dari jenderal, +{ $fortress } dari benteng = { $total } total"}
        }
    }
}

# Battle
ageofheroes-battle-start = Pertempuran dimulai. { $attacker } dengan { $att_armies } { $att_armies ->
    [one] tentara
    *[other] tentara
} melawan { $defender } dengan { $def_armies } { $def_armies ->
    [one] tentara
    *[other] tentara
}.
ageofheroes-dice-roll-detailed = { $name } melempar { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } dari jenderal" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 dari benteng" }
    *[other] { " + { $fortress } dari benteng" }
} = { $total }.
ageofheroes-dice-roll-detailed-you = Anda melempar { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } dari jenderal" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 dari benteng" }
    *[other] { " + { $fortress } dari benteng" }
} = { $total }.
ageofheroes-round-attacker-wins = { $attacker } menang putaran ini ({ $att_total } vs { $def_total }). { $defender } kehilangan satu tentara.
ageofheroes-round-defender-wins = { $defender } berhasil bertahan ({ $def_total } vs { $att_total }). { $attacker } kehilangan satu tentara.
ageofheroes-round-draw = Kedua sisi seri di { $total }. Tidak ada tentara yang hilang.
ageofheroes-battle-victory-attacker = { $attacker } mengalahkan { $defender }.
ageofheroes-battle-victory-defender = { $defender } berhasil bertahan melawan { $attacker }.
ageofheroes-battle-mutual-defeat = { $attacker } dan { $defender } kehilangan semua tentara.
ageofheroes-general-bonus = +{ $count } dari { $count ->
    [one] jenderal
    *[other] jenderal
}
ageofheroes-fortress-bonus = +{ $count } dari pertahanan benteng
ageofheroes-battle-winner = { $winner } memenangkan pertempuran.
ageofheroes-battle-draw = Pertempuran berakhir seri...
ageofheroes-battle-continue = Lanjutkan pertempuran.
ageofheroes-battle-end = Pertempuran telah berakhir.

# War outcomes
ageofheroes-conquest-success = { $attacker } menaklukkan { $count } { $count ->
    [one] kota
    *[other] kota
} dari { $defender }.
ageofheroes-plunder-success = { $attacker } menjarah { $count } { $count ->
    [one] kartu
    *[other] kartu
} dari { $defender }.
ageofheroes-destruction-success = { $attacker } menghancurkan { $count } { $count ->
    [one] sumber daya
    *[other] sumber daya
} monumen { $defender }.
ageofheroes-army-losses = { $player } kehilangan { $count } { $count ->
    [one] tentara
    *[other] tentara
}.
ageofheroes-army-losses-you = Anda kehilangan { $count } { $count ->
    [one] tentara
    *[other] tentara
}.

# Army return
ageofheroes-army-return-road = Pasukan Anda kembali segera melalui jalan.
ageofheroes-army-return-delayed = { $count } { $count ->
    [one] unit kembali
    *[other] unit kembali
} di akhir giliran Anda berikutnya.
ageofheroes-army-returned = Pasukan { $player } telah kembali dari perang.
ageofheroes-army-returned-you = Pasukan Anda telah kembali dari perang.
ageofheroes-army-recover = Tentara { $player } pulih dari gempa bumi.
ageofheroes-army-recover-you = Tentara Anda pulih dari gempa bumi.

# Olympics
ageofheroes-olympics-cancel = { $player } memainkan Olimpiade. Perang dibatalkan.
ageofheroes-olympics-prompt = { $attacker } telah menyatakan perang. Anda memiliki Olimpiade - gunakan untuk membatalkannya?
ageofheroes-yes = Ya
ageofheroes-no = Tidak

# Monument progress
ageofheroes-monument-progress = Monumen { $player } { $count }/5 selesai.
ageofheroes-monument-progress-you = Monumen Anda { $count }/5 selesai.

# Hand management
ageofheroes-discard-excess = Anda memiliki lebih dari { $max } kartu. Buang { $count } { $count ->
    [one] kartu
    *[other] kartu
}.
ageofheroes-discard-excess-other = { $player } harus membuang kartu berlebih.
ageofheroes-discard-more = Buang { $count } { $count ->
    [one] kartu
    *[other] kartu
} lagi.

# Victory
ageofheroes-victory-cities = { $player } telah membangun 5 kota! Kerajaan Lima Kota.
ageofheroes-victory-cities-you = Anda telah membangun 5 kota! Kerajaan Lima Kota.
ageofheroes-victory-monument = { $player } telah menyelesaikan monumen mereka! Pembawa Budaya Agung.
ageofheroes-victory-monument-you = Anda telah menyelesaikan monumen Anda! Pembawa Budaya Agung.
ageofheroes-victory-last-standing = { $player } adalah suku terakhir yang bertahan! Yang Paling Gigih.
ageofheroes-victory-last-standing-you = Anda adalah suku terakhir yang bertahan! Yang Paling Gigih.
ageofheroes-game-over = Permainan Berakhir.

# Elimination
ageofheroes-eliminated = { $player } telah dieliminasi.
ageofheroes-eliminated-you = Anda telah dieliminasi.

# Hand
ageofheroes-hand-empty = Anda tidak memiliki kartu.
ageofheroes-hand-contents = Kartu Anda ({ $count } { $count ->
    [one] kartu
    *[other] kartu
}): { $cards }

# Status
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [one] kota
    *[other] kota
}, { $armies } { $armies ->
    [one] tentara
    *[other] tentara
}, { $monument }/5 monumen
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = Kota: { $count }
ageofheroes-status-armies = Tentara: { $count }
ageofheroes-status-generals = Jenderal: { $count }
ageofheroes-status-fortresses = Benteng: { $count }
ageofheroes-status-monument = Monumen: { $count }/5
ageofheroes-status-roads = Jalan: { $left }{ $right }
ageofheroes-status-road-left = kiri
ageofheroes-status-road-right = kanan
ageofheroes-status-none = tidak ada
ageofheroes-status-earthquake-armies = Tentara yang pulih: { $count }
ageofheroes-status-returning-armies = Tentara yang kembali: { $count }
ageofheroes-status-returning-generals = Jenderal yang kembali: { $count }

# Deck info
ageofheroes-deck-empty = Tidak ada kartu { $card } lagi di dek.
ageofheroes-deck-count = Kartu tersisa: { $count }
ageofheroes-deck-reshuffled = Tumpukan buangan telah dikocok ulang ke dalam dek.

# Give up
ageofheroes-give-up-confirm = Apakah Anda yakin ingin menyerah?
ageofheroes-gave-up = { $player } menyerah!
ageofheroes-gave-up-you = Anda menyerah!

# Hero card
ageofheroes-hero-use = Gunakan sebagai tentara atau jenderal?
ageofheroes-hero-army = Tentara
ageofheroes-hero-general = Jenderal

# Fortune card
ageofheroes-fortune-reroll = { $player } menggunakan Keberuntungan untuk melempar ulang.
ageofheroes-fortune-prompt = Anda kalah dalam lemparan. Gunakan Keberuntungan untuk melempar ulang?

# Disabled action reasons
ageofheroes-not-your-turn = Bukan giliran Anda.
ageofheroes-game-not-started = Permainan belum dimulai.
ageofheroes-wrong-phase = Aksi ini tidak tersedia dalam fase saat ini.
ageofheroes-no-resources = Anda tidak memiliki sumber daya yang dibutuhkan.

# Building costs (for display)
ageofheroes-cost-army = 2 Gandum, Besi
ageofheroes-cost-fortress = Besi, Kayu, Batu
ageofheroes-cost-general = Besi, Emas
ageofheroes-cost-road = 2 Batu
ageofheroes-cost-city = 2 Kayu, Batu
