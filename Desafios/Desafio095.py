#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.
lista = dict()
campeonato = []
total = 0

while True:
    lista['nome'] = str(input('Nome: '))
    lista['partidas'] = int(input(f'Quantas partidas {lista["nome"]} jogou? '))

    for n in range(1,lista["partidas"]+1):
        campeonato.append(int(input(f'Quantos gols na partida {n}? ')))
    lista['gols'] = campeonato

    resp = str(input('Deseja continuar?' ))

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

    for n in range(1, lista["partidas"] + 1):
        print(f'Na partida {n} fez {lista["gols"][n-1]} gols.',end=' ')
        print()

    if resp in 'Nn':
        break

