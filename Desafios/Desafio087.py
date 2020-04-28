#Aprimore o desafio anterior, mostrando no final:
#A soma de todos os valores pares digitados:
#A soma dos valores da terceira coluna:
#O maior valor da segunda linha

matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = maior_valor = terceira_coluna = 0

for l in range  (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor {[l]}{[c]}: '))

for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()

print('-' * 30)

for l in range (0,3):
    for c in range (0,3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]

print(f'A Soma dos pares é: {soma}')

for l in range (0,3):
    for c in range (2,3):
        terceira_coluna += (matriz[l][c])

print(f'A Soma dos valores da terceira coluna é: {terceira_coluna}')

for l in range (1,2):
    for c in range (0,3):
        if c == 0:
            maior_valor = matriz[l][c]
        elif matriz[l][c] > maior_valor:
            maior_valor = matriz[l][c]
print(f'O maior valor da segunda linha é: {maior_valor}')



