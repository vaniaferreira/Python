#Refaça o exercício 9, mostrando a tabuada de um numero que o usuário escolher, só que agora utilizando um laço for.

tabuada = int(input('Informe a tabuada que deseja ver pronta: '))

for c in range (0,11):
    print(tabuada, 'x', c, '=', tabuada*c)


