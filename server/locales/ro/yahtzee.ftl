# Yahtzee game messages

# Game info
game-name-yahtzee = Yahtzee

# Actions - Rolling
yahtzee-roll = Rearuncați ({ $count } rămase)
yahtzee-roll-all = Aruncați zarurile

# Upper section scoring categories
yahtzee-score-ones = Unu pentru { $points } puncte
yahtzee-score-twos = Doi pentru { $points } puncte
yahtzee-score-threes = Trei pentru { $points } puncte
yahtzee-score-fours = Patru pentru { $points } puncte
yahtzee-score-fives = Cinci pentru { $points } puncte
yahtzee-score-sixes = Șase pentru { $points } puncte

# Lower section scoring categories
yahtzee-score-three-kind = Trei identice pentru { $points } puncte
yahtzee-score-four-kind = Patru identice pentru { $points } puncte
yahtzee-score-full-house = Full pentru { $points } puncte
yahtzee-score-small-straight = Scară mică pentru { $points } puncte
yahtzee-score-large-straight = Scară mare pentru { $points } puncte
yahtzee-score-yahtzee = Yahtzee pentru { $points } puncte
yahtzee-score-chance = Șansă pentru { $points } puncte

# Game events
yahtzee-you-rolled = Ați aruncat: { $dice }. Aruncări rămase: { $remaining }
yahtzee-player-rolled = { $player } a aruncat: { $dice }. Aruncări rămase: { $remaining }

# Scoring announcements
yahtzee-you-scored = Ați marcat { $points } puncte în { $category }.
yahtzee-player-scored = { $player } a marcat { $points } în { $category }.

# Yahtzee bonus
yahtzee-you-bonus = Bonus Yahtzee! +100 puncte
yahtzee-player-bonus = { $player } a primit un bonus Yahtzee! +100 puncte

# Upper section bonus
yahtzee-you-upper-bonus = Bonus secțiune superioară! +35 puncte ({ $total } în secțiunea superioară)
yahtzee-player-upper-bonus = { $player } a câștigat bonusul secțiunii superioare! +35 puncte
yahtzee-you-upper-bonus-missed = Ați ratat bonusul secțiunii superioare ({ $total } în secțiunea superioară, erau necesare 63).
yahtzee-player-upper-bonus-missed = { $player } a ratat bonusul secțiunii superioare.

# Scoring mode
yahtzee-choose-category = Alegeți o categorie pentru punctare.
yahtzee-continuing = Continuarea rândului.

# Status checks
yahtzee-check-scoresheet = Verificați foaia de scor
yahtzee-view-dice = Verificați mâna
yahtzee-your-dice = Zarurile dvs.: { $dice }.
yahtzee-your-dice-kept = Zarurile dvs.: { $dice }. Păstrând: { $kept }
yahtzee-not-rolled = Nu ați aruncat încă.

# Scoresheet display
yahtzee-scoresheet-header = === Foaia de scor a lui { $player } ===
yahtzee-scoresheet-upper = Secțiune superioară:
yahtzee-scoresheet-lower = Secțiune inferioară:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = Total superior: { $total } (BONUS: +35)
yahtzee-scoresheet-upper-total-needed = Total superior: { $total } ({ $needed } mai mult pentru bonus)
yahtzee-scoresheet-yahtzee-bonus = Bonusuri Yahtzee: { $count } x 100 = { $total }
yahtzee-scoresheet-grand-total = SCOR TOTAL: { $total }

# Category names (for announcements)
yahtzee-category-ones = Unu
yahtzee-category-twos = Doi
yahtzee-category-threes = Trei
yahtzee-category-fours = Patru
yahtzee-category-fives = Cinci
yahtzee-category-sixes = Șase
yahtzee-category-three-kind = Trei identice
yahtzee-category-four-kind = Patru identice
yahtzee-category-full-house = Full
yahtzee-category-small-straight = Scară mică
yahtzee-category-large-straight = Scară mare
yahtzee-category-yahtzee = Yahtzee
yahtzee-category-chance = Șansă

# Game end
yahtzee-winner = { $player } câștigă cu { $score } puncte!
yahtzee-winners-tie = Egalitate! { $players } au marcat toți { $score } puncte!

# Options
yahtzee-set-rounds = Număr de jocuri: { $rounds }
yahtzee-enter-rounds = Introduceți numărul de jocuri (1-10):
yahtzee-option-changed-rounds = Număr de jocuri setat la { $rounds }.

# Disabled action reasons
yahtzee-no-rolls-left = Nu mai aveți aruncări.
yahtzee-roll-first = Trebuie să aruncați mai întâi.
yahtzee-category-filled = Acea categorie este deja completată.
