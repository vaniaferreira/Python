#Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente
#Ex:Ana Maria de Souza. Primeiro Ana, último Souza

nome = str(input('Informe seu nome completo: ')).strip()
dividido = nome.split()
dividido_final = nome.rsplit()
tam = len(dividido_final)
print(tam)
print('O Primeiro nome é {}'.format(dividido[0]))
print('O último nome é {}'.format(dividido_final[tam-1]))

print('Seu primeiro nome é {}'.format(dividido[0]))
print('Seu último nome é {}'.format(dividido[len(dividido)-1]))
