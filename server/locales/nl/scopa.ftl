# Scopa game messages
# Note: Common messages like round-start, turn-start, target-score, team-mode are in games.ftl

# Game name
game-name-scopa = Scopa

# Game events
scopa-initial-table = Tafelkaarten: { $cards }
scopa-no-initial-table = Geen kaarten op tafel om te beginnen.
scopa-you-collect = Je verzamelt { $cards } met { $card }
scopa-player-collects = { $player } verzamelt { $cards } met { $card }
scopa-you-put-down = Je legt { $card } neer.
scopa-player-puts-down = { $player } legt { $card } neer.
scopa-scopa-suffix =  - SCOPA!
scopa-clear-table-suffix = , en ruimt de tafel leeg.
scopa-remaining-cards = { $player } krijgt de resterende tafelkaarten.
scopa-scoring-round = Scoren ronde...
scopa-most-cards = { $player } scoort 1 punt voor de meeste kaarten ({ $count } kaarten).
scopa-most-cards-tie = Meeste kaarten is gelijk - geen punt toegekend.
scopa-most-diamonds = { $player } scoort 1 punt voor de meeste ruiten ({ $count } ruiten).
scopa-most-diamonds-tie = Meeste ruiten is gelijk - geen punt toegekend.
scopa-seven-diamonds = { $player } scoort 1 punt voor de 7 van ruiten.
scopa-seven-diamonds-multi = { $player } scoort 1 punt voor de meeste 7 van ruiten ({ $count } × 7 van ruiten).
scopa-seven-diamonds-tie = 7 van ruiten is gelijk - geen punt toegekend.
scopa-most-sevens = { $player } scoort 1 punt voor de meeste zevens ({ $count } zevens).
scopa-most-sevens-tie = Meeste zevens is gelijk - geen punt toegekend.
scopa-round-scores = Ronde scores:
scopa-round-score-line = { $player }: +{ $round_score } (totaal: { $total_score })
scopa-table-empty = Er liggen geen kaarten op tafel.
scopa-no-such-card = Geen kaart op die positie.
scopa-captured-count = Je hebt { $count } kaarten verzameld

# View actions
scopa-view-table = Bekijk tafel
scopa-view-captured = Bekijk verzameld

# Scopa-specific options
scopa-enter-target-score = Voer doelscore in (1-121)
scopa-set-cards-per-deal = Kaarten per deel: { $cards }
scopa-enter-cards-per-deal = Voer kaarten per deel in (1-10)
scopa-set-decks = Aantal decks: { $decks }
scopa-enter-decks = Voer aantal decks in (1-6)
scopa-toggle-escoba = Escoba (som tot 15): { $enabled }
scopa-toggle-hints = Toon vangst hints: { $enabled }
scopa-set-mechanic = Scopa mechanisme: { $mechanic }
scopa-select-mechanic = Selecteer scopa mechanisme
scopa-toggle-instant-win = Direct winnen op scopa: { $enabled }
scopa-toggle-team-scoring = Pool teamkaarten voor scoren: { $enabled }
scopa-toggle-inverse = Omgekeerde modus (doelscore bereiken = eliminatie): { $enabled }

# Option change announcements
scopa-option-changed-cards = Kaarten per deel ingesteld op { $cards }.
scopa-option-changed-decks = Aantal decks ingesteld op { $decks }.
scopa-option-changed-escoba = Escoba { $enabled }.
scopa-option-changed-hints = Vangst hints { $enabled }.
scopa-option-changed-mechanic = Scopa mechanisme ingesteld op { $mechanic }.
scopa-option-changed-instant = Direct winnen op scopa { $enabled }.
scopa-option-changed-team-scoring = Team kaart scoren { $enabled }.
scopa-option-changed-inverse = Omgekeerde modus { $enabled }.

# Scopa mechanic choices
scopa-mechanic-normal = Normaal
scopa-mechanic-no_scopas = Geen Scopas
scopa-mechanic-only_scopas = Alleen Scopas

# Disabled action reasons
scopa-timer-not-active = De rondetimer is niet actief.

# Validation errors
scopa-error-not-enough-cards = Niet genoeg kaarten in { $decks } { $decks ->
    [one] deck
    *[other] decks
} voor { $players } { $players ->
    [one] speler
    *[other] spelers
} met { $cards_per_deal } kaarten elk. (Nodig { $cards_per_deal } × { $players } = { $cards_needed } kaarten, maar hebben slechts { $total_cards }.)
