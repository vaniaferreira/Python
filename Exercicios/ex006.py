import math
import random
import emoji

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é: {}'.format(num, math.floor(raiz)))

#floor --> arrendonda pra baixo
#ceil --> arredonda pra cima
#from math import sqrt, floor, ceil

#random - mostra numeros aleatorios entre 0 e 1
n1 = random.randint(1,10)
print(n1)
print(emoji.emojize(':heart:',use_aliases=True))
print(emoji.emojize(':sunglasses:',use_aliases=True))
print(emoji.emojize(':smile:',use_aliases=True))
print(emoji.emojize(':kissing:',use_aliases=True))








