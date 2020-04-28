#Tratamento de Erros e Exceções
try:
    a = int(input('Numerador:'))
    b = int(input('Denominador:'))
    r = a / b
except (ValueError, TypeError):
    print('Verifique os dados digitados!')
except (ZeroDivisionError):
    print('Não é possível dividir um número por 0!')
except (KeyboardInterrupt):
    print('O usuário preferiu não informar o valor!')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte Sempre!')


