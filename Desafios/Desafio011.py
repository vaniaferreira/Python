# Faça um programa que leia a altura e largura de uma parede em metros. Calcule sua área e a quantidade de tinta necessária
# para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m2.

altura = float(input('Informe a altura da parede em metros: '))
largura = float(input('Informe a largura da parede em metros:'))
area = float(altura * largura)
tinta_necessaria = float(area / 2)

print('Para altura {} e largura {}, é necessário {} litros de tinta para a área {}'.format(altura, largura, tinta_necessaria, area))
