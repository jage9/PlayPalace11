# Five Card Draw

game-name-fivecarddraw = Five Card Draw

draw-set-starting-chips = Starting chips: { $count }
draw-enter-starting-chips = Enter starting chips
draw-option-changed-starting-chips = Starting chips set to { $count }.

draw-set-ante = Ante: { $count }
draw-enter-ante = Enter ante amount
draw-option-changed-ante = Ante set to { $count }.

draw-set-turn-timer = Turn timer: { $mode }
draw-select-turn-timer = Select turn timer
draw-option-changed-turn-timer = Turn timer set to { $mode }.

draw-set-raise-mode = Raise mode: { $mode }
draw-select-raise-mode = Select raise mode
draw-option-changed-raise-mode = Raise mode set to { $mode }.

draw-set-max-raises = Max raises: { $count }
draw-enter-max-raises = Enter max raises (0 for unlimited)
draw-option-changed-max-raises = Max raises set to { $count }.

draw-antes-posted = Antes posted: { $amount }.
draw-betting-round-1 = Betting round.
draw-betting-round-2 = Betting round.
draw-begin-draw = Draw phase.
draw-not-draw-phase = Não é hora de comprar cartas.
draw-not-betting = Você não pode apostar durante a fase de troca.

draw-toggle-discard = Toggle discard for card { $index }
draw-card-keep = { $card }, mantida
draw-card-discard = { $card }, será descartada
draw-card-kept = Manter { $card }.
draw-card-discarded = Descartar { $card }.
draw-draw-cards = Draw cards
draw-draw-cards-count = Draw { $count } { $count ->
    [one] card
   *[other] cards
}
draw-dealt-cards = You are dealt { $cards }.
draw-you-drew-cards = Você compra { $cards }.
draw-you-draw = You draw { $count } { $count ->
    [one] card
   *[other] cards
}.
draw-player-draws = { $player } draws { $count } { $count ->
    [one] card
   *[other] cards
}.
draw-you-stand-pat = You stand pat.
draw-player-stands-pat = { $player } stands pat.
draw-you-discard-limit = You may discard up to { $count } cards.
draw-player-discard-limit = { $player } may discard up to { $count } cards.
