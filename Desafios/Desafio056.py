#Desenvolva o programa que leia o nome, idade, e sexo de 4 pessoas. No final, do programa mostre:
#a media de idade do grupo:
#qual é o nome do homem mais velho;
#quantas mulheres tem menos de 20 anos;
media = 0
Total_idade = 0
homem = 0
mulher = 0
mais_velho_idade = 0
mais_velho_nome = ''
menos_vinte = 0
cont_menos_vinte = 0


for c in range(1,5):
    nome = str(input('Digite o nome da {}ª pessoa:'.format(c)))
    idade = int(input('Digite a idade da {}ª pessoa:'.format(c)))
    sexo = str(input('Digite o sexo da {}ª pessoa:'.format(c))).upper()
    Total_idade += idade
    media = (Total_idade / 4)
    if c == 1:
        mais_velho_idade = idade
        mais_velho_nome = nome

    if sexo == 'F':
        menos_vinte = idade
        if menos_vinte < 20:
           cont_menos_vinte = cont_menos_vinte + 1
           print('menos vinte {}'.format(cont_menos_vinte))
    else:
         homem = homem + 1
         if idade > mais_velho_idade:
            mais_velho_idade = idade
            mais_velho_nome = nome

print('A média de idade do grupo é {}'.format(media))
print('O homem mais velho é o {} e sua idade é {}'.format(mais_velho_nome, mais_velho_idade))
print('{} mulheres tem menos de 20 anos'.format(cont_menos_vinte))


