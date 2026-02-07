# Chaos Bear game messages

# Game name
game-name-chaosbear = Kaotisk björn

# Actions
chaosbear-roll-dice = Kasta tärningar
chaosbear-draw-card = Dra ett kort
chaosbear-check-status = Kontrollera status

# Game intro (3 separate messages like v10)
chaosbear-intro-1 = Kaotisk björn har börjat! Alla spelare börjar 30 rutor framför björnen.
chaosbear-intro-2 = Kasta tärningar för att flytta framåt och dra kort på multipler av 5 för att få speciella effekter.
chaosbear-intro-3 = Låt inte björnen fånga dig!

# Turn announcement
chaosbear-turn = { $player }s tur; ruta { $position }.

# Rolling
chaosbear-roll = { $player } kastade { $roll }.
chaosbear-position = { $player } är nu på ruta { $position }.

# Drawing cards
chaosbear-draws-card = { $player } drar ett kort.
chaosbear-card-impulsion = Impuls! { $player } flyttar framåt 3 rutor till ruta { $position }!
chaosbear-card-super-impulsion = Superimpuls! { $player } flyttar framåt 5 rutor till ruta { $position }!
chaosbear-card-tiredness = Trötthet! Björnens energi minus 1. Den har nu { $energy } energi.
chaosbear-card-hunger = Hunger! Björnens energi plus 1. Den har nu { $energy } energi.
chaosbear-card-backward = Knuff bakåt! { $player } flyttar tillbaka till ruta { $position }.
chaosbear-card-random-gift = Slumpmässig gåva!
chaosbear-gift-back = { $player } gick tillbaka till ruta { $position }.
chaosbear-gift-forward = { $player } gick framåt till ruta { $position }!

# Bear turn
chaosbear-bear-roll = Björnen kastade { $roll } + sin { $energy } energi = { $total }.
chaosbear-bear-energy-up = Björnen kastade 3 och fick 1 energi!
chaosbear-bear-position = Björnen är nu på ruta { $position }!
chaosbear-player-caught = Björnen fångade { $player }! { $player } har besegrats!
chaosbear-bear-feast = Björnen förlorar 3 energi efter att ha festmåltid på deras kött!

# Status check
chaosbear-status-player-alive = { $player }: ruta { $position }.
chaosbear-status-player-caught = { $player }: fångad på ruta { $position }.
chaosbear-status-bear = Björnen är på ruta { $position } med { $energy } energi.

# End game
chaosbear-winner = { $player } överlevde och vinner! De nådde ruta { $position }!
chaosbear-tie = Det är oavgjort på ruta { $position }!

# Disabled action reasons
chaosbear-you-are-caught = Du har blivit fångad av björnen.
chaosbear-not-on-multiple = Du kan bara dra kort på multipler av 5.
