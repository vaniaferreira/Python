#Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o
#valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.import moeda
import moeda

p = float(input('Preço: R$'))
t = int(input('Taxa %: '))
print(f'{t}% de {moeda.moeda(p)} é igual a {moeda.aumentar(p,t,True)} ')
print(f'-{t}% de {moeda.moeda(p)} é igual a {moeda.diminuir(p,t, True)}')
print(f'Dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')