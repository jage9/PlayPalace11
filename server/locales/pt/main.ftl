# Mensagens principais da interface do PlayPalace (Português)

# Categorias de jogos
category-card-games = Jogos de Cartas
category-dice-games = Jogos de Dados
category-rb-play-center = RB Play Center
category-poker = Pôquer
category-uncategorized = Sem Categoria

# Títulos de menu
main-menu-title = Menu Principal
play-menu-title = Jogar
categories-menu-title = Categorias de Jogos
tables-menu-title = Mesas Disponíveis

# Itens de menu
play = Jogar
view-active-tables = Ver mesas ativas
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
whos-at-table = Quem está na mesa
check-scores = Ver pontuação
check-scores-detailed = Pontuação detalhada

# Mensagens de mesa
table-created = { $host } criou uma nova mesa de { $game }.
table-joined = { $player } entrou na mesa.
table-left = { $player } saiu da mesa.
new-host = { $player } agora é o anfitrião.
waiting-for-players = Aguardando jogadores. { $current }/{ $min } mínimo, { $max } máximo.
game-starting = O jogo está começando!
table-listing = Mesa de { $host } ({ $count } usuários)
table-listing-one = Mesa de { $host } ({ $count } usuário)
table-listing-with = Mesa de { $host } ({ $count } usuários) com { $members }
table-listing-game = { $game }: mesa de { $host } ({ $count } usuários)
table-listing-game-one = { $game }: mesa de { $host } ({ $count } usuário)
table-listing-game-with = { $game }: mesa de { $host } ({ $count } usuários) com { $members }
table-not-exists = A mesa não existe mais.
table-full = A mesa está cheia.
player-replaced-by-bot = { $player } saiu e foi substituído por um bot.
player-took-over = { $player } assumiu o controle do bot.
spectator-joined = Entrou na mesa de { $host } como espectador.
table-no-players = Sem jogadores.
table-players-one = { $count } jogador: { $players }.
table-players-many = { $count } jogadores: { $players }.
table-spectators = Espectadores: { $spectators }.

# Modo espectador
spectate = Assistir
now-playing = { $player } agora está jogando.
now-spectating = { $player } agora está assistindo.
spectator-left = { $player } parou de assistir.

# Geral
welcome = Bem-vindo ao PlayPalace!
goodbye = Até logo!

# Anúncios de presença do usuário
user-online = { $player } entrou online.
user-offline = { $player } saiu.
online-users-none = Nenhum usuário online.
online-users-one = 1 usuário: { $users }
online-users-many = { $count } usuários: { $users }
online-user-not-in-game = Fora do jogo
online-user-waiting-approval = Aguardando aprovação
user-is-admin = { $player } é um administrador do PlayPalace.
user-is-server-owner = { $player } é o proprietário do servidor PlayPalace.

# Opções
language = Idioma
language-option = Idioma: { $language }
language-changed = Idioma alterado para { $language }.

# Estados de opções booleanas
option-on = Ligado
option-off = Desligado

# Opções de som
turn-sound-option = Som de turno: { $status }

# Opções de dados
clear-kept-option = Limpar dados mantidos ao rolar: { $status }
dice-keeping-style-option = Estilo de manter dados: { $style }
dice-keeping-style-changed = Estilo de manter dados definido para { $style }.
dice-keeping-style-indexes = Índices dos dados
dice-keeping-style-values = Valores dos dados

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
no-active-tables = Não há mesas ativas.
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
my-stats-no-games = Você ainda não jogou nenhum jogo.
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
confirm-leave-game = Tem certeza de que deseja sair da mesa?
confirm-yes = Sim
confirm-no = Não

# Administração
administration = Administração
admin-menu-title = Administração

# Aprovação de contas
account-approval = Aprovação de Contas
account-approval-menu-title = Aprovação de Contas
no-pending-accounts = Não há contas pendentes.
approve-account = Aprovar
decline-account = Recusar
account-approved = A conta de { $player } foi aprovada.
account-declined = A conta de { $player } foi recusada e excluída.

# Aguardando aprovação (mostrado a usuários não aprovados)
waiting-for-approval = Sua conta está aguardando aprovação de um administrador. Por favor, aguarde...
account-approved-welcome = Sua conta foi aprovada! Bem-vindo ao PlayPalace!
account-declined-goodbye = Sua solicitação de conta foi recusada.
account-banned = Sua conta está banida e não pode ser acessada.

# Motivo da recusa
decline-reason-prompt = Digite um motivo para a recusa (ou pressione Escape para cancelar):
approval-reject-no-reason = Nenhum motivo fornecido.

# Notificações de admin para solicitações de conta
account-request = solicitação de conta
account-action = ação de conta realizada

# Promoção/rebaixamento de admin
promote-admin = Promover Admin
demote-admin = Rebaixar Admin
promote-admin-menu-title = Promover Admin
demote-admin-menu-title = Rebaixar Admin
no-users-to-promote = Não há usuários disponíveis para promover.
no-admins-to-demote = Não há admins disponíveis para rebaixar.
confirm-promote = Tem certeza de que deseja promover { $player } a admin?
confirm-demote = Tem certeza de que deseja rebaixar { $player } de admin?
broadcast-to-all = Anunciar a todos os usuários
broadcast-to-admins = Anunciar apenas aos admins
broadcast-to-nobody = Silencioso (sem anúncio)
promote-announcement = { $player } foi promovido a admin!
promote-announcement-you = Você foi promovido a admin!
demote-announcement = { $player } foi rebaixado de admin.
demote-announcement-you = Você foi rebaixado de admin.
not-admin-anymore = Você não é mais um admin e não pode realizar esta ação.
not-server-owner = Apenas o proprietário do servidor pode realizar esta ação.

# Transferência de propriedade do servidor
transfer-ownership = Transferir Propriedade
transfer-ownership-menu-title = Transferir Propriedade
no-admins-for-transfer = Não há admins disponíveis para transferir a propriedade.
confirm-transfer-ownership = Tem certeza de que deseja transferir a propriedade do servidor para { $player }? Você será rebaixado a admin.
transfer-ownership-announcement = { $player } agora é o proprietário do servidor Play Palace!
transfer-ownership-announcement-you = Você agora é o proprietário do servidor Play Palace!
