#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a ctps for diferente
#de zero, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar(35 anos de contribuição).

from _datetime import date
ano = date.today().year
aposentadoria = dict()

aposentadoria['nome'] = str(input('Nome: '))
aposentadoria['ano_nascto'] = int(input('Ano de Nascimento: '))

if aposentadoria['ano_nascto'] != 0:
    aposentadoria['idade'] = ano - aposentadoria['ano_nascto']

aposentadoria['ctps'] = int(input('CTPS - Caso não tenha digite 0: '))

if aposentadoria['ctps'] > 0:
    aposentadoria['ano_contratacao'] = int(input('Ano de Contratação: '))
    aposentadoria['aposentadoria'] = aposentadoria['ano_contratacao'] + 35
    aposentadoria['salario'] = float(input('Salário: '))

for k, v in aposentadoria.items():
    print(f'{k} tem o valor {v}')



