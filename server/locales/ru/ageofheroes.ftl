# Age of Heroes game messages
# A civilization-building card game for 2-6 players

# Game name
game-name-ageofheroes = Эпоха героев

# Tribes
ageofheroes-tribe-egyptians = Египтяне
ageofheroes-tribe-romans = Римляне
ageofheroes-tribe-greeks = Греки
ageofheroes-tribe-babylonians = Вавилоняне
ageofheroes-tribe-celts = Кельты
ageofheroes-tribe-chinese = Китайцы

# Special Resources (for monuments)
ageofheroes-special-limestone = Известняк
ageofheroes-special-concrete = Бетон
ageofheroes-special-marble = Мрамор
ageofheroes-special-bricks = Кирпичи
ageofheroes-special-sandstone = Песчаник
ageofheroes-special-granite = Гранит

# Standard Resources
ageofheroes-resource-iron = Железо
ageofheroes-resource-wood = Дерево
ageofheroes-resource-grain = Зерно
ageofheroes-resource-stone = Камень
ageofheroes-resource-gold = Золото

# Events
ageofheroes-event-population-growth = Прирост населения
ageofheroes-event-earthquake = Землетрясение
ageofheroes-event-eruption = Извержение
ageofheroes-event-hunger = Голод
ageofheroes-event-barbarians = Варвары
ageofheroes-event-olympics = Олимпийские игры
ageofheroes-event-hero = Герой
ageofheroes-event-fortune = Удача

# Buildings
ageofheroes-building-army = Армия
ageofheroes-building-fortress = Крепость
ageofheroes-building-general = Генерал
ageofheroes-building-road = Дорога
ageofheroes-building-city = Город

# Actions
ageofheroes-action-tax-collection = Сбор налогов
ageofheroes-action-construction = Строительство
ageofheroes-action-war = Война
ageofheroes-action-do-nothing = Ничего не делать
ageofheroes-play = Играть

# War goals
ageofheroes-war-conquest = Завоевание
ageofheroes-war-plunder = Разграбление
ageofheroes-war-destruction = Разрушение

# Game options
ageofheroes-set-victory-cities = Городов для победы: { $cities }
ageofheroes-enter-victory-cities = Введите число городов для победы (3-7)
ageofheroes-set-victory-monument = Завершение памятника: { $progress }%
ageofheroes-toggle-neighbor-roads = Дороги только к соседям: { $enabled }
ageofheroes-set-max-hand = Макс. карт в руке: { $cards }

# Option change announcements
ageofheroes-option-changed-victory-cities = Для победы требуется { $cities } { $cities ->
    [one] город
    [few] города
    *[other] городов
}.
ageofheroes-option-changed-victory-monument = Порог завершения памятника установлен на { $progress }%.
ageofheroes-option-changed-neighbor-roads = Дороги только к соседям: { $enabled }.
ageofheroes-option-changed-max-hand = Максимальный размер руки: { $cards } { $cards ->
    [one] карта
    [few] карты
    *[other] карт
}.

# Setup phase
ageofheroes-setup-start = Вы — вождь племени { $tribe }. Ваш особый ресурс памятника — { $special }. Бросьте кубики, чтобы определить очерёдность ходов.
ageofheroes-setup-viewer = Игроки бросают кубики, чтобы определить очерёдность ходов.
ageofheroes-roll-dice = Бросить кубики
ageofheroes-war-roll-dice = Бросить кубики
ageofheroes-dice-result = Вы выбросили { $total } ({ $die1 } + { $die2 }).
ageofheroes-dice-result-other = { $player } выбрасывает { $total }.
ageofheroes-dice-tie = Сразу несколько игроков выбросили { $total }. Перебрасываем...
ageofheroes-first-player = { $player } выбрасывает { $total } (больше всех) и ходит первым.
ageofheroes-first-player-you = Набрав { $total } { $total ->
    [one] очко
    [few] очка
    *[other] очков
}, вы ходите первым.

# Preparation phase
ageofheroes-prepare-start = Игроки должны разыграть карты событий и сбросить бедствия.
ageofheroes-prepare-your-turn = У вас { $count } { $count ->
    [one] карта
    [few] карты
    *[other] карт
} для розыгрыша или сброса.
ageofheroes-prepare-done = Фаза подготовки завершена.

