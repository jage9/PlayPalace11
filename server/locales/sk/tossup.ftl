# Toss Up game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-tossup = Hadzanie hore
tossup-category = Kockové hry

# Actions
tossup-roll-first = Hodiť { $count } kockami
tossup-roll-remaining = Hodiť zostávajúcimi { $count } kockami
tossup-bank = Uložiť { $points } bodov

# Game events
tossup-turn-start = Ťah hráča { $player }. Skóre: { $score }
tossup-you-roll = Hodil si: { $results }.
tossup-player-rolls = { $player } hodil: { $results }.

# Turn status
tossup-you-have-points = Body ťahu: { $turn_points }. Zostáva kociek: { $dice_count }.
tossup-player-has-points = { $player } má { $turn_points } bodov ťahu. Zostáva { $dice_count } kociek.

# Fresh dice
tossup-you-get-fresh = Žiadne kocky! Dostávate { $count } nových kociek.
tossup-player-gets-fresh = { $player } dostáva { $count } nových kociek.

# Bust
tossup-you-bust = Prasknutie! Strácate { $points } bodov za tento ťah.
tossup-player-busts = { $player } praskol a stráca { $points } bodov!

# Bank
tossup-you-bank = Ukladáte { $points } bodov. Celkové skóre: { $total }.
tossup-player-banks = { $player } ukladá { $points } bodov. Celkové skóre: { $total }.

# Winner
tossup-winner = { $player } vyhráva s { $score } bodmi!
tossup-tie-tiebreaker = Je to remíza medzi { $players }! Rozhodujúce kolo!

# Options
tossup-set-rules-variant = Varianta pravidiel: { $variant }
tossup-select-rules-variant = Vyberte variantu pravidiel:
tossup-option-changed-rules = Varianta pravidiel zmenená na { $variant }

tossup-set-starting-dice = Počiatočné kocky: { $count }
tossup-enter-starting-dice = Zadajte počet počiatočných kociek:
tossup-option-changed-dice = Počiatočné kocky zmenené na { $count }

# Rules variants
tossup-rules-standard = Štandardné
tossup-rules-playpalace = PlayPalace

# Rules explanations
tossup-rules-standard-desc = 3 zelené, 2 žlté, 1 červená na kocku. Prasknutie pri žiadnej zelenej a aspoň jednej červenej.
tossup-rules-playpalace-desc = Rovnomerné rozdelenie. Prasknutie ak sú všetky kocky červené.

# Disabled reasons
tossup-need-points = Potrebujete body na uloženie.
