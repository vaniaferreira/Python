#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
#ex: 1834, unidade 4, dezena 3, centena 8, milhar 1

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

tam = len(num)
print (tam)

if tam == 1:
    print('Unidade é {}'.format(num[0]))
if tam == 2:
    print('Dezena é {}'.format(num[0]))
    print('Unidade é {}'.format(num[1]))
if tam == 3:
    print('Centena é {}'.format(num[0]))
    print('Dezena é {}'.format(num[1]))
    print('Unidade é {}'.format(num[2]))
if tam == 4:
    print ('Milhar é {}'.format(num[0]))
    print ('Centena é {}'.format(num[1]))
    print ('Dezena é {}'.format(num[2]))
    print ('Unidade é {}'.format(num[3]))


