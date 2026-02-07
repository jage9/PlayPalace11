# Tradeoff game messages

# Game info
game-name-tradeoff = Zamenjava

# Round and iteration flow
tradeoff-round-start = Krog { $round }.
tradeoff-iteration = Roka { $iteration } od 3.

# Phase 1: Trading
tradeoff-you-rolled = Vrgli ste: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = zamenjava
tradeoff-trade-status-keeping = obdrži
tradeoff-confirm-trades = Potrdite zamenjave ({ $count } kock)
tradeoff-keeping = Obdržanje { $value }.
tradeoff-trading = Zamenjava { $value }.
tradeoff-player-traded = { $player } je zamenjal: { $dice }.
tradeoff-player-traded-none = { $player } je obdržal vse kocke.

# Phase 2: Taking from pool
tradeoff-your-turn-take = Vaša poteza za vzeti kocko iz sklada.
tradeoff-take-die = Vzemite { $value } (ostalo { $remaining })
tradeoff-you-take = Vzamete { $value }.
tradeoff-player-takes = { $player } vzame { $value }.

# Phase 3: Scoring
tradeoff-player-scored = { $player } ({ $points } toč.): { $sets }.
tradeoff-no-sets = { $player }: ni nizov.

# Set descriptions (concise)
tradeoff-set-triple = trojček { $value }
tradeoff-set-group = skupina { $value }
tradeoff-set-mini-straight = mini lestvica { $low }-{ $high }
tradeoff-set-double-triple = dvojni trojček ({ $v1 } in { $v2 })
tradeoff-set-straight = lestvica { $low }-{ $high }
tradeoff-set-double-group = dvojna skupina ({ $v1 } in { $v2 })
tradeoff-set-all-groups = vse skupine
tradeoff-set-all-triplets = vsi trojčki

# Round end
tradeoff-round-scores = Rezultati kroga { $round }:
tradeoff-score-line = { $player }: +{ $round_points } (skupaj: { $total })
tradeoff-leader = { $player } vodi z { $score }.

# Game end
tradeoff-winner = { $player } zmaga s { $score } točkami!
tradeoff-winners-tie = Neodločeno! { $players } neodločeno s { $score } točkami!

# Status checks
tradeoff-view-hand = Oglejte si svojo roko
tradeoff-view-pool = Oglejte si sklad
tradeoff-view-players = Oglejte si igralce
tradeoff-hand-display = Vaša roka ({ $count } kock): { $dice }
tradeoff-pool-display = Sklad ({ $count } kock): { $dice }
tradeoff-player-info = { $player }: { $hand }. Zamenjal: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. Ni zamenjal ničesar.

# Error messages
tradeoff-not-trading-phase = Ni faza zamenjave.
tradeoff-not-taking-phase = Ni faza jemanja.
tradeoff-already-confirmed = Že potrjeno.
tradeoff-no-die = Ni kocke za preklop.
tradeoff-no-more-takes = Ni več jemanj na voljo.
tradeoff-not-in-pool = Ta kocka ni v skladu.

# Options
tradeoff-set-target = Ciljni rezultat: { $score }
tradeoff-enter-target = Vnesite ciljni rezultat:
tradeoff-option-changed-target = Ciljni rezultat nastavljen na { $score }.
