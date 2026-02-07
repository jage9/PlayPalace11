# 1-4-24 (Midnight) game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-midnight = 1-4-24
midnight-category = Tärningsspel

# Actions
midnight-roll = Kasta tärningarna
midnight-keep-die = Behåll { $value }
midnight-bank = Bekräfta

# Game events
midnight-turn-start = { $player }s tur.
midnight-you-rolled = Du kastade: { $dice }.
midnight-player-rolled = { $player } kastade: { $dice }.

# Keeping dice
midnight-you-keep = Du behåller { $die }.
midnight-player-keeps = { $player } behåller { $die }.
midnight-you-unkeep = Du släpper { $die }.
midnight-player-unkeeps = { $player } släpper { $die }.

# Turn status
midnight-you-have-kept = Behållna tärningar: { $kept }. Återstående kast: { $remaining }.
midnight-player-has-kept = { $player } har behållit: { $kept }. { $remaining } tärningar kvar.

# Scoring
midnight-you-scored = Du fick { $score } poäng.
midnight-scored = { $player } fick { $score } poäng.
midnight-you-disqualified = Du har inte både 1 och 4. Diskvalificerad!
midnight-player-disqualified = { $player } har inte både 1 och 4. Diskvalificerad!

# Round results
midnight-round-winner = { $player } vinner rundan!
midnight-round-tie = Runda oavgjord mellan { $players }.
midnight-all-disqualified = Alla spelare diskvalificerade! Ingen vinnare denna runda.

# Game winner
midnight-game-winner = { $player } vinner spelet med { $wins } rundvinster!
midnight-game-tie = Det är oavgjort! { $players } vann var { $wins } rundor.

# Options
midnight-set-rounds = Rundor att spela: { $rounds }
midnight-enter-rounds = Ange antal rundor att spela:
midnight-option-changed-rounds = Rundor att spela ändrat till { $rounds }

# Disabled reasons
midnight-need-to-roll = Du måste kasta tärningarna först.
midnight-no-dice-to-keep = Inga tärningar tillgängliga att behålla.
midnight-must-keep-one = Du måste behålla minst en tärning per kast.
midnight-must-roll-first = Du måste kasta tärningarna först.
midnight-keep-all-first = Du måste behålla alla tärningar innan bekräftelse.
