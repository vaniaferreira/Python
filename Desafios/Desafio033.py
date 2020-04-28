#Faça um programa que leia três números e mostre qual é o maior e o menor.


a = int(input('Informe um número:'))
b = int(input('Informe outro número: '))
c = int(input('Informe mais outro número: '))

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor é o {}'.format(menor))
print('O maior valor é o {}'.format(maior))