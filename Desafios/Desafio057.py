#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Caso esteja errado, peça a digitação
#novamente até ter um valor correto.

#Guanabara:

sexo = str(input('Digite seu sexo: [F / M]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, por favor, digite seu sexo: [F / M]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))

#Eu:

sexo = 'x'

while  sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo: [F / M]: ')).upper().strip()
print('ACABOU')


