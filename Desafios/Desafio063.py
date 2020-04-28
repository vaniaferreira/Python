#Faça um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia fibonacci.
#ex: 0-1-1-2-3-5-8

continuar = 'S'
cont = 1
anterior1 = anterior2 = num = 0
termos = 1

while continuar == 'S':
    num = int(input('Digite um número: '))
    termos = int(input('Quantos termos você quer mostrar da série: '))
    while termos > 0:
        anterior1 = num - 1
        anterior2 = num - 2
        proximo = (num + anterior1 + anterior2)
        print('O numero {} tem como sequência Fibonacci {}'.format(num,proximo))
        num = proximo
        termos = termos -1
    continuar = str(input('Deseja continuar? [S / N]')).strip().upper()
print('Fim')
