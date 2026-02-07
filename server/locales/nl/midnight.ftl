# 1-4-24 (Midnight) game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-midnight = 1-4-24
midnight-category = Dobbelsteenspellen

# Actions
midnight-roll = Gooi de dobbelstenen
midnight-keep-die = Bewaar { $value }
midnight-bank = Bank

# Game events
midnight-turn-start = { $player } is aan de beurt.
midnight-you-rolled = Je gooide: { $dice }.
midnight-player-rolled = { $player } gooide: { $dice }.

# Keeping dice
midnight-you-keep = Je bewaart { $die }.
midnight-player-keeps = { $player } bewaart { $die }.
midnight-you-unkeep = Je bewaart { $die } niet meer.
midnight-player-unkeeps = { $player } bewaart { $die } niet meer.

# Turn status
midnight-you-have-kept = Bewaarde dobbelstenen: { $kept }. Resterende worpen: { $remaining }.
midnight-player-has-kept = { $player } heeft bewaard: { $kept }. { $remaining } dobbelstenen over.

# Scoring
midnight-you-scored = Je scoorde { $score } punten.
midnight-scored = { $player } scoorde { $score } punten.
midnight-you-disqualified = Je hebt niet zowel 1 als 4. Gediskwalificeerd!
midnight-player-disqualified = { $player } heeft niet zowel 1 als 4. Gediskwalificeerd!

# Round results
midnight-round-winner = { $player } wint de ronde!
midnight-round-tie = Ronde gelijk tussen { $players }.
midnight-all-disqualified = Alle spelers gediskwalificeerd! Geen winnaar deze ronde.

# Game winner
midnight-game-winner = { $player } wint het spel met { $wins } ronde overwinningen!
midnight-game-tie = Het is gelijk! { $players } wonnen elk { $wins } rondes.

# Options
midnight-set-rounds = Te spelen rondes: { $rounds }
midnight-enter-rounds = Voer aantal te spelen rondes in:
midnight-option-changed-rounds = Te spelen rondes gewijzigd naar { $rounds }

# Disabled reasons
midnight-need-to-roll = Je moet eerst de dobbelstenen gooien.
midnight-no-dice-to-keep = Geen beschikbare dobbelstenen om te bewaren.
midnight-must-keep-one = Je moet minstens één dobbelsteen bewaren per worp.
midnight-must-roll-first = Je moet eerst de dobbelstenen gooien.
midnight-keep-all-first = Je moet alle dobbelstenen bewaren voordat je bankt.
