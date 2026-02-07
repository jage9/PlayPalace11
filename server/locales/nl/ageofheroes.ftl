# Age of Heroes game messages
# A civilization-building card game for 2-6 players

# Game name
game-name-ageofheroes = Age of Heroes

# Tribes
ageofheroes-tribe-egyptians = Egyptenaren
ageofheroes-tribe-romans = Romeinen
ageofheroes-tribe-greeks = Grieken
ageofheroes-tribe-babylonians = Babyloniërs
ageofheroes-tribe-celts = Kelten
ageofheroes-tribe-chinese = Chinezen

# Special Resources (for monuments)
ageofheroes-special-limestone = Kalksteen
ageofheroes-special-concrete = Beton
ageofheroes-special-marble = Marmer
ageofheroes-special-bricks = Bakstenen
ageofheroes-special-sandstone = Zandsteen
ageofheroes-special-granite = Graniet

# Standard Resources
ageofheroes-resource-iron = IJzer
ageofheroes-resource-wood = Hout
ageofheroes-resource-grain = Graan
ageofheroes-resource-stone = Steen
ageofheroes-resource-gold = Goud

# Events
ageofheroes-event-population-growth = Bevolkingsgroei
ageofheroes-event-earthquake = Aardbeving
ageofheroes-event-eruption = Uitbarsting
ageofheroes-event-hunger = Honger
ageofheroes-event-barbarians = Barbaren
ageofheroes-event-olympics = Olympische Spelen
ageofheroes-event-hero = Held
ageofheroes-event-fortune = Fortuin

# Buildings
ageofheroes-building-army = Leger
ageofheroes-building-fortress = Fort
ageofheroes-building-general = Generaal
ageofheroes-building-road = Weg
ageofheroes-building-city = Stad

# Actions
ageofheroes-action-tax-collection = Belastinginning
ageofheroes-action-construction = Bouw
ageofheroes-action-war = Oorlog
ageofheroes-action-do-nothing = Doe Niets
ageofheroes-play = Speel

# War goals
ageofheroes-war-conquest = Verovering
ageofheroes-war-plunder = Plundering
ageofheroes-war-destruction = Vernietiging

# Game options
ageofheroes-set-victory-cities = Overwinning steden: { $cities }
ageofheroes-enter-victory-cities = Voer aantal steden om te winnen in (3-7)
ageofheroes-set-victory-monument = Monument voltooiing: { $progress }%
ageofheroes-toggle-neighbor-roads = Wegen alleen naar buren: { $enabled }
ageofheroes-set-max-hand = Maximale handgrootte: { $cards } kaarten

# Option change announcements
ageofheroes-option-changed-victory-cities = Overwinning vereist { $cities } steden.
ageofheroes-option-changed-victory-monument = Monument voltooiingsdrempel ingesteld op { $progress }%.
ageofheroes-option-changed-neighbor-roads = Wegen alleen naar buren { $enabled }.
ageofheroes-option-changed-max-hand = Maximale handgrootte ingesteld op { $cards } kaarten.

# Setup phase
ageofheroes-setup-start = Je bent de leider van de { $tribe } stam. Je speciale monumentbron is { $special }. Gooi de dobbelstenen om de beurtorde te bepalen.
ageofheroes-setup-viewer = Spelers gooien dobbelstenen om de beurtorde te bepalen.
ageofheroes-roll-dice = Gooi de dobbelstenen
ageofheroes-war-roll-dice = Gooi de dobbelstenen
ageofheroes-dice-result = Je gooide { $total } ({ $die1 } + { $die2 }).
ageofheroes-dice-result-other = { $player } gooide { $total }.
ageofheroes-dice-tie = Meerdere spelers gelijk met { $total }. Opnieuw gooien...
ageofheroes-first-player = { $player } gooide het hoogst met { $total } en gaat eerst.
ageofheroes-first-player-you = Met { $total } punten, ga jij eerst.

# Preparation phase
ageofheroes-prepare-start = Spelers moeten gebeurteniskaarten spelen en rampen weggooien.
ageofheroes-prepare-your-turn = Je hebt { $count } { $count ->
    [one] kaart
    *[other] kaarten
} om te spelen of weg te gooien.
ageofheroes-prepare-done = Voorbereidingsfase voltooid.