# Events played/discarded
ageofheroes-population-growth = { $player } разыгрывает «Прирост населения» и строит новый город.
ageofheroes-population-growth-you = Вы разыгрываете «Прирост населения» и строите новый город.
ageofheroes-discard-card = { $player } сбрасывает карту: { $card }.
ageofheroes-discard-card-you = Вы сбрасываете карту: { $card }.
ageofheroes-earthquake = Землетрясение поражает племя { $player }; его армии восстанавливаются.
ageofheroes-earthquake-you = Землетрясение поражает ваше племя; ваши армии восстанавливаются.
ageofheroes-eruption = Извержение разрушает один из городов игрока { $player }.
ageofheroes-eruption-you = Извержение разрушает один из ваших городов.

# Disaster effects
ageofheroes-hunger-strikes = Наступил голод.
ageofheroes-lose-card-hunger = Вы теряете карту: { $card }.
ageofheroes-barbarians-pillage = Варвары грабят ресурсы игрока { $player }.
ageofheroes-barbarians-attack = Варвары атакуют ресурсы игрока { $player }.
ageofheroes-barbarians-attack-you = Варвары атакуют ваши ресурсы.
ageofheroes-lose-card-barbarians = Вы теряете карту: { $card }.
ageofheroes-block-with-card = { $player } блокирует бедствие, используя карту { $card }.
ageofheroes-block-with-card-you = Вы блокируете бедствие, используя карту { $card }.

# Targeted disaster cards (Earthquake/Eruption)
ageofheroes-select-disaster-target = Выберите цель для карты { $card }.
ageofheroes-no-targets = Нет доступных целей.
ageofheroes-earthquake-strikes-you = { $attacker } разыгрывает «Землетрясение» против вас. Ваши армии выведены из строя.
ageofheroes-earthquake-strikes = { $attacker } разыгрывает «Землетрясение» против игрока { $player }.
ageofheroes-armies-disabled = { $count } { $count ->
    [one] армия выведена
    [few] армии выведены
    *[other] армий выведены
} из строя на один ход.
ageofheroes-eruption-strikes-you = { $attacker } разыгрывает «Извержение» против вас. Один из ваших городов разрушен.
ageofheroes-eruption-strikes = { $attacker } разыгрывает «Извержение» против игрока { $player }.
ageofheroes-city-destroyed = Город разрушен извержением.

# Fair phase
ageofheroes-fair-start = На ярмарке наступает утро.
ageofheroes-fair-draw-base = Вы берёте { $count } { $count ->
    [one] карту
    [few] карты
    *[other] карт
}.
ageofheroes-fair-draw-roads = Вы берёте ещё { $count } { $count ->
    [one] карту
    [few] карты
    *[other] карт
} благодаря вашей сети дорог.
ageofheroes-fair-draw-other = { $player } берёт { $count } { $count ->
    [one] карту
    [few] карты
    *[other] карт
}.

# Trading/Auction
ageofheroes-auction-start = Торги начинаются.
ageofheroes-offer-trade = Предложить обмен
ageofheroes-offer-made = { $player } предлагает { $card } в обмен на { $wanted }.
ageofheroes-offer-made-you = Вы предлагаете { $card } в обмен на { $wanted }.
ageofheroes-trade-accepted = { $player } принимает предложение игрока { $other } и меняет { $give } на { $receive }.
ageofheroes-trade-accepted-you = Вы принимаете предложение игрока { $other } и получаете { $receive }.
ageofheroes-trade-cancelled = { $player } отзывает своё предложение по карте { $card }.
ageofheroes-trade-cancelled-you = Вы отзываете своё предложение по карте { $card }.
ageofheroes-stop-trading = Закончить торговлю
ageofheroes-select-request = Вы предлагаете карту { $card }. Что вы хотите взамен?
ageofheroes-cancel = Отмена
ageofheroes-left-auction = { $player } уходит с ярмарки.
ageofheroes-left-auction-you = Вы покидаете ярмарку.
ageofheroes-any-card = Любая карта
ageofheroes-cannot-trade-own-special = Вы не можете обменивать свой собственный особый ресурс памятника.
ageofheroes-resource-not-in-game = Этот особый ресурс не используется в текущей игре.

