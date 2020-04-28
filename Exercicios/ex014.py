#While

impar = par = 0
n = 1
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} pares e {} ímpares.'.format(par,impar))
print('Acabou')
exit()

n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('Fim')

r = 'S'

while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar [S / N]:')).upper()
print('Fim')
