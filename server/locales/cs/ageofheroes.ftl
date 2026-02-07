# Age of Heroes - České zprávy hry
# Civilizační karetní hra pro 2-6 hráčů

# Název hry
game-name-ageofheroes = Věk hrdinů

# Kmeny
ageofheroes-tribe-egyptians = Egypťané
ageofheroes-tribe-romans = Římané
ageofheroes-tribe-greeks = Řekové
ageofheroes-tribe-babylonians = Babyloňané
ageofheroes-tribe-celts = Keltové
ageofheroes-tribe-chinese = Číňané

# Speciální suroviny (pro monumenty)
ageofheroes-special-limestone = Vápenec
ageofheroes-special-concrete = Beton
ageofheroes-special-marble = Mramor
ageofheroes-special-bricks = Cihly
ageofheroes-special-sandstone = Pískovec
ageofheroes-special-granite = Žula

# Standardní suroviny
ageofheroes-resource-iron = Železo
ageofheroes-resource-wood = Dřevo
ageofheroes-resource-grain = Obilí
ageofheroes-resource-stone = Kámen
ageofheroes-resource-gold = Zlato

# Události
ageofheroes-event-population-growth = Růst populace
ageofheroes-event-earthquake = Zemětřesení
ageofheroes-event-eruption = Erupce
ageofheroes-event-hunger = Hlad
ageofheroes-event-barbarians = Barbaři
ageofheroes-event-olympics = Olympijské hry
ageofheroes-event-hero = Hrdina
ageofheroes-event-fortune = Štěstí

# Budovy
ageofheroes-building-army = Armáda
ageofheroes-building-fortress = Pevnost
ageofheroes-building-general = Generál
ageofheroes-building-road = Cesta
ageofheroes-building-city = Město

# Akce
ageofheroes-action-tax-collection = Výběr daní
ageofheroes-action-construction = Stavba
ageofheroes-action-war = Válka
ageofheroes-action-do-nothing = Nedělat nic
ageofheroes-play = Hrát

# Cíle války
ageofheroes-war-conquest = Dobytí
ageofheroes-war-plunder = Plenění
ageofheroes-war-destruction = Zničení

# Herní možnosti
ageofheroes-set-victory-cities = Vítězná města: { $cities }
ageofheroes-enter-victory-cities = Zadejte počet měst pro vítězství (3-7)
ageofheroes-set-victory-monument = Dokončení monumentu: { $progress }%
ageofheroes-toggle-neighbor-roads = Cesty jen k sousedům: { $enabled }
ageofheroes-set-max-hand = Maximální počet karet v ruce: { $cards } karet

# Oznámení změn nastavení
ageofheroes-option-changed-victory-cities = Vítězství vyžaduje { $cities } { $cities ->
    [one] město
    [few] města
    [many] města
   *[other] měst
}.
ageofheroes-option-changed-victory-monument = Práh dokončení monumentu nastaven na { $progress }%.
ageofheroes-option-changed-neighbor-roads = Cesty jen k sousedům { $enabled }.
ageofheroes-option-changed-max-hand = Maximální počet karet v ruce nastaven na { $cards } { $cards ->
    [one] kartu
    [few] karty
    [many] karty
   *[other] karet
}.

# Fáze přípravy
ageofheroes-setup-start = Jste vůdcem kmene { $tribe }. Vaše speciální surovina pro monument je { $special }. Hoďte kostkami pro určení pořadí tahů.
ageofheroes-setup-viewer = Hráči hází kostkami pro určení pořadí tahů.
ageofheroes-roll-dice = Hodit kostkami
ageofheroes-war-roll-dice = Hodit kostkami
ageofheroes-dice-result = Hodil jste { $total } ({ $die1 } + { $die2 }).
ageofheroes-dice-result-other = { $player } hodil { $total }.
ageofheroes-dice-tie = Více hráčů má stejný výsledek { $total }. Hází se znovu...
ageofheroes-first-player = { $player } hodil nejvíc ({ $total }) a začína.
ageofheroes-first-player-you = S { $total } body začínáte vy.

# Přípravná fáze
ageofheroes-prepare-start = Hráči musí zahrát události a odhodit pohromy.
ageofheroes-prepare-your-turn = Máte { $count } { $count ->
    [one] kartu
    [few] karty
    [many] karty
   *[other] karet
} ke hraní nebo odhození.
ageofheroes-prepare-done = Přípravná fáze dokončena.

