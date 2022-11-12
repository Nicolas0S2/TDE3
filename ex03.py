#Nicolas Lamback de Paulo
def positivo_negativo(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'


retorno_funcao = positivo_negativo(10)
print(retorno_funcao)

retorno_funcao = positivo_negativo(-10)
print(retorno_funcao)
