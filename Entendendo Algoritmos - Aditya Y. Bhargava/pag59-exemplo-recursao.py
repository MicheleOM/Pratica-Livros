# Primeira abordagem: loop while - enquanto o monte existir, pegue uma caixa e olhe o que tem dentro dela

def procure_pela_chave(caixa_principal):
    pilha = caixa_principal.crie_uma_pilha_para_busca()
    while pilha is not vazia:
        caixa = pilha.pegue_caixa()
        for item in caixa:
            if item.e_uma_caixa():
                pilha.append(item)
            elif item.e_uma_chave():
                print ("achei a chave!")



# Segunda abordagem: recursão - quandoa  função chama a si mesma

def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item)
        elif item.e_uma_chave():
            print ("achei a chave!")

