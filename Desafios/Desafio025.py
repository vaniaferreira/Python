#Crie um programa que Leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input("Digite seu nome completo: ")).strip() #Elimina espaço antes e depois
retorno = nome.find('SILVA')
print(retorno)

if retorno == - 1:
    print('Não existe SILVA em seu nome')
if retorno >= 1:
    print('Existe SILVA em seu nome')

print('Seu nome tem Silva?{}'.format('SILVA' in nome.upper()))