# Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário com 15 % de aumento.

salario = float(input('Informe seu salário: '))
porcentagem = float(salario * 0.15)
novo_salario = float(salario + porcentagem)

novo = salario + (salario * 15/100)

print('Seu salário atual é: {}, com reajuste de 15% ficou: {:.2f}'.format(salario,novo_salario))
print('Seu salário atual é: {}, com reajuste de 15% ficou: {:.2f}'.format(salario,novo))