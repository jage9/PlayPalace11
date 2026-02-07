# Chaos Bear game messages

# Game name
game-name-chaosbear = Хаос Ведмідь

# Actions
chaosbear-roll-dice = Кинути кубики
chaosbear-draw-card = Взяти карту
chaosbear-check-status = Перевірити статус

# Game intro (3 separate messages like v10)
chaosbear-intro-1 = Хаос Ведмідь розпочався! Всі гравці починають на 30 клітинок попереду ведмедя.
chaosbear-intro-2 = Кидайте кубики, щоб рухатися вперед, і беріть карти на кратних 5, щоб отримати спеціальні ефекти.
chaosbear-intro-3 = Не дозволяйте ведмедю вас зловити!

# Turn announcement
chaosbear-turn = Хід { $player }; клітинка { $position }.

# Rolling
chaosbear-roll = { $player } кинув { $roll }.
chaosbear-position = { $player } тепер на клітинці { $position }.

# Drawing cards
chaosbear-draws-card = { $player } бере карту.
chaosbear-card-impulsion = Імпульс! { $player } рухається вперед на 3 клітинки до клітинки { $position }!
chaosbear-card-super-impulsion = Супер імпульс! { $player } рухається вперед на 5 клітинок до клітинки { $position }!
chaosbear-card-tiredness = Втома! Енергія ведмедя мінус 1. Тепер у нього { $energy } енергії.
chaosbear-card-hunger = Голод! Енергія ведмедя плюс 1. Тепер у нього { $energy } енергії.
chaosbear-card-backward = Поштовх назад! { $player } повертається на клітинку { $position }.
chaosbear-card-random-gift = Випадковий подарунок!
chaosbear-gift-back = { $player } повернувся на клітинку { $position }.
chaosbear-gift-forward = { $player } просунувся вперед до клітинки { $position }!

# Bear turn
chaosbear-bear-roll = Ведмідь кинув { $roll } + його { $energy } енергії = { $total }.
chaosbear-bear-energy-up = Ведмідь кинув 3 і отримав 1 енергію!
chaosbear-bear-position = Ведмідь тепер на клітинці { $position }!
chaosbear-player-caught = Ведмідь зловив { $player }! { $player } переможений!
chaosbear-bear-feast = Ведмідь втрачає 3 енергії після бенкету з їхньої плоті!

# Status check
chaosbear-status-player-alive = { $player }: клітинка { $position }.
chaosbear-status-player-caught = { $player }: зловлений на клітинці { $position }.
chaosbear-status-bear = Ведмідь на клітинці { $position } з { $energy } енергією.

# End game
chaosbear-winner = { $player } вижив і перемагає! Досяг клітинки { $position }!
chaosbear-tie = Нічия на клітинці { $position }!

# Disabled action reasons
chaosbear-you-are-caught = Вас зловив ведмідь.
chaosbear-not-on-multiple = Ви можете брати карти тільки на кратних 5.
