# Age of Heroes game messages
# A civilization-building card game for 2-6 players

# Game name
game-name-ageofheroes = Hjältarnas tid

# Tribes
ageofheroes-tribe-egyptians = Egyptier
ageofheroes-tribe-romans = Romare
ageofheroes-tribe-greeks = Greker
ageofheroes-tribe-babylonians = Babylonier
ageofheroes-tribe-celts = Kelter
ageofheroes-tribe-chinese = Kineser

# Special Resources (for monuments)
ageofheroes-special-limestone = Kalksten
ageofheroes-special-concrete = Betong
ageofheroes-special-marble = Marmor
ageofheroes-special-bricks = Tegel
ageofheroes-special-sandstone = Sandsten
ageofheroes-special-granite = Granit

# Standard Resources
ageofheroes-resource-iron = Järn
ageofheroes-resource-wood = Trä
ageofheroes-resource-grain = Spannmål
ageofheroes-resource-stone = Sten
ageofheroes-resource-gold = Guld

# Events
ageofheroes-event-population-growth = Befolkningstillväxt
ageofheroes-event-earthquake = Jordbävning
ageofheroes-event-eruption = Utbrott
ageofheroes-event-hunger = Hunger
ageofheroes-event-barbarians = Barbarer
ageofheroes-event-olympics = Olympiska spel
ageofheroes-event-hero = Hjälte
ageofheroes-event-fortune = Tur

# Buildings
ageofheroes-building-army = Armé
ageofheroes-building-fortress = Fästning
ageofheroes-building-general = General
ageofheroes-building-road = Väg
ageofheroes-building-city = Stad

# Actions
ageofheroes-action-tax-collection = Skatteuppbörd
ageofheroes-action-construction = Byggande
ageofheroes-action-war = Krig
ageofheroes-action-do-nothing = Gör ingenting
ageofheroes-play = Spela

# War goals
ageofheroes-war-conquest = Erövring
ageofheroes-war-plunder = Plundring
ageofheroes-war-destruction = Förstöring

# Game options
ageofheroes-set-victory-cities = Segerstäder: { $cities }
ageofheroes-enter-victory-cities = Ange antal städer för att vinna (3-7)
ageofheroes-set-victory-monument = Monumentets färdigställande: { $progress }%
ageofheroes-toggle-neighbor-roads = Vägar endast till grannar: { $enabled }
ageofheroes-set-max-hand = Maximal handstorlek: { $cards } kort

# Option change announcements
ageofheroes-option-changed-victory-cities = Seger kräver { $cities } städer.
ageofheroes-option-changed-victory-monument = Tröskeln för monumentets färdigställande är { $progress }%.
ageofheroes-option-changed-neighbor-roads = Vägar endast till grannar { $enabled }.
ageofheroes-option-changed-max-hand = Maximal handstorlek inställd på { $cards } kort.

# Setup phase
ageofheroes-setup-start = Du är ledare för { $tribe }-stammen. Din speciella monumentresurs är { $special }. Kasta tärningarna för att bestämma turordning.
ageofheroes-setup-viewer = Spelarna kastar tärningar för att bestämma turordning.
ageofheroes-roll-dice = Kasta tärningarna
ageofheroes-war-roll-dice = Kasta tärningarna
ageofheroes-dice-result = Du kastade { $total } ({ $die1 } + { $die2 }).
ageofheroes-dice-result-other = { $player } kastade { $total }.
ageofheroes-dice-tie = Flera spelare fick { $total }. Kastar igen...
ageofheroes-first-player = { $player } kastade högst med { $total } och börjar först.
ageofheroes-first-player-you = Med { $total } poäng börjar du först.

# Preparation phase
ageofheroes-prepare-start = Spelarna måste spela händelsekort och kasta katastrofer.
ageofheroes-prepare-your-turn = Du har { $count } { $count ->
    [one] kort
    *[other] kort
} att spela eller kasta.
ageofheroes-prepare-done = Förberedelsefasen slutförd.

