#Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa
#quadrado da hipotenusa é igual a soma dos quadrados dos catetos
import math

co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
hipotenusa = (co ** 2 + ca **2) ** (1/2)
hi = math.hypot(co,ca)
print('O valor do cateto oposto é {} e do cateto adjacente é {}. A hipotenusa é {:.2f} e da hi é {:.2f}'.format(co, ca, hipotenusa, hi))
