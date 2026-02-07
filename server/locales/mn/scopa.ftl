# Scopa game messages
# Note: Common messages like round-start, turn-start, target-score, team-mode are in games.ftl

# Game name
game-name-scopa = Скопа

# Game events
scopa-initial-table = Ширээн дээрх хөзрүүд: { $cards }
scopa-no-initial-table = Эхлэхэд ширээн дээр хөзөр байхгүй.
scopa-you-collect = Та { $card }-аар { $cards } цуглуулав
scopa-player-collects = { $player } { $card }-аар { $cards } цуглуулав
scopa-you-put-down = Та { $card } тавив.
scopa-player-puts-down = { $player } { $card } тавив.
scopa-scopa-suffix =  - СКОПА!
scopa-clear-table-suffix = , ширээг цэвэрлэв.
scopa-remaining-cards = { $player } үлдсэн ширээний хөзрүүдийг авав.
scopa-scoring-round = Оноо тоолох үе...
scopa-most-cards = { $player } хамгийн олон хөзрөөр 1 оноо авав ({ $count } хөзөр).
scopa-most-cards-tie = Хамгийн олон хөзөр тэнцсэн - оноо олгохгүй.
scopa-most-diamonds = { $player } хамгийн олон алмазаар 1 оноо авав ({ $count } алмаз).
scopa-most-diamonds-tie = Хамгийн олон алмаз тэнцсэн - оноо олгохгүй.
scopa-seven-diamonds = { $player } алмазын 7-оор 1 оноо авав.
scopa-seven-diamonds-multi = { $player } хамгийн олон алмазын 7-оор 1 оноо авав ({ $count } × алмазын 7).
scopa-seven-diamonds-tie = Алмазын 7 тэнцсэн - оноо олгохгүй.
scopa-most-sevens = { $player } хамгийн олон 7-оор 1 оноо авав ({ $count } ширхэг 7).
scopa-most-sevens-tie = Хамгийн олон 7 тэнцсэн - оноо олгохгүй.
scopa-round-scores = Тойргийн оноо:
scopa-round-score-line = { $player }: +{ $round_score } (нийт: { $total_score })
scopa-table-empty = Ширээн дээр хөзөр байхгүй.
scopa-no-such-card = Тэр байрлалд хөзөр байхгүй.
scopa-captured-count = Та { $count } хөзөр барьж авсан

# View actions
scopa-view-table = Ширээг харах
scopa-view-captured = Барьсныг харах

# Scopa-specific options
scopa-enter-target-score = Зорилтот оноо оруулах (1-121)
scopa-set-cards-per-deal = Нэг хуваалтын хөзөр: { $cards }
scopa-enter-cards-per-deal = Нэг хуваалтын хөзөр оруулах (1-10)
scopa-set-decks = Хөзрийн ширхэг: { $decks }
scopa-enter-decks = Хөзрийн ширхэг оруулах (1-6)
scopa-toggle-escoba = Эскоба (15 болгох): { $enabled }
scopa-toggle-hints = Барих заавар үзүүлэх: { $enabled }
scopa-set-mechanic = Скопа механик: { $mechanic }
scopa-select-mechanic = Скопа механик сонгох
scopa-toggle-instant-win = Скопа дээр шууд ялалт: { $enabled }
scopa-toggle-team-scoring = Багийн хөзрийг нэгтгэн оноо тоолох: { $enabled }
scopa-toggle-inverse = Урвуу горим (зорилтод хүрэх = хасагдах): { $enabled }

# Option change announcements
scopa-option-changed-cards = Нэг хуваалтын хөзөр { $cards }-д тохируулагдлаа.
scopa-option-changed-decks = Хөзрийн ширхэг { $decks }-д тохируулагдлаа.
scopa-option-changed-escoba = Эскоба { $enabled }.
scopa-option-changed-hints = Барих заавар { $enabled }.
scopa-option-changed-mechanic = Скопа механик { $mechanic }-д тохируулагдлаа.
scopa-option-changed-instant = Скопа дээр шууд ялалт { $enabled }.
scopa-option-changed-team-scoring = Багийн хөзөр оноо тоолох { $enabled }.
scopa-option-changed-inverse = Урвуу горим { $enabled }.

# Scopa mechanic choices
scopa-mechanic-normal = Энгийн
scopa-mechanic-no_scopas = Скопагүй
scopa-mechanic-only_scopas = Зөвхөн скопа

# Disabled action reasons
scopa-timer-not-active = Тойргийн цаг идэвхгүй байна.

# Validation errors
scopa-error-not-enough-cards = { $decks } { $decks ->
    [one] ширхэг
    *[other] ширхэг
} хөзөрт { $players } { $players ->
    [one] тоглогч
    *[other] тоглогч
}-д { $cards_per_deal } хөзөр өгөхөд хүрэхгүй байна. ({ $cards_per_deal } × { $players } = { $cards_needed } хөзөр хэрэгтэй, гэвч { $total_cards } л байна.)
