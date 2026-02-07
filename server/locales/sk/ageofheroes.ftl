# Age of Heroes game messages
# A civilization-building card game for 2-6 players

# Game name
game-name-ageofheroes = Vek hrdinov

# Tribes
ageofheroes-tribe-egyptians = Egypťania
ageofheroes-tribe-romans = Rimania
ageofheroes-tribe-greeks = Gréci
ageofheroes-tribe-babylonians = Babylončania
ageofheroes-tribe-celts = Kelti
ageofheroes-tribe-chinese = Číňania

# Special Resources (for monuments)
ageofheroes-special-limestone = Vápenec
ageofheroes-special-concrete = Betón
ageofheroes-special-marble = Mramor
ageofheroes-special-bricks = Tehly
ageofheroes-special-sandstone = Pieskoviec
ageofheroes-special-granite = Žula

# Standard Resources
ageofheroes-resource-iron = Železo
ageofheroes-resource-wood = Drevo
ageofheroes-resource-grain = Obilie
ageofheroes-resource-stone = Kameň
ageofheroes-resource-gold = Zlato

# Events
ageofheroes-event-population-growth = Rast populácie
ageofheroes-event-earthquake = Zemetrasenie
ageofheroes-event-eruption = Erupcia
ageofheroes-event-hunger = Hlad
ageofheroes-event-barbarians = Barbari
ageofheroes-event-olympics = Olympijské hry
ageofheroes-event-hero = Hrdina
ageofheroes-event-fortune = Šťastie

# Buildings
ageofheroes-building-army = Armáda
ageofheroes-building-fortress = Pevnosť
ageofheroes-building-general = Generál
ageofheroes-building-road = Cesta
ageofheroes-building-city = Mesto

# Actions
ageofheroes-action-tax-collection = Výber daní
ageofheroes-action-construction = Výstavba
ageofheroes-action-war = Vojna
ageofheroes-action-do-nothing = Neurobiť nič
ageofheroes-play = Hraj

# War goals
ageofheroes-war-conquest = Dobytie
ageofheroes-war-plunder = Plienenie
ageofheroes-war-destruction = Zničenie

# Game options
ageofheroes-set-victory-cities = Mestá na víťazstvo: { $cities }
ageofheroes-enter-victory-cities = Zadajte počet miest na výhru (3-7)
ageofheroes-set-victory-monument = Dokončenie pamätníka: { $progress }%
ageofheroes-toggle-neighbor-roads = Cesty len k susedom: { $enabled }
ageofheroes-set-max-hand = Maximálna veľkosť ruky: { $cards } kariet

# Option change announcements
ageofheroes-option-changed-victory-cities = Víťazstvo vyžaduje { $cities } miest.
ageofheroes-option-changed-victory-monument = Hranica dokončenia pamätníka nastavená na { $progress }%.
ageofheroes-option-changed-neighbor-roads = Cesty len k susedom { $enabled }.
ageofheroes-option-changed-max-hand = Maximálna veľkosť ruky nastavená na { $cards } kariet.

# Setup phase
ageofheroes-setup-start = Si vodcom kmeňa { $tribe }. Tvoj špeciálny zdroj pre pamätník je { $special }. Hoď kockami na určenie poradia ťahov.
ageofheroes-setup-viewer = Hráči hádžu kockami na určenie poradia ťahov.
ageofheroes-roll-dice = Hoď kockami
ageofheroes-war-roll-dice = Hoď kockami
ageofheroes-dice-result = Hodil si { $total } ({ $die1 } + { $die2 }).
ageofheroes-dice-result-other = { $player } hodil { $total }.
ageofheroes-dice-tie = Viacerí hráči hodili { $total }. Hádzame znova...
ageofheroes-first-player = { $player } hodil najviac s { $total } a začína prvý.
ageofheroes-first-player-you = S { $total } bodmi začínaš ty.

