# Five Card Draw

game-name-fivecarddraw = Pet Kart

draw-set-starting-chips = Začetni žetoni: { $count }
draw-enter-starting-chips = Vnesite začetne žetone
draw-option-changed-starting-chips = Začetni žetoni nastavljeni na { $count }.

draw-set-ante = Vložek: { $count }
draw-enter-ante = Vnesite znesek vložka
draw-option-changed-ante = Vložek nastavljen na { $count }.

draw-set-turn-timer = Časovnik poteze: { $mode }
draw-select-turn-timer = Izberite časovnik poteze
draw-option-changed-turn-timer = Časovnik poteze nastavljen na { $mode }.

draw-set-raise-mode = Način dvigovanja: { $mode }
draw-select-raise-mode = Izberite način dvigovanja
draw-option-changed-raise-mode = Način dvigovanja nastavljen na { $mode }.

draw-set-max-raises = Maksimalna dvigovanja: { $count }
draw-enter-max-raises = Vnesite maksimalna dvigovanja (0 za neomejeno)
draw-option-changed-max-raises = Maksimalna dvigovanja nastavljena na { $count }.

draw-antes-posted = Vložki postavljeni: { $amount }.
draw-betting-round-1 = Krog stavljenja.
draw-betting-round-2 = Krog stavljenja.
draw-begin-draw = Faza menjave.
draw-not-draw-phase = Ni čas za menjavo.
draw-not-betting = Ne morete stavljati med fazo menjave.

draw-toggle-discard = Preklopi zavrženje za karto { $index }
draw-card-keep = { $card }, obdržana
draw-card-discard = { $card }, bo zavržena
draw-card-kept = Obdržite { $card }.
draw-card-discarded = Zavrzite { $card }.
draw-draw-cards = Vlečete karte
draw-draw-cards-count = Vlečete { $count } { $count ->
    [one] karto
   *[other] kart
}
draw-dealt-cards = Dobite { $cards }.
draw-you-drew-cards = Vlečete { $cards }.
draw-you-draw = Vlečete { $count } { $count ->
    [one] karto
   *[other] kart
}.
draw-player-draws = { $player } vleče { $count } { $count ->
    [one] karto
   *[other] kart
}.
draw-you-stand-pat = Ostanete.
draw-player-stands-pat = { $player } ostane.
draw-you-discard-limit = Lahko zavržete do { $count } kart.
draw-player-discard-limit = { $player } lahko zavrže do { $count } kart.
