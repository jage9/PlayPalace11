# Age of Heroes game messages
# A civilization-building card game for 2-6 players

# Game name
game-name-ageofheroes = Doba herojev

# Tribes
ageofheroes-tribe-egyptians = Egipčani
ageofheroes-tribe-romans = Rimljani
ageofheroes-tribe-greeks = Grki
ageofheroes-tribe-babylonians = Babilonci
ageofheroes-tribe-celts = Kelti
ageofheroes-tribe-chinese = Kitajci

# Special Resources (for monuments)
ageofheroes-special-limestone = Apnenec
ageofheroes-special-concrete = Beton
ageofheroes-special-marble = Marmor
ageofheroes-special-bricks = Opeke
ageofheroes-special-sandstone = Peščenjak
ageofheroes-special-granite = Granit

# Standard Resources
ageofheroes-resource-iron = Železo
ageofheroes-resource-wood = Les
ageofheroes-resource-grain = Žito
ageofheroes-resource-stone = Kamen
ageofheroes-resource-gold = Zlato

# Events
ageofheroes-event-population-growth = Rast prebivalstva
ageofheroes-event-earthquake = Potres
ageofheroes-event-eruption = Izbruh
ageofheroes-event-hunger = Lakota
ageofheroes-event-barbarians = Barbari
ageofheroes-event-olympics = Olimpijske igre
ageofheroes-event-hero = Heroj
ageofheroes-event-fortune = Sreča

# Buildings
ageofheroes-building-army = Vojska
ageofheroes-building-fortress = Trdnjava
ageofheroes-building-general = General
ageofheroes-building-road = Cesta
ageofheroes-building-city = Mesto

# Actions
ageofheroes-action-tax-collection = Pobiranje davkov
ageofheroes-action-construction = Gradnja
ageofheroes-action-war = Vojna
ageofheroes-action-do-nothing = Ne počni ničesar
ageofheroes-play = Igraj

# War goals
ageofheroes-war-conquest = Osvojitev
ageofheroes-war-plunder = Rop
ageofheroes-war-destruction = Uničenje

# Game options
ageofheroes-set-victory-cities = Zmagovalna mesta: { $cities }
ageofheroes-enter-victory-cities = Vnesite število mest za zmago (3-7)
ageofheroes-set-victory-monument = Dokončanje spomenika: { $progress }%
ageofheroes-toggle-neighbor-roads = Ceste samo do sosedov: { $enabled }
ageofheroes-set-max-hand = Največja velikost roke: { $cards } kart

# Option change announcements
ageofheroes-option-changed-victory-cities = Za zmago je potrebnih { $cities } mest.
ageofheroes-option-changed-victory-monument = Prag dokončanja spomenika nastavljen na { $progress }%.
ageofheroes-option-changed-neighbor-roads = Ceste samo do sosedov { $enabled }.
ageofheroes-option-changed-max-hand = Največja velikost roke nastavljena na { $cards } kart.

# Setup phase
ageofheroes-setup-start = Si vodja plemena { $tribe }. Tvoj posebni vir za spomenik je { $special }. Vrzi kocke, da določiš vrstni red potez.
ageofheroes-setup-viewer = Igralci mečejo kocke, da določijo vrstni red potez.
ageofheroes-roll-dice = Vrzi kocke
ageofheroes-war-roll-dice = Vrzi kocke
ageofheroes-dice-result = Vrgel si { $total } ({ $die1 } + { $die2 }).
ageofheroes-dice-result-other = { $player } je vrgel { $total }.
ageofheroes-dice-tie = Več igralcev je vrglo { $total }. Mečemo ponovno...
ageofheroes-first-player = { $player } je vrgel najvišje s { $total } in začne prvi.
ageofheroes-first-player-you = S { $total } točkami začneš ti.

# Preparation phase
ageofheroes-prepare-start = Igralci morajo odigrati karte dogodkov in zavreči nesreče.
ageofheroes-prepare-your-turn = Imaš { $count } { $count ->
    [one] karto
    [two] karti
    [few] karte
    *[other] kart
} za igranje ali zavrženje.
ageofheroes-prepare-done = Faza priprave končana.

# Events played/discarded
ageofheroes-population-growth = { $player } igra Rast prebivalstva in gradi novo mesto.
ageofheroes-population-growth-you = Ti igraš Rast prebivalstva in gradiš novo mesto.
ageofheroes-discard-card = { $player } zavrže { $card }.
ageofheroes-discard-card-you = Ti zavržeš { $card }.
ageofheroes-earthquake = Potres je prizadel pleme { $player }; njihove vojske gredo v okrevanje.
ageofheroes-earthquake-you = Potres je prizadel tvoje pleme; tvoje vojske gredo v okrevanje.
ageofheroes-eruption = Izbruh uniči eno od mest { $player }.
ageofheroes-eruption-you = Izbruh uniči eno od tvojih mest.

