#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#Qual é o total gasto na compra
#Quantos produtos custam mais de R$1000
#Qual é o nome do produto mais barato.

print('-'*17)
print('Lojão vende tudo')
print('-'*17)

continuar = 'S'
produto = barato =  ''
preco = total = mais_mil = menor_preco = total = cont = 0

while continuar == 'S':
    produto = str(input('Produto: '))
    preco = float(input('Preço: '))
    total += preco
    cont += 1

    if preco > 1000:
        mais_mil += 1

    if cont == 1:
        menor_preco = preco
        barato = produto
    else:
        if preco < menor_preco:
            menor_preco = preco
            barato = produto

    continuar = str(input('Deseja continuar[S/N]?')).strip().upper()

    if continuar == 'N':
        break

print('O Total da compra foi de R${:.2f}'.format(total))
print('{} produtos custam mais de R$1000'.format(mais_mil))
print('O Produto {} tem o custo {} mais barato'.format(barato, menor_preco))