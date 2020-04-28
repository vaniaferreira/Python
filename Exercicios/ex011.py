#cores no terminal
# \033[0;33;44m
#onde o style é a fonte(0 - none), (1 - bold), (4 - underline) e (7 negative)
# onde o text é a cor do texto (30 - branco, 31 - vermelho, 32 - verde, 33 - amarelo, 34 - azul, 35 - roxo, 36 - ciano e 37 - cinza)
#onde back é a cor do fundo (40 - branco, 41 - vermelho, 42 - verde, 43 - amarelo, 44 - azul, 45 - roxo, 46 - ciano e 47 - cinza)

print('\033[1;31;43mOlá Mundo!\033[m')

#fundo vermelho e letra branca

print('\033[0;30;41mteste\033[m')

#fundo azul e letra amarela sublinhada

print('\033[4;33;44mteste\033[m')

#fundo amarelo e letra roxa

print('\033[1;35;43mteste\033[m')

#fundo verde e letra branca

print('\033[0;30;42mteste\033[m')

#fundo preto e letra cinza

print('\033[mteste\033[m')

#fundo branco e letra preta

print('\033[7;30mteste\033[m')

a = 3
b = 5

print('Os valores são \033[1;33m{}\033[m e \033[32m{}\033[m!!!'.format(a,b))

nome = 'Guanabara'

cores = {'limpa': '\033[m',
         'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
        'azul' : '\033[34m',
        'roxo' : '\033[35m',
        'ciano' : '\033[36m',
        'cinza' : '\033[37m',
         'pretoebranco': '\033[7;30m'
         }

print('Olá {}{}{} muito prazer!'.format('\033[1;34m',nome,'\033[m'))
print('Olá {}{}{} muito prazer!'.format(cores['pretoebranco'],nome,cores['limpa']))
print('olá {}{}{} muito prazer!'.format(cores['roxo'],nome,cores['limpa']))
print('olá {}{}{} muito prazer!'.format(cores['cinza'],nome,cores['limpa']))
print('olá {}{}{} muito prazer!'.format(cores['vermelho'],nome,cores['limpa']))
print('olá {}{}{} muito prazer!'.format(cores['verde'],nome,cores['limpa']))
print('olá {}{}{} muito prazer!'.format(cores['amarelo'],nome,cores['limpa']))
print('olá {}{}{} muito prazer!'.format(cores['ciano'],nome,cores['limpa']))


#onde o style é a fonte(0 - none), (1 - bold), (4 - underline) e (7 negative)
# onde o text é a cor do texto (30 - branco, 31 - vermelho, 32 - verde, 33 - amarelo, 34 - azul, 35 - roxo, 36 - ciano e 37 - cinza)
#onde back é a cor do fundo (40 - branco, 41 - vermelho, 42 - verde, 43 - amarelo, 44 - azul, 45 - roxo, 46 - ciano e 47 - cinza)

style = {
        'limpa': '\033[m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'negative': '\033[7m'
         }

nome = "Cadu"
print('olá {}{}{}'.format(style['bold'],nome,style['limpa']))
print('olá {}{}{}'.format(style['underline'],nome,style['limpa']))
print('olá {}{}{}'.format(style['negative'],nome,style['limpa']))

text = {
        'limpa': '\033[m',
        'branco': '\033[30m',
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'amarelo':'\033[33m',
        'azul': '\033[34m',
        'roxo': '\033[35m',
        'ciano': '\033[36m',
        'cinza': '\033[37m'
    }

print('olá {}{}{}'.format(text['branco'],nome,text['limpa']))
print('olá {}{}{}'.format(text['vermelho'],nome,text['limpa']))
print('olá {}{}{}'.format(text['verde'],nome,text['limpa']))
print('olá {}{}{}'.format(text['amarelo'],nome,text['limpa']))
print('olá {}{}{}'.format(text['azul'],nome,text['limpa']))
print('olá {}{}{}'.format(text['roxo'],nome,text['limpa']))
print('olá {}{}{}'.format(text['ciano'],nome,text['limpa']))
print('olá {}{}{}'.format(text['cinza'],nome,text['limpa']))

#onde back é a cor do fundo (40 - branco, 41 - vermelho, 42 - verde, 43 - amarelo, 44 - azul, 45 - roxo, 46 - ciano e 47 - cinza)

back = {
    'limpa': '\033[m',
    'branco': '\033[40m',
    'vermelho': '\033[41m',
    'verde': '\033[42m',
    'amarelo': '\033[43m',
    'azul': '\033[44m',
    'roxo': '\033[45m',
    'ciano': '\033[46m',
    'cinza': '\033[47m'
}

print('Olá {}{}{}'.format(back['branco'],nome,back['limpa']))
print('Olá {}{}{}'.format(back['vermelho'],nome,back['limpa']))
print('Olá {}{}{}'.format(back['verde'],nome,back['limpa']))
print('Olá {}{}{}'.format(back['amarelo'],nome,back['limpa']))
print('Olá {}{}{}'.format(back['azul'],nome,back['limpa']))
print('Olá {}{}{}'.format(back['roxo'],nome,back['limpa']))
print('Olá {}{}{}'.format(back['ciano'],nome,back['limpa']))
print('Olá {}{}{}'.format(back['cinza'],nome,back['limpa']))
