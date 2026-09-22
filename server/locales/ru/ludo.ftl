game-name-ludo = Лудо

ludo-roll-die = Бросить кубик
ludo-move-token = Передвинуть фишку
ludo-check-board = Посмотреть состояние доски
ludo-select-token = Выберите фишку для хода:

ludo-roll = { $player } выбрасывает { $roll }.
ludo-you-roll = Вы выбрасываете { $roll }.
ludo-no-moves = У игрока { $player } нет доступных ходов.
ludo-you-no-moves = У вас нет доступных ходов.
ludo-enter-board = { $player } ({ $color }) выводит фишку { $token } на поле.
ludo-move-track = { $player } ({ $color }) перемещает фишку { $token } на позицию { $position }.
ludo-enter-home = { $player } ({ $color }) заводит фишку { $token } в «дом».
ludo-home-finish = Фишка { $token } игрока { $player } ({ $color }) дошла до финиша. (Готово: { $finished }/4)
ludo-move-home = { $player } ({ $color }) перемещает фишку { $token } в «доме» (позиция { $position }/{ $total }).
ludo-captures = { $player } ({ $color }) сбивает фишку { $token } игрока { $captured_player } ({ $captured_color })! Она возвращается на базу.
ludo-extra-turn = { $player } выбрасывает 6. Дополнительный ход!
ludo-you-extra-turn = Вы выбросили 6. Дополнительный ход!
ludo-too-many-sixes = { $player } выбрасывает { $count } { $count ->
    [one] шестёрку
    [few] шестёрки
   *[other] шестёрок
} подряд. Последние ходы отменяются, ход завершён.
ludo-winner = { $player } ({ $color }) побеждает! Все 4 фишки в «доме».

ludo-board-player = { $player } ({ $color }): готово { $finished }/4
ludo-token-yard = Фишка { $token } (на базе)
ludo-token-track = Фишка { $token } (позиция { $position })
ludo-token-home = Фишка { $token } (в «доме», { $position }/{ $total })
ludo-token-finished = Фишка { $token } (финишировала)
ludo-last-roll = Последний бросок: { $roll }

ludo-set-max-sixes = Макс. шестёрок подряд: { $max_consecutive_sixes }
ludo-enter-max-sixes = Введите макс. количество шестёрок подряд
ludo-option-changed-max-sixes = Максимальное количество шестёрок подряд установлено на { $value }.
ludo-set-safe-start-squares = Безопасные стартовые клетки: { $safe_start_squares }
# English fallback until this locale has a translation.
ludo-desc-safe-start-squares = Make each player's starting square safe from capture
ludo-option-changed-safe-start-squares = Безопасные стартовые клетки: { $value }.
