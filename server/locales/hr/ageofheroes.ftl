# Age of Heroes game messages
# A civilization-building card game for 2-6 players

# Game name
game-name-ageofheroes = Doba heroja

# Tribes
ageofheroes-tribe-egyptians = Egipćani
ageofheroes-tribe-romans = Rimljani
ageofheroes-tribe-greeks = Grci
ageofheroes-tribe-babylonians = Babilonci
ageofheroes-tribe-celts = Kelti
ageofheroes-tribe-chinese = Kinezi

# Special Resources (for monuments)
ageofheroes-special-limestone = Vapnenac
ageofheroes-special-concrete = Beton
ageofheroes-special-marble = Mramor
ageofheroes-special-bricks = Cigle
ageofheroes-special-sandstone = Pješčenjak
ageofheroes-special-granite = Granit

# Standard Resources
ageofheroes-resource-iron = Željezo
ageofheroes-resource-wood = Drvo
ageofheroes-resource-grain = Žito
ageofheroes-resource-stone = Kamen
ageofheroes-resource-gold = Zlato

# Events
ageofheroes-event-population-growth = Rast stanovništva
ageofheroes-event-earthquake = Potres
ageofheroes-event-eruption = Erupcija
ageofheroes-event-hunger = Glad
ageofheroes-event-barbarians = Barbari
ageofheroes-event-olympics = Olimpijske igre
ageofheroes-event-hero = Heroj
ageofheroes-event-fortune = Sreća

# Buildings
ageofheroes-building-army = Vojska
ageofheroes-building-fortress = Tvrđava
ageofheroes-building-general = General
ageofheroes-building-road = Cesta
ageofheroes-building-city = Grad

# Actions
ageofheroes-action-tax-collection = Prikupljanje poreza
ageofheroes-action-construction = Gradnja
ageofheroes-action-war = Rat
ageofheroes-action-do-nothing = Ne radi ništa
ageofheroes-play = Igraj

# War goals
ageofheroes-war-conquest = Osvajanje
ageofheroes-war-plunder = Pljačka
ageofheroes-war-destruction = Razaranje

# Game options
ageofheroes-set-victory-cities = Gradovi za pobjedu: { $cities }
ageofheroes-enter-victory-cities = Unesite broj gradova za pobjedu (3-7)
ageofheroes-set-victory-monument = Dovršenost spomenika: { $progress }%
ageofheroes-toggle-neighbor-roads = Ceste samo do susjeda: { $enabled }
ageofheroes-set-max-hand = Maksimalna veličina ruke: { $cards } karata

# Option change announcements
ageofheroes-option-changed-victory-cities = Za pobjedu potrebno { $cities } gradova.
ageofheroes-option-changed-victory-monument = Prag dovršenosti spomenika postavljen na { $progress }%.
ageofheroes-option-changed-neighbor-roads = Ceste samo do susjeda { $enabled }.
ageofheroes-option-changed-max-hand = Maksimalna veličina ruke postavljena na { $cards } karata.

# Setup phase
ageofheroes-setup-start = Vi ste vođa plemena { $tribe }. Vaš poseban resurs za spomenik je { $special }. Bacite kockice da odredite redoslijed poteza.
ageofheroes-setup-viewer = Igrači bacaju kockice da odrede redoslijed poteza.
ageofheroes-roll-dice = Bacite kockice
ageofheroes-war-roll-dice = Bacite kockice
ageofheroes-dice-result = Bacili ste { $total } ({ $die1 } + { $die2 }).
ageofheroes-dice-result-other = { $player } je bacio { $total }.
ageofheroes-dice-tie = Više igrača ima { $total }. Bacamo ponovno...
ageofheroes-first-player = { $player } je bacio najviše s { $total } i ide prvi.
ageofheroes-first-player-you = S { $total } bodova, vi idete prvi.

# Preparation phase
ageofheroes-prepare-start = Igrači moraju odigrati karte događaja i odbaciti katastrofe.
ageofheroes-prepare-your-turn = Imate { $count } { $count ->
    [one] kartu
    [few] karte
    *[other] karata
} za igranje ili odbacivanje.
ageofheroes-prepare-done = Faza pripreme završena.

