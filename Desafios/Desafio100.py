#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somapar().
#A primeira função vai sortear 5 números e vai coloca-los dentro da lista.
#A segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteio(lista):
    for c in range (1,6):
        c = randint(1,10)
        numeros.append(c)


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos pares {lista} é de {soma}')


numeros = list()
sorteio(numeros)
somapar(numeros)

help(print)
