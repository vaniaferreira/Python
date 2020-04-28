#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
r1 = float(input('Informe valor de R1: '))
r2 = float(input('Informe valor de R2: '))
r3 = float(input('Informe valor de R3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas informadas podem formar um triangulo')
else:
    print('As retas informadas não podem formar um triangulo')
