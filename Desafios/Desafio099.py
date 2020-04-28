#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual é o maior.

def maior (* numeros):
    cont = 0
    for num in numeros:
        if cont == 0:
            m = num
        if num >= m:
            m = num
            cont += 1
    print(f'O maior dos {numeros} é o {m}')

maior(4, 5, 2, 14, 23, 3, 8)
#maior(5, 6, 2)
