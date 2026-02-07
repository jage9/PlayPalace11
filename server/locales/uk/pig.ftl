# Pig game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-pig = Свиня
pig-category = Ігри з кубиками

# Actions
pig-roll = Кинути кубик
pig-bank = Зберегти { $points } очок

# Game events (Pig-specific)
pig-rolls = { $player } кидає кубик...
pig-roll-result = { $roll }, всього { $total }
pig-bust = О ні, 1! { $player } втрачає { $points } очок.
pig-bank-action = { $player } вирішує зберегти { $points }, всього { $total }
pig-winner = У нас є переможець, і це { $player }!

# Pig-specific options
pig-set-min-bank = Мінімум для збереження: { $points }
pig-set-dice-sides = Граней кубика: { $sides }
pig-enter-min-bank = Введіть мінімальну кількість очок для збереження:
pig-enter-dice-sides = Введіть кількість граней кубика:
pig-option-changed-min-bank = Мінімум очок для збереження змінено на { $points }
pig-option-changed-dice = Тепер кубик має { $sides } граней

# Disabled reasons
pig-need-more-points = Вам потрібно більше очок для збереження.

# Validation errors
pig-error-min-bank-too-high = Мінімум очок для збереження повинен бути меншим за цільовий рахунок.
