#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

#Progressão aritmética é um tipo de seqüência numérica que a partir do segundo elemento cada termo (elemento) é a soma do seu antecessor
# por uma constante. (5,7,9,11,13,15,17) essa seqüência é uma Progressão aritmética, pois os seus elementos são formados pela soma do seu
# antecessor com a constante 2.

termo = int(input('Informe o primeiro termo: '))
razão = int(input('Informe a razão: '))
decimo = termo + (10 - 1) * razão
for c in range(termo,decimo,razão):
    print('{}'.format(c), end=' -')


