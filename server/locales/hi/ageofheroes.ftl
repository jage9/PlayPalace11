# Age of Heroes game messages
# A civilization-building card game for 2-6 players

# Game name
game-name-ageofheroes = एज ऑफ हीरोज

# Tribes
ageofheroes-tribe-egyptians = मिस्रवासी
ageofheroes-tribe-romans = रोमन
ageofheroes-tribe-greeks = यूनानी
ageofheroes-tribe-babylonians = बेबीलोनियन
ageofheroes-tribe-celts = सेल्ट
ageofheroes-tribe-chinese = चीनी

# Special Resources (for monuments)
ageofheroes-special-limestone = चूना पत्थर
ageofheroes-special-concrete = कंक्रीट
ageofheroes-special-marble = संगमरमर
ageofheroes-special-bricks = ईंटें
ageofheroes-special-sandstone = बलुआ पत्थर
ageofheroes-special-granite = ग्रेनाइट

# Standard Resources
ageofheroes-resource-iron = लोहा
ageofheroes-resource-wood = लकड़ी
ageofheroes-resource-grain = अनाज
ageofheroes-resource-stone = पत्थर
ageofheroes-resource-gold = सोना

# Events
ageofheroes-event-population-growth = जनसंख्या वृद्धि
ageofheroes-event-earthquake = भूकंप
ageofheroes-event-eruption = विस्फोट
ageofheroes-event-hunger = भूख
ageofheroes-event-barbarians = बर्बर
ageofheroes-event-olympics = ओलंपिक खेल
ageofheroes-event-hero = नायक
ageofheroes-event-fortune = भाग्य

# Buildings
ageofheroes-building-army = सेना
ageofheroes-building-fortress = किला
ageofheroes-building-general = जनरल
ageofheroes-building-road = सड़क
ageofheroes-building-city = शहर

# Actions
ageofheroes-action-tax-collection = कर संग्रह
ageofheroes-action-construction = निर्माण
ageofheroes-action-war = युद्ध
ageofheroes-action-do-nothing = कुछ नहीं करें
ageofheroes-play = खेलें

# War goals
ageofheroes-war-conquest = विजय
ageofheroes-war-plunder = लूटपाट
ageofheroes-war-destruction = विनाश

# Game options
ageofheroes-set-victory-cities = विजय के शहर: { $cities }
ageofheroes-enter-victory-cities = जीतने के लिए शहरों की संख्या दर्ज करें (3-7)
ageofheroes-set-victory-monument = स्मारक पूर्णता: { $progress }%
ageofheroes-toggle-neighbor-roads = केवल पड़ोसियों के लिए सड़कें: { $enabled }
ageofheroes-set-max-hand = अधिकतम हाथ का आकार: { $cards } कार्ड

# Option change announcements
ageofheroes-option-changed-victory-cities = विजय के लिए { $cities } शहरों की आवश्यकता है।
ageofheroes-option-changed-victory-monument = स्मारक पूर्णता सीमा { $progress }% पर सेट की गई।
ageofheroes-option-changed-neighbor-roads = केवल पड़ोसियों के लिए सड़कें { $enabled }।
ageofheroes-option-changed-max-hand = अधिकतम हाथ का आकार { $cards } कार्ड पर सेट किया गया।

# Setup phase
ageofheroes-setup-start = आप { $tribe } जनजाति के नेता हैं। आपका विशेष स्मारक संसाधन { $special } है। टर्न क्रम निर्धारित करने के लिए पासा फेंकें।
ageofheroes-setup-viewer = खिलाड़ी टर्न क्रम निर्धारित करने के लिए पासा फेंक रहे हैं।
ageofheroes-roll-dice = पासा फेंकें
ageofheroes-war-roll-dice = पासा फेंकें
ageofheroes-dice-result = आपने { $total } फेंका ({ $die1 } + { $die2 })।
ageofheroes-dice-result-other = { $player } ने { $total } फेंका।
ageofheroes-dice-tie = { $total } के साथ कई खिलाड़ी बराबर। फिर से फेंक रहे हैं...
ageofheroes-first-player = { $player } ने { $total } के साथ सबसे अधिक फेंका और पहले जाता है।
ageofheroes-first-player-you = { $total } अंकों के साथ, आप पहले जाते हैं।

