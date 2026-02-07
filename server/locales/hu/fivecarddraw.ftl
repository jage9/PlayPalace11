# Five Card Draw

game-name-fivecarddraw = Ötlapos Póker

draw-set-starting-chips = Kezdő zsetonok: { $count }
draw-enter-starting-chips = Adja meg a kezdő zsetonokat
draw-option-changed-starting-chips = Kezdő zsetonok beállítva: { $count }.

draw-set-ante = Tét: { $count }
draw-enter-ante = Adja meg a tét összegét
draw-option-changed-ante = Tét beállítva: { $count }.

draw-set-turn-timer = Körző időzítő: { $mode }
draw-select-turn-timer = Válassza ki a körző időzítőt
draw-option-changed-turn-timer = Körző időzítő beállítva: { $mode }.

draw-set-raise-mode = Emelési mód: { $mode }
draw-select-raise-mode = Válassza ki az emelési módot
draw-option-changed-raise-mode = Emelési mód beállítva: { $mode }.

draw-set-max-raises = Maximum emelések: { $count }
draw-enter-max-raises = Adja meg a maximum emeléseket (0 a korlátlanhoz)
draw-option-changed-max-raises = Maximum emelések beállítva: { $count }.

draw-antes-posted = Tétek feltéve: { $amount }.
draw-betting-round-1 = Fogadási kör.
draw-betting-round-2 = Fogadási kör.
draw-begin-draw = Csere fázis.
draw-not-draw-phase = Most nem lehet cserélni.
draw-not-betting = Nem fogadhat a csere fázisban.

draw-toggle-discard = Dobás váltása a { $index } kártyára
draw-card-keep = { $card }, megtartva
draw-card-discard = { $card }, eldobásra kerül
draw-card-kept = Megtartja: { $card }.
draw-card-discarded = Eldobja: { $card }.
draw-draw-cards = Kártyák húzása
draw-draw-cards-count = { $count } kártya { $count ->
    [one] húzása
   *[other] húzása
}
draw-dealt-cards = Kapott kártyák: { $cards }.
draw-you-drew-cards = Kártyákat húz: { $cards }.
draw-you-draw = { $count } kártyát { $count ->
    [one] húz
   *[other] húz
}.
draw-player-draws = { $player } { $count } kártyát { $count ->
    [one] húz
   *[other] húz
}.
draw-you-stand-pat = Nem cserél.
draw-player-stands-pat = { $player } nem cserél.
draw-you-discard-limit = Legfeljebb { $count } kártyát dobhat el.
draw-player-discard-limit = { $player } legfeljebb { $count } kártyát dobhat el.
