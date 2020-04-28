from Programa_Principal.Interface import *
from Programa_Principal.Arquivo import *

arq = 'cadastro.txt'

if not Arqexiste(arq):
    CriarArquivo(arq)

cabecalho("Sistema de Clientes")
opcao = list()
opcao = ('1 - Listar Clientes', '2 - Cadastrar Clientes', '3 - Alterar Dados', '4 - Excluir Dados', '5 - Sair')

for item in opcao:
    print(item)

while True:
    opcao_escolhida = int(input('Informe a opção desejada: '))
    if opcao_escolhida == 1:
        cabecalho('Listar Clientes')
        ListarClientes(arq)
    elif opcao_escolhida == 2:
        cabecalho('Cadastrar Clientes')
        cliente = str(input('Nome: '))
        idade = int(input('Idade: '))
        CadastrarClientes(arq, cliente, idade)
    elif opcao_escolhida == 3:
        cabecalho('Alterar Dados')
        nome_alterar = str(input('Nome de qual cliente deseja alterar? '))
        nome_alterado = str(input('Alterar para qual nome? '))
        AlterarDados(arq)
    elif opcao_escolhida == 4:
        cabecalho('Excluir Dados')
    elif opcao_escolhida == 5:
        cabecalho('Sair')
        print('Volte Logo!')
        break
    else:
        print('Você digitou a opção errada. Tente novamente!')



