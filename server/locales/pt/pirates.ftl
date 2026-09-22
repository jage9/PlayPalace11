# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = Piratas dos Mares Perdidos

# Game start and setup
pirates-welcome = Bem-vindo aos Piratas dos Mares Perdidos! Navegue pelos mares, colete gemas e lute contra outros piratas!
pirates-oceans = Sua viagem o levará através de: { $oceans }
pirates-gems-placed = { $total } gemas foram espalhadas pelos mares. Encontre todas!
pirates-golden-moon = A Lua Dourada nasce! Todos os ganhos de XP são triplicados nesta rodada!

# Turn announcements
pirates-turn = Turno de { $player }. Posição { $position }

# Movement actions
pirates-move-left = Navegar à esquerda
pirates-move-right = Navegar à direita
pirates-move-2-left = Navegar 2 casas à esquerda
pirates-move-2-right = Navegar 2 casas à direita
pirates-move-3-left = Navegar 3 casas à esquerda
pirates-move-3-right = Navegar 3 casas à direita

# Movement messages
pirates-move-you = Você navega { $direction } para a posição { $position }.
pirates-move-you-tiles = Você navega { $tiles } casas { $direction } para a posição { $position }.
pirates-move = { $player } navega { $direction } para a posição { $position }.
pirates-map-edge = Você não pode navegar mais longe. Você está na posição { $position }.

# Position and status
pirates-check-status = Verificar status
pirates-check-status-detailed = Status detalhado
pirates-check-position = Verificar posição
pirates-check-moon = Verificar brilho da lua
pirates-your-position = Sua posição: { $position } em { $ocean }
pirates-moon-brightness = A Lua Dourada está { $brightness }% brilhante. ({ $collected } de { $total } gemas foram coletadas).
pirates-no-golden-moon = A Lua Dourada não pode ser vista no céu agora.

# Gem collection
pirates-gem-found-you = Você encontrou uma { $gem }! Vale { $value } pontos.
pirates-gem-found = { $player } encontrou uma { $gem }! Vale { $value } pontos.
pirates-all-gems-collected = Todas as gemas foram coletadas!

# Winner
pirates-winner = { $player } vence com { $score } pontos!

# Skills menu
pirates-use-skill = Usar habilidade
pirates-select-skill = Selecione uma habilidade para usar

# Combat - Attack initiation
pirates-cannonball = Disparar bala de canhão
pirates-no-targets = Nenhum alvo a { $range } casas.
pirates-attack-you-fire = Você dispara uma bala de canhão em { $target }!
pirates-attack-incoming = { $attacker } dispara uma bala de canhão em você!
pirates-attack-fired = { $attacker } dispara uma bala de canhão em { $defender }!

# Combat - Rolls
pirates-attack-roll = Rolagem de ataque: { $roll }
pirates-attack-bonus = Bônus de ataque: +{ $bonus }
pirates-defense-roll = Rolagem de defesa: { $roll }
pirates-defense-roll-others = { $player } tira { $roll } para defesa.
pirates-defense-bonus = Bônus de defesa: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = Acerto direto! Você atingiu { $target }!
pirates-attack-hit-them = Você foi atingido por { $attacker }!
pirates-attack-hit = { $attacker } atinge { $defender }!

# Combat - Miss results
pirates-attack-miss-you = Sua bala de canhão errou { $target }.
pirates-attack-miss-them = A bala de canhão errou você!
pirates-attack-miss = A bala de canhão de { $attacker } erra { $defender }.

# Combat - Push
pirates-push-you = Você empurra { $target } { $direction } para a posição { $position }!
pirates-push-them = { $attacker } empurra você { $direction } para a posição { $position }!
pirates-push = { $attacker } empurra { $defender } { $direction } de { $old_pos } para { $new_pos }.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } tenta roubar uma gema!
pirates-steal-rolls = Rolagem de roubo: { $steal } vs defesa: { $defend }
pirates-steal-success-you = Você roubou uma { $gem } de { $target }!
pirates-steal-success-them = { $attacker } roubou sua { $gem }!
pirates-steal-success = { $attacker } rouba uma { $gem } de { $defender }!
pirates-steal-failed = A tentativa de roubo falhou!

# XP and Leveling
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player } alcançou o nível { $level }!
pirates-level-up-you = Você alcançou o nível { $level }!
pirates-level-up-multiple = { $player } ganhou { $levels } níveis! Agora nível { $level }!
pirates-level-up-multiple-you = Você ganhou { $levels } níveis! Agora nível { $level }!
pirates-skills-unlocked = { $player } desbloqueou novas habilidades: { $skills }.
pirates-skills-unlocked-you = Você desbloqueou novas habilidades: { $skills }.

# Skill activation
pirates-skill-activated = { $player } ativa { $skill }!
pirates-buff-expired = O bônus de { $skill } de { $player } acabou.

# Sword Fighter skill
pirates-sword-fighter-activated = Lutador de Espada ativado! +4 bônus de ataque por { $turns } turnos.

# Push skill (defense buff)
pirates-push-activated = Empurrão ativado! +3 bônus de defesa por { $turns } turnos.

# Skilled Captain skill
pirates-skilled-captain-activated = Capitão Habilidoso ativado! +2 ataque e +2 defesa por { $turns } turnos.

# Double Devastation skill
pirates-double-devastation-activated = Devastação Dupla ativada! Alcance de ataque aumentado para 10 casas por { $turns } turnos.

# Battleship skill
pirates-battleship-activated = Navio de Guerra ativado! Você pode disparar dois tiros neste turno!
pirates-battleship-no-targets = Nenhum alvo para o tiro { $shot }.
pirates-battleship-shot = Disparando tiro { $shot }...

# Portal skill
pirates-portal-no-ships = Nenhum outro navio à vista para teletransportar.
pirates-portal-fizzle = O portal de { $player } desaparece sem destino.
pirates-portal-success = { $player } se teletransporta para { $ocean } na posição { $position }!

# Gem Seeker skill
pirates-gem-seeker-reveal = Os mares sussurram sobre uma { $gem } na posição { $position }. ({ $uses } usos restantes)

# Level requirements
pirates-requires-level-15 = Requer nível 15
pirates-requires-level-150 = Requer nível 150

# XP Multiplier options
pirates-set-combat-xp-multiplier = multiplicador de xp de combate: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = experiência por combate
pirates-set-find-gem-xp-multiplier = multiplicador de xp de encontrar gema: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = experiência por encontrar uma gema

# Gem stealing options
pirates-set-gem-stealing = Roubo de gemas: { $mode }
pirates-select-gem-stealing = Selecione o modo de roubo de gemas
pirates-option-changed-stealing = Roubo de gemas definido para { $mode }.

# Gem stealing mode choices
pirates-stealing-with-bonus = Com bônus de rolagem
pirates-stealing-no-bonus = Sem bônus de rolagem
pirates-stealing-disabled = Desativado
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
