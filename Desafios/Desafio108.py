#Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor
#monetário formatado.

import moeda

p = float(input('Preço: R$'))
t = int(input('Taxa %: '))
print(f'{t}% de {moeda.moeda(p)} é igual a {moeda.moeda(moeda.aumentar(p,t))} ')
print(f'-{t}% de {moeda.moeda(p)} é igual a {moeda.moeda(moeda.diminuir(p,t))}')
print(f'Dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')