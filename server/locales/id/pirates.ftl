# Pirates of the Lost Seas game messages
# Note: Common messages like round-start, turn-start are in games.ftl

# Game name
game-name-pirates = Pirates of the Lost Seas

# Game start and setup
pirates-welcome = Selamat datang di Pirates of the Lost Seas! Berlayar di laut, kumpulkan permata, dan bertarung dengan bajak laut lain!
pirates-oceans = Perjalanan Anda akan membawa Anda melalui: { $oceans }
pirates-gems-placed = { $total } permata telah tersebar di seluruh laut. Temukan semuanya!
pirates-golden-moon = Bulan Emas terbit! Semua perolehan XP dikalikan tiga ronde ini!

# Turn announcements
pirates-turn = Giliran { $player }. Posisi { $position }

# Movement actions
pirates-move-left = Berlayar ke kiri
pirates-move-right = Berlayar ke kanan
pirates-move-2-left = Berlayar 2 ubin ke kiri
pirates-move-2-right = Berlayar 2 ubin ke kanan
pirates-move-3-left = Berlayar 3 ubin ke kiri
pirates-move-3-right = Berlayar 3 ubin ke kanan

# Movement messages
pirates-move-you = Anda berlayar ke { $direction } ke posisi { $position }.
pirates-move-you-tiles = Anda berlayar { $tiles } ubin ke { $direction } ke posisi { $position }.
pirates-move = { $player } berlayar ke { $direction } ke posisi { $position }.
pirates-map-edge = Anda tidak dapat berlayar lebih jauh. Anda berada di posisi { $position }.

# Position and status
pirates-check-status = Periksa status
pirates-check-position = Periksa posisi
pirates-check-moon = Periksa kecerahan bulan
pirates-your-position = Posisi Anda: { $position } di { $ocean }
pirates-moon-brightness = Bulan Emas { $brightness }% cerah. ({ $collected } dari { $total } permata telah dikumpulkan).
pirates-no-golden-moon = Bulan Emas tidak terlihat di langit sekarang.

# Gem collection
pirates-gem-found-you = Anda menemukan { $gem }! Bernilai { $value } poin.
pirates-gem-found = { $player } menemukan { $gem }! Bernilai { $value } poin.
pirates-all-gems-collected = Semua permata telah dikumpulkan!

# Winner
pirates-winner = { $player } menang dengan { $score } poin!

# Skills menu
pirates-use-skill = Gunakan skill
pirates-select-skill = Pilih skill untuk digunakan

# Combat - Attack initiation
pirates-cannonball = Tembakan meriam
pirates-no-targets = Tidak ada target dalam { $range } ubin.
pirates-attack-you-fire = Anda menembakkan meriam ke { $target }!
pirates-attack-incoming = { $attacker } menembakkan meriam ke Anda!
pirates-attack-fired = { $attacker } menembakkan meriam ke { $defender }!

# Combat - Rolls
pirates-attack-roll = Lemparan serangan: { $roll }
pirates-attack-bonus = Bonus serangan: +{ $bonus }
pirates-defense-roll = Lemparan pertahanan: { $roll }
pirates-defense-roll-others = { $player } melempar { $roll } untuk pertahanan.
pirates-defense-bonus = Bonus pertahanan: +{ $bonus }

# Combat - Hit results
pirates-attack-hit-you = Terkena langsung! Anda mengenai { $target }!
pirates-attack-hit-them = Anda telah terkena oleh { $attacker }!
pirates-attack-hit = { $attacker } mengenai { $defender }!

# Combat - Miss results
pirates-attack-miss-you = Meriam Anda meleset dari { $target }.
pirates-attack-miss-them = Meriam meleset dari Anda!
pirates-attack-miss = Meriam { $attacker } meleset dari { $defender }.

# Combat - Push
pirates-push-you = Anda mendorong { $target } ke { $direction } ke posisi { $position }!
pirates-push-them = { $attacker } mendorong Anda ke { $direction } ke posisi { $position }!
pirates-push = { $attacker } mendorong { $defender } ke { $direction } dari { $old_pos } ke { $new_pos }.

# Combat - Gem stealing
pirates-steal-attempt = { $attacker } mencoba mencuri permata!
pirates-steal-rolls = Lemparan mencuri: { $steal } vs pertahanan: { $defend }
pirates-steal-success-you = Anda mencuri { $gem } dari { $target }!
pirates-steal-success-them = { $attacker } mencuri { $gem } Anda!
pirates-steal-success = { $attacker } mencuri { $gem } dari { $defender }!
pirates-steal-failed = Upaya mencuri gagal!

# XP and Leveling
pirates-xp-gained = +{ $xp } XP
pirates-level-up = { $player } mencapai level { $level }!
pirates-level-up-you = Anda mencapai level { $level }!
pirates-level-up-multiple = { $player } naik { $levels } level! Sekarang level { $level }!
pirates-level-up-multiple-you = Anda naik { $levels } level! Sekarang level { $level }!
pirates-skills-unlocked = { $player } membuka skill baru: { $skills }.
pirates-skills-unlocked-you = Anda membuka skill baru: { $skills }.

# Skill activation
pirates-skill-activated = { $player } mengaktifkan { $skill }!
pirates-buff-expired = Buff { $skill } { $player } telah habis.

# Sword Fighter skill
pirates-sword-fighter-activated = Sword Fighter diaktifkan! Bonus serangan +4 selama { $turns } giliran.

# Push skill (defense buff)
pirates-push-activated = Push diaktifkan! Bonus pertahanan +3 selama { $turns } giliran.

# Skilled Captain skill
pirates-skilled-captain-activated = Skilled Captain diaktifkan! +2 serangan dan +2 pertahanan selama { $turns } giliran.

# Double Devastation skill
pirates-double-devastation-activated = Double Devastation diaktifkan! Jangkauan serangan meningkat menjadi 10 ubin selama { $turns } giliran.

# Battleship skill
pirates-battleship-activated = Battleship diaktifkan! Anda dapat menembak dua kali giliran ini!
pirates-battleship-no-targets = Tidak ada target untuk tembakan { $shot }.
pirates-battleship-shot = Menembak tembakan { $shot }...

# Portal skill
pirates-portal-no-ships = Tidak ada kapal lain yang terlihat untuk portal.
pirates-portal-fizzle = Portal { $player } gagal tanpa tujuan.
pirates-portal-success = { $player } berportal ke { $ocean } di posisi { $position }!

# Gem Seeker skill
pirates-gem-seeker-reveal = Laut membisikkan tentang { $gem } di posisi { $position }. ({ $uses } penggunaan tersisa)

# Level requirements
pirates-requires-level-15 = Memerlukan level 15
pirates-requires-level-150 = Memerlukan level 150

# XP Multiplier options
pirates-set-combat-xp-multiplier = pengganda xp pertempuran: { $combat_multiplier }
pirates-enter-combat-xp-multiplier = pengalaman untuk pertempuran
pirates-set-find-gem-xp-multiplier = pengganda xp menemukan permata: { $find_gem_multiplier }
pirates-enter-find-gem-xp-multiplier = pengalaman untuk menemukan permata

# Gem stealing options
pirates-set-gem-stealing = Pencurian permata: { $mode }
pirates-select-gem-stealing = Pilih mode pencurian permata
pirates-option-changed-stealing = Pencurian permata diatur ke { $mode }.

# Gem stealing mode choices
pirates-stealing-with-bonus = Dengan bonus lemparan
pirates-stealing-no-bonus = Tanpa bonus lemparan
pirates-stealing-disabled = Dinonaktifkan
