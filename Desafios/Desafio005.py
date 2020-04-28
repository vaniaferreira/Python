# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor

n1 = int(input('Informe um número inteiro:'))

sucessor = n1 + 1
antecessor = n1 - 1

print('O Sucessor de n1 é: {}'.format(sucessor))
print('O Antecessor de n1 é: {}'.format(antecessor))

print('Para o valor {}, o sucessor é: {} e o antecessor é {}'.format(n1, (n1+1),(n1-1)))

