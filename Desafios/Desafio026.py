#Faça um programa que leia uma frase pelo teclado e mostre:
# #quantas vezes aparece a letra 'A'
#Em que posição ela aparece a primeira vez;
#Em que posição ela aparece a última vez;

frase = str(input('Digite uma frase: ')).strip()
tam = len(frase)

print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira posição é {}'.format(frase[0:tam].find('A')))
print('A ultima posição é {}'.format(frase[0:tam].rfind('A')))

print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))
# mais um para começar com contador =1, sendo que no python começa com 0.