# Preparation phase
ageofheroes-prepare-start = Hráči musia zahrať karty udalostí a zhodiť katastrofy.
ageofheroes-prepare-your-turn = Máš { $count } { $count ->
    [one] kartu
    [few] karty
    [many] karty
    *[other] kariet
} na zahranie alebo zhodenie.
ageofheroes-prepare-done = Fáza prípravy dokončená.

# Events played/discarded
ageofheroes-population-growth = { $player } hrá Rast populácie a stavia nové mesto.
ageofheroes-population-growth-you = Ty hráš Rast populácie a staviaš nové mesto.
ageofheroes-discard-card = { $player } zhadzuje { $card }.
ageofheroes-discard-card-you = Ty zhadzuješ { $card }.
ageofheroes-earthquake = Zemetrasenie zasiahlo kmeň { $player }; jeho armády idú na zotavenie.
ageofheroes-earthquake-you = Zemetrasenie zasiahlo tvoj kmeň; tvoje armády idú na zotavenie.
ageofheroes-eruption = Erupcia ničí jedno z miest { $player }.
ageofheroes-eruption-you = Erupcia ničí jedno z tvojich miest.

# Disaster effects
ageofheroes-hunger-strikes = Hlad udiera.
ageofheroes-lose-card-hunger = Strácaš { $card }.
ageofheroes-barbarians-pillage = Barbari útočia na zdroje { $player }.
ageofheroes-barbarians-attack = Barbari útočia na zdroje { $player }.
ageofheroes-barbarians-attack-you = Barbari útočia na tvoje zdroje.
ageofheroes-lose-card-barbarians = Strácaš { $card }.
ageofheroes-block-with-card = { $player } blokuje katastrofu použitím { $card }.
ageofheroes-block-with-card-you = Ty blokuješ katastrofu použitím { $card }.

# Targeted disaster cards (Earthquake/Eruption)
ageofheroes-select-disaster-target = Vyber cieľ pre { $card }.
ageofheroes-no-targets = Žiadne platné ciele k dispozícii.
ageofheroes-earthquake-strikes-you = { $attacker } hrá Zemetrasenie proti tebe. Tvoje armády sú vypnuté.
ageofheroes-earthquake-strikes = { $attacker } hrá Zemetrasenie proti { $player }.
ageofheroes-armies-disabled = { $count } { $count ->
    [one] armáda je vypnutá
    [few] armády sú vypnuté
    [many] armády je vypnutých
    *[other] armád je vypnutých
} na jeden ťah.
ageofheroes-eruption-strikes-you = { $attacker } hrá Erupciu proti tebe. Jedno z tvojich miest je zničené.
ageofheroes-eruption-strikes = { $attacker } hrá Erupciu proti { $player }.
ageofheroes-city-destroyed = Mesto je zničené erupciou.

# Fair phase
ageofheroes-fair-start = Svitá na trhovisku.
ageofheroes-fair-draw-base = Ťaháš { $count } { $count ->
    [one] kartu
    [few] karty
    [many] karty
    *[other] kariet
}.
ageofheroes-fair-draw-roads = Ťaháš { $count } { $count ->
    [one] dodatočnú kartu
    [few] dodatočné karty
    [many] dodatočnej karty
    *[other] dodatočných kariet
} vďaka tvojej cestnej sieti.
ageofheroes-fair-draw-other = { $player } ťahá { $count } { $count ->
    [one] kartu
    [few] karty
    [many] karty
    *[other] kariet
}.

