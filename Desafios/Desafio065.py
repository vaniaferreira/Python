#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi
#o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = media = maior = menor = cont = soma = 0
continuar = 'S'

while continuar == 'S':
    num = int(input('Digite um número: '))
    continuar = str(input('Você deseja continuar? [S / N]: ')).strip().upper()
    cont += 1
    soma += num
    media = (soma / cont)
    if num > maior:
        maior = num
    else:
        menor = num
print('A média dos valores digitados foi {:.2f}'.format(media))
print('O maior valor digitado foi {} e o menor {}'.format(maior, menor))
print('Fim')
