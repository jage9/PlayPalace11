# Age of Heroes game messages
# A civilization-building card game for 2-6 players

# Game name
game-name-ageofheroes = Епоха Героїв

# Tribes
ageofheroes-tribe-egyptians = Єгиптяни
ageofheroes-tribe-romans = Римляни
ageofheroes-tribe-greeks = Греки
ageofheroes-tribe-babylonians = Вавилоняни
ageofheroes-tribe-celts = Кельти
ageofheroes-tribe-chinese = Китайці

# Special Resources (for monuments)
ageofheroes-special-limestone = Вапняк
ageofheroes-special-concrete = Бетон
ageofheroes-special-marble = Мармур
ageofheroes-special-bricks = Цегла
ageofheroes-special-sandstone = Пісковик
ageofheroes-special-granite = Граніт

# Standard Resources
ageofheroes-resource-iron = Залізо
ageofheroes-resource-wood = Деревина
ageofheroes-resource-grain = Зерно
ageofheroes-resource-stone = Камінь
ageofheroes-resource-gold = Золото

# Events
ageofheroes-event-population-growth = Зростання населення
ageofheroes-event-earthquake = Землетрус
ageofheroes-event-eruption = Виверження
ageofheroes-event-hunger = Голод
ageofheroes-event-barbarians = Варвари
ageofheroes-event-olympics = Олімпійські ігри
ageofheroes-event-hero = Герой
ageofheroes-event-fortune = Удача

# Buildings
ageofheroes-building-army = Армія
ageofheroes-building-fortress = Фортеця
ageofheroes-building-general = Генерал
ageofheroes-building-road = Дорога
ageofheroes-building-city = Місто

# Actions
ageofheroes-action-tax-collection = Збір податків
ageofheroes-action-construction = Будівництво
ageofheroes-action-war = Війна
ageofheroes-action-do-nothing = Нічого не робити
ageofheroes-play = Грати

# War goals
ageofheroes-war-conquest = Завоювання
ageofheroes-war-plunder = Пограбування
ageofheroes-war-destruction = Руйнування

# Game options
ageofheroes-set-victory-cities = Міст для перемоги: { $cities }
ageofheroes-enter-victory-cities = Введіть кількість міст для перемоги (3-7)
ageofheroes-set-victory-monument = Завершення пам'ятника: { $progress }%
ageofheroes-toggle-neighbor-roads = Дороги тільки до сусідів: { $enabled }
ageofheroes-set-max-hand = Максимальний розмір руки: { $cards } карт

# Option change announcements
ageofheroes-option-changed-victory-cities = Для перемоги потрібно { $cities } міст.
ageofheroes-option-changed-victory-monument = Поріг завершення пам'ятника встановлено на { $progress }%.
ageofheroes-option-changed-neighbor-roads = Дороги тільки до сусідів { $enabled }.
ageofheroes-option-changed-max-hand = Максимальний розмір руки встановлено на { $cards } карт.

# Setup phase
ageofheroes-setup-start = Ви лідер племені { $tribe }. Ваш спеціальний ресурс пам'ятника - { $special }. Киньте кубики, щоб визначити порядок ходів.
ageofheroes-setup-viewer = Гравці кидають кубики, щоб визначити порядок ходів.
ageofheroes-roll-dice = Кинути кубики
ageofheroes-war-roll-dice = Кинути кубики
ageofheroes-dice-result = Ви кинули { $total } ({ $die1 } + { $die2 }).
ageofheroes-dice-result-other = { $player } кинув { $total }.
ageofheroes-dice-tie = Кілька гравців отримали { $total }. Кидаємо знову...
ageofheroes-first-player = { $player } кинув найбільше з { $total } і ходить першим.
ageofheroes-first-player-you = З { $total } очками ви ходите першим.

# Preparation phase
ageofheroes-prepare-start = Гравці повинні зіграти карти подій і скинути лиха.
ageofheroes-prepare-your-turn = У вас є { $count } { $count ->
    [one] карта
    *[other] карт
} для гри або скидання.
ageofheroes-prepare-done = Фаза підготовки завершена.

