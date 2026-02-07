# Five Card Draw

game-name-fivecarddraw = Päťkartový Poker

draw-set-starting-chips = Začiatočné žetóny: { $count }
draw-enter-starting-chips = Zadajte začiatočné žetóny
draw-option-changed-starting-chips = Začiatočné žetóny nastavené na { $count }.

draw-set-ante = Ante: { $count }
draw-enter-ante = Zadajte sumu ante
draw-option-changed-ante = Ante nastavené na { $count }.

draw-set-turn-timer = Časovač ťahu: { $mode }
draw-select-turn-timer = Vyberte časovač ťahu
draw-option-changed-turn-timer = Časovač ťahu nastavený na { $mode }.

draw-set-raise-mode = Režim prihodzovania: { $mode }
draw-select-raise-mode = Vyberte režim prihodzovania
draw-option-changed-raise-mode = Režim prihodzovania nastavený na { $mode }.

draw-set-max-raises = Maximálne prihadzovanie: { $count }
draw-enter-max-raises = Zadajte maximálne prihadzovanie (0 pre neobmedzené)
draw-option-changed-max-raises = Maximálne prihadzovanie nastavené na { $count }.

draw-antes-posted = Ante zaplatené: { $amount }.
draw-betting-round-1 = Kolo stávkovania.
draw-betting-round-2 = Kolo stávkovania.
draw-begin-draw = Fáza výmeny.
draw-not-draw-phase = Teraz nie je čas na výmenu.
draw-not-betting = Nemôžete staviť počas fázy výmeny.

draw-toggle-discard = Prepnúť zahadzovanie pre kartu { $index }
draw-card-keep = { $card }, ponechaná
draw-card-discard = { $card }, bude zahadzaná
draw-card-kept = Ponecháte { $card }.
draw-card-discarded = Zahadíte { $card }.
draw-draw-cards = Ťaháte karty
draw-draw-cards-count = Ťaháte { $count } { $count ->
    [one] kartu
    [few] karty
    [many] kariet
   *[other] kariet
}
draw-dealt-cards = Dostávate { $cards }.
draw-you-drew-cards = Ťaháte { $cards }.
draw-you-draw = Ťaháte { $count } { $count ->
    [one] kartu
    [few] karty
    [many] kariet
   *[other] kariet
}.
draw-player-draws = { $player } ťahá { $count } { $count ->
    [one] kartu
    [few] karty
    [many] kariet
   *[other] kariet
}.
draw-you-stand-pat = Zostávate.
draw-player-stands-pat = { $player } zostáva.
draw-you-discard-limit = Môžete zahadiť až { $count } kariet.
draw-player-discard-limit = { $player } môže zahadiť až { $count } kariet.
