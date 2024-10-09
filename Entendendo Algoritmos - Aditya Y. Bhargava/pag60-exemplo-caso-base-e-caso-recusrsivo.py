# pag.60 - Caso base e caso recursivo

# Recursivo, rodando de forma infinita
def regressiva(i):
    print (i)
    regressiva(i-1)

# Caso base e caso recursivo
def regressiva(i):
    print (i)
    if i <= 1: 
        return
    else: 
        regressiva(i-1)
