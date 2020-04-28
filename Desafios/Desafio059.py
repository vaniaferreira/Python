#Crie um programa que leia 2 valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
numero1 = numero2 = opcao = 0

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

while opcao != 5:
    print('-=' * 15)
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do Programa ')
    print('-=' * 15)
    opcao = int(input('Escolha a opção no menu acima: '))
    if opcao == 1:
        print('A soma de {} + {} = {}'.format(numero1, numero2, numero1+numero2))
    elif opcao == 2:
        print('A multiplicação de {} x {} = {}'.format(numero1, numero2, numero1 * numero2))
    elif opcao == 3:
        if numero1 > numero2:
            print('O número maior entre {} e {} é {}'.format(numero1, numero2, numero1))
        else:
            print('O número maior entre {} e {} é {}'.format(numero2, numero1, numero2))
    elif opcao == 4:
        print('Informe novos números:')
        numero1 = int(input('Digite um número: '))
        numero2 = int(input('Digite outro número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente')
sleep(2)
print('Volte Sempre!')
