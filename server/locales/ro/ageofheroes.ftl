# Age of Heroes game messages
# A civilization-building card game for 2-6 players

# Game name
game-name-ageofheroes = Era Eroilor

# Tribes
ageofheroes-tribe-egyptians = Egipteni
ageofheroes-tribe-romans = Romani
ageofheroes-tribe-greeks = Greci
ageofheroes-tribe-babylonians = Babilonieni
ageofheroes-tribe-celts = Celți
ageofheroes-tribe-chinese = Chinezi

# Special Resources (for monuments)
ageofheroes-special-limestone = Calcar
ageofheroes-special-concrete = Beton
ageofheroes-special-marble = Marmură
ageofheroes-special-bricks = Cărămizi
ageofheroes-special-sandstone = Gresie
ageofheroes-special-granite = Granit

# Standard Resources
ageofheroes-resource-iron = Fier
ageofheroes-resource-wood = Lemn
ageofheroes-resource-grain = Grâu
ageofheroes-resource-stone = Piatră
ageofheroes-resource-gold = Aur

# Events
ageofheroes-event-population-growth = Creșterea Populației
ageofheroes-event-earthquake = Cutremur
ageofheroes-event-eruption = Erupție
ageofheroes-event-hunger = Foamete
ageofheroes-event-barbarians = Barbari
ageofheroes-event-olympics = Jocuri Olimpice
ageofheroes-event-hero = Erou
ageofheroes-event-fortune = Noroc

# Buildings
ageofheroes-building-army = Armată
ageofheroes-building-fortress = Fortăreață
ageofheroes-building-general = General
ageofheroes-building-road = Drum
ageofheroes-building-city = Oraș

# Actions
ageofheroes-action-tax-collection = Colectare Taxe
ageofheroes-action-construction = Construcție
ageofheroes-action-war = Război
ageofheroes-action-do-nothing = Nu Face Nimic
ageofheroes-play = Joacă

# War goals
ageofheroes-war-conquest = Cucerire
ageofheroes-war-plunder = Jefuire
ageofheroes-war-destruction = Distrugere

# Game options
ageofheroes-set-victory-cities = Orașe pentru victorie: { $cities }
ageofheroes-enter-victory-cities = Introduceți numărul de orașe pentru victorie (3-7)
ageofheroes-set-victory-monument = Completare monument: { $progress }%
ageofheroes-toggle-neighbor-roads = Drumuri doar către vecini: { $enabled }
ageofheroes-set-max-hand = Dimensiune maximă mână: { $cards } cărți

# Option change announcements
ageofheroes-option-changed-victory-cities = Victoria necesită { $cities } orașe.
ageofheroes-option-changed-victory-monument = Pragul de completare monument setat la { $progress }%.
ageofheroes-option-changed-neighbor-roads = Drumuri doar către vecini { $enabled }.
ageofheroes-option-changed-max-hand = Dimensiune maximă mână setată la { $cards } cărți.

# Setup phase
ageofheroes-setup-start = Ești liderul tribului { $tribe }. Resursa ta specială pentru monument este { $special }. Aruncă zarurile pentru a determina ordinea turelor.
ageofheroes-setup-viewer = Jucătorii aruncă zarurile pentru a determina ordinea turelor.
ageofheroes-roll-dice = Aruncă zarurile
ageofheroes-war-roll-dice = Aruncă zarurile
ageofheroes-dice-result = Ai obținut { $total } ({ $die1 } + { $die2 }).
ageofheroes-dice-result-other = { $player } a obținut { $total }.
ageofheroes-dice-tie = Mai mulți jucători au obținut { $total }. Aruncăm din nou...
ageofheroes-first-player = { $player } a obținut cel mai mare punctaj cu { $total } și începe primul.
ageofheroes-first-player-you = Cu { $total } puncte, tu începi primul.

# Preparation phase
ageofheroes-prepare-start = Jucătorii trebuie să joace cărți eveniment și să arunce dezastrele.
ageofheroes-prepare-your-turn = Ai { $count } { $count ->
    [one] carte
    [few] cărți
    *[other] de cărți
} de jucat sau aruncat.
ageofheroes-prepare-done = Faza de pregătire completată.

