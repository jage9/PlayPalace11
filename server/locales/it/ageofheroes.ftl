# Age of Heroes game messages
# A civilization-building card game for 2-6 players

# Game name
game-name-ageofheroes = Era degli Eroi

# Tribes
ageofheroes-tribe-egyptians = Egiziani
ageofheroes-tribe-romans = Romani
ageofheroes-tribe-greeks = Greci
ageofheroes-tribe-babylonians = Babilonesi
ageofheroes-tribe-celts = Celti
ageofheroes-tribe-chinese = Cinesi

# Special Resources (for monuments)
ageofheroes-special-limestone = Calcare
ageofheroes-special-concrete = Calcestruzzo
ageofheroes-special-marble = Marmo
ageofheroes-special-bricks = Mattoni
ageofheroes-special-sandstone = Arenaria
ageofheroes-special-granite = Granito

# Standard Resources
ageofheroes-resource-iron = Ferro
ageofheroes-resource-wood = Legno
ageofheroes-resource-grain = Grano
ageofheroes-resource-stone = Pietra
ageofheroes-resource-gold = Oro

# Events
ageofheroes-event-population-growth = Crescita Demografica
ageofheroes-event-earthquake = Terremoto
ageofheroes-event-eruption = Eruzione
ageofheroes-event-hunger = Carestia
ageofheroes-event-barbarians = Barbari
ageofheroes-event-olympics = Giochi Olimpici
ageofheroes-event-hero = Eroe
ageofheroes-event-fortune = Fortuna

# Buildings
ageofheroes-building-army = Esercito
ageofheroes-building-fortress = Fortezza
ageofheroes-building-general = Generale
ageofheroes-building-road = Strada
ageofheroes-building-city = Città

# Actions
ageofheroes-action-tax-collection = Riscossione Tasse
ageofheroes-action-construction = Costruzione
ageofheroes-action-war = Guerra
ageofheroes-action-do-nothing = Non Fare Nulla
ageofheroes-play = Gioca

# War goals
ageofheroes-war-conquest = Conquista
ageofheroes-war-plunder = Saccheggio
ageofheroes-war-destruction = Distruzione

# Game options
ageofheroes-set-victory-cities = Città per la vittoria: { $cities }
ageofheroes-enter-victory-cities = Inserisci il numero di città per vincere (3-7)
ageofheroes-set-victory-monument = Completamento monumento: { $progress }%
ageofheroes-toggle-neighbor-roads = Strade solo verso vicini: { $enabled }
ageofheroes-set-max-hand = Dimensione massima mano: { $cards } carte

# Option change announcements
ageofheroes-option-changed-victory-cities = Vittoria richiede { $cities } città.
ageofheroes-option-changed-victory-monument = Soglia completamento monumento impostata al { $progress }%.
ageofheroes-option-changed-neighbor-roads = Strade solo verso vicini { $enabled }.
ageofheroes-option-changed-max-hand = Dimensione massima mano impostata a { $cards } carte.

# Setup phase
ageofheroes-setup-start = Sei il capo della tribù { $tribe }. La tua risorsa speciale per il monumento è { $special }. Lancia i dadi per determinare l'ordine di gioco.
ageofheroes-setup-viewer = I giocatori stanno lanciando i dadi per determinare l'ordine di gioco.
ageofheroes-roll-dice = Lancia i dadi
ageofheroes-war-roll-dice = Lancia i dadi
ageofheroes-dice-result = Hai ottenuto { $total } ({ $die1 } + { $die2 }).
ageofheroes-dice-result-other = { $player } ha ottenuto { $total }.
ageofheroes-dice-tie = Più giocatori hanno ottenuto { $total }. Rilancio...
ageofheroes-first-player = { $player } ha ottenuto il punteggio più alto con { $total } e inizia per primo.
ageofheroes-first-player-you = Con { $total } punti, inizi tu.

# Preparation phase
ageofheroes-prepare-start = I giocatori devono giocare carte evento e scartare disastri.
ageofheroes-prepare-your-turn = Hai { $count } { $count ->
    [one] carta
    *[other] carte
} da giocare o scartare.
ageofheroes-prepare-done = Fase di preparazione completata.

