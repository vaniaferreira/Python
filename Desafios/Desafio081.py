#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disto, mostre:
#Quantos números foram digitados;
#A lista de valores ordenada de forma decrescente;
#Se o valor 5 foi digitado e se esta ou não na lista.

valores = []

while True:
    valores.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? '))
    if continuar in ('Nn'):
        break
print('-' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse = True)
print(f'Lista em forma decrescente {valores}')

if 5 in valores:
    print('Valor 5 contém na lista')
else:
    print('Valor 5 NÃO contém na lista')

print('Fim')