# Events played/discarded
ageofheroes-population-growth = { $player } spelar Befolkningstillväxt och bygger en ny stad.
ageofheroes-population-growth-you = Du spelar Befolkningstillväxt och bygger en ny stad.
ageofheroes-discard-card = { $player } kastar { $card }.
ageofheroes-discard-card-you = Du kastar { $card }.
ageofheroes-earthquake = En jordbävning drabbar { $player }s stam; deras arméer återhämtar sig.
ageofheroes-earthquake-you = En jordbävning drabbar din stam; dina arméer återhämtar sig.
ageofheroes-eruption = Ett utbrott förstör en av { $player }s städer.
ageofheroes-eruption-you = Ett utbrott förstör en av dina städer.

# Disaster effects
ageofheroes-hunger-strikes = Hungersnöd slår till.
ageofheroes-lose-card-hunger = Du förlorar { $card }.
ageofheroes-barbarians-pillage = Barbarer attackerar { $player }s resurser.
ageofheroes-barbarians-attack = Barbarer attackerar { $player }s resurser.
ageofheroes-barbarians-attack-you = Barbarer attackerar dina resurser.
ageofheroes-lose-card-barbarians = Du förlorar { $card }.
ageofheroes-block-with-card = { $player } blockerar katastrofen med { $card }.
ageofheroes-block-with-card-you = Du blockerar katastrofen med { $card }.

# Targeted disaster cards (Earthquake/Eruption)
ageofheroes-select-disaster-target = Välj ett mål för { $card }.
ageofheroes-no-targets = Inga giltiga mål tillgängliga.
ageofheroes-earthquake-strikes-you = { $attacker } spelar Jordbävning mot dig. Dina arméer är inaktiverade.
ageofheroes-earthquake-strikes = { $attacker } spelar Jordbävning mot { $player }.
ageofheroes-armies-disabled = { $count } { $count ->
    [one] armé är inaktiverad
    *[other] arméer är inaktiverade
} i ett drag.
ageofheroes-eruption-strikes-you = { $attacker } spelar Utbrott mot dig. En av dina städer förstörs.
ageofheroes-eruption-strikes = { $attacker } spelar Utbrott mot { $player }.
ageofheroes-city-destroyed = En stad förstörs av utbrottet.

# Fair phase
ageofheroes-fair-start = Gryningen på marknaden.
ageofheroes-fair-draw-base = Du drar { $count } { $count ->
    [one] kort
    *[other] kort
}.
ageofheroes-fair-draw-roads = Du drar { $count } extra { $count ->
    [one] kort
    *[other] kort
} tack vare ditt vägnätverk.
ageofheroes-fair-draw-other = { $player } drar { $count } { $count ->
    [one] kort
    *[other] kort
}.

# Trading/Auction
ageofheroes-auction-start = Auktionen börjar.
ageofheroes-offer-trade = Erbjud byte
ageofheroes-offer-made = { $player } erbjuder { $card } för { $wanted }.
ageofheroes-offer-made-you = Du erbjuder { $card } för { $wanted }.
ageofheroes-trade-accepted = { $player } accepterar { $other }s erbjudande och byter { $give } mot { $receive }.
ageofheroes-trade-accepted-you = Du accepterar { $other }s erbjudande och får { $receive }.
ageofheroes-trade-cancelled = { $player } drar tillbaka sitt erbjudande för { $card }.
ageofheroes-trade-cancelled-you = Du drar tillbaka ditt erbjudande för { $card }.
ageofheroes-stop-trading = Sluta handla
ageofheroes-select-request = Du erbjuder { $card }. Vad vill du ha i utbyte?
ageofheroes-cancel = Avbryt
ageofheroes-left-auction = { $player } lämnar.
ageofheroes-left-auction-you = Du lämnar marknaden.
ageofheroes-any-card = Vilket kort som helst
ageofheroes-cannot-trade-own-special = Du kan inte byta din egen speciella monumentresurs.
ageofheroes-resource-not-in-game = Denna speciella resurs används inte i detta spel.