# Events played/discarded
ageofheroes-population-growth = { $player } gioca Crescita Demografica e costruisce una nuova città.
ageofheroes-population-growth-you = Giochi Crescita Demografica e costruisci una nuova città.
ageofheroes-discard-card = { $player } scarta { $card }.
ageofheroes-discard-card-you = Scarti { $card }.
ageofheroes-earthquake = Un terremoto colpisce la tribù di { $player }; i loro eserciti vanno in recupero.
ageofheroes-earthquake-you = Un terremoto colpisce la tua tribù; i tuoi eserciti vanno in recupero.
ageofheroes-eruption = Un'eruzione distrugge una delle città di { $player }.
ageofheroes-eruption-you = Un'eruzione distrugge una delle tue città.

# Disaster effects
ageofheroes-hunger-strikes = La carestia colpisce.
ageofheroes-lose-card-hunger = Perdi { $card }.
ageofheroes-barbarians-pillage = I barbari attaccano le risorse di { $player }.
ageofheroes-barbarians-attack = I barbari attaccano le risorse di { $player }.
ageofheroes-barbarians-attack-you = I barbari attaccano le tue risorse.
ageofheroes-lose-card-barbarians = Perdi { $card }.
ageofheroes-block-with-card = { $player } blocca il disastro usando { $card }.
ageofheroes-block-with-card-you = Blocchi il disastro usando { $card }.

# Targeted disaster cards (Earthquake/Eruption)
ageofheroes-select-disaster-target = Seleziona un bersaglio per { $card }.
ageofheroes-no-targets = Nessun bersaglio valido disponibile.
ageofheroes-earthquake-strikes-you = { $attacker } gioca Terremoto contro di te. I tuoi eserciti sono disabilitati.
ageofheroes-earthquake-strikes = { $attacker } gioca Terremoto contro { $player }.
ageofheroes-armies-disabled = { $count } { $count ->
    [one] esercito è disabilitato
    *[other] eserciti sono disabilitati
} per un turno.
ageofheroes-eruption-strikes-you = { $attacker } gioca Eruzione contro di te. Una delle tue città è distrutta.
ageofheroes-eruption-strikes = { $attacker } gioca Eruzione contro { $player }.
ageofheroes-city-destroyed = Una città è distrutta dall'eruzione.

# Fair phase
ageofheroes-fair-start = L'alba sorge sul mercato.
ageofheroes-fair-draw-base = Peschi { $count } { $count ->
    [one] carta
    *[other] carte
}.
ageofheroes-fair-draw-roads = Peschi { $count } { $count ->
    [one] carta aggiuntiva
    *[other] carte aggiuntive
} grazie alla tua rete stradale.
ageofheroes-fair-draw-other = { $player } pesca { $count } { $count ->
    [one] carta
    *[other] carte
}.

# Trading/Auction
ageofheroes-auction-start = L'asta inizia.
ageofheroes-offer-trade = Offri scambio
ageofheroes-offer-made = { $player } offre { $card } per { $wanted }.
ageofheroes-offer-made-you = Offri { $card } per { $wanted }.
ageofheroes-trade-accepted = { $player } accetta l'offerta di { $other } e scambia { $give } per { $receive }.
ageofheroes-trade-accepted-you = Accetti l'offerta di { $other } e ricevi { $receive }.
ageofheroes-trade-cancelled = { $player } ritira la sua offerta per { $card }.
ageofheroes-trade-cancelled-you = Ritiri la tua offerta per { $card }.
ageofheroes-stop-trading = Smetti di Commerciare
ageofheroes-select-request = Stai offrendo { $card }. Cosa vuoi in cambio?
ageofheroes-cancel = Annulla
ageofheroes-left-auction = { $player } se ne va.
ageofheroes-left-auction-you = Te ne vai dal mercato.
ageofheroes-any-card = Qualsiasi carta
ageofheroes-cannot-trade-own-special = Non puoi scambiare la tua risorsa speciale per il monumento.
ageofheroes-resource-not-in-game = Questa risorsa speciale non è in uso in questa partita.

