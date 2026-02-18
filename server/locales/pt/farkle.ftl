# Mensagens do jogo Farkle (Português)

# Informações do jogo
game-name-farkle = Farkle

# Ações - Rolar e Bancar
farkle-roll = Rolar { $count } { $count ->
    [one] dado
   *[other] dados
}
farkle-bank = Bancar { $points } pontos

# Ações de combinação de pontuação (igual ao v10)
farkle-take-single-one = Um 1 por { $points } pontos
farkle-take-single-five = Um 5 por { $points } pontos
farkle-take-three-kind = Três { $number }s por { $points } pontos
farkle-take-four-kind = Quatro { $number }s por { $points } pontos
farkle-take-five-kind = Cinco { $number }s por { $points } pontos
farkle-take-six-kind = Seis { $number }s por { $points } pontos
farkle-take-small-straight = Sequência Pequena por { $points } pontos
farkle-take-large-straight = Sequência Grande por { $points } pontos
farkle-take-three-pairs = Três pares por { $points } pontos
farkle-take-double-triplets = Dupla trinca por { $points } pontos
farkle-take-full-house = Full house por { $points } pontos

# Eventos do jogo (igual ao v10)
farkle-rolls = { $player } rola { $count } { $count ->
    [one] dado
   *[other] dados
}...
farkle-you-roll = Você rola { $count } { $count -> [one] dado [other] dados }...
farkle-roll-result = { $dice }
farkle-farkle = FARKLE! { $player } perde { $points } pontos
farkle-you-farkle = FARKLE! Você perde { $points } pontos
farkle-takes-combo = { $player } pega { $combo } por { $points } pontos
farkle-you-take-combo = Você pega { $combo } por { $points } pontos
farkle-hot-dice = Dados quentes!
farkle-banks = { $player } banca { $points } pontos para um total de { $total }
farkle-you-bank = Você banca { $points } pontos para um total de { $total }
farkle-winner = { $player } vence com { $score } pontos!
farkle-you-win = Você venceu com { $score } pontos!
farkle-winners-tie = Temos um empate! Vencedores: { $players }

# Ação de verificar pontuação do turno
farkle-turn-score = { $player } tem { $points } pontos neste turno.
farkle-no-turn = Ninguém está jogando no momento.

# Opções específicas do Farkle
farkle-set-target-score = Pontuação alvo: { $score }
farkle-enter-target-score = Digite a pontuação alvo (500-5000):
farkle-option-changed-target = Pontuação alvo definida para { $score }.

# Razões para ações desabilitadas
farkle-must-take-combo = Você deve pegar uma combinação primeiro.
farkle-cannot-bank = Você não pode bancar agora.

# Additional Farkle options
farkle-set-initial-bank-score = Pontuação inicial para bancar: { $score }
farkle-enter-initial-bank-score = Digite a pontuação inicial para bancar (0-1000):
farkle-option-changed-initial-bank-score = Pontuação inicial para bancar definida para { $score }.
farkle-toggle-hot-dice-multiplier = Multiplicador de hot dice: { $enabled }
farkle-option-changed-hot-dice-multiplier = Multiplicador de hot dice definido para { $enabled }.

# Action feedback
farkle-minimum-initial-bank-score = A pontuação mínima inicial para bancar é { $score }.