# Events played/discarded
ageofheroes-population-growth = { $player } joacă Creșterea Populației și construiește un oraș nou.
ageofheroes-population-growth-you = Tu joci Creșterea Populației și construiești un oraș nou.
ageofheroes-discard-card = { $player } aruncă { $card }.
ageofheroes-discard-card-you = Tu arunci { $card }.
ageofheroes-earthquake = Un cutremur lovește tribul lui { $player }; armatele lor intră în recuperare.
ageofheroes-earthquake-you = Un cutremur lovește tribul tău; armatele tale intră în recuperare.
ageofheroes-eruption = O erupție distruge unul din orașele lui { $player }.
ageofheroes-eruption-you = O erupție distruge unul din orașele tale.

# Disaster effects
ageofheroes-hunger-strikes = Foametea lovește.
ageofheroes-lose-card-hunger = Pierzi { $card }.
ageofheroes-barbarians-pillage = Barbarii atacă resursele lui { $player }.
ageofheroes-barbarians-attack = Barbarii atacă resursele lui { $player }.
ageofheroes-barbarians-attack-you = Barbarii atacă resursele tale.
ageofheroes-lose-card-barbarians = Pierzi { $card }.
ageofheroes-block-with-card = { $player } blochează dezastrul folosind { $card }.
ageofheroes-block-with-card-you = Tu blochezi dezastrul folosind { $card }.

# Targeted disaster cards (Earthquake/Eruption)
ageofheroes-select-disaster-target = Selectează o țintă pentru { $card }.
ageofheroes-no-targets = Nicio țintă validă disponibilă.
ageofheroes-earthquake-strikes-you = { $attacker } joacă Cutremur împotriva ta. Armatele tale sunt dezactivate.
ageofheroes-earthquake-strikes = { $attacker } joacă Cutremur împotriva lui { $player }.
ageofheroes-armies-disabled = { $count } { $count ->
    [one] armată este dezactivată
    [few] armate sunt dezactivate
    *[other] de armate sunt dezactivate
} pentru o tură.
ageofheroes-eruption-strikes-you = { $attacker } joacă Erupție împotriva ta. Unul din orașele tale este distrus.
ageofheroes-eruption-strikes = { $attacker } joacă Erupție împotriva lui { $player }.
ageofheroes-city-destroyed = Un oraș este distrus de erupție.

# Fair phase
ageofheroes-fair-start = Zori de zi pe piață.
ageofheroes-fair-draw-base = Tragi { $count } { $count ->
    [one] carte
    [few] cărți
    *[other] de cărți
}.
ageofheroes-fair-draw-roads = Tragi { $count } { $count ->
    [one] carte suplimentară
    [few] cărți suplimentare
    *[other] de cărți suplimentare
} datorită rețelei tale de drumuri.
ageofheroes-fair-draw-other = { $player } trage { $count } { $count ->
    [one] carte
    [few] cărți
    *[other] de cărți
}.

# Trading/Auction
ageofheroes-auction-start = Licitația începe.
ageofheroes-offer-trade = Oferă schimb
ageofheroes-offer-made = { $player } oferă { $card } pentru { $wanted }.
ageofheroes-offer-made-you = Tu oferi { $card } pentru { $wanted }.
ageofheroes-trade-accepted = { $player } acceptă oferta lui { $other } și schimbă { $give } pentru { $receive }.
ageofheroes-trade-accepted-you = Tu accepți oferta lui { $other } și primești { $receive }.
ageofheroes-trade-cancelled = { $player } retrage oferta pentru { $card }.
ageofheroes-trade-cancelled-you = Tu retragi oferta pentru { $card }.
ageofheroes-stop-trading = Oprește Schimbul
ageofheroes-select-request = Oferi { $card }. Ce vrei în schimb?
ageofheroes-cancel = Anulează
ageofheroes-left-auction = { $player } pleacă.
ageofheroes-left-auction-you = Tu pleci de la piață.
ageofheroes-any-card = Orice carte
ageofheroes-cannot-trade-own-special = Nu poți schimba propria ta resursă specială pentru monument.
ageofheroes-resource-not-in-game = Această resursă specială nu este folosită în acest joc.

# Main play phase
ageofheroes-play-start = Faza de joc.
ageofheroes-day = Ziua { $day }
ageofheroes-draw-card = { $player } trage o carte din pachet.
ageofheroes-draw-card-you = Tu tragi { $card } din pachet.
ageofheroes-your-action = Ce vrei să faci?

