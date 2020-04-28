#Desenvolva um programa  que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#se o valor digitado por ímpar, desconsidere-o.
soma = 0
for c in range(0,6):
    numero = int(input('Digite um número inteiro:'))
    if numero % 2 == 0:
        soma = soma + numero
print('A soma dos números pares é: {}'.format(soma))



