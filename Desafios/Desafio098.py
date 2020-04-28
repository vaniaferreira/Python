#Faça um programa que tenha uma função chamada contador(), que receba 3 parâmetros: inicio, fim e passo e realize a contagem.
#seu programa tem que realizar três contagens através da função criada:
# a - De 1 até 10, de 1 em 1

def contador(inicio, fim, passo):
    for c in range(inicio, fim+1, passo):
        print(f'{c}',end=' ')


contador(1, 10, 1)



