#Melhore o desafio 61, perguntando  para o usuário se ele quer mostrar mais alguns termos . O programa encerra quando ele disser  que
#quer mostrar 0 termos.

primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
          print('{} ->'.format(termo), end='')
          termo += razao
          cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você deseja ver a mais'))
print('Fim')

