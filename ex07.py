#Nicolas Lamback de Paulo
from math import pi


def raio_diametro(diametro):
    return (int(diametro) / 2)


def raio_circunferencia(circunferencia):
    return (float(circunferencia) / (2 * pi))


retorno_funcao = raio_diametro(10)
print(retorno_funcao)


retorno_funcao = raio_circunferencia(300)
print(round(retorno_funcao))
