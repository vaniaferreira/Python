#Listas
# (Tuplas) --> São imutavéis
# [Listas] --> Podem ser mutavéis
# {Dicionário}

num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(len(num))
num.insert(2,0)
print(num)
#Elimina o último item da lista
num.pop()
print(num)
num.pop(2)
print(num)
num.remove(2)
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)

print('-' * 50)
print(f'{"Valores":^50}')
print('-' * 50)

valores = list()

valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(v)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao fim da lista')

lista = list()

for cont in range(0,5):
    lista.append(int(input('Digite um valor: ')))
  
for c, cont in enumerate(lista):
    print(f'Na posição {c} encontrei o valor {cont}')

print('-' * 30)
a = [2,3,4,7]
b = a[:] #Copia todos os elementos de A na B
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')


