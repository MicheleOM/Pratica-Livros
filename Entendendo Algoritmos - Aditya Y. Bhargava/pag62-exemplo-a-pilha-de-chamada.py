# pag.62 - A pilha de chamada

def sauda(nome):
    print ("Olá, " + nome + "!")
    sauda2(nome)
    print ("preparando para dizer tchau...")
    tchau()

# Esta função te cumprimenta e chama outras duas funções:

def sauda2(nome):
    print ("Como vai " + nome + "?")
def tchau():
    print ("ok, tchau!")
