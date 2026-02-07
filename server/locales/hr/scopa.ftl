# Scopa game messages
# Note: Common messages like round-start, turn-start, target-score, team-mode are in games.ftl

# Game name
game-name-scopa = Scopa

# Game events
scopa-initial-table = Karte na stolu: { $cards }
scopa-no-initial-table = Nema karata na stolu za početak.
scopa-you-collect = Skupljate { $cards } sa { $card }
scopa-player-collects = { $player } skuplja { $cards } sa { $card }
scopa-you-put-down = Stavljate { $card }.
scopa-player-puts-down = { $player } stavlja { $card }.
scopa-scopa-suffix =  - SCOPA!
scopa-clear-table-suffix = , čisteći stol.
scopa-remaining-cards = { $player } dobiva preostale karte sa stola.
scopa-scoring-round = Bodovanje runde...
scopa-most-cards = { $player } dobiva 1 bod za najviše karata ({ $count } karata).
scopa-most-cards-tie = Najviše karata je neriješeno - bod se ne dodjeljuje.
scopa-most-diamonds = { $player } dobiva 1 bod za najviše kara ({ $count } kara).
scopa-most-diamonds-tie = Najviše kara je neriješeno - bod se ne dodjeljuje.
scopa-seven-diamonds = { $player } dobiva 1 bod za sedmicu kara.
scopa-seven-diamonds-multi = { $player } dobiva 1 bod za najviše sedmica kara ({ $count } × sedmica kara).
scopa-seven-diamonds-tie = Sedmica kara je neriješeno - bod se ne dodjeljuje.
scopa-most-sevens = { $player } dobiva 1 bod za najviše sedmica ({ $count } sedmica).
scopa-most-sevens-tie = Najviše sedmica je neriješeno - bod se ne dodjeljuje.
scopa-round-scores = Rezultati runde:
scopa-round-score-line = { $player }: +{ $round_score } (ukupno: { $total_score })
scopa-table-empty = Nema karata na stolu.
scopa-no-such-card = Nema karte na toj poziciji.
scopa-captured-count = Uhvatili ste { $count } karata

# View actions
scopa-view-table = Pogledaj stol
scopa-view-captured = Pogledaj uhvaćene

# Scopa-specific options
scopa-enter-target-score = Unesite cilj bodova (1-121)
scopa-set-cards-per-deal = Karte po dijeljenju: { $cards }
scopa-enter-cards-per-deal = Unesite karte po dijeljenju (1-10)
scopa-set-decks = Broj špilova: { $decks }
scopa-enter-decks = Unesite broj špilova (1-6)
scopa-toggle-escoba = Escoba (zbroj do 15): { $enabled }
scopa-toggle-hints = Pokaži savjete za hvatanje: { $enabled }
scopa-set-mechanic = Scopa mehanika: { $mechanic }
scopa-select-mechanic = Odaberite scopa mehaniku
scopa-toggle-instant-win = Trenutna pobjeda na scopa: { $enabled }
scopa-toggle-team-scoring = Zajednički tim kartice za bodovanje: { $enabled }
scopa-toggle-inverse = Inverzni mod (dosezanje cilja = eliminacija): { $enabled }

# Option change announcements
scopa-option-changed-cards = Karte po dijeljenju postavljene na { $cards }.
scopa-option-changed-decks = Broj špilova postavljen na { $decks }.
scopa-option-changed-escoba = Escoba { $enabled }.
scopa-option-changed-hints = Savjeti za hvatanje { $enabled }.
scopa-option-changed-mechanic = Scopa mehanika postavljena na { $mechanic }.
scopa-option-changed-instant = Trenutna pobjeda na scopa { $enabled }.
scopa-option-changed-team-scoring = Bodovanje timskih karata { $enabled }.
scopa-option-changed-inverse = Inverzni mod { $enabled }.

# Scopa mechanic choices
scopa-mechanic-normal = Normalno
scopa-mechanic-no_scopas = Bez Scopa
scopa-mechanic-only_scopas = Samo Scope

# Disabled action reasons
scopa-timer-not-active = Mjerač vremena runde nije aktivan.

# Validation errors
scopa-error-not-enough-cards = Nema dovoljno karata u { $decks } { $decks ->
    [one] špilu
    *[other] špilova
} za { $players } { $players ->
    [one] igrača
    *[other] igrača
} sa { $cards_per_deal } karata svaki. (Potrebno { $cards_per_deal } × { $players } = { $cards_needed } karata, ali ima samo { $total_cards }.)
