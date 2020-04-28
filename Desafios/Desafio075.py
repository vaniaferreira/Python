#Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#Quantas vezes apareceu o número 9;
#Em que posição foi digitado o primeiro número 3.
#Quais foram os números pares.

numeros = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite mais outro número: ')))

print('Você digitou os valores {}'.format(numeros))
print('Número 9 apareceu {} vezes'.format(numeros.count(9)))

if 3 in numeros:
    print('Número 3 apareceu na posição {}'.format(numeros.index(3)))
else:
    print('Não existe número 3 na Tupla.')

for n in numeros:
    if n % 2 == 0:
        print('Números Pares digitados {}'.format(n))