# Tax Collection
ageofheroes-tax-collection = { $player } alege Colectare Taxe: { $cities } { $cities ->
    [one] oraș
    [few] orașe
    *[other] de orașe
} colectează { $cards } { $cards ->
    [one] carte
    [few] cărți
    *[other] de cărți
}.
ageofheroes-tax-collection-you = Tu alegi Colectare Taxe: { $cities } { $cities ->
    [one] oraș
    [few] orașe
    *[other] de orașe
} colectează { $cards } { $cards ->
    [one] carte
    [few] cărți
    *[other] de cărți
}.
ageofheroes-tax-no-city = Colectare Taxe: Nu ai orașe supraviețuitoare. Aruncă o carte pentru a trage una nouă.
ageofheroes-tax-no-city-done = { $player } alege Colectare Taxe dar nu are orașe, așa că schimbă o carte.
ageofheroes-tax-no-city-done-you = Colectare Taxe: Ai schimbat { $card } pentru o carte nouă.

# Construction
ageofheroes-construction-menu = Ce vrei să construiești?
ageofheroes-construction-done = { $player } a construit { $article } { $building }.
ageofheroes-construction-done-you = Tu ai construit { $article } { $building }.
ageofheroes-construction-stop = Oprește construcția
ageofheroes-construction-stopped = Ai decis să oprești construcția.
ageofheroes-road-select-neighbor = Selectează către care vecin să construiești un drum.
ageofheroes-direction-left = Spre stânga ta
ageofheroes-direction-right = Spre dreapta ta
ageofheroes-road-request-sent = Cerere de drum trimisă. Așteptăm aprobarea vecinului.
ageofheroes-road-request-received = { $requester } solicită permisiunea de a construi un drum către tribul tău.
ageofheroes-road-request-denied-you = Tu ai refuzat cererea de drum.
ageofheroes-road-request-denied = { $denier } a refuzat cererea ta de drum.
ageofheroes-road-built = { $tribe1 } și { $tribe2 } sunt acum conectați printr-un drum.
ageofheroes-road-no-target = Niciun trib vecin disponibil pentru construcția drumului.
ageofheroes-approve = Aprobă
ageofheroes-deny = Refuză
ageofheroes-supply-exhausted = Nu mai sunt { $building } disponibile pentru construcție.

# Do Nothing
ageofheroes-do-nothing = { $player } pasează.
ageofheroes-do-nothing-you = Tu pasezi...

# War
ageofheroes-war-declare = { $attacker } declară război lui { $defender }. Obiectiv: { $goal }.
ageofheroes-war-prepare = Selectează armatele tale pentru { $action }.
ageofheroes-war-no-army = Nu ai armate sau cărți erou disponibile.
ageofheroes-war-no-targets = Nicio țintă validă pentru război.
ageofheroes-war-no-valid-goal = Niciun obiectiv de război valid împotriva acestei ținte.
ageofheroes-war-select-target = Selectează ce jucător să ataci.
ageofheroes-war-select-goal = Selectează obiectivul tău de război.
ageofheroes-war-prepare-attack = Selectează forțele tale de atac.
ageofheroes-war-prepare-defense = { $attacker } te atacă; Selectează forțele tale de apărare.
ageofheroes-war-select-armies = Selectează armate: { $count }
ageofheroes-war-select-generals = Selectează generali: { $count }
ageofheroes-war-select-heroes = Selectează eroi: { $count }
ageofheroes-war-attack = Atacă...
ageofheroes-war-defend = Apără...
ageofheroes-war-prepared = Forțele tale: { $armies } { $armies ->
    [one] armată
    [few] armate
    *[other] de armate
}{ $generals ->
    [0] {""}
    [one] {" și 1 general"}
    [few] {" și { $generals } generali"}
    *[other] {" și { $generals } de generali"}
}{ $heroes ->
    [0] {""}
    [one] {" și 1 erou"}
    [few] {" și { $heroes } eroi"}
    *[other] {" și { $heroes } de eroi"}
}.
ageofheroes-war-roll-you = Tu obții { $roll }.
ageofheroes-war-roll-other = { $player } obține { $roll }.
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"+1 de la fortăreață = { $total } total"}
            [few] {"+{ $fortress } de la fortărețe = { $total } total"}
            *[other] {"+{ $fortress } de la fortărețe = { $total } total"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"+{ $general } de la general = { $total } total"}
            [one] {"+{ $general } de la general, +1 de la fortăreață = { $total } total"}
            [few] {"+{ $general } de la general, +{ $fortress } de la fortărețe = { $total } total"}
            *[other] {"+{ $general } de la general, +{ $fortress } de la fortărețe = { $total } total"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"{ $player }: +1 de la fortăreață = { $total } total"}
            [few] {"{ $player }: +{ $fortress } de la fortărețe = { $total } total"}
            *[other] {"{ $player }: +{ $fortress } de la fortărețe = { $total } total"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } de la general = { $total } total"}
            [one] {"{ $player }: +{ $general } de la general, +1 de la fortăreață = { $total } total"}
            [few] {"{ $player }: +{ $general } de la general, +{ $fortress } de la fortărețe = { $total } total"}
            *[other] {"{ $player }: +{ $general } de la general, +{ $fortress } de la fortărețe = { $total } total"}
        }
    }
}