# Events played/discarded
ageofheroes-population-growth = { $player } speelt Bevolkingsgroei en bouwt een nieuwe stad.
ageofheroes-population-growth-you = Je speelt Bevolkingsgroei en bouwt een nieuwe stad.
ageofheroes-discard-card = { $player } gooit { $card } weg.
ageofheroes-discard-card-you = Je gooit { $card } weg.
ageofheroes-earthquake = Een aardbeving treft { $player }'s stam; hun legers gaan in herstel.
ageofheroes-earthquake-you = Een aardbeving treft je stam; je legers gaan in herstel.
ageofheroes-eruption = Een uitbarsting vernietigt een van { $player }'s steden.
ageofheroes-eruption-you = Een uitbarsting vernietigt een van je steden.

# Disaster effects
ageofheroes-hunger-strikes = Honger slaat toe.
ageofheroes-lose-card-hunger = Je verliest { $card }.
ageofheroes-barbarians-pillage = Barbaren vallen { $player }'s hulpbronnen aan.
ageofheroes-barbarians-attack = Barbaren vallen { $player }'s hulpbronnen aan.
ageofheroes-barbarians-attack-you = Barbaren vallen je hulpbronnen aan.
ageofheroes-lose-card-barbarians = Je verliest { $card }.
ageofheroes-block-with-card = { $player } blokkeert de ramp met { $card }.
ageofheroes-block-with-card-you = Je blokkeert de ramp met { $card }.

# Targeted disaster cards (Earthquake/Eruption)
ageofheroes-select-disaster-target = Selecteer een doel voor { $card }.
ageofheroes-no-targets = Geen geldige doelen beschikbaar.
ageofheroes-earthquake-strikes-you = { $attacker } speelt Aardbeving tegen jou. Je legers zijn uitgeschakeld.
ageofheroes-earthquake-strikes = { $attacker } speelt Aardbeving tegen { $player }.
ageofheroes-armies-disabled = { $count } { $count ->
    [one] leger is
    *[other] legers zijn
} uitgeschakeld voor één beurt.
ageofheroes-eruption-strikes-you = { $attacker } speelt Uitbarsting tegen jou. Een van je steden wordt vernietigd.
ageofheroes-eruption-strikes = { $attacker } speelt Uitbarsting tegen { $player }.
ageofheroes-city-destroyed = Een stad wordt vernietigd door de uitbarsting.

# Fair phase
ageofheroes-fair-start = De dag breekt aan op de marktplaats.
ageofheroes-fair-draw-base = Je trekt { $count } { $count ->
    [one] kaart
    *[other] kaarten
}.
ageofheroes-fair-draw-roads = Je trekt { $count } extra { $count ->
    [one] kaart
    *[other] kaarten
} dankzij je wegennetwerk.
ageofheroes-fair-draw-other = { $player } trekt { $count } { $count ->
    [one] kaart
    *[other] kaarten
}.

# Trading/Auction
ageofheroes-auction-start = Veiling begint.
ageofheroes-offer-trade = Bied aan om te ruilen
ageofheroes-offer-made = { $player } biedt { $card } aan voor { $wanted }.
ageofheroes-offer-made-you = Je biedt { $card } aan voor { $wanted }.
ageofheroes-trade-accepted = { $player } accepteert { $other }'s aanbod en ruilt { $give } voor { $receive }.
ageofheroes-trade-accepted-you = Je accepteert { $other }'s aanbod en ontvangt { $receive }.
ageofheroes-trade-cancelled = { $player } trekt hun aanbod voor { $card } in.
ageofheroes-trade-cancelled-you = Je trekt je aanbod voor { $card } in.
ageofheroes-stop-trading = Stop met Ruilen
ageofheroes-select-request = Je biedt { $card } aan. Wat wil je ervoor terug?
ageofheroes-cancel = Annuleer
ageofheroes-left-auction = { $player } vertrekt.
ageofheroes-left-auction-you = Je vertrekt van de marktplaats.
ageofheroes-any-card = Elke kaart
ageofheroes-cannot-trade-own-special = Je kunt je eigen speciale monumentbron niet ruilen.
ageofheroes-resource-not-in-game = Deze speciale bron wordt niet gebruikt in dit spel.

