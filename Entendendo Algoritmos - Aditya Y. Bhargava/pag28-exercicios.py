# pag.28 exercícios pesquisa binária

import math

# Número de elementos na lista
n = 128

# Máximo de etapas
maxEtapas = math.ceil(math.log2(n))
print(maxEtapas)




# Duplicando o tamanho da lista
nDuplicado = n * 2

# Máximo de etapas para lista duplicada
maxEtapasDuplicado = math.ceil(math.log2(nDuplicado))
print(maxEtapasDuplicado)

