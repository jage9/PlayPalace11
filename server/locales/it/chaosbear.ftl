# Chaos Bear game messages

# Game name
game-name-chaosbear = Orso Caotico

# Actions
chaosbear-roll-dice = Tira i dadi
chaosbear-draw-card = Pesca una carta
chaosbear-check-status = Controlla stato

# Game intro (3 separate messages like v10)
chaosbear-intro-1 = L'Orso Caotico è iniziato! Tutti i giocatori iniziano 30 caselle davanti all'orso.
chaosbear-intro-2 = Tira i dadi per muoverti avanti e pesca carte sui multipli di 5 per ottenere effetti speciali.
chaosbear-intro-3 = Non farti prendere dall'orso!

# Turn announcement
chaosbear-turn = Turno di { $player }; casella { $position }.

# Rolling
chaosbear-roll = { $player } ha tirato { $roll }.
chaosbear-position = { $player } è ora alla casella { $position }.

# Drawing cards
chaosbear-draws-card = { $player } pesca una carta.
chaosbear-card-impulsion = Impulso! { $player } si muove avanti di 3 caselle alla casella { $position }!
chaosbear-card-super-impulsion = Super impulso! { $player } si muove avanti di 5 caselle alla casella { $position }!
chaosbear-card-tiredness = Stanchezza! Energia dell'orso meno 1. Ora ha { $energy } energia.
chaosbear-card-hunger = Fame! Energia dell'orso più 1. Ora ha { $energy } energia.
chaosbear-card-backward = Spinta indietro! { $player } torna alla casella { $position }.
chaosbear-card-random-gift = Regalo casuale!
chaosbear-gift-back = { $player } è tornato alla casella { $position }.
chaosbear-gift-forward = { $player } è andato avanti alla casella { $position }!

# Bear turn
chaosbear-bear-roll = L'orso ha tirato { $roll } + la sua { $energy } energia = { $total }.
chaosbear-bear-energy-up = L'orso ha tirato 3 e guadagnato 1 energia!
chaosbear-bear-position = L'orso è ora alla casella { $position }!
chaosbear-player-caught = L'orso ha preso { $player }! { $player } è stato sconfitto!
chaosbear-bear-feast = L'orso perde 3 energia dopo aver banchettato con la loro carne!

# Status check
chaosbear-status-player-alive = { $player }: casella { $position }.
chaosbear-status-player-caught = { $player }: preso alla casella { $position }.
chaosbear-status-bear = L'orso è alla casella { $position } con { $energy } energia.

# End game
chaosbear-winner = { $player } è sopravvissuto e vince! Ha raggiunto la casella { $position }!
chaosbear-tie = È un pareggio alla casella { $position }!

# Disabled action reasons
chaosbear-you-are-caught = Sei stato preso dall'orso.
chaosbear-not-on-multiple = Puoi pescare carte solo sui multipli di 5.
