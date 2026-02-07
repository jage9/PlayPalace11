# Scopa game messages
# Note: Common messages like round-start, turn-start, target-score, team-mode are in games.ftl

# Game name
game-name-scopa = Scopa

# Game events
scopa-initial-table = Cărți pe masă: { $cards }
scopa-no-initial-table = Nu sunt cărți pe masă la început.
scopa-you-collect = Colectezi { $cards } cu { $card }
scopa-player-collects = { $player } colectează { $cards } cu { $card }
scopa-you-put-down = Pui { $card }.
scopa-player-puts-down = { $player } pune { $card }.
scopa-scopa-suffix =  - SCOPA!
scopa-clear-table-suffix = , curățând masa.
scopa-remaining-cards = { $player } primește cărțile rămase de pe masă.
scopa-scoring-round = Punctarea rundei...
scopa-most-cards = { $player } primește 1 punct pentru cele mai multe cărți ({ $count } cărți).
scopa-most-cards-tie = Cele mai multe cărți este egalitate - nu se acordă punct.
scopa-most-diamonds = { $player } primește 1 punct pentru cele mai multe caro ({ $count } caro).
scopa-most-diamonds-tie = Cele mai multe caro este egalitate - nu se acordă punct.
scopa-seven-diamonds = { $player } primește 1 punct pentru 7 de caro.
scopa-seven-diamonds-multi = { $player } primește 1 punct pentru cele mai multe 7 de caro ({ $count } × 7 de caro).
scopa-seven-diamonds-tie = 7 de caro este egalitate - nu se acordă punct.
scopa-most-sevens = { $player } primește 1 punct pentru cele mai multe șepte ({ $count } șepte).
scopa-most-sevens-tie = Cele mai multe șepte este egalitate - nu se acordă punct.
scopa-round-scores = Scoruri runde:
scopa-round-score-line = { $player }: +{ $round_score } (total: { $total_score })
scopa-table-empty = Nu sunt cărți pe masă.
scopa-no-such-card = Nu există carte la acea poziție.
scopa-captured-count = Ai captat { $count } cărți

# View actions
scopa-view-table = Vezi masa
scopa-view-captured = Vezi captate

# Scopa-specific options
scopa-enter-target-score = Introdu scorul țintă (1-121)
scopa-set-cards-per-deal = Cărți pe împărțire: { $cards }
scopa-enter-cards-per-deal = Introdu cărți pe împărțire (1-10)
scopa-set-decks = Număr de pachete: { $decks }
scopa-enter-decks = Introdu numărul de pachete (1-6)
scopa-toggle-escoba = Escoba (sumă până la 15): { $enabled }
scopa-toggle-hints = Arată indicii de captare: { $enabled }
scopa-set-mechanic = Mecanică scopa: { $mechanic }
scopa-select-mechanic = Selectează mecanică scopa
scopa-toggle-instant-win = Victorie instantanee la scopa: { $enabled }
scopa-toggle-team-scoring = Grupează cărțile echipei pentru punctare: { $enabled }
scopa-toggle-inverse = Mod invers (atingerea țintei = eliminare): { $enabled }

# Option change announcements
scopa-option-changed-cards = Cărți pe împărțire setate la { $cards }.
scopa-option-changed-decks = Număr de pachete setat la { $decks }.
scopa-option-changed-escoba = Escoba { $enabled }.
scopa-option-changed-hints = Indicii de captare { $enabled }.
scopa-option-changed-mechanic = Mecanică scopa setată la { $mechanic }.
scopa-option-changed-instant = Victorie instantanee la scopa { $enabled }.
scopa-option-changed-team-scoring = Punctare cărți echipă { $enabled }.
scopa-option-changed-inverse = Mod invers { $enabled }.

# Scopa mechanic choices
scopa-mechanic-normal = Normal
scopa-mechanic-no_scopas = Fără Scope
scopa-mechanic-only_scopas = Doar Scope

# Disabled action reasons
scopa-timer-not-active = Cronometrul rundei nu este activ.

# Validation errors
scopa-error-not-enough-cards = Nu sunt destule cărți în { $decks } { $decks ->
    [one] pachet
    [few] pachete
    *[other] de pachete
} pentru { $players } { $players ->
    [one] jucător
    [few] jucători
    *[other] de jucători
} cu { $cards_per_deal } cărți fiecare. (Necesare { $cards_per_deal } × { $players } = { $cards_needed } cărți, dar sunt doar { $total_cards }.)