# Events played/discarded
ageofheroes-population-growth = { $player } igra Rast stanovništva i gradi novi grad.
ageofheroes-population-growth-you = Vi igrate Rast stanovništva i gradite novi grad.
ageofheroes-discard-card = { $player } odbacuje { $card }.
ageofheroes-discard-card-you = Vi odbacujete { $card }.
ageofheroes-earthquake = Potres pogađa pleme { $player }; njihove vojske idu na oporavak.
ageofheroes-earthquake-you = Potres pogađa vaše pleme; vaše vojske idu na oporavak.
ageofheroes-eruption = Erupcija uništava jedan od { $player } gradova.
ageofheroes-eruption-you = Erupcija uništava jedan od vaših gradova.

# Disaster effects
ageofheroes-hunger-strikes = Glad udara.
ageofheroes-lose-card-hunger = Gubite { $card }.
ageofheroes-barbarians-pillage = Barbari napadaju resurse { $player }.
ageofheroes-barbarians-attack = Barbari napadaju resurse { $player }.
ageofheroes-barbarians-attack-you = Barbari napadaju vaše resurse.
ageofheroes-lose-card-barbarians = Gubite { $card }.
ageofheroes-block-with-card = { $player } blokira katastrofu koristeći { $card }.
ageofheroes-block-with-card-you = Vi blokirate katastrofu koristeći { $card }.

# Targeted disaster cards (Earthquake/Eruption)
ageofheroes-select-disaster-target = Odaberite metu za { $card }.
ageofheroes-no-targets = Nema dostupnih meta.
ageofheroes-earthquake-strikes-you = { $attacker } igra Potres protiv vas. Vaše vojske su onesposobljene.
ageofheroes-earthquake-strikes = { $attacker } igra Potres protiv { $player }.
ageofheroes-armies-disabled = { $count } { $count ->
    [one] vojska je onesposobljena
    [few] vojske su onesposobljene
    *[other] vojski je onesposobljeno
} na jedan potez.
ageofheroes-eruption-strikes-you = { $attacker } igra Erupciju protiv vas. Jedan od vaših gradova je uništen.
ageofheroes-eruption-strikes = { $attacker } igra Erupciju protiv { $player }.
ageofheroes-city-destroyed = Grad je uništen erupcijom.

# Fair phase
ageofheroes-fair-start = Svitanje na tržnici.
ageofheroes-fair-draw-base = Povlačite { $count } { $count ->
    [one] kartu
    [few] karte
    *[other] karata
}.
ageofheroes-fair-draw-roads = Povlačite { $count } { $count ->
    [one] dodatnu kartu
    [few] dodatne karte
    *[other] dodatnih karata
} zahvaljujući vašoj cestovnoj mreži.
ageofheroes-fair-draw-other = { $player } povlači { $count } { $count ->
    [one] kartu
    [few] karte
    *[other] karata
}.

# Trading/Auction
ageofheroes-auction-start = Aukcija počinje.
ageofheroes-offer-trade = Ponudi razmjenu
ageofheroes-offer-made = { $player } nudi { $card } za { $wanted }.
ageofheroes-offer-made-you = Vi nudite { $card } za { $wanted }.
ageofheroes-trade-accepted = { $player } prihvaća ponudu { $other } i mijenja { $give } za { $receive }.
ageofheroes-trade-accepted-you = Vi prihvaćate ponudu { $other } i dobivate { $receive }.
ageofheroes-trade-cancelled = { $player } povlači svoju ponudu za { $card }.
ageofheroes-trade-cancelled-you = Vi povlačite svoju ponudu za { $card }.
ageofheroes-stop-trading = Prestani trgovati
ageofheroes-select-request = Nudite { $card }. Što želite zauzvrat?
ageofheroes-cancel = Otkaži
ageofheroes-left-auction = { $player } odlazi.
ageofheroes-left-auction-you = Vi odlazite s tržnice.
ageofheroes-any-card = Bilo koja karta
ageofheroes-cannot-trade-own-special = Ne možete trgovati vlastitim posebnim resursom za spomenik.
ageofheroes-resource-not-in-game = Ovaj poseban resurs se ne koristi u ovoj igri.

# Main play phase
ageofheroes-play-start = Faza igre.
ageofheroes-day = Dan { $day }
ageofheroes-draw-card = { $player } povlači kartu iz špila.
ageofheroes-draw-card-you = Vi povlačite { $card } iz špila.
ageofheroes-your-action = Što želite učiniti?

