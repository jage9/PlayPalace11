# Scopa game messages
# Note: Common messages like round-start, turn-start, target-score, team-mode are in games.ftl

# Game name
game-name-scopa = Scopa

# Game events
scopa-initial-table = Asztal lapjai: { $cards }
scopa-no-initial-table = Nincsenek lapok az asztalon kezdéskor.
scopa-you-collect = Összegyűjtöd { $cards } lapokat { $card } lappal
scopa-player-collects = { $player } összegyűjti { $cards } lapokat { $card } lappal
scopa-you-put-down = Leteszed { $card } lapot.
scopa-player-puts-down = { $player } leteszi { $card } lapot.
scopa-scopa-suffix =  - SCOPA!
scopa-clear-table-suffix = , kitisztítva az asztalt.
scopa-remaining-cards = { $player } megkapja a maradék asztali lapokat.
scopa-scoring-round = Kör pontozása...
scopa-most-cards = { $player } kap 1 pontot a legtöbb lapért ({ $count } lap).
scopa-most-cards-tie = A legtöbb lap döntetlen - nincs pont.
scopa-most-diamonds = { $player } kap 1 pontot a legtöbb káróért ({ $count } káró).
scopa-most-diamonds-tie = A legtöbb káró döntetlen - nincs pont.
scopa-seven-diamonds = { $player } kap 1 pontot a káró hétesért.
scopa-seven-diamonds-multi = { $player } kap 1 pontot a legtöbb káró hétesért ({ $count } × káró hetes).
scopa-seven-diamonds-tie = A káró hetes döntetlen - nincs pont.
scopa-most-sevens = { $player } kap 1 pontot a legtöbb hétesért ({ $count } hetes).
scopa-most-sevens-tie = A legtöbb hetes döntetlen - nincs pont.
scopa-round-scores = Kör eredményei:
scopa-round-score-line = { $player }: +{ $round_score } (összesen: { $total_score })
scopa-table-empty = Nincsenek lapok az asztalon.
scopa-no-such-card = Nincs lap ezen a pozíción.
scopa-captured-count = Összegyűjtöttél { $count } lapot

# View actions
scopa-view-table = Asztal megtekintése
scopa-view-captured = Összegyűjtött megtekintése

# Scopa-specific options
scopa-enter-target-score = Add meg a célpontszámot (1-121)
scopa-set-cards-per-deal = Lapok osztásonként: { $cards }
scopa-enter-cards-per-deal = Add meg a lapok számát osztásonként (1-10)
scopa-set-decks = Paklik száma: { $decks }
scopa-enter-decks = Add meg a paklik számát (1-6)
scopa-toggle-escoba = Escoba (összeg 15-ig): { $enabled }
scopa-toggle-hints = Befogási tippek mutatása: { $enabled }
scopa-set-mechanic = Scopa mechanika: { $mechanic }
scopa-select-mechanic = Válassz scopa mechanikát
scopa-toggle-instant-win = Azonnali győzelem scopánál: { $enabled }
scopa-toggle-team-scoring = Csapat lapok összevonása pontozáshoz: { $enabled }
scopa-toggle-inverse = Inverz mód (cél elérése = kiesés): { $enabled }

# Option change announcements
scopa-option-changed-cards = Lapok osztásonként beállítva: { $cards }.
scopa-option-changed-decks = Paklik száma beállítva: { $decks }.
scopa-option-changed-escoba = Escoba { $enabled }.
scopa-option-changed-hints = Befogási tippek { $enabled }.
scopa-option-changed-mechanic = Scopa mechanika beállítva: { $mechanic }.
scopa-option-changed-instant = Azonnali győzelem scopánál { $enabled }.
scopa-option-changed-team-scoring = Csapat lapok pontozása { $enabled }.
scopa-option-changed-inverse = Inverz mód { $enabled }.

# Scopa mechanic choices
scopa-mechanic-normal = Normál
scopa-mechanic-no_scopas = Nincs Scopa
scopa-mechanic-only_scopas = Csak Scopák

# Disabled action reasons
scopa-timer-not-active = A kör időzítője nem aktív.

# Validation errors
scopa-error-not-enough-cards = Nincs elég lap { $decks } { $decks ->
    [one] pakliban
    *[other] pakliban
} { $players } { $players ->
    [one] játékosnak
    *[other] játékosnak
} { $cards_per_deal } lappal egyenként. (Szükséges { $cards_per_deal } × { $players } = { $cards_needed } lap, de csak { $total_cards } van.)
