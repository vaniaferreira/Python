#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira.
import math
num = float(input('Digite um numero real: '))
print('A parte inteira do número {} é {}'.format(num,math.trunc(num),))


