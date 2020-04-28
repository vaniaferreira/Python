from Programa_Principal.Interface import *

def Arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ListarClientes(nome):
    try:
        a = open(nome, 'rt')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    except:
        print('Problemas ao listar clientes')
        return False
    else:
        return True
        a.close()


def CadastrarClientes(nome, cliente ='desconhecido', idade = 0):
    try:
        a = open(nome, 'at')
        a.write(f'{cliente};{idade}\n')
    except:
        print('Erro ao cadastrar clientes!')
        return False
    else:
        print(f'Sucesso ao gravar cliente {cliente} {idade}')
        return True
        a.close()


def AlterarDados(nome, ant, pos):
    try:
        print(ant)
        print(pos)
        a = open(nome, 'rt')
        for linha in a:
            dado = linha.split(';')
            if dado[0] in ant:
                print('sim')
                a = open(nome, 'wt')
                dado[0] = pos
                a.write(f'{dado[0].replace(ant,pos)}')
                #b.write(f'{dado.replace(ant,pos)};\n')
                #b.write(f'{pos};\n')
                #b.readlines()

               #a.write(dado[0].replace(f'{ant}, {pos}'))

    except:
        print('Erro ao Alterar Dados')