# Preparation phase
ageofheroes-prepare-start = खिलाड़ियों को घटना कार्ड खेलने और आपदाओं को डिस्कार्ड करना होगा।
ageofheroes-prepare-your-turn = आपके पास { $count } { $count ->
    [one] कार्ड
    *[other] कार्ड
} खेलने या डिस्कार्ड करने के लिए हैं।
ageofheroes-prepare-done = तैयारी चरण पूर्ण।

# Events played/discarded
ageofheroes-population-growth = { $player } जनसंख्या वृद्धि खेलता है और एक नया शहर बनाता है।
ageofheroes-population-growth-you = आप जनसंख्या वृद्धि खेलते हैं और एक नया शहर बनाते हैं।
ageofheroes-discard-card = { $player } { $card } डिस्कार्ड करता है।
ageofheroes-discard-card-you = आप { $card } डिस्कार्ड करते हैं।
ageofheroes-earthquake = { $player } की जनजाति में भूकंप आता है; उनकी सेनाएं पुनर्प्राप्ति में चली जाती हैं।
ageofheroes-earthquake-you = आपकी जनजाति में भूकंप आता है; आपकी सेनाएं पुनर्प्राप्ति में चली जाती हैं।
ageofheroes-eruption = एक विस्फोट { $player } के एक शहर को नष्ट कर देता है।
ageofheroes-eruption-you = एक विस्फोट आपके एक शहर को नष्ट कर देता है।

# Disaster effects
ageofheroes-hunger-strikes = भूख लगती है।
ageofheroes-lose-card-hunger = आप { $card } खो देते हैं।
ageofheroes-barbarians-pillage = बर्बर { $player } के संसाधनों पर हमला करते हैं।
ageofheroes-barbarians-attack = बर्बर { $player } के संसाधनों पर हमला करते हैं।
ageofheroes-barbarians-attack-you = बर्बर आपके संसाधनों पर हमला करते हैं।
ageofheroes-lose-card-barbarians = आप { $card } खो देते हैं।
ageofheroes-block-with-card = { $player } { $card } का उपयोग करके आपदा को रोकता है।
ageofheroes-block-with-card-you = आप { $card } का उपयोग करके आपदा को रोकते हैं।

# Targeted disaster cards (Earthquake/Eruption)
ageofheroes-select-disaster-target = { $card } के लिए एक लक्ष्य चुनें।
ageofheroes-no-targets = कोई वैध लक्ष्य उपलब्ध नहीं।
ageofheroes-earthquake-strikes-you = { $attacker } आपके खिलाफ भूकंप खेलता है। आपकी सेनाएं अक्षम हैं।
ageofheroes-earthquake-strikes = { $attacker } { $player } के खिलाफ भूकंप खेलता है।
ageofheroes-armies-disabled = { $count } { $count ->
    [one] सेना
    *[other] सेनाएं
} एक टर्न के लिए अक्षम है।
ageofheroes-eruption-strikes-you = { $attacker } आपके खिलाफ विस्फोट खेलता है। आपके एक शहर को नष्ट कर दिया गया है।
ageofheroes-eruption-strikes = { $attacker } { $player } के खिलाफ विस्फोट खेलता है।
ageofheroes-city-destroyed = विस्फोट से एक शहर नष्ट हो गया है।

# Fair phase
ageofheroes-fair-start = बाज़ार में दिन निकलता है।
ageofheroes-fair-draw-base = आप { $count } { $count ->
    [one] कार्ड
    *[other] कार्ड
} ड्रॉ करते हैं।
ageofheroes-fair-draw-roads = आप अपने सड़क नेटवर्क के लिए { $count } अतिरिक्त { $count ->
    [one] कार्ड
    *[other] कार्ड
} ड्रॉ करते हैं।
ageofheroes-fair-draw-other = { $player } { $count } { $count ->
    [one] कार्ड
    *[other] कार्ड
} ड्रॉ करता है।

