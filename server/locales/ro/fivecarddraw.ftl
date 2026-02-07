# Five Card Draw

game-name-fivecarddraw = Poker cu Cinci Cărți

draw-set-starting-chips = Jetoane inițiale: { $count }
draw-enter-starting-chips = Introduceți jetoanele inițiale
draw-option-changed-starting-chips = Jetoanele inițiale setate la { $count }.

draw-set-ante = Ante: { $count }
draw-enter-ante = Introduceți suma ante
draw-option-changed-ante = Ante setat la { $count }.

draw-set-turn-timer = Temporizator tură: { $mode }
draw-select-turn-timer = Selectați temporizatorul de tură
draw-option-changed-turn-timer = Temporizator tură setat la { $mode }.

draw-set-raise-mode = Mod de ridicare: { $mode }
draw-select-raise-mode = Selectați modul de ridicare
draw-option-changed-raise-mode = Mod de ridicare setat la { $mode }.

draw-set-max-raises = Ridicări maxime: { $count }
draw-enter-max-raises = Introduceți ridicările maxime (0 pentru nelimitat)
draw-option-changed-max-raises = Ridicări maxime setate la { $count }.

draw-antes-posted = Ante-uri postate: { $amount }.
draw-betting-round-1 = Rundă de pariuri.
draw-betting-round-2 = Rundă de pariuri.
draw-begin-draw = Faza de schimb.
draw-not-draw-phase = Nu este timpul să schimbați cărți.
draw-not-betting = Nu puteți paria în timpul fazei de schimb.

draw-toggle-discard = Comutați aruncarea pentru cartea { $index }
draw-card-keep = { $card }, păstrată
draw-card-discard = { $card }, va fi aruncată
draw-card-kept = Păstrați { $card }.
draw-card-discarded = Aruncați { $card }.
draw-draw-cards = Trageți cărți
draw-draw-cards-count = Trageți { $count } { $count ->
    [one] carte
    [few] cărți
   *[other] de cărți
}
draw-dealt-cards = Primiți { $cards }.
draw-you-drew-cards = Trageți { $cards }.
draw-you-draw = Trageți { $count } { $count ->
    [one] carte
    [few] cărți
   *[other] de cărți
}.
draw-player-draws = { $player } trage { $count } { $count ->
    [one] carte
    [few] cărți
   *[other] de cărți
}.
draw-you-stand-pat = Stați așa.
draw-player-stands-pat = { $player } stă așa.
draw-you-discard-limit = Puteți arunca până la { $count } cărți.
draw-player-discard-limit = { $player } poate arunca până la { $count } cărți.
