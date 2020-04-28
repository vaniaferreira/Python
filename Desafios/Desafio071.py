#Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual o valor sacado (número inteiro) e o
#programa vai informar quantas cédulas de cada valor serão entregues.]
#obs: Considere que o caixa possui cédulas de R$50,R$20,R$10 e R$1.

print('Caixa Eletrônico')
print('Cédulas de R$50, R$20, R$10 e R$1')
valor = int(input('Qual valor deseja sacar hoje?'))
total = valor
ced = 50
total_ced = 0

while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print('{} total de cédulas {}'.format(total_ced,ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break

'''
inteira = 0
resto = 0

inteira = valor // 100
resto = valor % 100

if inteira !=0:
    if resto !=0:
        if resto >= 50:
            print('Serão entregues {} de R$50'.format((inteira * 2)+ 1))
            inteira = resto // 50
            resto = resto % 50
            if inteira != 0:
                print('Serão entregues {} de R$50'.format(inteira))
            if resto <= 50:
                inteira = resto // 20
                resto = resto % 20
                if inteira != 0:
                    print('Serão entregues {} de R$20'.format(inteira))
                inteira = resto // 10
                resto = resto % 10
                if inteira != 0:
                    print('Serão entregues {} de R$10'.format(inteira))
                inteira = resto // 1
                resto = resto % 1
                if inteira != 0 or resto != 0:
                    print('Serão entregues {} de R$1'.format(inteira + resto))
        else:
            print('Serão entregues {} de R$50'.format(inteira * 2))
            inteira = resto // 50
            resto = resto % 50
            if inteira != 0:
                print('Serão entregues {} de R$50'.format(inteira))
            if resto <= 50:
               inteira = resto // 20
               resto = resto % 20
               if inteira != 0:
                  print('Serão entregues {} de R$20'.format(inteira))
               inteira = resto // 10
               resto = resto % 10
               if inteira != 0:
                  print('Serão entregues {} de R$10'.format(inteira))
               inteira = resto // 1
               resto = resto % 1
               if inteira != 0 or resto != 0:
                  print('Serão entregues {} de R$1'.format(inteira + resto))
    else:
        print('Serão entregues {} de R$50'.format(inteira * 2))
else:
    inteira = resto // 50
    resto = resto % 50
    if inteira != 0:
        print('Serão entregues {} de R$50'.format(inteira))
    if resto >= 50:
        print('Resto >=50')
    else:
        inteira = resto // 20
        resto = resto % 20
        if inteira !=0:
            print('Serão entregues {} de R$20'.format(inteira))
        inteira = resto // 10
        resto = resto % 10
        if inteira !=0:
            print('Serão entregues {} de R$10'.format(inteira))
        inteira = resto // 1
        resto = resto % 1
        if inteira !=0 or resto !=0:
            print('Serão entregues {} de R$1'.format(inteira + resto))'''

