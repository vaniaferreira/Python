#For
for c in range(0,5):
    print(c)
    print('Fim')
print('-=' * 11)
for c in range(5,0, -1):
    print(c)
    print('Fim')
print('-=' * 11)
for c in range(0,6,2):
    print(c)
    print('Fim')
print('-=' * 11)

n = int(input('Digite um número: '))
for c in range (0,n+1):
    print(n)
print('fim')

print('-=' * 20)

soma = 0
for c in range(1,5):
    n = int(input('Digite um valor: '))
    soma += n
print('A soma foi {}'.format(soma))
