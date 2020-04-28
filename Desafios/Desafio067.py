#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será
#interrompido quando o número solicitado for negativo.

tabuada = 1
c = 1

while True:
        tabuada = int(input('Quer ver a tabuada de que valor: '))
        while c < 11 and tabuada > 0:
            print(tabuada, ' x ', c, ' = ', tabuada * c)
            c += 1
        if c == 11:
           c = 1
        if tabuada < 0:
            break
print('Fim')