# Trading/Auction
ageofheroes-auction-start = Aukcia začína.
ageofheroes-offer-trade = Ponúknuť výmenu
ageofheroes-offer-made = { $player } ponúka { $card } za { $wanted }.
ageofheroes-offer-made-you = Ty ponúkaš { $card } za { $wanted }.
ageofheroes-trade-accepted = { $player } prijíma ponuku { $other } a vymieňa { $give } za { $receive }.
ageofheroes-trade-accepted-you = Ty prijímaš ponuku { $other } a dostávaš { $receive }.
ageofheroes-trade-cancelled = { $player } sťahuje svoju ponuku na { $card }.
ageofheroes-trade-cancelled-you = Ty sťahuješ svoju ponuku na { $card }.
ageofheroes-stop-trading = Prestať obchodovať
ageofheroes-select-request = Ponúkaš { $card }. Čo chceš na oplátku?
ageofheroes-cancel = Zrušiť
ageofheroes-left-auction = { $player } odchádza.
ageofheroes-left-auction-you = Ty odchádzaš z trhoviska.
ageofheroes-any-card = Akákoľvek karta
ageofheroes-cannot-trade-own-special = Nemôžeš vymeniť svoj vlastný špeciálny zdroj pre pamätník.
ageofheroes-resource-not-in-game = Tento špeciálny zdroj sa nepoužíva v tejto hre.

# Main play phase
ageofheroes-play-start = Fáza hry.
ageofheroes-day = Deň { $day }
ageofheroes-draw-card = { $player } ťahá kartu z balíčka.
ageofheroes-draw-card-you = Ty ťaháš { $card } z balíčka.
ageofheroes-your-action = Čo chceš urobiť?

# Tax Collection
ageofheroes-tax-collection = { $player } si vyberá Výber daní: { $cities } { $cities ->
    [one] mesto
    [few] mestá
    [many] mesta
    *[other] miest
} vyberie { $cards } { $cards ->
    [one] kartu
    [few] karty
    [many] karty
    *[other] kariet
}.
ageofheroes-tax-collection-you = Ty si vyberáš Výber daní: { $cities } { $cities ->
    [one] mesto
    [few] mestá
    [many] mesta
    *[other] miest
} vyberie { $cards } { $cards ->
    [one] kartu
    [few] karty
    [many] karty
    *[other] kariet
}.
ageofheroes-tax-no-city = Výber daní: Nemáš žiadne zachované mestá. Zhoď kartu, aby si ťahol novú.
ageofheroes-tax-no-city-done = { $player } si vyberá Výber daní, ale nemá mestá, takže vymieňa kartu.
ageofheroes-tax-no-city-done-you = Výber daní: Vymenil si { $card } za novú kartu.

# Construction
ageofheroes-construction-menu = Čo chceš postaviť?
ageofheroes-construction-done = { $player } postavil { $article } { $building }.
ageofheroes-construction-done-you = Ty si postavil { $article } { $building }.
ageofheroes-construction-stop = Prestať stavať
ageofheroes-construction-stopped = Rozhodol si sa prestať stavať.
ageofheroes-road-select-neighbor = Vyber, ku ktorému susedovi chceš postaviť cestu.
ageofheroes-direction-left = Naľavo od teba
ageofheroes-direction-right = Napravo od teba
ageofheroes-road-request-sent = Žiadosť o cestu odoslaná. Čakáme na schválenie suseda.
ageofheroes-road-request-received = { $requester } žiada povolenie postaviť cestu k tvojmu kmeňu.
ageofheroes-road-request-denied-you = Ty si odmietol žiadosť o cestu.
ageofheroes-road-request-denied = { $denier } odmietol tvoju žiadosť o cestu.
ageofheroes-road-built = { $tribe1 } a { $tribe2 } sú teraz spojené cestou.
ageofheroes-road-no-target = Žiadne susedné kmene dostupné na stavbu cesty.
ageofheroes-approve = Schváliť
ageofheroes-deny = Odmietnuť
ageofheroes-supply-exhausted = Už nie je viac { $building } na stavbu.

# Do Nothing
ageofheroes-do-nothing = { $player } pasuje.
ageofheroes-do-nothing-you = Ty pasuješ...

