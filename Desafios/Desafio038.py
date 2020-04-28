#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior;
#O segundo valor é maior;
#Não existe valor maior, os dois são iguais;

n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))

if n1 > n2:
    print('O valor de {} é maior que {}'.format(n1,n2))
elif n2 > n1:
    print('O valor de {} é maior que {}'.format(n2, n1))
else:
    print('Não existe valor maior. Os dois {}, {} são iguais'.format(n1, n2))