# Main play phase
ageofheroes-play-start = Spelfas.
ageofheroes-day = Dag { $day }
ageofheroes-draw-card = { $player } drar ett kort från kortleken.
ageofheroes-draw-card-you = Du drar { $card } från kortleken.
ageofheroes-your-action = Vad vill du göra?

# Tax Collection
ageofheroes-tax-collection = { $player } väljer Skatteuppbörd: { $cities } { $cities ->
    [one] stad
    *[other] städer
} samlar in { $cards } { $cards ->
    [one] kort
    *[other] kort
}.
ageofheroes-tax-collection-you = Du väljer Skatteuppbörd: { $cities } { $cities ->
    [one] stad
    *[other] städer
} samlar in { $cards } { $cards ->
    [one] kort
    *[other] kort
}.
ageofheroes-tax-no-city = Skatteuppbörd: Du har inga överlevande städer. Kasta ett kort för att dra ett nytt.
ageofheroes-tax-no-city-done = { $player } väljer Skatteuppbörd men har inga städer, så de byter ett kort.
ageofheroes-tax-no-city-done-you = Skatteuppbörd: Du bytte { $card } mot ett nytt kort.

# Construction
ageofheroes-construction-menu = Vad vill du bygga?
ageofheroes-construction-done = { $player } byggde { $article } { $building }.
ageofheroes-construction-done-you = Du byggde { $article } { $building }.
ageofheroes-construction-stop = Sluta bygga
ageofheroes-construction-stopped = Du bestämde dig för att sluta bygga.
ageofheroes-road-select-neighbor = Välj vilken granne du ska bygga en väg till.
ageofheroes-direction-left = Till vänster om dig
ageofheroes-direction-right = Till höger om dig
ageofheroes-road-request-sent = Vägförfrågan skickad. Väntar på grannens godkännande.
ageofheroes-road-request-received = { $requester } begär tillstånd att bygga en väg till din stam.
ageofheroes-road-request-denied-you = Du nekade vägförfrågan.
ageofheroes-road-request-denied = { $denier } nekade din vägförfrågan.
ageofheroes-road-built = { $tribe1 } och { $tribe2 } är nu förbundna med en väg.
ageofheroes-road-no-target = Inga grannstammar tillgängliga för vägbygge.
ageofheroes-approve = Godkänn
ageofheroes-deny = Neka
ageofheroes-supply-exhausted = Inga fler { $building } tillgängliga att bygga.

# Do Nothing
ageofheroes-do-nothing = { $player } passar.
ageofheroes-do-nothing-you = Du passar...

# War
ageofheroes-war-declare = { $attacker } förklarar krig mot { $defender }. Mål: { $goal }.
ageofheroes-war-prepare = Välj dina arméer för { $action }.
ageofheroes-war-no-army = Du har inga arméer eller hjältekort tillgängliga.
ageofheroes-war-no-targets = Inga giltiga mål för krig.
ageofheroes-war-no-valid-goal = Inga giltiga krigsmål mot detta mål.
ageofheroes-war-select-target = Välj vilken spelare du ska attackera.
ageofheroes-war-select-goal = Välj ditt krigsmål.
ageofheroes-war-prepare-attack = Välj dina anfallsstyrkor.
ageofheroes-war-prepare-defense = { $attacker } attackerar dig; Välj dina försvarsstyrkor.
ageofheroes-war-select-armies = Välj arméer: { $count }
ageofheroes-war-select-generals = Välj generaler: { $count }
ageofheroes-war-select-heroes = Välj hjältar: { $count }
ageofheroes-war-attack = Attackera...
ageofheroes-war-defend = Försvara...
ageofheroes-war-prepared = Dina styrkor: { $armies } { $armies ->
    [one] armé
    *[other] arméer
}{ $generals ->
    [0] {""}
    [one] {" och 1 general"}
    *[other] {" och { $generals } generaler"}
}{ $heroes ->
    [0] {""}
    [one] {" och 1 hjälte"}
    *[other] {" och { $heroes } hjältar"}
}.
ageofheroes-war-roll-you = Du kastar { $roll }.
ageofheroes-war-roll-other = { $player } kastar { $roll }.
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"+1 från fästning = { $total } totalt"}
            *[other] {"+{ $fortress } från fästningar = { $total } totalt"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"+{ $general } från general = { $total } totalt"}
            [one] {"+{ $general } från general, +1 från fästning = { $total } totalt"}
            *[other] {"+{ $general } från general, +{ $fortress } från fästningar = { $total } totalt"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"{ $player }: +1 från fästning = { $total } totalt"}
            *[other] {"{ $player }: +{ $fortress } från fästningar = { $total } totalt"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } från general = { $total } totalt"}
            [one] {"{ $player }: +{ $general } från general, +1 från fästning = { $total } totalt"}
            *[other] {"{ $player }: +{ $general } från general, +{ $fortress } från fästningar = { $total } totalt"}
        }
    }
}

