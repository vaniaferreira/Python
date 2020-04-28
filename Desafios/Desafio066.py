#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999.
#Que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando a flag.

n = soma = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
print('A soma é {}'.format(soma))