# Trading/Auction
ageofheroes-auction-start = नीलामी शुरू होती है।
ageofheroes-offer-trade = व्यापार की पेशकश करें
ageofheroes-offer-made = { $player } { $wanted } के लिए { $card } की पेशकश करता है।
ageofheroes-offer-made-you = आप { $wanted } के लिए { $card } की पेशकश करते हैं।
ageofheroes-trade-accepted = { $player } { $other } की पेशकश स्वीकार करता है और { $receive } के लिए { $give } का व्यापार करता है।
ageofheroes-trade-accepted-you = आप { $other } की पेशकश स्वीकार करते हैं और { $receive } प्राप्त करते हैं।
ageofheroes-trade-cancelled = { $player } { $card } के लिए अपनी पेशकश वापस लेता है।
ageofheroes-trade-cancelled-you = आप { $card } के लिए अपनी पेशकश वापस लेते हैं।
ageofheroes-stop-trading = व्यापार बंद करें
ageofheroes-select-request = आप { $card } की पेशकश कर रहे हैं। आप बदले में क्या चाहते हैं?
ageofheroes-cancel = रद्द करें
ageofheroes-left-auction = { $player } निकल जाता है।
ageofheroes-left-auction-you = आप बाज़ार से निकलते हैं।
ageofheroes-any-card = कोई भी कार्ड
ageofheroes-cannot-trade-own-special = आप अपने स्वयं के विशेष स्मारक संसाधन का व्यापार नहीं कर सकते।
ageofheroes-resource-not-in-game = इस विशेष संसाधन का उपयोग इस खेल में नहीं किया जा रहा है।

# Main play phase
ageofheroes-play-start = खेलने का चरण।
ageofheroes-day = दिन { $day }
ageofheroes-draw-card = { $player } डेक से एक कार्ड ड्रॉ करता है।
ageofheroes-draw-card-you = आप डेक से { $card } ड्रॉ करते हैं।
ageofheroes-your-action = आप क्या करना चाहते हैं?

# Tax Collection
ageofheroes-tax-collection = { $player } कर संग्रह चुनता है: { $cities } { $cities ->
    [one] शहर
    *[other] शहर
} { $cards } { $cards ->
    [one] कार्ड
    *[other] कार्ड
} एकत्र करता है।
ageofheroes-tax-collection-you = आप कर संग्रह चुनते हैं: { $cities } { $cities ->
    [one] शहर
    *[other] शहर
} { $cards } { $cards ->
    [one] कार्ड
    *[other] कार्ड
} एकत्र करता है।
ageofheroes-tax-no-city = कर संग्रह: आपके पास कोई जीवित शहर नहीं है। एक नया ड्रॉ करने के लिए एक कार्ड डिस्कार्ड करें।
ageofheroes-tax-no-city-done = { $player } कर संग्रह चुनता है लेकिन कोई शहर नहीं है, इसलिए वे एक कार्ड का आदान-प्रदान करते हैं।
ageofheroes-tax-no-city-done-you = कर संग्रह: आपने एक नए कार्ड के लिए { $card } का आदान-प्रदान किया।

# Construction
ageofheroes-construction-menu = आप क्या बनाना चाहते हैं?
ageofheroes-construction-done = { $player } ने { $article } { $building } बनाया।
ageofheroes-construction-done-you = आपने { $article } { $building } बनाया।
ageofheroes-construction-stop = निर्माण रोकें
ageofheroes-construction-stopped = आपने निर्माण रोकने का फैसला किया।
ageofheroes-road-select-neighbor = चुनें कि किस पड़ोसी के लिए सड़क बनानी है।
ageofheroes-direction-left = आपके बाईं ओर
ageofheroes-direction-right = आपके दाईं ओर
ageofheroes-road-request-sent = सड़क अनुरोध भेजा गया। पड़ोसी की स्वीकृति की प्रतीक्षा में।
ageofheroes-road-request-received = { $requester } आपकी जनजाति के लिए सड़क बनाने की अनुमति का अनुरोध करता है।
ageofheroes-road-request-denied-you = आपने सड़क अनुरोध को अस्वीकार कर दिया।
ageofheroes-road-request-denied = { $denier } ने आपका सड़क अनुरोध अस्वीकार कर दिया।
ageofheroes-road-built = { $tribe1 } और { $tribe2 } अब सड़क से जुड़े हुए हैं।
ageofheroes-road-no-target = सड़क निर्माण के लिए कोई पड़ोसी जनजाति उपलब्ध नहीं।
ageofheroes-approve = स्वीकृत करें
ageofheroes-deny = अस्वीकार करें
ageofheroes-supply-exhausted = बनाने के लिए और { $building } उपलब्ध नहीं।