# Tax Collection
ageofheroes-tax-collection = { $player } bira Prikupljanje poreza: { $cities } { $cities ->
    [one] grad
    [few] grada
    *[other] gradova
} prikuplja { $cards } { $cards ->
    [one] kartu
    [few] karte
    *[other] karata
}.
ageofheroes-tax-collection-you = Vi birate Prikupljanje poreza: { $cities } { $cities ->
    [one] grad
    [few] grada
    *[other] gradova
} prikuplja { $cards } { $cards ->
    [one] kartu
    [few] karte
    *[other] karata
}.
ageofheroes-tax-no-city = Prikupljanje poreza: Nemate preživjelih gradova. Odbacite kartu da povučete novu.
ageofheroes-tax-no-city-done = { $player } bira Prikupljanje poreza ali nema gradova, pa mijenja kartu.
ageofheroes-tax-no-city-done-you = Prikupljanje poreza: Zamijenili ste { $card } za novu kartu.

# Construction
ageofheroes-construction-menu = Što želite graditi?
ageofheroes-construction-done = { $player } je izgradio { $article } { $building }.
ageofheroes-construction-done-you = Vi ste izgradili { $article } { $building }.
ageofheroes-construction-stop = Prestani graditi
ageofheroes-construction-stopped = Odlučili ste prestati graditi.
ageofheroes-road-select-neighbor = Odaberite kojem susjedu želite graditi cestu.
ageofheroes-direction-left = Prema lijevo
ageofheroes-direction-right = Prema desno
ageofheroes-road-request-sent = Zahtjev za cestu poslan. Čekanje odobrenja susjeda.
ageofheroes-road-request-received = { $requester } traži dozvolu za izgradnju ceste do vašeg plemena.
ageofheroes-road-request-denied-you = Vi ste odbili zahtjev za cestu.
ageofheroes-road-request-denied = { $denier } je odbio vaš zahtjev za cestu.
ageofheroes-road-built = { $tribe1 } i { $tribe2 } su sada povezani cestom.
ageofheroes-road-no-target = Nema susjednih plemena za izgradnju ceste.
ageofheroes-approve = Odobri
ageofheroes-deny = Odbij
ageofheroes-supply-exhausted = Nema više { $building } za gradnju.

# Do Nothing
ageofheroes-do-nothing = { $player } preskače.
ageofheroes-do-nothing-you = Vi preskačete...

# War
ageofheroes-war-declare = { $attacker } objavljuje rat { $defender }. Cilj: { $goal }.
ageofheroes-war-prepare = Odaberite svoje vojske za { $action }.
ageofheroes-war-no-army = Nemate vojske ili karte heroja.
ageofheroes-war-no-targets = Nema valjanih meta za rat.
ageofheroes-war-no-valid-goal = Nema valjanih ciljeva rata protiv ove mete.
ageofheroes-war-select-target = Odaberite kojeg igrača napadnuti.
ageofheroes-war-select-goal = Odaberite svoj cilj rata.
ageofheroes-war-prepare-attack = Odaberite svoje napadačke snage.
ageofheroes-war-prepare-defense = { $attacker } vas napada; Odaberite svoje obrambene snage.
ageofheroes-war-select-armies = Odaberi vojske: { $count }
ageofheroes-war-select-generals = Odaberi generale: { $count }
ageofheroes-war-select-heroes = Odaberi heroje: { $count }
ageofheroes-war-attack = Napadni...
ageofheroes-war-defend = Obrani...
ageofheroes-war-prepared = Vaše snage: { $armies } { $armies ->
    [one] vojska
    [few] vojske
    *[other] vojski
}{ $generals ->
    [0] {""}
    [one] {" i 1 general"}
    [few] {" i { $generals } generala"}
    *[other] {" i { $generals } generala"}
}{ $heroes ->
    [0] {""}
    [one] {" i 1 heroj"}
    [few] {" i { $heroes } heroja"}
    *[other] {" i { $heroes } heroja"}
}.
ageofheroes-war-roll-you = Vi bacate { $roll }.
ageofheroes-war-roll-other = { $player } baca { $roll }.
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"+1 od tvrđave = { $total } ukupno"}
            [few] {"+{ $fortress } od tvrđava = { $total } ukupno"}
            *[other] {"+{ $fortress } od tvrđava = { $total } ukupno"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"+{ $general } od generala = { $total } ukupno"}
            [one] {"+{ $general } od generala, +1 od tvrđave = { $total } ukupno"}
            [few] {"+{ $general } od generala, +{ $fortress } od tvrđava = { $total } ukupno"}
            *[other] {"+{ $general } od generala, +{ $fortress } od tvrđava = { $total } ukupno"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"{ $player }: +1 od tvrđave = { $total } ukupno"}
            [few] {"{ $player }: +{ $fortress } od tvrđava = { $total } ukupno"}
            *[other] {"{ $player }: +{ $fortress } od tvrđava = { $total } ukupno"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } od generala = { $total } ukupno"}
            [one] {"{ $player }: +{ $general } od generala, +1 od tvrđave = { $total } ukupno"}
            [few] {"{ $player }: +{ $general } od generala, +{ $fortress } od tvrđava = { $total } ukupno"}
            *[other] {"{ $player }: +{ $general } od generala, +{ $fortress } od tvrđava = { $total } ukupno"}
        }
    }
}

