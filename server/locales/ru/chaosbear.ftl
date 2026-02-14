# Chaos Bear game messages

# Game name
game-name-chaosbear = Медведь Хаоса

# Actions
chaosbear-roll-dice = Бросить кубики
chaosbear-draw-card = Взять карту
chaosbear-check-status = Проверить статус

# Game intro (3 separate messages like v10)
chaosbear-intro-1 = Игра «Медведь Хаоса» началась! Все игроки начинают в 30 клетках впереди медведя.
chaosbear-intro-2 = Бросайте кубики, чтобы двигаться вперёд, и берите карты на каждой 5-й клетке, чтобы получить особые эффекты.
chaosbear-intro-3 = Не дайте медведю поймать вас!

# Turn announcement
chaosbear-turn = Ход игрока { $player }; клетка { $position }.

# Rolling
chaosbear-roll = { $player } выбрасывает { $roll }.
chaosbear-position = { $player } теперь на клетке { $position }.

# Drawing cards
chaosbear-draws-card = { $player } берёт карту.
chaosbear-card-impulsion = Импульс! { $player } продвигается на 3 клетки вперёд, на клетку { $position }!
chaosbear-card-super-impulsion = Супер-импульс! { $player } продвигается на 5 клеток вперёд, на клетку { $position }!
chaosbear-card-tiredness = Усталость! Энергия медведя снижена на 1. Теперь у него { $energy } энергии.
chaosbear-card-hunger = Голод! Энергия медведя увеличена на 1. Теперь у него { $energy } энергии.
chaosbear-card-backward = Толчёк назад! { $player } отступает на клетку { $position }.
chaosbear-card-random-gift = Случайный подарок!
chaosbear-gift-back = { $player } возвращается на клетку { $position }.
chaosbear-gift-forward = { $player } проходит вперёд на клетку { $position }!

# Bear turn
chaosbear-bear-roll = Медведь выбросил { $roll } + { $energy } (энергия) = итого { $total }.
chaosbear-bear-energy-up = Медведь выбросил 3 и получил 1 единицу энергии!
chaosbear-bear-position = Медведь теперь на клетке { $position }!
chaosbear-player-caught = Медведь поймал игрока { $player }! { $player } проигрывает!
chaosbear-bear-feast = Медведь теряет 3 единицы энергии, полакомившись его плотью!

# Status check
chaosbear-status-player-alive = { $player }: клетка { $position }.
chaosbear-status-player-caught = { $player }: пойман на клетке { $position }.
chaosbear-status-bear = Медведь находится на клетке { $position }, энергия: { $energy }.

# End game
chaosbear-winner = { $player } выжил и победил! Он достиг клетки { $position }!
chaosbear-tie = Ничья на клетке { $position }!

# Disabled action reasons
chaosbear-you-are-caught = Вас поймал медведь.
chaosbear-not-on-multiple = Карты можно брать только на клетках, кратных 5.
