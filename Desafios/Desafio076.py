#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência:
#No final, mostre uma listagem de preços, organizando os dados em uma forma tabular.

listagem = ('Pão', '1.70',
         'Leite', '4.75',
         'Carne', '15.00',
         'Feijão', '6.30',
         'Arroz', '15.75')

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for pos in range(0,len(listagem)):
    if pos % 2 ==0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>7}')
print('-' * 40)

