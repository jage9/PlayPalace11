# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = Pirates of the Lost Seas

# Game start and setup
pirates-welcome = Welcome to Pirates of the Lost Seas! Sail the seas, collect gems, and battle other pirates!
pirates-oceans = Your voyage will take you through: { $oceans }
pirates-gems-placed = { $total } gems have been scattered across the seas. Find them all!
pirates-golden-moon = The Golden Moon rises! All XP gains are tripled this round!

# Turn announcements
pirates-turn = { $player }'s turn. Position { $position }

# Movement actions
pirates-move-left = Sail left
pirates-move-right = Sail right
pirates-move-2-left = Sail 2 tiles left
pirates-move-2-right = Sail 2 tiles right
pirates-move-3-left = Sail 3 tiles left
pirates-move-3-right = Sail 3 tiles right

# Movement messages
pirates-move-you = You sail { $direction } to position { $position }.
pirates-move-you-tiles = You sail { $tiles } tiles { $direction } to position { $position }.
pirates-move = { $player } sails { $direction } to position { $position }.
pirates-map-edge = You cannot sail further. You are at position { $position }.

# Position and status
pirates-check-status = Check status
pirates-check-status-detailed = Szczegółowy status
pirates-check-position = Check position
pirates-check-moon = Check moon brightness
pirates-your-position = Your position: { $position } in { $ocean }
pirates-moon-brightness = The Golden Moon is { $brightness }% bright. ({ $collected } of { $total } gems have been collected).
pirates-no-golden-moon = The Golden Moon can not be seen up in the sky right now.

# Gem collection
pirates-gem-found-you = You found a { $gem }! Worth { $value } points.
pirates-gem-found = { $player } found a { $gem }! Worth { $value } points.
pirates-all-gems-collected = All gems have been collected!

# Winner
pirates-winner = { $player } wins with { $score } points!

# Skills menu
pirates-use-skill = Use skill
pirates-select-skill = Select a skill to use

# Combat - Attack initiation
pirates-cannonball = Fire cannonball
pirates-no-targets = No targets within { $range } tiles.
pirates-attack-you-fire = You fire a cannonball at { $target }!
pirates-attack-incoming = { $attacker } fires a cannonball at you!
pirates-attack-fired = { $attacker } fires a cannonball at { $defender }!

# Combat - Rolls
pirates-attack-roll = Attack roll: { $roll }
pirates-attack-bonus = Attack bonus: +{ $bonus }
pirates-defense-roll = Defense roll: { $roll }
pirates-defense-roll-others = { $player } rolls { $roll } for defense.
pirates-defense-bonus = Defense bonus: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = Direct hit! You struck { $target }!
pirates-attack-hit-them = You've been hit by { $attacker }!
pirates-attack-hit = { $attacker } hits { $defender }!

# Combat - Miss results
pirates-attack-miss-you = Your cannonball missed { $target }.
pirates-attack-miss-them = The cannonball missed you!
pirates-attack-miss = { $attacker }'s cannonball misses { $defender }.

# Combat - Push
pirates-push-you = You push { $target } { $direction } to position { $position }!
pirates-push-them = { $attacker } pushes you { $direction } to position { $position }!
pirates-push = { $attacker } pushes { $defender } { $direction } from { $old_pos } to { $new_pos }.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } attempts to steal a gem!
pirates-steal-rolls = Steal roll: { $steal } vs defense: { $defend }
pirates-steal-success-you = You stole a { $gem } from { $target }!
pirates-steal-success-them = { $attacker } stole your { $gem }!
pirates-steal-success = { $attacker } steals a { $gem } from { $defender }!
pirates-steal-failed = The steal attempt failed!

# XP and Leveling
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player } reached level { $level }!
pirates-level-up-you = You reached level { $level }!
pirates-level-up-multiple = { $player } gained { $levels } levels! Now level { $level }!
pirates-level-up-multiple-you = You gained { $levels } levels! Now level { $level }!
pirates-skills-unlocked = { $player } unlocked new skills: { $skills }.
pirates-skills-unlocked-you = You unlocked new skills: { $skills }.

# Skill activation
pirates-skill-activated = { $player } activates { $skill }!
pirates-buff-expired = { $player }'s { $skill } buff has worn off.

# Sword Fighter skill
pirates-sword-fighter-activated = Sword Fighter activated! +4 attack bonus for { $turns } turns.

# Push skill (defense buff)
pirates-push-activated = Push activated! +3 defense bonus for { $turns } turns.

# Skilled Captain skill
pirates-skilled-captain-activated = Skilled Captain activated! +2 attack and +2 defense for { $turns } turns.

# Double Devastation skill
pirates-double-devastation-activated = Double Devastation activated! Attack range increased to 10 tiles for { $turns } turns.

# Battleship skill
pirates-battleship-activated = Battleship activated! You can fire two shots this turn!
pirates-battleship-no-targets = No targets for shot { $shot }.
pirates-battleship-shot = Firing shot { $shot }...

# Portal skill
pirates-portal-no-ships = No other ships in sight to portal to.
pirates-portal-fizzle = { $player }'s portal fizzles out with no destination.
pirates-portal-success = { $player } portals to { $ocean } at position { $position }!

# Gem Seeker skill
pirates-gem-seeker-reveal = The seas whisper of a { $gem } at position { $position }. ({ $uses } uses remaining)

# Level requirements
pirates-requires-level-15 = Requires level 15
pirates-requires-level-150 = Requires level 150

# XP Multiplier options
pirates-set-combat-xp-multiplier = combat xp multiplier: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = experience for combat
pirates-set-find-gem-xp-multiplier = find gem xp multiplier: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = experience for finding a gem

# Gem stealing options
pirates-set-gem-stealing = Gem stealing: { $mode }
pirates-select-gem-stealing = Select gem stealing mode
pirates-option-changed-stealing = Gem stealing set to { $mode }.

# Gem stealing mode choices
pirates-stealing-with-bonus = With roll bonus
pirates-stealing-no-bonus = No roll bonus
pirates-stealing-disabled = Disabled
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
