# Ninety Nine - English Localization
# Messages match v10 exactly

# Game info
ninetynine-name = Devedeset Devet
ninetynine-description = Kartaška igra gdje igrači pokušavaju izbjeći da ukupni zbroj pređe 99. Posljednji igrač preživjeli pobjeđuje!

# Round
ninetynine-round = Runda { $round }.

# Turn
ninetynine-player-turn = Red igrača { $player }.

# Playing cards - match v10 exactly
ninetynine-you-play = Igrate { $card }. Zbroj je sada { $count }.
ninetynine-player-plays = { $player } igra { $card }. Zbroj je sada { $count }.

# Direction reverse
ninetynine-direction-reverses = Smjer igre se okreće!

# Skip
ninetynine-player-skipped = { $player } je preskočen.

# Token loss - match v10 exactly
ninetynine-you-lose-tokens = Gubite { $amount } { $amount ->
    [one] žeton
   *[other] žetona
}.
ninetynine-player-loses-tokens = { $player } gubi { $amount } { $amount ->
    [one] žeton
   *[other] žetona
}.

# Elimination
ninetynine-player-eliminated = { $player } je eliminiran!

# Game end
ninetynine-player-wins = { $player } pobjeđuje igru!

# Dealing
ninetynine-you-deal = Vi dijelite karte.
ninetynine-player-deals = { $player } dijeli karte.

# Drawing cards
ninetynine-you-draw = Izvlačite { $card }.
ninetynine-player-draws = { $player } izvlači kartu.

# No valid cards
ninetynine-no-valid-cards = { $player } nema karata koje neće preći 99!

# Status - for C key
ninetynine-current-count = Zbroj je { $count }.

# Hand check - for H key
ninetynine-hand-cards = Vaše karte: { $cards }.
ninetynine-hand-empty = Nemate karata.

# Ace choice
ninetynine-ace-choice = Igrajte as kao +1 ili +11?
ninetynine-ace-add-eleven = Dodaj 11
ninetynine-ace-add-one = Dodaj 1

# Ten choice
ninetynine-ten-choice = Igrajte 10 kao +10 ili -10?
ninetynine-ten-add = Dodaj 10
ninetynine-ten-subtract = Oduzmi 10

# Manual draw
ninetynine-draw-card = Izvuci kartu
ninetynine-draw-prompt = Pritisnite Space ili D za izvlačenje karte.

# Options
ninetynine-set-tokens = Početni žetoni: { $tokens }
ninetynine-enter-tokens = Unesite broj početnih žetona:
ninetynine-option-changed-tokens = Početni žetoni postavljeni na { $tokens }.
ninetynine-set-rules = Varijanta pravila: { $rules }
ninetynine-select-rules = Odaberite varijantu pravila
ninetynine-option-changed-rules = Varijanta pravila postavljena na { $rules }.
ninetynine-set-hand-size = Veličina ruke: { $size }
ninetynine-enter-hand-size = Unesite veličinu ruke:
ninetynine-option-changed-hand-size = Veličina ruke postavljena na { $size }.
ninetynine-set-autodraw = Automatsko izvlačenje: { $enabled }
ninetynine-option-changed-autodraw = Automatsko izvlačenje postavljeno na { $enabled }.

# Rules variant announcements (shown at game start)
ninetynine-rules-quentin = Quentin C pravila.
ninetynine-rules-rsgames = RS Games pravila.

# Rules variant choices (for menu display)
ninetynine-rules-variant-quentin_c = Quentin C
ninetynine-rules-variant-rs_games = RS Games

# Disabled action reasons
ninetynine-choose-first = Morate prvo napraviti izbor.
ninetynine-draw-first = Morate prvo izvući kartu.
