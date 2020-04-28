#refaça o exercicio 35 acrescentando o recurso de mostrar que tipo de triangulo será mostrado:]
#equilátero: todos os lados são iguais;
#isósceles: dois lados iguais;
#escaleno: todos os lados diferentes

reta1 = float(input('Informe reta1:'))
reta2 = float(input('Informe reta2:'))
reta3 = float(input('Informe reta3:'))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    if reta1 == reta2 and reta2 == reta3:
      print('Temos um triângulo Equilátero!')
    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
     print('Temos um triângulo Isósceles!')
    else:
      print('Temos um triângulo Escaleno!!')
else:
    print('Não se pode formar triângulo!')
