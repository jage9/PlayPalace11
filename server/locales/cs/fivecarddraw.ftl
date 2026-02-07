# Five Card Draw - České zprávy hry

game-name-fivecarddraw = Five Card Draw

draw-set-starting-chips = Počáteční žetony: { $count }
draw-enter-starting-chips = Zadejte počáteční žetony
draw-option-changed-starting-chips = Počáteční žetony nastaveny na { $count }.

draw-set-ante = Ante: { $count }
draw-enter-ante = Zadejte výši ante
draw-option-changed-ante = Ante nastaveno na { $count }.

draw-set-turn-timer = Časovač tahu: { $mode }
draw-select-turn-timer = Vyberte časovač tahu
draw-option-changed-turn-timer = Časovač tahu nastaven na { $mode }.

draw-set-raise-mode = Režim přihazování: { $mode }
draw-select-raise-mode = Vyberte režim přihazování
draw-option-changed-raise-mode = Režim přihazování nastaven na { $mode }.

draw-set-max-raises = Maximum přihození: { $count }
draw-enter-max-raises = Zadejte maximum přihození (0 pro neomezené)
draw-option-changed-max-raises = Maximum přihození nastaveno na { $count }.

draw-antes-posted = Ante zaplaceno: { $amount }.
draw-betting-round-1 = Kolo sázení.
draw-betting-round-2 = Kolo sázení.
draw-begin-draw = Fáze výměny.
draw-not-draw-phase = Ještě není čas na výměnu.
draw-not-betting = Nemůžete sázet během fáze výměny.

draw-toggle-discard = Přepnout odhození karty { $index }
draw-card-keep = { $card }, drženo
draw-card-discard = { $card }, bude odhozeno
draw-card-kept = Držet { $card }.
draw-card-discarded = Odhodit { $card }.
draw-draw-cards = Líznout karty
draw-draw-cards-count = Líznout { $count } { $count ->
    [one] kartu
    [few] karty
    [many] karty
   *[other] karet
}
draw-dealt-cards = Bylo vám rozdáno { $cards }.
draw-you-drew-cards = Líznete { $cards }.
draw-you-draw = Líznete { $count } { $count ->
    [one] kartu
    [few] karty
    [many] karty
   *[other] karet
}.
draw-player-draws = { $player } lízne { $count } { $count ->
    [one] kartu
    [few] karty
    [many] karty
   *[other] karet
}.
draw-you-stand-pat = Stojíte.
draw-player-stands-pat = { $player } stojí.
draw-you-discard-limit = Můžete odhodit až { $count } karet.
draw-player-discard-limit = { $player } může odhodit až { $count } karet.
