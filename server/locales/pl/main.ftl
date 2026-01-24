# Main UI messages for PlayPalace

# Game categories
category-card-games = Karcianki
category-dice-games = gry z kośćmi
category-rb-play-center = RB Play Center
category-poker = Poker
category-uncategorized = niezkategoryzowane

# Menu titles
main-menu-title = menu głuwne.
play-menu-title = graj
categories-menu-title = kategorje gier
tables-menu-title = dostępne stoły
play = Play
view-active-tables = Pokaż aktywne stoły
options = Opcje
logout = Wylogój się
back = wróć
go-back = wróć
context-menu = menu kontekstowe
no-actions-available = Brak dostępnych akcji.
create-table = utwórz nowy stół
join-as-player = dołącz, jako gracz.
join-as-spectator = śledź
leave-table = opuść stół.
start-game = rozpocznij grę
add-bot = Dodaj bota
remove-bot = Usuń bota
actions-menu = Menu akcji
save-table = zapisz stół
whose-turn = czyja tura?
whos-at-table = kto jest przy stole
check-scores = sprawdź wyniki
check-scores-detailed = Szczegułowe wyniki

# Turn messages
game-player-skipped = { $player } został pominięty.

# Table messages
table-created = { $host } utworzył stół z grą   { $game }.
table-joined = { $player } dołączył do stołu
table-left = { $player } opuścił stół.
new-host = { $player } jest teraz hostem.
waiting-for-players = Stół czeka na graczy, { $current }/{ $min } graczy, minimum, { $max } max
game-starting = gra się zaczyna!
table-listing = { stół od $host }' ({ $count } graczy)
table-listing-one = { stół od $host }' ({ $count } gracz)
table-listing-with = { stół od $host }' ({ $count } graczy) z { $members }
table-listing-game = { $game }: { stół od $host }' ({ $count } graczy)
table-listing-game-one = { $game }: { stół od $host }' ({ $count } gracz)
table-listing-game-with = { $game }: { stół od $host }' ({ $count } graczy) z { $members }
table-not-exists = Ten stół jóż nie istnieje
table-full = Stół jest pełny.
player-replaced-by-bot = { $player } opuścił grę, i został zastąpiony botem.
player-took-over = { $player } przejął kontrole od bota
spectator-joined = dołączył stół { $host } table jako spektator.

# Spectator mode
spectate = śledź
now-playing = { $player } dołącza do rozgrywki
now-spectating = { $player } teraz śledzi rozgrywkę

# General
welcome = witaj w Play Palace!
goodbye = pa!

# User presence announcements
user-online = { $player } jest online.
user-offline = { $player } poszedł offline

# Options
language = Język
language-option = Język: { $language }
language-changed = zmieniono język na  { $language }.

# Boolean option states
option-on = Wł
option-off = Wył

# Sound options
turn-sound-option = Dźwięk tury { $status }

# Dice options
clear-kept-option = odznacz kostki po rzucie: { $status }
dice-keeping-style-option = Styl zatrzymania kostek: { $style }
dice-keeping-style-changed = styl zatrzymania kostek po rzucie zmieniony na { $style }.
dice-keeping-style-indexes = Indeksy kości
dice-keeping-style-values = Wartości kości

# Bot names
cancel = Anuluj
no-bot-names-available = Brak nazw botów
select-bot-name = Nazwij bota
enter-bot-name = Wpisz nazwę bota
no-options-available = Brak obcji
no-scores-available = brak wyników

# Duration estimation
estimate-duration = oszacowany czas
estimate-computing = szacowanie czasu trwania gry
estimate-result = Oszacowany czas bota: { $bot_time } (± { $std_dev }). { $outlier_info }Szacowany czas gracza: { $human_time }.
estimate-error = Nie można osacować czasu.
estimate-already-running = Szacowanie w toku

# Save/Restore
saved-tables = Zapisane stoły
no-saved-tables = Nie masz zapisanych stołów
restore-table = przywróć
delete-saved-table = Usuń
saved-table-deleted = usunięto zapisany stół
missing-players = nie można przywrucić brakujący gracze: { $players }
table-restored = Przywrócono stół! wszyscy gracze zostali przeniesieni
table-saved-destroying = Zapisano stół, wracasz do głównego menu.
game-type-not-found = Ten typ gry jóż nie istnieje.

# Action disabled reasons
action-not-your-turn = To nie twoja tura
action-not-playing = gra jeszcze się nie zaczęła
action-spectator = spektatorzy nie mogą tego robić!
action-not-host = Tylko host to może zrobić!
action-game-in-progress = nie można tego zrobić, gdy gra trwa.
action-need-more-players = Potrzeba więcej graczy, aby zacząć.
action-table-full = Stół jest pełny
action-no-bots = Nie ma żadnych botów do usunięcia.
action-bots-cannot = boty nie mogą tego robić.
action-no-scores = Jeszcze nie ma wyników.

