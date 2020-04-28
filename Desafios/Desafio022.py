#Crie um programa  que leia o nome completo da pessoa e mostre
#o nome com todas as letras maiusculas
#o nome com todas minusculas
#Qtas letras ao to do(sem considerar espaços)
#Qtas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()#elimina espaço antes e depois
print('Analisando seu nome...')
print('Seu nome maíusculo é {}'.format(nome.upper()))
print('Seu nome minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ' )))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))