# Do Nothing
ageofheroes-do-nothing = { $player } पास करता है।
ageofheroes-do-nothing-you = आप पास करते हैं...

# War
ageofheroes-war-declare = { $attacker } { $defender } के खिलाफ युद्ध की घोषणा करता है। लक्ष्य: { $goal }।
ageofheroes-war-prepare = { $action } के लिए अपनी सेनाओं का चयन करें।
ageofheroes-war-no-army = आपके पास कोई सेना या नायक कार्ड उपलब्ध नहीं है।
ageofheroes-war-no-targets = युद्ध के लिए कोई वैध लक्ष्य नहीं।
ageofheroes-war-no-valid-goal = इस लक्ष्य के खिलाफ कोई वैध युद्ध लक्ष्य नहीं।
ageofheroes-war-select-target = चुनें कि किस खिलाड़ी पर हमला करना है।
ageofheroes-war-select-goal = अपना युद्ध लक्ष्य चुनें।
ageofheroes-war-prepare-attack = अपनी आक्रामक सेनाओं का चयन करें।
ageofheroes-war-prepare-defense = { $attacker } आप पर हमला कर रहा है; अपनी रक्षात्मक सेनाओं का चयन करें।
ageofheroes-war-select-armies = सेनाओं का चयन करें: { $count }
ageofheroes-war-select-generals = जनरलों का चयन करें: { $count }
ageofheroes-war-select-heroes = नायकों का चयन करें: { $count }
ageofheroes-war-attack = हमला...
ageofheroes-war-defend = रक्षा करें...
ageofheroes-war-prepared = आपकी सेनाएं: { $armies } { $armies ->
    [one] सेना
    *[other] सेनाएं
}{ $generals ->
    [0] {""}
    [one] {" और 1 जनरल"}
    *[other] {" और { $generals } जनरल"}
}{ $heroes ->
    [0] {""}
    [one] {" और 1 नायक"}
    *[other] {" और { $heroes } नायक"}
}।
ageofheroes-war-roll-you = आप { $roll } फेंकते हैं।
ageofheroes-war-roll-other = { $player } { $roll } फेंकता है।
ageofheroes-war-bonuses-you = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [1] {"+1 किले से = { $total } कुल"}
            *[other] {"+{ $fortress } किलों से = { $total } कुल"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"+{ $general } जनरल से = { $total } कुल"}
            [1] {"+{ $general } जनरल से, +1 किले से = { $total } कुल"}
            *[other] {"+{ $general } जनरल से, +{ $fortress } किलों से = { $total } कुल"}
        }
    }
}
ageofheroes-war-bonuses-other = { $general ->
    [0] {
        { $fortress ->
            [0] {""}
            [1] {"{ $player }: +1 किले से = { $total } कुल"}
            *[other] {"{ $player }: +{ $fortress } किलों से = { $total } कुल"}
        }
    }
    *[other] {
        { $fortress ->
            [0] {"{ $player }: +{ $general } जनरल से = { $total } कुल"}
            [1] {"{ $player }: +{ $general } जनरल से, +1 किले से = { $total } कुल"}
            *[other] {"{ $player }: +{ $general } जनरल से, +{ $fortress } किलों से = { $total } कुल"}
        }
    }
}

