# Pirates of the Lost Seas-Spielnachrichten
# Hinweis: Gemeinsame Nachrichten wie round-start, turn-start sind in games.ftl

# Spielname
game-name-pirates = Pirates of the Lost Seas

# Spielstart und Setup
pirates-welcome = Willkommen bei Pirates of the Lost Seas! Segeln Sie über die Meere, sammeln Sie Edelsteine und kämpfen Sie gegen andere Piraten!
pirates-oceans = Ihre Reise führt Sie durch: { $oceans }
pirates-gems-placed = { $total } Edelsteine wurden über die Meere verstreut. Finden Sie sie alle!
pirates-golden-moon = Der Goldene Mond steigt auf! Alle XP-Gewinne werden in dieser Runde verdreifacht!

# Zugankündigungen
pirates-turn = { $player } ist am Zug. Position { $position }

# Bewegungsaktionen
pirates-move-left = Nach links segeln
pirates-move-right = Nach rechts segeln
pirates-move-2-left = 2 Felder nach links segeln
pirates-move-2-right = 2 Felder nach rechts segeln
pirates-move-3-left = 3 Felder nach links segeln
pirates-move-3-right = 3 Felder nach rechts segeln

# Bewegungsnachrichten
pirates-move-you = Sie segeln { $direction } zur Position { $position }.
pirates-move-you-tiles = Sie segeln { $tiles } Felder { $direction } zur Position { $position }.
pirates-move = { $player } segelt { $direction } zur Position { $position }.
pirates-map-edge = Sie können nicht weiter segeln. Sie sind an Position { $position }.

# Position und Status
pirates-check-status = Status prüfen
pirates-check-status-detailed = Detaillierter Status
pirates-check-position = Position prüfen
pirates-check-moon = Mondhelligkeit prüfen
pirates-your-position = Ihre Position: { $position } in { $ocean }
pirates-moon-brightness = Der Goldene Mond ist { $brightness }% hell. ({ $collected } von { $total } Edelsteinen wurden gesammelt).
pirates-no-golden-moon = Der Goldene Mond kann momentan nicht am Himmel gesehen werden.

# Edelsteinsammlung
pirates-gem-found-you = Sie fanden einen { $gem }! Wert { $value } Punkte.
pirates-gem-found = { $player } fand einen { $gem }! Wert { $value } Punkte.
pirates-all-gems-collected = Alle Edelsteine wurden gesammelt!

# Gewinner
pirates-winner = { $player } gewinnt mit { $score } Punkten!

# Fähigkeitenmenü
pirates-use-skill = Fähigkeit verwenden
pirates-select-skill = Wählen Sie eine Fähigkeit zum Verwenden

# Kampf - Angriffseinleitung
pirates-cannonball = Kanonenkugel abfeuern
pirates-no-targets = Keine Ziele innerhalb von { $range } Feldern.
pirates-attack-you-fire = Sie feuern eine Kanonenkugel auf { $target }!
pirates-attack-incoming = { $attacker } feuert eine Kanonenkugel auf Sie!
pirates-attack-fired = { $attacker } feuert eine Kanonenkugel auf { $defender }!

# Kampf - Würfe
pirates-attack-roll = Angriffswurf: { $roll }
pirates-attack-bonus = Angriffsbonus: +{ $bonus }
pirates-defense-roll = Verteidigungswurf: { $roll }
pirates-defense-roll-others = { $player } würfelt { $roll } zur Verteidigung.
pirates-defense-bonus = Verteidigungsbonus: +{ $bonus }

# Kampf - Trefferergebnisse
pirates-attack-hit-you = Direkter Treffer! Sie trafen { $target }!
pirates-attack-hit-them = Sie wurden von { $attacker } getroffen!
pirates-attack-hit = { $attacker } trifft { $defender }!

# Kampf - Verfehlergebnisse
pirates-attack-miss-you = Ihre Kanonenkugel verfehlte { $target }.
pirates-attack-miss-them = Die Kanonenkugel verfehlte Sie!
pirates-attack-miss = { $attacker }s Kanonenkugel verfehlt { $defender }.