# Main play phase
ageofheroes-play-start = Fase di gioco.
ageofheroes-day = Giorno { $day }
ageofheroes-draw-card = { $player } pesca una carta dal mazzo.
ageofheroes-draw-card-you = Peschi { $card } dal mazzo.
ageofheroes-your-action = Cosa vuoi fare?

# Tax Collection
ageofheroes-tax-collection = { $player } sceglie Riscossione Tasse: { $cities } { $cities ->
    [one] città
    *[other] città
} riscuote { $cards } { $cards ->
    [one] carta
    *[other] carte
}.
ageofheroes-tax-collection-you = Scegli Riscossione Tasse: { $cities } { $cities ->
    [one] città
    *[other] città
} riscuote { $cards } { $cards ->
    [one] carta
    *[other] carte
}.
ageofheroes-tax-no-city = Riscossione Tasse: Non hai città sopravvissute. Scarta una carta per pescarne una nuova.
ageofheroes-tax-no-city-done = { $player } sceglie Riscossione Tasse ma non ha città, quindi scambia una carta.
ageofheroes-tax-no-city-done-you = Riscossione Tasse: Hai scambiato { $card } per una nuova carta.

# Construction
ageofheroes-construction-menu = Cosa vuoi costruire?
ageofheroes-construction-done = { $player } ha costruito { $article } { $building }.
ageofheroes-construction-done-you = Hai costruito { $article } { $building }.
ageofheroes-construction-stop = Smetti di costruire
ageofheroes-construction-stopped = Hai deciso di smettere di costruire.
ageofheroes-road-select-neighbor = Seleziona verso quale vicino costruire una strada.
ageofheroes-direction-left = Alla tua sinistra
ageofheroes-direction-right = Alla tua destra
ageofheroes-road-request-sent = Richiesta strada inviata. In attesa dell'approvazione del vicino.
ageofheroes-road-request-received = { $requester } chiede il permesso di costruire una strada verso la tua tribù.
ageofheroes-road-request-denied-you = Hai rifiutato la richiesta di strada.
ageofheroes-road-request-denied = { $denier } ha rifiutato la tua richiesta di strada.
ageofheroes-road-built = { $tribe1 } e { $tribe2 } sono ora collegati da una strada.
ageofheroes-road-no-target = Nessuna tribù vicina disponibile per la costruzione di strade.
ageofheroes-approve = Approva
ageofheroes-deny = Rifiuta
ageofheroes-supply-exhausted = Non ci sono più { $building } disponibili da costruire.

# Do Nothing
ageofheroes-do-nothing = { $player } passa.
ageofheroes-do-nothing-you = Passi...

# War
ageofheroes-war-declare = { $attacker } dichiara guerra a { $defender }. Obiettivo: { $goal }.
ageofheroes-war-prepare = Seleziona i tuoi eserciti per { $action }.
ageofheroes-war-no-army = Non hai eserciti o carte eroe disponibili.
ageofheroes-war-no-targets = Nessun bersaglio valido per la guerra.
ageofheroes-war-no-valid-goal = Nessun obiettivo di guerra valido contro questo bersaglio.
ageofheroes-war-select-target = Seleziona quale giocatore attaccare.
ageofheroes-war-select-goal = Seleziona il tuo obiettivo di guerra.
ageofheroes-war-prepare-attack = Seleziona le tue forze d'attacco.
ageofheroes-war-prepare-defense = { $attacker } ti sta attaccando; Seleziona le tue forze di difesa.
ageofheroes-war-select-armies = Seleziona eserciti: { $count }
ageofheroes-war-select-generals = Seleziona generali: { $count }
ageofheroes-war-select-heroes = Seleziona eroi: { $count }
ageofheroes-war-attack = Attacca...
ageofheroes-war-defend = Difendi...
ageofheroes-war-prepared = Le tue forze: { $armies } { $armies ->
    [one] esercito
    *[other] eserciti
}{ $generals ->
    [0] {""}
    [one] {" e 1 generale"}
    *[other] {" e { $generals } generali"}
}{ $heroes ->
    [0] {""}
    [one] {" e 1 eroe"}
    *[other] {" e { $heroes } eroi"}
}.
ageofheroes-war-roll-you = Tiri { $roll }.
ageofheroes-war-roll-other = { $player } tira { $roll }.
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"+1 dalla fortezza = { $total } totale"}
            *[other] {"+{ $fortress } dalle fortezze = { $total } totale"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"+{ $general } dal generale = { $total } totale"}
            [one] {"+{ $general } dal generale, +1 dalla fortezza = { $total } totale"}
            *[other] {"+{ $general } dal generale, +{ $fortress } dalle fortezze = { $total } totale"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"{ $player }: +1 dalla fortezza = { $total } totale"}
            *[other] {"{ $player }: +{ $fortress } dalle fortezze = { $total } totale"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } dal generale = { $total } totale"}
            [one] {"{ $player }: +{ $general } dal generale, +1 dalla fortezza = { $total } totale"}
            *[other] {"{ $player }: +{ $general } dal generale, +{ $fortress } dalle fortezze = { $total } totale"}
        }
    }
}

