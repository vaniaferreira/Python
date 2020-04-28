#Interropendo repetições while

cont = 1
while cont <=10:
    print(cont, ' ', end='')
    cont += 1
print('Fim')

n = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
print('A soma é {}'.format(soma))

nome = 'Jose'
idade = 33
#print(f 'O {nome} tem {idade} anos')