# Main play phase
ageofheroes-play-start = Фаза игры.
ageofheroes-day = День { $day }
ageofheroes-draw-card = { $player } берёт карту из колоды.
ageofheroes-draw-card-you = Вы берёте карту из колоды: { $card }.
ageofheroes-your-action = Что вы хотите сделать?

# Tax Collection
ageofheroes-tax-collection = { $player } выбирает сбор налогов: { $cities } { $cities ->
    [one] город приносит
    [few] города приносят
    *[other] городов приносят
} { $cards } { $cards ->
    [one] карту
    [few] карты
    *[other] карт
}.
ageofheroes-tax-collection-you = Сбор налогов: { $cities } { $cities ->
    [one] город приносит
    [few] города приносят
    *[other] городов приносят
} { $cards } { $cards ->
    [one] карту
    [few] карты
    *[other] карт
}.
ageofheroes-tax-no-city = Сбор налогов: у вас не осталось городов. Сбросьте карту, чтобы взять новую.
ageofheroes-tax-no-city-done = { $player } выбирает сбор налогов, но у него нет городов, поэтому он меняет карту.
ageofheroes-tax-no-city-done-you = Сбор налогов: вы обменяли карту { $card } на новую.

# Construction
ageofheroes-construction-menu = Что вы хотите построить?
ageofheroes-construction-done = { $player } строит: { $building }.
ageofheroes-construction-done-you = Вы построили: { $building }.
ageofheroes-construction-stop = Прекратить строительство
ageofheroes-construction-stopped = Вы решили прекратить строительство.
ageofheroes-road-select-neighbor = Выберите соседа, к которому хотите проложить дорогу.
ageofheroes-direction-left = Слева от вас
ageofheroes-direction-right = Справа от вас
ageofheroes-road-request-sent = Запрос на строительство дороги отправлен. Ожидание одобрения соседа...
ageofheroes-road-request-received = { $requester } запрашивает разрешение проложить дорогу к вашему племени.
ageofheroes-road-request-denied-you = Вы отклонили запрос на строительство дороги.
ageofheroes-road-request-denied = { $denier } отклонил ваш запрос на строительство дороги.
ageofheroes-road-built = { $tribe1 } и { $tribe2 } теперь соединены дорогой.
ageofheroes-road-no-target = Нет соседних племён для строительства дороги.
ageofheroes-approve = Одобрить
ageofheroes-deny = Отклонить
ageofheroes-supply-exhausted = Больше нельзя построить объект типа «{ $building }» (закончились запасы).

# Do Nothing
ageofheroes-do-nothing = { $player } пасует.
ageofheroes-do-nothing-you = Вы пасуете...

# War
ageofheroes-war-declare = { $attacker } объявляет войну игроку { $defender }. Цель: { $goal }.
ageofheroes-war-prepare = Выберите свои армии для действия: { $action }.
ageofheroes-war-no-army = У вас нет доступных армий или карт героев.
ageofheroes-war-no-targets = Нет подходящих целей для войны.
ageofheroes-war-no-valid-goal = Против этой цели нет доступных военных задач.
ageofheroes-war-select-target = Выберите игрока для атаки.
ageofheroes-war-select-goal = Выберите военную цель.
ageofheroes-war-prepare-attack = Выберите атакующие силы.
ageofheroes-war-prepare-defense = { $attacker } атакует вас! Выберите силы обороны.
ageofheroes-war-select-armies = Выберите армии: { $count }
ageofheroes-war-select-generals = Выберите генералов: { $count }
ageofheroes-war-select-heroes = Выберите героев: { $count }
ageofheroes-war-attack = В атаку...
ageofheroes-war-defend = В оборону...
ageofheroes-war-prepared = Ваши силы: { $armies } { $armies ->
    [one] армия
    [few] армии
    *[other] армий
}{ $generals ->
    [0] {""}
    [one] {" и 1 генерал"}
    [few] {" и { $generals } генерала"}
    *[other] {" и { $generals } генералов"}
}{ $heroes ->
    [0] {""}
    [one] {" и 1 герой"}
    [few] {" и { $heroes } героя"}
    *[other] {" и { $heroes } героев"}
}.
ageofheroes-war-roll-you = Вы выбросили { $roll }.
ageofheroes-war-roll-other = { $player } выбрасывает { $roll }.
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [1] {"+1 от крепости = итого { $total }"}
            *[other] {"+{ $fortress } от крепостей = итого { $total }"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"+{ $general } от генерала = итого { $total }"}
            [1] {"+{ $general } от генерала, +1 от крепости = итого { $total }"}
            *[other] {"+{ $general } от генерала, +{ $fortress } от крепостей = итого { $total }"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [1] {"{ $player }: +1 от крепости = итого { $total }"}
            *[other] {"{ $player }: +{ $fortress } от крепостей = итого { $total }"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } от генерала = итого { $total }"}
            [1] {"{ $player }: +{ $general } от генерала, +1 от крепости = итого { $total }"}
            *[other] {"{ $player }: +{ $general } от генерала, +{ $fortress } от крепостей = итого { $total }"}
        }
    }
}