# Battle
ageofheroes-battle-start = युद्ध शुरू होता है। { $attacker } की { $att_armies } { $att_armies ->
    [one] सेना
    *[other] सेनाएं
} बनाम { $defender } की { $def_armies } { $def_armies ->
    [one] सेना
    *[other] सेनाएं
}।
ageofheroes-dice-roll-detailed = { $name } { $dice } फेंकता है{ $general ->
    [0] {""}
    *[other] { " + जनरल से { $general }" }
}{ $fortress ->
    [0] {""}
    [one] { " + किले से 1" }
    *[other] { " + किलों से { $fortress }" }
} = { $total }।
ageofheroes-dice-roll-detailed-you = आप { $dice } फेंकते हैं{ $general ->
    [0] {""}
    *[other] { " + जनरल से { $general }" }
}{ $fortress ->
    [0] {""}
    [one] { " + किले से 1" }
    *[other] { " + किलों से { $fortress }" }
} = { $total }।
ageofheroes-round-attacker-wins = { $attacker } राउंड जीतता है ({ $att_total } बनाम { $def_total })। { $defender } एक सेना खो देता है।
ageofheroes-round-defender-wins = { $defender } सफलतापूर्वक रक्षा करता है ({ $def_total } बनाम { $att_total })। { $attacker } एक सेना खो देता है।
ageofheroes-round-draw = दोनों पक्ष { $total } पर बराबर। कोई सेना नहीं खोई।
ageofheroes-battle-victory-attacker = { $attacker } { $defender } को पराजित करता है।
ageofheroes-battle-victory-defender = { $defender } { $attacker } के खिलाफ सफलतापूर्वक रक्षा करता है।
ageofheroes-battle-mutual-defeat = { $attacker } और { $defender } दोनों अपनी सभी सेनाएं खो देते हैं।
ageofheroes-general-bonus = +{ $count } { $count ->
    [one] जनरल
    *[other] जनरलों
} से
ageofheroes-fortress-bonus = +{ $count } किले की रक्षा से
ageofheroes-battle-winner = { $winner } युद्ध जीतता है।
ageofheroes-battle-draw = युद्ध बराबरी में समाप्त होता है...
ageofheroes-battle-continue = युद्ध जारी रखें।
ageofheroes-battle-end = युद्ध समाप्त हो गया है।

# War outcomes
ageofheroes-conquest-success = { $attacker } { $defender } से { $count } { $count ->
    [one] शहर
    *[other] शहर
} जीतता है।
ageofheroes-plunder-success = { $attacker } { $defender } से { $count } { $count ->
    [one] कार्ड
    *[other] कार्ड
} लूटता है।
ageofheroes-destruction-success = { $attacker } { $defender } के { $count } स्मारक { $count ->
    [one] संसाधन
    *[other] संसाधनों
} को नष्ट करता है।
ageofheroes-army-losses = { $player } { $count } { $count ->
    [one] सेना
    *[other] सेनाएं
} खो देता है।
ageofheroes-army-losses-you = आप { $count } { $count ->
    [one] सेना
    *[other] सेनाएं
} खो देते हैं।

# Army return
ageofheroes-army-return-road = आपकी सेनाएं सड़क के माध्यम से तुरंत लौटती हैं।
ageofheroes-army-return-delayed = { $count } { $count ->
    [one] इकाई
    *[other] इकाइयां
} आपकी अगली बारी के अंत में लौटती हैं।
ageofheroes-army-returned = { $player } की सेनाएं युद्ध से लौट आई हैं।
ageofheroes-army-returned-you = आपकी सेनाएं युद्ध से लौट आई हैं।
ageofheroes-army-recover = { $player } की सेनाएं भूकंप से उबर गई हैं।
ageofheroes-army-recover-you = आपकी सेनाएं भूकंप से उबर गई हैं।

# Olympics
ageofheroes-olympics-cancel = { $player } ओलंपिक खेल खेलता है। युद्ध रद्द।
ageofheroes-olympics-prompt = { $attacker } ने युद्ध की घोषणा की है। आपके पास ओलंपिक खेल हैं - रद्द करने के लिए इसका उपयोग करें?
ageofheroes-yes = हां
ageofheroes-no = नहीं

# Monument progress
ageofheroes-monument-progress = { $player } का स्मारक { $count }/5 पूर्ण है।
ageofheroes-monument-progress-you = आपका स्मारक { $count }/5 पूर्ण है।

# Hand management
ageofheroes-discard-excess = आपके पास { $max } से अधिक कार्ड हैं। { $count } { $count ->
    [one] कार्ड
    *[other] कार्ड
} डिस्कार्ड करें।
ageofheroes-discard-excess-other = { $player } को अतिरिक्त कार्ड डिस्कार्ड करने होंगे।
ageofheroes-discard-more = { $count } और { $count ->
    [one] कार्ड
    *[other] कार्ड
} डिस्कार्ड करें।

