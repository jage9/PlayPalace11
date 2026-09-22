# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = Gusari izgubljenih mora

# Game start and setup
pirates-welcome = Dobro došli u gusare izgubljenih mora! Plovite morima, skupljajte dragulje, i borite se sa drugim gusarima!
pirates-oceans = Vaše putovanje će vas sprovesti kroz: { $oceans }
pirates-gems-placed = { $total } dragulja je rašireno kroz mora. Pronađite ih sve!
pirates-golden-moon = Zlatni mesec je osvetljen! Sva dobijanja iskustva se utrostručuju u ovom potezu!

# Turn announcements
pirates-turn = { $player } je na potezu. Pozicija { $position }

# Movement actions
pirates-move-left = Plovi levo
pirates-move-right = Plovi desno
pirates-move-2-left = Plovi dva polja levo
pirates-move-2-right = Plovi dva polja desno
pirates-move-3-left = Plovi tri polja levo
pirates-move-3-right = Plovi tri polja desno

# Movement messages
pirates-move-you = Plovite { $direction } na poziciju { $position }.
pirates-move-you-tiles = Plovite { $tiles } polja { $direction } na poziciju { $position }.
pirates-move = { $player } plovi { $direction } na poziciju { $position }.
pirates-map-edge = Ne možete više da plovite. Vi ste na poziciji { $position }.

# Position and status
pirates-check-status = Proveri status
pirates-check-status-detailed = Detaljni status
pirates-check-position = Proveri poziciju
pirates-check-moon = Proveri osvetljenje meseca
pirates-your-position = Vaša pozicija: { $position } u okejanu { $ocean }
pirates-moon-brightness = Osvetljenje zlatnog meseca je { $brightness }%. ({ $collected } od { $total } dragulja je prikupljeno).
pirates-no-golden-moon = Zlatni mesec se trenutno ne može videti na nebu.

# Gem collection
pirates-gem-found-you = Pronašli ste dragulj { $gem }! Vredi { $value } poena.
pirates-gem-found = { $player } pronalazi dragulj { $gem }! Vredi { $value } poena.
pirates-all-gems-collected = Svi dragulji su prikupljeni!

# Winner
pirates-winner = { $player } pobeđuje sa { $score } poena!

# Skills menu
pirates-use-skill = Koristi veštinu
pirates-select-skill = Izaberite veštinu za korišćenje

# Combat - Attack initiation
pirates-cannonball = Pucaj torpedom
pirates-no-targets = Nema protivnika koji su { $range } polja od vas.
pirates-attack-you-fire = pucate torpedom na igrača { $target }!
pirates-attack-incoming = { $attacker } puca torpedom u vas!
pirates-attack-fired = { $attacker } puca torpedom na igrača { $defender }!

# Combat - Rolls
pirates-attack-roll = Bacanje napada: { $roll }
pirates-attack-bonus = Bonus napada: +{ $bonus }
pirates-defense-roll = Bacanje odbrane: { $roll }
pirates-defense-roll-others = { $player } dobija { $roll } za odbranu.
pirates-defense-bonus = Bonus odbrane: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = Direktan udarac! Upucali ste { $target }!
pirates-attack-hit-them = Upucani ste od igrača { $attacker }!
pirates-attack-hit = { $attacker } pogađa igrača { $defender }!

# Combat - Miss results
pirates-attack-miss-you = Vaš torpedo je promašio igrača { $target }.
pirates-attack-miss-them = Torpedo vas je promašio!
pirates-attack-miss = Torpedo igrača { $attacker } promašuje igrača { $defender }.

# Combat - Push
pirates-push-you = Gurate igrača { $target } { $direction } na poziciju { $position }!
pirates-push-them = { $attacker } vas gura { $direction } na poziciju { $position }!
pirates-push = { $attacker } gura igrača { $defender } { $direction } sa { $old_pos } na { $new_pos }.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } pokušava da ukrade dragulj!
pirates-steal-rolls = Bacanje kradljivca: { $steal } Protiv odbrane: { $defend }
pirates-steal-success-you = Ukrali ste  { $gem } igraču { $target }!
pirates-steal-success-them = { $attacker } vam krade { $gem }!
pirates-steal-success = { $attacker } krade { $gem } od igrača { $defender }!
pirates-steal-failed = Pokušaj krađe je propao!

