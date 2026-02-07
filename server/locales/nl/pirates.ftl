# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = Pirates of the Lost Seas

# Game start and setup
pirates-welcome = Welkom bij Pirates of the Lost Seas! Vaar over de zeeën, verzamel edelstenen en vecht tegen andere piraten!
pirates-oceans = Je reis voert je door: { $oceans }
pirates-gems-placed = { $total } edelstenen zijn verspreid over de zeeën. Vind ze allemaal!
pirates-golden-moon = De Gouden Maan komt op! Alle XP winsten zijn drievoudig deze ronde!

# Turn announcements
pirates-turn = { $player } is aan de beurt. Positie { $position }

# Movement actions
pirates-move-left = Vaar naar links
pirates-move-right = Vaar naar rechts
pirates-move-2-left = Vaar 2 tegels naar links
pirates-move-2-right = Vaar 2 tegels naar rechts
pirates-move-3-left = Vaar 3 tegels naar links
pirates-move-3-right = Vaar 3 tegels naar rechts

# Movement messages
pirates-move-you = Je vaart { $direction } naar positie { $position }.
pirates-move-you-tiles = Je vaart { $tiles } tegels { $direction } naar positie { $position }.
pirates-move = { $player } vaart { $direction } naar positie { $position }.
pirates-map-edge = Je kunt niet verder varen. Je bent bij positie { $position }.

# Position and status
pirates-check-status = Bekijk status
pirates-check-position = Bekijk positie
pirates-check-moon = Bekijk maan helderheid
pirates-your-position = Jouw positie: { $position } in { $ocean }
pirates-moon-brightness = De Gouden Maan is { $brightness }% helder. ({ $collected } van { $total } edelstenen zijn verzameld).
pirates-no-golden-moon = De Gouden Maan is nu niet aan de hemel te zien.

# Gem collection
pirates-gem-found-you = Je vond een { $gem }! Waard { $value } punten.
pirates-gem-found = { $player } vond een { $gem }! Waard { $value } punten.
pirates-all-gems-collected = Alle edelstenen zijn verzameld!

# Winner
pirates-winner = { $player } wint met { $score } punten!

# Skills menu
pirates-use-skill = Gebruik vaardigheid
pirates-select-skill = Selecteer een vaardigheid om te gebruiken

# Combat - Attack initiation
pirates-cannonball = Vuur kanonskogel
pirates-no-targets = Geen doelen binnen { $range } tegels.
pirates-attack-you-fire = Je vuurt een kanonskogel naar { $target }!
pirates-attack-incoming = { $attacker } vuurt een kanonskogel naar jou!
pirates-attack-fired = { $attacker } vuurt een kanonskogel naar { $defender }!

# Combat - Rolls
pirates-attack-roll = Aanvalsworp: { $roll }
pirates-attack-bonus = Aanvalsbonus: +{ $bonus }
pirates-defense-roll = Verdedigingsworp: { $roll }
pirates-defense-roll-others = { $player } gooit { $roll } voor verdediging.
pirates-defense-bonus = Verdedigingsbonus: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = Voltreffer! Je raakte { $target }!
pirates-attack-hit-them = Je bent geraakt door { $attacker }!
pirates-attack-hit = { $attacker } raakt { $defender }!

# Combat - Miss results
pirates-attack-miss-you = Je kanonskogel miste { $target }.
pirates-attack-miss-them = De kanonskogel miste jou!
pirates-attack-miss = { $attacker }'s kanonskogel mist { $defender }.

# Combat - Push
pirates-push-you = Je duwt { $target } { $direction } naar positie { $position }!
pirates-push-them = { $attacker } duwt jou { $direction } naar positie { $position }!
pirates-push = { $attacker } duwt { $defender } { $direction } van { $old_pos } naar { $new_pos }.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } probeert een edelsteen te stelen!
pirates-steal-rolls = Steelworp: { $steal } tegen verdediging: { $defend }
pirates-steal-success-you = Je stal een { $gem } van { $target }!
pirates-steal-success-them = { $attacker } stal je { $gem }!
pirates-steal-success = { $attacker } steelt een { $gem } van { $defender }!
pirates-steal-failed = De steelpoging mislukte!

# XP and Leveling
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player } bereikte niveau { $level }!
pirates-level-up-you = Je bereikte niveau { $level }!
pirates-level-up-multiple = { $player } kreeg { $levels } niveaus! Nu niveau { $level }!
pirates-level-up-multiple-you = Je kreeg { $levels } niveaus! Nu niveau { $level }!
pirates-skills-unlocked = { $player } ontgrendelde nieuwe vaardigheden: { $skills }.
pirates-skills-unlocked-you = Je ontgrendelde nieuwe vaardigheden: { $skills }.

# Skill activation
pirates-skill-activated = { $player } activeert { $skill }!
pirates-buff-expired = { $player }'s { $skill } buff is uitgewerkt.

# Sword Fighter skill
pirates-sword-fighter-activated = Zwaardvechter geactiveerd! +4 aanvalsbonus voor { $turns } beurten.

# Push skill (defense buff)
pirates-push-activated = Duw geactiveerd! +3 verdedigingsbonus voor { $turns } beurten.

# Skilled Captain skill
pirates-skilled-captain-activated = Ervaren Kapitein geactiveerd! +2 aanval en +2 verdediging voor { $turns } beurten.

# Double Devastation skill
pirates-double-devastation-activated = Dubbele Vernietiging geactiveerd! Aanvalsbereik verhoogd naar 10 tegels voor { $turns } beurten.

# Battleship skill
pirates-battleship-activated = Slagschip geactiveerd! Je kunt twee schoten afvuren deze beurt!
pirates-battleship-no-targets = Geen doelen voor schot { $shot }.
pirates-battleship-shot = Schot { $shot } afvuren...

# Portal skill
pirates-portal-no-ships = Geen andere schepen in zicht om naar te portalen.
pirates-portal-fizzle = { $player }'s portal verdwijnt zonder bestemming.
pirates-portal-success = { $player } portalt naar { $ocean } op positie { $position }!

# Gem Seeker skill
pirates-gem-seeker-reveal = De zeeën fluisteren over een { $gem } op positie { $position }. ({ $uses } gebruik over)

# Level requirements
pirates-requires-level-15 = Vereist niveau 15
pirates-requires-level-150 = Vereist niveau 150

# XP Multiplier options
pirates-set-combat-xp-multiplier = gevecht xp vermenigvuldiger: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = ervaring voor gevecht
pirates-set-find-gem-xp-multiplier = edelsteen vinden xp vermenigvuldiger: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = ervaring voor het vinden van een edelsteen

# Gem stealing options
pirates-set-gem-stealing = Edelsteen stelen: { $mode }
pirates-select-gem-stealing = Selecteer edelsteen steelmodus
pirates-option-changed-stealing = Edelsteen stelen ingesteld op { $mode }.

# Gem stealing mode choices
pirates-stealing-with-bonus = Met worp bonus
pirates-stealing-no-bonus = Geen worp bonus
pirates-stealing-disabled = Uitgeschakeld
