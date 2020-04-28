frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[::2]) #Não sei o inicio nem o final, é a string inteira

print("""teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste
 teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste
  teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste
   """)
print(frase.count('o'))
print(frase.upper().count('O'))
print(frase.upper())
print(len(frase))
print(frase.lstrip()) # retira o espaço a esquerda. rstrip, retira o espaço a direita.
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print ('teste' in frase)
print(frase.find('Curso'))
print(frase.find('teste'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])



