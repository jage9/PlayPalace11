# Age of Heroes game messages
# A civilization-building card game for 2-6 players

# Game name
game-name-ageofheroes = Hősök kora

# Tribes
ageofheroes-tribe-egyptians = Egyiptomiak
ageofheroes-tribe-romans = Rómaiak
ageofheroes-tribe-greeks = Görögök
ageofheroes-tribe-babylonians = Babilóniaiak
ageofheroes-tribe-celts = Kelták
ageofheroes-tribe-chinese = Kínaiak

# Special Resources (for monuments)
ageofheroes-special-limestone = Mészkő
ageofheroes-special-concrete = Beton
ageofheroes-special-marble = Márvány
ageofheroes-special-bricks = Téglák
ageofheroes-special-sandstone = Homokkő
ageofheroes-special-granite = Gránit

# Standard Resources
ageofheroes-resource-iron = Vas
ageofheroes-resource-wood = Fa
ageofheroes-resource-grain = Gabona
ageofheroes-resource-stone = Kő
ageofheroes-resource-gold = Arany

# Events
ageofheroes-event-population-growth = Népességnövekedés
ageofheroes-event-earthquake = Földrengés
ageofheroes-event-eruption = Kitörés
ageofheroes-event-hunger = Éhínség
ageofheroes-event-barbarians = Barbárok
ageofheroes-event-olympics = Olimpiai játékok
ageofheroes-event-hero = Hős
ageofheroes-event-fortune = Szerencse

# Buildings
ageofheroes-building-army = Hadsereg
ageofheroes-building-fortress = Erőd
ageofheroes-building-general = Tábornok
ageofheroes-building-road = Út
ageofheroes-building-city = Város

# Actions
ageofheroes-action-tax-collection = Adószedés
ageofheroes-action-construction = Építkezés
ageofheroes-action-war = Háború
ageofheroes-action-do-nothing = Nem tesz semmit
ageofheroes-play = Játssz

# War goals
ageofheroes-war-conquest = Hódítás
ageofheroes-war-plunder = Fosztogatás
ageofheroes-war-destruction = Pusztítás

# Game options
ageofheroes-set-victory-cities = Győzelmi városok: { $cities }
ageofheroes-enter-victory-cities = Add meg a győzelemhez szükséges városok számát (3-7)
ageofheroes-set-victory-monument = Műemlék elkészültség: { $progress }%
ageofheroes-toggle-neighbor-roads = Utak csak szomszédokhoz: { $enabled }
ageofheroes-set-max-hand = Maximum kézben tartható kártyák: { $cards } kártya

# Option change announcements
ageofheroes-option-changed-victory-cities = A győzelemhez { $cities } város szükséges.
ageofheroes-option-changed-victory-monument = Műemlék elkészültségi küszöb { $progress }%-ra állítva.
ageofheroes-option-changed-neighbor-roads = Utak csak szomszédokhoz { $enabled }.
ageofheroes-option-changed-max-hand = Maximum kézméret { $cards } kártyára állítva.

# Setup phase
ageofheroes-setup-start = Te vagy a { $tribe } törzs vezetője. A különleges műemlék erőforrásod: { $special }. Dobjatok kockát a körök sorrendjének megállapításához.
ageofheroes-setup-viewer = A játékosok kockát dobnak a körök sorrendjének megállapításához.
ageofheroes-roll-dice = Dobj kockát
ageofheroes-war-roll-dice = Dobj kockát
ageofheroes-dice-result = { $total } pontot dobtál ({ $die1 } + { $die2 }).
ageofheroes-dice-result-other = { $player } { $total } pontot dobott.
ageofheroes-dice-tie = Több játékos is { $total } pontot dobott. Újra dobunk...
ageofheroes-first-player = { $player } dobta a legmagasabbat { $total } ponttal és kezd.
ageofheroes-first-player-you = { $total } ponttal te kezdesz.

# Preparation phase
ageofheroes-prepare-start = A játékosoknak eseménykártyákat kell kijátszaniuk és katasztrófákat eldobniuk.
ageofheroes-prepare-your-turn = { $count } { $count ->
    [one] kártyád
    *[other] kártyád
} van kijátszásra vagy eldobásra.
ageofheroes-prepare-done = Előkészítési szakasz befejezve.

