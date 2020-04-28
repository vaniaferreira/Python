#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de
#vitórias consecutivas que ele conquistou  no final do jogo.

soma = total = cont = 0

from random import randint

while True:
    print('Par ou Ímpar entre 0 e 10')
    computador = randint(0,10)
    jogador = int(input('Digite um valor inteiro entre 0 e 10: '))
    escolha = str(input('Digite Par ou Ímpar [P / I]: ')).strip().upper()
    soma = computador + jogador

    if soma % 2 == 0:
        total = 'P'
    else:
        total = 'I'

    print('Computador escolheu {} e jogador escolheu {}. A soma foi {}'.format(computador, jogador, soma))

    if total == escolha:
        print('Jogador venceu, vamos jogar novamente!')
        cont += 1
    else:
        print('Jogador perdeu, Game Over!')
        break

print('Placar de Final do Jogo')
print('Quantidade de vezes vencidas pelo jogador foi de {}'.format(cont))
