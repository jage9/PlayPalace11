# Age of Heroes game messages
# A civilization-building card game for 2-6 players

# Game name
game-name-ageofheroes = Баатруудын эрин

# Tribes
ageofheroes-tribe-egyptians = Египетчүүд
ageofheroes-tribe-romans = Ромчууд
ageofheroes-tribe-greeks = Грекчүүд
ageofheroes-tribe-babylonians = Вавилончууд
ageofheroes-tribe-celts = Кельтүүд
ageofheroes-tribe-chinese = Хятадууд

# Special Resources (for monuments)
ageofheroes-special-limestone = Шохойн чулуу
ageofheroes-special-concrete = Бетон
ageofheroes-special-marble = Гантиг
ageofheroes-special-bricks = Тоосго
ageofheroes-special-sandstone = Элсэн чулуу
ageofheroes-special-granite = Боржин чулуу

# Standard Resources
ageofheroes-resource-iron = Төмөр
ageofheroes-resource-wood = Мод
ageofheroes-resource-grain = Үр тариа
ageofheroes-resource-stone = Чулуу
ageofheroes-resource-gold = Алт

# Events
ageofheroes-event-population-growth = Хүн амын өсөлт
ageofheroes-event-earthquake = Газар хөдлөлт
ageofheroes-event-eruption = Дэлбэрэлт
ageofheroes-event-hunger = Өлсгөлөн
ageofheroes-event-barbarians = Зэрлэгүүд
ageofheroes-event-olympics = Олимпийн наадам
ageofheroes-event-hero = Баатар
ageofheroes-event-fortune = Аз

# Buildings
ageofheroes-building-army = Арми
ageofheroes-building-fortress = Цайз
ageofheroes-building-general = Генерал
ageofheroes-building-road = Зам
ageofheroes-building-city = Хот

# Actions
ageofheroes-action-tax-collection = Татварын цуглуулга
ageofheroes-action-construction = Барилга
ageofheroes-action-war = Дайн
ageofheroes-action-do-nothing = Юу ч хийхгүй
ageofheroes-play = Тоглох

# War goals
ageofheroes-war-conquest = Эзлэн авалт
ageofheroes-war-plunder = Дээрэм
ageofheroes-war-destruction = Сүйрэл

# Game options
ageofheroes-set-victory-cities = Ялах хотууд: { $cities }
ageofheroes-enter-victory-cities = Хожих хотын тоо оруулах (3-7)
ageofheroes-set-victory-monument = Хөшөө гүйцэтгэл: { $progress }%
ageofheroes-toggle-neighbor-roads = Зөвхөн хөршүүд рүү зам: { $enabled }
ageofheroes-set-max-hand = Хамгийн их хөзөр: { $cards } хөзөр

# Option change announcements
ageofheroes-option-changed-victory-cities = Ялахад { $cities } хот хэрэгтэй.
ageofheroes-option-changed-victory-monument = Хөшөө гүйцэтгэлийн шаардлага { $progress }% болов.
ageofheroes-option-changed-neighbor-roads = Зөвхөн хөршүүд рүү зам { $enabled }.
ageofheroes-option-changed-max-hand = Хамгийн их хөзөр { $cards } хөзөр болов.

# Setup phase
ageofheroes-setup-start = Та { $tribe } овгийн удирдагч. Таны тусгай хөшөө нөөц { $special }. Ээлжийн дарааллыг тогтоохын тулд шоо орхи.
ageofheroes-setup-viewer = Тоглогчид ээлжийн дарааллыг тогтоохоор шоо орхиж байна.
ageofheroes-roll-dice = Шоо орхих
ageofheroes-war-roll-dice = Шоо орхих
ageofheroes-dice-result = Та { $total } орхив ({ $die1 } + { $die2 }).
ageofheroes-dice-result-other = { $player } { $total } орхив.
ageofheroes-dice-tie = Олон тоглогч { $total }-р тэнцсэн. Дахин орхиж байна...
ageofheroes-first-player = { $player } хамгийн өндөр { $total } орхож эхэлнэ.
ageofheroes-first-player-you = { $total } оноогоор та эхэлнэ.

# Preparation phase
ageofheroes-prepare-start = Тоглогчид үйл явдлын хөзөр тоглож, гамшиг хаях ёстой.
ageofheroes-prepare-your-turn = Танд тоглох эсвэл хаях { $count } { $count ->
    [one] хөзөр
    *[other] хөзөр
} байна.
ageofheroes-prepare-done = Бэлтгэл үе шат дууслаа.

