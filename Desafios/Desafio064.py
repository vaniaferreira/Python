#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999
#que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. (desconsiderando o flag)

num = 0
cont = 0
soma = 0

while num != 999:
    num = int(input('Tente acertar o número de parada: '))
    cont += 1
    soma += num
print('Você acertou!, tentou {} vezes e a soma foi {}'.format(cont -1, soma-num))