# Disaster effects
ageofheroes-hunger-strikes = Lakota udari.
ageofheroes-lose-card-hunger = Izgubiš { $card }.
ageofheroes-barbarians-pillage = Barbari napadajo vire { $player }.
ageofheroes-barbarians-attack = Barbari napadajo vire { $player }.
ageofheroes-barbarians-attack-you = Barbari napadajo tvoje vire.
ageofheroes-lose-card-barbarians = Izgubiš { $card }.
ageofheroes-block-with-card = { $player } blokira nesrečo z uporabo { $card }.
ageofheroes-block-with-card-you = Ti blosiraš nesrečo z uporabo { $card }.

# Targeted disaster cards (Earthquake/Eruption)
ageofheroes-select-disaster-target = Izberi cilj za { $card }.
ageofheroes-no-targets = Ni veljavnih ciljev na voljo.
ageofheroes-earthquake-strikes-you = { $attacker } igra Potres proti tebi. Tvoje vojske so onemogočene.
ageofheroes-earthquake-strikes = { $attacker } igra Potres proti { $player }.
ageofheroes-armies-disabled = { $count } { $count ->
    [one] vojska je onemogočena
    [two] vojski sta onemogočeni
    [few] vojske so onemogočene
    *[other] vojsk je onemogočenih
} za eno potezo.
ageofheroes-eruption-strikes-you = { $attacker } igra Izbruh proti tebi. Eno od tvojih mest je uničeno.
ageofheroes-eruption-strikes = { $attacker } igra Izbruh proti { $player }.
ageofheroes-city-destroyed = Mesto je uničeno z izbruhom.

# Fair phase
ageofheroes-fair-start = Svet na tržnici.
ageofheroes-fair-draw-base = Potegneš { $count } { $count ->
    [one] karto
    [two] karti
    [few] karte
    *[other] kart
}.
ageofheroes-fair-draw-roads = Potegneš { $count } { $count ->
    [one] dodatno karto
    [two] dodatni karti
    [few] dodatne karte
    *[other] dodatnih kart
} zahvaljujoč tvojemu cestemu omrežju.
ageofheroes-fair-draw-other = { $player } potegne { $count } { $count ->
    [one] karto
    [two] karti
    [few] karte
    *[other] kart
}.

# Trading/Auction
ageofheroes-auction-start = Dražba se začne.
ageofheroes-offer-trade = Ponudi menjavo
ageofheroes-offer-made = { $player } ponuja { $card } za { $wanted }.
ageofheroes-offer-made-you = Ti ponujaš { $card } za { $wanted }.
ageofheroes-trade-accepted = { $player } sprejme ponudbo { $other } in zamenja { $give } za { $receive }.
ageofheroes-trade-accepted-you = Ti sprejmeš ponudbo { $other } in prejmeš { $receive }.
ageofheroes-trade-cancelled = { $player } umakne svojo ponudbo za { $card }.
ageofheroes-trade-cancelled-you = Ti umakneš svojo ponudbo za { $card }.
ageofheroes-stop-trading = Prenehaj trgovati
ageofheroes-select-request = Ponujaš { $card }. Kaj želiš v zameno?
ageofheroes-cancel = Prekliči
ageofheroes-left-auction = { $player } odide.
ageofheroes-left-auction-you = Ti odiš s tržnice.
ageofheroes-any-card = Kakršnokoli karto
ageofheroes-cannot-trade-own-special = Ne moreš zamenjati svojega posebnega vira za spomenik.
ageofheroes-resource-not-in-game = Ta posebni vir se ne uporablja v tej igri.

# Main play phase
ageofheroes-play-start = Faza igre.
ageofheroes-day = Dan { $day }
ageofheroes-draw-card = { $player } potegne karto iz kupa.
ageofheroes-draw-card-you = Ti potegneš { $card } iz kupa.
ageofheroes-your-action = Kaj želiš storiti?