# Battle
ageofheroes-battle-start = La battaglia inizia. { $attacker } ha { $att_armies } { $att_armies ->
    [one] esercito
    *[other] eserciti
} contro { $defender } con { $def_armies } { $def_armies ->
    [one] esercito
    *[other] eserciti
}.
ageofheroes-dice-roll-detailed = { $name } tira { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } dal generale" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 dalla fortezza" }
    *[other] { " + { $fortress } dalle fortezze" }
} = { $total }.
ageofheroes-dice-roll-detailed-you = Tiri { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } dal generale" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 dalla fortezza" }
    *[other] { " + { $fortress } dalle fortezze" }
} = { $total }.
ageofheroes-round-attacker-wins = { $attacker } vince il round ({ $att_total } contro { $def_total }). { $defender } perde un esercito.
ageofheroes-round-defender-wins = { $defender } difende con successo ({ $def_total } contro { $att_total }). { $attacker } perde un esercito.
ageofheroes-round-draw = Entrambe le parti pareggiano a { $total }. Nessun esercito perso.
ageofheroes-battle-victory-attacker = { $attacker } sconfigge { $defender }.
ageofheroes-battle-victory-defender = { $defender } difende con successo contro { $attacker }.
ageofheroes-battle-mutual-defeat = Sia { $attacker } che { $defender } perdono tutti gli eserciti.
ageofheroes-general-bonus = +{ $count } dal { $count ->
    [one] generale
    *[other] generali
}
ageofheroes-fortress-bonus = +{ $count } dalla difesa della fortezza
ageofheroes-battle-winner = { $winner } vince la battaglia.
ageofheroes-battle-draw = La battaglia finisce in pareggio...
ageofheroes-battle-continue = Continua la battaglia.
ageofheroes-battle-end = La battaglia è finita.

# War outcomes
ageofheroes-conquest-success = { $attacker } conquista { $count } { $count ->
    [one] città
    *[other] città
} da { $defender }.
ageofheroes-plunder-success = { $attacker } saccheggia { $count } { $count ->
    [one] carta
    *[other] carte
} da { $defender }.
ageofheroes-destruction-success = { $attacker } distrugge { $count } { $count ->
    [one] risorsa
    *[other] risorse
} del monumento di { $defender }.
ageofheroes-army-losses = { $player } perde { $count } { $count ->
    [one] esercito
    *[other] eserciti
}.
ageofheroes-army-losses-you = Perdi { $count } { $count ->
    [one] esercito
    *[other] eserciti
}.

# Army return
ageofheroes-army-return-road = Le tue truppe ritornano immediatamente via strada.
ageofheroes-army-return-delayed = { $count } { $count ->
    [one] unità ritorna
    *[other] unità ritornano
} alla fine del tuo prossimo turno.
ageofheroes-army-returned = Le truppe di { $player } sono tornate dalla guerra.
ageofheroes-army-returned-you = Le tue truppe sono tornate dalla guerra.
ageofheroes-army-recover = Gli eserciti di { $player } si riprendono dal terremoto.
ageofheroes-army-recover-you = I tuoi eserciti si riprendono dal terremoto.

