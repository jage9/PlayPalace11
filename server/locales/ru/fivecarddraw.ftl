# Five Card Draw

game-name-fivecarddraw = Пятикарточный покер

draw-set-starting-chips = Стартовые фишки: { $count }
draw-enter-starting-chips = Введите стартовое количество фишек
draw-option-changed-starting-chips = Стартовое количество фишек установлено на { $count }.

draw-set-ante = Анте: { $count }
draw-enter-ante = Введите размер анте
draw-option-changed-ante = Размер анте установлен на { $count }.

draw-set-turn-timer = Таймер хода: { $mode }
draw-select-turn-timer = Выберите таймер хода
draw-option-changed-turn-timer = Таймер хода установлен на { $mode }.

draw-set-raise-mode = Режим повышения: { $mode }
draw-select-raise-mode = Выберите режим повышения
draw-option-changed-raise-mode = Режим повышения установлен на { $mode }.

draw-set-max-raises = Макс. повышений: { $count }
draw-enter-max-raises = Введите макс. количество повышений (0 — без ограничений)
draw-option-changed-max-raises = Максимальное количество повышений установлено на { $count }.

draw-antes-posted = Анте внесены: { $amount }.
draw-betting-round-1 = Раунд торгов.
draw-betting-round-2 = Раунд торгов.
draw-begin-draw = Фаза обмена.
draw-not-draw-phase = Сейчас не время для обмена карт.
draw-not-betting = Вы не можете делать ставки в фазе обмена.

draw-toggle-discard = Переключить сброс карты { $index }
draw-card-keep = { $card }, оставлена
draw-card-discard = { $card }, будет сброшена
draw-card-kept = Оставить карту: { $card }.
draw-card-discarded = Сбросить карту: { $card }.
draw-draw-cards = Обменять карты
draw-draw-cards-count = Взять { $count } { $count ->
    [one] карту
    [few] карты
   *[other] карт
}
draw-dealt-cards = Вам сдали: { $cards }.
draw-you-drew-cards = Вы получили при обмене: { $cards }.
draw-you-draw = Вы берёте { $count } { $count ->
    [one] карту
    [few] карты
   *[other] карт
}.
draw-player-draws = { $player } берёт { $count } { $count ->
    [one] карту
    [few] карты
   *[other] карт
}.
draw-you-stand-pat = Вы не меняете карты.
draw-player-stands-pat = { $player } не меняет карты.
draw-you-discard-limit = Вы можете сбросить до { $count } { $count ->
    [one] карты
    [few] карт
   *[other] карт
}.
draw-player-discard-limit = { $player } может сбросить до { $count } { $count ->
    [one] карты
    [few] карт
   *[other] карт
}.