# Events played/discarded
ageofheroes-population-growth = { $player } Хүн амын өсөлт тоглож шинэ хот босгов.
ageofheroes-population-growth-you = Та Хүн амын өсөлт тоглож шинэ хот босгов.
ageofheroes-discard-card = { $player } { $card } хаяв.
ageofheroes-discard-card-you = Та { $card } хаяв.
ageofheroes-earthquake = Газар хөдлөлт { $player }-ийн овогт тусаж, армиуд нь нөхөн сэргэж байна.
ageofheroes-earthquake-you = Газар хөдлөлт таны овогт тусаж, таны армиуд нөхөн сэргэж байна.
ageofheroes-eruption = Дэлбэрэлт { $player }-ийн нэг хотыг устгав.
ageofheroes-eruption-you = Дэлбэрэлт таны нэг хотыг устгав.

# Disaster effects
ageofheroes-hunger-strikes = Өлсгөлөн дайрав.
ageofheroes-lose-card-hunger = Та { $card } алдав.
ageofheroes-barbarians-pillage = Зэрлэгүүд { $player }-ийн нөөцийг дайрав.
ageofheroes-barbarians-attack = Зэрлэгүүд { $player }-ийн нөөцийг дайрав.
ageofheroes-barbarians-attack-you = Зэрлэгүүд таны нөөцийг дайрав.
ageofheroes-lose-card-barbarians = Та { $card } алдав.
ageofheroes-block-with-card = { $player } { $card } ашиглан гамшгийг хаав.
ageofheroes-block-with-card-you = Та { $card } ашиглан гамшгийг хаав.

# Targeted disaster cards (Earthquake/Eruption)
ageofheroes-select-disaster-target = { $card }-ийн бай сонгох.
ageofheroes-no-targets = Зохих бай байхгүй.
ageofheroes-earthquake-strikes-you = { $attacker } танд Газар хөдлөлт тоглов. Таны армиуд идэвхгүй болов.
ageofheroes-earthquake-strikes = { $attacker } { $player } дээр Газар хөдлөлт тоглов.
ageofheroes-armies-disabled = { $count } { $count ->
    [one] арми
    *[other] арми
} нэг ээлж идэвхгүй болов.
ageofheroes-eruption-strikes-you = { $attacker } танд Дэлбэрэлт тоглов. Таны нэг хот устлаа.
ageofheroes-eruption-strikes = { $attacker } { $player } дээр Дэлбэрэлт тоглов.
ageofheroes-city-destroyed = Дэлбэрэлтийн улмаас нэг хот устлаа.

# Fair phase
ageofheroes-fair-start = Зах дээр өдөр үүрлээ.
ageofheroes-fair-draw-base = Та { $count } { $count ->
    [one] хөзөр
    *[other] хөзөр
} татлаа.
ageofheroes-fair-draw-roads = Та замын сүлжээний ачаар { $count } нэмэлт { $count ->
    [one] хөзөр
    *[other] хөзөр
} татлаа.
ageofheroes-fair-draw-other = { $player } { $count } { $count ->
    [one] хөзөр
    *[other] хөзөр
} татлаа.

# Trading/Auction
ageofheroes-auction-start = Дуудлага худалдаа эхэллээ.
ageofheroes-offer-trade = Солилцоо санал болгох
ageofheroes-offer-made = { $player } { $wanted }-ийн төлөө { $card } санал болголоо.
ageofheroes-offer-made-you = Та { $wanted }-ийн төлөө { $card } санал болголоо.
ageofheroes-trade-accepted = { $player } { $other }-ийн саналыг хүлээн авч { $give }-г { $receive }-тэй солив.
ageofheroes-trade-accepted-you = Та { $other }-ийн саналыг хүлээн авч { $receive } авлаа.
ageofheroes-trade-cancelled = { $player } { $card }-ийн саналаа цуцлав.
ageofheroes-trade-cancelled-you = Та { $card }-ийн саналаа цуцлав.
ageofheroes-stop-trading = Солилцоо зогсоох
ageofheroes-select-request = Та { $card } санал болгож байна. Хариуд юу хүсч байна?
ageofheroes-cancel = Цуцлах
ageofheroes-left-auction = { $player } явлаа.
ageofheroes-left-auction-you = Та захаас явлаа.
ageofheroes-any-card = Ямар ч хөзөр
ageofheroes-cannot-trade-own-special = Өөрийн тусгай хөшөө нөөцийг солилцож болохгүй.
ageofheroes-resource-not-in-game = Энэ тусгай нөөц энэ тоглоомд ашиглагдахгүй.