# Kampf - Stoßen
pirates-push-you = Sie stoßen { $target } { $direction } zur Position { $position }!
pirates-push-them = { $attacker } stößt Sie { $direction } zur Position { $position }!
pirates-push = { $attacker } stößt { $defender } { $direction } von { $old_pos } zu { $new_pos }.

# Kampf - Edelsteinstehlen
pirates-steal-attempt = { $attacker } versucht, einen Edelstein zu stehlen!
pirates-steal-rolls = Stiehlwurf: { $steal } gegen Verteidigung: { $defend }
pirates-steal-success-you = Sie stahlen einen { $gem } von { $target }!
pirates-steal-success-them = { $attacker } stahl Ihren { $gem }!
pirates-steal-success = { $attacker } stiehlt einen { $gem } von { $defender }!
pirates-steal-failed = Der Diebstahlversuch schlug fehl!

# XP und Levelaufstieg
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player } erreichte Level { $level }!
pirates-level-up-you = Sie erreichten Level { $level }!
pirates-level-up-multiple = { $player } gewann { $levels } Level! Jetzt Level { $level }!
pirates-level-up-multiple-you = Sie gewannen { $levels } Level! Jetzt Level { $level }!
pirates-skills-unlocked = { $player } schaltete neue Fähigkeiten frei: { $skills }.
pirates-skills-unlocked-you = Sie schalteten neue Fähigkeiten frei: { $skills }.

# Fähigkeitsaktivierung
pirates-skill-activated = { $player } aktiviert { $skill }!
pirates-buff-expired = { $player }s { $skill }-Verstärkung hat sich verflüchtigt.

# Sword Fighter-Fähigkeit
pirates-sword-fighter-activated = Sword Fighter aktiviert! +4 Angriffsbonus für { $turns } Züge.

# Push-Fähigkeit (Verteidigungsverstärkung)
pirates-push-activated = Push aktiviert! +3 Verteidigungsbonus für { $turns } Züge.

# Skilled Captain-Fähigkeit
pirates-skilled-captain-activated = Skilled Captain aktiviert! +2 Angriff und +2 Verteidigung für { $turns } Züge.

# Double Devastation-Fähigkeit
pirates-double-devastation-activated = Double Devastation aktiviert! Angriffsreichweite auf 10 Felder erhöht für { $turns } Züge.

# Battleship-Fähigkeit
pirates-battleship-activated = Battleship aktiviert! Sie können in diesem Zug zwei Schüsse abfeuern!
pirates-battleship-no-targets = Keine Ziele für Schuss { $shot }.
pirates-battleship-shot = Feuere Schuss { $shot }...

# Portal-Fähigkeit
pirates-portal-no-ships = Keine anderen Schiffe in Sicht, um zu portalen.
pirates-portal-fizzle = { $player }s Portal verpufft ohne Ziel.
pirates-portal-success = { $player } portalt nach { $ocean } an Position { $position }!

# Gem Seeker-Fähigkeit
pirates-gem-seeker-reveal = Die Meere flüstern von einem { $gem } an Position { $position }. ({ $uses } Verwendungen verbleiben)

# Level-Anforderungen
pirates-requires-level-15 = Benötigt Level 15
pirates-requires-level-150 = Benötigt Level 150

# XP-Multiplikator-Optionen
pirates-set-combat-xp-multiplier = Kampf-XP-Multiplikator: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = Erfahrung für Kampf
pirates-set-find-gem-xp-multiplier = Edelstein-Fund-XP-Multiplikator: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = Erfahrung für das Finden eines Edelsteins

# Edelsteinstehlen-Optionen
pirates-set-gem-stealing = Edelsteinstehlen: { $mode }
pirates-select-gem-stealing = Edelsteinstehlen-Modus auswählen
pirates-option-changed-stealing = Edelsteinstehlen auf { $mode } gesetzt.

# Edelsteinstehlen-Modus-Auswahlmöglichkeiten
pirates-stealing-with-bonus = Mit Wurfbonus
pirates-stealing-no-bonus = Ohne Wurfbonus
pirates-stealing-disabled = Deaktiviert
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
