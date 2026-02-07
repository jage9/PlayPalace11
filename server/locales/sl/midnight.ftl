# 1-4-24 (Midnight) game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-midnight = 1-4-24
midnight-category = Igre s Kockami

# Actions
midnight-roll = Vrzite kocke
midnight-keep-die = Obdržite { $value }
midnight-bank = Potrdite

# Game events
midnight-turn-start = Poteza igralca { $player }.
midnight-you-rolled = Vrgli ste: { $dice }.
midnight-player-rolled = { $player } je vrgel: { $dice }.

# Keeping dice
midnight-you-keep = Obdržite { $die }.
midnight-player-keeps = { $player } obdrži { $die }.
midnight-you-unkeep = Sprostite { $die }.
midnight-player-unkeeps = { $player } sprosti { $die }.

# Turn status
midnight-you-have-kept = Obdržane kocke: { $kept }. Preostali meti: { $remaining }.
midnight-player-has-kept = { $player } je obdržal: { $kept }. { $remaining } kock preostalih.

# Scoring
midnight-you-scored = Dosegli ste { $score } točk.
midnight-scored = { $player } je dosegel { $score } točk.
midnight-you-disqualified = Nimate niti 1 niti 4. Diskvalificirani ste!
midnight-player-disqualified = { $player } nima niti 1 niti 4. Diskvalificiran!

# Round results
midnight-round-winner = { $player } zmaga krog!
midnight-round-tie = Krog neodločen med { $players }.
midnight-all-disqualified = Vsi igralci diskvalificirani! Ni zmagovalca v tem krogu.

# Game winner
midnight-game-winner = { $player } zmaga igro z { $wins } zmagami kroga!
midnight-game-tie = Neodločeno! { $players } so vsak zmagali { $wins } krogov.

# Options
midnight-set-rounds = Krogi za igranje: { $rounds }
midnight-enter-rounds = Vnesite število krogov za igranje:
midnight-option-changed-rounds = Krogi za igranje spremenjeni na { $rounds }

# Disabled reasons
midnight-need-to-roll = Najprej morate vreči kocke.
midnight-no-dice-to-keep = Ni kock za obdržanje.
midnight-must-keep-one = Obdržati morate vsaj eno kocko na met.
midnight-must-roll-first = Najprej morate vreči kocke.
midnight-keep-all-first = Obdržati morate vse kocke pred potrditvijo.