# Olympics
ageofheroes-olympics-cancel = { $player } gioca Giochi Olimpici. Guerra annullata.
ageofheroes-olympics-prompt = { $attacker } ha dichiarato guerra. Hai i Giochi Olimpici - usarli per annullare?
ageofheroes-yes = Sì
ageofheroes-no = No

# Monument progress
ageofheroes-monument-progress = Il monumento di { $player } è { $count }/5 completo.
ageofheroes-monument-progress-you = Il tuo monumento è { $count }/5 completo.

# Hand management
ageofheroes-discard-excess = Hai più di { $max } carte. Scarta { $count } { $count ->
    [one] carta
    *[other] carte
}.
ageofheroes-discard-excess-other = { $player } deve scartare le carte in eccesso.
ageofheroes-discard-more = Scarta ancora { $count } { $count ->
    [one] carta
    *[other] carte
}.

# Victory
ageofheroes-victory-cities = { $player } ha costruito 5 città! Impero delle Cinque Città.
ageofheroes-victory-cities-you = Hai costruito 5 città! Impero delle Cinque Città.
ageofheroes-victory-monument = { $player } ha completato il suo monumento! Portatori di Grande Cultura.
ageofheroes-victory-monument-you = Hai completato il tuo monumento! Portatori di Grande Cultura.
ageofheroes-victory-last-standing = { $player } è l'ultima tribù sopravvissuta! Il Più Persistente.
ageofheroes-victory-last-standing-you = Sei l'ultima tribù sopravvissuta! Il Più Persistente.
ageofheroes-game-over = Fine Partita.

# Elimination
ageofheroes-eliminated = { $player } è stato eliminato.
ageofheroes-eliminated-you = Sei stato eliminato.

# Hand
ageofheroes-hand-empty = Non hai carte.
ageofheroes-hand-contents = La tua mano ({ $count } { $count ->
    [one] carta
    *[other] carte
}): { $cards }

# Status
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [one] città
    *[other] città
}, { $armies } { $armies ->
    [one] esercito
    *[other] eserciti
}, { $monument }/5 monumento
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = Città: { $count }
ageofheroes-status-armies = Eserciti: { $count }
ageofheroes-status-generals = Generali: { $count }
ageofheroes-status-fortresses = Fortezze: { $count }
ageofheroes-status-monument = Monumento: { $count }/5
ageofheroes-status-roads = Strade: { $left }{ $right }
ageofheroes-status-road-left = sinistra
ageofheroes-status-road-right = destra
ageofheroes-status-none = nessuna
ageofheroes-status-earthquake-armies = Eserciti in recupero: { $count }
ageofheroes-status-returning-armies = Eserciti di ritorno: { $count }
ageofheroes-status-returning-generals = Generali di ritorno: { $count }

# Deck info
ageofheroes-deck-empty = Non ci sono più carte { $card } nel mazzo.
ageofheroes-deck-count = Carte rimanenti: { $count }
ageofheroes-deck-reshuffled = Gli scarti sono stati rimescolati nel mazzo.

# Give up
ageofheroes-give-up-confirm = Sei sicuro di voler abbandonare?
ageofheroes-gave-up = { $player } ha abbandonato!
ageofheroes-gave-up-you = Hai abbandonato!

# Hero card
ageofheroes-hero-use = Usare come esercito o generale?
ageofheroes-hero-army = Esercito
ageofheroes-hero-general = Generale

# Fortune card
ageofheroes-fortune-reroll = { $player } usa Fortuna per ritirare.
ageofheroes-fortune-prompt = Hai perso il tiro. Usare Fortuna per ritirare?

# Disabled action reasons
ageofheroes-not-your-turn = Non è il tuo turno.
ageofheroes-game-not-started = La partita non è ancora iniziata.
ageofheroes-wrong-phase = Questa azione non è disponibile nella fase attuale.
ageofheroes-no-resources = Non hai le risorse richieste.

# Building costs (for display)
ageofheroes-cost-army = 2 grano, ferro
ageofheroes-cost-fortress = Ferro, legno, pietra
ageofheroes-cost-general = Ferro, oro
ageofheroes-cost-road = 2 pietre
ageofheroes-cost-city = 2 legno, pietra
