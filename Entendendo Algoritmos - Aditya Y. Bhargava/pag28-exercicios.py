# pag.28 exercícios pesquisa binária

import math

# Suponha que você tenha uma lista com 128 nomes e esteja fazendo uma pesquisa binária. Qual seria o número máximo de etapas que você levaria para encontrar o nome desejado?

# Número de elementos na lista
n = 128

# Máximo de etapas
maxEtapas = math.log2(n)
print(maxEtapas)


# Suponha que você duplique o tamanho da lista. Qual seria o número máximo de etapas agora?

# Duplicando o tamanho da lista
nDuplicado = n * 2

# Máximo de etapas para lista duplicada
maxEtapasDuplicado = math.log2(nDuplicado)
print(maxEtapasDuplicado)

