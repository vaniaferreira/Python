#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados em ordem crescente.

numeros = list()

while True:
    n = int(input('Digite um valor:'))
    if n not in numeros:
        numeros.append(n)
        print(f'O número {n} foi adicionado com sucesso.')
    else:
        print(f'O número {n} não foi adicionado, pois é repetido')
    continuar = str(input('Deseja continuar [S/N] ?'))
    if continuar in 'Nn':
        break
print(f'Ordem crescente {sorted(numeros)}')