# War
ageofheroes-war-declare = { $attacker } vyhlasuje vojnu { $defender }. Cieľ: { $goal }.
ageofheroes-war-prepare = Vyber svoje armády pre { $action }.
ageofheroes-war-no-army = Nemáš žiadne armády alebo karty hrdinov k dispozícii.
ageofheroes-war-no-targets = Žiadne platné ciele pre vojnu.
ageofheroes-war-no-valid-goal = Žiadne platné vojnové ciele proti tomuto cieľu.
ageofheroes-war-select-target = Vyber, ktorého hráča chceš zaútočiť.
ageofheroes-war-select-goal = Vyber svoj vojnový cieľ.
ageofheroes-war-prepare-attack = Vyber svoje útočné sily.
ageofheroes-war-prepare-defense = { $attacker } ťa napáda; Vyber svoje obranné sily.
ageofheroes-war-select-armies = Vyber armády: { $count }
ageofheroes-war-select-generals = Vyber generálov: { $count }
ageofheroes-war-select-heroes = Vyber hrdinov: { $count }
ageofheroes-war-attack = Zaútočiť...
ageofheroes-war-defend = Brániť...
ageofheroes-war-prepared = Tvoje sily: { $armies } { $armies ->
    [one] armáda
    [few] armády
    [many] armády
    *[other] armád
}{ $generals ->
    [0] {""}
    [one] {" a 1 generál"}
    [few] {" a { $generals } generáli"}
    [many] {" a { $generals } generála"}
    *[other] {" a { $generals } generálov"}
}{ $heroes ->
    [0] {""}
    [one] {" a 1 hrdina"}
    [few] {" a { $heroes } hrdinovia"}
    [many] {" a { $heroes } hrdinu"}
    *[other] {" a { $heroes } hrdinov"}
}.
ageofheroes-war-roll-you = Ty hádžeš { $roll }.
ageofheroes-war-roll-other = { $player } hádže { $roll }.
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"+1 z pevnosti = { $total } celkom"}
            [few] {"+{ $fortress } z pevností = { $total } celkom"}
            [many] {"+{ $fortress } z pevností = { $total } celkom"}
            *[other] {"+{ $fortress } z pevností = { $total } celkom"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"+{ $general } z generála = { $total } celkom"}
            [one] {"+{ $general } z generála, +1 z pevnosti = { $total } celkom"}
            [few] {"+{ $general } z generála, +{ $fortress } z pevností = { $total } celkom"}
            [many] {"+{ $general } z generála, +{ $fortress } z pevností = { $total } celkom"}
            *[other] {"+{ $general } z generála, +{ $fortress } z pevností = { $total } celkom"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"{ $player }: +1 z pevnosti = { $total } celkom"}
            [few] {"{ $player }: +{ $fortress } z pevností = { $total } celkom"}
            [many] {"{ $player }: +{ $fortress } z pevností = { $total } celkom"}
            *[other] {"{ $player }: +{ $fortress } z pevností = { $total } celkom"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } z generála = { $total } celkom"}
            [one] {"{ $player }: +{ $general } z generála, +1 z pevnosti = { $total } celkom"}
            [few] {"{ $player }: +{ $general } z generála, +{ $fortress } z pevností = { $total } celkom"}
            [many] {"{ $player }: +{ $general } z generála, +{ $fortress } z pevností = { $total } celkom"}
            *[other] {"{ $player }: +{ $general } z generála, +{ $fortress } z pevností = { $total } celkom"}
        }
    }
}

