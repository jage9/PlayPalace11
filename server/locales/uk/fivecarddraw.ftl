# Five Card Draw

game-name-fivecarddraw = П'ять карт

draw-set-starting-chips = Початкові фішки: { $count }
draw-enter-starting-chips = Введіть початкові фішки
draw-option-changed-starting-chips = Початкові фішки встановлено на { $count }.

draw-set-ante = Анте: { $count }
draw-enter-ante = Введіть суму анте
draw-option-changed-ante = Анте встановлено на { $count }.

draw-set-turn-timer = Таймер ходу: { $mode }
draw-select-turn-timer = Виберіть таймер ходу
draw-option-changed-turn-timer = Таймер ходу встановлено на { $mode }.

draw-set-raise-mode = Режим підвищення: { $mode }
draw-select-raise-mode = Виберіть режим підвищення
draw-option-changed-raise-mode = Режим підвищення встановлено на { $mode }.

draw-set-max-raises = Максимум підвищень: { $count }
draw-enter-max-raises = Введіть максимум підвищень (0 для необмеженого)
draw-option-changed-max-raises = Максимум підвищень встановлено на { $count }.

draw-antes-posted = Анте внесено: { $amount }.
draw-betting-round-1 = Раунд ставок.
draw-betting-round-2 = Раунд ставок.
draw-begin-draw = Фаза обміну.
draw-not-draw-phase = Зараз не час для обміну.
draw-not-betting = Ви не можете робити ставки під час фази обміну.

draw-toggle-discard = Перемкнути скидання для карти { $index }
draw-card-keep = { $card }, утримується
draw-card-discard = { $card }, буде скинута
draw-card-kept = Зберегти { $card }.
draw-card-discarded = Скинути { $card }.
draw-draw-cards = Взяти карти
draw-draw-cards-count = Взяти { $count } { $count ->
    [one] карту
   *[other] карт
}
draw-dealt-cards = Вам роздано { $cards }.
draw-you-drew-cards = Ви берете { $cards }.
draw-you-draw = Ви берете { $count } { $count ->
    [one] карту
   *[other] карт
}.
draw-player-draws = { $player } бере { $count } { $count ->
    [one] карту
   *[other] карт
}.
draw-you-stand-pat = Ви залишаєтесь з тим, що є.
draw-player-stands-pat = { $player } залишається з тим, що є.
draw-you-discard-limit = Ви можете скинути до { $count } карт.
draw-player-discard-limit = { $player } може скинути до { $count } карт.
