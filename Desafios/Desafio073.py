#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois
#mostre:
#Apenas os 5 primeiros colocados;
#Os últimos 4 colocados da tabela;
#Uma lista com os times em ordem alfabética;
#Em que posição da tabela esta o time da Flamengo.

campeonato = ('Atletico-PR', 'Atlético-GO','Atlético-MG','Bahia','Botafogo','Bragantino','Ceará','Corinthians','Coritiba','Flamengo',
              'Fluminense','Fortaleza','Goiás','Grêmio','Internacional','Palmeiras','Santos','São Paulo','Sport','Vasco')

print('5 primeiros colocados: ')
for c in range (0,5):
    print(campeonato[c])

print('4 últimos colocados na tabela: ')
print(campeonato[-5:])

print('Lista com os times em ordem alfabética: ')
print(sorted(campeonato))

print('Posição da tabela que esta o Flamengo: ')
print(campeonato.index('Flamengo'))



