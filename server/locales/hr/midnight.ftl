# 1-4-24 (Midnight) game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-midnight = 1-4-24
midnight-category = Igre s Kockicama

# Actions
midnight-roll = Bacite kockice
midnight-keep-die = Zadržite { $value }
midnight-bank = Potvrdite

# Game events
midnight-turn-start = Red igrača { $player }.
midnight-you-rolled = Bacili ste: { $dice }.
midnight-player-rolled = { $player } je bacio: { $dice }.

# Keeping dice
midnight-you-keep = Zadržavate { $die }.
midnight-player-keeps = { $player } zadržava { $die }.
midnight-you-unkeep = Otpuštate { $die }.
midnight-player-unkeeps = { $player } otpušta { $die }.

# Turn status
midnight-you-have-kept = Zadržane kockice: { $kept }. Preostali bacanja: { $remaining }.
midnight-player-has-kept = { $player } je zadržao: { $kept }. { $remaining } kockica preostalo.

# Scoring
midnight-you-scored = Osvojili ste { $score } bodova.
midnight-scored = { $player } je osvojio { $score } bodova.
midnight-you-disqualified = Nemate i 1 i 4. Diskvalificirani ste!
midnight-player-disqualified = { $player } nema i 1 i 4. Diskvalificiran!

# Round results
midnight-round-winner = { $player } pobjeđuje rundu!
midnight-round-tie = Runda neriješena između { $players }.
midnight-all-disqualified = Svi igrači diskvalificirani! Nema pobjednika ove runde.

# Game winner
midnight-game-winner = { $player } pobjeđuje igru sa { $wins } pobjeda u rundama!
midnight-game-tie = Neriješeno! { $players } svaki je osvojio { $wins } rundi.

# Options
midnight-set-rounds = Rundi za igranje: { $rounds }
midnight-enter-rounds = Unesite broj rundi za igranje:
midnight-option-changed-rounds = Rundi za igranje promijenjeno na { $rounds }

# Disabled reasons
midnight-need-to-roll = Morate prvo baciti kockice.
midnight-no-dice-to-keep = Nema dostupnih kockica za zadržavanje.
midnight-must-keep-one = Morate zadržati najmanje jednu kockicu po bacanju.
midnight-must-roll-first = Morate prvo baciti kockice.
midnight-keep-all-first = Morate zadržati sve kockice prije potvrđivanja.
