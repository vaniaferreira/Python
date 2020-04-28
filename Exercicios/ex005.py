# Ordem de Precedência
# []
# **
# * / // %(resto da divisao)
# + -

nome = input('Qual seu nome?')
print ('Prazer em te conhecer {}!'.format(nome))

n1 = int(input('Informe n1: '))
n2 = int(input('Informe n2: '))
soma = n1 + n2
divisao = n1 / n2
divisaointeira = n1 // n2
multiplicacao = n1 * n2
potencia = n1 ** n2
print('A soma é: {}, A Divisão é: {:.3} , A Divisão Inteira é: {}, A Multiplicação é: {}, A Potência é: {}'.format(soma,divisao,divisaointeira,multiplicacao,potencia))




