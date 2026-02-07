# Scopa game messages
# Note: Common messages like round-start, turn-start, target-score, team-mode are in games.ftl

# Game name
game-name-scopa = Scopa

# Game events
scopa-initial-table = Karte na mizi: { $cards }
scopa-no-initial-table = Na mizi ni kart za začetek.
scopa-you-collect = Zbiraš { $cards } z { $card }
scopa-player-collects = { $player } zbira { $cards } z { $card }
scopa-you-put-down = Položiš { $card }.
scopa-player-puts-down = { $player } položi { $card }.
scopa-scopa-suffix =  - SCOPA!
scopa-clear-table-suffix = , počistivši mizo.
scopa-remaining-cards = { $player } dobi preostale karte z mize.
scopa-scoring-round = Točkovanje kroga...
scopa-most-cards = { $player } dobi 1 točko za največ kart ({ $count } kart).
scopa-most-cards-tie = Največ kart je neodločeno - točka se ne podeli.
scopa-most-diamonds = { $player } dobi 1 točko za največ karo ({ $count } karo).
scopa-most-diamonds-tie = Največ karo je neodločeno - točka se ne podeli.
scopa-seven-diamonds = { $player } dobi 1 točko za sedmico karo.
scopa-seven-diamonds-multi = { $player } dobi 1 točko za največ sedmic karo ({ $count } × sedmica karo).
scopa-seven-diamonds-tie = Sedmica karo je neodločeno - točka se ne podeli.
scopa-most-sevens = { $player } dobi 1 točko za največ sedmic ({ $count } sedmic).
scopa-most-sevens-tie = Največ sedmic je neodločeno - točka se ne podeli.
scopa-round-scores = Rezultati kroga:
scopa-round-score-line = { $player }: +{ $round_score } (skupno: { $total_score })
scopa-table-empty = Na mizi ni kart.
scopa-no-such-card = Na tej poziciji ni karte.
scopa-captured-count = Zajel si { $count } kart

# View actions
scopa-view-table = Poglej mizo
scopa-view-captured = Poglej zajete

# Scopa-specific options
scopa-enter-target-score = Vnesi ciljno točkovanje (1-121)
scopa-set-cards-per-deal = Karte na delitev: { $cards }
scopa-enter-cards-per-deal = Vnesi karte na delitev (1-10)
scopa-set-decks = Število klopov: { $decks }
scopa-enter-decks = Vnesi število klopov (1-6)
scopa-toggle-escoba = Escoba (vsota do 15): { $enabled }
scopa-toggle-hints = Pokaži namige za zajemanje: { $enabled }
scopa-set-mechanic = Scopa mehanika: { $mechanic }
scopa-select-mechanic = Izberi scopa mehaniko
scopa-toggle-instant-win = Takojšnja zmaga na scopa: { $enabled }
scopa-toggle-team-scoring = Združi ekipne karte za točkovanje: { $enabled }
scopa-toggle-inverse = Obratni način (doseganje cilja = izločitev): { $enabled }

# Option change announcements
scopa-option-changed-cards = Karte na delitev nastavljene na { $cards }.
scopa-option-changed-decks = Število klopov nastavljeno na { $decks }.
scopa-option-changed-escoba = Escoba { $enabled }.
scopa-option-changed-hints = Namigi za zajemanje { $enabled }.
scopa-option-changed-mechanic = Scopa mehanika nastavljena na { $mechanic }.
scopa-option-changed-instant = Takojšnja zmaga na scopa { $enabled }.
scopa-option-changed-team-scoring = Točkovanje ekipnih kart { $enabled }.
scopa-option-changed-inverse = Obratni način { $enabled }.

# Scopa mechanic choices
scopa-mechanic-normal = Normalno
scopa-mechanic-no_scopas = Brez Scop
scopa-mechanic-only_scopas = Samo Scope

# Disabled action reasons
scopa-timer-not-active = Časovnik kroga ni aktiven.

# Validation errors
scopa-error-not-enough-cards = Ni dovolj kart v { $decks } { $decks ->
    [one] klopu
    *[other] klopih
} za { $players } { $players ->
    [one] igralca
    *[other] igralcev
} z { $cards_per_deal } kartami vsakemu. (Potrebnih { $cards_per_deal } × { $players } = { $cards_needed } kart, a je le { $total_cards }.)
