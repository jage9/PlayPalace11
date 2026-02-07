# Scopa game messages
# Note: Common messages like round-start, turn-start, target-score, team-mode are in games.ftl

# Game name
game-name-scopa = Scopa

# Game events
scopa-initial-table = Kartu meja: { $cards }
scopa-no-initial-table = Tidak ada kartu di meja untuk memulai.
scopa-you-collect = Anda mengumpulkan { $cards } dengan { $card }
scopa-player-collects = { $player } mengumpulkan { $cards } dengan { $card }
scopa-you-put-down = Anda menaruh { $card }.
scopa-player-puts-down = { $player } menaruh { $card }.
scopa-scopa-suffix =  - SCOPA!
scopa-clear-table-suffix = , membersihkan meja.
scopa-remaining-cards = { $player } mendapat kartu meja yang tersisa.
scopa-scoring-round = Ronde penilaian...
scopa-most-cards = { $player } mencetak 1 poin untuk kartu terbanyak ({ $count } kartu).
scopa-most-cards-tie = Kartu terbanyak seri - tidak ada poin yang diberikan.
scopa-most-diamonds = { $player } mencetak 1 poin untuk wajik terbanyak ({ $count } wajik).
scopa-most-diamonds-tie = Wajik terbanyak seri - tidak ada poin yang diberikan.
scopa-seven-diamonds = { $player } mencetak 1 poin untuk 7 wajik.
scopa-seven-diamonds-multi = { $player } mencetak 1 poin untuk 7 wajik terbanyak ({ $count } × 7 wajik).
scopa-seven-diamonds-tie = 7 wajik seri - tidak ada poin yang diberikan.
scopa-most-sevens = { $player } mencetak 1 poin untuk tujuh terbanyak ({ $count } tujuh).
scopa-most-sevens-tie = Tujuh terbanyak seri - tidak ada poin yang diberikan.
scopa-round-scores = Skor ronde:
scopa-round-score-line = { $player }: +{ $round_score } (total: { $total_score })
scopa-table-empty = Tidak ada kartu di meja.
scopa-no-such-card = Tidak ada kartu di posisi itu.
scopa-captured-count = Anda telah mengumpulkan { $count } kartu

# View actions
scopa-view-table = Lihat meja
scopa-view-captured = Lihat yang dikumpulkan

# Scopa-specific options
scopa-enter-target-score = Masukkan skor target (1-121)
scopa-set-cards-per-deal = Kartu per bagian: { $cards }
scopa-enter-cards-per-deal = Masukkan kartu per bagian (1-10)
scopa-set-decks = Jumlah dek: { $decks }
scopa-enter-decks = Masukkan jumlah dek (1-6)
scopa-toggle-escoba = Escoba (jumlah ke 15): { $enabled }
scopa-toggle-hints = Tampilkan petunjuk tangkapan: { $enabled }
scopa-set-mechanic = Mekanik scopa: { $mechanic }
scopa-select-mechanic = Pilih mekanik scopa
scopa-toggle-instant-win = Kemenangan instan pada scopa: { $enabled }
scopa-toggle-team-scoring = Gabungkan kartu tim untuk penilaian: { $enabled }
scopa-toggle-inverse = Mode terbalik (mencapai target = eliminasi): { $enabled }

# Option change announcements
scopa-option-changed-cards = Kartu per bagian diatur ke { $cards }.
scopa-option-changed-decks = Jumlah dek diatur ke { $decks }.
scopa-option-changed-escoba = Escoba { $enabled }.
scopa-option-changed-hints = Petunjuk tangkapan { $enabled }.
scopa-option-changed-mechanic = Mekanik scopa diatur ke { $mechanic }.
scopa-option-changed-instant = Kemenangan instan pada scopa { $enabled }.
scopa-option-changed-team-scoring = Penilaian kartu tim { $enabled }.
scopa-option-changed-inverse = Mode terbalik { $enabled }.

# Scopa mechanic choices
scopa-mechanic-normal = Normal
scopa-mechanic-no_scopas = Tanpa Scopa
scopa-mechanic-only_scopas = Hanya Scopa

# Disabled action reasons
scopa-timer-not-active = Timer ronde tidak aktif.

# Validation errors
scopa-error-not-enough-cards = Tidak cukup kartu di { $decks } { $decks ->
    [one] dek
    *[other] dek
} untuk { $players } { $players ->
    [one] pemain
    *[other] pemain
} dengan { $cards_per_deal } kartu masing-masing. (Butuh { $cards_per_deal } × { $players } = { $cards_needed } kartu, tetapi hanya punya { $total_cards }.)
