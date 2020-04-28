#Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando while

primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')
