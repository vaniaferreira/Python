#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#Quantidade de notas;
#A maior nota;
#A menor nota;
#A média da turma;
#A situação opcional;

#adicione também as docstrings da função.

def notas(*n, sit=False):
    r=dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n)/len(n)
    if sit:
        if r['Media'] >=7:
            r['Situação'] = 'Boa'
        elif r['Media'] >= 5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'
    return r

resp = notas(10, 8, 9, 8.5)
print(resp)