# Main play phase
ageofheroes-play-start = Тоглох үе шат.
ageofheroes-day = Өдөр { $day }
ageofheroes-draw-card = { $player } хөзрөөс хөзөр татав.
ageofheroes-draw-card-you = Та хөзрөөс { $card } татлаа.
ageofheroes-your-action = Та юу хийх вэ?

# Tax Collection
ageofheroes-tax-collection = { $player } Татварын цуглуулга сонголоо: { $cities } { $cities ->
    [one] хот
    *[other] хот
} { $cards } { $cards ->
    [one] хөзөр
    *[other] хөзөр
} цуглуулав.
ageofheroes-tax-collection-you = Та Татварын цуглуулга сонголоо: { $cities } { $cities ->
    [one] хот
    *[other] хот
} { $cards } { $cards ->
    [one] хөзөр
    *[other] хөзөр
} цуглуулав.
ageofheroes-tax-no-city = Татварын цуглуулга: Танд амьд хот байхгүй. Шинэ хөзөр татахын тулд нэг хөзөр хая.
ageofheroes-tax-no-city-done = { $player } Татварын цуглуулга сонгосон боловч хот байхгүй тул хөзөр солив.
ageofheroes-tax-no-city-done-you = Татварын цуглуулга: Та { $card }-г шинэ хөзөртэй солив.

# Construction
ageofheroes-construction-menu = Та юу барих вэ?
ageofheroes-construction-done = { $player } { $article } { $building } барив.
ageofheroes-construction-done-you = Та { $article } { $building } барив.
ageofheroes-construction-stop = Барихаа болих
ageofheroes-construction-stopped = Та барихаа больсон.
ageofheroes-road-select-neighbor = Аль хөрш рүү зам барихаа сонго.
ageofheroes-direction-left = Зүүн тал руу
ageofheroes-direction-right = Баруун тал руу
ageofheroes-road-request-sent = Замын хүсэлт илгээгдлээ. Хөршийн зөвшөөрлийг хүлээж байна.
ageofheroes-road-request-received = { $requester } таны овог руу зам барихыг хүсч байна.
ageofheroes-road-request-denied-you = Та замын хүсэлтийг татгалзав.
ageofheroes-road-request-denied = { $denier } таны замын хүсэлтийг татгалзав.
ageofheroes-road-built = { $tribe1 } болон { $tribe2 } одоо замаар холбогдлоо.
ageofheroes-road-no-target = Зам барих хөрш овог байхгүй.
ageofheroes-approve = Зөвшөөрөх
ageofheroes-deny = Татгалзах
ageofheroes-supply-exhausted = { $building } барих нөөц дууслаа.

# Do Nothing
ageofheroes-do-nothing = { $player } өнгөрлөө.
ageofheroes-do-nothing-you = Та өнгөрлөө...

# War
ageofheroes-war-declare = { $attacker } { $defender } дээр дайн зарлав. Зорилго: { $goal }.
ageofheroes-war-prepare = { $action }-д зориулж армиудаа сонго.
ageofheroes-war-no-army = Танд арми эсвэл баатрын хөзөр байхгүй.
ageofheroes-war-no-targets = Дайнд зохих бай байхгүй.
ageofheroes-war-no-valid-goal = Энэ байны эсрэг зохих дайны зорилго байхгүй.
ageofheroes-war-select-target = Дайрах тоглогч сонгох.
ageofheroes-war-select-goal = Дайны зорилгоо сонгох.
ageofheroes-war-prepare-attack = Довтлох хүчээ сонгох.
ageofheroes-war-prepare-defense = { $attacker } танд дайрч байна; Хамгаалах хүчээ сонгох.
ageofheroes-war-select-armies = Арми сонгох: { $count }
ageofheroes-war-select-generals = Генерал сонгох: { $count }
ageofheroes-war-select-heroes = Баатар сонгох: { $count }
ageofheroes-war-attack = Довтлох...
ageofheroes-war-defend = Хамгаалах...
ageofheroes-war-prepared = Таны хүч: { $armies } { $armies ->
    [one] арми
    *[other] арми
}{ $generals ->
    [0] {""}
    [one] {" болон 1 генерал"}
    *[other] {" болон { $generals } генерал"}
}{ $heroes ->
    [0] {""}
    [one] {" болон 1 баатар"}
    *[other] {" болон { $heroes } баатар"}
}.
ageofheroes-war-roll-you = Та { $roll } орхив.
ageofheroes-war-roll-other = { $player } { $roll } орхив.
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"+1 цайзнаас = { $total } нийт"}
            *[other] {"+{ $fortress } цайзнуудаас = { $total } нийт"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"+{ $general } генералаас = { $total } нийт"}
            [one] {"+{ $general } генералаас, +1 цайзнаас = { $total } нийт"}
            *[other] {"+{ $general } генералаас, +{ $fortress } цайзнуудаас = { $total } нийт"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [one] {"{ $player }: +1 цайзнаас = { $total } нийт"}
            *[other] {"{ $player }: +{ $fortress } цайзнуудаас = { $total } нийт"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } генералаас = { $total } нийт"}
            [one] {"{ $player }: +{ $general } генералаас, +1 цайзнаас = { $total } нийт"}
            *[other] {"{ $player }: +{ $general } генералаас, +{ $fortress } цайзнуудаас = { $total } нийт"}
        }
    }
}

