# Toss Up game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-tossup = Підкидання
tossup-category = Ігри з кубиками

# Actions
tossup-roll-first = Кинути { $count } кубиків
tossup-roll-remaining = Кинути { $count } залишкових кубиків
tossup-bank = Зберегти { $points } очок

# Game events
tossup-turn-start = Хід { $player }. Рахунок: { $score }
tossup-you-roll = Ви кинули: { $results }.
tossup-player-rolls = { $player } кинув: { $results }.

# Turn status
tossup-you-have-points = Очки ходу: { $turn_points }. Кубиків залишилось: { $dice_count }.
tossup-player-has-points = { $player } має { $turn_points } очок ходу. { $dice_count } кубиків залишилось.

# Fresh dice
tossup-you-get-fresh = Немає кубиків! Отримуємо { $count } свіжих кубиків.
tossup-player-gets-fresh = { $player } отримує { $count } свіжих кубиків.

# Bust
tossup-you-bust = Провал! Ви втрачаєте { $points } очок цього ходу.
tossup-player-busts = { $player } провалюється і втрачає { $points } очок!

# Bank
tossup-you-bank = Ви зберігаєте { $points } очок. Загальний рахунок: { $total }.
tossup-player-banks = { $player } зберігає { $points } очок. Загальний рахунок: { $total }.

# Winner
tossup-winner = { $player } виграє з { $score } очками!
tossup-tie-tiebreaker = Нічия між { $players }! Додатковий раунд!

# Options
tossup-set-rules-variant = Варіант правил: { $variant }
tossup-select-rules-variant = Виберіть варіант правил:
tossup-option-changed-rules = Варіант правил змінено на { $variant }

tossup-set-starting-dice = Початкові кубики: { $count }
tossup-enter-starting-dice = Введіть кількість початкових кубиків:
tossup-option-changed-dice = Початкові кубики змінено на { $count }

# Rules variants
tossup-rules-standard = Стандартні
tossup-rules-playpalace = PlayPalace

# Rules explanations
tossup-rules-standard-desc = 3 зелених, 2 жовтих, 1 червоний на кубик. Провал, якщо немає зелених і є принаймні один червоний.
tossup-rules-playpalace-desc = Рівний розподіл. Провал, якщо всі кубики червоні.

# Disabled reasons
tossup-need-points = Вам потрібні очки для збереження.
