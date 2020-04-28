#Função

def soma(a,b):
    s = a + b
    print(s)


def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


def contador(*num):
    tam = len(num)
    print(f'Recebi {num} números com o tamanho {tam}')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


def somas(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Soma dos valores {valores} temos {s}')


#Programa Principal

titulo(f'{"Curso em vídeo":^30}')
titulo(f'{"Aprenda Python":^30}')
titulo(f'{"Professor Gustavo Guanabara":^30}')

soma(4,5)
soma(8,9)
soma(2,1)

contador(2, 5, 8)
contador(2)
contador(31, 4, 5)

valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)

somas(5, 2)
somas(3, 1)
