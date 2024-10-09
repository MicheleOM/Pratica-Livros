# exercicios 3.1

'''Suponha que eu forneça uma pilha de chamada. Quais informações você pode retirar baseando-se apenas nesta pilha de chamada?

A pilha de chamadas mostra que a função sauda foi chamada recursivamente, passando o valor "maggie" como argumento para o parâmetro nome. Isso sugere que a função está repetindo sua execução, provavelmente sem um caso-base definido.
'''


# A pilha de chamada com recursão

#função recursiva para calcular a fatorial de um número

def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat (x-1)

x = 15
resultado = fat(x)
print("O fatorial de", x, "é", resultado)