# Events played/discarded
ageofheroes-population-growth = { $player } грає Зростання населення і будує нове місто.
ageofheroes-population-growth-you = Ви граєте Зростання населення і будуєте нове місто.
ageofheroes-discard-card = { $player } скидає { $card }.
ageofheroes-discard-card-you = Ви скидаєте { $card }.
ageofheroes-earthquake = Землетрус вдаряє по племені { $player }; їхні армії відновлюються.
ageofheroes-earthquake-you = Землетрус вдаряє по вашому племені; ваші армії відновлюються.
ageofheroes-eruption = Виверження знищує одне з міст { $player }.
ageofheroes-eruption-you = Виверження знищує одне з ваших міст.

# Disaster effects
ageofheroes-hunger-strikes = Голод наступає.
ageofheroes-lose-card-hunger = Ви втрачаєте { $card }.
ageofheroes-barbarians-pillage = Варвари атакують ресурси { $player }.
ageofheroes-barbarians-attack = Варвари атакують ресурси { $player }.
ageofheroes-barbarians-attack-you = Варвари атакують ваші ресурси.
ageofheroes-lose-card-barbarians = Ви втрачаєте { $card }.
ageofheroes-block-with-card = { $player } блокує лихо за допомогою { $card }.
ageofheroes-block-with-card-you = Ви блокуєте лихо за допомогою { $card }.

# Targeted disaster cards (Earthquake/Eruption)
ageofheroes-select-disaster-target = Виберіть ціль для { $card }.
ageofheroes-no-targets = Немає доступних цілей.
ageofheroes-earthquake-strikes-you = { $attacker } грає Землетрус проти вас. Ваші армії вимкнені.
ageofheroes-earthquake-strikes = { $attacker } грає Землетрус проти { $player }.
ageofheroes-armies-disabled = { $count } { $count ->
    [one] армія вимкнена
    *[other] армій вимкнено
} на один хід.
ageofheroes-eruption-strikes-you = { $attacker } грає Виверження проти вас. Одне з ваших міст знищено.
ageofheroes-eruption-strikes = { $attacker } грає Виверження проти { $player }.
ageofheroes-city-destroyed = Місто знищене виверженням.

# Fair phase
ageofheroes-fair-start = Світає день на ринку.
ageofheroes-fair-draw-base = Ви берете { $count } { $count ->
    [one] карту
    *[other] карт
}.
ageofheroes-fair-draw-roads = Ви берете { $count } додаткових { $count ->
    [one] карту
    *[other] карт
} завдяки вашій дорожній мережі.
ageofheroes-fair-draw-other = { $player } бере { $count } { $count ->
    [one] карту
    *[other] карт
}.

# Trading/Auction
ageofheroes-auction-start = Торги починаються.
ageofheroes-offer-trade = Запропонувати обмін
ageofheroes-offer-made = { $player } пропонує { $card } за { $wanted }.
ageofheroes-offer-made-you = Ви пропонуєте { $card } за { $wanted }.
ageofheroes-trade-accepted = { $player } приймає пропозицію { $other } і обмінює { $give } на { $receive }.
ageofheroes-trade-accepted-you = Ви приймаєте пропозицію { $other } і отримуєте { $receive }.
ageofheroes-trade-cancelled = { $player } відкликає свою пропозицію для { $card }.
ageofheroes-trade-cancelled-you = Ви відкликаєте свою пропозицію для { $card }.
ageofheroes-stop-trading = Припинити торгівлю
ageofheroes-select-request = Ви пропонуєте { $card }. Що ви хочете натомість?
ageofheroes-cancel = Скасувати
ageofheroes-left-auction = { $player } йде.
ageofheroes-left-auction-you = Ви йдете з ринку.
ageofheroes-any-card = Будь-яка карта
ageofheroes-cannot-trade-own-special = Ви не можете обміняти свій власний спеціальний ресурс пам'ятника.
ageofheroes-resource-not-in-game = Цей спеціальний ресурс не використовується в цій грі.

