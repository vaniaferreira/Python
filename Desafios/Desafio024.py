#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input("Digite o nome da cidade: ")).strip() #Eliminar espaços antes e depois
cidade = cidade.split()
valor = cidade[0]

if valor == 'SANTO':
    print('Cidade contém SANTO')

if valor != 'SANTO':
    print('Cidade não contém SANTO')


cid = str(input("Digite o nome da cidade: ")).strip() #Eliminar espaços antes e depois
print(cid[:5].upper()== 'SANTO')