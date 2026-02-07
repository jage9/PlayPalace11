# Toss Up game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-tossup = Metanje gor
tossup-category = Igre s kockami

# Actions
tossup-roll-first = Vrzi { $count } kock
tossup-roll-remaining = Vrzi preostale { $count } kocke
tossup-bank = Shrani { $points } točk

# Game events
tossup-turn-start = Poteza igralca { $player }. Rezultat: { $score }
tossup-you-roll = Vrgel si: { $results }.
tossup-player-rolls = { $player } je vrgel: { $results }.

# Turn status
tossup-you-have-points = Točke poteze: { $turn_points }. Preostale kocke: { $dice_count }.
tossup-player-has-points = { $player } ima { $turn_points } točk poteze. Preostalo { $dice_count } kock.

# Fresh dice
tossup-you-get-fresh = Ni več kock! Dobivaš { $count } novih kock.
tossup-player-gets-fresh = { $player } dobi { $count } novih kock.

# Bust
tossup-you-bust = Razpad! Izgubiš { $points } točk za to potezo.
tossup-player-busts = { $player } razpade in izgubi { $points } točk!

# Bank
tossup-you-bank = Shraniš { $points } točk. Skupni rezultat: { $total }.
tossup-player-banks = { $player } shrani { $points } točk. Skupni rezultat: { $total }.

# Winner
tossup-winner = { $player } zmaga s { $score } točkami!
tossup-tie-tiebreaker = Izenačeno med { $players }! Odločilna runda!

# Options
tossup-set-rules-variant = Različica pravil: { $variant }
tossup-select-rules-variant = Izberite različico pravil:
tossup-option-changed-rules = Različica pravil spremenjena v { $variant }

tossup-set-starting-dice = Začetne kocke: { $count }
tossup-enter-starting-dice = Vnesite število začetnih kock:
tossup-option-changed-dice = Začetne kocke spremenjene v { $count }

# Rules variants
tossup-rules-standard = Standardno
tossup-rules-playpalace = PlayPalace

# Rules explanations
tossup-rules-standard-desc = 3 zelene, 2 rumeni, 1 rdeča na kocko. Razpad če ni zelenih in vsaj ena rdeča.
tossup-rules-playpalace-desc = Enakomerna porazdelitev. Razpad če so vse kocke rdeče.

# Disabled reasons
tossup-need-points = Potrebuješ točke za shranjevanje.