# Battle
ageofheroes-battle-start = Bitka začína. { $attacker } má { $att_armies } { $att_armies ->
    [one] armádu
    [few] armády
    [many] armády
    *[other] armád
} proti { $defender } s { $def_armies } { $def_armies ->
    [one] armádou
    [few] armádami
    [many] armádami
    *[other] armádami
}.
ageofheroes-dice-roll-detailed = { $name } hádže { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } z generála" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 z pevnosti" }
    [few] { " + { $fortress } z pevností" }
    [many] { " + { $fortress } z pevností" }
    *[other] { " + { $fortress } z pevností" }
} = { $total }.
ageofheroes-dice-roll-detailed-you = Ty hádžeš { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } z generála" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 z pevnosti" }
    [few] { " + { $fortress } z pevností" }
    [many] { " + { $fortress } z pevností" }
    *[other] { " + { $fortress } z pevností" }
} = { $total }.
ageofheroes-round-attacker-wins = { $attacker } vyhráva kolo ({ $att_total } proti { $def_total }). { $defender } stráca armádu.
ageofheroes-round-defender-wins = { $defender } sa úspešne bráni ({ $def_total } proti { $att_total }). { $attacker } stráca armádu.
ageofheroes-round-draw = Obe strany majú { $total }. Žiadne straty armád.
ageofheroes-battle-victory-attacker = { $attacker } porazil { $defender }.
ageofheroes-battle-victory-defender = { $defender } sa úspešne bráni proti { $attacker }.
ageofheroes-battle-mutual-defeat = { $attacker } aj { $defender } strácajú všetky armády.
ageofheroes-general-bonus = +{ $count } z { $count ->
    [one] generála
    [few] generálov
    [many] generála
    *[other] generálov
}
ageofheroes-fortress-bonus = +{ $count } z obrany pevnosti
ageofheroes-battle-winner = { $winner } vyhráva bitku.
ageofheroes-battle-draw = Bitka sa končí remízou...
ageofheroes-battle-continue = Pokračovať v bitke.
ageofheroes-battle-end = Bitka je u konca.

# War outcomes
ageofheroes-conquest-success = { $attacker } dobýja { $count } { $count ->
    [one] mesto
    [few] mestá
    [many] mesta
    *[other] miest
} od { $defender }.
ageofheroes-plunder-success = { $attacker } pliení { $count } { $count ->
    [one] kartu
    [few] karty
    [many] karty
    *[other] kariet
} od { $defender }.
ageofheroes-destruction-success = { $attacker } ničí { $count } { $count ->
    [one] zdroj
    [few] zdroje
    [many] zdroja
    *[other] zdrojov
} pamätníka { $defender }.
ageofheroes-army-losses = { $player } stráca { $count } { $count ->
    [one] armádu
    [few] armády
    [many] armády
    *[other] armád
}.
ageofheroes-army-losses-you = Ty strácaš { $count } { $count ->
    [one] armádu
    [few] armády
    [many] armády
    *[other] armád
}.

# Army return
ageofheroes-army-return-road = Tvoje jednotky sa okamžite vrátia po ceste.
ageofheroes-army-return-delayed = { $count } { $count ->
    [one] jednotka sa vracia
    [few] jednotky sa vracajú
    [many] jednotky sa vracia
    *[other] jednotiek sa vracia
} na konci tvojho ďalšieho ťahu.
ageofheroes-army-returned = Jednotky { $player } sa vrátili z vojny.
ageofheroes-army-returned-you = Tvoje jednotky sa vrátili z vojny.
ageofheroes-army-recover = Armády { $player } sa zotavujú zo zemetrasenia.
ageofheroes-army-recover-you = Tvoje armády sa zotavujú zo zemetrasenia.

# Olympics
ageofheroes-olympics-cancel = { $player } hrá Olympijské hry. Vojna zrušená.
ageofheroes-olympics-prompt = { $attacker } vyhlásil vojnu. Máš Olympijské hry - použiť ich na zrušenie?
ageofheroes-yes = Áno
ageofheroes-no = Nie

# Monument progress
ageofheroes-monument-progress = Pamätník { $player } je { $count }/5 hotový.
ageofheroes-monument-progress-you = Tvoj pamätník je { $count }/5 hotový.

