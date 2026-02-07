# Toss Up game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-tossup = Házení nahoru
tossup-category = Karetní hry

# Actions
tossup-roll-first = Hodit { $count } kostkami
tossup-roll-remaining = Hodit zbývajícími { $count } kostkami
tossup-bank = Uložit { $points } bodů

# Game events
tossup-turn-start = Tah hráče { $player }. Skóre: { $score }
tossup-you-roll = Hodil jsi: { $results }.
tossup-player-rolls = { $player } hodil: { $results }.

# Turn status
tossup-you-have-points = Body tahu: { $turn_points }. Zbývá kostek: { $dice_count }.
tossup-player-has-points = { $player } má { $turn_points } bodů tahu. Zbývá { $dice_count } kostek.

# Fresh dice
tossup-you-get-fresh = Žádné kostky! Dostáváte { $count } nových kostek.
tossup-player-gets-fresh = { $player } dostává { $count } nových kostek.

# Bust
tossup-you-bust = Prasknutí! Ztrácíte { $points } bodů za tento tah.
tossup-player-busts = { $player } praskl a ztrácí { $points } bodů!

# Bank
tossup-you-bank = Ukládáte { $points } bodů. Celkové skóre: { $total }.
tossup-player-banks = { $player } ukládá { $points } bodů. Celkové skóre: { $total }.

# Winner
tossup-winner = { $player } vyhrává s { $score } body!
tossup-tie-tiebreaker = Je to remíza mezi { $players }! Rozhodující kolo!

# Options
tossup-set-rules-variant = Varianta pravidel: { $variant }
tossup-select-rules-variant = Vyberte variantu pravidel:
tossup-option-changed-rules = Varianta pravidel změněna na { $variant }

tossup-set-starting-dice = Počáteční kostky: { $count }
tossup-enter-starting-dice = Zadejte počet počátečních kostek:
tossup-option-changed-dice = Počáteční kostky změněny na { $count }

# Rules variants
tossup-rules-standard = Standardní
tossup-rules-playpalace = PlayPalace

# Rules explanations
tossup-rules-standard-desc = 3 zelené, 2 žluté, 1 červená na kostku. Prasknutí při žádné zelené a alespoň jedné červené.
tossup-rules-playpalace-desc = Rovnoměrné rozdělení. Prasknutí pokud jsou všechny kostky červené.

# Disabled reasons
tossup-need-points = Potřebujete body k uložení.