# Main play phase
ageofheroes-play-start = Speelfase.
ageofheroes-day = Dag { $day }
ageofheroes-draw-card = { $player } trekt een kaart van het deck.
ageofheroes-draw-card-you = Je trekt { $card } van het deck.
ageofheroes-your-action = Wat wil je doen?

# Tax Collection
ageofheroes-tax-collection = { $player } kiest Belastinginning: { $cities } { $cities ->
    [one] stad
    *[other] steden
} verzamelt { $cards } { $cards ->
    [one] kaart
    *[other] kaarten
}.
ageofheroes-tax-collection-you = Je kiest Belastinginning: { $cities } { $cities ->
    [one] stad
    *[other] steden
} verzamelt { $cards } { $cards ->
    [one] kaart
    *[other] kaarten
}.
ageofheroes-tax-no-city = Belastinginning: Je hebt geen overlevende steden. Gooi een kaart weg om een nieuwe te trekken.
ageofheroes-tax-no-city-done = { $player } kiest Belastinginning maar heeft geen steden, dus ze wisselen een kaart.
ageofheroes-tax-no-city-done-you = Belastinginning: Je wisselde { $card } voor een nieuwe kaart.

# Construction
ageofheroes-construction-menu = Wat wil je bouwen?
ageofheroes-construction-done = { $player } bouwde { $article } { $building }.
ageofheroes-construction-done-you = Je bouwde { $article } { $building }.
ageofheroes-construction-stop = Stop met bouwen
ageofheroes-construction-stopped = Je besloot te stoppen met bouwen.
ageofheroes-road-select-neighbor = Selecteer naar welke buur je een weg wilt bouwen.
ageofheroes-direction-left = Naar je linker
ageofheroes-direction-right = Naar je rechter
ageofheroes-road-request-sent = Wegverzoek verzonden. Wachten op goedkeuring van buur.
ageofheroes-road-request-received = { $requester } vraagt toestemming om een weg naar je stam te bouwen.
ageofheroes-road-request-denied-you = Je weigerde het wegverzoek.
ageofheroes-road-request-denied = { $denier } weigerde je wegverzoek.
ageofheroes-road-built = { $tribe1 } en { $tribe2 } zijn nu verbonden per weg.
ageofheroes-road-no-target = Geen naburige stammen beschikbaar voor wegenbouw.
ageofheroes-approve = Goedkeuren
ageofheroes-deny = Weigeren
ageofheroes-supply-exhausted = Geen { $building } meer beschikbaar om te bouwen.

# Do Nothing
ageofheroes-do-nothing = { $player } past.
ageofheroes-do-nothing-you = Je past...

# War
ageofheroes-war-declare = { $attacker } verklaart oorlog aan { $defender }. Doel: { $goal }.
ageofheroes-war-prepare = Selecteer je legers voor { $action }.
ageofheroes-war-no-army = Je hebt geen legers of heldenkaarten beschikbaar.
ageofheroes-war-no-targets = Geen geldige doelen voor oorlog.
ageofheroes-war-no-valid-goal = Geen geldige oorlogsdoelen tegen dit doel.
ageofheroes-war-select-target = Selecteer welke speler je wilt aanvallen.
ageofheroes-war-select-goal = Selecteer je oorlogsdoel.
ageofheroes-war-prepare-attack = Selecteer je aanvallende troepen.
ageofheroes-war-prepare-defense = { $attacker } valt je aan; Selecteer je verdedigende troepen.
ageofheroes-war-select-armies = Selecteer legers: { $count }
ageofheroes-war-select-generals = Selecteer generaals: { $count }
ageofheroes-war-select-heroes = Selecteer helden: { $count }
ageofheroes-war-attack = Aanvallen...
ageofheroes-war-defend = Verdedigen...
ageofheroes-war-prepared = Je troepen: { $armies } { $armies ->
    [one] leger
    *[other] legers
}{ $generals ->
    [0] {""}
    [one] {" en 1 generaal"}
    *[other] {" en { $generals } generaals"}
}{ $heroes ->
    [0] {""}
    [one] {" en 1 held"}
    *[other] {" en { $heroes } helden"}
}.
ageofheroes-war-roll-you = Je gooit { $roll }.
ageofheroes-war-roll-other = { $player } gooit { $roll }.
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [1] {"+1 van fort = { $total } totaal"}
            *[other] {"+{ $fortress } van forten = { $total } totaal"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"+{ $general } van generaal = { $total } totaal"}
            [1] {"+{ $general } van generaal, +1 van fort = { $total } totaal"}
            *[other] {"+{ $general } van generaal, +{ $fortress } van forten = { $total } totaal"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [1] {"{ $player }: +1 van fort = { $total } totaal"}
            *[other] {"{ $player }: +{ $fortress } van forten = { $total } totaal"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } van generaal = { $total } totaal"}
            [1] {"{ $player }: +{ $general } van generaal, +1 van fort = { $total } totaal"}
            *[other] {"{ $player }: +{ $general } van generaal, +{ $fortress } van forten = { $total } totaal"}
        }
    }
}