# Zahrané/odhozené události
ageofheroes-population-growth = { $player } hraje Růst populace a staví nové město.
ageofheroes-population-growth-you = Hrajete Růst populace a stavíte nové město.
ageofheroes-discard-card = { $player } odhazuje { $card }.
ageofheroes-discard-card-you = Odhazujete { $card }.
ageofheroes-earthquake = Zemětřesení postihuje kmen { $player }; jejich armády se zotavují.
ageofheroes-earthquake-you = Zemětřesení postihuje váš kmen; vaše armády se zotavují.
ageofheroes-eruption = Erupce ničí jedno z měst hráče { $player }.
ageofheroes-eruption-you = Erupce ničí jedno z vašich měst.

# Účinky pohromy
ageofheroes-hunger-strikes = Útočí hlad.
ageofheroes-lose-card-hunger = Ztrácíte { $card }.
ageofheroes-barbarians-pillage = Barbaři napadají suroviny hráče { $player }.
ageofheroes-barbarians-attack = Barbaři napadají suroviny hráče { $player }.
ageofheroes-barbarians-attack-you = Barbaři napadají vaše suroviny.
ageofheroes-lose-card-barbarians = Ztrácíte { $card }.
ageofheroes-block-with-card = { $player } blokuje pohromu použitím { $card }.
ageofheroes-block-with-card-you = Blokujete pohromu použitím { $card }.

# Cílené karty pohrom (Zemětřesení/Erupce)
ageofheroes-select-disaster-target = Vyberte cíl pro { $card }.
ageofheroes-no-targets = Nejsou k dispozici žádné platné cíle.
ageofheroes-earthquake-strikes-you = { $attacker } hraje Zemětřesení proti vám. Vaše armády jsou vyřazeny.
ageofheroes-earthquake-strikes = { $attacker } hraje Zemětřesení proti { $player }.
ageofheroes-armies-disabled = { $count } { $count ->
    [one] armáda je
    [few] armády jsou
    [many] armády je
   *[other] armád je
} vyřazeno na jeden tah.
ageofheroes-eruption-strikes-you = { $attacker } hraje Erupci proti vám. Jedno z vašich měst je zničeno.
ageofheroes-eruption-strikes = { $attacker } hraje Erupci proti { $player }.
ageofheroes-city-destroyed = Město je zničeno erupcí.

# Tržní fáze
ageofheroes-fair-start = Den svítá na tržišti.
ageofheroes-fair-draw-base = Berete { $count } { $count ->
    [one] kartu
    [few] karty
    [many] karty
   *[other] karet
}.
ageofheroes-fair-draw-roads = Berete { $count } { $count ->
    [one] další kartu
    [few] další karty
    [many] další karty
   *[other] dalších karet
} díky vaší cestní síti.
ageofheroes-fair-draw-other = { $player } bere { $count } { $count ->
    [one] kartu
    [few] karty
    [many] karty
   *[other] karet
}.

# Obchodování/Aukce
ageofheroes-auction-start = Začíná aukce.
ageofheroes-offer-trade = Nabídnout výměnu
ageofheroes-offer-made = { $player } nabízí { $card } za { $wanted }.
ageofheroes-offer-made-you = Nabízíte { $card } za { $wanted }.
ageofheroes-trade-accepted = { $player } přijímá nabídku hráče { $other } a vyměňuje { $give } za { $receive }.
ageofheroes-trade-accepted-you = Přijímáte nabídku hráče { $other } a dostáváte { $receive }.
ageofheroes-trade-cancelled = { $player } stahuje svou nabídku za { $card }.
ageofheroes-trade-cancelled-you = Stahujete svou nabídku za { $card }.
ageofheroes-stop-trading = Ukončit obchodování
ageofheroes-select-request = Nabízíte { $card }. Co chcete na oplátku?
ageofheroes-cancel = Zrušit
ageofheroes-left-auction = { $player } odchází.
ageofheroes-left-auction-you = Odcházíte z tržiště.
ageofheroes-any-card = Jakákoli karta
ageofheroes-cannot-trade-own-special = Nemůžete obchodovat s vlastní speciální surovinou pro monument.
ageofheroes-resource-not-in-game = Tato speciální surovina se v této hře nepoužívá.

# Hlavní herní fáze
ageofheroes-play-start = Herní fáze.
ageofheroes-day = Den { $day }
ageofheroes-draw-card = { $player } bere kartu z balíčku.
ageofheroes-draw-card-you = Berete { $card } z balíčku.
ageofheroes-your-action = Co chcete dělat?

