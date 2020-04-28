#Desenvolva uma lágica que leia o peso e a altura de uma pessoa. Calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
#abaixo de 18.5: Abaixo do peso;
#entre 18.5 e 25: Peso ideal;
#25 até 30: Sobrepeso;
#30 até 40: Obesidade;
#acima de 40: Obesidade mórbida.

print('Descubra seu IMC')
peso = float(input('Informe seu peso: '))
altura = float (input('Informe sua altura:'))
imc = peso / (altura ** 2)

print('Seu IMC é: {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso!')
elif imc > 18.5 and imc <=25:
    print('Peso ideal!')
elif imc > 25 and imc <=30:
    print('Sobrepeso!')
elif imc > 30 and imc <=40:
    print('Obesidade!')
elif imc > 40:
    print('Obesidade Mórbida!')