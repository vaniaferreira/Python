#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio.
#Indo de 10 até 0. Com uma pausa de 1 segundo entre eles.
from time import sleep
import emoji
for c in range (10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':boom:',use_aliases=True))