# Events played/discarded
ageofheroes-population-growth = { $player } kijátssza a Népességnövekedést és új várost épít.
ageofheroes-population-growth-you = Te kijátszod a Népességnövekedést és új várost építesz.
ageofheroes-discard-card = { $player } eldobja: { $card }.
ageofheroes-discard-card-you = Te eldobod: { $card }.
ageofheroes-earthquake = Földrengés sújtja { $player } törzsét; hadseregei felépülésre várnak.
ageofheroes-earthquake-you = Földrengés sújtja törzsed; hadseregeid felépülésre várnak.
ageofheroes-eruption = Kitörés elpusztít egyet { $player } városai közül.
ageofheroes-eruption-you = Kitörés elpusztít egyet a városaid közül.

# Disaster effects
ageofheroes-hunger-strikes = Éhínség pusztít.
ageofheroes-lose-card-hunger = Elveszíted: { $card }.
ageofheroes-barbarians-pillage = Barbárok támadják { $player } erőforrásait.
ageofheroes-barbarians-attack = Barbárok támadják { $player } erőforrásait.
ageofheroes-barbarians-attack-you = Barbárok támadják erőforrásaidat.
ageofheroes-lose-card-barbarians = Elveszíted: { $card }.
ageofheroes-block-with-card = { $player } blokkolja a katasztrófát ezzel: { $card }.
ageofheroes-block-with-card-you = Te blokkolod a katasztrófát ezzel: { $card }.

# Targeted disaster cards (Earthquake/Eruption)
ageofheroes-select-disaster-target = Válassz célpontot ehhez: { $card }.
ageofheroes-no-targets = Nincs elérhető célpont.
ageofheroes-earthquake-strikes-you = { $attacker } Földrengést játszik ellened. Hadseregeid kikapcsolva.
ageofheroes-earthquake-strikes = { $attacker } Földrengést játszik { $player } ellen.
ageofheroes-armies-disabled = { $count } { $count ->
    [one] hadsereg
    *[other] hadsereg
} kikapcsolva egy körig.
ageofheroes-eruption-strikes-you = { $attacker } Kitörést játszik ellened. Egyik városod elpusztul.
ageofheroes-eruption-strikes = { $attacker } Kitörést játszik { $player } ellen.
ageofheroes-city-destroyed = Egy város elpusztul a kitörésben.

# Fair phase
ageofheroes-fair-start = Felkel a nap a piactéren.
ageofheroes-fair-draw-base = Húzol { $count } { $count ->
    [one] kártyát
    *[other] kártyát
}.
ageofheroes-fair-draw-roads = Húzol { $count } további { $count ->
    [one] kártyát
    *[other] kártyát
} az úthálózatodnak köszönhetően.
ageofheroes-fair-draw-other = { $player } húz { $count } { $count ->
    [one] kártyát
    *[other] kártyát
}.

# Trading/Auction
ageofheroes-auction-start = Az árverés kezdődik.
ageofheroes-offer-trade = Csere ajánlata
ageofheroes-offer-made = { $player } felajánlja: { $card } ezért: { $wanted }.
ageofheroes-offer-made-you = Te felajánlod: { $card } ezért: { $wanted }.
ageofheroes-trade-accepted = { $player } elfogadja { $other } ajánlatát és kicseréli { $give } erre: { $receive }.
ageofheroes-trade-accepted-you = Te elfogadod { $other } ajánlatát és megkapod: { $receive }.
ageofheroes-trade-cancelled = { $player } visszavonja ajánlatát: { $card }.
ageofheroes-trade-cancelled-you = Te visszavonod ajánlatodat: { $card }.
ageofheroes-stop-trading = Kereskedés befejezése
ageofheroes-select-request = Felajánlod: { $card }. Mit szeretnél cserébe?
ageofheroes-cancel = Mégse
ageofheroes-left-auction = { $player } távozik.
ageofheroes-left-auction-you = Te távozol a piactérről.
ageofheroes-any-card = Bármilyen kártya
ageofheroes-cannot-trade-own-special = Nem cserélheted el saját különleges műemlék erőforrásodat.
ageofheroes-resource-not-in-game = Ez a különleges erőforrás nincs használatban ebben a játékban.

