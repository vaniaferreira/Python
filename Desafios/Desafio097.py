#Faça um programa que tenha uma função chamada escreva ().
#Que receberá um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável

def escreva(frase):
    print('~' * len(frase))
    print(frase)
    print('~' * len(frase))

frase = "O sapo não lava o pé"
frase1 = "Lavou"
escreva(frase)
escreva(frase1)






