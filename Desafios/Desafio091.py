#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
#No final, coloque esse dicionário em ordem, sabendo que, o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

dados = dict()
ranking = list()

dados['Jogador1'] = randint(1,7)
dados['Jogador2'] = randint(1,7)
dados['Jogador3'] = randint(1,7)
dados['Jogador4'] = randint(1,7)

print('-'*30)
print(f'{"Valores sorteados":^30}')
print('-'*30)

for k, v in dados.items():
    print(f'O {k} tirou {v}')
    sleep(1)

print('-' * 30)
print(f'{"Ranking dos Jogadores":^30}')
print('-' * 30)

ranking = sorted(dados.items(),key=itemgetter(1), reverse=True)

print(ranking)

for i, v in enumerate(ranking):
    print(f'{i} lugar:  {v[0]} com {v[1]}')







