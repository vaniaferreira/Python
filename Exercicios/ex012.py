#Condições aninhadas
#if: elif: else:

nome = str(input('Qual é seu nome: '))

if nome == 'Cadu':
    print('Que nome bonito')
elif nome == 'Maria'or nome == 'José' or nome == 'João':
    print('Que nome simples')
elif nome in 'Claudia, Ana, Abelardo, Antônio, Pedro':
    print('Belo nome!')
else:
    print('Que nome diferente!')

print('Tenha um bom dia, {}!'.format(nome))