# Tax Collection
ageofheroes-tax-collection = { $player } izbere Pobiranje davkov: { $cities } { $cities ->
    [one] mesto
    [two] mesti
    [few] mesta
    *[other] mest
} pobere { $cards } { $cards ->
    [one] karto
    [two] karti
    [few] karte
    *[other] kart
}.
ageofheroes-tax-collection-you = Ti izbereš Pobiranje davkov: { $cities } { $cities ->
    [one] mesto
    [two] mesti
    [few] mesta
    *[other] mest
} pobere { $cards } { $cards ->
    [one] karto
    [two] karti
    [few] karte
    *[other] kart
}.
ageofheroes-tax-no-city = Pobiranje davkov: Nimaš preživelih mest. Zavrzi karto, da potegneš novo.
ageofheroes-tax-no-city-done = { $player } izbere Pobiranje davkov, a nima mest, zato zamenja karto.
ageofheroes-tax-no-city-done-you = Pobiranje davkov: Zamenjal si { $card } za novo karto.

# Construction
ageofheroes-construction-menu = Kaj želiš zgraditi?
ageofheroes-construction-done = { $player } je zgradil { $article } { $building }.
ageofheroes-construction-done-you = Ti si zgradil { $article } { $building }.
ageofheroes-construction-stop = Prenehaj graditi
ageofheroes-construction-stopped = Odločil si se prenehati graditi.
ageofheroes-road-select-neighbor = Izberi, h kateremu sosedu želiš zgraditi cesto.
ageofheroes-direction-left = Na tvojo levo
ageofheroes-direction-right = Na tvojo desno
ageofheroes-road-request-sent = Prošnja za cesto poslana. Čakamo na odobritev soseda.
ageofheroes-road-request-received = { $requester } prosi za dovoljenje za gradnjo ceste do tvojega plemena.
ageofheroes-road-request-denied-you = Ti si zavrnil prošnjo za cesto.
ageofheroes-road-request-denied = { $denier } je zavrnil tvojo prošnjo za cesto.
ageofheroes-road-built = { $tribe1 } in { $tribe2 } sta zdaj povezana s cesto.
ageofheroes-road-no-target = Ni sosednjih plemen na voljo za gradnjo ceste.
ageofheroes-approve = Odobri
ageofheroes-deny = Zavrni
ageofheroes-supply-exhausted = Ni več { $building } na voljo za gradnjo.

# Do Nothing
ageofheroes-do-nothing = { $player } preskoči.
ageofheroes-do-nothing-you = Ti preskočiš...

# War
ageofheroes-war-declare = { $attacker } napove vojno { $defender }. Cilj: { $goal }.
ageofheroes-war-prepare = Izberi svoje vojske za { $action }.
ageofheroes-war-no-army = Nimaš vojsk ali kart herojev na voljo.
ageofheroes-war-no-targets = Ni veljavnih ciljev za vojno.
ageofheroes-war-no-valid-goal = Ni veljavnih vojnih ciljev proti temu cilju.
ageofheroes-war-select-target = Izberi, katerega igralca boš napadel.
ageofheroes-war-select-goal = Izberi svoj vojni cilj.
ageofheroes-war-prepare-attack = Izberi svoje napadalske sile.
ageofheroes-war-prepare-defense = { $attacker } te napada; Izberi svoje obrambne sile.
ageofheroes-war-select-armies = Izberi vojske: { $count }
ageofheroes-war-select-generals = Izberi generale: { $count }
ageofheroes-war-select-heroes = Izberi heroje: { $count }
ageofheroes-war-attack = Napadi...
ageofheroes-war-defend = Brani...
ageofheroes-war-prepared = Tvoje sile: { $armies } { $armies ->
    [one] vojska
    [two] vojski
    [few] vojske
    *[other] vojsk
}{ $generals ->
    [0] {""}
    [one] {" in 1 general"}
    [two] {" in { $generals } generala"}
    [few] {" in { $generals } generali"}
    *[other] {" in { $generals } generalov"}
}{ $heroes ->
    [0] {""}
    [one] {" in 1 heroj"}
    [two] {" in { $heroes } heroja"}
    [few] {" in { $heroes } heroji"}
    *[other] {" in { $heroes } herojev"}
}.
ageofheroes-war-roll-you = Ti vržeš { $roll }.
ageofheroes-war-roll-other = { $player } vrže { $roll }.
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"+1 iz trdnjave = { $total } skupaj"}
            [two] {"+{ $fortress } iz trdnjav = { $total } skupaj"}
            [few] {"+{ $fortress } iz trdnjav = { $total } skupaj"}
            *[other] {"+{ $fortress } iz trdnjav = { $total } skupaj"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"+{ $general } iz generala = { $total } skupaj"}
            [one] {"+{ $general } iz generala, +1 iz trdnjave = { $total } skupaj"}
            [two] {"+{ $general } iz generala, +{ $fortress } iz trdnjav = { $total } skupaj"}
            [few] {"+{ $general } iz generala, +{ $fortress } iz trdnjav = { $total } skupaj"}
            *[other] {"+{ $general } iz generala, +{ $fortress } iz trdnjav = { $total } skupaj"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"{ $player }: +1 iz trdnjave = { $total } skupaj"}
            [two] {"{ $player }: +{ $fortress } iz trdnjav = { $total } skupaj"}
            [few] {"{ $player }: +{ $fortress } iz trdnjav = { $total } skupaj"}
            *[other] {"{ $player }: +{ $fortress } iz trdnjav = { $total } skupaj"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } iz generala = { $total } skupaj"}
            [one] {"{ $player }: +{ $general } iz generala, +1 iz trdnjave = { $total } skupaj"}
            [two] {"{ $player }: +{ $general } iz generala, +{ $fortress } iz trdnjav = { $total } skupaj"}
            [few] {"{ $player }: +{ $general } iz generala, +{ $fortress } iz trdnjav = { $total } skupaj"}
            *[other] {"{ $player }: +{ $general } iz generala, +{ $fortress } iz trdnjav = { $total } skupaj"}
        }
    }
}