# Battle
ageofheroes-battle-start = Striden börjar. { $attacker }s { $att_armies } { $att_armies ->
    [one] armé
    *[other] arméer
} mot { $defender }s { $def_armies } { $def_armies ->
    [one] armé
    *[other] arméer
}.
ageofheroes-dice-roll-detailed = { $name } kastar { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } från general" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 från fästning" }
    *[other] { " + { $fortress } från fästningar" }
} = { $total }.
ageofheroes-dice-roll-detailed-you = Du kastar { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } från general" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 från fästning" }
    *[other] { " + { $fortress } från fästningar" }
} = { $total }.
ageofheroes-round-attacker-wins = { $attacker } vinner omgången ({ $att_total } mot { $def_total }). { $defender } förlorar en armé.
ageofheroes-round-defender-wins = { $defender } försvarar sig framgångsrikt ({ $def_total } mot { $att_total }). { $attacker } förlorar en armé.
ageofheroes-round-draw = Båda sidor har { $total }. Inga förlorade arméer.
ageofheroes-battle-victory-attacker = { $attacker } besegrar { $defender }.
ageofheroes-battle-victory-defender = { $defender } försvarar sig framgångsrikt mot { $attacker }.
ageofheroes-battle-mutual-defeat = Både { $attacker } och { $defender } förlorar alla arméer.
ageofheroes-general-bonus = +{ $count } från { $count ->
    [one] general
    *[other] generaler
}
ageofheroes-fortress-bonus = +{ $count } från fästningsförsvar
ageofheroes-battle-winner = { $winner } vinner striden.
ageofheroes-battle-draw = Striden slutar oavgjort...
ageofheroes-battle-continue = Fortsätt striden.
ageofheroes-battle-end = Striden är över.

# War outcomes
ageofheroes-conquest-success = { $attacker } erövrar { $count } { $count ->
    [one] stad
    *[other] städer
} från { $defender }.
ageofheroes-plunder-success = { $attacker } plundrar { $count } { $count ->
    [one] kort
    *[other] kort
} från { $defender }.
ageofheroes-destruction-success = { $attacker } förstör { $count } { $count ->
    [one] monumentresurs
    *[other] monumentresurser
} från { $defender }.
ageofheroes-army-losses = { $player } förlorar { $count } { $count ->
    [one] armé
    *[other] arméer
}.
ageofheroes-army-losses-you = Du förlorar { $count } { $count ->
    [one] armé
    *[other] arméer
}.

# Army return
ageofheroes-army-return-road = Dina trupper återvänder omedelbart via vägen.
ageofheroes-army-return-delayed = { $count } { $count ->
    [one] enhet återvänder
    *[other] enheter återvänder
} i slutet av ditt nästa drag.
ageofheroes-army-returned = { $player }s trupper har återvänt från kriget.
ageofheroes-army-returned-you = Dina trupper har återvänt från kriget.
ageofheroes-army-recover = { $player }s arméer återhämtar sig från jordbävningen.
ageofheroes-army-recover-you = Dina arméer återhämtar sig från jordbävningen.

