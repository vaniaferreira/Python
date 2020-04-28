#Faça um programa que ajude um jogador da mega sena a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma
#lista completa.

from random import randint

lista = []
jogos = []
cont = 0
tot = 1

print('-' * 30)
print(f'{"JOGO DA MEGASENA":^30}')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))

while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'Sorteando {quant} de jogos','-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')



