# Five Card Draw

game-name-fivecarddraw = Femkorts Dragpoker

draw-set-starting-chips = Startmarker: { $count }
draw-enter-starting-chips = Ange startmarker
draw-option-changed-starting-chips = Startmarker inställda på { $count }.

draw-set-ante = Ante: { $count }
draw-enter-ante = Ange ante-belopp
draw-option-changed-ante = Ante inställd på { $count }.

draw-set-turn-timer = Turtimer: { $mode }
draw-select-turn-timer = Välj turtimer
draw-option-changed-turn-timer = Turtimer inställd på { $mode }.

draw-set-raise-mode = Höjningsläge: { $mode }
draw-select-raise-mode = Välj höjningsläge
draw-option-changed-raise-mode = Höjningsläge inställt på { $mode }.

draw-set-max-raises = Max höjningar: { $count }
draw-enter-max-raises = Ange max höjningar (0 för obegränsat)
draw-option-changed-max-raises = Max höjningar inställda på { $count }.

draw-antes-posted = Ante-insatser lagda: { $amount }.
draw-betting-round-1 = Satsningsrunda.
draw-betting-round-2 = Satsningsrunda.
draw-begin-draw = Bytfas.
draw-not-draw-phase = Det är inte dags att byta kort.
draw-not-betting = Du kan inte satsa under bytfasen.

draw-toggle-discard = Växla kasta för kort { $index }
draw-card-keep = { $card }, behålls
draw-card-discard = { $card }, kommer kastas
draw-card-kept = Behåll { $card }.
draw-card-discarded = Kasta { $card }.
draw-draw-cards = Dra kort
draw-draw-cards-count = Dra { $count } { $count ->
    [one] kort
   *[other] kort
}
draw-dealt-cards = Du får { $cards }.
draw-you-drew-cards = Du drar { $cards }.
draw-you-draw = Du drar { $count } { $count ->
    [one] kort
   *[other] kort
}.
draw-player-draws = { $player } drar { $count } { $count ->
    [one] kort
   *[other] kort
}.
draw-you-stand-pat = Du står.
draw-player-stands-pat = { $player } står.
draw-you-discard-limit = Du kan kasta upp till { $count } kort.
draw-player-discard-limit = { $player } kan kasta upp till { $count } kort.