# Battle
ageofheroes-battle-start = Bitka se začne. { $attacker } ima { $att_armies } { $att_armies ->
    [one] vojsko
    [two] vojski
    [few] vojske
    *[other] vojsk
} proti { $defender } z { $def_armies } { $def_armies ->
    [one] vojsko
    [two] vojskama
    [few] vojskami
    *[other] vojskami
}.
ageofheroes-dice-roll-detailed = { $name } vrže { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } iz generala" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 iz trdnjave" }
    [two] { " + { $fortress } iz trdnjav" }
    [few] { " + { $fortress } iz trdnjav" }
    *[other] { " + { $fortress } iz trdnjav" }
} = { $total }.
ageofheroes-dice-roll-detailed-you = Ti vržeš { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } iz generala" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 iz trdnjave" }
    [two] { " + { $fortress } iz trdnjav" }
    [few] { " + { $fortress } iz trdnjav" }
    *[other] { " + { $fortress } iz trdnjav" }
} = { $total }.
ageofheroes-round-attacker-wins = { $attacker } zmaga v rundi ({ $att_total } proti { $def_total }). { $defender } izgubi vojsko.
ageofheroes-round-defender-wins = { $defender } se uspešno brani ({ $def_total } proti { $att_total }). { $attacker } izgubi vojsko.
ageofheroes-round-draw = Obe strani sta na { $total }. Ni izgubljenih vojsk.
ageofheroes-battle-victory-attacker = { $attacker } premaga { $defender }.
ageofheroes-battle-victory-defender = { $defender } se uspešno brani proti { $attacker }.
ageofheroes-battle-mutual-defeat = { $attacker } in { $defender } izgubita vse vojske.
ageofheroes-general-bonus = +{ $count } iz { $count ->
    [one] generala
    [two] generalov
    [few] generalov
    *[other] generalov
}
ageofheroes-fortress-bonus = +{ $count } iz obrambe trdnjave
ageofheroes-battle-winner = { $winner } zmaga v bitki.
ageofheroes-battle-draw = Bitka se konča z neodločeno...
ageofheroes-battle-continue = Nadaljuj bitko.
ageofheroes-battle-end = Bitka je končana.

# War outcomes
ageofheroes-conquest-success = { $attacker } osvoji { $count } { $count ->
    [one] mesto
    [two] mesti
    [few] mesta
    *[other] mest
} od { $defender }.
ageofheroes-plunder-success = { $attacker } orobi { $count } { $count ->
    [one] karto
    [two] karti
    [few] karte
    *[other] kart
} od { $defender }.
ageofheroes-destruction-success = { $attacker } uniči { $count } { $count ->
    [one] vir
    [two] vira
    [few] vire
    *[other] virov
} spomenika { $defender }.
ageofheroes-army-losses = { $player } izgubi { $count } { $count ->
    [one] vojsko
    [two] vojski
    [few] vojske
    *[other] vojsk
}.
ageofheroes-army-losses-you = Ti izgubiš { $count } { $count ->
    [one] vojsko
    [two] vojski
    [few] vojske
    *[other] vojsk
}.

# Army return
ageofheroes-army-return-road = Tvoje čete se takoj vrnejo po cesti.
ageofheroes-army-return-delayed = { $count } { $count ->
    [one] enota se vrne
    [two] enoti se vrneta
    [few] enote se vrnejo
    *[other] enot se vrne
} ob koncu tvoje naslednje poteze.
ageofheroes-army-returned = Čete { $player } so se vrnile iz vojne.
ageofheroes-army-returned-you = Tvoje čete so se vrnile iz vojne.
ageofheroes-army-recover = Vojske { $player } okrevajo po potresu.
ageofheroes-army-recover-you = Tvoje vojske okrevajo po potresu.

