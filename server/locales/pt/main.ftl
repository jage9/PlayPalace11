# Mensagens principais da interface do PlayPalace (Português)

# Categorias de jogos
category-card-games = Jogos de Cartas
category-dice-games = Jogos de Dados
category-rb-play-center = RB Play Center
category-uncategorized = Sem Categoria

# Títulos de menu
main-menu-title = Menu Principal
play-menu-title = Jogar
categories-menu-title = Categorias de Jogos
tables-menu-title = Mesas Disponíveis

# Itens de menu
play = Jogar
options = Opções
logout = Sair
back = Voltar
create-table = Criar uma nova mesa
join-as-player = Entrar como jogador
join-as-spectator = Entrar como espectador
leave-table = Sair da mesa
start-game = Iniciar jogo
add-bot = Adicionar bot
remove-bot = Remover bot
actions-menu = Menu de ações
save-table = Salvar mesa
whose-turn = De quem é a vez
check-scores = Ver pontuação
check-scores-detailed = Pontuação detalhada

# Mensagens de mesa
table-created = { $host } criou uma nova mesa de { $game }.
table-joined = { $player } entrou na mesa.
table-left = { $player } saiu da mesa.
new-host = { $player } agora é o anfitrião.
waiting-for-players = Aguardando jogadores. { $current }/{ $min } mínimo, { $max } máximo.
game-starting = O jogo está começando!
table-listing = Mesa de { $host } ({ $count } jogadores)
table-not-exists = A mesa não existe mais.
table-full = A mesa está cheia.
player-replaced-by-bot = { $player } saiu e foi substituído por um bot.
player-took-over = { $player } assumiu o controle do bot.
spectator-joined = Entrou na mesa de { $host } como espectador.

# Modo espectador
spectate = Assistir
now-playing = { $player } agora está jogando.
now-spectating = { $player } agora está assistindo.

# Geral
welcome = Bem-vindo ao PlayPalace!
goodbye = Até logo!

# Opções
language = Idioma
language-english = Inglês
language-portuguese = Português
language-option = Idioma: { $language }
language-changed = Idioma alterado para { $language }.

# Nomes de bots
cancel = Cancelar
no-bot-names-available = Nenhum nome de bot disponível.
select-bot-name = Selecione um nome para o bot
enter-bot-name = Digite o nome do bot
no-options-available = Nenhuma opção disponível.
no-scores-available = Nenhuma pontuação disponível.

# Salvar/Restaurar
saved-tables = Mesas Salvas
no-saved-tables = Você não tem mesas salvas.
restore-table = Restaurar
delete-saved-table = Excluir
saved-table-deleted = Mesa salva excluída.
missing-players = Não é possível restaurar: estes jogadores não estão disponíveis: { $players }
table-restored = Mesa restaurada! Todos os jogadores foram transferidos.
table-saved-destroying = Mesa salva! Voltando ao menu principal.
game-type-not-found = Este tipo de jogo não existe mais.

# Placares
leaderboards = Placares
leaderboards-menu-title = Placares
leaderboards-select-game = Selecione um jogo para ver seu placar
leaderboard-no-data = Ainda não há dados de placar para este jogo.

# Tipos de placar
leaderboard-type-wins = Líderes em Vitórias
leaderboard-type-rating = Classificação de Habilidade
leaderboard-type-total-score = Pontuação Total
leaderboard-type-high-score = Maior Pontuação
leaderboard-type-games-played = Jogos Disputados
leaderboard-type-avg-points-per-turn = Média de Pontos por Turno
leaderboard-type-best-single-turn = Melhor Turno
leaderboard-type-score-per-round = Pontuação por Rodada

# Cabeçalhos de placar
leaderboard-wins-header = { $game } - Líderes em Vitórias
leaderboard-total-score-header = { $game } - Pontuação Total
leaderboard-high-score-header = { $game } - Maior Pontuação
leaderboard-games-played-header = { $game } - Jogos Disputados
leaderboard-rating-header = { $game } - Classificação de Habilidade
leaderboard-avg-points-header = { $game } - Média de Pontos por Turno
leaderboard-best-turn-header = { $game } - Melhor Turno
leaderboard-score-per-round-header = { $game } - Pontuação por Rodada

# Entradas de placar
leaderboard-wins-entry = { $rank }: { $player }, { $wins } { $wins ->
    [one] vitória
   *[other] vitórias
} { $losses } { $losses ->
    [one] derrota
   *[other] derrotas
}, { $percentage }% de vitórias
leaderboard-score-entry = { $rank }. { $player }: { $value }
leaderboard-avg-entry = { $rank }. { $player }: { $value } média
leaderboard-games-entry = { $rank }. { $player }: { $value } jogos

# Estatísticas do jogador
leaderboard-player-stats = Suas estatísticas: { $wins } vitórias, { $losses } derrotas ({ $percentage }% de vitórias)
leaderboard-no-player-stats = Você ainda não jogou este jogo.

# Placar de classificação de habilidade
leaderboard-no-ratings = Ainda não há dados de classificação para este jogo.
leaderboard-rating-entry = { $rank }. { $player }: { $rating } classificação ({ $mu } ± { $sigma })
leaderboard-player-rating = Sua classificação: { $rating } ({ $mu } ± { $sigma })
leaderboard-no-player-rating = Você ainda não tem classificação neste jogo.

# Menu Minhas Estatísticas
my-stats = Minhas Estatísticas
my-stats-select-game = Selecione um jogo para ver suas estatísticas
my-stats-no-data = Você ainda não jogou este jogo.
my-stats-header = { $game } - Suas Estatísticas
my-stats-wins = Vitórias: { $value }
my-stats-losses = Derrotas: { $value }
my-stats-winrate = Taxa de vitórias: { $value }%
my-stats-games-played = Jogos disputados: { $value }
my-stats-total-score = Pontuação total: { $value }
my-stats-high-score = Maior pontuação: { $value }
my-stats-rating = Classificação de habilidade: { $value } ({ $mu } ± { $sigma })
my-stats-no-rating = Ainda sem classificação de habilidade
my-stats-avg-per-turn = Média de pontos por turno: { $value }
my-stats-best-turn = Melhor turno: { $value }

# Sistema de previsão
predict-outcomes = Prever resultados
predict-header = Resultados Previstos (por classificação de habilidade)
predict-entry = { $rank }. { $player } (classificação: { $rating })
predict-entry-2p = { $rank }. { $player } (classificação: { $rating }, { $probability }% de chance de vitória)
predict-unavailable = Previsões de classificação não estão disponíveis.
predict-need-players = Necessário pelo menos 2 jogadores humanos para previsões.
action-need-more-humans = Necessário mais jogadores humanos.
