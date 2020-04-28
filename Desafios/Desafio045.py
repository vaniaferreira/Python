#Crie um programa que faça o computador jogar jokenpô com você
#Jokenpo é uma brincadeira japonesa, onde dois jogadores escolhem um dentre três possíveis itens: Pedra, Papel ou Tesoura.
# O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.
# As regras são as seguintes: Pedra empata com Pedra e ganha de Tesoura.

from random import randint
from time import sleep

lista = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
    [0] Pedra
    [1] Papel
    [2] Tesoura''')
jogador = int(input('Qual sua jogada:'))

if jogador != 0 and jogador !=1 and jogador !=2:
    print('Opção inválida!')
    exit()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 11)
print('Computador jogou: {}'.format(computador))
print('Jogador jogou: {}'.format(jogador))
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('Empate, ambos jogaram Pedra!')
    elif jogador == 1:
        print('Computador Pedra e Jogador Papel!')
    elif jogador == 2:
        print('Computador Pedra e Jogador Tesoura!')
        print('Computador Ganhou!')
elif computador == 1:
    if jogador == 0:
        print('Computador Papel e Jogador Pedra!')
    elif jogador == 1:
        print('Empate, ambos jogaram Papel!')
    elif jogador == 2:
        print('Computador Papel e Jogador Tesoura!')
elif computador == 2:
    if jogador == 0:
        print('Computador Tesoura e Jogador Pedra!')
        print('Jogador ganhou!')
    elif jogador == 1:
        print('Computador Tesoura e Jogador Papel!')
    elif jogador == 2:
        print('Empate, ambos jogaram Tesoura!')


