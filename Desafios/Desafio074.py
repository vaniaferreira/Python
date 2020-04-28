#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados
# # E também indique o menor e o maior valores que estão na tupla.

from random import randint

numeros = randint(0,5), randint(0,5), randint(0,5), randint(0,5), randint(0,5)
print('Os valores sorteados foram:'.format(numeros))
for n in numeros:
    print('',n,end=' ')

print('\nO maior número foi {}'.format(max(numeros)))
print('O menor número foi {}'.format(min(numeros)))




