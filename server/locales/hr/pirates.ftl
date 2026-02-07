# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = Pirati Izgubljenih Mora

# Game start and setup
pirates-welcome = Dobrodošli u Pirati Izgubljenih Mora! Plovite morima, skupljajte dragulje i borite se s drugim piratima!
pirates-oceans = Vaše putovanje odvest će vas kroz: { $oceans }
pirates-gems-placed = { $total } dragulja rasuto je po morima. Pronađite ih sve!
pirates-golden-moon = Zlatni Mjesec izlazi! Svi XP dobici su utrostručeni ovu rundu!

# Turn announcements
pirates-turn = Red igrača { $player }. Pozicija { $position }

# Movement actions
pirates-move-left = Plovi lijevo
pirates-move-right = Plovi desno
pirates-move-2-left = Plovi 2 polja lijevo
pirates-move-2-right = Plovi 2 polja desno
pirates-move-3-left = Plovi 3 polja lijevo
pirates-move-3-right = Plovi 3 polja desno

# Movement messages
pirates-move-you = Plovite { $direction } na poziciju { $position }.
pirates-move-you-tiles = Plovite { $tiles } polja { $direction } na poziciju { $position }.
pirates-move = { $player } plovi { $direction } na poziciju { $position }.
pirates-map-edge = Ne možete ploviti dalje. Nalazite se na poziciji { $position }.

# Position and status
pirates-check-status = Provjeri status
pirates-check-position = Provjeri poziciju
pirates-check-moon = Provjeri sjaj mjeseca
pirates-your-position = Vaša pozicija: { $position } u { $ocean }
pirates-moon-brightness = Zlatni Mjesec sjaji { $brightness }%. ({ $collected } od { $total } dragulja je skupljeno).
pirates-no-golden-moon = Zlatni Mjesec se trenutno ne vidi na nebu.

# Gem collection
pirates-gem-found-you = Pronašli ste { $gem }! Vrijedi { $value } bodova.
pirates-gem-found = { $player } je pronašao { $gem }! Vrijedi { $value } bodova.
pirates-all-gems-collected = Svi dragulji su skupljeni!

# Winner
pirates-winner = { $player } pobjeđuje sa { $score } bodova!

# Skills menu
pirates-use-skill = Koristi vještinu
pirates-select-skill = Odaberite vještinu za korištenje

# Combat - Attack initiation
pirates-cannonball = Ispali topovsku kuglu
pirates-no-targets = Nema ciljeva unutar { $range } polja.
pirates-attack-you-fire = Ispalite topovsku kuglu na { $target }!
pirates-attack-incoming = { $attacker } ispaljuje topovsku kuglu na vas!
pirates-attack-fired = { $attacker } ispaljuje topovsku kuglu na { $defender }!

# Combat - Rolls
pirates-attack-roll = Napadački bacaj: { $roll }
pirates-attack-bonus = Napadački bonus: +{ $bonus }
pirates-defense-roll = Obrambeni bacaj: { $roll }
pirates-defense-roll-others = { $player } baca { $roll } za obranu.
pirates-defense-bonus = Obrambeni bonus: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = Direktan pogodak! Pogodili ste { $target }!
pirates-attack-hit-them = Pogođeni ste od { $attacker }!
pirates-attack-hit = { $attacker } pogađa { $defender }!

# Combat - Miss results
pirates-attack-miss-you = Vaša topovska kugla je promašila { $target }.
pirates-attack-miss-them = Topovska kugla vas je promašila!
pirates-attack-miss = Topovska kugla igrača { $attacker } promašuje { $defender }.

# Combat - Push
pirates-push-you = Gurate { $target } { $direction } na poziciju { $position }!
pirates-push-them = { $attacker } vas gura { $direction } na poziciju { $position }!
pirates-push = { $attacker } gura { $defender } { $direction } sa { $old_pos } na { $new_pos }.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } pokušava ukrasti dragulj!
pirates-steal-rolls = Bacaj krađe: { $steal } vs obrana: { $defend }
pirates-steal-success-you = Ukrali ste { $gem } od { $target }!
pirates-steal-success-them = { $attacker } je ukrao vaš { $gem }!
pirates-steal-success = { $attacker } krade { $gem } od { $defender }!
pirates-steal-failed = Pokušaj krađe nije uspio!

# XP and Leveling
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player } je dostigao razinu { $level }!
pirates-level-up-you = Dosegli ste razinu { $level }!
pirates-level-up-multiple = { $player } je dobio { $levels } razina! Sada razina { $level }!
pirates-level-up-multiple-you = Dobili ste { $levels } razina! Sada razina { $level }!
pirates-skills-unlocked = { $player } je otključao nove vještine: { $skills }.
pirates-skills-unlocked-you = Otključali ste nove vještine: { $skills }.

# Skill activation
pirates-skill-activated = { $player } aktivira { $skill }!
pirates-buff-expired = Bonus igrača { $player } za { $skill } je istekao.

# Sword Fighter skill
pirates-sword-fighter-activated = Mačevalac aktiviran! +4 napadački bonus za { $turns } poteza.

# Push skill (defense buff)
pirates-push-activated = Guranje aktivirano! +3 obrambeni bonus za { $turns } poteza.

# Skilled Captain skill
pirates-skilled-captain-activated = Vješti Kapetan aktiviran! +2 napad i +2 obrana za { $turns } poteza.

# Double Devastation skill
pirates-double-devastation-activated = Dvostruka Devastacija aktivirana! Domet napada povećan na 10 polja za { $turns } poteza.

# Battleship skill
pirates-battleship-activated = Bojni Brod aktiviran! Možete ispaliti dva hica ovaj potez!
pirates-battleship-no-targets = Nema ciljeva za hitac { $shot }.
pirates-battleship-shot = Ispaljivanje hica { $shot }...

# Portal skill
pirates-portal-no-ships = Nema drugih brodova u vidiku za portal.
pirates-portal-fizzle = Portal igrača { $player } se raspršuje bez odredišta.
pirates-portal-success = { $player } se portalizira u { $ocean } na poziciju { $position }!

# Gem Seeker skill
pirates-gem-seeker-reveal = Mora šapću o { $gem } na poziciji { $position }. ({ $uses } korištenja preostalo)

# Level requirements
pirates-requires-level-15 = Zahtijeva razinu 15
pirates-requires-level-150 = Zahtijeva razinu 150

# XP Multiplier options
pirates-set-combat-xp-multiplier = multiplikator XP-a za borbu: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = iskustvo za borbu
pirates-set-find-gem-xp-multiplier = multiplikator XP-a za pronalaženje dragulja: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = iskustvo za pronalaženje dragulja

# Gem stealing options
pirates-set-gem-stealing = Krađa dragulja: { $mode }
pirates-select-gem-stealing = Odaberite način krađe dragulja
pirates-option-changed-stealing = Krađa dragulja postavljena na { $mode }.

# Gem stealing mode choices
pirates-stealing-with-bonus = S bonusom bacaja
pirates-stealing-no-bonus = Bez bonusa bacaja
pirates-stealing-disabled = Onemogućeno
