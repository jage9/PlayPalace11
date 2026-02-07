# Ninety Nine - English Localization
# Messages match v10 exactly

# Game info
ninetynine-name = Novantanove
ninetynine-description = Un gioco di carte dove i giocatori cercano di evitare di superare il totale di 99. Vince l'ultimo giocatore rimasto!

# Round
ninetynine-round = Round { $round }.

# Turn
ninetynine-player-turn = Turno di { $player }.

# Playing cards - match v10 exactly
ninetynine-you-play = Giochi { $card }. Il conteggio è ora { $count }.
ninetynine-player-plays = { $player } gioca { $card }. Il conteggio è ora { $count }.

# Direction reverse
ninetynine-direction-reverses = La direzione di gioco si inverte!

# Skip
ninetynine-player-skipped = { $player } viene saltato.

# Token loss - match v10 exactly
ninetynine-you-lose-tokens = Perdi { $amount } { $amount ->
    [one] gettone
   *[other] gettoni
}.
ninetynine-player-loses-tokens = { $player } perde { $amount } { $amount ->
    [one] gettone
   *[other] gettoni
}.

# Elimination
ninetynine-player-eliminated = { $player } è stato eliminato!

# Game end
ninetynine-player-wins = { $player } vince il gioco!

# Dealing
ninetynine-you-deal = Distribuisci le carte.
ninetynine-player-deals = { $player } distribuisce le carte.

# Drawing cards
ninetynine-you-draw = Peschi { $card }.
ninetynine-player-draws = { $player } pesca una carta.

# No valid cards
ninetynine-no-valid-cards = { $player } non ha carte che non superino 99!

# Status - for C key
ninetynine-current-count = Il conteggio è { $count }.

# Hand check - for H key
ninetynine-hand-cards = Le tue carte: { $cards }.
ninetynine-hand-empty = Non hai carte.

# Ace choice
ninetynine-ace-choice = Gioca l'Asso come +1 o +11?
ninetynine-ace-add-eleven = Aggiungi 11
ninetynine-ace-add-one = Aggiungi 1

# Ten choice
ninetynine-ten-choice = Gioca il 10 come +10 o -10?
ninetynine-ten-add = Aggiungi 10
ninetynine-ten-subtract = Sottrai 10

# Manual draw
ninetynine-draw-card = Pesca carta
ninetynine-draw-prompt = Premi Spazio o D per pescare una carta.

# Options
ninetynine-set-tokens = Gettoni iniziali: { $tokens }
ninetynine-enter-tokens = Inserisci il numero di gettoni iniziali:
ninetynine-option-changed-tokens = Gettoni iniziali impostati a { $tokens }.
ninetynine-set-rules = Variante delle regole: { $rules }
ninetynine-select-rules = Seleziona variante delle regole
ninetynine-option-changed-rules = Variante delle regole impostata a { $rules }.
ninetynine-set-hand-size = Dimensione della mano: { $size }
ninetynine-enter-hand-size = Inserisci dimensione della mano:
ninetynine-option-changed-hand-size = Dimensione della mano impostata a { $size }.
ninetynine-set-autodraw = Pesca automatica: { $enabled }
ninetynine-option-changed-autodraw = Pesca automatica impostata a { $enabled }.

# Rules variant announcements (shown at game start)
ninetynine-rules-quentin = Regole Quentin C.
ninetynine-rules-rsgames = Regole RS Games.

# Rules variant choices (for menu display)
ninetynine-rules-variant-quentin_c = Quentin C
ninetynine-rules-variant-rs_games = RS Games

# Disabled action reasons
ninetynine-choose-first = Devi prima fare una scelta.
ninetynine-draw-first = Devi prima pescare una carta.
