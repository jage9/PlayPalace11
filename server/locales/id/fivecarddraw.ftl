# Five Card Draw

game-name-fivecarddraw = Five Card Draw

draw-set-starting-chips = Chip awal: { $count }
draw-enter-starting-chips = Masukkan chip awal
draw-option-changed-starting-chips = Chip awal diatur ke { $count }.

draw-set-ante = Ante: { $count }
draw-enter-ante = Masukkan jumlah ante
draw-option-changed-ante = Ante diatur ke { $count }.

draw-set-turn-timer = Timer giliran: { $mode }
draw-select-turn-timer = Pilih timer giliran
draw-option-changed-turn-timer = Timer giliran diatur ke { $mode }.

draw-set-raise-mode = Mode raise: { $mode }
draw-select-raise-mode = Pilih mode raise
draw-option-changed-raise-mode = Mode raise diatur ke { $mode }.

draw-set-max-raises = Raise maksimal: { $count }
draw-enter-max-raises = Masukkan raise maksimal (0 untuk tanpa batas)
draw-option-changed-max-raises = Raise maksimal diatur ke { $count }.

draw-antes-posted = Ante dipasang: { $amount }.
draw-betting-round-1 = Ronde taruhan.
draw-betting-round-2 = Ronde taruhan.
draw-begin-draw = Fase ambil.
draw-not-draw-phase = Belum waktunya untuk mengambil.
draw-not-betting = Anda tidak dapat bertaruh selama fase ambil.

draw-toggle-discard = Ubah buang untuk kartu { $index }
draw-card-keep = { $card }, ditahan
draw-card-discard = { $card }, akan dibuang
draw-card-kept = Tahan { $card }.
draw-card-discarded = Buang { $card }.
draw-draw-cards = Ambil kartu
draw-draw-cards-count = Ambil { $count } { $count ->
    [one] kartu
   *[other] kartu
}
draw-dealt-cards = Anda dibagikan { $cards }.
draw-you-drew-cards = Anda mengambil { $cards }.
draw-you-draw = Anda mengambil { $count } { $count ->
    [one] kartu
   *[other] kartu
}.
draw-player-draws = { $player } mengambil { $count } { $count ->
    [one] kartu
   *[other] kartu
}.
draw-you-stand-pat = Anda stand pat.
draw-player-stands-pat = { $player } stand pat.
draw-you-discard-limit = Anda dapat membuang hingga { $count } kartu.
draw-player-discard-limit = { $player } dapat membuang hingga { $count } kartu.
