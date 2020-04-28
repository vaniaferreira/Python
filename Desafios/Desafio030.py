#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

n1 = int(input('Digite um número inteiro: '))
resultado = n1 % 2
if resultado == 0:
    print('O número é par')
else:
    print('o número é impar')