# Main play phase
ageofheroes-play-start = Фаза гри.
ageofheroes-day = День { $day }
ageofheroes-draw-card = { $player } бере карту з колоди.
ageofheroes-draw-card-you = Ви берете { $card } з колоди.
ageofheroes-your-action = Що ви хочете зробити?

# Tax Collection
ageofheroes-tax-collection = { $player } обирає Збір податків: { $cities } { $cities ->
    [one] місто
    *[other] міст
} збирає { $cards } { $cards ->
    [one] карту
    *[other] карт
}.
ageofheroes-tax-collection-you = Ви обираєте Збір податків: { $cities } { $cities ->
    [one] місто
    *[other] міст
} збирає { $cards } { $cards ->
    [one] карту
    *[other] карт
}.
ageofheroes-tax-no-city = Збір податків: У вас немає міст, що вижили. Скиньте карту, щоб взяти нову.
ageofheroes-tax-no-city-done = { $player } обирає Збір податків, але не має міст, тому обмінює карту.
ageofheroes-tax-no-city-done-you = Збір податків: Ви обміняли { $card } на нову карту.

# Construction
ageofheroes-construction-menu = Що ви хочете побудувати?
ageofheroes-construction-done = { $player } побудував { $article } { $building }.
ageofheroes-construction-done-you = Ви побудували { $article } { $building }.
ageofheroes-construction-stop = Припинити будівництво
ageofheroes-construction-stopped = Ви вирішили припинити будівництво.
ageofheroes-road-select-neighbor = Виберіть, до якого сусіда побудувати дорогу.
ageofheroes-direction-left = Ліворуч від вас
ageofheroes-direction-right = Праворуч від вас
ageofheroes-road-request-sent = Запит на дорогу надіслано. Очікуємо схвалення сусіда.
ageofheroes-road-request-received = { $requester } просить дозволу побудувати дорогу до вашого племені.
ageofheroes-road-request-denied-you = Ви відхилили запит на дорогу.
ageofheroes-road-request-denied = { $denier } відхилив ваш запит на дорогу.
ageofheroes-road-built = { $tribe1 } і { $tribe2 } тепер з'єднані дорогою.
ageofheroes-road-no-target = Немає сусідніх племен для будівництва дороги.
ageofheroes-approve = Схвалити
ageofheroes-deny = Відхилити
ageofheroes-supply-exhausted = Більше немає { $building } для будівництва.

# Do Nothing
ageofheroes-do-nothing = { $player } пасує.
ageofheroes-do-nothing-you = Ви пасуєте...

# War
ageofheroes-war-declare = { $attacker } оголошує війну { $defender }. Мета: { $goal }.
ageofheroes-war-prepare = Виберіть свої армії для { $action }.
ageofheroes-war-no-army = У вас немає армій або карт героїв.
ageofheroes-war-no-targets = Немає дійсних цілей для війни.
ageofheroes-war-no-valid-goal = Немає дійсних цілей війни проти цієї цілі.
ageofheroes-war-select-target = Виберіть, якого гравця атакувати.
ageofheroes-war-select-goal = Виберіть вашу мету війни.
ageofheroes-war-prepare-attack = Виберіть ваші атакуючі сили.
ageofheroes-war-prepare-defense = { $attacker } атакує вас; Виберіть ваші захисні сили.
ageofheroes-war-select-armies = Виберіть армії: { $count }
ageofheroes-war-select-generals = Виберіть генералів: { $count }
ageofheroes-war-select-heroes = Виберіть героїв: { $count }
ageofheroes-war-attack = Атакувати...
ageofheroes-war-defend = Захищати...
ageofheroes-war-prepared = Ваші сили: { $armies } { $armies ->
    [one] армія
    *[other] армій
}{ $generals ->
    [0] {""}
    [one] {" і 1 генерал"}
    *[other] {" і { $generals } генералів"}
}{ $heroes ->
    [0] {""}
    [one] {" і 1 герой"}
    *[other] {" і { $heroes } героїв"}
}.
ageofheroes-war-roll-you = Ви кидаєте { $roll }.
ageofheroes-war-roll-other = { $player } кидає { $roll }.
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [1] {"+1 від фортеці = { $total } всього"}
            *[other] {"+{ $fortress } від фортець = { $total } всього"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"+{ $general } від генерала = { $total } всього"}
            [1] {"+{ $general } від генерала, +1 від фортеці = { $total } всього"}
            *[other] {"+{ $general } від генерала, +{ $fortress } від фортець = { $total } всього"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [1] {"{ $player }: +1 від фортеці = { $total } всього"}
            *[other] {"{ $player }: +{ $fortress } від фортець = { $total } всього"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } від генерала = { $total } всього"}
            [1] {"{ $player }: +{ $general } від генерала, +1 від фортеці = { $total } всього"}
            *[other] {"{ $player }: +{ $general } від генерала, +{ $fortress } від фортець = { $total } всього"}
        }
    }
}

