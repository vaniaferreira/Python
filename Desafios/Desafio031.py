#Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por KM
#para viagens de até 200 km e R$0,45 para viagens mais longas.

distancia = float(input('Digite a distância de uma viagem: '))
if distancia <=200:
   print('O preço da viagem é de {}'.format(distancia*0.45))
else:
    print('O preço da viagem é de {}'.format((distancia*0.50)))

