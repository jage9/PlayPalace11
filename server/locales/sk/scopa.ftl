# Scopa game messages
# Note: Common messages like round-start, turn-start, target-score, team-mode are in games.ftl

# Game name
game-name-scopa = Scopa

# Game events
scopa-initial-table = Karty na stole: { $cards }
scopa-no-initial-table = Na stole nie sú žiadne karty na začiatok.
scopa-you-collect = Zbieraš { $cards } s { $card }
scopa-player-collects = { $player } zbiera { $cards } s { $card }
scopa-you-put-down = Položíš { $card }.
scopa-player-puts-down = { $player } položí { $card }.
scopa-scopa-suffix =  - SCOPA!
scopa-clear-table-suffix = , vyčistiac stôl.
scopa-remaining-cards = { $player } dostáva zostávajúce karty zo stola.
scopa-scoring-round = Bodovanie kola...
scopa-most-cards = { $player } získava 1 bod za najviac kariet ({ $count } kariet).
scopa-most-cards-tie = Najviac kariet je remíza - bod sa neudeľuje.
scopa-most-diamonds = { $player } získava 1 bod za najviac káro ({ $count } káro).
scopa-most-diamonds-tie = Najviac káro je remíza - bod sa neudeľuje.
scopa-seven-diamonds = { $player } získava 1 bod za sedmičku káro.
scopa-seven-diamonds-multi = { $player } získava 1 bod za najviac sedmičiek káro ({ $count } × sedmička káro).
scopa-seven-diamonds-tie = Sedmička káro je remíza - bod sa neudeľuje.
scopa-most-sevens = { $player } získava 1 bod za najviac sedmičiek ({ $count } sedmičiek).
scopa-most-sevens-tie = Najviac sedmičiek je remíza - bod sa neudeľuje.
scopa-round-scores = Výsledky kola:
scopa-round-score-line = { $player }: +{ $round_score } (celkovo: { $total_score })
scopa-table-empty = Na stole nie sú žiadne karty.
scopa-no-such-card = Na tej pozícii nie je karta.
scopa-captured-count = Zachytil si { $count } kariet

# View actions
scopa-view-table = Zobraziť stôl
scopa-view-captured = Zobraziť zachytené

# Scopa-specific options
scopa-enter-target-score = Zadaj cieľové skóre (1-121)
scopa-set-cards-per-deal = Karty na rozdanie: { $cards }
scopa-enter-cards-per-deal = Zadaj karty na rozdanie (1-10)
scopa-set-decks = Počet balíčkov: { $decks }
scopa-enter-decks = Zadaj počet balíčkov (1-6)
scopa-toggle-escoba = Escoba (súčet do 15): { $enabled }
scopa-toggle-hints = Zobraziť nápovedy zachytenia: { $enabled }
scopa-set-mechanic = Scopa mechanika: { $mechanic }
scopa-select-mechanic = Vyber scopa mechaniku
scopa-toggle-instant-win = Okamžitá výhra na scopa: { $enabled }
scopa-toggle-team-scoring = Spojiť tímové karty na bodovanie: { $enabled }
scopa-toggle-inverse = Inverzný režim (dosiahnutie cieľa = eliminácia): { $enabled }

# Option change announcements
scopa-option-changed-cards = Karty na rozdanie nastavené na { $cards }.
scopa-option-changed-decks = Počet balíčkov nastavený na { $decks }.
scopa-option-changed-escoba = Escoba { $enabled }.
scopa-option-changed-hints = Nápovedy zachytenia { $enabled }.
scopa-option-changed-mechanic = Scopa mechanika nastavená na { $mechanic }.
scopa-option-changed-instant = Okamžitá výhra na scopa { $enabled }.
scopa-option-changed-team-scoring = Bodovanie tímových kariet { $enabled }.
scopa-option-changed-inverse = Inverzný režim { $enabled }.

# Scopa mechanic choices
scopa-mechanic-normal = Normálny
scopa-mechanic-no_scopas = Bez Scop
scopa-mechanic-only_scopas = Len Scopy

# Disabled action reasons
scopa-timer-not-active = Časovač kola nie je aktívny.

# Validation errors
scopa-error-not-enough-cards = Nie je dosť kariet v { $decks } { $decks ->
    [one] balíčku
    [few] balíčkoch
    [many] balíčka
    *[other] balíčkoch
} pre { $players } { $players ->
    [one] hráča
    [few] hráčov
    [many] hráča
    *[other] hráčov
} s { $cards_per_deal } kartami každý. (Potrebných { $cards_per_deal } × { $players } = { $cards_needed } kariet, ale je len { $total_cards }.)