# Main play phase
ageofheroes-play-start = Játék szakasz.
ageofheroes-day = { $day }. nap
ageofheroes-draw-card = { $player } húz egy kártyát a pakliból.
ageofheroes-draw-card-you = Te húzol { $card } a pakliból.
ageofheroes-your-action = Mit szeretnél tenni?

# Tax Collection
ageofheroes-tax-collection = { $player } Adószedést választ: { $cities } { $cities ->
    [one] város
    *[other] város
} { $cards } { $cards ->
    [one] kártyát
    *[other] kártyát
} gyűjt.
ageofheroes-tax-collection-you = Te Adószedést választasz: { $cities } { $cities ->
    [one] város
    *[other] város
} { $cards } { $cards ->
    [one] kártyát
    *[other] kártyát
} gyűjt.
ageofheroes-tax-no-city = Adószedés: Nincs megmaradt városod. Dobj el egy kártyát, hogy húzz egy újat.
ageofheroes-tax-no-city-done = { $player } Adószedést választ, de nincs városa, így kicserél egy kártyát.
ageofheroes-tax-no-city-done-you = Adószedés: Kicseréltél { $card } egy új kártyára.

# Construction
ageofheroes-construction-menu = Mit szeretnél építeni?
ageofheroes-construction-done = { $player } megépített { $article } { $building }.
ageofheroes-construction-done-you = Te megépítettél { $article } { $building }.
ageofheroes-construction-stop = Építés befejezése
ageofheroes-construction-stopped = Úgy döntöttél, abbahagyod az építkezést.
ageofheroes-road-select-neighbor = Válaszd ki, melyik szomszédhoz szeretnél utat építeni.
ageofheroes-direction-left = Balra
ageofheroes-direction-right = Jobbra
ageofheroes-road-request-sent = Út kérelem elküldve. Várakozás a szomszéd jóváhagyására.
ageofheroes-road-request-received = { $requester } engedélyt kér út építésére törzsedhez.
ageofheroes-road-request-denied-you = Te elutasítottad az út kérelmet.
ageofheroes-road-request-denied = { $denier } elutasította az út kérelmedet.
ageofheroes-road-built = { $tribe1 } és { $tribe2 } most úttal van összekötve.
ageofheroes-road-no-target = Nincs szomszédos törzs útépítéshez.
ageofheroes-approve = Jóváhagy
ageofheroes-deny = Elutasít
ageofheroes-supply-exhausted = Nincs több { $building } építéshez.

# Do Nothing
ageofheroes-do-nothing = { $player } passzol.
ageofheroes-do-nothing-you = Te passzolsz...

# War
ageofheroes-war-declare = { $attacker } háborút indít { $defender } ellen. Cél: { $goal }.
ageofheroes-war-prepare = Válaszd ki hadseregeidet ehhez: { $action }.
ageofheroes-war-no-army = Nincs hadseregeid vagy hőskártyád.
ageofheroes-war-no-targets = Nincs érvényes célpont háborúhoz.
ageofheroes-war-no-valid-goal = Nincs érvényes háborús cél ez ellen a célpont ellen.
ageofheroes-war-select-target = Válaszd ki, melyik játékost támadod meg.
ageofheroes-war-select-goal = Válaszd ki háborús célodat.
ageofheroes-war-prepare-attack = Válaszd ki támadó erőidet.
ageofheroes-war-prepare-defense = { $attacker } támad téged; Válaszd ki védekező erőidet.
ageofheroes-war-select-armies = Hadseregek kiválasztása: { $count }
ageofheroes-war-select-generals = Tábornokok kiválasztása: { $count }
ageofheroes-war-select-heroes = Hősök kiválasztása: { $count }
ageofheroes-war-attack = Támadás...
ageofheroes-war-defend = Védelem...
ageofheroes-war-prepared = Erőid: { $armies } { $armies ->
    [one] hadsereg
    *[other] hadsereg
}{ $generals ->
    [0] {""}
    [one] {" és 1 tábornok"}
    *[other] {" és { $generals } tábornok"}
}{ $heroes ->
    [0] {""}
    [one] {" és 1 hős"}
    *[other] {" és { $heroes } hős"}
}.
ageofheroes-war-roll-you = Te dobsz { $roll }.
ageofheroes-war-roll-other = { $player } dob { $roll }.
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"+1 erődtől = összesen { $total }"}
            *[other] {"+{ $fortress } erődöktől = összesen { $total }"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"+{ $general } tábornoktól = összesen { $total }"}
            [one] {"+{ $general } tábornoktól, +1 erődtől = összesen { $total }"}
            *[other] {"+{ $general } tábornoktól, +{ $fortress } erődöktől = összesen { $total }"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"{ $player }: +1 erődtől = összesen { $total }"}
            *[other] {"{ $player }: +{ $fortress } erődöktől = összesen { $total }"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } tábornoktól = összesen { $total }"}
            [one] {"{ $player }: +{ $general } tábornoktól, +1 erődtől = összesen { $total }"}
            *[other] {"{ $player }: +{ $general } tábornoktól, +{ $fortress } erődöktől = összesen { $total }"}
        }
    }
}

