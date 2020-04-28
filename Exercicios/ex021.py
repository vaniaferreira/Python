# Docstrings

def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: não tem retorno
    Função criada por Vânia em 15/04/2020
    """
    c = 1
    while c<= f:
        print(f'{c}', end=' ')
        c += p
    print('Fim')

help(contador)

def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma de {a}, {b} e {c} é {s}')


somar(1, 2)


def somatoria(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somatoria(3, 2, 5)
r2 = somatoria(1, 7)
r3 = somatoria(4)
print(f'Meus cálculos deram: {r1}, {r2} e {r3}')




