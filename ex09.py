#Nicolas Lamback de Paulo
def total(conta):
    return "R$" + str((float(conta) * (10 / 100))) + ", De gorjeta!"

retorno_funcao = total(100)
print(retorno_funcao)

retorno_funcao = total(50)
print(retorno_funcao)
