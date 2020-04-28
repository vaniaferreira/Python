#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo. Desconsiderando os espaços.
frase2 = str(input('Digite uma frase: ')).strip()
frase2 = frase2.replace(' ','')
tamanho = len(frase2)
total = ''

for c in range(tamanho -1, -1, -1):
   total = total + frase2[c]
print(total)

if total == frase2:
   print('A frase é um palíndromo')
else:
   print('A frase não é um palíndromo')

#Solução pelo Guanabara

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)

if junto == inverso:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')


