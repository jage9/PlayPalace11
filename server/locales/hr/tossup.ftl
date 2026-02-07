# Toss Up game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-tossup = Bacanje gore
tossup-category = Igre s kockicama

# Actions
tossup-roll-first = Baci { $count } kockica
tossup-roll-remaining = Baci preostale { $count } kockice
tossup-bank = Spremi { $points } bodova

# Game events
tossup-turn-start = Potez igrača { $player }. Rezultat: { $score }
tossup-you-roll = Bacio si: { $results }.
tossup-player-rolls = { $player } je bacio: { $results }.

# Turn status
tossup-you-have-points = Bodovi poteza: { $turn_points }. Preostalo kockica: { $dice_count }.
tossup-player-has-points = { $player } ima { $turn_points } bodova poteza. Preostalo { $dice_count } kockica.

# Fresh dice
tossup-you-get-fresh = Nema kockica! Dobivate { $count } novih kockica.
tossup-player-gets-fresh = { $player } dobiva { $count } novih kockica.

# Bust
tossup-you-bust = Propast! Gubite { $points } bodova za ovaj potez.
tossup-player-busts = { $player } propada i gubi { $points } bodova!

# Bank
tossup-you-bank = Spremate { $points } bodova. Ukupan rezultat: { $total }.
tossup-player-banks = { $player } sprema { $points } bodova. Ukupan rezultat: { $total }.

# Winner
tossup-winner = { $player } pobjeđuje s { $score } bodova!
tossup-tie-tiebreaker = Izjednačeno između { $players }! Odlučujuća runda!

# Options
tossup-set-rules-variant = Varijanta pravila: { $variant }
tossup-select-rules-variant = Odaberite varijantu pravila:
tossup-option-changed-rules = Varijanta pravila promijenjena na { $variant }

tossup-set-starting-dice = Početne kockice: { $count }
tossup-enter-starting-dice = Unesite broj početnih kockica:
tossup-option-changed-dice = Početne kockice promijenjene na { $count }

# Rules variants
tossup-rules-standard = Standardno
tossup-rules-playpalace = PlayPalace

# Rules explanations
tossup-rules-standard-desc = 3 zelene, 2 žute, 1 crvena po kockici. Propast ako nema zelenih i barem jedna crvena.
tossup-rules-playpalace-desc = Ravnomjerna raspodjela. Propast ako su sve kockice crvene.

# Disabled reasons
tossup-need-points = Trebate bodove za spremanje.