# XP and Leveling
pirates-xp-gained = +{ $xp } iskustva
pirates-level-up = { $player } dostiže nivo { $level }!
pirates-level-up-you = Dostigli ste nivo { $level }!
pirates-level-up-multiple = { $player } dobija { $levels } nivoa! Sada je na nivou { $level }!
pirates-level-up-multiple-you = Dobili ste { $levels } nivoa! Sada ste na nivou { $level }!
pirates-skills-unlocked = { $player } otključava nove veštine: { $skills }.
pirates-skills-unlocked-you = Otključali ste nove veštine: { $skills }.

# Skill activation
pirates-skill-activated = { $player } aktivira veštinu { $skill }!
pirates-buff-expired = Bonus igrača { $player } { $skill } je istekao.

# Sword Fighter skill
pirates-sword-fighter-activated = Mačevalac aktiviran! +4 bonus za napad na { $turns } poteza.

# Push skill (defense buff)
pirates-push-activated = Guranje aktivirano! +3 bonus za odbranu na { $turns } poteza.

# Skilled Captain skill
pirates-skilled-captain-activated = Vešt kapetan aktiviran! +2 napad i +2 odbrana na { $turns } poteza.

# Double Devastation skill
pirates-double-devastation-activated = Dvostruka pustoš aktivirana! Opseg napada povećan na 10 polja na { $turns } poteza.

# Battleship skill
pirates-battleship-activated = Mornarica aktivirana! Možete da pucate dva puta u ovom potezu!
pirates-battleship-no-targets = Nema protivnika za pucanje { $shot }.
pirates-battleship-shot = Pucanje { $shot }...

# Portal skill
pirates-portal-no-ships = Nema drugih brodova u blizini u koje se možete teleportovati.
pirates-portal-fizzle = Portal igrača { $player } se ispraznio bez cilja.
pirates-portal-success = { $player } se teleportuje u { $ocean } na poziciji { $position }!

# Gem Seeker skill
pirates-gem-seeker-reveal = Mora šapuću o dragulju { $gem } na poziciji { $position }. ({ $uses } korišćenja preostalo)

# Level requirements
pirates-requires-level-15 = zahteva nivo 15
pirates-requires-level-150 = Zahteva nivo 150

# XP Multiplier options
pirates-set-combat-xp-multiplier = Množilac borbenog iskustva: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = Iskustvo za borbu
pirates-set-find-gem-xp-multiplier = Množilac iskustva za pronalazak dragulja: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = Iskustvo za pronalazak dragulja

# Gem stealing options
pirates-set-gem-stealing = Krađa dragulja: { $mode }
pirates-select-gem-stealing = Izaberite režim krađe dragulja
pirates-option-changed-stealing = Krađa dragulja podešena na { $mode }.

# Gem stealing mode choices
pirates-stealing-with-bonus = Uz bonus bacanja
pirates-stealing-no-bonus = Bez bonusa bacanja
pirates-stealing-disabled = Onemogućeno
# Skill/status messages use the English locale fallback until translated.
pirates-skill-name-cannonball = Cannonball Shot
pirates-skill-name-instinct = Sailor's Instinct
pirates-skill-name-portal = Portal
pirates-skill-name-gem-seeker = Gem Seeker
pirates-skill-name-sword-fighter = Sword Fighter
pirates-skill-name-push = Push
pirates-skill-name-skilled-captain = Skilled Captain
pirates-skill-name-battleship = Battleship
pirates-skill-name-double-devastation = Double Devastation
pirates-skill-requires-level = Requires level { $level }
pirates-skill-already-active = { $skill } is already active ({ $turns } turns remaining)
pirates-skill-on-cooldown = { $skill } is on cooldown ({ $turns } turns)
pirates-skill-active = { $skill } (active: { $turns } turns)
pirates-skill-cooldown = { $skill } (cooldown: { $turns } turns)
pirates-skill-activate = { $skill } (activate)
pirates-skill-no-uses = { $skill } (no uses remaining)
pirates-skill-uses-left = { $skill } ({ $uses } uses left)
pirates-portal-menu = { $skill } (teleport to occupied ocean)
pirates-battleship-menu = { $skill } (fire extra shot)
pirates-not-your-turn = Not your turn
pirates-no-uses-remaining = No uses remaining
pirates-cannot-battleship-double = Cannot use Battleship while Double Devastation is active
pirates-no-targets-in-range = No targets in range
pirates-unknown = Unknown
pirates-map-sectors = Map Sectors:
pirates-charted-full = Fully charted
pirates-charted-partial = Partially charted ({ $count }/5)
pirates-charted-none = Uncharted
pirates-sector = Sector { $sector } ({ $start }-{ $end }): { $status }
pirates-status-player = { $player }: Level { $level }, { $xp } XP, { $score } points, { $gems }
