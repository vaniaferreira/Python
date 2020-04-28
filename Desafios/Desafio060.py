#Faça um programa que leia um número qualquer e mostre o seu fatorial
#ex:5! = 5x4x3x2x1=120

numero = 0
import math
numero = int(input('Informe um número: '))
fatorial = math.factorial(numero)
print('O fatorial deste número é {}'.format(fatorial))

n = 0
c = 0
f = 1

n = int(input('Informe um número: '))
c = n
while c > 0:
      print('{}'.format(c), end='')
      print(' x ' if c > 1 else ' = ', end ='')
      f *= c
      c -= 1
print('\nO fatorial de {} é {}'.format(n, f))













