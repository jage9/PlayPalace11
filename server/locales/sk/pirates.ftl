# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = Piráti Stratených Morí

# Game start and setup
pirates-welcome = Vitajte v Pirátoch Stratených Morí! Plávajte po moriach, zbierajte drahokamy a bojujte s inými pirátmi!
pirates-oceans = Vaša plavba vás zavedie cez: { $oceans }
pirates-gems-placed = { $total } drahokamov bolo roztrúsených po moriach. Nájdite ich všetky!
pirates-golden-moon = Zlatý Mesiac vychádza! Všetky zisky XP sú strojnásobené toto kolo!

# Turn announcements
pirates-turn = Ťah hráča { $player }. Pozícia { $position }

# Movement actions
pirates-move-left = Plávať doľava
pirates-move-right = Plávať doprava
pirates-move-2-left = Plávať 2 políčka doľava
pirates-move-2-right = Plávať 2 políčka doprava
pirates-move-3-left = Plávať 3 políčka doľava
pirates-move-3-right = Plávať 3 políčka doprava

# Movement messages
pirates-move-you = Plávaš { $direction } na pozíciu { $position }.
pirates-move-you-tiles = Plávaš { $tiles } políčok { $direction } na pozíciu { $position }.
pirates-move = { $player } pláva { $direction } na pozíciu { $position }.
pirates-map-edge = Nemôžeš plávať ďalej. Si na pozícii { $position }.

# Position and status
pirates-check-status = Skontrolovať stav
pirates-check-position = Skontrolovať pozíciu
pirates-check-moon = Skontrolovať jas mesiaca
pirates-your-position = Tvoja pozícia: { $position } v { $ocean }
pirates-moon-brightness = Zlatý Mesiac svietí na { $brightness }%. ({ $collected } z { $total } drahokamov bolo zozbieraných).
pirates-no-golden-moon = Zlatý Mesiac nie je teraz viditeľný na oblohe.

# Gem collection
pirates-gem-found-you = Našiel si { $gem }! Má hodnotu { $value } bodov.
pirates-gem-found = { $player } našiel { $gem }! Má hodnotu { $value } bodov.
pirates-all-gems-collected = Všetky drahokamy boli zozbierané!

# Winner
pirates-winner = { $player } vyhráva s { $score } bodmi!

# Skills menu
pirates-use-skill = Použiť schopnosť
pirates-select-skill = Vyber schopnosť na použitie

# Combat - Attack initiation
pirates-cannonball = Vystreliť delovou guľu
pirates-no-targets = Žiadne ciele v dosahu { $range } políčok.
pirates-attack-you-fire = Vystreľuješ delovú guľu na { $target }!
pirates-attack-incoming = { $attacker } vystreľuje delovú guľu na teba!
pirates-attack-fired = { $attacker } vystreľuje delovú guľu na { $defender }!

# Combat - Rolls
pirates-attack-roll = Hod na útok: { $roll }
pirates-attack-bonus = Bonus na útok: +{ $bonus }
pirates-defense-roll = Hod na obranu: { $roll }
pirates-defense-roll-others = { $player } hodí { $roll } na obranu.
pirates-defense-bonus = Bonus na obranu: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = Priamy zásah! Zasiahol si { $target }!
pirates-attack-hit-them = Bol si zasiahnutý hráčom { $attacker }!
pirates-attack-hit = { $attacker } zasiahne { $defender }!

# Combat - Miss results
pirates-attack-miss-you = Tvoja delová guľa minula { $target }.
pirates-attack-miss-them = Delová guľa ťa minula!
pirates-attack-miss = Delová guľa hráča { $attacker } minie { $defender }.

# Combat - Push
pirates-push-you = Tlačíš { $target } { $direction } na pozíciu { $position }!
pirates-push-them = { $attacker } ťa tlačí { $direction } na pozíciu { $position }!
pirates-push = { $attacker } tlačí { $defender } { $direction } z { $old_pos } na { $new_pos }.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } sa pokúša ukradnúť drahokam!
pirates-steal-rolls = Hod na krádež: { $steal } vs obrana: { $defend }
pirates-steal-success-you = Ukradol si { $gem } od { $target }!
pirates-steal-success-them = { $attacker } ti ukradol { $gem }!
pirates-steal-success = { $attacker } kradne { $gem } od { $defender }!
pirates-steal-failed = Pokus o krádež zlyhal!

# XP and Leveling
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player } dosiahol úroveň { $level }!
pirates-level-up-you = Dosiahol si úroveň { $level }!
pirates-level-up-multiple = { $player } získal { $levels } úrovní! Teraz úroveň { $level }!
pirates-level-up-multiple-you = Získal si { $levels } úrovní! Teraz úroveň { $level }!
pirates-skills-unlocked = { $player } odomkol nové schopnosti: { $skills }.
pirates-skills-unlocked-you = Odomkol si nové schopnosti: { $skills }.

# Skill activation
pirates-skill-activated = { $player } aktivuje { $skill }!
pirates-buff-expired = Bonus { $skill } hráča { $player } skončil.

# Sword Fighter skill
pirates-sword-fighter-activated = Bojovník s Mečom aktivovaný! +4 bonus na útok na { $turns } ťahov.

# Push skill (defense buff)
pirates-push-activated = Tlačenie aktivované! +3 bonus na obranu na { $turns } ťahov.

# Skilled Captain skill
pirates-skilled-captain-activated = Zručný Kapitán aktivovaný! +2 na útok a +2 na obranu na { $turns } ťahov.

# Double Devastation skill
pirates-double-devastation-activated = Dvojitá Devastácia aktivovaná! Dosah útoku zvýšený na 10 políčok na { $turns } ťahov.

# Battleship skill
pirates-battleship-activated = Bojová loď aktivovaná! Môžeš vystrel dva výstrely tento ťah!
pirates-battleship-no-targets = Žiadne ciele pre výstrel { $shot }.
pirates-battleship-shot = Strieľa sa výstrel { $shot }...

# Portal skill
pirates-portal-no-ships = Žiadne ďalšie lode na dohľad pre portál.
pirates-portal-fizzle = Portál hráča { $player } sa rozplynie bez cieľa.
pirates-portal-success = { $player } sa teleportuje do { $ocean } na pozíciu { $position }!

# Gem Seeker skill
pirates-gem-seeker-reveal = Moria šepkajú o { $gem } na pozícii { $position }. ({ $uses } použití zostáva)

# Level requirements
pirates-requires-level-15 = Vyžaduje úroveň 15
pirates-requires-level-150 = Vyžaduje úroveň 150

# XP Multiplier options
pirates-set-combat-xp-multiplier = násobič xp za boj: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = skúsenosti za boj
pirates-set-find-gem-xp-multiplier = násobič xp za nájdenie drahokamu: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = skúsenosti za nájdenie drahokamu

# Gem stealing options
pirates-set-gem-stealing = Krádež drahokamov: { $mode }
pirates-select-gem-stealing = Vyber režim krádeže drahokamov
pirates-option-changed-stealing = Krádež drahokamov nastavená na { $mode }.

# Gem stealing mode choices
pirates-stealing-with-bonus = S bonusom na hod
pirates-stealing-no-bonus = Bez bonusu na hod
pirates-stealing-disabled = Vypnuté
