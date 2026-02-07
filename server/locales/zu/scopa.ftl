# Scopa game messages (isiZulu)

# Game name
game-name-scopa = Scopa

# Game events
scopa-initial-table = Amakhadi etafula: { $cards }
scopa-no-initial-table = Awekho makhadi etafula ekuqaleni.
scopa-you-collect = Wena uqoqa { $cards } nge-{ $card }
scopa-player-collects = U-{ $player } uqoqa { $cards } nge-{ $card }
scopa-you-put-down = Wena ubeka phansi { $card }.
scopa-player-puts-down = U-{ $player } ubeka phansi { $card }.
scopa-scopa-suffix =  - I-SCOPA!
scopa-clear-table-suffix = , kusula itafula.
scopa-remaining-cards = U-{ $player } uthola amakhadi etafula asele.
scopa-scoring-round = Umjikelezo wokubala amaphuzu...
scopa-most-cards = U-{ $player } uphumelela iphuzu eli-1 ngamakhadi amaningi (amakhadi angu-{ $count }).
scopa-most-cards-tie = Amakhadi amaningi ayalinganiswa - ayikho iphuzu elinikwe.
scopa-most-diamonds = U-{ $player } uphumelela iphuzu eli-1 ngamadayimane amaningi (amadayimane angu-{ $count }).
scopa-most-diamonds-tie = Amadayimane amaningi ayalinganiswa - ayikho iphuzu elinikwe.
scopa-seven-diamonds = U-{ $player } uphumelela iphuzu eli-1 nge-7 yamadayimane.
scopa-seven-diamonds-multi = U-{ $player } uphumelela iphuzu eli-1 nge-7 yamadayimane eningi ({ $count } × 7 yamadayimane).
scopa-seven-diamonds-tie = U-7 yamadayimane uyalinganiswa - ayikho iphuzu elinikwe.
scopa-most-sevens = U-{ $player } uphumelela iphuzu eli-1 ngama-sevens amaningi (ama-sevens angu-{ $count }).
scopa-most-sevens-tie = Ama-sevens amaningi ayalinganiswa - ayikho iphuzu elinikwe.
scopa-round-scores = Amaphuzu omjikelezo:
scopa-round-score-line = { $player }: +{ $round_score } (isamba: { $total_score })
scopa-table-empty = Awekho makhadi etafula.
scopa-no-such-card = Alikho ikhadi kuleyo ndawo.
scopa-captured-count = Ubambe amakhadi angu-{ $count }

# View actions
scopa-view-table = Bheka itafula
scopa-view-captured = Bheka okubanjwe

# Scopa-specific options
scopa-enter-target-score = Faka amaphuzu ahlosiwe (1-121)
scopa-set-cards-per-deal = Amakhadi ngokwabela: { $cards }
scopa-enter-cards-per-deal = Faka amakhadi ngokwabela (1-10)
scopa-set-decks = Inani lamadekhi: { $decks }
scopa-enter-decks = Faka inani lamadekhi (1-6)
scopa-toggle-escoba = I-Escoba (isamba sibe ngu-15): { $enabled }
scopa-toggle-hints = Khombisa amaqondiso okubamba: { $enabled }
scopa-set-mechanic = Ubuchwepheshe be-scopa: { $mechanic }
scopa-select-mechanic = Khetha ubuchwepheshe be-scopa
scopa-toggle-instant-win = Ukunqoba ngokushesha nge-scopa: { $enabled }
scopa-toggle-team-scoring = Hlanganyela amakhadi ethimba ukuze ubale amaphuzu: { $enabled }
scopa-toggle-inverse = Imodi ephambene (finyelela okuhlosiwe = ukukhishwa): { $enabled }

# Option change announcements
scopa-option-changed-cards = Amakhadi ngokwabela asetelwe ku-{ $cards }.
scopa-option-changed-decks = Inani lamadekhi lisetelwe ku-{ $decks }.
scopa-option-changed-escoba = I-Escoba { $enabled }.
scopa-option-changed-hints = Amaqondiso okubamba { $enabled }.
scopa-option-changed-mechanic = Ubuchwepheshe be-scopa busetelwe ku-{ $mechanic }.
scopa-option-changed-instant = Ukunqoba ngokushesha nge-scopa { $enabled }.
scopa-option-changed-team-scoring = Ukubala amaphuzu kwamakhadi ethimba { $enabled }.
scopa-option-changed-inverse = Imodi ephambene { $enabled }.

# Scopa mechanic choices
scopa-mechanic-normal = Okuvamile
scopa-mechanic-no_scopas = Awekho ma-Scopas
scopa-mechanic-only_scopas = Ama-Scopas Kuphela

# Disabled action reasons
scopa-timer-not-active = Isikhathi somjikelezo asisebenzi.

# Validation errors
scopa-error-not-enough-cards = Awanele amakhadi ku-{ $decks } { $decks ->
    [one] idekhi
    *[other] amadekhi
} ngabadlali abangu-{ $players } { $players ->
    [one] umdlali
    *[other] abadlali
} ngamakhadi angu-{ $cards_per_deal } ngamunye. (Kudinga { $cards_per_deal } × { $players } = amakhadi angu-{ $cards_needed }, kodwa kunama-{ $total_cards } kuphela.)
