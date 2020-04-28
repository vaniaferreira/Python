#Reescreva a função leiaInt() que fizemos no desafio 104,Incluindo agora a possibilidade da digitação de um número
# de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError or TypeError):
            print('Digite um valor inteiro válido!')
            continue
        except KeyboardInterrupt:
            print('Usuário decidiu não informar valor inteiro!')
            return 0
        else:
             return n

def leiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError or TypeError):
            print('Digite um valor real válido!')
            continue
        except KeyboardInterrupt:
            print('Usuário decidiu não informar valor Real!')
            return 0
        else:
             return f

n = leiaint('Digite um número inteiro: ')
f = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro: {n}')
print(f'Você digitou o número real: {f}')
