#Crie um programa que tenha uma tupla com várias palavras(Não usar acentos).
#Depois disto, você deve mostrar, para cada palavra, quais são suas vogais.

palavras = ('Mamão','Pao','Queijo', 'Danone', 'Cafe', 'Leite')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ',end='')
    for letra in p:
        if letra.lower() in ('aeiou'):
            print(letra, end=' ')


