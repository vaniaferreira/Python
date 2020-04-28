#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

#Números primos são os números naturais que têm apenas dois divisores diferentes: o 1 e ele mesmo.
# Exemplos: 1) 2 tem apenas os divisores 1 e 2, portanto 2 é um número primo. 2) 17 tem apenas os divisores 1 e 17,
# portanto 17 é um número primo.

numero = int(input('Informe um número: '))
total = 0
for c in range(1,numero + 1):
    if numero % c == 0:
        print('\033[32m', end= '')
        total = total +  1
    else:
        print('\033[31m', end= '')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes '.format(numero,total))

if total == 2:
    print('Número é primo')
else:
    print('Número não é primo')