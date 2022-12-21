#tupla = tuple()
#tupla = () #Esse também serve para criar uma Tupla!
#print(type(tupla))
tupla = ('Um',)
print(type(tupla))
#print(tupla[0])
#tupla[0] = 'novo'# Retornará erro pois não é possível alterar itens de uma Tupla!
cores = ('verde', 'amarelo', 'azul', 'branco')
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index('amarelo'))
print(cores.count('azul')) #Retorna quantos elementos especificados existem na tupla.
print(len(cores))