#Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual será a base de conversão
#1 para binário
#2 para octal
#3 para hexadecimal

import math
numero = int(input('Digite um número inteiro qualquer: '))

base = input('''Escolha qual base de conversão deseja:
        [1] - Binário
        [2] - Octal
        [3] - Hexadecimal ''')
if base == '1':
    print('Convertido o numero {} em Binário {}'.format(numero,bin(numero)[2:]))
elif base == '2':
    print('Convertido o numero {} em Octal {}'.format(numero, oct(numero)[2:]))
elif base == '3':
    print('Convertido o numero {} em Hexadecimal {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida, tente novamente!')