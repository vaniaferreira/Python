#Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a função input() do python, só que fazendo a validação
#para aceitar apenas valor númerico.
#ex: n = leiaint('Digite um n')

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m ERRO! Digite um número válido.\033[m')
        if ok:
            break
    return valor

n = leiaint('Digite um n: ')
print(f'Você digitou o número {n}')
