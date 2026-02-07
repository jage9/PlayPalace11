# Ninety Nine - English Localization
# Messages match v10 exactly

# Game info
ninetynine-name = Дев'яносто дев'ять
ninetynine-description = Карткова гра, де гравці намагаються не перевищити поточну суму 99. Останній гравець, що залишився, виграє!

# Round
ninetynine-round = Раунд { $round }.

# Turn
ninetynine-player-turn = Хід { $player }.

# Playing cards - match v10 exactly
ninetynine-you-play = Ви граєте { $card }. Рахунок тепер { $count }.
ninetynine-player-plays = { $player } грає { $card }. Рахунок тепер { $count }.

# Direction reverse
ninetynine-direction-reverses = Напрямок гри змінюється!

# Skip
ninetynine-player-skipped = { $player } пропущений.

# Token loss - match v10 exactly
ninetynine-you-lose-tokens = Ви втрачаєте { $amount } { $amount ->
    [one] жетон
    *[other] жетонів
}.
ninetynine-player-loses-tokens = { $player } втрачає { $amount } { $amount ->
    [one] жетон
    *[other] жетонів
}.

# Elimination
ninetynine-player-eliminated = { $player } вибув!

# Game end
ninetynine-player-wins = { $player } виграє гру!

# Dealing
ninetynine-you-deal = Ви роздаєте карти.
ninetynine-player-deals = { $player } роздає карти.

# Drawing cards
ninetynine-you-draw = Ви берете { $card }.
ninetynine-player-draws = { $player } бере карту.

# No valid cards
ninetynine-no-valid-cards = { $player } не має карт, які не перевищать 99!

# Status - for C key
ninetynine-current-count = Рахунок { $count }.

# Hand check - for H key
ninetynine-hand-cards = Ваші карти: { $cards }.
ninetynine-hand-empty = У вас немає карт.

# Ace choice
ninetynine-ace-choice = Грати туза як +1 або +11?
ninetynine-ace-add-eleven = Додати 11
ninetynine-ace-add-one = Додати 1

# Ten choice
ninetynine-ten-choice = Грати 10 як +10 або -10?
ninetynine-ten-add = Додати 10
ninetynine-ten-subtract = Відняти 10

# Manual draw
ninetynine-draw-card = Взяти карту
ninetynine-draw-prompt = Натисніть Пробіл або D, щоб взяти карту.

# Options
ninetynine-set-tokens = Початкові жетони: { $tokens }
ninetynine-enter-tokens = Введіть кількість початкових жетонів:
ninetynine-option-changed-tokens = Початкові жетони встановлено на { $tokens }.
ninetynine-set-rules = Варіант правил: { $rules }
ninetynine-select-rules = Виберіть варіант правил
ninetynine-option-changed-rules = Варіант правил встановлено на { $rules }.
ninetynine-set-hand-size = Розмір руки: { $size }
ninetynine-enter-hand-size = Введіть розмір руки:
ninetynine-option-changed-hand-size = Розмір руки встановлено на { $size }.
ninetynine-set-autodraw = Автоматичне взяття: { $enabled }
ninetynine-option-changed-autodraw = Автоматичне взяття встановлено на { $enabled }.

# Rules variant announcements (shown at game start)
ninetynine-rules-quentin = Правила Quentin C.
ninetynine-rules-rsgames = Правила RS Games.

# Rules variant choices (for menu display)
ninetynine-rules-variant-quentin_c = Quentin C
ninetynine-rules-variant-rs_games = RS Games

# Disabled action reasons
ninetynine-choose-first = Спочатку потрібно зробити вибір.
ninetynine-draw-first = Спочатку потрібно взяти карту.
