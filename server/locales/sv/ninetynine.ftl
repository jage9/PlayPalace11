# Ninety Nine - English Localization
# Messages match v10 exactly

# Game info
ninetynine-name = Nittionio
ninetynine-description = Ett kortspel där spelare försöker undvika att driva den löpande summan över 99. Sista spelaren kvar vinner!

# Round
ninetynine-round = Runda { $round }.

# Turn
ninetynine-player-turn = { $player }s tur.

# Playing cards - match v10 exactly
ninetynine-you-play = Du spelar { $card }. Räkningen är nu { $count }.
ninetynine-player-plays = { $player } spelar { $card }. Räkningen är nu { $count }.

# Direction reverse
ninetynine-direction-reverses = Spelets riktning vänds!

# Skip
ninetynine-player-skipped = { $player } hoppas över.

# Token loss - match v10 exactly
ninetynine-you-lose-tokens = Du förlorar { $amount } { $amount ->
    [one] pollert
   *[other] pollettar
}.
ninetynine-player-loses-tokens = { $player } förlorar { $amount } { $amount ->
    [one] pollert
   *[other] pollettar
}.

# Elimination
ninetynine-player-eliminated = { $player } har blivit utslagen!

# Game end
ninetynine-player-wins = { $player } vinner spelet!

# Dealing
ninetynine-you-deal = Du ger ut korten.
ninetynine-player-deals = { $player } ger ut korten.

# Drawing cards
ninetynine-you-draw = Du drar { $card }.
ninetynine-player-draws = { $player } drar ett kort.

# No valid cards
ninetynine-no-valid-cards = { $player } har inga kort som inte går över 99!

# Status - for C key
ninetynine-current-count = Räkningen är { $count }.

# Hand check - for H key
ninetynine-hand-cards = Dina kort: { $cards }.
ninetynine-hand-empty = Du har inga kort.

# Ace choice
ninetynine-ace-choice = Spela ess som +1 eller +11?
ninetynine-ace-add-eleven = Lägg till 11
ninetynine-ace-add-one = Lägg till 1

# Ten choice
ninetynine-ten-choice = Spela 10 som +10 eller -10?
ninetynine-ten-add = Lägg till 10
ninetynine-ten-subtract = Subtrahera 10

# Manual draw
ninetynine-draw-card = Dra kort
ninetynine-draw-prompt = Tryck mellanslag eller D för att dra ett kort.

# Options
ninetynine-set-tokens = Startpollettar: { $tokens }
ninetynine-enter-tokens = Ange antal startpollettar:
ninetynine-option-changed-tokens = Startpollettar inställda på { $tokens }.
ninetynine-set-rules = Regelvariant: { $rules }
ninetynine-select-rules = Välj regelvariant
ninetynine-option-changed-rules = Regelvariant inställd på { $rules }.
ninetynine-set-hand-size = Handstorlek: { $size }
ninetynine-enter-hand-size = Ange handstorlek:
ninetynine-option-changed-hand-size = Handstorlek inställd på { $size }.
ninetynine-set-autodraw = Automatisk dragning: { $enabled }
ninetynine-option-changed-autodraw = Automatisk dragning inställd på { $enabled }.

# Rules variant announcements (shown at game start)
ninetynine-rules-quentin = Quentin C-regler.
ninetynine-rules-rsgames = RS Games-regler.

# Rules variant choices (for menu display)
ninetynine-rules-variant-quentin_c = Quentin C
ninetynine-rules-variant-rs_games = RS Games

# Disabled action reasons
ninetynine-choose-first = Du måste göra ett val först.
ninetynine-draw-first = Du måste dra ett kort först.
