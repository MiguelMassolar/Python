nome = 'Ana Paula'
#print(nome[0])
#print(nome[6]) #Ao acessar o conteúdo da string, o espaço conta!
#print(nome[-3]) #Dá para fazer de trás para frente também!
#print(nome[4:]) #Acessar um range (conjunto de elemento).
#print(nome[-5:])
#print(nome[:3])
#print(nome[:4])
#print(nome[2:5])
print(nome[::-1])

numeros = '1234567890'
print(numeros)
print(numeros[::2]) #Vai pegar os números de 2 em 2!
print(numeros[1::2]) #O mesmo que o anterior, porém começará a partir do primeiro!
print(numeros[::-2])