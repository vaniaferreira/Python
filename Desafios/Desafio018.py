#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

num = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(num))
cosseno = math.cos(math.radians(num))
tangente = math.tan(math.radians(num))
print ('Para o ângulo {}, o seno é {:.2f}, cosseno é {:.2f} e a tangente é {:.2f}'.format(num,seno, cosseno, tangente))

