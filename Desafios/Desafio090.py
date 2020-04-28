#Faça um programa que leia nome e média de um aluno. Guardando também a situação em um dicionário. No final, mostre a estrutura final na tela.

situacao = dict()
situacao['nome'] = str(input('Nome: '))
situacao['media'] = float(input('Media: '))

if situacao['media'] >= 7:
    situacao['Situacao'] = 'Aprovado'
else:
    situacao['Situacao'] = 'Reprovado'

for k, v in situacao.items():
    print(f'{k} é igual a {v}')






