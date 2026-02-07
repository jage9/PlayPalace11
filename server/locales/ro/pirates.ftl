# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = Pirații Mărilor Pierdute

# Game start and setup
pirates-welcome = Bine ai venit la Pirații Mărilor Pierdute! Navighează pe mări, colectează gemme și luptă cu alți pirați!
pirates-oceans = Călătoria ta te va duce prin: { $oceans }
pirates-gems-placed = { $total } gemme au fost împrăștiate pe mări. Găsește-le pe toate!
pirates-golden-moon = Luna de Aur răsare! Toate câștigurile XP sunt triplate în această rundă!

# Turn announcements
pirates-turn = Tura lui { $player }. Poziția { $position }

# Movement actions
pirates-move-left = Navighează la stânga
pirates-move-right = Navighează la dreapta
pirates-move-2-left = Navighează 2 casete la stânga
pirates-move-2-right = Navighează 2 casete la dreapta
pirates-move-3-left = Navighează 3 casete la stânga
pirates-move-3-right = Navighează 3 casete la dreapta

# Movement messages
pirates-move-you = Navighezi { $direction } la poziția { $position }.
pirates-move-you-tiles = Navighezi { $tiles } casete { $direction } la poziția { $position }.
pirates-move = { $player } navighează { $direction } la poziția { $position }.
pirates-map-edge = Nu poți naviga mai departe. Ești la poziția { $position }.

# Position and status
pirates-check-status = Verifică starea
pirates-check-position = Verifică poziția
pirates-check-moon = Verifică luminozitatea lunii
pirates-your-position = Poziția ta: { $position } în { $ocean }
pirates-moon-brightness = Luna de Aur este luminoasă { $brightness }%. ({ $collected } din { $total } gemme au fost colectate).
pirates-no-golden-moon = Luna de Aur nu poate fi văzută pe cer acum.

# Gem collection
pirates-gem-found-you = Ai găsit un { $gem }! Valorează { $value } puncte.
pirates-gem-found = { $player } a găsit un { $gem }! Valorează { $value } puncte.
pirates-all-gems-collected = Toate gemmele au fost colectate!

# Winner
pirates-winner = { $player } câștigă cu { $score } puncte!

# Skills menu
pirates-use-skill = Folosește abilitate
pirates-select-skill = Selectează o abilitate de folosit

# Combat - Attack initiation
pirates-cannonball = Trage cu tunul
pirates-no-targets = Nicio țintă în raza de { $range } casete.
pirates-attack-you-fire = Tragi cu tunul la { $target }!
pirates-attack-incoming = { $attacker } trage cu tunul la tine!
pirates-attack-fired = { $attacker } trage cu tunul la { $defender }!

# Combat - Rolls
pirates-attack-roll = Aruncare atac: { $roll }
pirates-attack-bonus = Bonus atac: +{ $bonus }
pirates-defense-roll = Aruncare apărare: { $roll }
pirates-defense-roll-others = { $player } aruncă { $roll } pentru apărare.
pirates-defense-bonus = Bonus apărare: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = Lovitură directă! Ai lovit { $target }!
pirates-attack-hit-them = Ai fost lovit de { $attacker }!
pirates-attack-hit = { $attacker } lovește { $defender }!

# Combat - Miss results
pirates-attack-miss-you = Glonțul tău de tun a ratat { $target }.
pirates-attack-miss-them = Glonțul de tun te-a ratat!
pirates-attack-miss = Glonțul de tun al lui { $attacker } ratează { $defender }.

# Combat - Push
pirates-push-you = Îl împingi pe { $target } { $direction } la poziția { $position }!
pirates-push-them = { $attacker } te împinge { $direction } la poziția { $position }!
pirates-push = { $attacker } împinge { $defender } { $direction } de la { $old_pos } la { $new_pos }.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } încearcă să fure o gemmă!
pirates-steal-rolls = Aruncare furt: { $steal } vs apărare: { $defend }
pirates-steal-success-you = Ai furat un { $gem } de la { $target }!
pirates-steal-success-them = { $attacker } ți-a furat { $gem }!
pirates-steal-success = { $attacker } fură un { $gem } de la { $defender }!
pirates-steal-failed = Încercarea de furt a eșuat!

# XP and Leveling
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player } a ajuns la nivelul { $level }!
pirates-level-up-you = Ai ajuns la nivelul { $level }!
pirates-level-up-multiple = { $player } a câștigat { $levels } nivele! Acum nivelul { $level }!
pirates-level-up-multiple-you = Ai câștigat { $levels } nivele! Acum nivelul { $level }!
pirates-skills-unlocked = { $player } a deblocat abilități noi: { $skills }.
pirates-skills-unlocked-you = Ai deblocat abilități noi: { $skills }.

# Skill activation
pirates-skill-activated = { $player } activează { $skill }!
pirates-buff-expired = Bonusul { $skill } al lui { $player } s-a încheiat.

# Sword Fighter skill
pirates-sword-fighter-activated = Luptător cu Sabia activat! +4 bonus atac pentru { $turns } ture.

# Push skill (defense buff)
pirates-push-activated = Împingere activată! +3 bonus apărare pentru { $turns } ture.

# Skilled Captain skill
pirates-skilled-captain-activated = Căpitan Calificat activat! +2 atac și +2 apărare pentru { $turns } ture.

# Double Devastation skill
pirates-double-devastation-activated = Devastare Dublă activată! Raza de atac crescută la 10 casete pentru { $turns } ture.

# Battleship skill
pirates-battleship-activated = Crucișător activat! Poți trage două focuri în această tură!
pirates-battleship-no-targets = Nicio țintă pentru focul { $shot }.
pirates-battleship-shot = Tragând focul { $shot }...

# Portal skill
pirates-portal-no-ships = Nicio altă navă în vedere pentru portal.
pirates-portal-fizzle = Portalul lui { $player } dispare fără destinație.
pirates-portal-success = { $player } se teleportează la { $ocean } la poziția { $position }!

# Gem Seeker skill
pirates-gem-seeker-reveal = Mările șoptesc despre un { $gem } la poziția { $position }. ({ $uses } utilizări rămase)

# Level requirements
pirates-requires-level-15 = Necesită nivelul 15
pirates-requires-level-150 = Necesită nivelul 150

# XP Multiplier options
pirates-set-combat-xp-multiplier = multiplicator xp luptă: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = experiență pentru luptă
pirates-set-find-gem-xp-multiplier = multiplicator xp găsire gemmă: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = experiență pentru găsirea unei gemme

# Gem stealing options
pirates-set-gem-stealing = Furt de gemme: { $mode }
pirates-select-gem-stealing = Selectează modul de furt de gemme
pirates-option-changed-stealing = Furt de gemme setat la { $mode }.

# Gem stealing mode choices
pirates-stealing-with-bonus = Cu bonus aruncare
pirates-stealing-no-bonus = Fără bonus aruncare
pirates-stealing-disabled = Dezactivat
