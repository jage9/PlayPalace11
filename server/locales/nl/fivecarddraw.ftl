# Five Card Draw

game-name-fivecarddraw = Five Card Draw

draw-set-starting-chips = Startchips: { $count }
draw-enter-starting-chips = Voer startchips in
draw-option-changed-starting-chips = Startchips ingesteld op { $count }.

draw-set-ante = Ante: { $count }
draw-enter-ante = Voer ante bedrag in
draw-option-changed-ante = Ante ingesteld op { $count }.

draw-set-turn-timer = Beurttimer: { $mode }
draw-select-turn-timer = Selecteer beurttimer
draw-option-changed-turn-timer = Beurttimer ingesteld op { $mode }.

draw-set-raise-mode = Verhoogmodus: { $mode }
draw-select-raise-mode = Selecteer verhoogmodus
draw-option-changed-raise-mode = Verhoogmodus ingesteld op { $mode }.

draw-set-max-raises = Max verhogingen: { $count }
draw-enter-max-raises = Voer max verhogingen in (0 voor onbeperkt)
draw-option-changed-max-raises = Max verhogingen ingesteld op { $count }.

draw-antes-posted = Antes geplaatst: { $amount }.
draw-betting-round-1 = Wedronde.
draw-betting-round-2 = Wedronde.
draw-begin-draw = Trekfase.
draw-not-draw-phase = Het is geen tijd om te trekken.
draw-not-betting = Je kunt niet wedden tijdens de trekfase.

draw-toggle-discard = Schakel weggooien voor kaart { $index }
draw-card-keep = { $card }, vastgehouden
draw-card-discard = { $card }, wordt weggegooid
draw-card-kept = { $card } houden.
draw-card-discarded = { $card } weggooien.
draw-draw-cards = Trek kaarten
draw-draw-cards-count = Trek { $count } { $count ->
    [one] kaart
   *[other] kaarten
}
draw-dealt-cards = Je krijgt { $cards } gedeeld.
draw-you-drew-cards = Je trekt { $cards }.
draw-you-draw = Je trekt { $count } { $count ->
    [one] kaart
   *[other] kaarten
}.
draw-player-draws = { $player } trekt { $count } { $count ->
    [one] kaart
   *[other] kaarten
}.
draw-you-stand-pat = Je staat pat.
draw-player-stands-pat = { $player } staat pat.
draw-you-discard-limit = Je mag tot { $count } kaarten weggooien.
draw-player-discard-limit = { $player } mag tot { $count } kaarten weggooien.
