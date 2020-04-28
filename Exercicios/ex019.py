#Dicionários
pessoas = {'Nome': 'Gustavo','Sexo': 'Masculino','idade':'22'}
print(pessoas)
print(pessoas['Nome'])
print(f'O {pessoas["Nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k,v in pessoas.items():
    print(f'{k} = {v}')

del pessoas ['Sexo']
print(pessoas)

pessoas['Nome'] = 'Leandro'
print(pessoas)

pessoas['Peso'] = 98.5
print(pessoas)

brasil = []
estado1 = {'uf:' 'Rio de Janeiro', 'Sigla:' 'RJ'}
estado2 = {'uf:' 'São Paulo', 'Sigla:' 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v,end=' ')