# Battle
ageofheroes-battle-start = Битва починається. { $attacker }: { $att_armies } { $att_armies ->
    [one] армія
    *[other] армій
} проти { $defender }: { $def_armies } { $def_armies ->
    [one] армія
    *[other] армій
}.
ageofheroes-dice-roll-detailed = { $name } кидає { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } від генерала" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 від фортеці" }
    *[other] { " + { $fortress } від фортець" }
} = { $total }.
ageofheroes-dice-roll-detailed-you = Ви кидаєте { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } від генерала" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 від фортеці" }
    *[other] { " + { $fortress } від фортець" }
} = { $total }.
ageofheroes-round-attacker-wins = { $attacker } перемагає в раунді ({ $att_total } проти { $def_total }). { $defender } втрачає армію.
ageofheroes-round-defender-wins = { $defender } успішно захищається ({ $def_total } проти { $att_total }). { $attacker } втрачає армію.
ageofheroes-round-draw = Обидві сторони нічия з { $total }. Армії не втрачено.
ageofheroes-battle-victory-attacker = { $attacker } перемагає { $defender }.
ageofheroes-battle-victory-defender = { $defender } успішно захищається проти { $attacker }.
ageofheroes-battle-mutual-defeat = І { $attacker }, і { $defender } втрачають всі армії.
ageofheroes-general-bonus = +{ $count } від { $count ->
    [one] генерала
    *[other] генералів
}
ageofheroes-fortress-bonus = +{ $count } від захисту фортеці
ageofheroes-battle-winner = { $winner } вигравує битву.
ageofheroes-battle-draw = Битва закінчується внічию...
ageofheroes-battle-continue = Продовжити битву.
ageofheroes-battle-end = Битва закінчена.

# War outcomes
ageofheroes-conquest-success = { $attacker } завойовує { $count } { $count ->
    [one] місто
    *[other] міст
} у { $defender }.
ageofheroes-plunder-success = { $attacker } грабує { $count } { $count ->
    [one] карту
    *[other] карт
} у { $defender }.
ageofheroes-destruction-success = { $attacker } знищує { $count } ресурсів пам'ятника { $defender } { $count ->
    [one] ресурс
    *[other] ресурсів
}.
ageofheroes-army-losses = { $player } втрачає { $count } { $count ->
    [one] армію
    *[other] армій
}.
ageofheroes-army-losses-you = Ви втрачаєте { $count } { $count ->
    [one] армію
    *[other] армій
}.

# Army return
ageofheroes-army-return-road = Ваші війська повертаються негайно дорогою.
ageofheroes-army-return-delayed = { $count } { $count ->
    [one] підрозділ повертається
    *[other] підрозділів повертаються
} в кінці вашого наступного ходу.
ageofheroes-army-returned = Війська { $player } повернулися з війни.
ageofheroes-army-returned-you = Ваші війська повернулися з війни.
ageofheroes-army-recover = Армії { $player } відновлюються після землетрусу.
ageofheroes-army-recover-you = Ваші армії відновлюються після землетрусу.

