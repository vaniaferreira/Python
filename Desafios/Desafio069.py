#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário
#quer ou não continuar. No final, mostre:
#Quantas pessoas tem mais de 18 anos:
#Quantos homens foram cadastrados:
#Quantas mulheres tem menos de 20 anos.

idade = homens = mulheres = mais_dezoito = 0
sexo = continuar = 'S'

while continuar == 'S':
    idade = int(input('Infor e sua idade: '))
    if idade > 18:
        mais_dezoito += 1
    sexo = str(input('Informe seu sexo [F / M]: ')).strip().upper()
    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        if idade < 20:
            mulheres += 1
    continuar = str(input('Pessoa cadastrada com sucesso! Deseja continuar [S / N]: ')).strip().upper()

print('{} pessoas tem mais de 18 anos.'.format(mais_dezoito))
print('{} homens foram cadastrados.'.format(homens))
print('{} mulheres tem menos de 20 anos.'.format(mulheres))



