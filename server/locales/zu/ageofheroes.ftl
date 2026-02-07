# Age of Heroes game messages (isiZulu)
# Umdlalo wokwakha imihlaba yamasiko amadala emidlalo yamakhadi abadlali aba-2 kuya ku-6

# Game name
game-name-ageofheroes = Age of Heroes

# Tribes
ageofheroes-tribe-egyptians = AbaseGibithe
ageofheroes-tribe-romans = AbaseRoma
ageofheroes-tribe-greeks = AmaGriki
ageofheroes-tribe-babylonians = AmaBhabhiloni
ageofheroes-tribe-celts = AmaCelts
ageofheroes-tribe-chinese = AmaShayina

# Special Resources (for monuments)
ageofheroes-special-limestone = Itshe Lekalishi
ageofheroes-special-concrete = Ukhonkolo
ageofheroes-special-marble = Itshe Lemabula
ageofheroes-special-bricks = Izitini
ageofheroes-special-sandstone = Itshe Lesihlabathi
ageofheroes-special-granite = Igranayithi

# Standard Resources
ageofheroes-resource-iron = Insimbi
ageofheroes-resource-wood = Ukhuni
ageofheroes-resource-grain = Okusanhlamvu
ageofheroes-resource-stone = Itshe
ageofheroes-resource-gold = Igolide

# Events
ageofheroes-event-population-growth = Ukukhula Kwabantu
ageofheroes-event-earthquake = Ukuzamazama Komhlaba
ageofheroes-event-eruption = Ukuqhuma Kwentaba
ageofheroes-event-hunger = Indlala
ageofheroes-event-barbarians = AmaBarbarian
ageofheroes-event-olympics = Imidlalo Ye-Olympics
ageofheroes-event-hero = Iqhawe
ageofheroes-event-fortune = Inhlanhla

# Buildings
ageofheroes-building-army = Ibutho
ageofheroes-building-fortress = Inqaba
ageofheroes-building-general = Umenzi
ageofheroes-building-road = Umgwaqo
ageofheroes-building-city = Idolobha

# Actions
ageofheroes-action-tax-collection = Ukuqoqa Intela
ageofheroes-action-construction = Ukwakha
ageofheroes-action-war = Impi
ageofheroes-action-do-nothing = Ungenza Lutho
ageofheroes-play = Dlala

# War goals
ageofheroes-war-conquest = Ukunqoba
ageofheroes-war-plunder = Ukuphanga
ageofheroes-war-destruction = Ukubhujiswa

# Game options
ageofheroes-set-victory-cities = Amadolobha okunqoba: { $cities }
ageofheroes-enter-victory-cities = Faka inani lamadolobha okunqoba (3-7)
ageofheroes-set-victory-monument = Ukuqedwa kwesikhumbuzo: { $progress }%
ageofheroes-toggle-neighbor-roads = Imigwaqo kuphela kubomakhelwane: { $enabled }
ageofheroes-set-max-hand = Ubungako besandla: Amakhadi angu-{ $cards }

# Option change announcements
ageofheroes-option-changed-victory-cities = Ukunqoba kudinga amadolobha angu-{ $cities }.
ageofheroes-option-changed-victory-monument = Isilinganiso sokuqedwa kwesikhumbuzo sisetelwe ku-{ $progress }%.
ageofheroes-option-changed-neighbor-roads = Imigwaqo kuphela kubomakhelwane { $enabled }.
ageofheroes-option-changed-max-hand = Ubukhulu besandla busetelwe kumakhadi angu-{ $cards }.

# Setup phase
ageofheroes-setup-start = Wena ungumholi wamasiko { $tribe }. Okwakho okukhethekile kwesikhumbuzo ngu-{ $special }. Phonsa amadayisi ukuze unqume uhlelo lokushintshana.
ageofheroes-setup-viewer = Abadlali baphonsa amadayisi ukuze banqume uhlelo lokushintshana.
ageofheroes-roll-dice = Phonsa amadayisi
ageofheroes-war-roll-dice = Phonsa amadayisi
ageofheroes-dice-result = Uphonse { $total } ({ $die1 } + { $die2 }).
ageofheroes-dice-result-other = U-{ $player } uphonse { $total }.
ageofheroes-dice-tie = Abadlali abaningi bafanele ngo-{ $total }. Iyaphinda iphonsa...
ageofheroes-first-player = U-{ $player } uphonse okuphezulu ngo-{ $total } futhi udlala kuqala.
ageofheroes-first-player-you = Ngamaphuzu angu-{ $total }, wena udlala kuqala.