# Olympics
ageofheroes-olympics-cancel = { $player } грає Олімпійські ігри. Війна скасована.
ageofheroes-olympics-prompt = { $attacker } оголосив війну. У вас є Олімпійські ігри - використати для скасування?
ageofheroes-yes = Так
ageofheroes-no = Ні

# Monument progress
ageofheroes-monument-progress = Пам'ятник { $player } завершено на { $count }/5.
ageofheroes-monument-progress-you = Ваш пам'ятник завершено на { $count }/5.

# Hand management
ageofheroes-discard-excess = У вас більше { $max } карт. Скиньте { $count } { $count ->
    [one] карту
    *[other] карт
}.
ageofheroes-discard-excess-other = { $player } повинен скинути зайві карти.
ageofheroes-discard-more = Скиньте ще { $count } { $count ->
    [one] карту
    *[other] карт
}.

# Victory
ageofheroes-victory-cities = { $player } побудував 5 міст! Імперія п'яти міст.
ageofheroes-victory-cities-you = Ви побудували 5 міст! Імперія п'яти міст.
ageofheroes-victory-monument = { $player } завершив свій пам'ятник! Носії великої культури.
ageofheroes-victory-monument-you = Ви завершили свій пам'ятник! Носії великої культури.
ageofheroes-victory-last-standing = { $player } - останнє племе, що залишилося! Найбільш наполегливий.
ageofheroes-victory-last-standing-you = Ви останнє племе, що залишилося! Найбільш наполегливий.
ageofheroes-game-over = Гра закінчена.

# Elimination
ageofheroes-eliminated = { $player } вибув з гри.
ageofheroes-eliminated-you = Ви вибули з гри.

# Hand
ageofheroes-hand-empty = У вас немає карт.
ageofheroes-hand-contents = Ваша рука ({ $count } { $count ->
    [one] карта
    *[other] карт
}): { $cards }

# Status
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [one] місто
    *[other] міст
}, { $armies } { $armies ->
    [one] армія
    *[other] армій
}, { $monument }/5 пам'ятник
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = Міста: { $count }
ageofheroes-status-armies = Армії: { $count }
ageofheroes-status-generals = Генерали: { $count }
ageofheroes-status-fortresses = Фортеці: { $count }
ageofheroes-status-monument = Пам'ятник: { $count }/5
ageofheroes-status-roads = Дороги: { $left }{ $right }
ageofheroes-status-road-left = ліворуч
ageofheroes-status-road-right = праворуч
ageofheroes-status-none = немає
ageofheroes-status-earthquake-armies = Армії, що відновлюються: { $count }
ageofheroes-status-returning-armies = Армії, що повертаються: { $count }
ageofheroes-status-returning-generals = Генерали, що повертаються: { $count }

# Deck info
ageofheroes-deck-empty = Більше немає карт { $card } в колоді.
ageofheroes-deck-count = Карт залишилося: { $count }
ageofheroes-deck-reshuffled = Скинуту колоду перетасовано назад в колоду.

# Give up
ageofheroes-give-up-confirm = Ви впевнені, що хочете здатися?
ageofheroes-gave-up = { $player } здався!
ageofheroes-gave-up-you = Ви здалися!

# Hero card
ageofheroes-hero-use = Використати як армію чи генерала?
ageofheroes-hero-army = Армія
ageofheroes-hero-general = Генерал

# Fortune card
ageofheroes-fortune-reroll = { $player } використовує Удачу для перекидання.
ageofheroes-fortune-prompt = Ви програли кидок. Використати Удачу для перекидання?

# Disabled action reasons
ageofheroes-not-your-turn = Зараз не ваш хід.
ageofheroes-game-not-started = Гра ще не почалася.
ageofheroes-wrong-phase = Ця дія недоступна в поточній фазі.
ageofheroes-no-resources = У вас немає необхідних ресурсів.

# Building costs (for display)
ageofheroes-cost-army = 2 Зерно, Залізо
ageofheroes-cost-fortress = Залізо, Деревина, Камінь
ageofheroes-cost-general = Залізо, Золото
ageofheroes-cost-road = 2 Камінь
ageofheroes-cost-city = 2 Деревина, Камінь