# Battle
ageofheroes-battle-start = Bitka počinje. { $attacker } ima { $att_armies } { $att_armies ->
    [one] vojsku
    [few] vojske
    *[other] vojski
} protiv { $defender } sa { $def_armies } { $def_armies ->
    [one] vojskom
    [few] vojske
    *[other] vojski
}.
ageofheroes-dice-roll-detailed = { $name } baca { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } od generala" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 od tvrđave" }
    [few] { " + { $fortress } od tvrđava" }
    *[other] { " + { $fortress } od tvrđava" }
} = { $total }.
ageofheroes-dice-roll-detailed-you = Vi bacate { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } od generala" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 od tvrđave" }
    [few] { " + { $fortress } od tvrđava" }
    *[other] { " + { $fortress } od tvrđava" }
} = { $total }.
ageofheroes-round-attacker-wins = { $attacker } pobjeđuje u rundi ({ $att_total } protiv { $def_total }). { $defender } gubi vojsku.
ageofheroes-round-defender-wins = { $defender } se uspješno brani ({ $def_total } protiv { $att_total }). { $attacker } gubi vojsku.
ageofheroes-round-draw = Obje strane imaju { $total }. Nema izgubljenih vojski.
ageofheroes-battle-victory-attacker = { $attacker } pobjeđuje { $defender }.
ageofheroes-battle-victory-defender = { $defender } se uspješno brani protiv { $attacker }.
ageofheroes-battle-mutual-defeat = I { $attacker } i { $defender } gube sve vojske.
ageofheroes-general-bonus = +{ $count } od { $count ->
    [one] generala
    [few] generala
    *[other] generala
}
ageofheroes-fortress-bonus = +{ $count } od obrane tvrđave
ageofheroes-battle-winner = { $winner } pobjeđuje u bitci.
ageofheroes-battle-draw = Bitka završava neriješeno...
ageofheroes-battle-continue = Nastavite bitku.
ageofheroes-battle-end = Bitka je završena.

# War outcomes
ageofheroes-conquest-success = { $attacker } osvaja { $count } { $count ->
    [one] grad
    [few] grada
    *[other] gradova
} od { $defender }.
ageofheroes-plunder-success = { $attacker } pljačka { $count } { $count ->
    [one] kartu
    [few] karte
    *[other] karata
} od { $defender }.
ageofheroes-destruction-success = { $attacker } uništava { $count } { $count ->
    [one] resurs
    [few] resursa
    *[other] resursa
} spomenika { $defender }.
ageofheroes-army-losses = { $player } gubi { $count } { $count ->
    [one] vojsku
    [few] vojske
    *[other] vojski
}.
ageofheroes-army-losses-you = Vi gubite { $count } { $count ->
    [one] vojsku
    [few] vojske
    *[other] vojski
}.

# Army return
ageofheroes-army-return-road = Vaše trupe se odmah vraćaju cestom.
ageofheroes-army-return-delayed = { $count } { $count ->
    [one] jedinica se vraća
    [few] jedinice se vraćaju
    *[other] jedinica se vraća
} na kraju vašeg sljedećeg poteza.
ageofheroes-army-returned = Trupe { $player } su se vratile s rata.
ageofheroes-army-returned-you = Vaše trupe su se vratile s rata.
ageofheroes-army-recover = Vojske { $player } se oporavljaju od potresa.
ageofheroes-army-recover-you = Vaše vojske se oporavljaju od potresa.

