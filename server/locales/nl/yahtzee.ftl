# Yahtzee game messages

# Game info
game-name-yahtzee = Yahtzee

# Actions - Rolling
yahtzee-roll = Opnieuw gooien ({ $count } over)
yahtzee-roll-all = Gooi dobbelstenen

# Upper section scoring categories
yahtzee-score-ones = Enen voor { $points } punten
yahtzee-score-twos = Tweeën voor { $points } punten
yahtzee-score-threes = Drieën voor { $points } punten
yahtzee-score-fours = Vieren voor { $points } punten
yahtzee-score-fives = Vijven voor { $points } punten
yahtzee-score-sixes = Zessen voor { $points } punten

# Lower section scoring categories
yahtzee-score-three-kind = Three of a Kind voor { $points } punten
yahtzee-score-four-kind = Four of a Kind voor { $points } punten
yahtzee-score-full-house = Full House voor { $points } punten
yahtzee-score-small-straight = Kleine Straat voor { $points } punten
yahtzee-score-large-straight = Grote Straat voor { $points } punten
yahtzee-score-yahtzee = Yahtzee voor { $points } punten
yahtzee-score-chance = Kans voor { $points } punten

# Game events
yahtzee-you-rolled = Je gooide: { $dice }. Worpen over: { $remaining }
yahtzee-player-rolled = { $player } gooide: { $dice }. Worpen over: { $remaining }

# Scoring announcements
yahtzee-you-scored = Je scoorde { $points } punten in { $category }.
yahtzee-player-scored = { $player } scoorde { $points } in { $category }.

# Yahtzee bonus
yahtzee-you-bonus = Yahtzee bonus! +100 punten
yahtzee-player-bonus = { $player } kreeg een Yahtzee bonus! +100 punten

# Upper section bonus
yahtzee-you-upper-bonus = Bovensectie bonus! +35 punten ({ $total } in bovensectie)
yahtzee-player-upper-bonus = { $player } verdiende de bovensectie bonus! +35 punten
yahtzee-you-upper-bonus-missed = Je miste de bovensectie bonus ({ $total } in bovensectie, nodig 63).
yahtzee-player-upper-bonus-missed = { $player } miste de bovensectie bonus.

# Scoring mode
yahtzee-choose-category = Kies een categorie om in te scoren.
yahtzee-continuing = Beurt voortzetten.

# Status checks
yahtzee-check-scoresheet = Bekijk scorekaart
yahtzee-view-dice = Bekijk hand
yahtzee-your-dice = Jouw dobbelstenen: { $dice }.
yahtzee-your-dice-kept = Jouw dobbelstenen: { $dice }. Bewaren: { $kept }
yahtzee-not-rolled = Je hebt nog niet gegooid.

# Scoresheet display
yahtzee-scoresheet-header = === { $player }'s Scorekaart ===
yahtzee-scoresheet-upper = Bovensectie:
yahtzee-scoresheet-lower = Ondersectie:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = Boventotaal: { $total } (BONUS: +35)
yahtzee-scoresheet-upper-total-needed = Boventotaal: { $total } ({ $needed } meer voor bonus)
yahtzee-scoresheet-yahtzee-bonus = Yahtzee Bonussen: { $count } x 100 = { $total }
yahtzee-scoresheet-grand-total = TOTALE SCORE: { $total }

# Category names (for announcements)
yahtzee-category-ones = Enen
yahtzee-category-twos = Tweeën
yahtzee-category-threes = Drieën
yahtzee-category-fours = Vieren
yahtzee-category-fives = Vijven
yahtzee-category-sixes = Zessen
yahtzee-category-three-kind = Three of a Kind
yahtzee-category-four-kind = Four of a Kind
yahtzee-category-full-house = Full House
yahtzee-category-small-straight = Kleine Straat
yahtzee-category-large-straight = Grote Straat
yahtzee-category-yahtzee = Yahtzee
yahtzee-category-chance = Kans

# Game end
yahtzee-winner = { $player } wint met { $score } punten!
yahtzee-winners-tie = Het is gelijk! { $players } scoorden allemaal { $score } punten!

# Options
yahtzee-set-rounds = Aantal spellen: { $rounds }
yahtzee-enter-rounds = Voer aantal spellen in (1-10):
yahtzee-option-changed-rounds = Aantal spellen ingesteld op { $rounds }.

# Disabled action reasons
yahtzee-no-rolls-left = Je hebt geen worpen meer over.
yahtzee-roll-first = Je moet eerst gooien.
yahtzee-category-filled = Die categorie is al gevuld.
