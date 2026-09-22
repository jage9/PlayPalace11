# Messages du jeu Pirates of the Lost Seas

# Nom du jeu
game-name-pirates = Pirates of the Lost Seas

# Démarrage et configuration du jeu
pirates-welcome = Bienvenue à Pirates of the Lost Seas ! Naviguez sur les mers, collectez des gemmes et combattez d'autres pirates !
pirates-oceans = Votre voyage vous mènera à travers : { $oceans }
pirates-gems-placed = { $total } gemmes ont été dispersées à travers les mers. Trouvez-les toutes !
pirates-golden-moon = La Lune Dorée se lève ! Tous les gains d'XP sont triplés cette manche !

# Annonces de tour
pirates-turn = Tour de { $player }. Position { $position }

# Actions de mouvement
pirates-move-left = Naviguer à gauche
pirates-move-right = Naviguer à droite
pirates-move-2-left = Naviguer 2 cases à gauche
pirates-move-2-right = Naviguer 2 cases à droite
pirates-move-3-left = Naviguer 3 cases à gauche
pirates-move-3-right = Naviguer 3 cases à droite

# Messages de mouvement
pirates-move-you = Vous naviguez { $direction } à la position { $position }.
pirates-move-you-tiles = Vous naviguez { $tiles } cases { $direction } à la position { $position }.
pirates-move = { $player } navigue { $direction } à la position { $position }.
pirates-map-edge = Vous ne pouvez pas naviguer plus loin. Vous êtes à la position { $position }.

# Position et statut
pirates-check-status = Vérifier le statut
pirates-check-status-detailed = Statut détaillé
pirates-check-position = Vérifier la position
pirates-check-moon = Vérifier la luminosité de la lune
pirates-your-position = Votre position : { $position } dans { $ocean }
pirates-moon-brightness = La Lune Dorée est { $brightness }% lumineuse. ({ $collected } des { $total } gemmes ont été collectées).
pirates-no-golden-moon = La Lune Dorée ne peut pas être vue dans le ciel en ce moment.

# Collection de gemmes
pirates-gem-found-you = Vous avez trouvé un { $gem } ! Vaut { $value } points.
pirates-gem-found = { $player } a trouvé un { $gem } ! Vaut { $value } points.
pirates-all-gems-collected = Toutes les gemmes ont été collectées !

# Gagnant
pirates-winner = { $player } gagne avec { $score } points !

# Menu des compétences
pirates-use-skill = Utiliser une compétence
pirates-select-skill = Sélectionnez une compétence à utiliser

# Combat - Initiation d'attaque
pirates-cannonball = Tirer un boulet de canon
pirates-no-targets = Aucune cible dans les { $range } cases.
pirates-attack-you-fire = Vous tirez un boulet de canon sur { $target } !
pirates-attack-incoming = { $attacker } tire un boulet de canon sur vous !
pirates-attack-fired = { $attacker } tire un boulet de canon sur { $defender } !

# Combat - Lancers
pirates-attack-roll = Lancer d'attaque : { $roll }
pirates-attack-bonus = Bonus d'attaque : +{ $bonus }
pirates-defense-roll = Lancer de défense : { $roll }
pirates-defense-roll-others = { $player } lance { $roll } pour la défense.
pirates-defense-bonus = Bonus de défense : +{ $bonus }

# Combat - Résultats de touche
pirates-attack-hit-you = Coup direct ! Vous avez frappé { $target } !
pirates-attack-hit-them = Vous avez été touché par { $attacker } !
pirates-attack-hit = { $attacker } touche { $defender } !

# Combat - Résultats de manque
pirates-attack-miss-you = Votre boulet de canon a raté { $target }.
pirates-attack-miss-them = Le boulet de canon vous a raté !
pirates-attack-miss = Le boulet de canon de { $attacker } rate { $defender }.

# Combat - Poussée
pirates-push-you = Vous poussez { $target } { $direction } à la position { $position } !
pirates-push-them = { $attacker } vous pousse { $direction } à la position { $position } !
pirates-push = { $attacker } pousse { $defender } { $direction } de { $old_pos } à { $new_pos }.

# Combat - Vol de gemmes
pirates-steal-attempt = { $attacker } tente de voler une gemme !
pirates-steal-rolls = Lancer de vol : { $steal } vs défense : { $defend }
pirates-steal-success-you = Vous avez volé un { $gem } de { $target } !
pirates-steal-success-them = { $attacker } a volé votre { $gem } !
pirates-steal-success = { $attacker } vole un { $gem } de { $defender } !
pirates-steal-failed = La tentative de vol a échoué !

# XP et montée de niveau
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player } a atteint le niveau { $level } !
pirates-level-up-you = Vous avez atteint le niveau { $level } !
pirates-level-up-multiple = { $player } a gagné { $levels } niveaux ! Maintenant niveau { $level } !
pirates-level-up-multiple-you = Vous avez gagné { $levels } niveaux ! Maintenant niveau { $level } !
pirates-skills-unlocked = { $player } a débloqué de nouvelles compétences : { $skills }.
pirates-skills-unlocked-you = Vous avez débloqué de nouvelles compétences : { $skills }.

# Activation de compétence
pirates-skill-activated = { $player } active { $skill } !
pirates-buff-expired = Le buff { $skill } de { $player } s'est dissipé.

# Compétence Sword Fighter
pirates-sword-fighter-activated = Sword Fighter activé ! +4 bonus d'attaque pour { $turns } tours.

# Compétence Push (buff de défense)
pirates-push-activated = Push activé ! +3 bonus de défense pour { $turns } tours.

# Compétence Skilled Captain
pirates-skilled-captain-activated = Skilled Captain activé ! +2 attaque et +2 défense pour { $turns } tours.

# Compétence Double Devastation
pirates-double-devastation-activated = Double Devastation activé ! Portée d'attaque augmentée à 10 cases pour { $turns } tours.

# Compétence Battleship
pirates-battleship-activated = Battleship activé ! Vous pouvez tirer deux coups ce tour !
pirates-battleship-no-targets = Aucune cible pour le coup { $shot }.
pirates-battleship-shot = Tir du coup { $shot }...

# Compétence Portal
pirates-portal-no-ships = Aucun autre navire en vue pour se téléporter.
pirates-portal-fizzle = Le portail de { $player } s'évanouit sans destination.
pirates-portal-success = { $player } se téléporte à { $ocean } à la position { $position } !

# Compétence Gem Seeker
pirates-gem-seeker-reveal = Les mers murmurent d'un { $gem } à la position { $position }. ({ $uses } utilisations restantes)

# Exigences de niveau
pirates-requires-level-15 = Nécessite le niveau 15
pirates-requires-level-150 = Nécessite le niveau 150

# Options de multiplicateur d'XP
pirates-set-combat-xp-multiplier = multiplicateur d'xp de combat : { $combat_multiplier }
pirates-enter-combat-xp-multiplier = expérience pour le combat
pirates-set-find-gem-xp-multiplier = multiplicateur d'xp de recherche de gemme : { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = expérience pour trouver une gemme

# Options de vol de gemmes
pirates-set-gem-stealing = Vol de gemmes : { $mode }
pirates-select-gem-stealing = Sélectionnez le mode de vol de gemmes
pirates-option-changed-stealing = Vol de gemmes défini sur { $mode }.

# Choix de mode de vol de gemmes
pirates-stealing-with-bonus = Avec bonus de lancer
pirates-stealing-no-bonus = Sans bonus de lancer
pirates-stealing-disabled = Désactivé
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