# Výběr daní
ageofheroes-tax-collection = { $player } volí Výběr daní: { $cities } { $cities ->
    [one] město
    [few] města
    [many] města
   *[other] měst
} vybírá { $cards } { $cards ->
    [one] kartu
    [few] karty
    [many] karty
   *[other] karet
}.
ageofheroes-tax-collection-you = Volíte Výběr daní: { $cities } { $cities ->
    [one] město
    [few] města
    [many] města
   *[other] měst
} vybírá { $cards } { $cards ->
    [one] kartu
    [few] karty
    [many] karty
   *[other] karet
}.
ageofheroes-tax-no-city = Výběr daní: Nemáte žádná města. Odhoďte kartu a doberte novou.
ageofheroes-tax-no-city-done = { $player } volí Výběr daní, ale nemá města, tak vyměňuje kartu.
ageofheroes-tax-no-city-done-you = Výběr daní: Vyměnili jste { $card } za novou kartu.

# Stavba
ageofheroes-construction-menu = Co chcete postavit?
ageofheroes-construction-done = { $player } postavil { $article } { $building }.
ageofheroes-construction-done-you = Postavili jste { $article } { $building }.
ageofheroes-construction-stop = Ukončit stavbu
ageofheroes-construction-stopped = Rozhodli jste se ukončit stavbu.
ageofheroes-road-select-neighbor = Vyberte, ke kterému sousedovi postavit cestu.
ageofheroes-direction-left = Nalevo
ageofheroes-direction-right = Napravo
ageofheroes-road-request-sent = Žádost o cestu odeslána. Čeká se na souhlas souseda.
ageofheroes-road-request-received = { $requester } žádá o povolení postavit cestu k vašemu kmeni.
ageofheroes-road-request-denied-you = Odmítli jste žádost o cestu.
ageofheroes-road-request-denied = { $denier } odmítl vaši žádost o cestu.
ageofheroes-road-built = { $tribe1 } a { $tribe2 } jsou nyní propojeny cestou.
ageofheroes-road-no-target = Žádné sousední kmeny nejsou k dispozici pro stavbu cesty.
ageofheroes-approve = Schválit
ageofheroes-deny = Odmítnout
ageofheroes-supply-exhausted = Již nejsou k dispozici žádné { $building } ke stavbě.

# Nedělat nic
ageofheroes-do-nothing = { $player } pasuje.
ageofheroes-do-nothing-you = Pasujete...

# Válka
ageofheroes-war-declare = { $attacker } vyhlašuje válku { $defender }. Cíl: { $goal }.
ageofheroes-war-prepare = Vyberte své armády pro { $action }.
ageofheroes-war-no-army = Nemáte k dispozici žádné armády ani karty hrdinů.
ageofheroes-war-no-targets = Žádné platné cíle pro válku.
ageofheroes-war-no-valid-goal = Žádné platné válečné cíle proti tomuto cíli.
ageofheroes-war-select-target = Vyberte, kterého hráče napadnout.
ageofheroes-war-select-goal = Vyberte svůj válečný cíl.
ageofheroes-war-prepare-attack = Vyberte své útočící síly.
ageofheroes-war-prepare-defense = { $attacker } vás napadá; Vyberte své obranné síly.
ageofheroes-war-select-armies = Vyberte armády: { $count }
ageofheroes-war-select-generals = Vyberte generály: { $count }
ageofheroes-war-select-heroes = Vyberte hrdiny: { $count }
ageofheroes-war-attack = Útok...
ageofheroes-war-defend = Obrana...
ageofheroes-war-prepared = Vaše síly: { $armies } { $armies ->
    [one] armáda
    [few] armády
    [many] armády
   *[other] armád
}{ $generals ->
    [0] {""}
    [one] {" a 1 generál"}
    [few] {" a { $generals } generálové"}
    [many] {" a { $generals } generála"}
   *[other] {" a { $generals } generálů"}
}{ $heroes ->
    [0] {""}
    [one] {" a 1 hrdina"}
    [few] {" a { $heroes } hrdinové"}
    [many] {" a { $heroes } hrdiny"}
   *[other] {" a { $heroes } hrdinů"}
}.
ageofheroes-war-roll-you = Hážete { $roll }.
ageofheroes-war-roll-other = { $player } hází { $roll }.
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [1] {"+1 z pevnosti = { $total } celkem"}
           *[other] {"+{ $fortress } z pevností = { $total } celkem"}
        }
    }
   *[other] {
        { $fortress ->
            [0] {"+{ $general } od generála = { $total } celkem"}
            [1] {"+{ $general } od generála, +1 z pevnosti = { $total } celkem"}
           *[other] {"+{ $general } od generála, +{ $fortress } z pevností = { $total } celkem"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [1] {"{ $player }: +1 z pevnosti = { $total } celkem"}
           *[other] {"{ $player }: +{ $fortress } z pevností = { $total } celkem"}
        }
    }
   *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } od generála = { $total } celkem"}
            [1] {"{ $player }: +{ $general } od generála, +1 z pevnosti = { $total } celkem"}
           *[other] {"{ $player }: +{ $general } od generála, +{ $fortress } z pevností = { $total } celkem"}
        }
    }
}

