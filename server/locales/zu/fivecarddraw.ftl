# Five Card Draw (isiZulu)

game-name-fivecarddraw = Five Card Draw

draw-set-starting-chips = Ama-chips okuqala: { $count }
draw-enter-starting-chips = Faka ama-chips okuqala
draw-option-changed-starting-chips = Ama-chips okuqala asetelwe ku-{ $count }.

draw-set-ante = I-Ante: { $count }
draw-enter-ante = Faka inani le-ante
draw-option-changed-ante = I-Ante isetelwe ku-{ $count }.

draw-set-turn-timer = Isikhathi sokushintshana: { $mode }
draw-select-turn-timer = Khetha isikhathi sokushintshana
draw-option-changed-turn-timer = Isikhathi sokushintshana sisetelwe ku-{ $mode }.

draw-set-raise-mode = Imodi yokuphakamisa: { $mode }
draw-select-raise-mode = Khetha imodi yokuphakamisa
draw-option-changed-raise-mode = Imodi yokuphakamisa isetelwe ku-{ $mode }.

draw-set-max-raises = Ukuphakamisa okuphezulu: { $count }
draw-enter-max-raises = Faka ukuphakamisa okuphezulu (0 okungenamkhawulo)
draw-option-changed-max-raises = Ukuphakamisa okuphezulu kusetelwe ku-{ $count }.

draw-antes-posted = Ama-antes athunyelwe: { $amount }.
draw-betting-round-1 = Umjikelezo wokubheja.
draw-betting-round-2 = Umjikelezo wokubheja.
draw-begin-draw = Isigaba sokudonsa.
draw-not-draw-phase = Akusikho isikhathi sokudonsa.
draw-not-betting = Awukwazi ukubheja ngesikhathi sesigaba sokudonsa.

draw-toggle-discard = Shintsha ukulahlwa kwekhadi { $index }
draw-card-keep = { $card }, libambile
draw-card-discard = { $card }, lizocalahla
draw-card-kept = Gcina { $card }.
draw-card-discarded = Lahla { $card }.
draw-draw-cards = Donsa amakhadi
draw-draw-cards-count = Donsa { $count } { $count ->
    [one] ikhadi
   *[other] amakhadi
}
draw-dealt-cards = Unikezelwe { $cards }.
draw-you-drew-cards = Wena udonsa { $cards }.
draw-you-draw = Wena udonsa { $count } { $count ->
    [one] ikhadi
   *[other] amakhadi
}.
draw-player-draws = U-{ $player } udonsa { $count } { $count ->
    [one] ikhadi
   *[other] amakhadi
}.
draw-you-stand-pat = Wena ugxila.
draw-player-stands-pat = U-{ $player } ugxila.
draw-you-discard-limit = Ungalahla amakhadi afika ku-{ $count }.
draw-player-discard-limit = U-{ $player } angalahla amakhadi afika ku-{ $count }.
