#Tuplas são imutavéis

lanche = ('hamburguer','suco','pizza','pudim', 'batata frita')
print(sorted(lanche))

print(len(lanche))
print(lanche)
print(lanche[2])

for comida in lanche:
    print('Eu vou comer {}'.format(comida))
print('Comi pra caramba')

for cont in range(0, len(lanche)):
    print (lanche[cont])
print('Comi pra caramba')