# Battle
ageofheroes-battle-start = Gevecht begint. { $attacker }'s { $att_armies } { $att_armies ->
    [one] leger
    *[other] legers
} tegen { $defender }'s { $def_armies } { $def_armies ->
    [one] leger
    *[other] legers
}.
ageofheroes-dice-roll-detailed = { $name } gooit { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } van generaal" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 van fort" }
    *[other] { " + { $fortress } van forten" }
} = { $total }.
ageofheroes-dice-roll-detailed-you = Je gooit { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } van generaal" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 van fort" }
    *[other] { " + { $fortress } van forten" }
} = { $total }.
ageofheroes-round-attacker-wins = { $attacker } wint de ronde ({ $att_total } tegen { $def_total }). { $defender } verliest een leger.
ageofheroes-round-defender-wins = { $defender } verdedigt succesvol ({ $def_total } tegen { $att_total }). { $attacker } verliest een leger.
ageofheroes-round-draw = Beide kanten gelijk op { $total }. Geen legers verloren.
ageofheroes-battle-victory-attacker = { $attacker } verslaat { $defender }.
ageofheroes-battle-victory-defender = { $defender } verdedigt succesvol tegen { $attacker }.
ageofheroes-battle-mutual-defeat = Zowel { $attacker } als { $defender } verliezen alle legers.
ageofheroes-general-bonus = +{ $count } van { $count ->
    [one] generaal
    *[other] generaals
}
ageofheroes-fortress-bonus = +{ $count } van fort verdediging
ageofheroes-battle-winner = { $winner } wint het gevecht.
ageofheroes-battle-draw = Het gevecht eindigt in gelijkspel...
ageofheroes-battle-continue = Zet het gevecht voort.
ageofheroes-battle-end = Het gevecht is voorbij.

# War outcomes
ageofheroes-conquest-success = { $attacker } verovert { $count } { $count ->
    [one] stad
    *[other] steden
} van { $defender }.
ageofheroes-plunder-success = { $attacker } plundert { $count } { $count ->
    [one] kaart
    *[other] kaarten
} van { $defender }.
ageofheroes-destruction-success = { $attacker } vernietigt { $count } van { $defender }'s monument { $count ->
    [one] bron
    *[other] bronnen
}.
ageofheroes-army-losses = { $player } verliest { $count } { $count ->
    [one] leger
    *[other] legers
}.
ageofheroes-army-losses-you = Je verliest { $count } { $count ->
    [one] leger
    *[other] legers
}.

# Army return
ageofheroes-army-return-road = Je troepen keren direct terug via de weg.
ageofheroes-army-return-delayed = { $count } { $count ->
    [one] eenheid keert terug
    *[other] eenheden keren terug
} aan het einde van je volgende beurt.
ageofheroes-army-returned = { $player }'s troepen zijn teruggekeerd van oorlog.
ageofheroes-army-returned-you = Je troepen zijn teruggekeerd van oorlog.
ageofheroes-army-recover = { $player }'s legers herstellen van de aardbeving.
ageofheroes-army-recover-you = Je legers herstellen van de aardbeving.

