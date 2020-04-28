#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos
#durante o campeonato.

lista = dict()
campeonato = []
total = 0

lista['nome'] = str(input('Nome: '))
lista['partidas'] = int(input(f'Quantas partidas {lista["nome"]} jogou? '))

for n in range(1,lista["partidas"]+1):
    campeonato.append(int(input(f'Quantos gols na partida {n}? ')))
lista['gols'] = campeonato

for v in campeonato:
    total = total + v

lista['total'] = total

print('-' * 30)
print(lista)

print('-' * 30)

for k, v in lista.items():
    print(f'O campo {k} tem o valor {v}')

print('-' * 30)
print(f'O jogador {lista["nome"]} jogou {lista["partidas"]} partidas.')

print(lista["gols"][1])

for n in range(1, lista["partidas"] + 1):
    print(f'Na partida {n} fez {lista["gols"][n-1]} gols.',end=' ')
    print()






