# Victory
ageofheroes-victory-cities = { $player } ने 5 शहर बनाए हैं! पांच शहरों का साम्राज्य।
ageofheroes-victory-cities-you = आपने 5 शहर बनाए हैं! पांच शहरों का साम्राज्य।
ageofheroes-victory-monument = { $player } ने अपना स्मारक पूरा कर लिया है! महान संस्कृति के वाहक।
ageofheroes-victory-monument-you = आपने अपना स्मारक पूरा कर लिया है! महान संस्कृति के वाहक।
ageofheroes-victory-last-standing = { $player } अंतिम खड़ी जनजाति है! सबसे दृढ़।
ageofheroes-victory-last-standing-you = आप अंतिम खड़ी जनजाति हैं! सबसे दृढ़।
ageofheroes-game-over = खेल समाप्त।

# Elimination
ageofheroes-eliminated = { $player } को समाप्त कर दिया गया है।
ageofheroes-eliminated-you = आपको समाप्त कर दिया गया है।

# Hand
ageofheroes-hand-empty = आपके पास कोई कार्ड नहीं है।
ageofheroes-hand-contents = आपका हाथ ({ $count } { $count ->
    [one] कार्ड
    *[other] कार्ड
}): { $cards }

# Status
ageofheroes-status = { $player } ({ $tribe }): { $cities } { $cities ->
    [one] शहर
    *[other] शहर
}, { $armies } { $armies ->
    [one] सेना
    *[other] सेनाएं
}, { $monument }/5 स्मारक
ageofheroes-status-detailed-header = { $player } ({ $tribe })
ageofheroes-status-cities = शहर: { $count }
ageofheroes-status-armies = सेनाएं: { $count }
ageofheroes-status-generals = जनरल: { $count }
ageofheroes-status-fortresses = किले: { $count }
ageofheroes-status-monument = स्मारक: { $count }/5
ageofheroes-status-roads = सड़कें: { $left }{ $right }
ageofheroes-status-road-left = बाएं
ageofheroes-status-road-right = दाएं
ageofheroes-status-none = कोई नहीं
ageofheroes-status-earthquake-armies = पुनर्प्राप्ति में सेनाएं: { $count }
ageofheroes-status-returning-armies = लौटती सेनाएं: { $count }
ageofheroes-status-returning-generals = लौटते जनरल: { $count }

# Deck info
ageofheroes-deck-empty = डेक में और { $card } कार्ड नहीं।
ageofheroes-deck-count = शेष कार्ड: { $count }
ageofheroes-deck-reshuffled = डिस्कार्ड पाइल को डेक में वापस फेंट दिया गया है।

# Give up
ageofheroes-give-up-confirm = क्या आप वाकई हार मानना चाहते हैं?
ageofheroes-gave-up = { $player } ने हार मान ली!
ageofheroes-gave-up-you = आपने हार मान ली!

# Hero card
ageofheroes-hero-use = सेना या जनरल के रूप में उपयोग करें?
ageofheroes-hero-army = सेना
ageofheroes-hero-general = जनरल

# Fortune card
ageofheroes-fortune-reroll = { $player } फिर से फेंकने के लिए भाग्य का उपयोग करता है।
ageofheroes-fortune-prompt = आप फेंकने में हार गए। फिर से फेंकने के लिए भाग्य का उपयोग करें?

# Disabled action reasons
ageofheroes-not-your-turn = यह आपकी बारी नहीं है।
ageofheroes-game-not-started = खेल अभी शुरू नहीं हुआ है।
ageofheroes-wrong-phase = यह क्रिया वर्तमान चरण में उपलब्ध नहीं है।
ageofheroes-no-resources = आपके पास आवश्यक संसाधन नहीं हैं।

# Building costs (for display)
ageofheroes-cost-army = 2 अनाज, लोहा
ageofheroes-cost-fortress = लोहा, लकड़ी, पत्थर
ageofheroes-cost-general = लोहा, सोना
ageofheroes-cost-road = 2 पत्थर
ageofheroes-cost-city = 2 लकड़ी, पत्थर