# Bitva
ageofheroes-battle-start = Začíná bitva. { $attacker } má { $att_armies } { $att_armies ->
    [one] armádu
    [few] armády
    [many] armády
   *[other] armád
} proti { $def_armies } { $def_armies ->
    [one] armádě
    [few] armádám
    [many] armádám
   *[other] armádám
} hráče { $defender }.
ageofheroes-dice-roll-detailed = { $name } hází { $dice }{ $general ->
    [0] {""}
   *[other] { " + { $general } od generála" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 z pevnosti" }
   *[other] { " + { $fortress } z pevností" }
} = { $total }.
ageofheroes-dice-roll-detailed-you = Hážete { $dice }{ $general ->
    [0] {""}
   *[other] { " + { $general } od generála" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 z pevnosti" }
   *[other] { " + { $fortress } z pevností" }
} = { $total }.
ageofheroes-round-attacker-wins = { $attacker } vyhrává kolo ({ $att_total } vs { $def_total }). { $defender } ztrácí armádu.
ageofheroes-round-defender-wins = { $defender } úspěšně brání ({ $def_total } vs { $att_total }). { $attacker } ztrácí armádu.
ageofheroes-round-draw = Obě strany remizují na { $total }. Žádné armády neztraceny.
ageofheroes-battle-victory-attacker = { $attacker } poráží { $defender }.
ageofheroes-battle-victory-defender = { $defender } úspěšně brání proti { $attacker }.
ageofheroes-battle-mutual-defeat = { $attacker } i { $defender } ztrácejí všechny armády.
ageofheroes-general-bonus = +{ $count } od { $count ->
    [one] generála
    [few] generálů
    [many] generála
   *[other] generálů
}
ageofheroes-fortress-bonus = +{ $count } od obrany pevností
ageofheroes-battle-winner = { $winner } vyhrává bitvu.
ageofheroes-battle-draw = Bitva končí remízou...
ageofheroes-battle-continue = Pokračovat v bitvě.
ageofheroes-battle-end = Bitva skončila.

# Výsledky války
ageofheroes-conquest-success = { $attacker } dobývá { $count } { $count ->
    [one] město
    [few] města
    [many] města
   *[other] měst
} od { $defender }.
ageofheroes-plunder-success = { $attacker } plenÍ { $count } { $count ->
    [one] kartu
    [few] karty
    [many] karty
   *[other] karet
} od { $defender }.
ageofheroes-destruction-success = { $attacker } ničí { $count } { $count ->
    [one] surovinu
    [few] suroviny
    [many] suroviny
   *[other] surovin
} monumentu hráče { $defender }.
ageofheroes-army-losses = { $player } ztrácí { $count } { $count ->
    [one] armádu
    [few] armády
    [many] armády
   *[other] armád
}.
ageofheroes-army-losses-you = Ztrácíte { $count } { $count ->
    [one] armádu
    [few] armády
    [many] armády
   *[other] armád
}.

# Návrat armády
ageofheroes-army-return-road = Vaše jednotky se vracejí ihned po cestě.
ageofheroes-army-return-delayed = { $count } { $count ->
    [one] jednotka se vrací
    [few] jednotky se vracejí
    [many] jednotky se vrací
   *[other] jednotek se vrací
} na konci vašeho příštího tahu.
ageofheroes-army-returned = Jednotky hráče { $player } se vrátily z války.
ageofheroes-army-returned-you = Vaše jednotky se vrátily z války.
ageofheroes-army-recover = Armády hráče { $player } se zotavují ze zemětřesení.
ageofheroes-army-recover-you = Vaše armády se zotavují ze zemětřesení.

# Olympiáda
ageofheroes-olympics-cancel = { $player } hraje Olympijské hry. Válka zrušena.
ageofheroes-olympics-prompt = { $attacker } vyhlásil válku. Máte Olympijské hry - použít je ke zrušení?
ageofheroes-yes = Ano
ageofheroes-no = Ne

# Postup monumentu
ageofheroes-monument-progress = Monument hráče { $player } je dokončen na { $count }/5.
ageofheroes-monument-progress-you = Váš monument je dokončen na { $count }/5.

# Správa ruky
ageofheroes-discard-excess = Máte více než { $max } karet. Odhoďte { $count } { $count ->
    [one] kartu
    [few] karty
    [many] karty
   *[other] karet
}.
ageofheroes-discard-excess-other = { $player } musí odhodit přebytečné karty.
ageofheroes-discard-more = Odhoďte ještě { $count } { $count ->
    [one] kartu
    [few] karty
    [many] karty
   *[other] karet
}.

# Vítězství
ageofheroes-victory-cities = { $player } postavil 5 měst! Říše pěti měst.
ageofheroes-victory-cities-you = Postavili jste 5 měst! Říše pěti měst.
ageofheroes-victory-monument = { $player } dokončil svůj monument! Nositelé velké kultury.
ageofheroes-victory-monument-you = Dokončili jste svůj monument! Nositelé velké kultury.
ageofheroes-victory-last-standing = { $player } je poslední přeživší kmen! Nejodolnější.
ageofheroes-victory-last-standing-you = Jste poslední přeživší kmen! Nejodolnější.
ageofheroes-game-over = Konec hry.

# Vyřazení
ageofheroes-eliminated = { $player } byl vyřazen.
ageofheroes-eliminated-you = Byli jste vyřazeni.

# Ruka
ageofheroes-hand-empty = Nemáte žádné karty.
ageofheroes-hand-contents = Vaše ruka ({ $count } { $count ->
    [one] karta
    [few] karty
    [many] karty
   *[other] karet
}): { $cards }

# Stav
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [one] město
    [few] města
    [many] města
   *[other] měst
}, { $armies } { $armies ->
    [one] armáda
    [few] armády
    [many] armády
   *[other] armád
}, { $monument }/5 monument
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = Města: { $count }
ageofheroes-status-armies = Armády: { $count }
ageofheroes-status-generals = Generálové: { $count }
ageofheroes-status-fortresses = Pevnosti: { $count }
ageofheroes-status-monument = Monument: { $count }/5
ageofheroes-status-roads = Cesty: { $left }{ $right }
ageofheroes-status-road-left = vlevo
ageofheroes-status-road-right = vpravo
ageofheroes-status-none = žádné
ageofheroes-status-earthquake-armies = Zotavující se armády: { $count }
ageofheroes-status-returning-armies = Vracející se armády: { $count }
ageofheroes-status-returning-generals = Vracející se generálové: { $count }

# Informace o balíčku
ageofheroes-deck-empty = V balíčku již nejsou žádné karty { $card }.
ageofheroes-deck-count = Zbývající karty: { $count }
ageofheroes-deck-reshuffled = Odhazovací balíček byl zamíchán zpět do balíčku.

# Vzdání se
ageofheroes-give-up-confirm = Opravdu se chcete vzdát?
ageofheroes-gave-up = { $player } se vzdal!
ageofheroes-gave-up-you = Vzdali jste se!

# Karta hrdiny
ageofheroes-hero-use = Použít jako armádu nebo generála?
ageofheroes-hero-army = Armáda
ageofheroes-hero-general = Generál

# Karta štěstí
ageofheroes-fortune-reroll = { $player } používá Štěstí k přehození.
ageofheroes-fortune-prompt = Prohráli jste hod. Použít Štěstí k přehození?

# Důvody zakázaných akcí
ageofheroes-not-your-turn = Není váš tah.
ageofheroes-game-not-started = Hra ještě nezačala.
ageofheroes-wrong-phase = Tato akce není dostupná v aktuální fázi.
ageofheroes-no-resources = Nemáte potřebné suroviny.

# Náklady na stavby (pro zobrazení)
ageofheroes-cost-army = 2× Obilí, Železo
ageofheroes-cost-fortress = Železo, Dřevo, Kámen
ageofheroes-cost-general = Železo, Zlato
ageofheroes-cost-road = 2× Kámen
ageofheroes-cost-city = 2× Dřevo, Kámen
