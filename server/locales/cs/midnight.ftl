# 1-4-24 (Midnight) - České zprávy hry

# Informace o hře
game-name-midnight = 1-4-24
midnight-category = Hry s kostkami

# Akce
midnight-roll = Hodit kostkami
midnight-keep-die = Držet { $value }
midnight-bank = Uložit

# Herní události
midnight-turn-start = Tah hráče { $player }.
midnight-you-rolled = Hodil jste: { $dice }.
midnight-player-rolled = { $player } hodil: { $dice }.

# Držení kostek
midnight-you-keep = Držíte { $die }.
midnight-player-keeps = { $player } drží { $die }.
midnight-you-unkeep = Uvolňujete { $die }.
midnight-player-unkeeps = { $player } uvolňuje { $die }.

# Stav tahu
midnight-you-have-kept = Držené kostky: { $kept }. Zbývající hody: { $remaining }.
midnight-player-has-kept = { $player } drží: { $kept }. Zbývá { $remaining } { $remaining ->
    [one] kostka
    [few] kostky
    [many] kostky
   *[other] kostek
}.

# Skórování
midnight-you-scored = Získal jste { $score } bodů.
midnight-scored = { $player } získal { $score } bodů.
midnight-you-disqualified = Nemáte obě 1 a 4. Diskvalifikován!
midnight-player-disqualified = { $player } nemá obě 1 a 4. Diskvalifikován!

# Výsledky kola
midnight-round-winner = { $player } vyhrává kolo!
midnight-round-tie = Remíza v kole mezi { $players }.
midnight-all-disqualified = Všichni hráči diskvalifikováni! Žádný vítěz tohoto kola.

# Vítěz hry
midnight-game-winner = { $player } vyhrává hru s { $wins } { $wins ->
    [one] výhrou
    [few] výhrami
    [many] výhry
   *[other] výhrami
} kol!
midnight-game-tie = Remíza! { $players } každý vyhrál { $wins } { $wins ->
    [one] kolo
    [few] kola
    [many] kola
   *[other] kol
}.

# Možnosti
midnight-set-rounds = Počet kol: { $rounds }
midnight-enter-rounds = Zadejte počet kol:
midnight-option-changed-rounds = Počet kol změněn na { $rounds }

# Důvody zakázání
midnight-need-to-roll = Musíte nejprve hodit kostkami.
midnight-no-dice-to-keep = Žádné dostupné kostky k držení.
midnight-must-keep-one = Musíte držet alespoň jednu kostku při každém hodu.
midnight-must-roll-first = Musíte nejprve hodit kostkami.
midnight-keep-all-first = Musíte držet všechny kostky před uložením.
