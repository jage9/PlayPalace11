# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = Pirati dei Mari Perduti

# Game start and setup
pirates-welcome = Benvenuto a Pirati dei Mari Perduti! Naviga i mari, raccogli gemme e combatti altri pirati!
pirates-oceans = Il tuo viaggio ti porterà attraverso: { $oceans }
pirates-gems-placed = { $total } gemme sono state sparse nei mari. Trovale tutte!
pirates-golden-moon = La Luna d'Oro sorge! Tutti i guadagni XP sono triplicati questo turno!

# Turn announcements
pirates-turn = Turno di { $player }. Posizione { $position }

# Movement actions
pirates-move-left = Naviga a sinistra
pirates-move-right = Naviga a destra
pirates-move-2-left = Naviga 2 caselle a sinistra
pirates-move-2-right = Naviga 2 caselle a destra
pirates-move-3-left = Naviga 3 caselle a sinistra
pirates-move-3-right = Naviga 3 caselle a destra

# Movement messages
pirates-move-you = Navighi { $direction } alla posizione { $position }.
pirates-move-you-tiles = Navighi { $tiles } caselle { $direction } alla posizione { $position }.
pirates-move = { $player } naviga { $direction } alla posizione { $position }.
pirates-map-edge = Non puoi navigare oltre. Sei alla posizione { $position }.

# Position and status
pirates-check-status = Controlla stato
pirates-check-position = Controlla posizione
pirates-check-moon = Controlla luminosità della luna
pirates-your-position = Tua posizione: { $position } in { $ocean }
pirates-moon-brightness = La Luna d'Oro è luminosa al { $brightness }%. ({ $collected } di { $total } gemme sono state raccolte).
pirates-no-golden-moon = La Luna d'Oro non può essere vista nel cielo in questo momento.

# Gem collection
pirates-gem-found-you = Hai trovato un { $gem }! Vale { $value } punti.
pirates-gem-found = { $player } ha trovato un { $gem }! Vale { $value } punti.
pirates-all-gems-collected = Tutte le gemme sono state raccolte!

# Winner
pirates-winner = { $player } vince con { $score } punti!

# Skills menu
pirates-use-skill = Usa abilità
pirates-select-skill = Seleziona un'abilità da usare

# Combat - Attack initiation
pirates-cannonball = Spara palla di cannone
pirates-no-targets = Nessun bersaglio entro { $range } caselle.
pirates-attack-you-fire = Spari una palla di cannone a { $target }!
pirates-attack-incoming = { $attacker } spara una palla di cannone a te!
pirates-attack-fired = { $attacker } spara una palla di cannone a { $defender }!

# Combat - Rolls
pirates-attack-roll = Tiro d'attacco: { $roll }
pirates-attack-bonus = Bonus attacco: +{ $bonus }
pirates-defense-roll = Tiro di difesa: { $roll }
pirates-defense-roll-others = { $player } tira { $roll } per la difesa.
pirates-defense-bonus = Bonus difesa: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = Colpo diretto! Hai colpito { $target }!
pirates-attack-hit-them = Sei stato colpito da { $attacker }!
pirates-attack-hit = { $attacker } colpisce { $defender }!

# Combat - Miss results
pirates-attack-miss-you = La tua palla di cannone ha mancato { $target }.
pirates-attack-miss-them = La palla di cannone ti ha mancato!
pirates-attack-miss = La palla di cannone di { $attacker } manca { $defender }.

# Combat - Push
pirates-push-you = Spingi { $target } { $direction } alla posizione { $position }!
pirates-push-them = { $attacker } ti spinge { $direction } alla posizione { $position }!
pirates-push = { $attacker } spinge { $defender } { $direction } da { $old_pos } a { $new_pos }.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } tenta di rubare una gemma!
pirates-steal-rolls = Tiro furto: { $steal } vs difesa: { $defend }
pirates-steal-success-you = Hai rubato un { $gem } da { $target }!
pirates-steal-success-them = { $attacker } ha rubato il tuo { $gem }!
pirates-steal-success = { $attacker } ruba un { $gem } da { $defender }!
pirates-steal-failed = Il tentativo di furto è fallito!

# XP and Leveling
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player } ha raggiunto il livello { $level }!
pirates-level-up-you = Hai raggiunto il livello { $level }!
pirates-level-up-multiple = { $player } ha guadagnato { $levels } livelli! Ora livello { $level }!
pirates-level-up-multiple-you = Hai guadagnato { $levels } livelli! Ora livello { $level }!
pirates-skills-unlocked = { $player } ha sbloccato nuove abilità: { $skills }.
pirates-skills-unlocked-you = Hai sbloccato nuove abilità: { $skills }.

# Skill activation
pirates-skill-activated = { $player } attiva { $skill }!
pirates-buff-expired = Il bonus { $skill } di { $player } è terminato.

# Sword Fighter skill
pirates-sword-fighter-activated = Spadaccino attivato! +4 bonus attacco per { $turns } turni.

# Push skill (defense buff)
pirates-push-activated = Spinta attivata! +3 bonus difesa per { $turns } turni.

# Skilled Captain skill
pirates-skilled-captain-activated = Capitano Abile attivato! +2 attacco e +2 difesa per { $turns } turni.

# Double Devastation skill
pirates-double-devastation-activated = Devastazione Doppia attivata! Raggio d'attacco aumentato a 10 caselle per { $turns } turni.

# Battleship skill
pirates-battleship-activated = Corazzata attivata! Puoi sparare due colpi questo turno!
pirates-battleship-no-targets = Nessun bersaglio per il colpo { $shot }.
pirates-battleship-shot = Sparando colpo { $shot }...

# Portal skill
pirates-portal-no-ships = Nessuna nave in vista per il portale.
pirates-portal-fizzle = Il portale di { $player } svanisce senza destinazione.
pirates-portal-success = { $player } si teletrasporta a { $ocean } alla posizione { $position }!

# Gem Seeker skill
pirates-gem-seeker-reveal = I mari sussurrano di un { $gem } alla posizione { $position }. ({ $uses } usi rimanenti)

# Level requirements
pirates-requires-level-15 = Richiede livello 15
pirates-requires-level-150 = Richiede livello 150

# XP Multiplier options
pirates-set-combat-xp-multiplier = moltiplicatore xp combattimento: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = esperienza per combattimento
pirates-set-find-gem-xp-multiplier = moltiplicatore xp trova gemma: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = esperienza per trovare una gemma

# Gem stealing options
pirates-set-gem-stealing = Furto gemme: { $mode }
pirates-select-gem-stealing = Seleziona modalità furto gemme
pirates-option-changed-stealing = Furto gemme impostato a { $mode }.

# Gem stealing mode choices
pirates-stealing-with-bonus = Con bonus tiro
pirates-stealing-no-bonus = Senza bonus tiro
pirates-stealing-disabled = Disabilitato
