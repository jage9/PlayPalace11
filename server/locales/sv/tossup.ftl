# Toss Up game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-tossup = Toss Up
tossup-category = Tärningsspel

# Actions
tossup-roll-first = Kasta { $count } tärningar
tossup-roll-remaining = Kasta { $count } återstående tärningar
tossup-bank = Spara { $points } poäng

# Game events
tossup-turn-start = { $player }s tur. Poäng: { $score }
tossup-you-roll = Du kastade: { $results }.
tossup-player-rolls = { $player } kastade: { $results }.

# Turn status
tossup-you-have-points = Turpoäng: { $turn_points }. Återstående tärningar: { $dice_count }.
tossup-player-has-points = { $player } har { $turn_points } turpoäng. { $dice_count } tärningar kvar.

# Fresh dice
tossup-you-get-fresh = Inga tärningar kvar! Får { $count } nya tärningar.
tossup-player-gets-fresh = { $player } får { $count } nya tärningar.

# Bust
tossup-you-bust = Krasch! Du förlorar { $points } poäng för denna tur.
tossup-player-busts = { $player } kraschar och förlorar { $points } poäng!

# Bank
tossup-you-bank = Du sparar { $points } poäng. Totalpoäng: { $total }.
tossup-player-banks = { $player } sparar { $points } poäng. Totalpoäng: { $total }.

# Winner
tossup-winner = { $player } vinner med { $score } poäng!
tossup-tie-tiebreaker = Det är oavgjort mellan { $players }! Avgörande omgång!

# Options
tossup-set-rules-variant = Regelvariant: { $variant }
tossup-select-rules-variant = Välj regelvariant:
tossup-option-changed-rules = Regelvariant ändrad till { $variant }

tossup-set-starting-dice = Starttärningar: { $count }
tossup-enter-starting-dice = Ange antal starttärningar:
tossup-option-changed-dice = Starttärningar ändrade till { $count }

# Rules variants
tossup-rules-standard = Standard
tossup-rules-playpalace = PlayPalace

# Rules explanations
tossup-rules-standard-desc = 3 gröna, 2 gula, 1 röd per tärning. Krasch om inga gröna och minst en röd.
tossup-rules-playpalace-desc = Jämn fördelning. Krasch om alla tärningar är röda.

# Disabled reasons
tossup-need-points = Du behöver poäng för att spara.
