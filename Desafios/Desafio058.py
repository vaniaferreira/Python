# Melhore o jogo do desafio 028 onde o computador vai pensar em um número de 0 a 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
n1 = 0
n2 = 1
palpite = 0

while n1 != n2:
    n1 = random.randint(0, 10)
    n2 = int(input('Informe um número de 0 a 10:'))
    print('Numero escolhido pelo computador foi: {} e por você foi {}'.format(n1,n2))
    if n1 != n2:
       palpite += 1
       print('número errado, tente novamente...')
    else:
        print('Parabéns você acertou! Foram necessários {} palpites para vencer!'.format(palpite))
print('Acabou')

