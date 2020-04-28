# Crie um programa que leia qto dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar.
# Considere 1 dolar igual a 3,27 reais

n1 = float(input('Informe o valor que tem na carteira R$: '))
conversao = n1 / 3.27
print('Com R${}, você poderá comprar US${:.2f}!'.format(n1,conversao))

