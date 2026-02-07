# 1-4-24 (Midnight) game messages
# Note: Common messages like round-start, turn-start, target-score are in games.ftl

# Game info
game-name-midnight = 1-4-24
midnight-category = Ігри з кубиками

# Actions
midnight-roll = Кинути кубики
midnight-keep-die = Зберегти { $value }
midnight-bank = Зберегти

# Game events
midnight-turn-start = Хід { $player }.
midnight-you-rolled = Ви кинули: { $dice }.
midnight-player-rolled = { $player } кинув: { $dice }.

# Keeping dice
midnight-you-keep = Ви зберігаєте { $die }.
midnight-player-keeps = { $player } зберігає { $die }.
midnight-you-unkeep = Ви відміняєте збереження { $die }.
midnight-player-unkeeps = { $player } відміняє збереження { $die }.

# Turn status
midnight-you-have-kept = Збережені кубики: { $kept }. Залишилось кидків: { $remaining }.
midnight-player-has-kept = { $player } зберіг: { $kept }. { $remaining } кубиків залишилось.

# Scoring
midnight-you-scored = Ви набрали { $score } очок.
midnight-scored = { $player } набрав { $score } очок.
midnight-you-disqualified = У вас немає і 1, і 4. Дискваліфіковано!
midnight-player-disqualified = { $player } не має і 1, і 4. Дискваліфіковано!

# Round results
midnight-round-winner = { $player } виграє раунд!
midnight-round-tie = Нічия між { $players }.
midnight-all-disqualified = Всі гравці дискваліфіковані! Немає переможця цього раунду.

# Game winner
midnight-game-winner = { $player } виграє гру з { $wins } перемогами в раундах!
midnight-game-tie = Нічия! { $players } виграли по { $wins } раундів.

# Options
midnight-set-rounds = Раундів для гри: { $rounds }
midnight-enter-rounds = Введіть кількість раундів для гри:
midnight-option-changed-rounds = Раундів для гри змінено на { $rounds }

# Disabled reasons
midnight-need-to-roll = Спочатку потрібно кинути кубики.
midnight-no-dice-to-keep = Немає доступних кубиків для збереження.
midnight-must-keep-one = Ви повинні зберегти принаймні один кубик за кидок.
midnight-must-roll-first = Спочатку потрібно кинути кубики.
midnight-keep-all-first = Ви повинні зберегти всі кубики перед збереженням.