# Preparation phase
ageofheroes-prepare-start = Abadlali kufanele badlale amakhadi ezenzakalo futhi balahle izinhlekelele.
ageofheroes-prepare-your-turn = Unakhadi { $count } { $count ->
    [one] elikhadi
    *[other] amakhadi
} okudlala noma ukalahle.
ageofheroes-prepare-done = Isigaba sokulungiselela siphelile.

# Events played/discarded
ageofheroes-population-growth = U-{ $player } udlala Ukukhula Kwabantu futhi wakha idolobha elisha.
ageofheroes-population-growth-you = Wena udlala Ukukhula Kwabantu futhi wakha idolobha elisha.
ageofheroes-discard-card = U-{ $player } ukalahla { $card }.
ageofheroes-discard-card-you = Wena ukalahla { $card }.
ageofheroes-earthquake = Ukuzamazama komhlaba kushaya amasiko ka-{ $player }; amabutho akhe ayabuyela.
ageofheroes-earthquake-you = Ukuzamazama komhlaba kushaya amasiko akho; amabutho akho ayabuyela.
ageofheroes-eruption = Ukuqhuma kubhubhisa elinye lamadolobha ka-{ $player }.
ageofheroes-eruption-you = Ukuqhuma kubhubhisa elinye lamadolobha akho.

# Disaster effects
ageofheroes-hunger-strikes = Indlala iyashaya.
ageofheroes-lose-card-hunger = Ulahlekelwe { $card }.
ageofheroes-barbarians-pillage = AmaBarbarian ahlasela izimpahla zika-{ $player }.
ageofheroes-barbarians-attack = AmaBarbarian ahlasela izimpahla zika-{ $player }.
ageofheroes-barbarians-attack-you = AmaBarbarian ahlasela izimpahla zakho.
ageofheroes-lose-card-barbarians = Ulahlekelwe { $card }.
ageofheroes-block-with-card = U-{ $player } uvimbela inhlekelele esebenzisa { $card }.
ageofheroes-block-with-card-you = Wena uvimbela inhlekelele usebenzisa { $card }.

# Targeted disaster cards (Earthquake/Eruption)
ageofheroes-select-disaster-target = Khetha okuhlosiwe ku-{ $card }.
ageofheroes-no-targets = Akukho okuhlosiwe okutholakalayo.
ageofheroes-earthquake-strikes-you = U-{ $attacker } udlala Ukuzamazama Komhlaba ngawe. Amabutho akho ayavinjwa.
ageofheroes-earthquake-strikes = U-{ $attacker } udlala Ukuzamazama Komhlaba ngo-{ $player }.
ageofheroes-armies-disabled = { $count } { $count ->
    [one] ibutho
    *[other] amabutho
} { $count ->
    [one] livalwe
    *[other] avalwe
} ngokwesikhathi esisodwa.
ageofheroes-eruption-strikes-you = U-{ $attacker } udlala Ukuqhuma ngawe. Elinye lamadolobha akho liyabhubhiswa.
ageofheroes-eruption-strikes = U-{ $attacker } udlala Ukuqhuma ngo-{ $player }.
ageofheroes-city-destroyed = Idolobha liyabhubhiswa ukuqhuma.

# Fair phase
ageofheroes-fair-start = Ilanga liyaphuma emakethe.
ageofheroes-fair-draw-base = Udonsa { $count } { $count ->
    [one] ikhadi
    *[other] amakhadi
}.
ageofheroes-fair-draw-roads = Udonsa { $count } { $count ->
    [one] ikhadi
    *[other] amakhadi
} elengeziwe ngenxa yemigwaqo yakho.
ageofheroes-fair-draw-other = U-{ $player } udonsa { $count } { $count ->
    [one] ikhadi
    *[other] amakhadi
}.

