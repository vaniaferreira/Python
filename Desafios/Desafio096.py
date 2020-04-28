#Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a
#área do terreno.

def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno {larg}x{comp} é de {a}m2')



print(f'Controle de Terrenos')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)