# Battle
ageofheroes-battle-start = Битва начинается. { $att_armies } { $att_armies ->
    [one] армия
    [few] армии
    *[other] армий
} игрока { $attacker } против { $def_armies } { $def_armies ->
    [one] армия
    [few] армии
    *[other] армий
} игрока { $defender }.
ageofheroes-dice-roll-detailed = { $name } выбрасывает { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } от генерала" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 от крепости" }
    *[other] { " + { $fortress } от крепостей" }
} = { $total }.
ageofheroes-dice-roll-detailed-you = Вы выбрасываете { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } от генерала" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 от крепости" }
    *[other] { " + { $fortress } от крепостей" }
} = { $total }.
ageofheroes-round-attacker-wins = { $attacker } побеждает в раунде ({ $att_total } против { $def_total }). { $defender } теряет армию.
ageofheroes-round-defender-wins = { $defender } успешно обороняется ({ $def_total } против { $att_total }). { $attacker } теряет армию.
ageofheroes-round-draw = Ничья: у обоих { $total }. Армии не потеряны.
ageofheroes-battle-victory-attacker = { $attacker } побеждает { $defender }.
ageofheroes-battle-victory-defender = { $defender } успешно отражает атаку игрока { $attacker }.
ageofheroes-battle-mutual-defeat = И { $attacker }, и { $defender } теряют все свои армии.
ageofheroes-general-bonus = +{ $count } от { $count ->
    [one] генерала
    [few] генералов
    *[other] генералов
}
ageofheroes-fortress-bonus = +{ $count } от защиты крепости
ageofheroes-battle-winner = { $winner } побеждает в битве.
ageofheroes-battle-draw = Битва заканчивается вничью...
ageofheroes-battle-continue = Продолжить битву.
ageofheroes-battle-end = Битва окончена.

# War outcomes
ageofheroes-conquest-success = { $attacker } захватывает { $count } { $count ->
    [one] город
    [few] города
    *[other] городов
} у игрока { $defender }.
ageofheroes-plunder-success = { $attacker } грабит { $count } { $count ->
    [one] карту
    [few] карты
    *[other] карт
} у игрока { $defender }.
ageofheroes-destruction-success = { $attacker } разрушает { $count } { $count ->
    [one] ресурс
    [few] ресурса
    *[other] ресурсов
} памятника игрока { $defender }.
ageofheroes-army-losses = { $player } теряет { $count } { $count ->
    [one] армию
    [few] армии
    *[other] армий
}.
ageofheroes-army-losses-you = Вы теряете { $count } { $count ->
    [one] армию
    [few] армии
    *[other] армий
}.

# Army return
ageofheroes-army-return-road = Ваши войска немедленно возвращаются по дороге.
ageofheroes-army-return-delayed = { $count } { $count ->
    [one] армия вернётся
    [few] армии вернутся
    *[other] армий вернутся
} в конце вашего следующего хода.
ageofheroes-army-returned = Войска игрока { $player } вернулись с войны.
ageofheroes-army-returned-you = Ваши войска вернулись с войны.
ageofheroes-army-recover = Армии игрока { $player } восстановились после землетрясения.
ageofheroes-army-recover-you = Ваши армии восстановились после землетрясения.

