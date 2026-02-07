# Scopa - České zprávy hry

# Název hry
game-name-scopa = Scopa

# Herní události
scopa-initial-table = Karty na stole: { $cards }
scopa-no-initial-table = Na začátku nejsou žádné karty na stole.
scopa-you-collect = Sbíráte { $cards } s { $card }
scopa-player-collects = { $player } sbírá { $cards } s { $card }
scopa-you-put-down = Pokládáte { $card }.
scopa-player-puts-down = { $player } pokládá { $card }.
scopa-scopa-suffix =  - SCOPA!
scopa-clear-table-suffix = , čištění stolu.
scopa-remaining-cards = { $player } dostává zbývající karty na stole.
scopa-scoring-round = Skórování kola...
scopa-most-cards = { $player } získává 1 bod za nejvíce karet ({ $count } karet).
scopa-most-cards-tie = Nejvíce karet je remíza - žádný bod udělen.
scopa-most-diamonds = { $player } získává 1 bod za nejvíce kárových ({ $count } kárových).
scopa-most-diamonds-tie = Nejvíce kárových je remíza - žádný bod udělen.
scopa-seven-diamonds = { $player } získává 1 bod za sedmičku károvou.
scopa-seven-diamonds-multi = { $player } získává 1 bod za nejvíce sedmiček kárových ({ $count } × sedmička kárová).
scopa-seven-diamonds-tie = Sedmička kárová je remíza - žádný bod udělen.
scopa-most-sevens = { $player } získává 1 bod za nejvíce sedmiček ({ $count } sedmiček).
scopa-most-sevens-tie = Nejvíce sedmiček je remíza - žádný bod udělen.
scopa-round-scores = Skóre kola:
scopa-round-score-line = { $player }: +{ $round_score } (celkem: { $total_score })
scopa-table-empty = Na stole nejsou žádné karty.
scopa-no-such-card = Na této pozici není žádná karta.
scopa-captured-count = Sebrali jste { $count } karet

# Akce zobrazení
scopa-view-table = Zobrazit stůl
scopa-view-captured = Zobrazit sebrané

# Možnosti specifické pro Scopa
scopa-enter-target-score = Zadejte cílové skóre (1-121)
scopa-set-cards-per-deal = Karet na rozdání: { $cards }
scopa-enter-cards-per-deal = Zadejte počet karet na rozdání (1-10)
scopa-set-decks = Počet balíčků: { $decks }
scopa-enter-decks = Zadejte počet balíčků (1-6)
scopa-toggle-escoba = Escoba (součet 15): { $enabled }
scopa-toggle-hints = Zobrazit nápovědy sběru: { $enabled }
scopa-set-mechanic = Mechanika scopy: { $mechanic }
scopa-select-mechanic = Vyberte mechaniku scopy
scopa-toggle-instant-win = Okamžitá výhra při scopě: { $enabled }
scopa-toggle-team-scoring = Sdílení týmových karet pro skórování: { $enabled }
scopa-toggle-inverse = Inverzní režim (dosažení cíle = vyřazení): { $enabled }

# Oznámení změn možností
scopa-option-changed-cards = Počet karet na rozdání nastaven na { $cards }.
scopa-option-changed-decks = Počet balíčků nastaven na { $decks }.
scopa-option-changed-escoba = Escoba { $enabled }.
scopa-option-changed-hints = Nápovědy sběru { $enabled }.
scopa-option-changed-mechanic = Mechanika scopy nastavena na { $mechanic }.
scopa-option-changed-instant = Okamžitá výhra při scopě { $enabled }.
scopa-option-changed-team-scoring = Skórování týmových karet { $enabled }.
scopa-option-changed-inverse = Inverzní režim { $enabled }.

# Volby mechaniky scopy
scopa-mechanic-normal = Normální
scopa-mechanic-no_scopas = Bez scop
scopa-mechanic-only_scopas = Pouze scopy

# Důvody zakázaných akcí
scopa-timer-not-active = Časovač kola není aktivní.

# Chyby validace
scopa-error-not-enough-cards = Nedostatek karet v { $decks } { $decks ->
    [one] balíčku
    [few] balíčcích
    [many] balíčku
   *[other] balíčcích
} pro { $players } { $players ->
    [one] hráče
    [few] hráče
    [many] hráče
   *[other] hráčů
} s { $cards_per_deal } kartami každý. (Potřeba { $cards_per_deal } × { $players } = { $cards_needed } karet, ale je jen { $total_cards }.)