# Trading/Auction
ageofheroes-auction-start = Inkundla iyaqala.
ageofheroes-offer-trade = Nikela ukushintshanisa
ageofheroes-offer-made = U-{ $player } unikela { $card } nge-{ $wanted }.
ageofheroes-offer-made-you = Wena unikela { $card } nge-{ $wanted }.
ageofheroes-trade-accepted = U-{ $player } uyamukela isipho sika-{ $other } futhi ushintshanisa { $give } nge-{ $receive }.
ageofheroes-trade-accepted-you = Wena uyamukela isipho sika-{ $other } futhi uthola { $receive }.
ageofheroes-trade-cancelled = U-{ $player } uyabuyisa isipho sakhe se-{ $card }.
ageofheroes-trade-cancelled-you = Wena ubuyisa isipho sakho se-{ $card }.
ageofheroes-stop-trading = Yima Ukushintshanisa
ageofheroes-select-request = Unikela { $card }. Ufuna ukuphi?
ageofheroes-cancel = Khansela
ageofheroes-left-auction = U-{ $player } uyahamba.
ageofheroes-left-auction-you = Wena uyahamba emakethe.
ageofheroes-any-card = Noma yiliphi ikhadi
ageofheroes-cannot-trade-own-special = Awukwazi ukushintshanisa okwakho okukhethekile kwesikhumbuzo.
ageofheroes-resource-not-in-game = Lesi sifunda esikhethekile asisasebenzi kulesi mdlalo.

# Main play phase
ageofheroes-play-start = Isigaba sokudlala.
ageofheroes-day = Usuku { $day }
ageofheroes-draw-card = U-{ $player } udonsa ikhadi esigangeni.
ageofheroes-draw-card-you = Wena udonsa { $card } esigangeni.
ageofheroes-your-action = Ufuna ukwenzani?

# Tax Collection
ageofheroes-tax-collection = U-{ $player } ukhetha Ukuqoqa Intela: { $cities } { $cities ->
    [one] idolobha
    *[other] amadolobha
} liqoqa { $cards } { $cards ->
    [one] ikhadi
    *[other] amakhadi
}.
ageofheroes-tax-collection-you = Wena ukhetha Ukuqoqa Intela: { $cities } { $cities ->
    [one] idolobha
    *[other] amadolobha
} liqoqa { $cards } { $cards ->
    [one] ikhadi
    *[other] amakhadi
}.
ageofheroes-tax-no-city = Ukuqoqa Intela: Awunayo amadolobha asaphilayo. Lahla ikhadi ukuze udonse elisha.
ageofheroes-tax-no-city-done = U-{ $player } ukhetha Ukuqoqa Intela kodwa anayo amadolobha, ngakho bashintshanisa ikhadi.
ageofheroes-tax-no-city-done-you = Ukuqoqa Intela: Ushintshanise { $card } ngekhadi elisha.

# Construction
ageofheroes-construction-menu = Ufuna ukwakhani?
ageofheroes-construction-done = U-{ $player } wakhe { $article } { $building }.
ageofheroes-construction-done-you = Wena wakhe { $article } { $building }.
ageofheroes-construction-stop = Yima ukwakha
ageofheroes-construction-stopped = Unqume ukuyeka ukwakha.
ageofheroes-road-select-neighbor = Khetha omakhelwane omele wakhe umgwaqo kuye.
ageofheroes-direction-left = Ngakwesokunxele kwakho
ageofheroes-direction-right = Ngakwesokunene kwakho
ageofheroes-road-request-sent = Isicelo somgwaqo sithunyelwe. Kulinde imvumo yomakhelwane.
ageofheroes-road-request-received = U-{ $requester } ucela imvumo yokwakha umgwaqo kumasiko akho.
ageofheroes-road-request-denied-you = Wena unqabile isicelo somgwaqo.
ageofheroes-road-request-denied = U-{ $denier } unqabile isicelo sakho somgwaqo.
ageofheroes-road-built = { $tribe1 } no-{ $tribe2 } manje baxhunywe ngomgwaqo.
ageofheroes-road-no-target = Akukho masiko angomakhelwane atholakalayo wokwakha umgwaqo.
ageofheroes-approve = Vumela
ageofheroes-deny = Nqaba
ageofheroes-supply-exhausted = Akusekho { $building } etholakalayo yokwakha.

