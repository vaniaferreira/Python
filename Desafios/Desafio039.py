#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar;
#se é a hora de se alistar;
#se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou o tempo que passou do prazo.

from datetime import date
atual = date.today().year
nascimento = int(input('Informe sua data de nascimento: '))
idade = (atual - nascimento)
if idade ==18 or idade ==17:
    print('É hora de se alistar!')
elif idade >18:
    anos = idade - 18
    print('Já passou o tempo de alistamento, precisamente {} anos!'.format(anos))
    ano = (atual - anos)
    print('Seu alistamento foi em {}!'.format(ano))
elif idade < 18:
    anos = 18 - idade
    print('Você ainda vai se alistar ao serviço militar. Daqui precisamente {} anos!'.format(anos))
    ano = (atual + anos)
    print('Seu alistamento será em {}!'.format(ano))