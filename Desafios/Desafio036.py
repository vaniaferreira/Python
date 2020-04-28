#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder a 30% do salário ou então o empréstimo será negado.

print('Programa para empréstimo bancário...')

casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual seu último salário: '))
anos = int(input('Quantos anos deseja pagar?'))
excedeu =  (salario * 30 / 100)
prestacao = casa / (anos * 12)
saldo = excedeu - prestacao

if prestacao >= excedeu:
    print('Sua prestação mensal {:.2f} excedeu {:.2f} a 30% do salário {:.2f}, seu empréstimo foi negado'.format(prestacao,excedeu,salario))
else:
    print('Sua prestação mensal é de {:.2f} e será paga em {} anos. Você tem {:.2f} de saldo para não comprometer sua renda.'.format(prestacao,anos,saldo))

