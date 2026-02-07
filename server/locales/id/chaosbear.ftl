# Chaos Bear game messages

# Game name
game-name-chaosbear = Chaos Bear

# Actions
chaosbear-roll-dice = Lempar dadu
chaosbear-draw-card = Ambil kartu
chaosbear-check-status = Periksa status

# Game intro (3 separate messages like v10)
chaosbear-intro-1 = Chaos Bear telah dimulai! Semua pemain mulai 30 kotak di depan beruang.
chaosbear-intro-2 = Lempar dadu untuk bergerak maju, dan ambil kartu pada kelipatan 5 untuk mendapat efek khusus.
chaosbear-intro-3 = Jangan biarkan beruang menangkap Anda!

# Turn announcement
chaosbear-turn = Giliran { $player }; kotak { $position }.

# Rolling
chaosbear-roll = { $player } melempar { $roll }.
chaosbear-position = { $player } sekarang di kotak { $position }.

# Drawing cards
chaosbear-draws-card = { $player } mengambil kartu.
chaosbear-card-impulsion = Dorongan! { $player } maju 3 kotak ke kotak { $position }!
chaosbear-card-super-impulsion = Dorongan super! { $player } maju 5 kotak ke kotak { $position }!
chaosbear-card-tiredness = Kelelahan! Energi beruang minus 1. Sekarang memiliki { $energy } energi.
chaosbear-card-hunger = Kelaparan! Energi beruang plus 1. Sekarang memiliki { $energy } energi.
chaosbear-card-backward = Dorongan mundur! { $player } mundur ke kotak { $position }.
chaosbear-card-random-gift = Hadiah acak!
chaosbear-gift-back = { $player } mundur ke kotak { $position }.
chaosbear-gift-forward = { $player } maju ke kotak { $position }!

# Bear turn
chaosbear-bear-roll = Beruang melempar { $roll } + { $energy } energinya = { $total }.
chaosbear-bear-energy-up = Beruang melempar 3 dan mendapat 1 energi!
chaosbear-bear-position = Beruang sekarang di kotak { $position }!
chaosbear-player-caught = Beruang menangkap { $player }! { $player } telah kalah!
chaosbear-bear-feast = Beruang kehilangan 3 energi setelah memangsa mereka!

# Status check
chaosbear-status-player-alive = { $player }: kotak { $position }.
chaosbear-status-player-caught = { $player }: tertangkap di kotak { $position }.
chaosbear-status-bear = Beruang di kotak { $position } dengan { $energy } energi.

# End game
chaosbear-winner = { $player } selamat dan menang! Mereka mencapai kotak { $position }!
chaosbear-tie = Seri di kotak { $position }!

# Disabled action reasons
chaosbear-you-are-caught = Anda telah ditangkap oleh beruang.
chaosbear-not-on-multiple = Anda hanya bisa mengambil kartu pada kelipatan 5.
