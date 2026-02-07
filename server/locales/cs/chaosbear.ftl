# Chaos Bear game messages

# Game name
game-name-chaosbear = Chaotický medvěd

# Actions
chaosbear-roll-dice = Hodit kostkami
chaosbear-draw-card = Táhnout kartu
chaosbear-check-status = Zkontrolovat stav

# Game intro (3 separate messages like v10)
chaosbear-intro-1 = Chaotický medvěd začal! Všichni hráči začínají 30 polí před medvědem.
chaosbear-intro-2 = Hoďte kostkami pro posun vpřed a tažte karty na násobcích 5 pro získání speciálních efektů.
chaosbear-intro-3 = Nenechte se chytit medvědem!

# Turn announcement
chaosbear-turn = Tah hráče { $player }; pole { $position }.

# Rolling
chaosbear-roll = { $player } hodil { $roll }.
chaosbear-position = { $player } je nyní na poli { $position }.

# Drawing cards
chaosbear-draws-card = { $player } táhne kartu.
chaosbear-card-impulsion = Impuls! { $player } se posouvá vpřed o 3 pole na pole { $position }!
chaosbear-card-super-impulsion = Super impuls! { $player } se posouvá vpřed o 5 polí na pole { $position }!
chaosbear-card-tiredness = Únava! Energie medvěda minus 1. Nyní má { $energy } energie.
chaosbear-card-hunger = Hlad! Energie medvěda plus 1. Nyní má { $energy } energie.
chaosbear-card-backward = Strčení zpět! { $player } se vrací na pole { $position }.
chaosbear-card-random-gift = Náhodný dárek!
chaosbear-gift-back = { $player } se vrátil na pole { $position }.
chaosbear-gift-forward = { $player } se posunul vpřed na pole { $position }!

# Bear turn
chaosbear-bear-roll = Medvěd hodil { $roll } + jeho { $energy } energie = { $total }.
chaosbear-bear-energy-up = Medvěd hodil 3 a získal 1 energii!
chaosbear-bear-position = Medvěd je nyní na poli { $position }!
chaosbear-player-caught = Medvěd chytil { $player }! { $player } byl poražen!
chaosbear-bear-feast = Medvěd ztrácí 3 energie po hostině na jejich těle!

# Status check
chaosbear-status-player-alive = { $player }: pole { $position }.
chaosbear-status-player-caught = { $player }: chycen na poli { $position }.
chaosbear-status-bear = Medvěd je na poli { $position } s { $energy } energií.

# End game
chaosbear-winner = { $player } přežil a vyhrává! Dosáhl pole { $position }!
chaosbear-tie = Remíza na poli { $position }!

# Disabled action reasons
chaosbear-you-are-caught = Byl jsi chycen medvědem.
chaosbear-not-on-multiple = Můžete táhnout karty pouze na násobcích 5.