# Olympics
ageofheroes-olympics-cancel = { $player } igra Olimpijske igre. Rat otkazan.
ageofheroes-olympics-prompt = { $attacker } je objavio rat. Imate Olimpijske igre - želite li ih iskoristiti za otkazivanje?
ageofheroes-yes = Da
ageofheroes-no = Ne

# Monument progress
ageofheroes-monument-progress = Spomenik { $player } je dovršen { $count }/5.
ageofheroes-monument-progress-you = Vaš spomenik je dovršen { $count }/5.

# Hand management
ageofheroes-discard-excess = Imate više od { $max } karata. Odbacite { $count } { $count ->
    [one] kartu
    [few] karte
    *[other] karata
}.
ageofheroes-discard-excess-other = { $player } mora odbaciti višak karata.
ageofheroes-discard-more = Odbacite još { $count } { $count ->
    [one] kartu
    [few] karte
    *[other] karata
}.

# Victory
ageofheroes-victory-cities = { $player } je izgradio 5 gradova! Carstvo pet gradova.
ageofheroes-victory-cities-you = Vi ste izgradili 5 gradova! Carstvo pet gradova.
ageofheroes-victory-monument = { $player } je dovršio svoj spomenik! Nositelji velike kulture.
ageofheroes-victory-monument-you = Vi ste dovršili svoj spomenik! Nositelji velike kulture.
ageofheroes-victory-last-standing = { $player } je posljednje preživjelo pleme! Najuporniji.
ageofheroes-victory-last-standing-you = Vi ste posljednje preživjelo pleme! Najuporniji.
ageofheroes-game-over = Igra završena.

# Elimination
ageofheroes-eliminated = { $player } je eliminiran.
ageofheroes-eliminated-you = Vi ste eliminirani.

# Hand
ageofheroes-hand-empty = Nemate karata.
ageofheroes-hand-contents = Vaša ruka ({ $count } { $count ->
    [one] karta
    [few] karte
    *[other] karata
}): { $cards }

# Status
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [one] grad
    [few] grada
    *[other] gradova
}, { $armies } { $armies ->
    [one] vojska
    [few] vojske
    *[other] vojski
}, { $monument }/5 spomenik
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = Gradovi: { $count }
ageofheroes-status-armies = Vojske: { $count }
ageofheroes-status-generals = Generali: { $count }
ageofheroes-status-fortresses = Tvrđave: { $count }
ageofheroes-status-monument = Spomenik: { $count }/5
ageofheroes-status-roads = Ceste: { $left }{ $right }
ageofheroes-status-road-left = lijevo
ageofheroes-status-road-right = desno
ageofheroes-status-none = ništa
ageofheroes-status-earthquake-armies = Vojske na oporavku: { $count }
ageofheroes-status-returning-armies = Vojske koje se vraćaju: { $count }
ageofheroes-status-returning-generals = Generali koji se vraćaju: { $count }

# Deck info
ageofheroes-deck-empty = Nema više { $card } karata u špilu.
ageofheroes-deck-count = Preostalo karata: { $count }
ageofheroes-deck-reshuffled = Hrpa odbačenih karata je promiješana u špil.

# Give up
ageofheroes-give-up-confirm = Jeste li sigurni da želite odustati?
ageofheroes-gave-up = { $player } je odustao!
ageofheroes-gave-up-you = Vi ste odustali!

# Hero card
ageofheroes-hero-use = Koristiti kao vojsku ili generala?
ageofheroes-hero-army = Vojska
ageofheroes-hero-general = General

# Fortune card
ageofheroes-fortune-reroll = { $player } koristi Sreću za ponovno bacanje.
ageofheroes-fortune-prompt = Izgubili ste bacanje. Iskoristiti Sreću za ponovno bacanje?

# Disabled action reasons
ageofheroes-not-your-turn = Nije vaš potez.
ageofheroes-game-not-started = Igra još nije počela.
ageofheroes-wrong-phase = Ova akcija nije dostupna u trenutnoj fazi.
ageofheroes-no-resources = Nemate potrebne resurse.

# Building costs (for display)
ageofheroes-cost-army = 2 žita, željezo
ageofheroes-cost-fortress = Željezo, drvo, kamen
ageofheroes-cost-general = Željezo, zlato
ageofheroes-cost-road = 2 kamena
ageofheroes-cost-city = 2 drva, kamen