# Battle
ageofheroes-battle-start = Тулаан эхэллээ. { $attacker }-ийн { $att_armies } { $att_armies ->
    [one] арми
    *[other] арми
} эсрэг { $defender }-ийн { $def_armies } { $def_armies ->
    [one] арми
    *[other] арми
}.
ageofheroes-dice-roll-detailed = { $name } { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } генералаас" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 цайзнаас" }
    *[other] { " + { $fortress } цайзнуудаас" }
} = { $total } орхив.
ageofheroes-dice-roll-detailed-you = Та { $dice }{ $general ->
    [0] {""}
    *[other] { " + { $general } генералаас" }
}{ $fortress ->
    [0] {""}
    [one] { " + 1 цайзнаас" }
    *[other] { " + { $fortress } цайзнуудаас" }
} = { $total } орхив.
ageofheroes-round-attacker-wins = { $attacker } энэ шатыг хожлоо ({ $att_total } эсрэг { $def_total }). { $defender } нэг арми алдав.
ageofheroes-round-defender-wins = { $defender } амжилттай хамгааллаа ({ $def_total } эсрэг { $att_total }). { $attacker } нэг арми алдав.
ageofheroes-round-draw = Хоёулаа { $total }-р тэнцлээ. Арми алдагдсангүй.
ageofheroes-battle-victory-attacker = { $attacker } { $defender }-г ялав.
ageofheroes-battle-victory-defender = { $defender } { $attacker }-ийн эсрэг амжилттай хамгааллаа.
ageofheroes-battle-mutual-defeat = { $attacker } болон { $defender } хоёулаа бүх армиа алдлаа.
ageofheroes-general-bonus = +{ $count } { $count ->
    [one] генералаас
    *[other] генералуудаас
}
ageofheroes-fortress-bonus = +{ $count } цайзны хамгаалалтаас
ageofheroes-battle-winner = { $winner } тулааныг хожлоо.
ageofheroes-battle-draw = Тулаан тэнцээтэй дууслаа...
ageofheroes-battle-continue = Тулааныг үргэлжлүүлэх.
ageofheroes-battle-end = Тулаан дууслаа.

# War outcomes
ageofheroes-conquest-success = { $attacker } { $defender }-с { $count } { $count ->
    [one] хот
    *[other] хот
} эзэлж авав.
ageofheroes-plunder-success = { $attacker } { $defender }-с { $count } { $count ->
    [one] хөзөр
    *[other] хөзөр
} дээрэмдэв.
ageofheroes-destruction-success = { $attacker } { $defender }-ийн { $count } хөшөө { $count ->
    [one] нөөцийг
    *[other] нөөцийг
} устгав.
ageofheroes-army-losses = { $player } { $count } { $count ->
    [one] арми
    *[other] арми
} алдав.
ageofheroes-army-losses-you = Та { $count } { $count ->
    [one] арми
    *[other] арми
} алдав.

# Army return
ageofheroes-army-return-road = Таны цэргүүд замаар шууд буцаж ирлээ.
ageofheroes-army-return-delayed = { $count } { $count ->
    [one] нэгж
    *[other] нэгж
} дараагийн ээлжийн төгсгөлд буцна.
ageofheroes-army-returned = { $player }-ийн цэргүүд дайнаас буцаж ирлээ.
ageofheroes-army-returned-you = Таны цэргүүд дайнаас буцаж ирлээ.
ageofheroes-army-recover = { $player }-ийн армиуд газар хөдлөлтөөс сэргэлээ.
ageofheroes-army-recover-you = Таны армиуд газар хөдлөлтөөс сэргэлээ.

