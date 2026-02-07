# Tradeoff - České zprávy hry

# Informace o hře
game-name-tradeoff = Tradeoff

# Průběh kola a iterací
tradeoff-round-start = Kolo { $round }.
tradeoff-iteration = Rozdání { $iteration } ze 3.

# Fáze 1: Obchodování
tradeoff-you-rolled = Hodil jste: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = obchodování
tradeoff-trade-status-keeping = držení
tradeoff-confirm-trades = Potvrdit obchody ({ $count } kostek)
tradeoff-keeping = Držení { $value }.
tradeoff-trading = Obchodování { $value }.
tradeoff-player-traded = { $player } obchodoval: { $dice }.
tradeoff-player-traded-none = { $player } si všechny kostky nechal.

# Fáze 2: Brání z poolu
tradeoff-your-turn-take = Váš tah vzít kostku z poolu.
tradeoff-take-die = Vzít { $value } (zbývá { $remaining })
tradeoff-you-take = Berete { $value }.
tradeoff-player-takes = { $player } bere { $value }.

# Fáze 3: Skórování
tradeoff-player-scored = { $player } ({ $points } bodů): { $sets }.
tradeoff-no-sets = { $player }: žádné sady.

# Popisy sad (stručně)
tradeoff-set-triple = trojice { $value }
tradeoff-set-group = skupina { $value }
tradeoff-set-mini-straight = malá postupka { $low }-{ $high }
tradeoff-set-double-triple = dvojitá trojice ({ $v1 } a { $v2 })
tradeoff-set-straight = postupka { $low }-{ $high }
tradeoff-set-double-group = dvojitá skupina ({ $v1 } a { $v2 })
tradeoff-set-all-groups = všechny skupiny
tradeoff-set-all-triplets = všechny trojice

# Konec kola
tradeoff-round-scores = Skóre kola { $round }:
tradeoff-score-line = { $player }: +{ $round_points } (celkem: { $total })
tradeoff-leader = { $player } vede s { $score }.

# Konec hry
tradeoff-winner = { $player } vyhrává s { $score } body!
tradeoff-winners-tie = Remíza! { $players } remizovali s { $score } body!

# Kontroly stavu
tradeoff-view-hand = Zobrazit vaši ruku
tradeoff-view-pool = Zobrazit pool
tradeoff-view-players = Zobrazit hráče
tradeoff-hand-display = Vaše ruka ({ $count } { $count ->
    [one] kostka
    [few] kostky
    [many] kostky
   *[other] kostek
}): { $dice }
tradeoff-pool-display = Pool ({ $count } { $count ->
    [one] kostka
    [few] kostky
    [many] kostky
   *[other] kostek
}): { $dice }
tradeoff-player-info = { $player }: { $hand }. Obchodováno: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. Nic neobchodováno.

# Chybové zprávy
tradeoff-not-trading-phase = Není fáze obchodování.
tradeoff-not-taking-phase = Není fáze brání.
tradeoff-already-confirmed = Již potvrzeno.
tradeoff-no-die = Žádná kostka k přepnutí.
tradeoff-no-more-takes = Žádná další brání nejsou k dispozici.
tradeoff-not-in-pool = Tato kostka není v poolu.

# Možnosti
tradeoff-set-target = Cílové skóre: { $score }
tradeoff-enter-target = Zadejte cílové skóre:
tradeoff-option-changed-target = Cílové skóre nastaveno na { $score }.
