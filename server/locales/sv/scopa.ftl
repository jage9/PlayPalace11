# Scopa game messages
# Note: Common messages like round-start, turn-start, target-score, team-mode are in games.ftl

# Game name
game-name-scopa = Scopa

# Game events
scopa-initial-table = Bordskort: { $cards }
scopa-no-initial-table = Inga kort på bordet för start.
scopa-you-collect = Du samlar { $cards } med { $card }
scopa-player-collects = { $player } samlar { $cards } med { $card }
scopa-you-put-down = Du lägger ner { $card }.
scopa-player-puts-down = { $player } lägger ner { $card }.
scopa-scopa-suffix =  - SCOPA!
scopa-clear-table-suffix = , rensar bordet.
scopa-remaining-cards = { $player } får de återstående korten från bordet.
scopa-scoring-round = Poängräkning av omgång...
scopa-most-cards = { $player } får 1 poäng för flest kort ({ $count } kort).
scopa-most-cards-tie = Flest kort är oavgjort - ingen poäng tilldelas.
scopa-most-diamonds = { $player } får 1 poäng för flest ruter ({ $count } ruter).
scopa-most-diamonds-tie = Flest ruter är oavgjort - ingen poäng tilldelas.
scopa-seven-diamonds = { $player } får 1 poäng för ruter sjua.
scopa-seven-diamonds-multi = { $player } får 1 poäng för flest ruter sjuor ({ $count } × ruter sjua).
scopa-seven-diamonds-tie = Ruter sjua är oavgjort - ingen poäng tilldelas.
scopa-most-sevens = { $player } får 1 poäng för flest sjuor ({ $count } sjuor).
scopa-most-sevens-tie = Flest sjuor är oavgjort - ingen poäng tilldelas.
scopa-round-scores = Omgångspoäng:
scopa-round-score-line = { $player }: +{ $round_score } (totalt: { $total_score })
scopa-table-empty = Det finns inga kort på bordet.
scopa-no-such-card = Inget kort på den positionen.
scopa-captured-count = Du har fångat { $count } kort

# View actions
scopa-view-table = Visa bord
scopa-view-captured = Visa fångade

# Scopa-specific options
scopa-enter-target-score = Ange målpoäng (1-121)
scopa-set-cards-per-deal = Kort per given: { $cards }
scopa-enter-cards-per-deal = Ange kort per given (1-10)
scopa-set-decks = Antal lekar: { $decks }
scopa-enter-decks = Ange antal lekar (1-6)
scopa-toggle-escoba = Escoba (summa till 15): { $enabled }
scopa-toggle-hints = Visa fångsttips: { $enabled }
scopa-set-mechanic = Scopa-mekanik: { $mechanic }
scopa-select-mechanic = Välj scopa-mekanik
scopa-toggle-instant-win = Omedelbar vinst på scopa: { $enabled }
scopa-toggle-team-scoring = Slå samman lagkort för poängräkning: { $enabled }
scopa-toggle-inverse = Inverterat läge (nå målet = eliminering): { $enabled }

# Option change announcements
scopa-option-changed-cards = Kort per given inställt på { $cards }.
scopa-option-changed-decks = Antal lekar inställt på { $decks }.
scopa-option-changed-escoba = Escoba { $enabled }.
scopa-option-changed-hints = Fångsttips { $enabled }.
scopa-option-changed-mechanic = Scopa-mekanik inställd på { $mechanic }.
scopa-option-changed-instant = Omedelbar vinst på scopa { $enabled }.
scopa-option-changed-team-scoring = Lagkort poängräkning { $enabled }.
scopa-option-changed-inverse = Inverterat läge { $enabled }.

# Scopa mechanic choices
scopa-mechanic-normal = Normal
scopa-mechanic-no_scopas = Inga Scopor
scopa-mechanic-only_scopas = Endast Scopor

# Disabled action reasons
scopa-timer-not-active = Omgångens timer är inte aktiv.

# Validation errors
scopa-error-not-enough-cards = Inte tillräckligt med kort i { $decks } { $decks ->
    [one] lek
    *[other] lekar
} för { $players } { $players ->
    [one] spelare
    *[other] spelare
} med { $cards_per_deal } kort vardera. (Behöver { $cards_per_deal } × { $players } = { $cards_needed } kort, men har bara { $total_cards }.)