# Olympics
ageofheroes-olympics-cancel = { $player } Олимпийн наадам тоглов. Дайн цуцлагдлаа.
ageofheroes-olympics-prompt = { $attacker } дайн зарлав. Танд Олимпийн наадам байна - цуцлах уу?
ageofheroes-yes = Тийм
ageofheroes-no = Үгүй

# Monument progress
ageofheroes-monument-progress = { $player }-ийн хөшөө { $count }/5 дууссан.
ageofheroes-monument-progress-you = Таны хөшөө { $count }/5 дууссан.

# Hand management
ageofheroes-discard-excess = Танд { $max } хөзрөөс илүү байна. { $count } { $count ->
    [one] хөзөр
    *[other] хөзөр
} хая.
ageofheroes-discard-excess-other = { $player } илүү хөзрүүдээ хаях ёстой.
ageofheroes-discard-more = { $count } { $count ->
    [one] хөзөр
    *[other] хөзөр
} дахин хая.

# Victory
ageofheroes-victory-cities = { $player } 5 хот барьсан! Таван хотын эзэнт гүрэн.
ageofheroes-victory-cities-you = Та 5 хот барьсан! Таван хотын эзэнт гүрэн.
ageofheroes-victory-monument = { $player } хөшөөгөө барьж дууслаа! Агуу соёлын өвлөгчид.
ageofheroes-victory-monument-you = Та хөшөөгөө барьж дууслаа! Агуу соёлын өвлөгчид.
ageofheroes-victory-last-standing = { $player } сүүлд үлдсэн овог! Хамгийн тэсвэртэй.
ageofheroes-victory-last-standing-you = Та сүүлд үлдсэн овог! Хамгийн тэсвэртэй.
ageofheroes-game-over = Тоглоом дууслаа.

# Elimination
ageofheroes-eliminated = { $player } хасагдлаа.
ageofheroes-eliminated-you = Та хасагдлаа.

# Hand
ageofheroes-hand-empty = Танд хөзөр байхгүй.
ageofheroes-hand-contents = Таны хөзөр ({ $count } { $count ->
    [one] хөзөр
    *[other] хөзөр
}): { $cards }

# Status
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [one] хот
    *[other] хот
}, { $armies } { $armies ->
    [one] арми
    *[other] арми
}, { $monument }/5 хөшөө
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = Хотууд: { $count }
ageofheroes-status-armies = Армиуд: { $count }
ageofheroes-status-generals = Генералууд: { $count }
ageofheroes-status-fortresses = Цайзнууд: { $count }
ageofheroes-status-monument = Хөшөө: { $count }/5
ageofheroes-status-roads = Замууд: { $left }{ $right }
ageofheroes-status-road-left = зүүн
ageofheroes-status-road-right = баруун
ageofheroes-status-none = байхгүй
ageofheroes-status-earthquake-armies = Сэргэж буй армиуд: { $count }
ageofheroes-status-returning-armies = Буцаж ирэх армиуд: { $count }
ageofheroes-status-returning-generals = Буцаж ирэх генералууд: { $count }

# Deck info
ageofheroes-deck-empty = { $card } хөзөр хөзөрт байхгүй.
ageofheroes-deck-count = Үлдсэн хөзөр: { $count }
ageofheroes-deck-reshuffled = Хаясан хөзрийг буцаан хольж оруулав.

# Give up
ageofheroes-give-up-confirm = Та бууж өгөхдөө итгэлтэй байна уу?
ageofheroes-gave-up = { $player } бууж өглөө!
ageofheroes-gave-up-you = Та бууж өглөө!

# Hero card
ageofheroes-hero-use = Арми эсвэл генералаар ашиглах уу?
ageofheroes-hero-army = Арми
ageofheroes-hero-general = Генерал

# Fortune card
ageofheroes-fortune-reroll = { $player } Аз ашиглаж дахин орхив.
ageofheroes-fortune-prompt = Та шооны дүнд хожигдлоо. Аз ашиглаж дахин орхих уу?

# Disabled action reasons
ageofheroes-not-your-turn = Таны ээлж биш байна.
ageofheroes-game-not-started = Тоглоом хараахан эхлээгүй байна.
ageofheroes-wrong-phase = Энэ үйлдэл одоогийн үе шатад боломжгүй.
ageofheroes-no-resources = Танд шаардлагатай нөөц байхгүй.

# Building costs (for display)
ageofheroes-cost-army = 2 Үр тариа, Төмөр
ageofheroes-cost-fortress = Төмөр, Мод, Чулуу
ageofheroes-cost-general = Төмөр, Алт
ageofheroes-cost-road = 2 Чулуу
ageofheroes-cost-city = 2 Мод, Чулуу