# Battle
ageofheroes-battle-start = A csata kezdődik. { $attacker } { $att_armies } { $att_armies ->
    [one] hadserege
    *[other] hadserege
} { $defender } { $def_armies } { $def_armies ->
    [one] hadserege
    *[other] hadserege
} ellen.
ageofheroes-dice-roll-detailed = { $name } dob { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } tábornoktól" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 erődtől" }
    *[other] { " + { $fortress } erődöktől" }
} = { $total }.
ageofheroes-dice-roll-detailed-you = Te dobsz { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } tábornoktól" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 erődtől" }
    *[other] { " + { $fortress } erődöktől" }
} = { $total }.
ageofheroes-round-attacker-wins = { $attacker } nyeri a kört ({ $att_total } vs { $def_total }). { $defender } veszít egy hadsereget.
ageofheroes-round-defender-wins = { $defender } sikeresen védekezik ({ $def_total } vs { $att_total }). { $attacker } veszít egy hadsereget.
ageofheroes-round-draw = Mindkét oldal { $total } pontot ért el. Nincs veszteség.
ageofheroes-battle-victory-attacker = { $attacker } legyőzi { $defender }.
ageofheroes-battle-victory-defender = { $defender } sikeresen védekezik { $attacker } ellen.
ageofheroes-battle-mutual-defeat = { $attacker } és { $defender } is elveszíti összes hadseregét.
ageofheroes-general-bonus = +{ $count } { $count ->
    [one] tábornoktól
    *[other] tábornoktól
}
ageofheroes-fortress-bonus = +{ $count } erőd védelemből
ageofheroes-battle-winner = { $winner } nyeri a csatát.
ageofheroes-battle-draw = A csata döntetlennel ér véget...
ageofheroes-battle-continue = Csata folytatása.
ageofheroes-battle-end = A csata véget ért.

# War outcomes
ageofheroes-conquest-success = { $attacker } meghódít { $count } { $count ->
    [one] várost
    *[other] várost
} { $defender } től.
ageofheroes-plunder-success = { $attacker } { $count } { $count ->
    [one] kártyát
    *[other] kártyát
} zsákmányol { $defender } től.
ageofheroes-destruction-success = { $attacker } elpusztít { $count } műemlék { $count ->
    [one] erőforrást
    *[other] erőforrást
} { $defender } től.
ageofheroes-army-losses = { $player } veszít { $count } { $count ->
    [one] hadsereget
    *[other] hadsereget
}.
ageofheroes-army-losses-you = Te veszítesz { $count } { $count ->
    [one] hadsereget
    *[other] hadsereget
}.

# Army return
ageofheroes-army-return-road = Csapataid azonnal visszatérnek az úton.
ageofheroes-army-return-delayed = { $count } { $count ->
    [one] egység
    *[other] egység
} visszatér következő köröd végén.
ageofheroes-army-returned = { $player } csapatai visszatértek a háborúból.
ageofheroes-army-returned-you = Csapataid visszatértek a háborúból.
ageofheroes-army-recover = { $player } hadseregei felépülnek a földrengésből.
ageofheroes-army-recover-you = Hadseregeid felépülnek a földrengésből.

