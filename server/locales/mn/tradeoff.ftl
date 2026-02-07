# Tradeoff тоглоомын мессежүүд

# Тоглоомын мэдээлэл
game-name-tradeoff = Солилцоо

# Тойрог ба давталтын урсгал
tradeoff-round-start = { $round } дугаар тойрог.
tradeoff-iteration = 3-н { $iteration } дахь гар.

# 1 дэх үе: Солилцоо
tradeoff-you-rolled = Та гүйлгэв: { $dice }.
tradeoff-toggle-trade = { $value } ({ $status })
tradeoff-trade-status-trading = солилцож байна
tradeoff-trade-status-keeping = хадгалж байна
tradeoff-confirm-trades = Солилцоог батлах ({ $count } шоо)
tradeoff-keeping = { $value } хадгална.
tradeoff-trading = { $value } солилцно.
tradeoff-player-traded = { $player } солилцов: { $dice }.
tradeoff-player-traded-none = { $player } бүх шоог хадгалав.

# 2 дахь үе: Сангаас авах
tradeoff-your-turn-take = Таны ээлж сангаас шоо авах.
tradeoff-take-die = { $value } авах ({ $remaining } үлдсэн)
tradeoff-you-take = Та { $value } авна.
tradeoff-player-takes = { $player } { $value } авна.

# 3 дахь үе: Оноо тоолох
tradeoff-player-scored = { $player } ({ $points } оноо): { $sets }.
tradeoff-no-sets = { $player }: багц алга.

# Багцын тодорхойлолт (товч)
tradeoff-set-triple = { $value }-н гурвал
tradeoff-set-group = { $value }-н бүлэг
tradeoff-set-mini-straight = бага шулуун { $low }-{ $high }
tradeoff-set-double-triple = давхар гурвал ({ $v1 } ба { $v2 })
tradeoff-set-straight = шулуун { $low }-{ $high }
tradeoff-set-double-group = давхар бүлэг ({ $v1 } ба { $v2 })
tradeoff-set-all-groups = бүх бүлгүүд
tradeoff-set-all-triplets = бүх гурвалууд

# Тойрог дуусах
tradeoff-round-scores = { $round } дугаар тойргийн оноонууд:
tradeoff-score-line = { $player }: +{ $round_points } (нийт: { $total })
tradeoff-leader = { $player } { $score }-р тэргүүлж байна.

# Тоглоом дуусах
tradeoff-winner = { $player } { $score } оноогоор ялна!
tradeoff-winners-tie = Тэнцсэн! { $players } { $score } оноогоор тэнцсэн!

# Статус шалгалт
tradeoff-view-hand = Гараа харах
tradeoff-view-pool = Сангийг харах
tradeoff-view-players = Тоглогчдыг харах
tradeoff-hand-display = Таны гар ({ $count } шоо): { $dice }
tradeoff-pool-display = Санг ({ $count } шоо): { $dice }
tradeoff-player-info = { $player }: { $hand }. Солилцсон: { $traded }.
tradeoff-player-info-no-trade = { $player }: { $hand }. Юу ч солилцоогүй.

# Алдааны мессежүүд
tradeoff-not-trading-phase = Солилцооны үе биш.
tradeoff-not-taking-phase = Авах үе биш.
tradeoff-already-confirmed = Аль хэдийн баталсан.
tradeoff-no-die = Солих шоо алга.
tradeoff-no-more-takes = Авах боломж алга.
tradeoff-not-in-pool = Тэр шоо сангад байхгүй.

# Сонголтууд
tradeoff-set-target = Зорилтот оноо: { $score }
tradeoff-enter-target = Зорилтот оноо оруулна уу:
tradeoff-option-changed-target = Зорилтот оноо { $score } болгов.