# Olympics
ageofheroes-olympics-cancel = { $player } spelar Olympiska spel. Krig avbrutet.
ageofheroes-olympics-prompt = { $attacker } har förklarat krig. Du har Olympiska spel - använda det för att avbryta?
ageofheroes-yes = Ja
ageofheroes-no = Nej

# Monument progress
ageofheroes-monument-progress = { $player }s monument är { $count }/5 klart.
ageofheroes-monument-progress-you = Ditt monument är { $count }/5 klart.

# Hand management
ageofheroes-discard-excess = Du har fler än { $max } kort. Kasta { $count } { $count ->
    [one] kort
    *[other] kort
}.
ageofheroes-discard-excess-other = { $player } måste kasta överflödiga kort.
ageofheroes-discard-more = Kasta { $count } { $count ->
    [one] kort
    *[other] kort
} till.

# Victory
ageofheroes-victory-cities = { $player } har byggt 5 städer! Fem städers imperium.
ageofheroes-victory-cities-you = Du har byggt 5 städer! Fem städers imperium.
ageofheroes-victory-monument = { $player } har fullbordat sitt monument! Bärare av stor kultur.
ageofheroes-victory-monument-you = Du har fullbordat ditt monument! Bärare av stor kultur.
ageofheroes-victory-last-standing = { $player } är den sista kvarvarande stammen! Den mest uthålliga.
ageofheroes-victory-last-standing-you = Du är den sista kvarvarande stammen! Den mest uthålliga.
ageofheroes-game-over = Spelet slut.

# Elimination
ageofheroes-eliminated = { $player } har eliminerats.
ageofheroes-eliminated-you = Du har eliminerats.

# Hand
ageofheroes-hand-empty = Du har inga kort.
ageofheroes-hand-contents = Din hand ({ $count } { $count ->
    [one] kort
    *[other] kort
}): { $cards }

# Status
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [one] stad
    *[other] städer
}, { $armies } { $armies ->
    [one] armé
    *[other] arméer
}, { $monument }/5 monument
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = Städer: { $count }
ageofheroes-status-armies = Arméer: { $count }
ageofheroes-status-generals = Generaler: { $count }
ageofheroes-status-fortresses = Fästningar: { $count }
ageofheroes-status-monument = Monument: { $count }/5
ageofheroes-status-roads = Vägar: { $left }{ $right }
ageofheroes-status-road-left = vänster
ageofheroes-status-road-right = höger
ageofheroes-status-none = ingen
ageofheroes-status-earthquake-armies = Återhämtande arméer: { $count }
ageofheroes-status-returning-armies = Återvändande arméer: { $count }
ageofheroes-status-returning-generals = Återvändande generaler: { $count }

# Deck info
ageofheroes-deck-empty = Inga fler { $card }-kort i kortleken.
ageofheroes-deck-count = Återstående kort: { $count }
ageofheroes-deck-reshuffled = Kasthögen har blandats tillbaka i kortleken.

# Give up
ageofheroes-give-up-confirm = Är du säker på att du vill ge upp?
ageofheroes-gave-up = { $player } gav upp!
ageofheroes-gave-up-you = Du gav upp!

# Hero card
ageofheroes-hero-use = Använd som armé eller general?
ageofheroes-hero-army = Armé
ageofheroes-hero-general = General

# Fortune card
ageofheroes-fortune-reroll = { $player } använder Tur för att kasta om.
ageofheroes-fortune-prompt = Du förlorade kastet. Använda Tur för att kasta om?

# Disabled action reasons
ageofheroes-not-your-turn = Det är inte din tur.
ageofheroes-game-not-started = Spelet har inte startat än.
ageofheroes-wrong-phase = Denna åtgärd är inte tillgänglig i den aktuella fasen.
ageofheroes-no-resources = Du har inte de nödvändiga resurserna.

# Building costs (for display)
ageofheroes-cost-army = 2 spannmål, järn
ageofheroes-cost-fortress = Järn, trä, sten
ageofheroes-cost-general = Järn, guld
ageofheroes-cost-road = 2 sten
ageofheroes-cost-city = 2 trä, sten
