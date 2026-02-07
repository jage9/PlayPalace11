# Messages for Left Right Center (Mongolian)

# Game name
game-name-leftrightcenter = Зүүн Баруун Төв

# Actions
lrc-roll = { $count } { $count ->
    [one] шоо
   *[other] шоо
} шидэх

# Dice faces
lrc-face-left = Зүүн
lrc-face-right = Баруун
lrc-face-center = Төв
lrc-face-dot = Цэг

# Game events
lrc-roll-results = { $player } { $results } гаргалаа.
lrc-pass-left = { $player } { $count } { $count ->
    [one] чип
   *[other] чип
} { $target }-д зүүн тийш дамжууллаа.
lrc-pass-right = { $player } { $count } { $count ->
    [one] чип
   *[other] чип
} { $target }-д баруун тийш дамжууллаа.
lrc-pass-center = { $player } { $count } { $count ->
    [one] чип
   *[other] чип
} төвд тавилаа.
lrc-no-chips = { $player } шидэх чипгүй байна.
lrc-center-pot = Төвд { $count } { $count ->
    [one] чип
   *[other] чип
} байна.
lrc-player-chips = { $player } одоо { $count } { $count ->
    [one] чип
   *[other] чип
} байна.
lrc-winner = { $player } { $count } { $count ->
    [one] чип
   *[other] чип
}-ээр ялалт байгууллаа!

# Options
lrc-set-starting-chips = Эхлэх чип: { $count }
lrc-enter-starting-chips = Эхлэх чип оруулна уу:
lrc-option-changed-starting-chips = Эхлэх чип { $count } болов.