# Olympics
ageofheroes-olympics-cancel = { $player } kijátssza az Olimpiai játékokat. Háború törölve.
ageofheroes-olympics-prompt = { $attacker } háborút indított. Van Olimpiai játékok kártyád - használod törlésre?
ageofheroes-yes = Igen
ageofheroes-no = Nem

# Monument progress
ageofheroes-monument-progress = { $player } műemlékének állapota: { $count }/5 kész.
ageofheroes-monument-progress-you = Műemlékének állapota: { $count }/5 kész.

# Hand management
ageofheroes-discard-excess = Több mint { $max } kártyád van. Dobj el { $count } { $count ->
    [one] kártyát
    *[other] kártyát
}.
ageofheroes-discard-excess-other = { $player } nak el kell dobnia felesleges kártyákat.
ageofheroes-discard-more = Dobj el még { $count } { $count ->
    [one] kártyát
    *[other] kártyát
}.

# Victory
ageofheroes-victory-cities = { $player } megépített 5 várost! Az öt város birodalma.
ageofheroes-victory-cities-you = Te megépítettél 5 várost! Az öt város birodalma.
ageofheroes-victory-monument = { $player } befejezte műemlékét! A nagy kultúra hordozói.
ageofheroes-victory-monument-you = Te befejezted műemlékedet! A nagy kultúra hordozói.
ageofheroes-victory-last-standing = { $player } az utolsó fennmaradt törzs! A legkitartóbb.
ageofheroes-victory-last-standing-you = Te vagy az utolsó fennmaradt törzs! A legkitartóbb.
ageofheroes-game-over = Játék vége.

# Elimination
ageofheroes-eliminated = { $player } kiesett.
ageofheroes-eliminated-you = Te kiesett.

# Hand
ageofheroes-hand-empty = Nincs kártyád.
ageofheroes-hand-contents = Kártyáid ({ $count } { $count ->
    [one] kártya
    *[other] kártya
}): { $cards }

# Status
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [one] város
    *[other] város
}, { $armies } { $armies ->
    [one] hadsereg
    *[other] hadsereg
}, { $monument }/5 műemlék
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = Városok: { $count }
ageofheroes-status-armies = Hadseregek: { $count }
ageofheroes-status-generals = Tábornokok: { $count }
ageofheroes-status-fortresses = Erődök: { $count }
ageofheroes-status-monument = Műemlék: { $count }/5
ageofheroes-status-roads = Utak: { $left }{ $right }
ageofheroes-status-road-left = bal
ageofheroes-status-road-right = jobb
ageofheroes-status-none = nincs
ageofheroes-status-earthquake-armies = Felépülő hadseregek: { $count }
ageofheroes-status-returning-armies = Visszatérő hadseregek: { $count }
ageofheroes-status-returning-generals = Visszatérő tábornokok: { $count }

# Deck info
ageofheroes-deck-empty = Nincs több { $card } kártya a pakliban.
ageofheroes-deck-count = Hátralévő kártyák: { $count }
ageofheroes-deck-reshuffled = A dobott kártyák visszakeverve a pakliba.

# Give up
ageofheroes-give-up-confirm = Biztosan fel akarod adni?
ageofheroes-gave-up = { $player } feladta!
ageofheroes-gave-up-you = Te feladtad!

# Hero card
ageofheroes-hero-use = Hadseregként vagy tábornokként használod?
ageofheroes-hero-army = Hadsereg
ageofheroes-hero-general = Tábornok

# Fortune card
ageofheroes-fortune-reroll = { $player } Szerencsét használ újradobáshoz.
ageofheroes-fortune-prompt = Veszítettél a dobásban. Szerencsét használsz újradobáshoz?

# Disabled action reasons
ageofheroes-not-your-turn = Nem te következel.
ageofheroes-game-not-started = A játék még nem kezdődött el.
ageofheroes-wrong-phase = Ez a művelet nem elérhető ebben a szakaszban.
ageofheroes-no-resources = Nincs meg a szükséges erőforrásod.

# Building costs (for display)
ageofheroes-cost-army = 2 gabona, vas
ageofheroes-cost-fortress = Vas, fa, kő
ageofheroes-cost-general = Vas, arany
ageofheroes-cost-road = 2 kő
ageofheroes-cost-city = 2 fa, kő
