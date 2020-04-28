#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário.
#E todos os dicionarios em uma lista. No final, mostre:
#Quantas pessoas foram cadastradas;
#A média de idade do grupo:
#Uma lista com todas as mulheres:
#uma lista com todas as pessoas com idade acima da média
pessoa = dict()
lista = []
media_idade_grupo = media = 0

while True:
    pessoa['nome'] = str(input('Nome:'))
    pessoa['sexo'] = str(input('Sexo: '))
    pessoa['idade'] = int(input('Idade: '))
    media_idade_grupo += pessoa['idade']
    lista.append(pessoa.copy())
    resp = str(input('Deseja continuar? '))
    if resp in 'Nn':
        break
print(f'Foram cadastradas {len(lista)} pessoas')
media = media_idade_grupo / len(lista)
print(f'A média de idade do grupo é de {media}')
print(f'A lista de mulheres foram: ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}',end=' ')
print(f'Lista geral com pessoas com idade acima da média foram' , end=' ')
for p in lista:
    if p['idade'] >= media:
        print(f'{p["nome"]}',end=' ')

