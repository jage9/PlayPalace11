# Five Card Draw

game-name-fivecarddraw = Pet Karata

draw-set-starting-chips = Početni žetoni: { $count }
draw-enter-starting-chips = Unesite početne žetone
draw-option-changed-starting-chips = Početni žetoni postavljeni na { $count }.

draw-set-ante = Ulazni ulog: { $count }
draw-enter-ante = Unesite iznos ulaznog uloga
draw-option-changed-ante = Ulazni ulog postavljen na { $count }.

draw-set-turn-timer = Mjerač vremena: { $mode }
draw-select-turn-timer = Odaberite mjerač vremena
draw-option-changed-turn-timer = Mjerač vremena postavljen na { $mode }.

draw-set-raise-mode = Način povećanja: { $mode }
draw-select-raise-mode = Odaberite način povećanja
draw-option-changed-raise-mode = Način povećanja postavljen na { $mode }.

draw-set-max-raises = Maksimalno povećanja: { $count }
draw-enter-max-raises = Unesite maksimalno povećanja (0 za neograničeno)
draw-option-changed-max-raises = Maksimalno povećanja postavljeno na { $count }.

draw-antes-posted = Ulazni ulozi postavljeni: { $amount }.
draw-betting-round-1 = Runda klađenja.
draw-betting-round-2 = Runda klađenja.
draw-begin-draw = Faza izvlačenja.
draw-not-draw-phase = Nije vrijeme za izvlačenje.
draw-not-betting = Ne možete se kladiti tijekom faze izvlačenja.

draw-toggle-discard = Prebaci odbacivanje za kartu { $index }
draw-card-keep = { $card }, zadržano
draw-card-discard = { $card }, bit će odbačeno
draw-card-kept = Zadržite { $card }.
draw-card-discarded = Odbacite { $card }.
draw-draw-cards = Izvucite karte
draw-draw-cards-count = Izvucite { $count } { $count ->
    [one] kartu
   *[other] karata
}
draw-dealt-cards = Dobivate { $cards }.
draw-you-drew-cards = Izvlačite { $cards }.
draw-you-draw = Izvlačite { $count } { $count ->
    [one] kartu
   *[other] karata
}.
draw-player-draws = { $player } izvlači { $count } { $count ->
    [one] kartu
   *[other] karata
}.
draw-you-stand-pat = Stojite.
draw-player-stands-pat = { $player } stoji.
draw-you-discard-limit = Možete odbaciti do { $count } karata.
draw-player-discard-limit = { $player } može odbaciti do { $count } karata.
