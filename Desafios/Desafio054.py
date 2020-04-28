#Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre qtas pessoas ainda não atingiram a maioridade e
#quantas já.

from datetime import date
ano = date.today().year
maioridade = 0
maior = 0
menor = 0
for c in range(0,7):
    nascimento = int(input('Digite seu ano de nascimento: '))
    maioridade = ano - nascimento
    if maioridade >=21:
        maior = maior + 1
    else:
        menor = menor + 1
print('Atingiram a maioridade {}'.format(maior))
print('Não atingiram a maioridade {}'.format(menor))