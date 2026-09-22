# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = Pirates of the Lost Seas

# Game start and setup
pirates-welcome = ¡Bienvenido a Pirates of the Lost Seas! ¡Navega los mares, colecciona gemas y lucha contra otros piratas!
pirates-oceans = Tu viaje te llevará a través de: { $oceans }
pirates-gems-placed = { $total } gemas han sido dispersadas por los mares. ¡Encuéntralas todas!
pirates-golden-moon = ¡La Luna Dorada se eleva! Todas las ganancias de XP se triplican esta ronda!

# Turn announcements
pirates-turn = Turno de { $player }. Posición { $position }

# Movement actions
pirates-move-left = Navegar a la izquierda
pirates-move-right = Navegar a la derecha
pirates-move-2-left = Navegar 2 casillas a la izquierda
pirates-move-2-right = Navegar 2 casillas a la derecha
pirates-move-3-left = Navegar 3 casillas a la izquierda
pirates-move-3-right = Navegar 3 casillas a la derecha

# Movement messages
pirates-move-you = Navegas { $direction } a la posición { $position }.
pirates-move-you-tiles = Navegas { $tiles } casillas { $direction } a la posición { $position }.
pirates-move = { $player } navega { $direction } a la posición { $position }.
pirates-map-edge = No puedes navegar más lejos. Estás en la posición { $position }.

# Position and status
pirates-check-status = Verificar estado
pirates-check-status-detailed = Estado detallado
pirates-check-position = Verificar posición
pirates-check-moon = Verificar brillo de la luna
pirates-your-position = Tu posición: { $position } en { $ocean }
pirates-moon-brightness = La Luna Dorada está { $brightness }% brillante. ({ $collected } de { $total } gemas han sido coleccionadas).
pirates-no-golden-moon = La Luna Dorada no puede verse en el cielo ahora mismo.

# Gem collection
pirates-gem-found-you = ¡Encontraste una { $gem }! Vale { $value } puntos.
pirates-gem-found = ¡{ $player } encontró una { $gem }! Vale { $value } puntos.
pirates-all-gems-collected = ¡Todas las gemas han sido coleccionadas!

# Winner
pirates-winner = ¡{ $player } gana con { $score } puntos!

# Skills menu
pirates-use-skill = Usar habilidad
pirates-select-skill = Selecciona una habilidad para usar

# Combat - Attack initiation
pirates-cannonball = Disparar bala de cañón
pirates-no-targets = No hay objetivos dentro de { $range } casillas.
pirates-attack-you-fire = ¡Disparas una bala de cañón a { $target }!
pirates-attack-incoming = ¡{ $attacker } dispara una bala de cañón hacia ti!
pirates-attack-fired = ¡{ $attacker } dispara una bala de cañón a { $defender }!

# Combat - Rolls
pirates-attack-roll = Tirada de ataque: { $roll }
pirates-attack-bonus = Bono de ataque: +{ $bonus }
pirates-defense-roll = Tirada de defensa: { $roll }
pirates-defense-roll-others = { $player } saca { $roll } para defensa.
pirates-defense-bonus = Bono de defensa: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = ¡Impacto directo! ¡Golpeaste a { $target }!
pirates-attack-hit-them = ¡{ $attacker } te golpeó!
pirates-attack-hit = ¡{ $attacker } golpea a { $defender }!

# Combat - Miss results
pirates-attack-miss-you = Tu bala de cañón falló a { $target }.
pirates-attack-miss-them = ¡La bala de cañón te falló!
pirates-attack-miss = La bala de cañón de { $attacker } falla a { $defender }.

# Combat - Push
pirates-push-you = ¡Empujas a { $target } { $direction } a la posición { $position }!
pirates-push-them = ¡{ $attacker } te empuja { $direction } a la posición { $position }!
pirates-push = { $attacker } empuja a { $defender } { $direction } de { $old_pos } a { $new_pos }.

# Combat - Gem stealing
pirates-steal-attempt = ¡{ $attacker } intenta robar una gema!
pirates-steal-rolls = Tirada de robo: { $steal } vs defensa: { $defend }
pirates-steal-success-you = ¡Robaste una { $gem } de { $target }!
pirates-steal-success-them = ¡{ $attacker } robó tu { $gem }!
pirates-steal-success = ¡{ $attacker } roba una { $gem } de { $defender }!
pirates-steal-failed = ¡El intento de robo falló!

# XP and Leveling
pirates-xp-gained = +{ $xp } XP
pirates-level-up = ¡{ $player } alcanzó el nivel { $level }!
pirates-level-up-you = ¡Alcanzaste el nivel { $level }!
pirates-level-up-multiple = ¡{ $player } ganó { $levels } niveles! ¡Ahora nivel { $level }!
pirates-level-up-multiple-you = ¡Ganaste { $levels } niveles! ¡Ahora nivel { $level }!
pirates-skills-unlocked = { $player } desbloqueó nuevas habilidades: { $skills }.
pirates-skills-unlocked-you = Desbloqueaste nuevas habilidades: { $skills }.

# Skill activation
pirates-skill-activated = ¡{ $player } activa { $skill }!
pirates-buff-expired = El beneficio de { $skill } de { $player } se ha desvanecido.

# Sword Fighter skill
pirates-sword-fighter-activated = ¡Luchador de Espada activado! +4 bono de ataque por { $turns } turnos.

# Push skill (defense buff)
pirates-push-activated = ¡Empujón activado! +3 bono de defensa por { $turns } turnos.

# Skilled Captain skill
pirates-skilled-captain-activated = ¡Capitán Hábil activado! +2 ataque y +2 defensa por { $turns } turnos.

# Double Devastation skill
pirates-double-devastation-activated = ¡Doble Devastación activada! Rango de ataque aumentado a 10 casillas por { $turns } turnos.

# Battleship skill
pirates-battleship-activated = ¡Acorazado activado! ¡Puedes disparar dos tiros este turno!
pirates-battleship-no-targets = No hay objetivos para el tiro { $shot }.
pirates-battleship-shot = Disparando tiro { $shot }...

# Portal skill
pirates-portal-no-ships = No hay otros barcos a la vista para teletransportar.
pirates-portal-fizzle = El portal de { $player } se desvanece sin destino.
pirates-portal-success = ¡{ $player } se teletransporta a { $ocean } en la posición { $position }!

# Gem Seeker skill
pirates-gem-seeker-reveal = Los mares susurran de una { $gem } en la posición { $position }. ({ $uses } usos restantes)

# Level requirements
pirates-requires-level-15 = Requiere nivel 15
pirates-requires-level-150 = Requiere nivel 150

# XP Multiplier options
pirates-set-combat-xp-multiplier = multiplicador de xp de combate: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = experiencia por combate
pirates-set-find-gem-xp-multiplier = multiplicador de xp de encontrar gema: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = experiencia por encontrar una gema

# Gem stealing options
pirates-set-gem-stealing = Robo de gemas: { $mode }
pirates-select-gem-stealing = Selecciona el modo de robo de gemas
pirates-option-changed-stealing = Robo de gemas establecido en { $mode }.

# Gem stealing mode choices
pirates-stealing-with-bonus = Con bono de tirada
pirates-stealing-no-bonus = Sin bono de tirada
pirates-stealing-disabled = Deshabilitado
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
