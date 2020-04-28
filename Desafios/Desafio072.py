#Crie um progama que tenha uma tupla totalmente preenchida com uma contagem por extensão de Zero até Vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.

numeros = ('zero','um', 'dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze',
           'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    c = int(input('Digite um número entre 0 e 20: '))
    if 0 <= c <= 20 :
        break
    print('Tente novamente!')

print(numeros[c])

