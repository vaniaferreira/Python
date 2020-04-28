#Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
n1 = random.randint(0,5)
n2 = int(input('Informe um número de 0 a 5:'))
print('Numero escolhido pelo computador foi: {} e por você foi {}'.format(n1,n2))

if n1 == n2:
    print('Parabéns você acertou!')
else:
    print('número errado, tente novamente...')

