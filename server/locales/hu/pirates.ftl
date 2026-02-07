# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = A Elveszett Tengerek Kalózai

# Game start and setup
pirates-welcome = Üdvözöl az Elveszett Tengerek Kalózai! Vitorlázz a tengereken, gyűjts drágaköveket és küzdj más kalózokkal!
pirates-oceans = Az utazásod elvezet: { $oceans }
pirates-gems-placed = { $total } drágakő szét van szórva a tengereken. Találd meg mindegyiket!
pirates-golden-moon = Az Arany Hold felkel! Minden XP nyereség háromszorozódik ebben a körben!

# Turn announcements
pirates-turn = { $player } köre. Pozíció { $position }

# Movement actions
pirates-move-left = Vitorlázz balra
pirates-move-right = Vitorlázz jobbra
pirates-move-2-left = Vitorlázz 2 mezőt balra
pirates-move-2-right = Vitorlázz 2 mezőt jobbra
pirates-move-3-left = Vitorlázz 3 mezőt balra
pirates-move-3-right = Vitorlázz 3 mezőt jobbra

# Movement messages
pirates-move-you = { $direction } vitorlázol a { $position } pozícióra.
pirates-move-you-tiles = { $tiles } mezőt vitorlázol { $direction } a { $position } pozícióra.
pirates-move = { $player } { $direction } vitorlázik a { $position } pozícióra.
pirates-map-edge = Nem tudsz tovább vitorlázni. A { $position } pozíción vagy.

# Position and status
pirates-check-status = Státusz ellenőrzése
pirates-check-position = Pozíció ellenőrzése
pirates-check-moon = Hold fényesség ellenőrzése
pirates-your-position = Pozíciód: { $position } itt: { $ocean }
pirates-moon-brightness = Az Arany Hold { $brightness }% fényesen ragyog. ({ $collected } / { $total } drágakő összegyűjtve).
pirates-no-golden-moon = Az Arany Hold jelenleg nem látható az égen.

# Gem collection
pirates-gem-found-you = Találtál egy { $gem }-t! { $value } pontot ér.
pirates-gem-found = { $player } talált egy { $gem }-t! { $value } pontot ér.
pirates-all-gems-collected = Minden drágakő összegyűjtve!

# Winner
pirates-winner = { $player } nyer { $score } ponttal!

# Skills menu
pirates-use-skill = Képesség használata
pirates-select-skill = Válassz képességet

# Combat - Attack initiation
pirates-cannonball = Ágyúgolyó kilövése
pirates-no-targets = Nincs célpont { $range } mezőn belül.
pirates-attack-you-fire = Ágyúgolyót lősz { $target }-re!
pirates-attack-incoming = { $attacker } ágyúgolyót lő rád!
pirates-attack-fired = { $attacker } ágyúgolyót lő { $defender }-re!

# Combat - Rolls
pirates-attack-roll = Támadó dobás: { $roll }
pirates-attack-bonus = Támadó bónusz: +{ $bonus }
pirates-defense-roll = Védekező dobás: { $roll }
pirates-defense-roll-others = { $player } { $roll }-t dob védelem céljából.
pirates-defense-bonus = Védelmi bónusz: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = Telitalálat! Eltaláltad { $target }-t!
pirates-attack-hit-them = { $attacker } eltalált téged!
pirates-attack-hit = { $attacker } eltalálja { $defender }-t!

# Combat - Miss results
pirates-attack-miss-you = Az ágyúgolyód nem talált { $target }-re.
pirates-attack-miss-them = Az ágyúgolyó nem talált rád!
pirates-attack-miss = { $attacker } ágyúgolyója nem találja { $defender }-t.

# Combat - Push
pirates-push-you = Tolod { $target }-t { $direction } a { $position } pozícióra!
pirates-push-them = { $attacker } tol téged { $direction } a { $position } pozícióra!
pirates-push = { $attacker } tolja { $defender }-t { $direction } { $old_pos }-ről { $new_pos }-re.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } megpróbál ellopni egy drágakövet!
pirates-steal-rolls = Lopás dobás: { $steal } vs védelem: { $defend }
pirates-steal-success-you = Elloptál egy { $gem }-t { $target }-tól!
pirates-steal-success-them = { $attacker } ellopott egy { $gem }-t tőled!
pirates-steal-success = { $attacker } ellop egy { $gem }-t { $defender }-től!
pirates-steal-failed = A lopás kudarcot vallott!

# XP and Leveling
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player } elérte a { $level }. szintet!
pirates-level-up-you = Elérted a { $level }. szintet!
pirates-level-up-multiple = { $player } { $levels } szintet lépett! Most { $level }. szint!
pirates-level-up-multiple-you = { $levels } szintet léptél! Most { $level }. szint!
pirates-skills-unlocked = { $player } új képességeket nyitott: { $skills }.
pirates-skills-unlocked-you = Új képességeket nyitottál: { $skills }.

# Skill activation
pirates-skill-activated = { $player } aktiválja: { $skill }!
pirates-buff-expired = { $player } { $skill } bónusza lejárt.

# Sword Fighter skill
pirates-sword-fighter-activated = Kardforgató aktiválva! +4 támadó bónusz { $turns } körig.

# Push skill (defense buff)
pirates-push-activated = Tolás aktiválva! +3 védelmi bónusz { $turns } körig.

# Skilled Captain skill
pirates-skilled-captain-activated = Képzett Kapitány aktiválva! +2 támadás és +2 védelem { $turns } körig.

# Double Devastation skill
pirates-double-devastation-activated = Dupla Pusztítás aktiválva! Támadási távolság 10 mezőre nőtt { $turns } körig.

# Battleship skill
pirates-battleship-activated = Csatahajó aktiválva! Két lövést adhatsz le ebben a körben!
pirates-battleship-no-targets = Nincs célpont a { $shot }. lövéshez.
pirates-battleship-shot = { $shot }. lövés leadása...

# Portal skill
pirates-portal-no-ships = Nincs más hajó látótávolságban a portálhoz.
pirates-portal-fizzle = { $player } portálja elmúlik cél nélkül.
pirates-portal-success = { $player } portálozik { $ocean }-ba, { $position } pozícióra!

# Gem Seeker skill
pirates-gem-seeker-reveal = A tengerek suttognak egy { $gem }-ről a { $position } pozíción. ({ $uses } használat maradt)

# Level requirements
pirates-requires-level-15 = 15. szintet igényel
pirates-requires-level-150 = 150. szintet igényel

# XP Multiplier options
pirates-set-combat-xp-multiplier = harci xp szorzó: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = tapasztalat harcért
pirates-set-find-gem-xp-multiplier = drágakő találás xp szorzó: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = tapasztalat drágakő találásért

# Gem stealing options
pirates-set-gem-stealing = Drágakő lopás: { $mode }
pirates-select-gem-stealing = Válaszd ki a drágakő lopás módját
pirates-option-changed-stealing = Drágakő lopás beállítva: { $mode }.

# Gem stealing mode choices
pirates-stealing-with-bonus = Dobási bónusszal
pirates-stealing-no-bonus = Dobási bónusz nélkül
pirates-stealing-disabled = Letiltva
