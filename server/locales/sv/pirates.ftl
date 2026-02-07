# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = Piraterna från de Förlorade Haven

# Game start and setup
pirates-welcome = Välkommen till Piraterna från de Förlorade Haven! Segla på haven, samla ädelstenar och kämpa mot andra pirater!
pirates-oceans = Din resa kommer att ta dig genom: { $oceans }
pirates-gems-placed = { $total } ädelstenar har spridits över haven. Hitta dem alla!
pirates-golden-moon = Den Gyllene Månen stiger! Alla XP-vinster tredubblas denna runda!

# Turn announcements
pirates-turn = { $player }s tur. Position { $position }

# Movement actions
pirates-move-left = Segla vänster
pirates-move-right = Segla höger
pirates-move-2-left = Segla 2 rutor vänster
pirates-move-2-right = Segla 2 rutor höger
pirates-move-3-left = Segla 3 rutor vänster
pirates-move-3-right = Segla 3 rutor höger

# Movement messages
pirates-move-you = Du seglar { $direction } till position { $position }.
pirates-move-you-tiles = Du seglar { $tiles } rutor { $direction } till position { $position }.
pirates-move = { $player } seglar { $direction } till position { $position }.
pirates-map-edge = Du kan inte segla längre. Du är vid position { $position }.

# Position and status
pirates-check-status = Kontrollera status
pirates-check-position = Kontrollera position
pirates-check-moon = Kontrollera månens ljusstyrka
pirates-your-position = Din position: { $position } i { $ocean }
pirates-moon-brightness = Den Gyllene Månen lyser { $brightness }%. ({ $collected } av { $total } ädelstenar har samlats).
pirates-no-golden-moon = Den Gyllene Månen kan inte ses på himlen just nu.

# Gem collection
pirates-gem-found-you = Du hittade en { $gem }! Värd { $value } poäng.
pirates-gem-found = { $player } hittade en { $gem }! Värd { $value } poäng.
pirates-all-gems-collected = Alla ädelstenar har samlats!

# Winner
pirates-winner = { $player } vinner med { $score } poäng!

# Skills menu
pirates-use-skill = Använd förmåga
pirates-select-skill = Välj en förmåga att använda

# Combat - Attack initiation
pirates-cannonball = Avfyra kanonkula
pirates-no-targets = Inga mål inom { $range } rutor.
pirates-attack-you-fire = Du avfyrar en kanonkula mot { $target }!
pirates-attack-incoming = { $attacker } avfyrar en kanonkula mot dig!
pirates-attack-fired = { $attacker } avfyrar en kanonkula mot { $defender }!

# Combat - Rolls
pirates-attack-roll = Attackkast: { $roll }
pirates-attack-bonus = Attackbonus: +{ $bonus }
pirates-defense-roll = Försvarskast: { $roll }
pirates-defense-roll-others = { $player } kastar { $roll } för försvar.
pirates-defense-bonus = Försvarsbonus: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = Direktträff! Du träffade { $target }!
pirates-attack-hit-them = Du blev träffad av { $attacker }!
pirates-attack-hit = { $attacker } träffar { $defender }!

# Combat - Miss results
pirates-attack-miss-you = Din kanonkula missade { $target }.
pirates-attack-miss-them = Kanonkulan missade dig!
pirates-attack-miss = { $attacker }s kanonkula missar { $defender }.

# Combat - Push
pirates-push-you = Du knuffar { $target } { $direction } till position { $position }!
pirates-push-them = { $attacker } knuffar dig { $direction } till position { $position }!
pirates-push = { $attacker } knuffar { $defender } { $direction } från { $old_pos } till { $new_pos }.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } försöker stjäla en ädelsten!
pirates-steal-rolls = Stöldkast: { $steal } mot försvar: { $defend }
pirates-steal-success-you = Du stal en { $gem } från { $target }!
pirates-steal-success-them = { $attacker } stal din { $gem }!
pirates-steal-success = { $attacker } stjäl en { $gem } från { $defender }!
pirates-steal-failed = Stöldförsöket misslyckades!

# XP and Leveling
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player } nådde nivå { $level }!
pirates-level-up-you = Du nådde nivå { $level }!
pirates-level-up-multiple = { $player } fick { $levels } nivåer! Nu nivå { $level }!
pirates-level-up-multiple-you = Du fick { $levels } nivåer! Nu nivå { $level }!
pirates-skills-unlocked = { $player } låste upp nya förmågor: { $skills }.
pirates-skills-unlocked-you = Du låste upp nya förmågor: { $skills }.

# Skill activation
pirates-skill-activated = { $player } aktiverar { $skill }!
pirates-buff-expired = { $player }s { $skill }-bonus har upphört.

# Sword Fighter skill
pirates-sword-fighter-activated = Svärdkämpe aktiverad! +4 attackbonus i { $turns } drag.

# Push skill (defense buff)
pirates-push-activated = Knuff aktiverad! +3 försvarsbonus i { $turns } drag.

# Skilled Captain skill
pirates-skilled-captain-activated = Skicklig Kapten aktiverad! +2 attack och +2 försvar i { $turns } drag.

# Double Devastation skill
pirates-double-devastation-activated = Dubbel Förödelse aktiverad! Attackräckvidd ökad till 10 rutor i { $turns } drag.

# Battleship skill
pirates-battleship-activated = Slagskepp aktiverat! Du kan avfyra två skott detta drag!
pirates-battleship-no-targets = Inga mål för skott { $shot }.
pirates-battleship-shot = Avfyrar skott { $shot }...

# Portal skill
pirates-portal-no-ships = Inga andra skepp i sikte för portal.
pirates-portal-fizzle = { $player }s portal försvinner utan destination.
pirates-portal-success = { $player } teleporterar till { $ocean } vid position { $position }!

# Gem Seeker skill
pirates-gem-seeker-reveal = Haven viskar om en { $gem } vid position { $position }. ({ $uses } användningar kvar)

# Level requirements
pirates-requires-level-15 = Kräver nivå 15
pirates-requires-level-150 = Kräver nivå 150

# XP Multiplier options
pirates-set-combat-xp-multiplier = strid xp-multiplikator: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = erfarenhet för strid
pirates-set-find-gem-xp-multiplier = hitta ädelsten xp-multiplikator: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = erfarenhet för att hitta en ädelsten

# Gem stealing options
pirates-set-gem-stealing = Ädelstenstöld: { $mode }
pirates-select-gem-stealing = Välj ädelstenstöldläge
pirates-option-changed-stealing = Ädelstenstöld inställd på { $mode }.

# Gem stealing mode choices
pirates-stealing-with-bonus = Med kastbonus
pirates-stealing-no-bonus = Ingen kastbonus
pirates-stealing-disabled = Inaktiverad