# Battle
ageofheroes-battle-start = Bătălia începe. { $attacker } are { $att_armies } { $att_armies ->
    [one] armată
    [few] armate
    *[other] de armate
} împotriva lui { $defender } cu { $def_armies } { $def_armies ->
    [one] armată
    [few] armate
    *[other] de armate
}.
ageofheroes-dice-roll-detailed = { $name } obține { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } de la general" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 de la fortăreață" }
    [few] { " + { $fortress } de la fortărețe" }
    *[other] { " + { $fortress } de la fortărețe" }
} = { $total }.
ageofheroes-dice-roll-detailed-you = Tu obții { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } de la general" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 de la fortăreață" }
    [few] { " + { $fortress } de la fortărețe" }
    *[other] { " + { $fortress } de la fortărețe" }
} = { $total }.
ageofheroes-round-attacker-wins = { $attacker } câștigă runda ({ $att_total } față de { $def_total }). { $defender } pierde o armată.
ageofheroes-round-defender-wins = { $defender } se apără cu succes ({ $def_total } față de { $att_total }). { $attacker } pierde o armată.
ageofheroes-round-draw = Ambele părți au { $total }. Nicio armată pierdută.
ageofheroes-battle-victory-attacker = { $attacker } îl învinge pe { $defender }.
ageofheroes-battle-victory-defender = { $defender } se apără cu succes împotriva lui { $attacker }.
ageofheroes-battle-mutual-defeat = Atât { $attacker } cât și { $defender } pierd toate armatele.
ageofheroes-general-bonus = +{ $count } de la { $count ->
    [one] general
    [few] generali
    *[other] de generali
}
ageofheroes-fortress-bonus = +{ $count } de la apărarea fortăreței
ageofheroes-battle-winner = { $winner } câștigă bătălia.
ageofheroes-battle-draw = Bătălia se termină la egalitate...
ageofheroes-battle-continue = Continuă bătălia.
ageofheroes-battle-end = Bătălia s-a terminat.

# War outcomes
ageofheroes-conquest-success = { $attacker } cucerește { $count } { $count ->
    [one] oraș
    [few] orașe
    *[other] de orașe
} de la { $defender }.
ageofheroes-plunder-success = { $attacker } jefuiește { $count } { $count ->
    [one] carte
    [few] cărți
    *[other] de cărți
} de la { $defender }.
ageofheroes-destruction-success = { $attacker } distruge { $count } { $count ->
    [one] resursă
    [few] resurse
    *[other] de resurse
} de monument ale lui { $defender }.
ageofheroes-army-losses = { $player } pierde { $count } { $count ->
    [one] armată
    [few] armate
    *[other] de armate
}.
ageofheroes-army-losses-you = Tu pierzi { $count } { $count ->
    [one] armată
    [few] armate
    *[other] de armate
}.

# Army return
ageofheroes-army-return-road = Trupele tale se întorc imediat pe drum.
ageofheroes-army-return-delayed = { $count } { $count ->
    [one] unitate se întoarce
    [few] unități se întorc
    *[other] de unități se întorc
} la sfârșitul turei tale următoare.
ageofheroes-army-returned = Trupele lui { $player } s-au întors din război.
ageofheroes-army-returned-you = Trupele tale s-au întors din război.
ageofheroes-army-recover = Armatele lui { $player } se recuperează după cutremur.
ageofheroes-army-recover-you = Armatele tale se recuperează după cutremur.