# Hand management
ageofheroes-discard-excess = Máš viac ako { $max } kariet. Zhoď { $count } { $count ->
    [one] kartu
    [few] karty
    [many] karty
    *[other] kariet
}.
ageofheroes-discard-excess-other = { $player } musí zhodiť prebytočné karty.
ageofheroes-discard-more = Zhoď ešte { $count } { $count ->
    [one] kartu
    [few] karty
    [many] karty
    *[other] kariet
}.

# Victory
ageofheroes-victory-cities = { $player } postavil 5 miest! Ríša piatich miest.
ageofheroes-victory-cities-you = Ty si postavil 5 miest! Ríša piatich miest.
ageofheroes-victory-monument = { $player } dokončil svoj pamätník! Nositeľ veľkej kultúry.
ageofheroes-victory-monument-you = Ty si dokončil svoj pamätník! Nositeľ veľkej kultúry.
ageofheroes-victory-last-standing = { $player } je posledný pozostávajúci kmeň! Najvytrvalejší.
ageofheroes-victory-last-standing-you = Ty si posledný pozostávajúci kmeň! Najvytrvalejší.
ageofheroes-game-over = Koniec hry.

# Elimination
ageofheroes-eliminated = { $player } bol eliminovaný.
ageofheroes-eliminated-you = Ty si bol eliminovaný.

# Hand
ageofheroes-hand-empty = Nemáš žiadne karty.
ageofheroes-hand-contents = Tvoja ruka ({ $count } { $count ->
    [one] karta
    [few] karty
    [many] karty
    *[other] kariet
}): { $cards }

# Status
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [one] mesto
    [few] mestá
    [many] mesta
    *[other] miest
}, { $armies } { $armies ->
    [one] armáda
    [few] armády
    [many] armády
    *[other] armád
}, { $monument }/5 pamätník
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = Mestá: { $count }
ageofheroes-status-armies = Armády: { $count }
ageofheroes-status-generals = Generáli: { $count }
ageofheroes-status-fortresses = Pevnosti: { $count }
ageofheroes-status-monument = Pamätník: { $count }/5
ageofheroes-status-roads = Cesty: { $left }{ $right }
ageofheroes-status-road-left = vľavo
ageofheroes-status-road-right = vpravo
ageofheroes-status-none = žiadne
ageofheroes-status-earthquake-armies = Zotavujúce sa armády: { $count }
ageofheroes-status-returning-armies = Vracajúce sa armády: { $count }
ageofheroes-status-returning-generals = Vracajúci sa generáli: { $count }

# Deck info
ageofheroes-deck-empty = Už nie sú žiadne karty { $card } v balíčku.
ageofheroes-deck-count = Zostávajúce karty: { $count }
ageofheroes-deck-reshuffled = Hromada odhodeých kariet bola zamiešaná späť do balíčka.

# Give up
ageofheroes-give-up-confirm = Si si istý, že chceš vzdať?
ageofheroes-gave-up = { $player } sa vzdal!
ageofheroes-gave-up-you = Ty si sa vzdal!

# Hero card
ageofheroes-hero-use = Použiť ako armádu alebo generála?
ageofheroes-hero-army = Armáda
ageofheroes-hero-general = Generál

# Fortune card
ageofheroes-fortune-reroll = { $player } používa Šťastie na prehratie.
ageofheroes-fortune-prompt = Prehral si hod. Použiť Šťastie na prehratie?

# Disabled action reasons
ageofheroes-not-your-turn = Nie je tvoj ťah.
ageofheroes-game-not-started = Hra ešte nezačala.
ageofheroes-wrong-phase = Táto akcia nie je dostupná v aktuálnej fáze.
ageofheroes-no-resources = Nemáš potrebné zdroje.

# Building costs (for display)
ageofheroes-cost-army = 2 obilie, železo
ageofheroes-cost-fortress = Železo, drevo, kameň
ageofheroes-cost-general = Železo, zlato
ageofheroes-cost-road = 2 kamene
ageofheroes-cost-city = 2 drevo, kameň
