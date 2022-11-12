#Nicolas Lamback de Paulo
def conta_letrinhas(string, letrinha):
    contagem = str(string).count(letrinha)
    return contagem


retorno_funcao = conta_letrinhas('Se você não sabe onde quer ir, qualquer caminho serve! ;)', 'a')
print(retorno_funcao)
