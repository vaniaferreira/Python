#Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
#valor digitado e as suas respectivas posições da lista.

listanum = []
maior = menor = 0

for c in range (0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        else:
            menor = listanum[c]

print('-' * 30)

for pos, valor in enumerate(listanum):
    if valor == maior:
        print(f'O número maior digitado é o {maior} e a posição é a {pos}')
    elif valor == menor:
        print(f'O número menor digitado é o {menor} e a posição é a {pos}')