# Olympics
ageofheroes-olympics-cancel = { $player } speelt Olympische Spelen. Oorlog geannuleerd.
ageofheroes-olympics-prompt = { $attacker } heeft oorlog verklaard. Je hebt Olympische Spelen - gebruiken om te annuleren?
ageofheroes-yes = Ja
ageofheroes-no = Nee

# Monument progress
ageofheroes-monument-progress = { $player }'s monument is { $count }/5 voltooid.
ageofheroes-monument-progress-you = Je monument is { $count }/5 voltooid.

# Hand management
ageofheroes-discard-excess = Je hebt meer dan { $max } kaarten. Gooi { $count } { $count ->
    [one] kaart
    *[other] kaarten
} weg.
ageofheroes-discard-excess-other = { $player } moet overtollige kaarten weggooien.
ageofheroes-discard-more = Gooi { $count } meer { $count ->
    [one] kaart
    *[other] kaarten
} weg.

# Victory
ageofheroes-victory-cities = { $player } heeft 5 steden gebouwd! Rijk van Vijf Steden.
ageofheroes-victory-cities-you = Je hebt 5 steden gebouwd! Rijk van Vijf Steden.
ageofheroes-victory-monument = { $player } heeft hun monument voltooid! Dragers van Grote Cultuur.
ageofheroes-victory-monument-you = Je hebt je monument voltooid! Dragers van Grote Cultuur.
ageofheroes-victory-last-standing = { $player } is de laatste overlevende stam! De Meest Volhardende.
ageofheroes-victory-last-standing-you = Je bent de laatste overlevende stam! De Meest Volhardende.
ageofheroes-game-over = Spel Voorbij.

# Elimination
ageofheroes-eliminated = { $player } is geëlimineerd.
ageofheroes-eliminated-you = Je bent geëlimineerd.

# Hand
ageofheroes-hand-empty = Je hebt geen kaarten.
ageofheroes-hand-contents = Je hand ({ $count } { $count ->
    [one] kaart
    *[other] kaarten
}): { $cards }

# Status
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [one] stad
    *[other] steden
}, { $armies } { $armies ->
    [one] leger
    *[other] legers
}, { $monument }/5 monument
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = Steden: { $count }
ageofheroes-status-armies = Legers: { $count }
ageofheroes-status-generals = Generaals: { $count }
ageofheroes-status-fortresses = Forten: { $count }
ageofheroes-status-monument = Monument: { $count }/5
ageofheroes-status-roads = Wegen: { $left }{ $right }
ageofheroes-status-road-left = links
ageofheroes-status-road-right = rechts
ageofheroes-status-none = geen
ageofheroes-status-earthquake-armies = Herstellende legers: { $count }
ageofheroes-status-returning-armies = Terugkerende legers: { $count }
ageofheroes-status-returning-generals = Terugkerende generaals: { $count }

# Deck info
ageofheroes-deck-empty = Geen { $card } kaarten meer in het deck.
ageofheroes-deck-count = Resterende kaarten: { $count }
ageofheroes-deck-reshuffled = De aflegstapel is opnieuw geschud in het deck.

# Give up
ageofheroes-give-up-confirm = Weet je zeker dat je wilt opgeven?
ageofheroes-gave-up = { $player } gaf op!
ageofheroes-gave-up-you = Je gaf op!

# Hero card
ageofheroes-hero-use = Gebruik als leger of generaal?
ageofheroes-hero-army = Leger
ageofheroes-hero-general = Generaal

# Fortune card
ageofheroes-fortune-reroll = { $player } gebruikt Fortuin om opnieuw te gooien.
ageofheroes-fortune-prompt = Je verloor de worp. Fortuin gebruiken om opnieuw te gooien?

# Disabled action reasons
ageofheroes-not-your-turn = Het is niet jouw beurt.
ageofheroes-game-not-started = Het spel is nog niet begonnen.
ageofheroes-wrong-phase = Deze actie is niet beschikbaar in de huidige fase.
ageofheroes-no-resources = Je hebt de vereiste bronnen niet.

# Building costs (for display)
ageofheroes-cost-army = 2 Graan, IJzer
ageofheroes-cost-fortress = IJzer, Hout, Steen
ageofheroes-cost-general = IJzer, Goud
ageofheroes-cost-road = 2 Steen
ageofheroes-cost-city = 2 Hout, Steen