# Olympics
ageofheroes-olympics-cancel = { $player } igra Olimpijske igre. Vojna preklicana.
ageofheroes-olympics-prompt = { $attacker } je napovedal vojno. Imaš Olimpijske igre - jih uporabiš za preklic?
ageofheroes-yes = Da
ageofheroes-no = Ne

# Monument progress
ageofheroes-monument-progress = Spomenik { $player } je { $count }/5 dokončan.
ageofheroes-monument-progress-you = Tvoj spomenik je { $count }/5 dokončan.

# Hand management
ageofheroes-discard-excess = Imaš več kot { $max } kart. Zavrzi { $count } { $count ->
    [one] karto
    [two] karti
    [few] karte
    *[other] kart
}.
ageofheroes-discard-excess-other = { $player } mora zavreči presežne karte.
ageofheroes-discard-more = Zavrzi še { $count } { $count ->
    [one] karto
    [two] karti
    [few] karte
    *[other] kart
}.

# Victory
ageofheroes-victory-cities = { $player } je zgradil 5 mest! Imperij petih mest.
ageofheroes-victory-cities-you = Ti si zgradil 5 mest! Imperij petih mest.
ageofheroes-victory-monument = { $player } je dokončal svoj spomenik! Nosilci velike kulture.
ageofheroes-victory-monument-you = Ti si dokončal svoj spomenik! Nosilci velike kulture.
ageofheroes-victory-last-standing = { $player } je zadnje preživelo pleme! Najvztrajnejši.
ageofheroes-victory-last-standing-you = Ti si zadnje preživelo pleme! Najvztrajnejši.
ageofheroes-game-over = Igra končana.

# Elimination
ageofheroes-eliminated = { $player } je bil eliminiran.
ageofheroes-eliminated-you = Ti si bil eliminiran.

# Hand
ageofheroes-hand-empty = Nimaš kart.
ageofheroes-hand-contents = Tvoja roka ({ $count } { $count ->
    [one] karta
    [two] karti
    [few] karte
    *[other] kart
}): { $cards }

# Status
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [one] mesto
    [two] mesti
    [few] mesta
    *[other] mest
}, { $armies } { $armies ->
    [one] vojska
    [two] vojski
    [few] vojske
    *[other] vojsk
}, { $monument }/5 spomenik
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = Mesta: { $count }
ageofheroes-status-armies = Vojske: { $count }
ageofheroes-status-generals = Generali: { $count }
ageofheroes-status-fortresses = Trdnjave: { $count }
ageofheroes-status-monument = Spomenik: { $count }/5
ageofheroes-status-roads = Ceste: { $left }{ $right }
ageofheroes-status-road-left = levo
ageofheroes-status-road-right = desno
ageofheroes-status-none = nobena
ageofheroes-status-earthquake-armies = Vojske v okrevanju: { $count }
ageofheroes-status-returning-armies = Vojske, ki se vračajo: { $count }
ageofheroes-status-returning-generals = Generali, ki se vračajo: { $count }

# Deck info
ageofheroes-deck-empty = V kupu ni več kart { $card }.
ageofheroes-deck-count = Preostale karte: { $count }
ageofheroes-deck-reshuffled = Kup zavrženih kart je bil premešan nazaj v kup.

# Give up
ageofheroes-give-up-confirm = Si prepričan, da se želiš vdati?
ageofheroes-gave-up = { $player } se je vdal!
ageofheroes-gave-up-you = Ti si se vdal!

# Hero card
ageofheroes-hero-use = Uporabi kot vojsko ali generala?
ageofheroes-hero-army = Vojska
ageofheroes-hero-general = General

# Fortune card
ageofheroes-fortune-reroll = { $player } uporabi Srečo za ponovni met.
ageofheroes-fortune-prompt = Izgubil si met. Uporabiš Srečo za ponovni met?

# Disabled action reasons
ageofheroes-not-your-turn = Ni tvoja poteza.
ageofheroes-game-not-started = Igra se še ni začela.
ageofheroes-wrong-phase = To dejanje ni na voljo v trenutni fazi.
ageofheroes-no-resources = Nimaš zahtevanih virov.

# Building costs (for display)
ageofheroes-cost-army = 2 žito, železo
ageofheroes-cost-fortress = Železo, les, kamen
ageofheroes-cost-general = Železo, zlato
ageofheroes-cost-road = 2 kamna
ageofheroes-cost-city = 2 les, kamen