# Do Nothing
ageofheroes-do-nothing = U-{ $player } uyadlula.
ageofheroes-do-nothing-you = Wena uyadlula...

# War
ageofheroes-war-declare = U-{ $attacker } umemezela impi ngo-{ $defender }. Injongo: { $goal }.
ageofheroes-war-prepare = Khetha amabutho akho { $action }.
ageofheroes-war-no-army = Awunayo amabutho noma amakhadi eqhawe atholakalayo.
ageofheroes-war-no-targets = Akukho okuhlosiwe okufanelekile kwempi.
ageofheroes-war-no-valid-goal = Akukho njongo yempi efanelekile kulokhu okuhlosiwe.
ageofheroes-war-select-target = Khetha umdlali ozomhlasela.
ageofheroes-war-select-goal = Khetha injongo yakho yempi.
ageofheroes-war-prepare-attack = Khetha amabutho akho okuphikisana.
ageofheroes-war-prepare-defense = U-{ $attacker } uyakuhlasela; Khetha amabutho akho okuzivikela.
ageofheroes-war-select-armies = Khetha amabutho: { $count }
ageofheroes-war-select-generals = Khetha abenzi: { $count }
ageofheroes-war-select-heroes = Khetha amaqhawe: { $count }
ageofheroes-war-attack = Hlasela...
ageofheroes-war-defend = Zivikele...
ageofheroes-war-prepared = Amabutho akho: { $armies } { $armies ->
    [one] ibutho
    *[other] amabutho
}{ $generals ->
    [0] {""}
    [one] {" kanye no-1 umenzi"}
    *[other] {" kanye nabenzi abangu-{ $generals }"}
}{ $heroes ->
    [0] {""}
    [one] {" kanye neqhawe eli-1"}
    *[other] {" kanye namaqhawe angu-{ $heroes }"}
}.
ageofheroes-war-roll-you = Wena uphonsa { $roll }.
ageofheroes-war-roll-other = U-{ $player } uphonsa { $roll }.
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [1] {"+1 kusuka enqabeni = isamba esingu-{ $total }"}
            *[other] {"+{ $fortress } kusuka ezinqabeni = isamba esingu-{ $total }"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"+{ $general } kusuka kumenzi = isamba esingu-{ $total }"}
            [1] {"+{ $general } kusuka kumenzi, +1 kusuka enqabeni = isamba esingu-{ $total }"}
            *[other] {"+{ $general } kusuka kumenzi, +{ $fortress } kusuka ezinqabeni = isamba esingu-{ $total }"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [1] {"{ $player }: +1 kusuka enqabeni = isamba esingu-{ $total }"}
            *[other] {"{ $player }: +{ $fortress } kusuka ezinqabeni = isamba esingu-{ $total }"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } kusuka kumenzi = isamba esingu-{ $total }"}
            [1] {"{ $player }: +{ $general } kusuka kumenzi, +1 kusuka enqabeni = isamba esingu-{ $total }"}
            *[other] {"{ $player }: +{ $general } kusuka kumenzi, +{ $fortress } kusuka ezinqabeni = isamba esingu-{ $total }"}
        }
    }
}