# Olympics
ageofheroes-olympics-cancel = { $player } разыгрывает «Олимпийские игры». Война отменена.
ageofheroes-olympics-prompt = { $attacker } объявил войну. У вас есть «Олимпийские игры» — использовать их для отмены?
ageofheroes-yes = Да
ageofheroes-no = Нет

# Monument progress
ageofheroes-monument-progress = Памятник игрока { $player } завершён на { $count }/5.
ageofheroes-monument-progress-you = Ваш памятник завершён на { $count }/5.

# Hand management
ageofheroes-discard-excess = У вас больше { $max } карт. Сбросьте { $count } { $count ->
    [one] карту
    [few] карты
    *[other] карт
}.
ageofheroes-discard-excess-other = { $player } должен сбросить лишние карты.
ageofheroes-discard-more = Сбросьте ещё { $count } { $count ->
    [one] карту
    [few] карты
    *[other] карт
}.

# Victory
ageofheroes-victory-cities = { $player } построил 5 городов! Империя Пяти Городов.
ageofheroes-victory-cities-you = Вы построили 5 городов! Империя Пяти Городов.
ageofheroes-victory-monument = { $player } завершил строительство памятника! Носители великой культуры.
ageofheroes-victory-monument-you = Вы завершили строительство своего памятника! Носители великой культуры.
ageofheroes-victory-last-standing = { $player } — последнее уцелевшее племя! Самый стойкий.
ageofheroes-victory-last-standing-you = Вы — последнее уцелевшее племя! Самый стойкий.
ageofheroes-game-over = Игра окончена.

# Elimination
ageofheroes-eliminated = Игрок { $player } выбывает из игры.
ageofheroes-eliminated-you = Вы выбыли из игры.

# Hand
ageofheroes-hand-empty = У вас нет карт.
ageofheroes-hand-contents = Ваша рука ({ $count } { $count ->
    [one] карта
    [few] карты
    *[other] карт
}): { $cards }

# Status
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [one] город
    [few] города
    *[other] городов
}, { $armies } { $armies ->
    [one] армия
    [few] армии
    *[other] армий
}, памятник { $monument }/5
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = Городов: { $count }
ageofheroes-status-armies = Армий: { $count }
ageofheroes-status-generals = Генералов: { $count }
ageofheroes-status-fortresses = Крепостей: { $count }
ageofheroes-status-monument = Памятник: { $count }/5
ageofheroes-status-roads = Дороги: { $left }{ $right }
ageofheroes-status-road-left = слева
ageofheroes-status-road-right = справа
ageofheroes-status-none = нет
ageofheroes-status-earthquake-armies = Восстанавливающиеся армии: { $count }
ageofheroes-status-returning-armies = Возвращающиеся армии: { $count }
ageofheroes-status-returning-generals = Возвращающиеся генералы: { $count }

# Deck info
ageofheroes-deck-empty = В колоде больше нет карт типа «{ $card }».
ageofheroes-deck-count = Карт осталось: { $count }
ageofheroes-deck-reshuffled = Стопка сброса перемешана и возвращена в колоду.

# Give up
ageofheroes-give-up-confirm = Вы уверены, что хотите сдаться?
ageofheroes-gave-up = { $player } сдался!
ageofheroes-gave-up-you = Вы сдались!

# Hero card
ageofheroes-hero-use = Использовать как армию или как генерала?
ageofheroes-hero-army = Армия
ageofheroes-hero-general = Генерал

# Fortune card
ageofheroes-fortune-reroll = { $player } использует «Удачу», чтобы перебросить кубики.
ageofheroes-fortune-prompt = Вы проиграли бросок. Использовать «Удачу», чтобы перебросить?

# Disabled action reasons
ageofheroes-not-your-turn = Сейчас не ваш ход.
ageofheroes-game-not-started = Игра ещё не началась.
ageofheroes-wrong-phase = Это действие недоступно в текущей фазе.
ageofheroes-no-resources = У вас нет необходимых ресурсов.

# Building costs (for display)
ageofheroes-cost-army = 2 Зерна, Железо
ageofheroes-cost-fortress = Железо, Дерево, Камень
ageofheroes-cost-general = Железо, Золото
ageofheroes-cost-road = 2 Камня
ageofheroes-cost-city = 2 Дерева, Камень
