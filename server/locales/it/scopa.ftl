# Scopa game messages
# Note: Common messages like round-start, turn-start, target-score, team-mode are in games.ftl

# Game name
game-name-scopa = Scopa

# Game events
scopa-initial-table = Carte sul tavolo: { $cards }
scopa-no-initial-table = Nessuna carta sul tavolo all'inizio.
scopa-you-collect = Raccogli { $cards } con { $card }
scopa-player-collects = { $player } raccoglie { $cards } con { $card }
scopa-you-put-down = Metti giù { $card }.
scopa-player-puts-down = { $player } mette giù { $card }.
scopa-scopa-suffix =  - SCOPA!
scopa-clear-table-suffix = , pulendo il tavolo.
scopa-remaining-cards = { $player } prende le carte rimanenti sul tavolo.
scopa-scoring-round = Conteggio punti del turno...
scopa-most-cards = { $player } segna 1 punto per più carte ({ $count } carte).
scopa-most-cards-tie = Più carte è un pareggio - nessun punto assegnato.
scopa-most-diamonds = { $player } segna 1 punto per più denari ({ $count } denari).
scopa-most-diamonds-tie = Più denari è un pareggio - nessun punto assegnato.
scopa-seven-diamonds = { $player } segna 1 punto per il 7 di denari.
scopa-seven-diamonds-multi = { $player } segna 1 punto per più 7 di denari ({ $count } × 7 di denari).
scopa-seven-diamonds-tie = Il 7 di denari è un pareggio - nessun punto assegnato.
scopa-most-sevens = { $player } segna 1 punto per più sette ({ $count } sette).
scopa-most-sevens-tie = Più sette è un pareggio - nessun punto assegnato.
scopa-round-scores = Punteggi del turno:
scopa-round-score-line = { $player }: +{ $round_score } (totale: { $total_score })
scopa-table-empty = Non ci sono carte sul tavolo.
scopa-no-such-card = Nessuna carta in quella posizione.
scopa-captured-count = Hai catturato { $count } carte

# View actions
scopa-view-table = Vedi tavolo
scopa-view-captured = Vedi catturate

# Scopa-specific options
scopa-enter-target-score = Inserisci punteggio obiettivo (1-121)
scopa-set-cards-per-deal = Carte per mano: { $cards }
scopa-enter-cards-per-deal = Inserisci carte per mano (1-10)
scopa-set-decks = Numero di mazzi: { $decks }
scopa-enter-decks = Inserisci numero di mazzi (1-6)
scopa-toggle-escoba = Escoba (somma a 15): { $enabled }
scopa-toggle-hints = Mostra suggerimenti cattura: { $enabled }
scopa-set-mechanic = Meccanica scopa: { $mechanic }
scopa-select-mechanic = Seleziona meccanica scopa
scopa-toggle-instant-win = Vittoria immediata su scopa: { $enabled }
scopa-toggle-team-scoring = Raccolta carte squadra per punteggio: { $enabled }
scopa-toggle-inverse = Modalità inversa (raggiungere obiettivo = eliminazione): { $enabled }

# Option change announcements
scopa-option-changed-cards = Carte per mano impostate a { $cards }.
scopa-option-changed-decks = Numero di mazzi impostato a { $decks }.
scopa-option-changed-escoba = Escoba { $enabled }.
scopa-option-changed-hints = Suggerimenti cattura { $enabled }.
scopa-option-changed-mechanic = Meccanica scopa impostata a { $mechanic }.
scopa-option-changed-instant = Vittoria immediata su scopa { $enabled }.
scopa-option-changed-team-scoring = Punteggio carte squadra { $enabled }.
scopa-option-changed-inverse = Modalità inversa { $enabled }.

# Scopa mechanic choices
scopa-mechanic-normal = Normale
scopa-mechanic-no_scopas = Senza Scope
scopa-mechanic-only_scopas = Solo Scope

# Disabled action reasons
scopa-timer-not-active = Il timer del turno non è attivo.

# Validation errors
scopa-error-not-enough-cards = Non ci sono abbastanza carte in { $decks } { $decks ->
    [one] mazzo
    *[other] mazzi
} per { $players } { $players ->
    [one] giocatore
    *[other] giocatori
} con { $cards_per_deal } carte ciascuno. (Servono { $cards_per_deal } × { $players } = { $cards_needed } carte, ma ce ne sono solo { $total_cards }.)