# Battle
ageofheroes-battle-start = Impi iyaqala. { $attacker } ina-{ $att_armies } { $att_armies ->
    [one] ibutho
    *[other] amabutho
} ngokumelene no-{ $defender } ona-{ $def_armies } { $def_armies ->
    [one] ibutho
    *[other] amabutho
}.
ageofheroes-dice-roll-detailed = U-{ $name } uphonsa { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } kusuka kumenzi" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 kusuka enqabeni" }
    *[other] { " + { $fortress } kusuka ezinqabeni" }
} = { $total }.
ageofheroes-dice-roll-detailed-you = Wena uphonsa { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } kusuka kumenzi" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 kusuka enqabeni" }
    *[other] { " + { $fortress } kusuka ezinqabeni" }
} = { $total }.
ageofheroes-round-attacker-wins = U-{ $attacker } uwina umjikelezo ({ $att_total } ngokumelene no-{ $def_total }). U-{ $defender } ulahlekelwe ibutho.
ageofheroes-round-defender-wins = U-{ $defender } uyazivikela ngempumelelo ({ $def_total } ngokumelene no-{ $att_total }). U-{ $attacker } ulahlekelwe ibutho.
ageofheroes-round-draw = Zombili izinhlangothi ziyafanana ngo-{ $total }. Awekho amabutho alahlekile.
ageofheroes-battle-victory-attacker = U-{ $attacker } uyehlula u-{ $defender }.
ageofheroes-battle-victory-defender = U-{ $defender } uyazivikela ngempumelelo kuhlaselo luka-{ $attacker }.
ageofheroes-battle-mutual-defeat = Bobabili u-{ $attacker } no-{ $defender } balahlekelwe onke amabutho.
ageofheroes-general-bonus = +{ $count } kusuka ku-{ $count ->
    [one] umenzi
    *[other] abenzi
}
ageofheroes-fortress-bonus = +{ $count } kusuka ekuvikeleni kwenqaba
ageofheroes-battle-winner = U-{ $winner } uwina impi.
ageofheroes-battle-draw = Impi iphela ngokufanana...
ageofheroes-battle-continue = Qhubeka nempi.
ageofheroes-battle-end = Impi iphelile.

# War outcomes
ageofheroes-conquest-success = U-{ $attacker } unqoba { $count } { $count ->
    [one] idolobha
    *[other] amadolobha
} kusuka ku-{ $defender }.
ageofheroes-plunder-success = U-{ $attacker } uphanga { $count } { $count ->
    [one] ikhadi
    *[other] amakhadi
} kusuka ku-{ $defender }.
ageofheroes-destruction-success = U-{ $attacker } ubhubhisa { $count } { $count ->
    [one] isifunda
    *[other] izifunda
} zesikhumbuzo sika-{ $defender }.
ageofheroes-army-losses = U-{ $player } ulahlekelwa { $count } { $count ->
    [one] ibutho
    *[other] amabutho
}.
ageofheroes-army-losses-you = Wena ulahlekelwe { $count } { $count ->
    [one] ibutho
    *[other] amabutho
}.

# Army return
ageofheroes-army-return-road = Amabutho akho ayabuya ngokushesha ngomgwaqo.
ageofheroes-army-return-delayed = { $count } { $count ->
    [one] isoldati liyabuya
    *[other] amasoldate ayabuya
} ekupheleni kokushintshana kwakho okulandelayo.
ageofheroes-army-returned = Amabutho ka-{ $player } asebuyile empini.
ageofheroes-army-returned-you = Amabutho akho asebuyile empini.
ageofheroes-army-recover = Amabutho ka-{ $player } ayabulawa ukuzamazama komhlaba.
ageofheroes-army-recover-you = Amabutho akho ayabulawa ukuzamazama komhlaba.

# Olympics
ageofheroes-olympics-cancel = U-{ $player } udlala Imidlalo Ye-Olympics. Impi iyakhansela.
ageofheroes-olympics-prompt = U-{ $attacker } umemezele impi. Unayo i-Olympics - uyisebenzisa ukukhansela?
ageofheroes-yes = Yebo
ageofheroes-no = Cha

# Monument progress
ageofheroes-monument-progress = Isikhumbuzo sika-{ $player } singu-{ $count }/5 siqedile.
ageofheroes-monument-progress-you = Isikhumbuzo sakho singu-{ $count }/5 siqedile.

