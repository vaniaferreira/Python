#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do aumento. Para salários superiores a R$1250
#calcule o aumento de 10%, para inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe seu salário:'))

if salario <= 1250:
    print('Seu novo salário será: {}'.format(salario + (salario * 15) / 100))
else:
    print('Seu novo salário será: {}'.format(salario + (salario * 10) / 100))
