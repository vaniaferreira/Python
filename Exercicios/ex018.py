#Listas parte 2
teste = list ()
teste.append('Gustavo')
teste.append(40)
print(teste)

galera = list()
galera.append(teste[:])
teste[0]='Maria'
teste[1]=22
galera.append(teste[:])
print(galera)

galeras = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galeras)
print(galeras[0])
print(galeras[0][0])
print(galeras[0][1])
print(galeras[2][0])

for p in galeras:
    print(f'{p[0]} tem {p[1]} de idade')

time = list ()
dado = list ()
totalmaior = totalmenor = 0

for c in range (0,3):
    dado.append(str(input('Nome:')))
    dado.append(str(input('Idade: ')))
    time.append(dado[:])
    dado.clear()
print(time)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalmenor += 1
print(f'Total de maior é {totalmaior} e de menor é {totalmenor}')