# Olympics
ageofheroes-olympics-cancel = { $player } joacă Jocuri Olimpice. Război anulat.
ageofheroes-olympics-prompt = { $attacker } a declarat război. Ai Jocuri Olimpice - le folosești pentru anulare?
ageofheroes-yes = Da
ageofheroes-no = Nu

# Monument progress
ageofheroes-monument-progress = Monumentul lui { $player } este { $count }/5 completat.
ageofheroes-monument-progress-you = Monumentul tău este { $count }/5 completat.

# Hand management
ageofheroes-discard-excess = Ai mai mult de { $max } cărți. Aruncă { $count } { $count ->
    [one] carte
    [few] cărți
    *[other] de cărți
}.
ageofheroes-discard-excess-other = { $player } trebuie să arunce cărțile în exces.
ageofheroes-discard-more = Aruncă încă { $count } { $count ->
    [one] carte
    [few] cărți
    *[other] de cărți
}.

# Victory
ageofheroes-victory-cities = { $player } a construit 5 orașe! Imperiul celor Cinci Orașe.
ageofheroes-victory-cities-you = Tu ai construit 5 orașe! Imperiul celor Cinci Orașe.
ageofheroes-victory-monument = { $player } și-a completat monumentul! Purtătorii Marii Culturi.
ageofheroes-victory-monument-you = Tu ți-ai completat monumentul! Purtătorii Marii Culturi.
ageofheroes-victory-last-standing = { $player } este ultimul trib în viață! Cel Mai Persistent.
ageofheroes-victory-last-standing-you = Tu ești ultimul trib în viață! Cel Mai Persistent.
ageofheroes-game-over = Joc Terminat.

# Elimination
ageofheroes-eliminated = { $player } a fost eliminat.
ageofheroes-eliminated-you = Tu ai fost eliminat.

# Hand
ageofheroes-hand-empty = Nu ai cărți.
ageofheroes-hand-contents = Mâna ta ({ $count } { $count ->
    [one] carte
    [few] cărți
    *[other] de cărți
}): { $cards }

# Status
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [one] oraș
    [few] orașe
    *[other] de orașe
}, { $armies } { $armies ->
    [one] armată
    [few] armate
    *[other] de armate
}, { $monument }/5 monument
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = Orașe: { $count }
ageofheroes-status-armies = Armate: { $count }
ageofheroes-status-generals = Generali: { $count }
ageofheroes-status-fortresses = Fortărețe: { $count }
ageofheroes-status-monument = Monument: { $count }/5
ageofheroes-status-roads = Drumuri: { $left }{ $right }
ageofheroes-status-road-left = stânga
ageofheroes-status-road-right = dreapta
ageofheroes-status-none = niciunul
ageofheroes-status-earthquake-armies = Armate în recuperare: { $count }
ageofheroes-status-returning-armies = Armate care se întorc: { $count }
ageofheroes-status-returning-generals = Generali care se întorc: { $count }

# Deck info
ageofheroes-deck-empty = Nu mai sunt cărți { $card } în pachet.
ageofheroes-deck-count = Cărți rămase: { $count }
ageofheroes-deck-reshuffled = Grămada de aruncare a fost amestecată înapoi în pachet.

# Give up
ageofheroes-give-up-confirm = Ești sigur că vrei să renunți?
ageofheroes-gave-up = { $player } a renunțat!
ageofheroes-gave-up-you = Tu ai renunțat!

# Hero card
ageofheroes-hero-use = Folosit ca armată sau general?
ageofheroes-hero-army = Armată
ageofheroes-hero-general = General

# Fortune card
ageofheroes-fortune-reroll = { $player } folosește Noroc pentru a arunca din nou.
ageofheroes-fortune-prompt = Ai pierdut aruncarea. Folosești Noroc pentru a arunca din nou?

# Disabled action reasons
ageofheroes-not-your-turn = Nu este tura ta.
ageofheroes-game-not-started = Jocul nu a început încă.
ageofheroes-wrong-phase = Această acțiune nu este disponibilă în faza curentă.
ageofheroes-no-resources = Nu ai resursele necesare.

# Building costs (for display)
ageofheroes-cost-army = 2 grâu, fier
ageofheroes-cost-fortress = Fier, lemn, piatră
ageofheroes-cost-general = Fier, aur
ageofheroes-cost-road = 2 pietre
ageofheroes-cost-city = 2 lemn, piatră
