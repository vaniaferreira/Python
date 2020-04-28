# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

#10*5/100 - Lê-se 5 porcento de 10

preco = float(input('Informe o preço do produto:'))
porcentagem = float(preco * 0.05)
desconto = float(preco - porcentagem)

novo = preco - (preco * 5 /100)

print('O produto informado estava {}, com desconto de 5%, passou a valer {:.2f}'.format(preco, desconto))
print('O produto informado estava {}, com desconto de 5%, passou a valer {:.2f}'.format(preco, novo))