# Dice actions
dice-not-rolled = Jeszcze nie rzuciłeś kostką.
dice-locked = Ta kość jest zablokowana
dice-no-dice = brak kości

# Game actions
game-turn-start = { tura $player }.
game-no-turn = nikt teraz nie ma tury.
table-no-players = Brak graczy.
table-players-one = { $count } gracz: { $players }.
table-players-many = { $count } graczy: { $players }.
table-spectators = Widzowie: { $spectators }.
game-leave = Opuść
game-over = Koniec gry
game-final-scores = Wyniki końcowe
game-points = { $count } { $count ->
    [one] punkt
   *[other] punktów
}
status-box-closed = Zamknięty.
play = Graj

# Leaderboards
leaderboards = Rankingi
leaderboards-menu-title = Rankingi
leaderboards-select-game = Zaznacz grę, aby przeglądać wyniki.
leaderboard-no-data = Brak wyników dla tej gry.

# Leaderboard types
leaderboard-type-wins = Rankingi wygranych
leaderboard-type-rating = ranking umiejętności
leaderboard-type-total-score = całkowity wynik
leaderboard-type-high-score = najwyższy wynik
leaderboard-type-games-played = grane gry
leaderboard-type-avg-points-per-turn = średnia punktów na turę
leaderboard-type-best-single-turn = Najlepsza pojedyńcza tura
leaderboard-type-score-per-round = wynik na rundę

# Leaderboard headers
leaderboard-wins-header = { $game } - liderzy wygranych gier
leaderboard-total-score-header = { $game } - Całkowity wynik.
leaderboard-high-score-header = { $game } - najwyższy wynik
leaderboard-games-played-header = { $game } - granych gier
leaderboard-rating-header = { $game } - oceny umiejętności
leaderboard-avg-points-header = { $game } - punktów AFK na turę
leaderboard-best-turn-header = { $game } - Najlepsza pojedyńcza tura
leaderboard-score-per-round-header = { $game } - Wynik na rundę

# Leaderboard entries
leaderboard-wins-entry = { $rank }: { $player }, { $wins } { $wins ->
    [one] wygrana
   *[other] wygranych
} { $losses } { $losses ->
    [one] przegrana
   *[other] przegranych
}, { $percentage }% winrate
leaderboard-score-entry = { $rank }. { $player }: { $value }
leaderboard-avg-entry = { $rank }. { $player }: { $value } avg
leaderboard-games-entry = { $rank }. { $player }: { $value } gier

# Player stats
leaderboard-player-stats = Twoje statystyki: { $wins } wins, { $losses } losses ({ $percentage }% procent wygranych)
leaderboard-no-player-stats = Jeszcze nie grałeś w tą grę

# Skill rating leaderboard
leaderboard-no-ratings = Brak  danych dla tej gry.
leaderboard-rating-entry = { $rank }. { $player }: { $rating } rating ({ $mu } ± { $sigma })
leaderboard-player-rating = Twój ranking: { $rating } ({ $mu } ± { $sigma })
leaderboard-no-player-rating = Nie jesteś w rankingó w tej grze

# My Stats menu
my-stats = Moje  Statystyki
my-stats-select-game = Zaznacz grę aby zobaczyć swoje statystyki
my-stats-no-data = Jeszcze nie grałeś w tą grę
my-stats-no-games = Jeszcze nie grałeś w żadną grę.
my-stats-header = { $game } - Twoje statystyki
my-stats-wins = Wygranych: { $value }
my-stats-losses = Wygranych: { $value }
my-stats-winrate = Procent wygranych: { $value }%
my-stats-games-played = Zagrane rozgrywki: { $value }
my-stats-total-score = Wszystkie wyniki: { $value }
my-stats-high-score = Najwyższy wynik: { $value }
my-stats-rating = Ocena umiejętności: { $value } ({ $mu } ± { $sigma })
my-stats-no-rating = Brak oceny umiejętności
my-stats-avg-per-turn = średnia ilość punktów na turę: { $value }
my-stats-best-turn = Najlepsza pojedyńcza tura: { $value }
# Prediction system
predict-outcomes = Predict outcomes
predict-header = Predicted Outcomes (by skill rating)
predict-entry = { $rank }. { $player } (rating: { $rating })
predict-entry-2p = { $rank }. { $player } (rating: { $rating }, { $probability }% win chance)
predict-unavailable = Prognoza ocen nie jest dostępna.
predict-need-players = potrzebuje conajmniej 2 luckich graczy do przewidywania
action-need-more-humans = Potrzeba więcej ludzi
confirm-leave-game = Czy na pewno chcesz opuścić stół?
confirm-yes = Tak
confirm-no = Nie
