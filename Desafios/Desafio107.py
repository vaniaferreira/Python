#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

p = float(input('Preço: R$'))
t = int(input('Taxa %: '))
print(f'{t}% de {p} é igual a {moeda.aumentar(p,t)} ')
print(f'-{t}% de {p} é igual a {moeda.diminuir(p,t)}')
print(f'Dobro de {p} é {moeda.dobro(p)}')
print(f'Metade de {p} é {moeda.metade(p)}')


