#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar a 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.

import emoji

velocidade = float(input('Digite quantos KM/H você esta: '))

if velocidade >80:
    nova_velocidade = velocidade - 80
    valor = 7 * nova_velocidade
    print('Você foi multado! Sua multa é de R$: {:.2f}'.format(valor))
    print(emoji.emojize(':smile:',use_aliases=True))
else:
    if velocidade ==80:
        print('Você esta de acordo com a velocidade da via')

if velocidade <80:
   print('Você esta muito lerdo, pisa ai!')
   print(emoji.emojize(':rage:',use_aliases=True))