# Hand management
ageofheroes-discard-excess = Unamakhadi angaphezu kuka-{ $max }. Lahla { $count } { $count ->
    [one] ikhadi
    *[other] amakhadi
}.
ageofheroes-discard-excess-other = U-{ $player } kufanele alahle amakhadi angaphezu.
ageofheroes-discard-more = Lahla { $count } { $count ->
    [one] elinye ikhadi
    *[other] amanye amakhadi
}.

# Victory
ageofheroes-victory-cities = U-{ $player } wakhe amadolobha ama-5! Umbuso Wamadolobha Amahlanu.
ageofheroes-victory-cities-you = Wena wakhe amadolobha ama-5! Umbuso Wamadolobha Amahlanu.
ageofheroes-victory-monument = U-{ $player } uqedile isikhumbuzo sakhe! Abaphathi Bamasiko Amakhulu.
ageofheroes-victory-monument-you = Wena uqedile isikhumbuzo sakho! Abaphathi Bamasiko Amakhulu.
ageofheroes-victory-last-standing = U-{ $player } yisiko sokugcina esimile! Abaqhubekayo.
ageofheroes-victory-last-standing-you = Wena uyisiko sokugcina esimile! Abaqhubekayo.
ageofheroes-game-over = Umdlalo Uphelile.

# Elimination
ageofheroes-eliminated = U-{ $player } ukhishiwe.
ageofheroes-eliminated-you = Wena ukhishiwe.

# Hand
ageofheroes-hand-empty = Awunayo amakhadi.
ageofheroes-hand-contents = Isandla sakho ({ $count } { $count ->
    [one] ikhadi
    *[other] amakhadi
}): { $cards }

# Status
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [one] idolobha
    *[other] amadolobha
}, { $armies } { $armies ->
    [one] ibutho
    *[other] amabutho
}, { $monument }/5 isikhumbuzo
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = Amadolobha: { $count }
ageofheroes-status-armies = Amabutho: { $count }
ageofheroes-status-generals = Abenzi: { $count }
ageofheroes-status-fortresses = Izinqaba: { $count }
ageofheroes-status-monument = Isikhumbuzo: { $count }/5
ageofheroes-status-roads = Imigwaqo: { $left }{ $right }
ageofheroes-status-road-left = kwesokunxele
ageofheroes-status-road-right = kwesokudla
ageofheroes-status-none = lutho
ageofheroes-status-earthquake-armies = Amabutho abuyako: { $count }
ageofheroes-status-returning-armies = Amabutho abuyako: { $count }
ageofheroes-status-returning-generals = Abenzi ababuyako: { $count }

# Deck info
ageofheroes-deck-empty = Akusekho { $card } amakhadi esigangeni.
ageofheroes-deck-count = Amakhadi asele: { $count }
ageofheroes-deck-reshuffled = Inqwaba yokulahlwa isixutshwe isigange.

# Give up
ageofheroes-give-up-confirm = Uqinisekile ukuthi ufuna ukunikela?
ageofheroes-gave-up = U-{ $player } unikele!
ageofheroes-gave-up-you = Wena unikele!

# Hero card
ageofheroes-hero-use = Sebenzisa njengebutho noma umenzi?
ageofheroes-hero-army = Ibutho
ageofheroes-hero-general = Umenzi

# Fortune card
ageofheroes-fortune-reroll = U-{ $player } usebenzisa Inhlanhla ukuze aphonse futhi.
ageofheroes-fortune-prompt = Ulahlekelwe ukuphonsa. Sebenzisa Inhlanhla ukuphonsa futhi?

# Disabled action reasons
ageofheroes-not-your-turn = Akusikho isikhathi sakho.
ageofheroes-game-not-started = Umdlalo awukaqali.
ageofheroes-wrong-phase = Lesi senzo asitholakali kulesi sigaba samanje.
ageofheroes-no-resources = Awunayo izimpahla ezidingekayo.

# Building costs (for display)
ageofheroes-cost-army = Okusanhlamvu okungu-2, Insimbi
ageofheroes-cost-fortress = Insimbi, Ukhuni, Itshe
ageofheroes-cost-general = Insimbi, Igolide
ageofheroes-cost-road = Amatshe ama-2
ageofheroes-cost-city = Ukhuni olungu-2, Itshe
