# Light Turret game messages

# Game name
game-name-lightturret = Световая турель

# Intro
lightturret-intro = Игра «Световая турель» началась! У каждого игрока есть турель мощностью { $power }. Стреляйте из турели, чтобы получать свет и монеты, но если количество света превысит вашу мощность, вы выбываете! Покупайте улучшения за монеты, чтобы увеличить свою мощность. Победит тот, у кого в конце игры будет больше всего света!

# Actions
lightturret-shoot = Выстрелить из турели
lightturret-upgrade = Купить улучшение (10 монет)
lightturret-check-stats = Проверить характеристики

# Action results
lightturret-shoot-result = { $player } стреляет из турели и получает { $gain } { $gain ->
    [one] единицу
    [few] единицы
   *[other] единиц
} света! Теперь в турели { $light } { $light ->
    [one] единица
    [few] единицы
   *[other] единиц
} света.
lightturret-coins-gained = { $player } получает { $coins } { $coins ->
    [one] монету
    [few] монеты
   *[other] монет
}! Теперь у игрока { $player } { $total } { $total ->
    [one] монета
    [few] монеты
   *[other] монет
}.
lightturret-buys-upgrade = { $player } покупает улучшение мощности!
lightturret-power-gained = { $player } получает { $gain } { $gain ->
    [one] единицу
    [few] единицы
   *[other] единиц
} мощности! Теперь её значение — { $power }.
lightturret-upgrade-accident = Улучшение случайно слилось с турелью! В результате в ней теперь { $light } { $light ->
    [one] единица
    [few] единицы
   *[other] единиц
} света.
lightturret-not-enough-coins = У вас недостаточно монет! Нужно { $need }, а у вас только { $have }.

# Elimination
lightturret-eliminated = Света стало слишком много для души игрока { $player }! { $player } выбывает!

# Stats
lightturret-stats-alive = { $player }: мощность { $power }, свет { $light }, монеты: { $coins }.
lightturret-stats-eliminated = { $player }: выбыл, накопив { $light } света.

# Game end
lightturret-game-over = Игра окончена!
lightturret-final-alive = { $player } закончил игру с результатом { $light }.
lightturret-final-eliminated = { $player } выбыл, набрав { $light } света.
lightturret-winner = { $player } побеждает со счётом { $light }!
lightturret-tie = Ничья при { $light } света!

# Options
lightturret-set-starting-power = Начальная мощность: { $power }
lightturret-enter-starting-power = Введите начальную мощность:
lightturret-option-changed-power = Начальная мощность установлена на { $power }.
lightturret-set-max-rounds = Макс. раундов: { $rounds }
lightturret-enter-max-rounds = Введите макс. количество раундов:
lightturret-option-changed-rounds = Максимальное количество раундов установлено на { $rounds }.

# Disabled action reasons
lightturret-you-are-eliminated = Вы выбыли из игры.
