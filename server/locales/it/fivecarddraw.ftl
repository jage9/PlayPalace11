# Five Card Draw

game-name-fivecarddraw = Poker a Cinque Carte

draw-set-starting-chips = Fiches iniziali: { $count }
draw-enter-starting-chips = Inserisci fiches iniziali
draw-option-changed-starting-chips = Fiches iniziali impostate a { $count }.

draw-set-ante = Ante: { $count }
draw-enter-ante = Inserisci importo dell'ante
draw-option-changed-ante = Ante impostato a { $count }.

draw-set-turn-timer = Timer di turno: { $mode }
draw-select-turn-timer = Seleziona timer di turno
draw-option-changed-turn-timer = Timer di turno impostato a { $mode }.

draw-set-raise-mode = Modalità rilancio: { $mode }
draw-select-raise-mode = Seleziona modalità rilancio
draw-option-changed-raise-mode = Modalità rilancio impostata a { $mode }.

draw-set-max-raises = Rilanci massimi: { $count }
draw-enter-max-raises = Inserisci rilanci massimi (0 per illimitati)
draw-option-changed-max-raises = Rilanci massimi impostati a { $count }.

draw-antes-posted = Ante piazzate: { $amount }.
draw-betting-round-1 = Giro di puntate.
draw-betting-round-2 = Giro di puntate.
draw-begin-draw = Fase di cambio.
draw-not-draw-phase = Non è il momento di cambiare.
draw-not-betting = Non puoi puntare durante la fase di cambio.

draw-toggle-discard = Attiva/disattiva scarto per carta { $index }
draw-card-keep = { $card }, tenuta
draw-card-discard = { $card }, verrà scartata
draw-card-kept = Tieni { $card }.
draw-card-discarded = Scarta { $card }.
draw-draw-cards = Pesca carte
draw-draw-cards-count = Pesca { $count } { $count ->
    [one] carta
   *[other] carte
}
draw-dealt-cards = Ricevi { $cards }.
draw-you-drew-cards = Peschi { $cards }.
draw-you-draw = Peschi { $count } { $count ->
    [one] carta
   *[other] carte
}.
draw-player-draws = { $player } pesca { $count } { $count ->
    [one] carta
   *[other] carte
}.
draw-you-stand-pat = Stai servito.
draw-player-stands-pat = { $player } sta servito.
draw-you-discard-limit = Puoi scartare fino a { $count } carte.
draw-player-discard-limit = { $player } può scartare fino a { $count } carte.
