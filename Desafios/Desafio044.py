#Elabore um programa que calcule o valor a ser pago de um produto, considerando o seu preço normal e condição de pagamento:
#a vista dinheiro / cheque 10% desconto
#A vista no cartão: 5% de desconto
#em até 2x, preço normal
#3x ou mais no cartão, 20% de juros.

print('Programa que calcula o valor a ser pago')
produto = float(input('informe o valor do produto: '))
print('informe condição de pagamento')
print('1 - À Vista dinheiro ou cheque - 10% de desconto:')
print('2 - À Vista cartão - 5% de desconto:')
print('3 - Em até 2x sem acréscimo:')
print('4 - 3x ou mais no cartão - 20% de juros:')
opcao = int(input('Escolha uma opção para prosseguir: '))

if opcao == 1:
    preço = produto - (produto *10 / 100)
    print('Escolhendo a opção 1, o produto sairá por {} ao invés de {}'.format(preço,produto))
elif opcao == 2:
    preço = produto - (produto * 5 / 100)
    print('Escolhendo a opção 2, o produto sairá por {} ao invés de {}'.format(preço, produto))
elif opcao == 3:
     print('Escolhendo a opção 3, o produto sairá pelo mesmo valor {}, porém pagará em 2x'.format(produto))
elif opcao == 4:
    preço = produto + (produto * 20 / 100)
    print('Escolhendo a opção 4, o produto sairá por {} ao invés de {}, porém pagará em 3x ou mais'.format(preço, produto))
else:
    print('Opção informada inexistente!')




