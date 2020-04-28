#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
#de acordo com a idade:
#até 9 anos: mirim;
#até 14 anos:infantil;
#até 19 anos:junior;
#até 20 anos: senior;
#acima:master.

idade = int(input('Informe sua idade: '))

if idade == 9:
    print('Mirim'.format(idade))
elif idade >9 and idade<=14:
    print('Infantil',format(idade))
elif idade >14 and idade<=19:
    print('junior',format(idade))
elif idade <=20 and idade >19:
    print('Senior',format(idade))
elif idade >20:
    print('Master',format(idade))
else:
    print('Você não esta em nenhuma categoria. É considerado bebê com {} anos'.format(idade))

