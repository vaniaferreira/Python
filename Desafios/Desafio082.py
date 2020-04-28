#Crie um programa que vai ler vários números e colocar em uma lista. Depois disto:
#Crie duas listas extras que vão conter apenas os valores pares e os ímpares respectivamente.
#Ao final, mostre as 3 listas

valores = []
par = []
impar = []

while True:
    n = int(input('Insira um número: '))
    valores.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    continuar = str(input('Deseja continuar?'))
    if continuar in ('Nn'):
        break
print(f'A lista criada foi {valores}')
print(f'A lista par é {par}')
print(f'A lista Ímpar é {impar}')




