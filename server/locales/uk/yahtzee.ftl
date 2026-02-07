# Yahtzee game messages

# Game info
game-name-yahtzee = Ятзі

# Actions - Rolling
yahtzee-roll = Перекинути ({ $count } залишилось)
yahtzee-roll-all = Кинути кубики

# Upper section scoring categories
yahtzee-score-ones = Одиниці за { $points } очок
yahtzee-score-twos = Двійки за { $points } очок
yahtzee-score-threes = Трійки за { $points } очок
yahtzee-score-fours = Четвірки за { $points } очок
yahtzee-score-fives = П'ятірки за { $points } очок
yahtzee-score-sixes = Шістки за { $points } очок

# Lower section scoring categories
yahtzee-score-three-kind = Трійка за { $points } очок
yahtzee-score-four-kind = Каре за { $points } очок
yahtzee-score-full-house = Фул-хаус за { $points } очок
yahtzee-score-small-straight = Малий стріт за { $points } очок
yahtzee-score-large-straight = Великий стріт за { $points } очок
yahtzee-score-yahtzee = Ятзі за { $points } очок
yahtzee-score-chance = Шанс за { $points } очок

# Game events
yahtzee-you-rolled = Ви кинули: { $dice }. Кидків залишилось: { $remaining }
yahtzee-player-rolled = { $player } кинув: { $dice }. Кидків залишилось: { $remaining }

# Scoring announcements
yahtzee-you-scored = Ви набрали { $points } очок у { $category }.
yahtzee-player-scored = { $player } набрав { $points } у { $category }.

# Yahtzee bonus
yahtzee-you-bonus = Бонус Ятзі! +100 очок
yahtzee-player-bonus = { $player } отримав бонус Ятзі! +100 очок

# Upper section bonus
yahtzee-you-upper-bonus = Бонус верхньої секції! +35 очок ({ $total } у верхній секції)
yahtzee-player-upper-bonus = { $player } отримав бонус верхньої секції! +35 очок
yahtzee-you-upper-bonus-missed = Ви не отримали бонус верхньої секції ({ $total } у верхній секції, потрібно було 63).
yahtzee-player-upper-bonus-missed = { $player } не отримав бонус верхньої секції.

# Scoring mode
yahtzee-choose-category = Виберіть категорію для підрахунку.
yahtzee-continuing = Продовжуємо хід.

# Status checks
yahtzee-check-scoresheet = Перевірити таблицю рахунку
yahtzee-view-dice = Перевірити руку
yahtzee-your-dice = Ваші кубики: { $dice }.
yahtzee-your-dice-kept = Ваші кубики: { $dice }. Зберігаємо: { $kept }
yahtzee-not-rolled = Ви ще не кидали.

# Scoresheet display
yahtzee-scoresheet-header = === Таблиця рахунку { $player } ===
yahtzee-scoresheet-upper = Верхня секція:
yahtzee-scoresheet-lower = Нижня секція:
yahtzee-scoresheet-category-filled = { $category }: { $points }
yahtzee-scoresheet-category-open = { $category }: -
yahtzee-scoresheet-upper-total-bonus = Верхня сума: { $total } (БОНУС: +35)
yahtzee-scoresheet-upper-total-needed = Верхня сума: { $total } (ще { $needed } для бонусу)
yahtzee-scoresheet-yahtzee-bonus = Бонуси Ятзі: { $count } x 100 = { $total }
yahtzee-scoresheet-grand-total = ЗАГАЛЬНИЙ РАХУНОК: { $total }

# Category names (for announcements)
yahtzee-category-ones = Одиниці
yahtzee-category-twos = Двійки
yahtzee-category-threes = Трійки
yahtzee-category-fours = Четвірки
yahtzee-category-fives = П'ятірки
yahtzee-category-sixes = Шістки
yahtzee-category-three-kind = Трійка
yahtzee-category-four-kind = Каре
yahtzee-category-full-house = Фул-хаус
yahtzee-category-small-straight = Малий стріт
yahtzee-category-large-straight = Великий стріт
yahtzee-category-yahtzee = Ятзі
yahtzee-category-chance = Шанс

# Game end
yahtzee-winner = { $player } виграє з { $score } очками!
yahtzee-winners-tie = Нічия! { $players } всі набрали { $score } очок!

# Options
yahtzee-set-rounds = Кількість ігор: { $rounds }
yahtzee-enter-rounds = Введіть кількість ігор (1-10):
yahtzee-option-changed-rounds = Кількість ігор встановлено на { $rounds }.

# Disabled action reasons
yahtzee-no-rolls-left = У вас не залишилось кидків.
yahtzee-roll-first = Спочатку потрібно кинути кубики.
yahtzee-category-filled = Ця категорія вже заповнена.
